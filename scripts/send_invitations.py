#!/usr/bin/env python3
"""Send the Kick-off and Green-light calendar invitations.

The rest of the pipeline already collects everything an invitation needs:

  registrations/assessments.csv   what, when, where (scripts/fetch_registrations.py)
  mycase/cases/*.json             who: student, supervisors, delegate (scripts/fetch_mycase.py)

This script joins the two, decides which assessments are ready to invite, and
hands each invitation to a Power Automate flow that creates a real Outlook
meeting and mails the attendees. Microsoft Graph is deliberately not used
(ICT does not allow an app registration), and neither is the Forms submission
trigger (the delegate is appointed *after* the registration): the script is
the gatekeeper and runs the flow afterwards.

The flow is dumb on purpose: it only creates, updates or deletes the event.
All the rules -- who gets invited, when an assessment is ready, what the body
says, how changes are detected -- live here, in git.

An assessment is sent only when all of this holds:

  - the student has an open MyCase case with an e-mail address;
  - the case has a supervisory team in MyCase;
  - a delegate has been appointed in MyCase (with an e-mail address);
  - the form carries a date, a time slot of the right length, and a room;
  - the date is not in the past.

Anything else is reported as waiting or blocked and never sent. Sending is
idempotent: the state file remembers what went out, so a second run does
nothing, an edited date/time/room/attendee list becomes an update, and a
registration that disappeared can become a cancellation (--cancel-missing).

Read-only by default; there are two transports. The manual one needs no
premium licence, because the Request connector (HTTP trigger, Response) is
premium and the M365 seeded Power Automate only has standard connectors:

  --batch            write the ready invitations as one JSON array, to paste
                     into the manual flow's `payload` input;
  --import-results   read back the event ids the flow mails as a JSON array
                     (use '-' for stdin: pbpaste | ... --import-results -);
  --send             POST each invitation to the flow's HTTP trigger instead
                     (premium; same payloads, and the Response action returns
                     the event id directly).

Real invitations additionally need `allow_real_send: true` in the config, so
testing cannot mail students by accident. --test builds a dummy student and
only mails the addresses listed in `test_to`, with its own state and batch:

  python3 scripts/send_invitations.py                  # dry run, real data
  python3 scripts/send_invitations.py --test           # dry run, dummy student
  python3 scripts/send_invitations.py --test --batch   # batch for the flow
  pbpaste | python3 scripts/send_invitations.py --test --import-results -
  python3 scripts/send_invitations.py --send           # premium variant

Configuration (gitignored, it holds addresses and the trigger URL):

  registrations/invite_config.yml
    organizer: k.ohori@tudelft.nl   # ORGANIZER in the preview .ics
    flow_url: https://prod-...      # the flow's HTTP trigger (--send only)
    test_to: [me@tudelft.nl, ...]   # --test recipients (add your own accounts)
    allow_real_send: false          # flip to true when ready for students

Requires: pyyaml.
"""

import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import re
import sys
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
REG_DIR = REPO_ROOT / "registrations"
ASSESSMENTS_CSV = REG_DIR / "assessments.csv"
CASES_DIR = REPO_ROOT / "mycase" / "cases"
CONFIG_PATH = REG_DIR / "invite_config.yml"
STATE_PATH = REG_DIR / "invitations_state.json"
TEST_STATE_PATH = REG_DIR / "invitations_test_state.json"
OUTBOX_DIR = REG_DIR / "outbox"
BATCH_PATH = REG_DIR / "batch.json"
TEST_BATCH_PATH = REG_DIR / "batch_test.json"
PENDING_PATH = REG_DIR / "pending_batch.json"
TEST_PENDING_PATH = REG_DIR / "pending_batch_test.json"
REPORT_PATH = REG_DIR / "invitations_report.md"
TEST_REPORT_PATH = REG_DIR / "invitations_test_report.md"
SLOT_PAGE = REPO_ROOT / "registration" / "index.md"

FORMS = {"kickoff": "Kick-off", "greenlight": "Green-light"}
MINUTES = {"kickoff": 45, "greenlight": 60}
TZ = ZoneInfo("Europe/Amsterdam")
FLOW_TZ = "W. Europe Standard Time"
RULES_URL = "https://geomatics.bk.tudelft.nl/geo2022/rules/"
UID_DOMAIN = "geo2022.bk.tudelft.nl"
TIME_RE = re.compile(r"(\d{1,2}):(\d{2})\s*[-\u2013\u2014]\s*(\d{1,2}):(\d{2})")
EMPTY_ROOMS = {"", "TBA", "TBD", "TBC", "?"}


# --------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------

def normalise(name: str) -> str:
    """Lowercase, accent- and punctuation-free form used to match people.

    The Forms responses and MyCase spell names slightly differently; the same
    normalisation as scripts/fetch_registrations.py, plus accent folding so
    'Carmem Félix Aires' matches 'Carmem Felix Aires'.
    """
    text = unicodedata.normalize("NFKD", str(name or ""))
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^a-z ]", " ", text.lower())
    return re.sub(r"\s+", " ", text).strip()


def parse_date(value: str):
    try:
        return dt.date.fromisoformat((value or "").strip())
    except ValueError:
        return None


