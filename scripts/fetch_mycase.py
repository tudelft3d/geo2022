#!/usr/bin/env python3
"""Fetch MSc graduation case metadata from MyCase (mycase.tudelft.nl) for
maintaining the thesis lists on this site.

Pulls every Geomatics graduation case (open and closed) and extracts the
five useful tabs:

  Summary       course (code/year/EC), student info, entry/green-light
                requirement checks, and the whole Project content nested
  Stakeholders  supervisory team: 1st (responsible) supervisor, 2nd
                supervisors, graduation delegate, with departments
  Project       thesis title, grade, cum laude, presentation date/time/
                location, repository link, review comments and decisions
  Agreements    human participation, confidentiality, external graduation
  Planning      start/kick-off/midterm/greenlight/finalisation dates

Outputs (gitignored — contains grades, student numbers and supervisor
comments and must never end up on the public site):
  mycase/mycase_index.csv     one row per case with the flattened useful
                              fields, including a suggested website cohort
                              (e.g. 2025sep) derived from the start date
  mycase/cases/*.json         the raw tab content per case; private contact
                              details (home address etc.) are stripped

Login goes through SURFconext -> TU Delft SSO (NetID + MFA) in a browser
window that opens automatically; a persistent profile and rolling refresh
tokens (mycase_session.json) skip the login on consecutive runs within
~30 minutes. Everything else uses MyCase's REST API directly:

  POST /api/v1/case/msc-gra/search                          case list
  GET  /api/v1/tudelft/document/msc-gra/{uuid}/tab/{tab}    tab content

Requires: requests, playwright (playwright install chromium).

Usage:
  python3 scripts/fetch_mycase.py
  python3 scripts/fetch_mycase.py --limit 3      # test run
"""

import argparse
import csv
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import requests
from playwright.sync_api import sync_playwright

ORIGIN = "https://mycase.tudelft.nl"
TOKEN_URL = "https://auth.tudelft.nl/auth/realms/mycase/protocol/openid-connect/token"
CLIENT_ID = "mycase-console"
REPO_ROOT = Path(__file__).resolve().parent.parent
PROFILE_DIR = REPO_ROOT / "mycase_profile"
SESSION_FILE = REPO_ROOT / "mycase_session.json"
OUT_DIR = REPO_ROOT / "mycase"
CASES_DIR = OUT_DIR / "cases"
INDEX_CSV = OUT_DIR / "mycase_index.csv"

TABS = ["summary", "stakeholders", "project", "agreements", "planning"]

# Map the search API's column keys to CSV columns via the app's own
# list-column titles (see /api/v1/case/msc-gra/list-column).
TITLE_TO_COLUMN = {
    "Student Name": "student_name", "Student Number": "student_number",
    "Faculty": "faculty", "Programme": "programme", "Track": "track",
    "Course Code": "course_code", "Phase": "phase",
    "Next Milestone": "next_milestone",
    "Responsible Supervisor": "responsible_supervisor", "Chair": "chair",
    "Created on": "created_on", "Last modified": "last_modified",
    "Status": "status", "ID": "case_id",
}
LIST_COLUMNS = list(TITLE_TO_COLUMN.values())

INDEX_COLUMNS = [
    "student_name", "student_number", "student_email", "status", "phase",
    "course_code", "course_year", "ec_points",
    "thesis_title", "grade", "cum_laude", "repository_link",
    "presentation_date", "presentation_time", "presentation_location",
    "supervisor_1", "supervisor_1_username", "supervisor_1_department",
    "supervisor_2", "supervisor_2_username", "supervisor_2_department",
    "grad_delegate",
    "start_date", "kick_off_date", "midterm_date", "greenlight_date",
    "finalisation_date",
    "human_participation", "confidentiality", "external_graduation",
    "greenlight_requirements", "entry_requirements",
    "responsible_supervisor", "chair",
    "created_on", "modified_on", "case_uuid",
    "academic_year", "suggested_cohort",
]


def normalise_name(name: str) -> str:
    name = re.sub(r"\s+", " ", name.strip())
    # The list sometimes repeats the name ("Citra Citra Andinasari");
    # collapse an immediate doubling of the first part of the name.
    parts = name.split(" ")
    half = len(parts) // 2
    if len(parts) >= 3 and parts[:half] == parts[half:2 * half]:
        name = " ".join(parts[half:])
    return name


