#!/usr/bin/env python3
"""Find pre-archive Geomatics theses via supervisor search on the repository.

The GDMC and 3d.bk.tudelft.nl lists (scripts/find_missing_theses.py) only
reach back to the archive's own start, so older theses -- particularly the
remote-sensing-supervised ones -- need a different net. This script sweeps
the repository search API for MSc theses whose supervisors (record
contributors) have a surname from scripts/geomatics_supervisors.yml, keeps
the ones from before the archive's coverage, fetches their repository
record pages (cached, robots.txt-delayed) to get mentors and programme,
and writes old_theses_report.md:

  confirmed gaps    the record's Programme field names Geomatics
  likely            a mentor's initials + surname match a supervisor on
                    the list (pre-2017 records have no Programme field)
  name collisions   surname matches but the initials say someone else

Hand verdicts go into scripts/verified_theses.yml (same format as for
scripts/find_missing_theses.py; entries with author+year there are never
reported again).

Usage:
  python3 scripts/find_old_theses.py              # search + fetch + report
  python3 scripts/find_old_theses.py --offline    # work from cache only
  python3 scripts/find_old_theses.py --add        # also append to archive
  python3 scripts/find_old_theses.py --all-years  # also list post-coverage
                                                  # search hits (no fetches)
  python3 scripts/find_old_theses.py --delay 5    # record fetch delay
"""

import argparse
import difflib
import json
import re
import sys
import time
import unicodedata
from datetime import datetime
from pathlib import Path

import requests
import yaml

import enrich_geotheses as eg

REPO_ROOT = Path(__file__).resolve().parent.parent
SUPERVISORS_FILE = REPO_ROOT / "scripts" / "geomatics_supervisors.yml"
VERIFIED_FILE = REPO_ROOT / "scripts" / "verified_theses.yml"
REPORT_FILE = REPO_ROOT / "old_theses_report.md"
SEARCH_API = "https://repository.tudelft.nl/search/data"
TUSS = {"van", "de", "den", "der", "ter", "te", "het", "'t"}
MAX_PAGES = 40  # per surname; 800 records is plenty for any one person


# ------------------------------------------------------------ supervisors

def load_supervisors():
    """(surname_key, display) for every status='yes' supervisor, plus the
    archive aliases' initial strings per key (e.g. ['me'] for
    'M.E. De Vries'), used for consistency checks."""
    supervisors = yaml.safe_load(SUPERVISORS_FILE.read_text())["supervisors"]
    keys, initials = {}, {}
    for entry in supervisors:
        if entry.get("status") != "yes":
            continue
        key = surname_key(entry["surname"])
        keys[key] = entry["surname"]
        for alias in entry.get("aliases", []):
            got = given_initials(alias)
            if got:
                initials.setdefault(key, set()).add(got)
    return keys, initials


def surname_key(surname):
    """Normalised matching key: fold case/accents (transliterating, like
    eg.foldcase -- ğ -> g), drop tussenvoegsels (the repository is
    inconsistent about them) and keep the last word."""
    tokens = surname.split()
    i = 0
    while i < len(tokens) - 1 and tokens[i].lower().strip("'") in TUSS:
        i += 1
    return eg.foldcase(tokens[-1])


def search_query(surname):
    """Search term for one supervisor: the surname minus tussenvoegsels."""
    tokens = [t for t in surname.split()
              if t.lower().strip("'") not in TUSS and not t.islower()]
    return tokens[-1] if len(tokens) == 1 else " ".join(tokens)


# ----------------------------------------------------------------- search

def search_surname(surname, offline):
    """All repository MSc theses matching the surname, via the search
    front-end's JSON API. Pages are cached under .geotheses_cache/ so runs
    resume (and repeat runs are free)."""
    query = search_query(surname)
    slug = re.sub(r"[^a-z0-9]+", "-", unicodedata.normalize(
        "NFKD", query).encode("ascii", "ignore").decode().lower()).strip("-")
    records = []
    for page in range(1, MAX_PAGES + 1):
        cache = eg.CACHE_DIR / f"oldsearch-{slug}-p{page}.json"
        if cache.exists():
            data = json.loads(cache.read_text())
        else:
            if offline:
                break
            try:
                r = requests.get(SEARCH_API,
                                 params={"search_term": query,
                                         "page": str(page),
                                         "sort": "relevance",
                                         "record_type": "master_thesis"},
                                 headers={"User-Agent": eg.USER_AGENT},
                                 timeout=60)
                data = r.json()
            except (requests.RequestException, ValueError) as e:
                print(f"    search {query} p{page}: {e}", flush=True)
                break
            eg.CACHE_DIR.mkdir(exist_ok=True)
            cache.write_text(json.dumps(data))
            time.sleep(2)
        records += data.get("records", [])
        total = int(data.get("total", 0))
        if len(data.get("records", [])) < 20 or page * 20 >= total:
            break
    return records


