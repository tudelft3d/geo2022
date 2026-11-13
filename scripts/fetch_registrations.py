#!/usr/bin/env python3
"""Fetch the Kick-off and Green-light assessment registrations, and the
thesis-topic picks, from the Microsoft Forms used for GEO2022.

Microsoft publishes no Graph endpoint for Forms responses, so this borrows the
endpoints the Forms web app itself uses. They are undocumented but stable, and
they authenticate with the browser session cookie rather than a bearer token:

  GET /formapi/api/{tenant}/users/{owner}/light/forms      form list (by title)
  GET /formapi/api/{tenant}/users/{owner}/forms('{id}')/questions
  GET /formapi/api/{tenant}/users/{owner}/forms('{id}')/responses

tenant and owner are not configured here: the ResponsePage link of each form is
base64(tenant GUID + owner GUID + short form id), so the script reads the links
straight out of the pages that publish them (registration/index.md for the two
assessments, potentialtopics/index.md for the topic form, which is also linked
on rules/index.md and checked to be the same form). Replace a form on the site
and the script follows, without changes.

Authentication is a browser session against forms.cloud.microsoft (NetID +
MFA), kept in a persistent Chromium profile. The first run therefore opens a
window; later runs are headless and reuse the cookies until they expire.

Outputs (gitignored: the responses carry student names, student numbers and
e-mail addresses and must not end up on the public site):

  registrations/assessments.csv        one row per response, both forms
  registrations/topics.csv             one row per topic-pick response
  registrations/<form>_responses.json  raw payload per form
  registrations/_debug/                captures and screenshots on failure

Both outputs are checked against the rest of the site data:

  - assessment registrations that have no open MyCase case (no entry in
    _data/ongoing_theses.yml), no date/room yet, or a student who submitted
    more than once;
  - topic picks for students who are not in _data/ongoing_theses.yml, and
    title / 1st supervisor disagreements.

MyCase has priority over the forms: a title or first supervisor registered there
(via mycase/mycase_index.csv) is reported as authoritative, so the form cannot
change it. The form only fills in what MyCase does not have yet -- typically a
case still in Preparation -- and --fill writes exactly those values into
_data/ongoing_theses.yml. Nothing is ever overwritten; a disagreement is
reported and left for a human.

Requires: playwright (playwright install chromium), pyyaml.

Usage:
  python3 scripts/fetch_registrations.py            # headless, reuses session
  python3 scripts/fetch_registrations.py --login     # force a fresh login
  python3 scripts/fetch_registrations.py --fill       # apply missing topics
"""

import argparse
import base64
import csv
import json
import re
import sys
import time
import uuid
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import yaml
from playwright.sync_api import sync_playwright

ORIGIN = "https://forms.cloud.microsoft"
REPO_ROOT = Path(__file__).resolve().parent.parent
PROFILE_DIR = REPO_ROOT / "registrations_profile"
OUT_DIR = REPO_ROOT / "registrations"
DEBUG_DIR = OUT_DIR / "_debug"
ASSESSMENTS_CSV = OUT_DIR / "assessments.csv"
TOPICS_CSV = OUT_DIR / "topics.csv"
ONGOING_YML = REPO_ROOT / "_data" / "ongoing_theses.yml"
MYCASE_INDEX = REPO_ROOT / "mycase" / "mycase_index.csv"

# Where each form's ResponsePage link is published, and which of that page's
# links it is (the registration page has one per assessment). Pages carry the
# link either as a markdown link or as an <a href> button, hence the plain URL
# scan below.
FORM_PAGES = {
    "kickoff": ("registration/index.md", 0),
    "greenlight": ("registration/index.md", 1),
    "topics": ("potentialtopics/index.md", 0),
}
# The topic form is published twice (also as a button on the rules page);
# both copies must point at the same form.
DUPLICATE_FORM_PAGES = {"topics": ["rules/index.md"]}
LINK_RE = re.compile(
    r"https://forms\.cloud\.microsoft/Pages/ResponsePage\.aspx\?id=[\w.-]+")
FIELDS = ["form", "student", "date", "time", "room",
          "submitted", "responder", "response_id"]
TOPIC_FIELDS = ["student", "topic", "supervisor", "email",
                "submitted", "response_id"]