def parse_date(s: str):
    """Accept ISO datetimes from the API and plain dates."""
    s = (s or "").strip()
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00")).replace(tzinfo=None)
    except ValueError:
        pass
    for fmt in ("%d-%m-%Y %H:%M", "%d-%m-%Y"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    return None


def academic_year(dt) -> str:
    """TU Delft academic year runs 1 Sep - 31 Aug."""
    if dt is None:
        return ""
    if dt.month >= 9:
        return f"{dt.year}/{dt.year + 1}"
    return f"{dt.year - 1}/{dt.year}"


def suggested_cohort(dt, fallback_dt=None) -> str:
    """The website's per-quarter thesis lists (e.g. 2025sep). The case's
    start date is the best proxy for the cohort; Feb is ambiguous in
    MyCase (Josephine 26/2 -> 2026feb, Juan 16/2 -> 2026april), so entries
    created in Dec-Feb still deserve a manual check."""
    dt = dt or fallback_dt
    if dt is None:
        return ""
    y, m = dt.year, dt.month
    if m >= 9:
        return f"{y}sep"
    if m == 1:
        return f"{y - 1}sep"
    if m in (2, 3):
        return f"{y}feb"
    return f"{y}april"


class Tokens:
    """OIDC tokens with rolling refresh; persisted to mycase_session.json."""

    MAX_AGE_S = 240          # refresh before the 5-minute access token expires
    MAX_SESSION_S = 25 * 60  # refresh tokens expire after 30 minutes

    def __init__(self):
        self.data = None
        self.obtained_at = 0.0

    def update(self, token_response: dict):
        if token_response and token_response.get("access_token"):
            self.data = token_response
            self.obtained_at = time.time()
            self.save()

    def valid(self) -> bool:
        return (self.data is not None
                and time.time() - self.obtained_at < self.MAX_AGE_S)

    def usable(self) -> bool:
        return (self.data is not None
                and time.time() - self.obtained_at < self.MAX_SESSION_S)

    def save(self):
        if self.data:
            SESSION_FILE.write_text(json.dumps({
                "tokens": self.data, "obtained_at": self.obtained_at}))
            SESSION_FILE.chmod(0o600)

    @classmethod
    def try_load(cls) -> "Tokens":
        t = cls()
        try:
            raw = json.loads(SESSION_FILE.read_text())
            if time.time() - raw.get("obtained_at", 1e12) < t.MAX_SESSION_S:
                t.data = raw["tokens"]
                t.obtained_at = raw["obtained_at"]
        except Exception:
            pass
        return t

    def refresh(self) -> bool:
        """Refresh via the public client's refresh-token grant. The new
        tokens (including the next single-use refresh token) are saved
        immediately, so consecutive refreshes must never run in parallel."""
        rt = (self.data or {}).get("refresh_token")
        if not rt:
            return False
        try:
            r = requests.post(TOKEN_URL, data={
                "grant_type": "refresh_token",
                "client_id": CLIENT_ID,
                "refresh_token": rt,
            }, timeout=30)
            body = r.json()
            if r.status_code == 200 and body.get("access_token"):
                self.update(body)
                return True
        except Exception:
            pass
        return False

    def authorisation(self) -> str:
        return f"Bearer {self.data['access_token']}" if self.data else ""


def login_via_browser(tokens: Tokens, timeout_s: int = 600) -> None:
    """Open the MyCase console in a browser and let the user log in. The
    SPA's OIDC code exchange is captured by a response listener; the
    browser closes as soon as we hold a valid token."""
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            str(PROFILE_DIR), headless=False,
            viewport={"width": 1280, "height": 900})
        page = context.pages[0] if context.pages else context.new_page()
        page.on("response", lambda resp: _capture_token(resp, tokens))
        page.goto(ORIGIN, wait_until="domcontentloaded")
        print("\n>>> Please complete the login (NetID + MFA) in the opened "
              "browser window if prompted. Waiting up to 10 minutes...\n",
              flush=True)
        deadline = time.time() + timeout_s
        while time.time() < deadline:
            if tokens.valid():
                context.close()
                return
            page.wait_for_timeout(1000)
        context.close()
        raise RuntimeError("Login was not completed within 10 minutes.")


def _capture_token(resp, tokens: Tokens):
    if TOKEN_URL in resp.url:
        try:
            tokens.update(resp.json())
        except Exception:
            pass