def parse_time(value: str):
    """'13:45 - 14:30' -> (time(13,45), time(14,30)); None when unusable."""
    match = TIME_RE.search(value or "")
    if not match:
        return None
    try:
        start = dt.time(int(match.group(1)), int(match.group(2)))
        end = dt.time(int(match.group(3)), int(match.group(4)))
    except ValueError:
        return None
    return (start, end) if end > start else None


def minutes_between(start: dt.time, end: dt.time) -> int:
    return (end.hour * 60 + end.minute) - (start.hour * 60 + start.minute)


def slot_table() -> dict:
    """Official slot strings per form, read from registration/index.md.

    Parsing the published page keeps the check in sync with what supervisors
    are told; if the page changes shape the sets stay empty and the check is
    skipped rather than wrong.
    """
    out = {"kickoff": set(), "greenlight": set()}
    try:
        text = SLOT_PAGE.read_text(encoding="utf-8")
    except OSError:
        return out
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        for key, cell in zip(("kickoff", "greenlight"), cells[:2]):
            match = re.search(r"(\d{2}:\d{2})\s*[-\u2013\u2014]\s*(\d{2}:\d{2})", cell)
            if match:
                out[key].add(f"{match.group(1)}-{match.group(2)}")
    return out


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    tmp.replace(path)


def die(message: str):
    raise SystemExit(message)


# --------------------------------------------------------------------------
# Config
# --------------------------------------------------------------------------

def load_config(path: Path = CONFIG_PATH) -> dict:
    config = {"organizer": "", "flow_url": "", "test_to": [],
              "allow_real_send": False}
    try:
        loaded = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except OSError:
        loaded = {}
    except yaml.YAMLError as e:
        die(f"Cannot parse {path}: {e}")
    if isinstance(loaded, dict):
        config.update(loaded)
    if os.environ.get("INVITE_FLOW_URL"):
        config["flow_url"] = os.environ["INVITE_FLOW_URL"]
    config["test_to"] = [str(a).strip() for a in (config.get("test_to") or [])
                         if str(a).strip()]
    return config


def test_recipients(config: dict, args) -> list:
    people = args.test_to or config["test_to"]
    organizer = config["organizer"].strip().lower()
    out = []
    for address in people:
        address = address.strip()
        if address and address.lower() != organizer \
                and address.lower() not in [a.lower() for a in out]:
            out.append(address)
    return out


# --------------------------------------------------------------------------
# MyCase: who to invite
# --------------------------------------------------------------------------

def case_records() -> dict:
    """{normalised student name: record} from mycase/cases/*.json.

    The case JSON is used rather than mycase_index.csv because it carries the
    e-mail addresses of the student, both supervisors and the delegate, plus
    MyCase's own planning dates for the cross-check. An open case wins over a
    closed one with the same name.
    """
    out = {}
    for path in sorted(CASES_DIR.glob("*.json")):
        try:
            case = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        tabs = case.get("tabs") or {}
        search = case.get("search") or {}
        summary = tabs.get("summary") or {}
        student = summary.get("studentInfo") or {}
        project = tabs.get("project") or summary.get("project") or {}
        team = (tabs.get("stakeholders") or {}).get("team") or {}
        planning = (tabs.get("planning") or {}).get("currentPlanning") or {}

        name = search.get("student_name") or student.get("name") or ""
        key = normalise(name)
        if not key:
            continue

        responsible = team.get("gradResponsibleSupervisor") or {}
        others = [s for s in (team.get("gradSupervisor") or [])
                  if s.get("email") and s.get("email") != responsible.get("email")]
        delegate = team.get("gradDelegate") or {}

        record = {
            "name": name,
            "uuid": case.get("case_uuid") or f"case-{search.get('case_id', '')}",
            "status": search.get("status", ""),
            "phase": search.get("phase", ""),
            "email": (student.get("email") or "").strip(),
            "title": (project.get("title") or "").strip(),
            "people": [p for p in [responsible] + others if p.get("email")],
            "delegate": delegate,
            "plan": {"kickoff": planning.get("kick-off", ""),
                     "greenlight": planning.get("greenlight", "")},
        }
        if key in out and out[key]["status"] == "open" and record["status"] != "open":
            continue
        out[key] = record
    return out


def read_rows(path: Path = ASSESSMENTS_CSV):
    """(latest row per (form, student), [(row, superseded row), ...])."""
    try:
        with path.open(encoding="utf-8") as handle:
            rows = [r for r in csv.DictReader(handle)
                    if (r.get("student") or "").strip()]
    except OSError:
        die(f"Cannot read {path}. Run scripts/fetch_registrations.py first.")

    def when(row):
        try:
            number = int(row.get("response_id") or 0)
        except ValueError:
            number = 0
        return (row.get("submitted") or "", number)

    latest, superseded = {}, []
    for row in rows:
        key = (row["form"].strip().lower(), normalise(row["student"]))
        if key not in latest:
            latest[key] = row
            continue
        superseded.append((row, latest[key]))
        if when(row) > when(latest[key]):
            latest[key] = row
    return list(latest.values()), superseded


# --------------------------------------------------------------------------
# Turning a registration into an invitation
# --------------------------------------------------------------------------