# --------------------------------------------------------------------------
# Configuration: the published links
# --------------------------------------------------------------------------

def decode_link(url: str) -> dict:
    """ResponsePage.aspx?id=<b64> holds tenant GUID + owner GUID + form id."""
    blob = parse_qs(urlparse(url).query)["id"][0]
    raw = base64.urlsafe_b64decode(blob + "=" * (-len(blob) % 4))
    return {
        "blob": blob,
        "tenant": str(uuid.UUID(bytes_le=raw[:16])),
        "owner": str(uuid.UUID(bytes_le=raw[16:32])),
        "short_id": raw[32:].decode("ascii", "replace"),
    }


def page_links(page: str) -> list:
    """The Forms ResponsePage URLs on one page of the site, in order."""
    path = REPO_ROOT / page
    try:
        text = path.read_text()
    except OSError as e:
        raise SystemExit(f"Cannot read {path}: {e}")
    return LINK_RE.findall(text)


def form_links() -> dict:
    """Decode the form links published on the site, keyed by output name."""
    out = {}
    for key, (page, index) in FORM_PAGES.items():
        urls = page_links(page)
        if len(urls) <= index:
            raise SystemExit(
                f"{page} has {len(urls)} form link(s); expected at least "
                f"{index + 1} for the {key} form. Has the page changed?")
        out[key] = decode_link(urls[index])

    for key, pages in DUPLICATE_FORM_PAGES.items():
        for page in pages:
            urls = page_links(page)
            if out[key]["blob"] not in [decode_link(u)["blob"] for u in urls]:
                raise SystemExit(
                    f"{page} links a different {key} form than "
                    f"{FORM_PAGES[key][0]}; students would land on the "
                    f"wrong form. Fix the two links (the others in "
                    f"{page}: {[u[-20:] for u in urls]}).")

    tenants = {info["tenant"] for info in out.values()}
    owners = {info["owner"] for info in out.values()}
    if len(tenants) > 1 or len(owners) > 1:
        raise SystemExit("The form links do not share a tenant/owner; "
                         "unexpected, check them by hand.")
    return out


# --------------------------------------------------------------------------
# Browser session
# --------------------------------------------------------------------------

class FormsSession:
    """Chromium context holding the Forms cookies, plus a JSON getter.

    Playwright is started explicitly rather than through a `with` block,
    because the context has to outlive the function that creates it.
    """

    def __init__(self, headless: bool):
        self._pw = sync_playwright().start()
        self.context = self._pw.chromium.launch_persistent_context(
            str(PROFILE_DIR), headless=headless,
            viewport={"width": 1400, "height": 950})
        self.page = (self.context.pages[0] if self.context.pages
                     else self.context.new_page())
        self.page.goto(ORIGIN, wait_until="domcontentloaded")

    def close(self):
        try:
            self.context.close()
        except Exception:
            pass
        try:
            self._pw.stop()
        except Exception:
            pass

    def get(self, path: str):
        """GET a formapi path; None when the session is not authenticated."""
        body = self.page.evaluate("""async (u) => {
            const r = await fetch(u, {headers: {"Accept": "application/json"},
                                      credentials: "include"});
            const t = await r.text();
            if (!r.headers.get("content-type")?.includes("json")) return null;
            return t;
        }""", path)
        if body is None:
            return None
        try:
            return json.loads(body)
        except ValueError:
            return None

    def authenticated(self) -> bool:
        return self.get("/formapi/api/userInfo") is not None


def open_session(force_login: bool, timeout_s: int = 600) -> FormsSession:
    """Headless if the saved cookies still work, otherwise log in for real."""
    if not force_login:
        session = FormsSession(headless=True)
        if session.authenticated():
            print("Reusing the saved Forms session.", flush=True)
            return session
        session.close()

    print("""\
==============================================================================
  A Chromium window is opening to log in to Microsoft Forms.
    1. Log in with your NetID (+ MFA).
    2. Once you are on the Forms start page, close the window.
  You do not need to open the forms: the script fetches the responses.
  The session is then reused headlessly until the cookies expire.
==============================================================================
""", flush=True)
    session = FormsSession(headless=False)
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        if session.authenticated():
            print("Logged in.", flush=True)
            return session
        try:
            session.page.wait_for_timeout(3000)
        except Exception:
            # The user closed the window; the cookies may still be good.
            break
    if session.authenticated():
        print("Logged in.", flush=True)
        return session
    session.close()
    raise SystemExit("Not logged in; nothing fetched.")