# --------------------------------------------------------------- matching

def contributor_surnames(record):
    """Normalised surnames of the record's contributors (mentors etc.)."""
    out = set()
    for person in record.get("contributors", []):
        key = surname_key(person.get("last_name") or "")
        if key:
            out.add(key)
    return out


def given_initials(full_name):
    """Ordered initials of 'B.G.H. Gorte' -> 'bgh'; 'Bert Gorte' -> 'b';
    '' when there is no given part."""
    tokens = full_name.replace(",", " ").split()
    if len(tokens) < 2:
        return ""
    first = tokens[0]
    if "." in first:
        return "".join(c.lower() for c in re.findall(r"[A-Za-z]", first))
    return first[0].lower()


def initials_consistent(initials, aliases):
    """True when the initials match some archive alias: same first
    initial, and no initial the alias does not have (records abbreviate
    'B.G.H.' to 'B.', they never extend it)."""
    if not initials:
        return True
    for want in aliases:
        if initials[0] == want[0] and all(c in want for c in initials):
            return True
    return False


def initials_match(mentor_name, aliases):
    return initials_consistent(given_initials(mentor_name), aliases)


def search_initials_match(record, initials):
    """True when some contributor with a list surname also has consistent
    initials (in the search data). Missing initials count as consistent;
    the record page is the real check."""
    for person in record.get("contributors", []):
        key = surname_key(person.get("last_name") or "")
        if key not in initials:
            continue
        got = given_initials((person.get("first_name") or "") + " "
                             + (person.get("last_name") or ""))
        if initials_consistent(got, initials[key]):
            return True
    return False


# --------------------------------------------------------------- classify

def load_verdicts():
    """(author surname, year) -> verdict from verified_theses.yml."""
    verdicts = {}
    if VERIFIED_FILE.exists():
        for v in yaml.safe_load(VERIFIED_FILE.read_text()) or []:
            author = v.get("author", "")
            surname = author.split()[-1] if author else ""
            verdicts[(eg.foldcase(surname), v.get("year"))] = \
                v.get("programme", "")
    return verdicts


def classify(theses, initials, verdicts):
    gaps, likely, collisions, verified_non = [], [], [], []
    for t in theses:
        verdict = verdicts.get((eg.foldcase(t["surname"]), t["year"]))
        if verdict == "Geomatics":
            gaps.append(t)
            continue
        if verdict and verdict != "Geomatics":
            verified_non.append(t)
            continue
        if t.get("programme") and "geomat" in t["programme"].lower():
            gaps.append(t)
            continue
        mentors = t.get("mentors", []) + t.get("coaches", [])
        match_names = {m.split()[-1] for m in mentors
                       if surname_key(m.split()[-1]) in initials
                       and initials_match(m, initials[surname_key(
                           m.split()[-1])])}
        if match_names or t.get("search_initials_ok"):
            likely.append(t)
        else:
            collisions.append(t)
    return gaps, likely, collisions, verified_non


# ----------------------------------------------------------------- report

def describe(t):
    lines = [f"- **{t['author']} ({t['year']})** — {t['title'] or '?'}"]
    if t.get("mentors") or t.get("coaches"):
        who = "; ".join(t.get("mentors", []) + t.get("coaches", []))
        lines.append(f"  - mentors/coaches: {who}")
    elif t.get("search_initials_ok"):
        lines.append("  - note: record page gave no mentor names; "
                     "initials matched in the search data only")
    if t.get("programme"):
        lines.append(f"  - programme: {t['programme']}")
    if t.get("matched"):
        lines.append(f"  - supervisor surnames on the record: "
                     f"{', '.join(sorted(t['matched']))}")
    if t.get("uuid"):
        lines.append(f"  - record: {eg.RESOLVER_URL.format(uuid=t['uuid'])}")
    return "\n".join(lines)