def event_text(form: str, student: str, case: dict, date: dt.date,
               start: dt.time, end: dt.time, room: str) -> tuple:
    """(subject, body) of the invitation."""
    label = FORMS[form]
    subject = f"{label} assessment \u2014 {student}"
    lines = [
        f"{label} assessment for the MSc Geomatics graduation thesis of {student}.",
        "",
    ]
    if case.get("title"):
        lines.append(f"Thesis: {case['title']}")
    supervisor_names = [p.get("display_name", "") for p in case.get("people", [])]
    supervisor_names = [n for n in supervisor_names if n]
    if supervisor_names:
        lines.append(f"Supervisors: {', '.join(supervisor_names)}")
    delegate = (case.get("delegate") or {})
    if delegate.get("display_name"):
        lines.append(f"Delegate: {delegate['display_name']}")
    lines += [
        "",
        f"Date: {date:%A} {date.day} {date:%B %Y}",
        f"Time: {start:%H:%M}\u2013{end:%H:%M}",
        f"Room: {room}",
        "",
        f"The assessment procedure is described in {RULES_URL}",
    ]
    return subject, "\n".join(lines)


def make_invite(form: str, student: str, date, times, room: str, case: dict,
                problems: list, waiting: list, warnings: list,
                test: bool = False) -> dict:
    """One invitation candidate, sent or not, with its reasons."""
    invite = {
        "form": form,
        "student": student,
        "date": date.isoformat() if date else "",
        "start": times[0].strftime("%H:%M") if times else "",
        "end": times[1].strftime("%H:%M") if times else "",
        "room": room,
        "test": test,
        "status": "ready" if not problems and not waiting
                  else ("blocked" if problems else "waiting"),
        "problems": problems,
        "waiting": waiting,
        "warnings": warnings,
        "attendees": [],
        "action": None,
    }
    if case is None or not date or not times:
        return invite

    attendees = []
    for person in ([{"email": case.get("email"), "display_name": student}]
                   + list(case.get("people") or []) + [case.get("delegate") or {}]):
        address = (person.get("email") or "").strip()
        if address and address.lower() not in [a.lower() for a in attendees]:
            attendees.append(address)
    organizer = case.get("_organizer", "")
    invite["attendees"] = [a for a in attendees if a.lower() != organizer.lower()]

    subject, body = event_text(form, student, case, date, times[0], times[1], room)
    if test:
        subject = f"[TEST] {subject}"
        body = ("TEST INVITATION \u2014 no real assessment is scheduled; this "
                "meeting exists only to test the invitation pipeline.\n\n" + body)
    invite.update(subject=subject, body=body)
    invite["uid"] = (f"test-{form}@{UID_DOMAIN}" if test
                     else f"{form}-{case['uuid']}@{UID_DOMAIN}")
    invite["hash"] = payload_hash(invite)
    return invite


def payload_hash(invite: dict) -> str:
    fields = {
        "subject": invite.get("subject", ""),
        "body": invite.get("body", ""),
        "date": invite.get("date", ""),
        "start": invite.get("start", ""),
        "end": invite.get("end", ""),
        "location": invite.get("room", ""),
        "attendees": sorted(a.lower() for a in invite.get("attendees", [])),
    }
    return hashlib.sha256(json.dumps(fields, sort_keys=True,
                                     ensure_ascii=False).encode()).hexdigest()


def build_invites(rows: list, cases: dict, config: dict, args) -> list:
    """Assess every registration and return one invitation candidate each."""
    slots = slot_table()
    today = dt.date.today()
    invites = []
    for row in rows:
        form = (row.get("form") or "").strip().lower()
        student = (row.get("student") or "").strip()
        if args.form and form != args.form:
            continue
        if args.student and args.student.lower() not in student.lower():
            continue

        problems, waiting, warnings = [], [], []
        if form not in FORMS:
            problems.append(f"unknown form {form!r}")

        date = parse_date(row.get("date"))
        times = parse_time(row.get("time"))
        room = (row.get("room") or "").strip()

        if date is None:
            problems.append("no usable date")
        if times is None:
            problems.append("no usable time slot")
        if date and times:
            duration = minutes_between(*times)
            if form in MINUTES and duration != MINUTES[form]:
                problems.append(f"{FORMS[form]} slots last {MINUTES[form]} "
                                f"minutes, the form says {duration}")
            if date < today:
                problems.append("the date is in the past")
            slot = f"{times[0]:%H:%M}-{times[1]:%H:%M}"
            if slots.get(form) and slot not in slots[form]:
                warnings.append(f"{slot} is not one of the published "
                                f"{FORMS[form].lower()} time slots")
        if room.upper() in EMPTY_ROOMS:
            waiting.append("no room yet (TBA/TBD)")

        case = cases.get(normalise(student))
        if case is None:
            problems.append("no MyCase case with this student name")
        else:
            case["_organizer"] = config.get("organizer", "")
            if case.get("status") and case["status"] != "open":
                problems.append(f"the MyCase case is {case['status']}")
            if not case.get("email"):
                problems.append("the MyCase case has no student e-mail")
            if not case.get("people"):
                waiting.append("no supervisory team in MyCase")
            if not (case.get("delegate") or {}).get("email"):
                waiting.append("no delegate appointed in MyCase")
            planned = case.get("plan", {}).get(form, "")
            if planned and date and planned != date.isoformat():
                warnings.append(f"MyCase planning says {planned} for the "
                                f"{FORMS[form].lower()}")

        invite = make_invite(form, student, date, times, room, case,
                             problems, waiting, warnings)
        invite["case"] = case
        invites.append(invite)
    return invites