# --------------------------------------------------------------------------
# Fetching
# --------------------------------------------------------------------------

def api_base(info: dict) -> str:
    return (f"/formapi/api/{info['tenant']}/users/{info['owner']}")


def list_forms(session: FormsSession, links: dict) -> dict:
    """The forms to fetch, keyed as in the outputs.

    Every form is matched by the id decoded from its published link, which is
    the same blob the API returns in the form list.
    """
    info = next(iter(links.values()))
    data = session.get(f"{api_base(info)}/light/forms") or {}
    forms = data.get("value") or []
    out = {}
    for key, link in links.items():
        match = next((f for f in forms if f.get("id") == link["blob"]), None)
        if match is None:
            raise SystemExit(
                f"The {key} form ({link['short_id']}) is not in the owner's "
                f"form list: has it been deleted or replaced? Forms on offer: "
                f"{[f.get('title') for f in forms]}")
        out[key] = {"id": match["id"], "title": match.get("title", "")}
    return out


def questions(session: FormsSession, info: dict, form_id: str) -> dict:
    """{questionId: title} for one form."""
    data = session.get(f"{api_base(info)}/forms('{form_id}')/questions") or {}
    return {q["id"]: q.get("title", "") for q in data.get("value") or []}


def responses(session: FormsSession, info: dict, form_id: str) -> list:
    data = session.get(f"{api_base(info)}/forms('{form_id}')/responses") or {}
    return data.get("value") or []


def parse_answers(resp: dict) -> list:
    """The answers arrive as a JSON string, not as a nested array."""
    answers = resp.get("answers")
    if isinstance(answers, str):
        try:
            answers = json.loads(answers)
        except ValueError:
            answers = []
    return answers or []


def answer_values(resp: dict, titles: dict) -> dict:
    """{lowercased question title: value} for one response."""
    out = {}
    for answer in parse_answers(resp):
        title = titles.get(answer.get("questionId"), "").lower().strip()
        value = answer.get("answer1")
        if title:
            out[title] = "" if value is None else str(value).strip()
    return out


def flatten(key: str, rows: list, titles: dict) -> list:
    """One dict per assessment response, questions mapped onto columns."""
    out = []
    for resp in rows:
        row = {
            "form": key,
            "response_id": resp.get("id", ""),
            "submitted": (resp.get("submitDate") or "")[:16].replace("T", " "),
            "responder": resp.get("responder", ""),
            "student": "", "date": "", "time": "", "room": "",
        }
        for title, value in answer_values(resp, titles).items():
            if title.startswith("student name"):
                row["student"] = value
            elif "date" in title:
                row["date"] = value
            elif "time" in title:
                row["time"] = value
            elif "room" in title:
                row["room"] = value
            else:
                row[title] = value
        out.append(row)
    return out


def flatten_topic(rows: list, titles: dict) -> list:
    """One dict per topic-pick response; the student is the responder."""
    out = []
    for resp in rows:
        row = {
            "response_id": resp.get("id", ""),
            "submitted": (resp.get("submitDate") or "")[:16].replace("T", " "),
            "student": resp.get("responderName", ""),
            "email": resp.get("responder", ""),
            "topic": "", "supervisor": "",
        }
        for title, value in answer_values(resp, titles).items():
            if "supervisor" in title:
                row["supervisor"] = value
            elif "topic" in title or "title" in title:
                row["topic"] = value
        out.append(row)
    return out


# --------------------------------------------------------------------------
# Cross-check against the open MyCase cases
# --------------------------------------------------------------------------

def ongoing_entries() -> list:
    """The entries of _data/ongoing_theses.yml (empty if unreadable)."""
    try:
        return yaml.safe_load(ONGOING_YML.read_text()) or []
    except OSError:
        return []


def ongoing_names() -> set:
    """Normalised full names of the students on the Current Theses page."""
    names = set()
    for entry in ongoing_entries():
        given = str(entry.get("name", "")).strip()
        surname = str(entry.get("surname", "")).strip()
        if given or surname:
            names.add(normalise(f"{given} {surname}"))
    return names