def write_report(gaps, likely, collisions, verified_non, n_archive,
                 n_matched, n_new, before_year, from_year, n_discarded,
                 extra_years):
    with REPORT_FILE.open("w", encoding="utf-8") as f:
        f.write(f"# Supervisor-search cross-check "
                f"({datetime.now():%Y-%m-%d})\n\n")
        f.write(f"The archive holds {n_archive} theses. Sweeping the "
                f"repository for MSc theses supervised by the surnames in "
                f"scripts/geomatics_supervisors.yml matched {n_matched} "
                f"theses, {n_new} of them from {from_year}–{before_year - 1} "
                f"and absent from the archive (another {n_discarded} from "
                f"before {from_year} were discarded).\n\n")
        f.write(f"## Confirmed gaps ({len(gaps)})\n\n"
                "The repository record's Programme field names Geomatics.\n\n")
        for t in gaps:
            f.write(describe(t) + "\n")
        f.write(f"\n## Likely ({len(likely)})\n\n"
                "Pre-2017 records have no Programme field; these have a "
                "mentor whose initials and surname match a supervisor on "
                "the list. Check the PDF title page.\n\n")
        for t in likely:
            f.write(describe(t) + "\n")
        f.write(f"\n## Name collisions ({len(collisions)})\n\n"
                "Same surname among the mentors, but the initials point "
                "to someone else (or no usable mentor name). Probably not "
                "ours, listed for completeness.\n\n")
        for t in collisions:
            f.write(describe(t) + "\n")
        if verified_non:
            f.write(f"\n## Verified non-Geomatics "
                    f"({len(verified_non)})\n\n"
                    "Already verdict-ed in scripts/verified_theses.yml.\n\n")
            for t in verified_non:
                f.write(describe(t) + "\n")
        if extra_years:
            f.write(f"\n## Post-{before_year - 1} search hits missing "
                    f"from the archive (no records fetched)\n\n")
            for t in extra_years:
                f.write(f"- {t['author']} ({t['year']}) — "
                        f"{(t['title'] or '')[:70]}"
                        f" [{', '.join(sorted(t['matched']))}]\n")


# ------------------------------------------------------------------- add

def append_theses(theses, args):
    """Append confirmed gaps + likely theses to the archive, enriched from
    the record page where possible; needs_review until a human confirms."""
    entries = yaml.safe_load((REPO_ROOT / "_data" / "geotheses.yml")
                             .read_text())
    known_uuids = {e.get("uuid") for e in entries if e.get("uuid")}
    added = 0
    for t in theses:
        if not t.get("uuid") or t["uuid"] in known_uuids:
            continue
        surname, given = eg.split_full_name(t["author"])
        entry = {"surname": surname, "name": " ".join(given),
                 "title": t["title"], "year": t["year"],
                 "needs_review": True}
        entry["link"] = eg.RESOLVER_URL.format(uuid=t["uuid"])
        entry["uuid"] = t["uuid"]
        sups = t.get("mentors") or t.get("coaches")
        if sups:
            entry["supervisors"] = "; ".join(sups)
        if t.get("abstract"):
            entry["abstract"] = t["abstract"]
        if t.get("graduation_date"):
            try:
                entry["graduation_date"] = datetime.strptime(
                    t["graduation_date"], "%d-%m-%Y").date().isoformat()
            except ValueError:
                entry["graduation_date"] = t["graduation_date"]
        entries.append(entry)
        known_uuids.add(t["uuid"])
        added += 1
        print(f"  appended: {t['author']} ({t['year']})")
    if added:
        eg.write_yaml(entries)
    return added