def test_invites(config: dict, args) -> list:
    """A dummy student so the whole pipeline can be exercised in isolation."""
    form = args.form or "kickoff"
    date = dt.date.today() + dt.timedelta(days=7)
    slot = "13:45 - 14:30" if form == "kickoff" else "13:45 - 14:45"
    times = parse_time(slot)
    recipients = test_recipients(config, args)
    warnings = []
    if not recipients:
        warnings.append("test_to has no address besides the organizer; add "
                        "another of your own accounts to receive a real test "
                        "invitation")
    case = {
        "name": "Dummy Student",
        "uuid": "dummy-test-case",
        "status": "open",
        "email": "dummy.student@example.invalid",
        "title": "A dummy thesis used to test the invitation pipeline",
        "people": [{"display_name": "Dummy Supervisor",
                    "email": "dummy.supervisor@example.invalid"}],
        "delegate": {"display_name": "Dummy Delegate",
                     "email": "dummy.delegate@example.invalid"},
        "plan": {"kickoff": "", "greenlight": ""},
        "_organizer": config.get("organizer", ""),
    }
    invite = make_invite(form, "Dummy Student", date, times,
                         "Room-00.00.Dummy", case, [], [], warnings, test=True)
    invite["attendees"] = recipients
    invite["hash"] = payload_hash(invite)
    invite["case"] = case
    return [invite]


# --------------------------------------------------------------------------
# Reconciling with what has already been sent
# --------------------------------------------------------------------------

def reconcile(invites: list, state: dict, args) -> None:
    """Set each invitation's action: create, update, or nothing."""
    for invite in invites:
        if invite["status"] != "ready" or "subject" not in invite:
            continue
        entry = state.get(invite["uid"], {})
        invite["entry"] = entry
        if entry and entry.get("event_id"):
            if entry.get("hash") == invite["hash"] and not args.force:
                invite["action"] = None
                continue
            invite["action"] = "update"
            invite["sequence"] = int(entry.get("sequence", 1)) + 1
            continue
        if entry:
            invite["warnings"].append(
                "changed since it was sent, but the flow returned no event "
                "id; cannot update, re-check the calendar before creating")
        invite["action"] = "create"
        invite["sequence"] = int(entry.get("sequence", 0)) + 1


def cancellations(state: dict, invites: list, args) -> list:
    """Sent invitations whose registration disappeared from the forms."""
    known = {i["uid"] for i in invites}
    if not args.cancel_missing:
        return []
    out = []
    for uid, entry in state.items():
        if uid in known or not entry.get("event_id"):
            continue
        out.append({"uid": uid, "entry": entry, "action": "cancel",
                    "sequence": int(entry.get("sequence", 1)) + 1})
    return out


# --------------------------------------------------------------------------
# The manual-transport variant: export a batch, import the flow's results
# --------------------------------------------------------------------------

def load_results(path: str) -> list:
    """Result objects from a JSON file, stdin ('-'), or an e-mail body.

    The flow mails the results, so the pasted text may carry a greeting or
    signature around the JSON; the outermost array is extracted as a fallback.
    """
    if path == "-":
        text = sys.stdin.read()
    else:
        try:
            text = Path(path).read_text(encoding="utf-8")
        except OSError as e:
            die(f"Cannot read the results: {e}")
    text = text.strip().lstrip("\ufeff")
    if not text:
        die("The results are empty.")

    data = None
    try:
        data = json.loads(text)
    except ValueError:
        start, end = text.find("["), text.rfind("]")
        if start >= 0 and end > start:
            try:
                data = json.loads(text[start:end + 1])
            except ValueError:
                data = None
    if data is None:
        die("No JSON found in the results; paste the body of the flow's "
            "results e-mail unchanged.")

    if isinstance(data, dict):
        for key in ("value", "results", "Results", "items"):
            if isinstance(data.get(key), list):
                return data[key]
        return [data]
    if isinstance(data, list):
        return data
    return [data]