def normalise(name: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z ]", "", name.lower())).strip()


def same_text(a: str, b: str) -> bool:
    """Compare titles/supervisor names ignoring case and spacing."""
    return re.sub(r"\s+", " ", a).strip().casefold() == \
        re.sub(r"\s+", " ", b).strip().casefold()


def report_assessments(rows: list) -> None:
    """Print the registrations and flag anything that needs a manual look."""
    current = ongoing_names()
    print("\n=== assessment registrations ===", flush=True)
    for row in sorted(rows, key=lambda r: (r["date"], r["time"])):
        print(f"  {row['form']:10s} {row['date']} {row['time']:14s} "
              f"{row['room']:22s} {row['student']}", flush=True)

    problems = []
    for row in rows:
        if not row["student"]:
            problems.append(f"response {row['response_id']} ({row['form']}) "
                            f"has no student name")
        if not row["date"]:
            problems.append(f"{row['student'] or row['response_id']} "
                            f"({row['form']}) has no date")
        if not row["room"] or row["room"].upper() == "TBA":
            problems.append(f"{row['student'] or row['response_id']} "
                            f"({row['form']}) has no room yet")
        if current and row["student"] and normalise(row["student"]) not in current:
            problems.append(f"{row['student']} ({row['form']}) is not in "
                            f"_data/ongoing_theses.yml -- no open MyCase case?")

    seen = {}
    for row in rows:
        key = (row["form"], normalise(row["student"]))
        if not key[1]:
            continue
        seen.setdefault(key, []).append(row["response_id"])
    for (form, student), ids in seen.items():
        if len(ids) > 1:
            problems.append(f"{student} submitted the {form} form "
                            f"{len(ids)} times (responses {ids}); "
                            f"the latest edit is likely the valid one")

    print_problems(problems)