class MyCase:
    """Requests-based API client with automatic token refresh."""

    def __init__(self, tokens: Tokens):
        self.tokens = tokens
        self.session = requests.Session()

    def _ensure_tokens(self):
        if not self.tokens.valid() and not self.tokens.refresh():
            raise RuntimeError(
                "Session expired (refresh token no longer valid). "
                "Re-run the script to log in again.")

    def _headers(self) -> dict:
        return {"Accept": "application/json",
                "Authorization": self.tokens.authorisation()}

    def _get(self, url: str):
        self._ensure_tokens()
        r = self.session.get(url, headers=self._headers(), timeout=60)
        if r.status_code != 200:
            raise RuntimeError(f"GET {url} -> {r.status_code}: {r.text[:200]}")
        return r.json() if "application/json" in r.headers.get(
            "content-type", "") else r

    def _post_json(self, url: str, body: dict):
        self._ensure_tokens()
        headers = self._headers()
        headers["Content-Type"] = "application/json"
        r = self.session.post(url, data=json.dumps(body), headers=headers,
                              timeout=60)
        if r.status_code != 200:
            raise RuntimeError(f"POST {url} -> {r.status_code}: {r.text[:200]}")
        return r.json()

    def search_cases(self, status: str) -> list:
        """All msc-gra cases with the given status ('open' or 'closed')."""
        body = {
            "documentDefinitionName": "msc-gra",
            "searchOperator": "AND",
            "assigneeFilter": "ALL",
            "statusFilter": [status],
            "caseTagsFilter": [],
        }
        key_map = {}
        for col in self._get(f"{ORIGIN}/api/v1/case/msc-gra/list-column"):
            csv_col = TITLE_TO_COLUMN.get(col.get("title", ""))
            if csv_col:
                key_map[col["key"]] = csv_col
        cases, page_no = [], 0
        while True:
            url = (f"{ORIGIN}/api/v1/case/msc-gra/search"
                   f"?definitionName=msc-gra&page={page_no}&size=100&sort=createdOn,DESC")
            data = self._post_json(url, body)
            for row in data.get("content", []):
                case = {col: "" for col in LIST_COLUMNS}
                for item in row.get("items", []):
                    col = key_map.get(item.get("key"))
                    if col and item.get("value") is not None:
                        case[col] = str(item["value"])
                case["case_uuid"] = row.get("id", "")
                case["status"] = status
                cases.append(case)
            print(f"  {status} search page {page_no}: "
                  f"{len(data.get('content', []))} rows "
                  f"({len(cases)}/{data.get('totalElements', '?')})", flush=True)
            if data.get("last", True) or not data.get("content"):
                break
            page_no += 1
        return cases

    def case_tab(self, case_uuid: str, tab: str):
        data = self._get(
            f"{ORIGIN}/api/v1/tudelft/document/msc-gra/{case_uuid}/tab/{tab}")
        return data.get("content")


def first(content: dict, *path):
    """Follow a path of keys, returning '' when anything is missing."""
    cur = content
    for key in path:
        if not isinstance(cur, dict):
            return ""
        cur = cur.get(key)
    return "" if cur is None else str(cur)


def supervisor_fields(content: dict) -> dict:
    team = (content.get("team") or {})
    responsible = team.get("gradResponsibleSupervisor") or {}
    seconds = [s for s in (team.get("gradSupervisor") or [])
               if s.get("display_name") != responsible.get("display_name")]

    def names(people):
        return "; ".join(p.get("display_name", "") for p in people if p.get("display_name"))

    def usernames(people):
        return "; ".join(p.get("username", "") for p in people if p.get("username"))

    def departments(people):
        return "; ".join(
            (p.get("primary_department") or {}).get("code", "") or
            p.get("combined_code", "")
            for p in people if p.get("display_name"))

    delegate = team.get("gradDelegate") or {}
    return {
        "supervisor_1": responsible.get("display_name", ""),
        "supervisor_1_username": responsible.get("username", ""),
        "supervisor_1_department": (responsible.get("primary_department") or {}).get("code", ""),
        "supervisor_2": names(seconds),
        "supervisor_2_username": usernames(seconds),
        "supervisor_2_department": departments(seconds),
        "grad_delegate": delegate.get("display_name", ""),
    }


