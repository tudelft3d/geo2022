#!/usr/bin/env python3
"""Clean and enrich the completed-thesis archive data (_data/geotheses.yml).

Three stages, all idempotent, so the script can be re-run at any time:

  clean   rule-based fixes on the YAML: strip the "missing " prefixes from
          links, fold the stray "van:" field into the surname, move trailing
          tussenvoegsels from given names into surnames, and canonicalise
          repository links to https://resolver.tudelft.nl/uuid:<uuid>
  fetch   download each thesis's repository record page (respecting the
          repository's robots.txt crawl-delay) into a gitignored cache;
          already-cached records are never re-fetched, so runs resume
  merge   parse the cached record pages and add title/author/abstract/
          supervisors/graduation date from the finished thesis, fill gaps
          from MyCase's closed cases (never grades or student numbers),
          fix swapped name fields against the repository's author string,
          and append closed MyCase cases that are missing from the archive
          (flagged needs_review)

Output: the rewritten _data/geotheses.yml (a backup of the original is kept
at geotheses.yml.original on first run) and a human-readable
geotheses_report.md listing everything that needs a manual look.

Usage:
  python3 scripts/enrich_geotheses.py              # fetch (if needed) + merge
  python3 scripts/enrich_geotheses.py --offline    # merge from cache only
  python3 scripts/enrich_geotheses.py --fetch-only # only download records
  python3 scripts/enrich_geotheses.py --delay 5    # override crawl delay (s)
"""

import argparse
import csv
import html
import re
import sys
import time
import unicodedata
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote, urlparse

import requests
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = REPO_ROOT / "_data" / "geotheses.yml"
BACKUP_FILE = REPO_ROOT / "geotheses.yml.original"
CACHE_DIR = REPO_ROOT / ".geotheses_cache"
REPORT_FILE = REPO_ROOT / "geotheses_report.md"
MYCASE_CSV = REPO_ROOT / "mycase" / "mycase_index.csv"

RECORD_URL = "https://repository.tudelft.nl/record/uuid:{uuid}"
RESOLVER_URL = "https://resolver.tudelft.nl/uuid:{uuid}"
USER_AGENT = ("geo2022-site-maintainer/1.0 "
              "(https://geomatics.bk.tudelft.nl/geo2022/; one-off metadata "
              "sync for the thesis archive, honors robots.txt)")

TUSS_ENVGESELLS = ("van ", "de ", "den ", "der ", "ter ", "te ", "het ", "'t ")
FIELD_ORDER = ["surname", "name", "title", "supervisors", "year",
               "graduation_date", "link", "image", "github", "paper",
               "abstract", "uuid", "needs_review"]


# ---------------------------------------------------------------- cleaning

def canonicalise_link(link):
    """Return (canonical_url, uuid). Outlook safelinks are unwrapped, and
    repository record/islandora/resolver links become resolver URLs;
    anything else is returned unchanged."""
    if not link:
        return "", None
    url = unquote(link.strip())
    # Outlook "safe links" carry the real URL in their query string.
    if "safelinks.protection.outlook.com" in url:
        m = re.search(r"[?&]url=([^&]+)", url)
        if m:
            url = unquote(m.group(1))
    m = re.search(r"uuid[:%3A]+([0-9a-fA-F-]{36})", url)
    if not m:
        return url, None
    uuid = m.group(1).lower()
    host = urlparse(url).netloc
    if host in ("resolver.tudelft.nl", "repository.tudelft.nl",
                "repository.tudelft.nl:443"):
        return RESOLVER_URL.format(uuid=uuid), uuid
    return url, uuid