# ------------------------------------------------------------------ main

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--add", action="store_true",
                    help="append confirmed gaps + likely theses to "
                         "_data/geotheses.yml (flagged needs_review)")
    ap.add_argument("--offline", action="store_true",
                    help="work from the cache only, no network")
    ap.add_argument("--delay", type=float, default=20.0,
                    help="seconds between repository record fetches "
                         "(robots.txt asks for 20)")
    ap.add_argument("--before-year", type=int, default=2013,
                    help="target theses from before this year "
                         "(the archive's coverage; default 2013)")
    ap.add_argument("--from-year", type=int, default=2006,
                    help="discard theses from before this year "
                         "(default 2006)")
    ap.add_argument("--all-years", action="store_true",
                    help="also list post-coverage search hits (metadata "
                         "only, no record fetches)")
    args = ap.parse_args()

    keys, initials = load_supervisors()
    print(f"{len(keys)} supervisor surnames on the list.", flush=True)

    # stage 1: search API, cached per surname
    matched = {}  # uuid -> search record + matched surnames
    for i, (key, display) in enumerate(sorted(keys.items(), key=lambda kv: kv[1]), 1):
        records = search_surname(display, args.offline)
        for record in records:
            uuid = (record.get("id") or "").replace("Thing_", "")
            if not uuid:
                continue
            if contributor_surnames(record) & keys.keys():
                entry = matched.setdefault(uuid, dict(record, matched=set()))
                entry["matched"].add(display)
        print(f"[{i}/{len(keys)}] {display}: "
              f"{len(records)} MSc theses matched", flush=True)
    print(f"Unique MSc theses with a supervisor-list surname as "
          f"contributor: {len(matched)}", flush=True)

    # stage 2: keep the pre-coverage ones the archive does not have
    archive = yaml.safe_load((REPO_ROOT / "_data" / "geotheses.yml")
                             .read_text())
    archive_uuids = {e["uuid"] for e in archive if e.get("uuid")}
    archive_titles = {eg.foldcase(e.get("title") or "") for e in archive}
    theses, extra = [], []
    discarded = 0
    for uuid, record in matched.items():
        year = int(record.get("publication_year") or 0)
        title = record.get("title") or ""
        in_archive = uuid in archive_uuids or (
            bool(title) and eg.foldcase(title) in archive_titles) or (
            bool(title) and any(difflib.SequenceMatcher(
                None, eg.foldcase(title), t).ratio() > 0.93
                for t in archive_titles))
        if in_archive:
            continue
        if year and year < args.from_year:
            discarded += 1
            continue
        authors = record.get("authors", [])
        t = {"uuid": uuid, "title": title, "year": year,
             "matched": record["matched"],
             "surname": surname_key(authors[0].get("last_name") or "")
             if authors else "",
             "author": "; ".join(
                 (a.get("last_name") or "") + " " + (a.get("first_name") or "")
                 for a in authors) or "?",
             "search_initials_ok": search_initials_match(record, initials)}
        if year and year >= args.before_year:
            extra.append(t)
        else:
            theses.append(t)
    to_fetch = [t for t in theses if t["search_initials_ok"]]
    print(f"Before {args.before_year} and not in the archive: {len(theses)} "
          f"({len(to_fetch)} pass the initials pre-filter)", flush=True)

    # stage 3: record pages (cached, robots-delayed) for mentors/programme;
    # records that already failed the initials pre-filter are not fetched
    for i, t in enumerate(to_fetch, 1):
        page = eg.fetch_record(t["uuid"], args.delay, args.offline)
        if not page:
            continue
        rec = eg.parse_record(page)
        t.update({k: rec[k] for k in
                  ("mentors", "coaches", "programme", "graduation_date",
                   "abstract") if rec.get(k)})
        rec_authors = rec.get("authors")
        if rec_authors:
            t["author"] = rec_authors[0]
        if i % 25 == 0:
            print(f"  fetched {i}/{len(to_fetch)} record pages", flush=True)

    verdicts = load_verdicts()
    gaps, likely, collisions, verified_non = classify(
        theses, initials, verdicts)
    for group in (gaps, likely, collisions, verified_non):
        group.sort(key=lambda t: (t["year"], eg.foldcase(t["title"])))
    print(f"classified: {len(gaps)} confirmed gaps, {len(likely)} likely, "
          f"{len(collisions)} name collisions, "
          f"{len(verified_non)} verified non-Geomatics", flush=True)

    write_report(gaps, likely, collisions, verified_non, len(archive),
                 len(matched), len(theses), args.before_year,
                 args.from_year, discarded,
                 extra if args.all_years else [])
    print(f"Report written to {REPORT_FILE}", flush=True)

    if args.add:
        added = append_theses(gaps + likely, args)
        print(f"Appended {added} theses to the archive "
              "(flagged needs_review).", flush=True)
        return 0
    return 1 if gaps else 0


if __name__ == "__main__":
    sys.exit(main())