def flatten(case: dict, tabs: dict) -> dict:
    summary = tabs.get("summary") or {}
    stakeholders = tabs.get("stakeholders") or {}
    project = tabs.get("project") or {}
    agreements = tabs.get("agreements") or {}
    planning = tabs.get("planning") or {}

    course = (summary.get("courseDetails") or {}).get("course") or {}
    student = summary.get("studentInfo") or {}
    pres = project.get("presentationDetails") or {}
    plan = planning.get("currentPlanning") or {}

    start = parse_date(plan.get("startDate", ""))
    row = {
        "student_name": normalise_name(case.get("student_name", "")),
        "student_number": student.get("student_number", case.get("student_number", "")),
        "student_email": student.get("email", ""),
        "status": case.get("status", ""),
        "phase": case.get("phase", ""),
        "course_code": course.get("code", case.get("course_code", "")),
        "course_year": course.get("year", ""),
        "ec_points": course.get("ecPoints", ""),
        "thesis_title": project.get("title", ""),
        "grade": project.get("grade", ""),
        "cum_laude": project.get("cumLaude", ""),
        "repository_link": project.get("repositoryLink", ""),
        "presentation_date": pres.get("date", ""),
        "presentation_time": pres.get("time", ""),
        "presentation_location": pres.get("location", ""),
        "start_date": plan.get("startDate", ""),
        "kick_off_date": plan.get("kick-off", ""),
        "midterm_date": plan.get("midterm", ""),
        "greenlight_date": plan.get("greenlight", ""),
        "finalisation_date": plan.get("finalisation", ""),
        "human_participation": ((agreements.get("humanParticipation") or {})
                                .get("hasHumanParticipation", "")),
        "confidentiality": ((agreements.get("confidentiality") or {})
                            .get("hasConfidentiality", "")),
        "external_graduation": ((agreements.get("externalGraduation") or {})
                                .get("hasExternalGraduationAgreement", "")),
        "greenlight_requirements": (summary.get("greenLightRequirementsCheck")
                                    or {}).get("status", ""),
        "entry_requirements": (summary.get("requirementsCheck") or {}).get("status", ""),
        "responsible_supervisor": case.get("responsible_supervisor", ""),
        "chair": case.get("chair", ""),
        "created_on": case.get("created_on", ""),
        "modified_on": case.get("last_modified", ""),
        "case_uuid": case.get("case_uuid", ""),
    }
    row.update(supervisor_fields(stakeholders))

    row["academic_year"] = academic_year(start or parse_date(row["created_on"]))
    row["suggested_cohort"] = suggested_cohort(start, parse_date(row["created_on"]))
    return row


def strip_private(content):
    """Remove the student's private contact details from a summary tab."""
    if isinstance(content, dict):
        content.pop("contactDetails", None)
    return content


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--limit", type=int, default=None,
                    help="only process the first N cases per status (testing)")
    args = ap.parse_args()

    tokens = Tokens.try_load()
    if tokens.valid():
        print("Reusing session from mycase_session.json.", flush=True)
    elif tokens.usable() and tokens.refresh():
        print("Session refreshed from saved refresh token.", flush=True)
    else:
        print("Opening MyCase login...", flush=True)
        login_via_browser(tokens)

    mc = MyCase(tokens)
    cases = mc.search_cases("closed") + mc.search_cases("open")
    if args.limit:
        cases = cases[:args.limit]
    print(f"Collected {len(cases)} cases.", flush=True)

    CASES_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    for idx, case in enumerate(cases, 1):
        name = normalise_name(case.get("student_name", "?"))
        print(f"[{idx}/{len(cases)}] {name} ({case.get('student_number', '?')})",
              flush=True)
        tabs = {}
        for tab in TABS:
            try:
                tabs[tab] = mc.case_tab(case["case_uuid"], tab)
            except Exception as e:
                print(f"    !! tab/{tab}: {e}", flush=True)
                tabs[tab] = None
        stem = f"{case.get('student_number', '?')} {name.lower()}"
        stem = re.sub(r"[^\w.-]+", " ", stem).strip().replace(" ", "_")
        (CASES_DIR / f"{stem}.json").write_text(json.dumps({
            "search": {k: v for k, v in case.items() if k != "case_uuid"},
            "case_uuid": case.get("case_uuid", ""),
            "tabs": {t: strip_private(c) for t, c in tabs.items()},
        }, indent=1, ensure_ascii=False))
        rows.append(flatten(case, tabs))
        print(f"    {rows[-1]['phase'] or 'no phase'} | "
              f"{rows[-1]['thesis_title'][:55] or '(no title yet)'}", flush=True)

    with INDEX_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=INDEX_COLUMNS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"\nWrote {INDEX_CSV} ({len(rows)} rows)", flush=True)
    print(f"Raw tab content in {CASES_DIR}/", flush=True)

    filled = [r for r in rows if r["human_participation"]]
    yes = [r["student_name"] for r in rows if r["human_participation"] == "yes"]
    pending = [r["student_name"] for r in rows if not r["human_participation"]]
    ext = [r["student_name"] for r in rows if r["external_graduation"] == "yes"]
    conf = [r["student_name"] for r in rows if r["confidentiality"] == "yes"]
    print("\n=== agreements summary ===")
    print(f"human participation: yes {len(yes)}, no {len(filled) - len(yes)}, "
          f"not filled in {len(pending)}")
    if yes:
        print(f"  yes: {', '.join(sorted(yes))}")
    if pending:
        print(f"  not filled in: {', '.join(sorted(pending))}")
    print(f"external graduation: yes {len(ext)}"
          + (f" ({', '.join(sorted(ext))})" if ext else ""))
    print(f"confidential: {', '.join(sorted(conf)) if conf else 'none'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