def import_results(path: str, state: dict, state_path: Path,
                   pending_path: Path) -> tuple:
    """Merge the flow's results (uid -> event id) into the state file."""
    items = load_results(path)
    pending = read_json(pending_path)
    applied, problems = [], []
    for item in items:
        if not isinstance(item, dict):
            problems.append(f"not an object: {str(item)[:120]}")
            continue
        uid = find_value(item, "uid")
        action = (find_value(item, "action") or "create").lower()
        event_id = find_value(item, "eventId", "event_id", "id")
        web_link = find_value(item, "webLink", "web_link")
        error = find_value(item, "error", "message")
        if not uid:
            problems.append(f"a result has no uid: {json.dumps(item)[:120]}")
            continue
        meta = pending.get(uid) or {}
        body = meta.get("payload") or {}
        entry = state.get(uid) or {}
        if error and not event_id:
            problems.append(f"{uid}: the flow reported {error!r}")
            continue
        if action == "cancel":
            if uid in state:
                state.pop(uid)
                applied.append(f"{uid}: cancelled")
            else:
                problems.append(f"{uid}: cancellation of an unknown meeting")
            continue

        event_id = event_id or entry.get("event_id", "")
        entry.update({
            "hash": meta.get("hash", entry.get("hash", "")),
            "sequence": body.get("sequence", entry.get("sequence", 1)),
            "event_id": event_id,
            "web_link": web_link or entry.get("web_link", ""),
            "sent_at": dt.datetime.now().isoformat(timespec="seconds"),
            "subject": body.get("subject", entry.get("subject", "")),
            "form": body.get("form", entry.get("form", "")),
            "student": body.get("student", entry.get("student", "")),
            "date": (body.get("start") or "")[:10] or entry.get("date", ""),
            "start": (body.get("start") or "")[11:16] or entry.get("start", ""),
            "end": (body.get("end") or "")[11:16] or entry.get("end", ""),
            "location": body.get("location", entry.get("location", "")),
            "attendees": body.get("attendees", entry.get("attendees", [])),
            "test": body.get("test", entry.get("test", False)),
        })
        state[uid] = entry
        applied.append(f"{uid}: {action}" + ("" if event_id
                                             else " (no event id)"))
        if not event_id:
            problems.append(f"{uid}: no event id in the results, so a later "
                            f"change would create a second meeting")
    write_json(state_path, state)
    if not pending:
        problems.append(f"no {pending_path.name} found; hashes were taken "
                        f"from the current data, so verify before changing "
                        f"an invitation again")
    return applied, problems


def write_batch(payloads: list, hashes: dict, path: Path,
                pending_path: Path) -> None:
    """Write the batch for the manual flow and what it was generated from."""
    write_json(path, payloads)
    write_json(pending_path, {
        item["uid"]: {"hash": hashes.get(item["uid"], ""), "payload": item}
        for item in payloads})



# --------------------------------------------------------------------------
# Output: outbox, preview .ics, report
# --------------------------------------------------------------------------

def payload(invite: dict, action: str) -> dict:
    """The JSON the Power Automate flow receives."""
    entry = invite.get("entry") or {}
    return {
        "action": action,
        "uid": invite["uid"],
        "sequence": invite.get("sequence", 1),
        "test": bool(invite.get("test")),
        "form": invite.get("form", ""),
        "student": invite.get("student", ""),
        "subject": invite.get("subject", ""),
        "start": f"{invite['date']}T{invite['start']}:00",
        "end": f"{invite['date']}T{invite['end']}:00",
        "timezone": FLOW_TZ,
        "location": invite.get("room", ""),
        "body": invite.get("body", ""),
        "attendees": invite.get("attendees", []),
        "event_id": entry.get("event_id", ""),
    }


def cancel_payload(item: dict) -> dict:
    """The JSON for cancelling a meeting that is already in the calendar."""
    entry = item["entry"]
    return {
        "action": "cancel",
        "uid": item["uid"],
        "sequence": item["sequence"],
        "test": bool(entry.get("test")),
        "form": entry.get("form", ""),
        "student": entry.get("student", ""),
        "subject": entry.get("subject", ""),
        "start": f"{entry.get('date', '')}T{entry.get('start', '00:00')}:00",
        "end": f"{entry.get('date', '')}T{entry.get('end', '00:00')}:00",
        "timezone": FLOW_TZ,
        "location": entry.get("location", ""),
        "body": "",
        "attendees": entry.get("attendees", []),
        "event_id": entry.get("event_id", ""),
    }


def write_outbox(payloads: list, directory: Path) -> list:
    directory.mkdir(parents=True, exist_ok=True)
    for stale in directory.glob("*.json"):
        stale.unlink()
    written = []
    for item in payloads:
        name = re.sub(r"[^a-z0-9]+", "-",
                      f"{item['uid'].split('@')[0]}-{item['action']}").strip("-")
        path = directory / f"{name}.json"
        write_json(path, item)
        written.append(path)
    return written


def ics_escape(value: str) -> str:
    return (str(value).replace("\\", "\\\\").replace(";", "\\;")
            .replace(",", "\\,").replace("\n", "\\n"))


def write_ics(invites: list, directory: Path, organizer: str) -> list:
    """Preview files; not used for sending, but handy to eyeball the events."""
    directory.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    written = []
    for invite in invites:
        if invite["action"] not in ("create", "update"):
            continue
        date = dt.date.fromisoformat(invite["date"])
        start = dt.time.fromisoformat(invite["start"])
        end = dt.time.fromisoformat(invite["end"])
        begin = dt.datetime.combine(date, start, tzinfo=TZ).astimezone(dt.timezone.utc)
        finish = dt.datetime.combine(date, end, tzinfo=TZ).astimezone(dt.timezone.utc)
        lines = [
            "BEGIN:VCALENDAR",
            "VERSION:2.0",
            "PRODID:-//GEO2022//invitations//EN",
            "METHOD:REQUEST",
            "BEGIN:VEVENT",
            f"UID:{invite['uid']}",
            f"SEQUENCE:{invite.get('sequence', 1)}",
            f"DTSTAMP:{stamp}",
            f"DTSTART:{begin:%Y%m%dT%H%M%SZ}",
            f"DTEND:{finish:%Y%m%dT%H%M%SZ}",
            f"SUMMARY:{ics_escape(invite['subject'])}",
            f"LOCATION:{ics_escape(invite['room'])}",
            f"DESCRIPTION:{ics_escape(invite['body'])}",
            "STATUS:CONFIRMED",
            "TRANSP:OPAQUE",
        ]
        if organizer:
            lines.append(f"ORGANIZER;CN=GEO2022 coordinator:mailto:{organizer}")
        for address in invite["attendees"]:
            lines.append("ATTENDEE;ROLE=REQ-PARTICIPANT;RSVP=TRUE:"
                         f"mailto:{address}")
        lines += ["END:VEVENT", "END:VCALENDAR", ""]
        path = directory / f"{invite['uid'].replace('@', '_at_')}.ics"
        path.write_text("\r\n".join(lines), encoding="utf-8")
        written.append(path)
    return written