def clean_entry(entry, issues):
    """Rule-based fixes on one entry. Returns (entry, uuid)."""
    entry = dict(entry)

    # "link: missing https://..." notes left by the student assistant.
    link = str(entry.get("link", "")).strip()
    if link.startswith("missing"):
        rest = link[len("missing"):].strip()
        if rest:
            entry["link"] = rest
            issues.append(f"{entry.get('surname')}: unverified link kept "
                          f"from 'missing' note: {rest}")
        else:
            entry.pop("link", None)
            issues.append(f"{entry.get('surname')}: no link at all "
                          "(was 'missing')")

    # "surname: Duijn / van: den" -> "van den Duijn".
    van = entry.pop("van", None)
    if van:
        entry["surname"] = f"{van} {entry['surname']}"
        issues.append(f"{entry['surname']}: folded 'van:' field into surname")

    # "name: Marieke van" + "surname: Arnhem" -> "Marieke" / "van Arnhem".
    name, surname = entry.get("name", ""), entry.get("surname", "")
    for tuss in TUSS_ENVGESELLS:
        if name.lower().endswith(" " + tuss.strip()) and \
                not surname.lower().startswith(tuss):
            entry["name"] = name[: -len(tuss)].rstrip()
            entry["surname"] = f"{tuss}{surname}"
            issues.append(f"{entry['surname']}: moved tussenvoegsel from "
                          "given name into surname")
            break

    link, uuid = canonicalise_link(entry.get("link", ""))
    if link != str(entry.get("link", "")):
        entry["link"] = link
    if uuid:
        entry["uuid"] = uuid

    entry.pop("swapnames", None)  # resolved against the record in merge()
    return entry, uuid


# ------------------------------------------------------------------ record

def fetch_record(uuid, delay, offline):
    """Download (or load from cache) one record page. Returns HTML or None."""
    cache = CACHE_DIR / f"{uuid}.html"
    if cache.exists():
        return cache.read_text(encoding="utf-8", errors="replace")
    if offline:
        return None
    CACHE_DIR.mkdir(exist_ok=True)
    for attempt in (1, 2):
        try:
            r = requests.get(RECORD_URL.format(uuid=uuid),
                             headers={"User-Agent": USER_AGENT}, timeout=60)
        except requests.RequestException as e:
            print(f"    fetch {uuid}: {e}", flush=True)
            time.sleep(delay)
            continue
        if r.status_code == 200 and "Something went wrong" not in r.text:
            cache.write_text(r.text, encoding="utf-8")
            time.sleep(delay)
            return r.text
        print(f"    fetch {uuid}: HTTP {r.status_code} "
              f"(attempt {attempt})", flush=True)
        time.sleep(delay)
    return None


def names_in(section_html):
    """Extract 'name [– role] [(faculty)]' <p> blocks from a record section.
    Names are either links or greyed-out spans (revoked accounts)."""
    out = []
    for p in re.findall(r"<p>(.*?)</p>", section_html, re.S):
        m = (re.search(r'<a href="/person/[^"]*"[^>]*>\s*([^<]+?)\s*</a>', p)
             or re.search(r'<span[^>]*tabindex="-1"[^>]*>\s*([^<]+?)\s*</span>', p))
        if not m:
            continue
        who = re.sub(r"\s+", " ", html.unescape(m.group(1))).strip()
        role_m = re.search(r"–\s*([A-Za-z][A-Za-z /-]*)", p)
        role = re.sub(r"\s+", " ", html.unescape(role_m.group(1))).strip() \
            if role_m else ""
        out.append((who, role))
    return out


def section(html, start_label, end_labels):
    i = html.find(start_label)
    if i < 0:
        return ""
    j = len(html)
    for end in end_labels:
        k = html.find(end, i + len(start_label))
        if k >= 0:
            j = min(j, k)
    return html[i:j]


def parse_record(page):
    """Extract the fields we publish from a record page."""
    rec = {}

    m = re.search(r"<h1>(.*?)</h1>", page, re.S)
    if m:
        rec["title"] = re.sub(r"\s+", " ", html.unescape(m.group(1))).strip()
    m = re.search(r'<h3 class="mt-2 font-bold">(.*?)</h3>', page, re.S)
    if m:
        rec["subtitle"] = re.sub(r"\s+", " ",
                                 html.unescape(m.group(1))).strip()

    rec["authors"] = [who for who, _ in names_in(
        section(page, "<div>Author(s)</div>", ["<div>Contributor(s)</div>",
                                               "<div>Faculty</div>"]))]

    contributors = names_in(section(
        page, "<div>Contributor(s)</div>",
        ["<div>Faculty</div>", "<div>Copyright</div>",
         "To reference this document use"]))
    rec["mentors"] = [who for who, role in contributors
                      if role.lower().startswith("mentor")]
    rec["coaches"] = [who for who, role in contributors
                      if role.lower().startswith("coach")]

    for field, label in [("graduation_date", "Graduation Date"),
                         ("publication_year", "Publication Year"),
                         ("programme", "Programme")]:
        m = re.search(rf'<div class="text-black font-bold">{label}</div>\s*'
                      rf"([^<]+)", page)
        if m:
            rec[field] = m.group(1).strip()

    m = re.search(r'<div id="abstract"[^>]*>\s*<h2>Abstract</h2>(.*?)</div>',
                  page, re.S)
    if m:
        paras = re.findall(r"<p>(.*?)</p>", m.group(1), re.S)
        text = "\n\n".join(
            re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", p)).strip()
            for p in paras)
        rec["abstract"] = html.unescape(text).strip()
    return rec


