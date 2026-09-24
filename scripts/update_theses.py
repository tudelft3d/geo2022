#!/usr/bin/env python3
"""Sync _data/ongoing_theses.yml (the Current Theses page) with MyCase.

Every open MyCase case must appear on the page, and every entry on the
page must have an open case. One run:

  adds    an entry (name, cohort, phase, supervisors, official title when
          one is registered) for open cases that are missing, flagged
          needs_summary until the proposal summary is written
  syncs   phase, the official title (registered at green light) and the
          supervisory team from MyCase into existing entries; hand-written
          summaries and images are never touched
  prunes  with --prune, removes entries whose case is no longer open —
          reported first, so graduated students can be moved to the
          archive (scripts/enrich_geotheses.py) before pruning

MyCase's cohort suggestion is applied to new entries only; for existing
entries a differing suggestion is reported (February starts are
ambiguous, see scripts/fetch_mycase.py). Only public fields are copied:
never grades, student numbers or e-mail addresses.

Usage:
  python3 scripts/update_theses.py
  python3 scripts/update_theses.py --prune
"""

import argparse
import csv
import sys

import yaml

import enrich_geotheses as eg

REPO_ROOT = eg.REPO_ROOT
DATA_FILE = REPO_ROOT / "_data" / "ongoing_theses.yml"

FIELD_ORDER = ["surname", "name", "cohort", "phase", "title", "supervisors",
               "summary", "image", "needs_summary"]
PHASE_RANK = {"preparation": 1, "kick-off": 2, "midterm": 3,
              "green light": 4}
TERM_RANK = {"feb": 1, "april": 2, "sep": 3}


def cohort_sort_key(cohort):
    cohort = str(cohort or "")
    year = cohort[:4] if cohort[:4].isdigit() else "0000"
    return (-int(year), -TERM_RANK.get(cohort[4:], 0))


def entry_sort_key(e):
    return (cohort_sort_key(e.get("cohort")),
            -PHASE_RANK.get(str(e.get("phase", "")).lower(), 0),
            eg.foldcase(e.get("surname", "")), eg.foldcase(e.get("name", "")))


def write_yaml(entries):
    ordered = []
    for e in sorted(entries, key=entry_sort_key):
        clean = {}
        for field in FIELD_ORDER:
            if field in e and e[field] not in (None, ""):
                clean[field] = e[field]
        for extra in sorted(k for k in e
                            if k not in FIELD_ORDER and not k.startswith("_")):
            clean[extra] = e[extra]
        ordered.append(clean)
    header = ("# Ongoing MSc Geomatics theses (open MyCase cases), grouped\n"
              "# by starting cohort, newest first. scripts/update_theses.py\n"
              "# syncs names, cohorts, phases, titles and supervisors from\n"
              "# MyCase; summaries and images are maintained by hand. Validate\n"
              "# with scripts/check_geotheses.py (archive) — this file has no\n"
              "# checker yet.\n")
    body = yaml.safe_dump(ordered, allow_unicode=True, width=72,
                          sort_keys=False, default_flow_style=False)
    DATA_FILE.write_text(header + body, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--prune", action="store_true",
                    help="remove entries without an open MyCase case "
                         "(reported first either way)")
    args = ap.parse_args()

    if not eg.MYCASE_CSV.exists():
        print(f"No {eg.MYCASE_CSV} — run scripts/fetch_mycase.py first.")
        return 1
    with eg.MYCASE_CSV.open(encoding="utf-8") as f:
        open_cases = [r for r in csv.DictReader(f) if r["status"] == "open"]

    entries = yaml.safe_load(DATA_FILE.read_text()) or []

    used_cases = set()
    matched = []
    for e in entries:
        for i, row in enumerate(open_cases):
            if i in used_cases:
                continue
            if eg.names_match(e, row["student_name"]):
                used_cases.add(i)
                e["_row"] = row
                matched.append(e)
                break

    notes = []
    # sync existing entries from their case
    for e in entries:
        row = e.pop("_row", None)
        if not row:
            continue
        label = f"{e.get('name')} {e.get('surname')}"
        if row.get("phase") and row["phase"] != e.get("phase"):
            notes.append(f"PHASE {label}: {e.get('phase')} -> {row['phase']}")
            e["phase"] = row["phase"]
        title = (row.get("thesis_title") or "").strip()
        # MyCase truncates registered titles (~55 chars), so prefer the
        # longer of the hand-written and the registered title.
        if title and title != e.get("title"):
            if not e.get("title") or len(title) > len(e["title"]):
                notes.append(f"TITLE {label}: set from MyCase ({title[:50]}…)")
                e["title"] = title
            else:
                notes.append(f"TITLE {label}: MyCase's shorter (possibly "
                             f"truncated) title not applied: {title[:50]}…")
        sups = "; ".join(n.strip() for n in (
            (row.get("supervisor_1") or "").split(";")
            + (row.get("supervisor_2") or "").split(";")) if n.strip())
        if sups and sups != e.get("supervisors"):
            notes.append(f"SUPERVISORS {label}: set from MyCase ({sups})")
            e["supervisors"] = sups
        suggestion = row.get("suggested_cohort", "")
        if suggestion and suggestion != str(e.get("cohort", "")):
            notes.append(f"COHORT {label}: MyCase suggests {suggestion}, "
                         f"entry says {e.get('cohort')} (not changed)")

    # report pre-existing entries without an open case
    orphans = [e for e in entries if e not in matched]
    for e in orphans:
        notes.append(f"NOT OPEN ANYMORE: {e.get('name')} {e.get('surname')} "
                     f"({e.get('cohort')}) — move to the archive with "
                     "scripts/enrich_geotheses.py")
    if args.prune and orphans:
        entries = matched
        notes.append(f"PRUNED {len(orphans)} entry(ies)")

    # add missing open cases
    for i, row in enumerate(open_cases):
        if i in used_cases:
            continue
        surname, given = eg.split_full_name(row["student_name"])
        entry = {
            "surname": surname,
            "name": " ".join(given),
            "cohort": row.get("suggested_cohort", ""),
            "phase": row.get("phase", ""),
            "needs_summary": True,
        }
        title = (row.get("thesis_title") or "").strip()
        if title:
            entry["title"] = title
        sups = "; ".join(n.strip() for n in (
            (row.get("supervisor_1") or "").split(";")
            + (row.get("supervisor_2") or "").split(";")) if n.strip())
        if sups:
            entry["supervisors"] = sups
        entries.append(entry)
        notes.append(f"ADDED {row['student_name']} "
                     f"({row.get('suggested_cohort')}, {row.get('phase')}) "
                     "— write a proposal summary, then drop needs_summary")

    write_yaml(entries)
    print(f"{len(entries)} ongoing entries in {DATA_FILE.name}; "
          f"{len(notes)} note(s):")
    for n in notes:
        print(f"  - {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