def write_report(path: Path, invites: list, cancels: list, state: dict,
                 superseded: list, args, config: dict, sent: list,
                 outbox: list) -> None:
    label = {True: "test (dummy student)", False: "real"}[bool(args.test)]
    if args.send:
        outcome = (f"Sent {len(sent)} request(s) to the flow." if sent
                   else "Sending mode: nothing new to send.")
    elif args.batch:
        outcome = "Batch written for the manual flow; nothing was sent."
    else:
        outcome = "Nothing was sent (dry run)."
    lines = [
        f"# Invitation report ({dt.date.today().isoformat()}, {label})",
        "",
        outcome,
        "",
    ]
    if args.send and not args.test and not config.get("allow_real_send"):
        lines += ["Real sending is disabled in registrations/invite_config.yml "
                  "(`allow_real_send: false`).", ""]

    groups = [("Ready", [i for i in invites if i["status"] == "ready"]),
              ("Waiting", [i for i in invites if i["status"] == "waiting"]),
              ("Blocked", [i for i in invites if i["status"] == "blocked"])]
    ok = {item["uid"]: item for item in sent if 200 <= item["status"] < 300}
    for title, group in groups:
        lines += [f"## {title} ({len(group)})", ""]
        if not group:
            lines += ["None.", ""]
            continue
        lines += ["| form | date | time | room | student | action |",
                  "|---|---|---|---|---|---|"]
        for invite in group:
            if invite["uid"] in ok:
                action = "sent"
            else:
                action = invite.get("action") or (
                    "\u2014" if invite["status"] == "ready" else "")
            lines.append(
                f"| {FORMS.get(invite['form'], invite['form'])} "
                f"| {invite['date'] or '?'} "
                f"| {invite['start'] or '?'}\u2013{invite['end'] or '?'} "
                f"| {invite['room'] or '?'} | {invite['student']} | {action} |")
        lines.append("")
        for invite in group:
            notes = invite["problems"] + invite["waiting"] + invite["warnings"]
            if notes:
                lines.append(f"- **{invite['student']} "
                             f"({FORMS.get(invite['form'], invite['form'])})**: "
                             + "; ".join(notes))
        if any(invite["problems"] + invite["waiting"] + invite["warnings"]
               for invite in group):
            lines.append("")
        attendees = [i for i in group if i.get("attendees")]
        for invite in attendees:
            lines.append(f"- {invite['student']}: invite "
                         f"{', '.join(invite['attendees'])}")
        if attendees:
            lines.append("")

    if cancels:
        lines += [f"## Cancellations ({len(cancels)})", ""]
        for item in cancels:
            lines.append(f"- {item['uid']} (event "
                         f"{item['entry'].get('event_id', '?')})")
        lines.append("")
    elif state and not args.cancel_missing and not args.test:
        lines += ["## Cancellations", "",
                  "Not checked; pass --cancel-missing to cancel meetings "
                  "whose registration disappeared.", ""]

    if superseded:
        lines += ["## Multiple form responses", ""]
        for row, previous in superseded:
            lines.append(f"- {row['student']} ({row['form']}): using the "
                         f"response submitted {row.get('submitted', '?')} "
                         f"(superseding {previous.get('submitted', '?')})")
        lines.append("")

    if sent:
        lines += ["## Replies from the flow", ""]
        for item in sent:
            detail = f", event {item['event_id']}" if item["event_id"] else ""
            lines.append(f"- {item['uid']} ({item['action']}): "
                         f"HTTP {item['status']}{detail}")
            if not 200 <= item["status"] < 300:
                lines.append(f"  - response: {item['raw']}")
        lines.append("")
    if outbox:
        lines += ["## Payloads written", ""]
        lines += [f"- `{p.relative_to(REPO_ROOT)}`" for p in outbox]
        lines.append("")
    if args.batch:
        batch = TEST_BATCH_PATH if args.test else BATCH_PATH
        lines += ["## Manual flow", "",
                  f"Batch: `{batch.relative_to(REPO_ROOT)}` ({len(outbox)} "
                  f"request(s)). Paste its contents into the flow's `payload` "
                  f"input, run it, then import the e-mail body:", "",
                  "```sh",
                  ("pbpaste | python3 scripts/send_invitations.py --test "
                   "--import-results -" if args.test else
                   "pbpaste | python3 scripts/send_invitations.py "
                   "--import-results -"),
                  "```", ""]

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


# --------------------------------------------------------------------------
# Sending
# --------------------------------------------------------------------------