# ----------------------------------------------------------------- mycase

_STROKE_CHARS = str.maketrans({"ł": "l", "Ł": "L", "ø": "o", "Ø": "O",
                               "đ": "d", "Đ": "D", "ð": "d", "Ð": "D"})


def foldcase(s):
    s = unicodedata.normalize("NFKD", s).translate(_STROKE_CHARS)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]", "", s.lower())


def strip_tussenvoegsel(surname):
    return re.sub(r"^(van|de|den|der|ter|te|het|'t) ", "", surname or "",
                  flags=re.IGNORECASE)


def split_full_name(display_name):
    """'Segher ter Braak' -> ('ter Braak', ['Segher']); the last token is
    the surname unless it is preceded by a tussenvoegsel."""
    tokens = display_name.strip().split()
    surname = [tokens[-1]] if tokens else []
    i = len(tokens) - 2
    while i >= 0 and tokens[i].lower() in (
            "van", "de", "den", "der", "ter", "te", "het", "'t"):
        surname.insert(0, tokens[i])
        i -= 1
    return " ".join(surname), tokens[:i + 1]


def initials(given_tokens):
    return [foldcase(g)[:1] for g in given_tokens if foldcase(g)]


def names_match(entry, mycase_row):
    """Tolerant match between an archive entry and a MyCase student name:
    same core surname plus a first-initial overlap handles 'R.M. Aalders'
    vs 'Rian Aalders' and 'Carmem Aires' vs 'Carmem Félix Aires'; a full
    containment handles doubled/extra tokens such as 'Derian Der Derian
    Auliyaa Bainus'."""
    surname, given = split_full_name(mycase_row)
    surname_k = foldcase(strip_tussenvoegsel(surname))
    own_surname_k = foldcase(strip_tussenvoegsel(entry.get("surname", "")))
    own_given = [g for g in re.split(r"[\s.]+",
                 (entry.get("name") or "").strip()) if g]

    if surname_k and surname_k == own_surname_k:
        mine = set(initials(given)) & set(initials(own_given))
        if mine or not initials(given) or not initials(own_given):
            return True

    full_mine = foldcase(mycase_row)
    full_own = foldcase(f"{entry.get('name', '')} "
                        f"{entry.get('surname', '')}")
    if len(full_own) >= 10 and (full_own == full_mine
                                or full_own in full_mine
                                or full_mine in full_own):
        return True

    # Some display names put the family name mid-string (e.g. MyCase's
    # "Shawn Roy Tew How Wei" for family name Tew): accept when the entry
    # surname appears as a token and a given-name initial matches too.
    row_tokens = [foldcase(t) for t in mycase_row.split() if foldcase(t)]
    own_surname_t = foldcase(strip_tussenvoegsel(entry.get("surname", "")))
    if len(own_surname_t) >= 3 and own_surname_t in row_tokens:
        row_initials = {t[:1] for t in row_tokens}
        if set(initials(own_given)) & row_initials:
            return True
    return False


def mycase_closed():
    if not MYCASE_CSV.exists():
        return []
    with MYCASE_CSV.open(encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if r["status"] == "closed"]


def mycase_supervisors(row):
    names = []
    for field in ("supervisor_1", "supervisor_2"):
        for n in (row.get(field) or "").split(";"):
            n = n.strip()
            if n and n not in names:
                names.append(n)
    return "; ".join(names)