def mycase_topics() -> dict:
    """{normalised name: {'title', 'supervisor'}} from MyCase's case index.

    Optional: mycase/ only exists after scripts/fetch_mycase.py has run. Open
    cases win over closed ones for the same student.
    """
    try:
        with MYCASE_INDEX.open(encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    except OSError:
        return {}
    out = {}
    for row in rows:
        key = normalise(row.get("student_name", ""))
        if not key:
            continue
        if key in out and out[key]["_status"] == "open":
            continue
        out[key] = {
            "title": (row.get("thesis_title") or "").strip(),
            "supervisor": (row.get("supervisor_1") or "").strip(),
            "_status": row.get("status", ""),
        }
    return out


def report_topics(rows: list, fill: bool = False) -> None:
    """Print the topic picks and compare them with the rest of the site data.

    MyCase has priority: a title or first supervisor registered there is
    authoritative, and the form only fills in what is still missing (usually a
    case that is in Preparation, where MyCase has neither yet). Nothing is ever
    overwritten, and a disagreement is reported rather than resolved.
    """
    entries = ongoing_entries()
    by_name = {normalise(f"{e.get('name', '')} {e.get('surname', '')}"): e
               for e in entries}
    mycase = mycase_topics()
    print("\n=== thesis topic picks ===", flush=True)
    for row in rows:
        print(f"  {row['student'] or row['email']}", flush=True)
        print(f"    {row['topic']}", flush=True)
        print(f"    1st supervisor: {row['supervisor']}", flush=True)
    if not mycase:
        print("  (mycase/mycase_index.csv missing: run scripts/fetch_mycase.py "
              "to let MyCase take priority)", flush=True)

    problems, fills = [], []
    for row in rows:
        key = normalise(row["student"])
        entry = by_name.get(key)
        if entry is None:
            problems.append(f"{row['student'] or row['email']} filled in the "
                            f"topic form but is not in _data/ongoing_theses.yml")
            continue
        yaml_title = str(entry.get("title") or "").strip()
        yaml_supervisors = str(entry.get("supervisors") or "").strip()
        known = mycase.get(key) or {}
        mc_title = known.get("title", "")
        mc_supervisor = known.get("supervisor", "")

        # The value that wins, and where it came from.
        title, title_src = ((mc_title, "MyCase") if mc_title
                            else (yaml_title, "_data/ongoing_theses.yml"))
        supervisor, supervisor_src = (
            (mc_supervisor, "MyCase") if mc_supervisor
            else (yaml_supervisors.split(";")[0].strip(),
                  "_data/ongoing_theses.yml"))

        if not row["topic"]:
            problems.append(f"{row['student']} submitted no topic title")
        elif not title:
            fills.append((entry, "title", row["topic"], row))
        elif not same_text(title, row["topic"]):
            problems.append(
                f"{row['student']}: the form says {row['topic']!r} but "
                f"{title_src} has {title!r} -- {title_src} wins, so either "
                f"the form or the case needs correcting")

        if not row["supervisor"]:
            problems.append(f"{row['student']} submitted no 1st supervisor")
        elif not supervisor:
            fills.append((entry, "supervisors", row["supervisor"], row))
        elif not same_text(supervisor, row["supervisor"]):
            problems.append(
                f"{row['student']}: the form says 1st supervisor "
                f"{row['supervisor']!r} but {supervisor_src} has "
                f"{supervisor!r} -- {supervisor_src} wins")

        # MyCase has moved on from the published page: sync it.
        if mc_title and yaml_title and not same_text(mc_title, yaml_title):
            problems.append(f"{row['student']}: MyCase title {mc_title!r} is "
                            f"not in _data/ongoing_theses.yml ({yaml_title!r}) "
                            f"-- run scripts/update_theses.py")

        if not row["email"].lower().endswith(("@tudelft.nl", "@student.tudelft.nl")):
            problems.append(f"{row['student']} replied from {row['email']!r}; "
                            f"not a TU Delft address, check that it is the "
                            f"right student")

    for entry, field, value, row in fills:
        print(f"  + {'filled' if fill else 'can fill'} "
              f"{row['student']}.{field} = {value!r}", flush=True)
    if fills and fill:
        for entry, field, value, _ in fills:
            entry[field] = value
        import update_theses
        update_theses.write_yaml(entries)
        print(f"Updated {rel(ONGOING_YML)} "
              f"({len(fills)} fields); review with git diff.", flush=True)
    elif fills:
        print("  (re-run with --fill to write those into "
              "_data/ongoing_theses.yml)", flush=True)

    print_problems(problems)


def print_problems(problems: list) -> None:
    if problems:
        print("\n=== needs a look ===", flush=True)
        for problem in problems:
            print(f"  ! {problem}", flush=True)
    else:
        print("  nothing to flag.", flush=True)


def rel(path: Path) -> str:
    """Path relative to the repo when possible (for messages)."""
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def write_csv(path: Path, columns: list, rows: list) -> None:
    columns = columns + sorted({c for r in rows for c in r} - set(columns))
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {rel(path)} ({len(rows)} rows)", flush=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--login", action="store_true",
                    help="force a fresh browser login")
    ap.add_argument("--timeout", type=int, default=600,
                    help="seconds to wait for the login (default 600)")
    ap.add_argument("--fill", action="store_true",
                    help="write topics/1st supervisors that MyCase does not "
                         "have yet into _data/ongoing_theses.yml")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    links = form_links()
    info = next(iter(links.values()))  # both forms share tenant/owner
    print(f"tenant {info['tenant']}, owner {info['owner']}", flush=True)

    assessments, topics = [], []
    session = open_session(force_login=args.login, timeout_s=args.timeout)
    try:
        for key, form in list_forms(session, links).items():
            titles = questions(session, info, form["id"])
            raw = responses(session, info, form["id"])
            (OUT_DIR / f"{key}_responses.json").write_text(
                json.dumps(raw, indent=1, ensure_ascii=False))
            if key == "topics":
                flat_topics = flatten_topic(raw, titles)
                print(f"topics: {len(flat_topics)} responses "
                      f"({form['title']})", flush=True)
                topics.extend(flat_topics)
            else:
                flat = flatten(key, raw, titles)
                print(f"{key}: {len(flat)} responses ({form['title']})",
                      flush=True)
                assessments.extend(flat)
    finally:
        session.close()

    write_csv(ASSESSMENTS_CSV, FIELDS, assessments)
    write_csv(TOPICS_CSV, TOPIC_FIELDS, topics)

    report_assessments(assessments)
    report_topics(topics, fill=args.fill)
    return 0


if __name__ == "__main__":
    sys.exit(main())