def post_flow(url: str, body: dict, timeout: int = 90) -> tuple:
    data = json.dumps(body).encode("utf-8")
    request = urllib.request.Request(
        url, data=data, method="POST",
        headers={"Content-Type": "application/json",
                 "Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, response.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as error:
        return error.code, error.read().decode("utf-8", "replace")
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        return 0, str(error)


def find_value(data, *names: str) -> str:
    """First string value under any of the names, searching nested objects."""
    if isinstance(data, dict):
        lowered = {str(k).lower(): v for k, v in data.items()}
        for name in names:
            value = lowered.get(name.lower())
            if isinstance(value, str) and value:
                return value
        for value in data.values():
            found = find_value(value, *names)
            if found:
                return found
    elif isinstance(data, list):
        for value in data:
            found = find_value(value, *names)
            if found:
                return found
    return ""


def send(payloads: list, url: str, state: dict, state_path: Path,
         timeout: int = 90) -> list:
    results = []
    for body in payloads:
        status, raw = post_flow(url, body, timeout=timeout)
        try:
            reply = json.loads(raw) if raw.strip() else {}
        except ValueError:
            reply = {}
        # A Response action whose body is a single string yields a JSON string
        # rather than an object; unwrap it so the event id is still found.
        if isinstance(reply, str):
            try:
                reply = json.loads(reply)
            except ValueError:
                pass
        ok = 200 <= status < 300
        result = {"uid": body["uid"], "action": body["action"],
                  "status": status, "event_id": find_value(reply, "eventId",
                                                           "event_id", "id"),
                  "web_link": find_value(reply, "webLink", "web_link",
                                         "htmlLink"),
                  "raw": raw[:500]}
        results.append(result)

        if ok:
            entry = state.get(body["uid"], {})
            if body["action"] != "cancel":
                entry.update({
                    "hash": "",
                    "sequence": body["sequence"],
                    "event_id": result["event_id"] or entry.get("event_id", ""),
                    "web_link": result["web_link"] or entry.get("web_link", ""),
                    "sent_at": dt.datetime.now().isoformat(timespec="seconds"),
                    "subject": body["subject"],
                    "form": body["form"],
                    "student": body["student"],
                    "date": body["start"][:10],
                    "start": body["start"][11:16],
                    "end": body["end"][11:16],
                    "location": body["location"],
                    "attendees": body["attendees"],
                    "test": body["test"],
                })
                state[body["uid"]] = entry
            else:
                state.pop(body["uid"], None)
            write_json(state_path, state)
        print(f"  {body['action']:6s} {body['uid']}: HTTP {status} "
              f"{'ok' if ok else raw[:200]}", flush=True)
    return results


def finish_state(invites: list, state_path: Path, sent: list) -> None:
    """Record the payload hash of what was actually sent for each invite.

    Only successful requests count: a failed update must not make the next run
    believe that the change already went out.
    """
    ok = {item["uid"] for item in sent if 200 <= item["status"] < 300}
    state = read_json(state_path)
    for invite in invites:
        if invite["uid"] in ok and invite.get("hash"):
            entry = state.get(invite["uid"])
            if entry is not None:
                entry["hash"] = invite["hash"]
    write_json(state_path, state)


# --------------------------------------------------------------------------
# Command line
# --------------------------------------------------------------------------

def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Send the Kick-off and Green-light calendar invitations "
                    "through a Power Automate flow. Dry run unless --batch "
                    "(manual flow) or --send (HTTP trigger, premium).")
    parser.add_argument("--send", action="store_true",
                        help="POST the ready invitations to a flow's HTTP "
                             "trigger (premium connector)")
    parser.add_argument("--batch", action="store_true",
                        help="write the ready invitations as one JSON batch "
                             "for the manual flow, and stop there")
    parser.add_argument("--import-results", metavar="PATH",
                        help="import the flow's results (event ids); '-' "
                             "reads stdin, e.g. pbpaste | ... --import-results -")
    parser.add_argument("--test", action="store_true",
                        help="use a dummy student and only the test_to "
                             "addresses")
    parser.add_argument("--test-to", action="append", metavar="EMAIL",
                        help="extra test recipient (repeatable)")
    parser.add_argument("--flow-url", metavar="URL",
                        help="override the flow's HTTP trigger URL")
    parser.add_argument("--config", type=Path, default=CONFIG_PATH,
                        help=f"config file (default {CONFIG_PATH.relative_to(REPO_ROOT)})")
    parser.add_argument("--form", choices=sorted(FORMS),
                        help="only this assessment")
    parser.add_argument("--student", metavar="TEXT",
                        help="only students whose name contains TEXT")
    parser.add_argument("--force", action="store_true",
                        help="send even if nothing changed since last time")
    parser.add_argument("--cancel-missing", action="store_true",
                        help="cancel meetings whose registration disappeared")
    parser.add_argument("--outbox", type=Path, default=OUTBOX_DIR,
                        help=f"where the payloads are written (default "
                             f"{OUTBOX_DIR.relative_to(REPO_ROOT)})")
    parser.add_argument("--ics-dir", type=Path,
                        help="also write preview .ics files here")
    parser.add_argument("--report", type=Path,
                        help="report path (default per mode)")
    parser.add_argument("--timeout", type=int, default=90,
                        help="POST timeout in seconds (default 90)")
    return parser.parse_args(argv)


def main(argv=None) -> None:
    args = parse_args(argv)
    config = load_config(args.config)
    if args.flow_url:
        config["flow_url"] = args.flow_url
    config["organizer"] = (config.get("organizer") or "").strip()

    if args.send and args.batch:
        die("Choose one transport: --send (HTTP trigger) or --batch (manual).")

    label = "test (dummy student)" if args.test else "real"
    print(f"Invitations: {label} mode", flush=True)

    state_path = TEST_STATE_PATH if args.test else STATE_PATH
    state = read_json(state_path)

    if args.import_results:
        pending_path = TEST_PENDING_PATH if args.test else PENDING_PATH
        applied, problems = import_results(args.import_results, state,
                                           state_path, pending_path)
        for line in applied:
            print(f"  {line}", flush=True)
        for line in problems:
            print(f"  ! {line}", flush=True)
        print(f"\nState: {state_path.relative_to(REPO_ROOT)} "
              f"({len(state)} meeting(s))", flush=True)
        if applied:
            print("Re-run without --import-results to see what is left "
                  "to send.", flush=True)
        return

    superseded = []
    if args.test:
        invites = test_invites(config, args)
    else:
        rows, superseded = read_rows()
        invites = build_invites(rows, case_records(), config, args)
    if not invites:
        print("Nothing registered for these filters.", flush=True)

    reconcile(invites, state, args)
    cancels = [] if args.test else cancellations(state, invites, args)

    bodies = [cancel_payload(c) for c in cancels] + \
             [payload(i, i["action"]) for i in invites if i.get("action")]
    outbox = write_outbox(bodies, args.outbox)
    if args.ics_dir:
        write_ics(invites, args.ics_dir, config["organizer"])

    pending = [i for i in invites if i.get("action")]
    print(f"  ready {sum(1 for i in invites if i['status'] == 'ready')}, "
          f"waiting {sum(1 for i in invites if i['status'] == 'waiting')}, "
          f"blocked {sum(1 for i in invites if i['status'] == 'blocked')}, "
          f"to send {len(pending) + len(cancels)}", flush=True)
    for invite in invites:
        note = "; ".join(invite["problems"] + invite["waiting"]
                         + invite["warnings"])
        print(f"  {invite['status']:7s} {FORMS.get(invite['form'], '?'):10s} "
              f"{invite['student']:22s} {note}", flush=True)

    if args.batch:
        batch_path = TEST_BATCH_PATH if args.test else BATCH_PATH
        pending_path = TEST_PENDING_PATH if args.test else PENDING_PATH
        if not bodies:
            print("Nothing to send; no batch written.", flush=True)
        elif args.test and not (pending[0]["attendees"] if pending else []):
            die("--test has no recipients: add your own accounts to "
                "`test_to` in the config, or pass --test-to EMAIL.")
        else:
            if not args.test and not config.get("allow_real_send"):
                print("  ! `allow_real_send` is still false: running this "
                      "batch in the flow will mail students anyway.",
                      flush=True)
            hashes = {i["uid"]: i["hash"] for i in invites if i.get("action")}
            write_batch(bodies, hashes, batch_path, pending_path)
            print(f"\nBatch: {batch_path.relative_to(REPO_ROOT)} "
                  f"({len(bodies)} request(s))", flush=True)
            print("  1. Power Automate -> Run flow -> paste the file into "
                  "the `payload` input.", flush=True)
            print("  2. Copy the body of the results e-mail, then:", flush=True)
            prefix = "--test " if args.test else ""
            print(f"     pbpaste | python3 scripts/send_invitations.py "
                  f"{prefix}--import-results -", flush=True)

    sent = []
    if args.send:
        if not pending and not cancels:
            print("Nothing to send.", flush=True)
        elif not args.test and not config.get("allow_real_send"):
            die("Refusing to mail students: set `allow_real_send: true` in "
                f"{args.config.relative_to(REPO_ROOT)} once the flow has been "
                "tested (or run with --test).")
        elif not config.get("flow_url"):
            die("No flow URL: set `flow_url` in "
                f"{args.config.relative_to(REPO_ROOT)}, or pass --flow-url.")
        else:
            if args.test and not (pending[0]["attendees"] if pending else []):
                die("--test has no recipients: add your own accounts to "
                    "`test_to` in the config, or pass --test-to EMAIL.")
            print(f"Posting to the flow at {config['flow_url']}", flush=True)
            sent = send(bodies, config["flow_url"], state, state_path,
                        timeout=args.timeout)
            finish_state(pending, state_path, sent)
            failures = [r for r in sent if not 200 <= r["status"] < 300]
            if failures:
                print(f"\n{len(failures)} request(s) failed; nothing is "
                      "retried automatically. Check the flow's run history.",
                      flush=True)

    report = args.report or (TEST_REPORT_PATH if args.test else REPORT_PATH)
    write_report(report, invites, cancels, state, superseded, args, config,
                 sent, outbox)
    print(f"\nReport: {report.relative_to(REPO_ROOT)}", flush=True)
    if not args.send and not args.batch:
        print("Dry run: nothing was sent. Add --batch (manual flow) or "
              "--send (HTTP trigger).", flush=True)


if __name__ == "__main__":
    main()