# ------------------------------------------------------------------- main

def write_yaml(entries):
    def sort_key(e):
        return (-int(e.get("year") or 0), foldcase(e.get("surname", "")),
                foldcase(e.get("name", "")))

    ordered = []
    for e in sorted(entries, key=sort_key):
        clean = {}
        for field in FIELD_ORDER:
            if field in e and e[field] not in (None, ""):
                clean[field] = e[field]
        for extra in sorted(k for k in e if k not in FIELD_ORDER):
            clean[extra] = e[extra]
        ordered.append(clean)

    header = ("# Completed MSc Geomatics theses, newest first.\n"
              "# name/surname as on the thesis record page; supervisors and\n"
              "# abstract from the finished thesis (repository record), not\n"
              "# the proposal. Maintain by hand or via\n"
              "# scripts/enrich_geotheses.py; validate with\n"
              "# scripts/check_geotheses.py.\n")
    body = yaml.safe_dump(ordered, allow_unicode=True, width=72,
                          sort_keys=False, default_flow_style=False)
    DATA_FILE.write_text(header + body, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--offline", action="store_true",
                    help="merge from cached records only, no network")
    ap.add_argument("--adopt-record-titles", action="store_true",
                    help="replace entry titles with the repository's "
                         "title (+ ': ' + subtitle) where they differ")
    ap.add_argument("--fetch-only", action="store_true",
                    help="download record pages, skip cleaning and merging")
    ap.add_argument("--delay", type=float, default=20.0,
                    help="seconds between record fetches "
                         "(repository robots.txt asks for 20)")
    ap.add_argument("--limit", type=int, default=None,
                    help="only process the first N entries (testing)")
    args = ap.parse_args()

    entries = yaml.safe_load(DATA_FILE.read_text())
    if args.fetch_only:
        entries = [{**e} for e in entries]
        todo = []
        for e in entries:
            _, uuid = canonicalise_link(str(e.get("link", "")))
            if uuid and not (CACHE_DIR / f"{uuid}.html").exists():
                todo.append(uuid)
        if args.limit:
            todo = todo[: args.limit]
        print(f"{len(todo)} record(s) to fetch, {args.delay}s apart.")
        for i, uuid in enumerate(todo, 1):
            print(f"[{i}/{len(todo)}] {uuid}", flush=True)
            fetch_record(uuid, args.delay, offline=False)
        print("Done fetching.")
        return 0

    issues, reports = [], []
    cleaned = []
    for e in entries:
        e, uuid = clean_entry(e, issues)
        cleaned.append(e)

    for idx, e in enumerate(cleaned, 1):
        uuid = e.get("uuid")
        if not uuid:
            continue
        if args.limit and idx > args.limit:
            break
        html = fetch_record(uuid, args.delay, args.offline)
        if not html:
            reports.append(f"NO RECORD PAGE: {e.get('surname')} "
                           f"({e.get('year')}) uuid={uuid}")
            continue
        rec = parse_record(html)
        e["_rec"] = rec

    # --- merge repository data into the entries
    stats = {"abstract": 0, "supervisors": 0, "graduation_date": 0}
    for e in cleaned:
        rec = e.pop("_rec", None)
        if not rec:
            continue
        label = f"{e.get('surname')} ({e.get('year')})"

        if rec.get("title"):
            ours = re.sub(r"\s+", " ", str(e.get("title", ""))).strip()
            theirs = rec["title"] + (": " + rec["subtitle"]
                                     if rec.get("subtitle") and
                                     rec["subtitle"] not in ours else "")
            if ours.lower() != theirs.lower() and \
                    rec["title"].lower() not in ours.lower():
                if args.adopt_record_titles:
                    e["title"] = theirs
                    reports.append(f"TITLE ADOPTED from record: {label}")
                else:
                    reports.append(f"TITLE DIFFERS: {label}\n"
                                   f"    yaml: {ours}\n    repo: {theirs}")

        if rec.get("programme") and "geomatics" not in \
                rec["programme"].lower():
            reports.append(f"PROGRAMME NOT GEOMATICS: {label} -> "
                           f"{rec['programme']}")

        author = (rec.get("authors") or [""])[0]
        if author and e.get("name") and e.get("surname"):
            same_order = foldcase(author) == foldcase(
                f"{e['name']} {e['surname']}")
            swapped = foldcase(author) == foldcase(
                f"{e['surname']} {e['name']}")
            if swapped and not same_order:
                e["name"], e["surname"] = e["surname"], e["name"]
                reports.append(f"NAME ORDER FIXED from record: "
                               f"{label} -> {author}")
            elif not same_order and not names_match(e, author):
                reports.append(f"NAME CHECK: {label}\n"
                               f"    yaml: {e['name']} {e['surname']}\n"
                               f"    repo: {author}")

        if not e.get("abstract") and rec.get("abstract"):
            e["abstract"] = rec["abstract"]
            stats["abstract"] += 1
        if not e.get("supervisors"):
            sups = rec.get("mentors") or rec.get("coaches")
            if sups:
                e["supervisors"] = "; ".join(sups)
                if not rec.get("mentors"):
                    reports.append(f"SUPERVISORS FROM COACHES (no mentor on "
                                   f"record): {label}")
                stats["supervisors"] += 1
        if not e.get("graduation_date"):
            gd = rec.get("graduation_date")
            if gd:
                try:
                    e["graduation_date"] = datetime.strptime(
                        gd, "%d-%m-%Y").date().isoformat()
                except ValueError:
                    e["graduation_date"] = gd
                stats["graduation_date"] += 1

    # --- fill gaps from MyCase (closed cases only, public fields only)
    closed = mycase_closed()
    used_cases = set()
    for e in cleaned:
        for i, row in enumerate(closed):
            if i in used_cases:
                continue
            if names_match(e, row["student_name"]):
                used_cases.add(i)
                if not e.get("supervisors") and row.get("supervisor_1"):
                    e["supervisors"] = mycase_supervisors(row)
                    stats["supervisors"] += 1
                    reports.append(f"SUPERVISORS FROM MYCASE: "
                                   f"{e.get('surname')} ({e.get('year')})")
                if not e.get("graduation_date") and \
                        row.get("finalisation_date"):
                    e["graduation_date"] = row["finalisation_date"]
                break

    appended = []
    for i, row in enumerate(closed):
        if i in used_cases:
            continue
        year = (row.get("finalisation_date") or "")[:4]
        surname, given = split_full_name(row["student_name"])
        entry = {
            "surname": surname,
            "name": " ".join(given),
            "title": row.get("thesis_title", ""),
            "year": int(year) if year.isdigit() else None,
            "needs_review": True,
        }
        link, uuid = canonicalise_link(row.get("repository_link", ""))
        if link:
            entry["link"], entry["uuid"] = link, uuid
        if row.get("supervisor_1"):
            entry["supervisors"] = mycase_supervisors(row)
        appended.append(entry)
        cleaned.append(entry)
        reports.append(f"APPENDED FROM MYCASE (not in archive before): "
                       f"{row['student_name']} ({year}) "
                       f"{row.get('thesis_title', '')}")

    # --- write everything back
    if not BACKUP_FILE.exists():
        BACKUP_FILE.write_text(DATA_FILE.read_text())
        print(f"Original kept at {BACKUP_FILE.name}")

    output = [dict(e) for e in cleaned if not e.pop("_rec", None)]
    write_yaml(output)

    with REPORT_FILE.open("w", encoding="utf-8") as f:
        f.write(f"# geotheses enrichment report ({datetime.now():%Y-%m-%d})\n\n")
        f.write(f"{len(output)} entries written to _data/geotheses.yml.\n\n")
        f.write(f"Enriched from repository records: abstracts "
                f"{stats['abstract']}, supervisors {stats['supervisors']}, "
                f"graduation dates {stats['graduation_date']}.\n")
        f.write(f"{len(appended)} entries appended from MyCase "
                "(needs_review: true).\n\n## Needs a manual look\n\n")
        for line in issues + reports:
            f.write(f"- {line}\n")
    print(f"Wrote {DATA_FILE.name} ({len(output)} entries) and "
          f"{REPORT_FILE.name}; {len(issues) + len(reports)} note(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
