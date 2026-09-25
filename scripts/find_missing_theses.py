#!/usr/bin/env python3
"""Cross-check the completed-thesis archive against external thesis lists.

Compares every MSc thesis on the two external lists that cover Geomatics
graduates -- the 3D geoinformation group's education page
(https://3d.bk.tudelft.nl/education/, section "MSc thesis projects –
Completed") and the GDMC publication list
(https://www.gdmc.nl/publications/pubs.php) -- against _data/geotheses.yml
and investigates the theses the archive is missing.

Evidence used to classify an uncovered thesis, most reliable first:

  1. GDMC's citation names the thesis's programme ("Master's thesis,
     Geomatics, ..."); only its post-2017 entries are explicit.
  2. The repository record's Programme field (2017+ records only; older
     records migrated from the previous repository have no Programme).
  3. The thesis PDF's title page ("Master of Science in Geomatics"),
     which GDMC hosts for most of its theses. A passing mention of
     Geomatics in the PDF text is noted as a hint, not as evidence.

A thesis with decisive Geomatics evidence is a confirmed gap; one whose
record/PDF names another programme (GIMA, AUBS, remote sensing, ...) is a
verified non-Geomatics thesis; anything still undecided is a candidate
for a manual look. Theses from before --from-year (default: 2013, where
the archive starts) are skipped, and GIMA theses are never gaps by
definition: the archive covers the MSc Geomatics programme only.

Output: missing_theses_report.md at the repo root and a console summary.
Exit status is 1 while confirmed gaps remain, 2 when a source page could
not be parsed (so silent breakage of the two external pages is noticed).

Usage:
  python3 scripts/find_missing_theses.py               # check + investigate
  python3 scripts/find_missing_theses.py --add         # also append confirmed gaps to the archive
  python3 scripts/find_missing_theses.py --offline     # investigate from cache only
  python3 scripts/find_missing_theses.py --delay 5     # repository fetch delay override
  python3 scripts/find_missing_theses.py --no-pdf      # skip the (large) PDF downloads
"""

import argparse
import difflib
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import requests
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import enrich_geotheses as eg  # noqa: E402  (shared helpers)

REPO_ROOT = eg.REPO_ROOT
REPORT_FILE = REPO_ROOT / "missing_theses_report.md"

GDMC_URL = "https://www.gdmc.nl/publications/pubs.php"
THREE_DGE_URL = "https://3d.bk.tudelft.nl/education/"
SEARCH_API = "https://repository.tudelft.nl/search/data"

# Cache files in eg.CACHE_DIR (gitignored): the two source pages and the
# extracted title-page text of the thesis PDFs (the PDFs themselves are
# large, so only the text is kept).
SRC_GDMC = "src-gdmc-pubs.html"
SRC_3DGE = "src-3dge-education.html"
PDF_TEXT = "pdftext-{slug}.txt"

# Programmes that GDMC/3D-geo theses name instead of Geomatics; used to
# label verified non-Geomatics theses when no repository record exists.
OTHER_PROGRAMMES = ("GIMA", "Urbanism", "Building Technology", "MADE",
                    "Remote Sensing", "Mechanical Engineering",
                    "Construction Management", "Applied Earth Sciences",
                    "Sustainable Energy", "Science Communication",
                    "Complex Systems")


# ---------------------------------------------------------------- sources

def http_get(url, timeout=120):
    r = requests.get(url, headers={"User-Agent": eg.USER_AGENT},
                     timeout=timeout)
    r.raise_for_status()
    return r.content


def load_source(url, cache_name, offline):
    """Fetch (or load from cache) one external source page. The GDMC page
    declares ISO-8859-1 but serves UTF-8, so decode as UTF-8 leniently."""
    cache = eg.CACHE_DIR / cache_name
    if cache.exists():
        return cache.read_text(encoding="utf-8", errors="replace")
    if offline:
        return None
    text = http_get(url).decode("utf-8", errors="replace")
    eg.CACHE_DIR.mkdir(exist_ok=True)
    cache.write_text(text, encoding="utf-8")
    return text


def parse_gdmc(text):
    """All MSc theses in the GDMC publication list, all years."""
    theses, year, section = [], None, None
    pat = re.compile(r'<h2>(\d{4})</h2>|<h3>(.*?)</h3>'
                     r'|<li class="bibline">(.*?)(?=<li class="bibline">'
                     r"|<div id='toggle)", re.S)
    for m in pat.finditer(text):
        if m.group(1):
            year = int(m.group(1))
        elif m.group(2) is not None:
            section = m.group(2)
        elif section == "MSc Thesis":
            blk = m.group(3)
            nm = re.match(r'(?:<a class="bibanchor" id="[^"]*"></a>)?'
                          r'(.*?),\s*<span class="bibtitle">', blk, re.S)
            if not nm:
                continue
            author = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "",
                                                nm.group(1))).strip()
            tt = re.search(r'<span class="bibtitle">(.*?)</span>', blk, re.S)
            title = re.sub(r"\s+", " ", tt.group(1)).strip() if tt else ""
            school = ""
            ms = re.search(r"Master's thesis,(.*?)\s*,\s*((?:19|20)\d\d)\s*\.",
                           blk, re.S)
            if ms:
                school = re.sub(r",?\s+pp\. \d+$", "",
                                " ".join(ms.group(1).split())).strip()
            u = re.search(r'href="https?://resolver\.tudelft\.nl/uuid:'
                          r'([0-9a-fA-F-]{36})"', blk)
            pdf = re.search(r'href="(//www\.gdmc\.nl/publications/[^"]+\.pdf)"',
                            blk)
            theses.append({"author": author, "title": title, "year": year,
                           "school": school,
                           "uuid": u.group(1).lower() if u else "",
                           "pdf": ("https:" + pdf.group(1)) if pdf else ""})
    return theses


def parse_3dge(text):
    """All completed MSc theses on the 3dge education page."""
    start = text.find("msc-thesis-projects--completed")
    if start < 0:
        return []
    theses = []
    for m in re.finditer(r"<h3>\s*(\d{4})\s*</h3>"
                         r"(.*?)(?=<h3>\s*\d{4}\s*</h3>|\Z)",
                         text[start:], re.S):
        year, body = int(m.group(1)), m.group(2)
        for e in re.finditer(r'<div class="media">(.*?)'
                             r"(?=<div class=\"media\">|\Z)", body, re.S):
            blk = e.group(1)
            nm = re.search(r'<h4 class="media-heading">\s*(.*?)\s*</h4>',
                           blk, re.S)
            if not nm:
                continue
            author = re.sub(r"\s+", " ", nm.group(1)).strip()
            ti = re.search(r"</h4>\s*(.*?)\s*(?:<br|\Z)", blk, re.S)
            title = re.sub(r"\s+", " ", ti.group(1)).strip() if ti else ""
            u = re.search(r"uuid[:%3A]+([0-9a-fA-F-]{36})", blk)
            theses.append({"author": author, "title": title, "year": year,
                           "school": "",
                           "uuid": u.group(1).lower() if u else "",
                           "pdf": ""})
    return theses


# --------------------------------------------------------------- matching

def find_in_archive(archive, thesis):
    """Return (entry, basis) for the archive entry covering this thesis,
    or (None, None). Basis is 'uuid' or 'name'."""
    if thesis["uuid"]:
        for e in archive:
            if e.get("uuid") == thesis["uuid"]:
                return e, "uuid"
    cands = [e for e in archive
             if abs(int(e.get("year") or 0) - thesis["year"]) <= 1]
    for e in cands:
        if eg.names_match(e, thesis["author"]):
            return e, "name"
    # last resort: any-year full-name containment (odd name orders) and
    # exact family-name-first matches ("Xu Weilin" for Weilin Xu), which
    # names_match deliberately does not attempt for short surnames
    full_b = eg.foldcase(thesis["author"])
    for e in archive:
        full_a = eg.foldcase(f"{e.get('name', '')} {e.get('surname', '')}")
        swapped = eg.foldcase(f"{e.get('surname', '')} {e.get('name', '')}")
        if len(full_a) >= 10 and (full_a == full_b or full_a in full_b
                                  or full_b in full_a):
            return e, "name"
        if swapped and swapped == full_b:
            return e, "name"
    return None, None


# --------------------------------------------------------------- evidence

def repository_programme(uuid, delay, offline):
    """(programme, record title). Programme is '' when the record has no
    Programme field (pre-2017 records) and both are ''/None when there is
    no usable record."""
    page = eg.fetch_record(uuid, delay, offline)
    if not page:
        return None, None
    rec = eg.parse_record(page)
    return rec.get("programme", ""), rec.get("title", "")


def search_repository_uuid(title, author, year, offline):
    """Find a repository uuid by title via the search front-end's JSON API
    (the repository has no programme filter, so this is only used to
    locate records of uncovered theses that lack a uuid on the source
    pages). Results (including misses) are cached so offline runs reuse
    them."""
    slug = eg.foldcase(f"{author} {year}")
    cache = eg.CACHE_DIR / f"search-{slug}.txt"
    if cache.exists():
        return cache.read_text(encoding="utf-8").strip() or None
    if offline or not title:
        return None
    try:
        r = requests.get(SEARCH_API,
                         params={"search_term": '"%s"' % title[:70],
                                 "page": "1", "sort": "relevance"},
                         headers={"User-Agent": eg.USER_AGENT}, timeout=60)
        hits = r.json().get("records", [])
    except Exception as e:
        print(f"    search API: {e}", flush=True)
        return None
    time.sleep(2)
    best, score = None, 0.0
    for hit in hits[:6]:
        ratio = difflib.SequenceMatcher(
            None, (hit.get("title") or "").lower(), title.lower()).ratio()
        if ratio > score:
            best, score = hit, ratio
    uuid = ""
    if best and score > 0.55 and best.get("id", "").startswith("Thing_"):
        uuid = best["id"][len("Thing_"):].lower()
    eg.CACHE_DIR.mkdir(exist_ok=True)
    cache.write_text(uuid, encoding="utf-8")
    return uuid or None


def pdf_programme(pdf_url, author, year, offline):
    """(programme named on the thesis PDF's title pages, mentions
    geomatics anywhere in them). programme is '' when the title pages
    name no programme, and both are None, None when the PDF could not be
    read. The extracted text is cached so the (large) PDFs are downloaded
    only once."""
    if not pdf_url:
        return None, None
    slug = eg.foldcase(f"{author} {year}")
    cache = eg.CACHE_DIR / PDF_TEXT.format(slug=slug)
    if cache.exists():
        text = cache.read_text(encoding="utf-8", errors="replace")
    elif offline:
        return None, None
    else:
        try:
            import io
            import pypdf
            reader = pypdf.PdfReader(io.BytesIO(http_get(pdf_url)))
            text = re.sub(r"\s+", " ", " ".join(
                reader.pages[i].extract_text() or ""
                for i in range(min(8, len(reader.pages)))))
        except Exception as e:
            print(f"    pdf {pdf_url}: {e}", flush=True)
            return None, None
        eg.CACHE_DIR.mkdir(exist_ok=True)
        cache.write_text(text, encoding="utf-8")
    m = re.search(r"[Mm]aster of [Ss]cience in ([A-Za-z][A-Za-z ,&/+]{2,60})"
                  r"|[Mm]Sc\.? (?:in |of )?([A-Z][A-Za-z ,&/+]{2,60})", text)
    named = ""
    if m:
        named = (m.group(1) or m.group(2)).strip(" ,.&")
        named = re.split(r"\s+by\s+|\s+[Tt]hesis\s+|\s+degree\b", named)[0]
    return named, bool(re.search(r"[Gg]eomatics", text))


# ------------------------------------------------------------------- main

def investigate(t, args):
    """Set t['evidence'] and return 'gap', 'non' or 'cand'."""
    evidence = []
    school = t.get("school", "")
    verdict = None
    if "geomatic" in school.lower():
        verdict = "gap"
        evidence.append(f"GDMC names the programme: {school}")
    elif any(p.lower() in school.lower() for p in OTHER_PROGRAMMES):
        verdict = "non"
        evidence.append(f"GDMC names the programme: {school}")

    if verdict is None:
        uuid = t["uuid"]
        if not uuid:
            uuid = search_repository_uuid(t["title"], t["author"],
                                          t["year"], args.offline)
            if uuid:
                evidence.append(f"repository record found by title search: "
                                f"{eg.RESOLVER_URL.format(uuid=uuid)}")
        prog, _ = (repository_programme(uuid, args.delay, args.offline)
                   if uuid else (None, None))
        if prog is None:
            evidence.append("no repository record found")
        elif prog == "":
            evidence.append("repository record has no Programme field "
                            "(older, migrated record)")
        elif "geomatic" in prog.lower():
            verdict = "gap"
            evidence.append(f"repository Programme: {prog}")
        else:
            verdict = "non"
            evidence.append(f"repository Programme: {prog}")

        if verdict is None and not args.no_pdf:
            named, mentions = pdf_programme(t.get("pdf", ""), t["author"],
                                            t["year"], args.offline)
            if named is None:
                if t.get("pdf"):
                    evidence.append("thesis PDF could not be read")
            else:
                # the capture picks up what follows the programme on the
                # title page ("Geomatics by Ada Lovelace June 2016",
                # all-caps thesis titles, ...), so trim it
                clean = re.split(r"\s+by\s+|\s+at the\s+|\s+for the\s+"
                                 r"|\s+[Tt]hesis\s+|\s+degree\b|,\s+",
                                 named)[0].strip(" ,.&")
                if clean.lower().startswith("geomatics"):
                    verdict = "gap"
                    evidence.append("thesis PDF title page: Master of "
                                    "Science in Geomatics")
                elif clean:
                    verdict = "non"
                    evidence.append(f"thesis PDF title page names: {clean}")
                elif mentions:
                    evidence.append("thesis PDF mentions Geomatics but its "
                                    "title pages name no programme")
                elif t.get("pdf"):
                    evidence.append("thesis PDF names no recognisable "
                                    "programme on its title pages")

    if "3dge" in t["sources"]:
        evidence.append("listed on 3d.bk.tudelft.nl")
    if t.get("pdf"):
        evidence.append(f"pdf: {t['pdf']}")
    if t["uuid"]:
        evidence.append(f"record: {eg.RESOLVER_URL.format(uuid=t['uuid'])}")
    t["evidence"] = evidence
    return verdict or "cand"


def describe(t):
    lines = [f"- **{t['author']} ({t['year']})** — "
             f"{t['title'] or '(no title on the source page)'}"]
    lines += [f"  - {e}" for e in t["evidence"]]
    return "\n".join(lines)


def write_report(gaps, candidates, non_geo, covered_name, n_archive,
                 n_theses, from_year, skipped_old):
    with REPORT_FILE.open("w", encoding="utf-8") as f:
        f.write(f"# External-source cross-check "
                f"({datetime.now():%Y-%m-%d})\n\n")
        f.write(f"The archive holds {n_archive} theses; the GDMC and "
                f"3d.bk.tudelft.nl lists together cover {n_theses} MSc "
                f"theses from {from_year} onwards"
                f"{f' ({skipped_old} earlier ones ignored)' if skipped_old else ''}.\n\n")
        f.write(f"## Confirmed gaps ({len(gaps)})\n\n"
                "Geomatics theses on the external lists that the archive "
                "is missing.\n\n")
        if not gaps:
            f.write("None — the archive covers every thesis the sources "
                    "identify as Geomatics.\n")
        for t in gaps:
            f.write(describe(t) + "\n")
        f.write(f"\n## Candidates for a manual look ({len(candidates)})\n\n"
                "No source names a programme; most are pre-2017, when "
                "repository records still had no Programme field. Check "
                "the thesis PDF's title page or the faculty records.\n\n")
        if not candidates:
            f.write("None.\n")
        for t in candidates:
            f.write(describe(t) + "\n")
        f.write(f"\n## Verified non-Geomatics ({len(non_geo)})\n\n"
                "On the external lists but named to another programme — "
                "correctly absent from the archive.\n\n")
        if not non_geo:
            f.write("None.\n")
        for t in non_geo:
            f.write(describe(t) + "\n")
        if covered_name:
            f.write(f"\n## Archive matches by name only "
                    f"({len(covered_name)})\n\n"
                    "Matched on name and year without a repository uuid "
                    "on both sides; worth glancing at for wrong "
                    "attributions.\n\n")
            for t in covered_name:
                f.write(f"- {t['author']} ({t['year']}) — "
                        f"{(t['title'] or '')[:70]}\n")


def append_gaps(gaps, args):
    """Append confirmed gaps to the archive, enriched where a repository
    record provides the fields; needs_review until a human confirms."""
    entries = yaml.safe_load((REPO_ROOT / "_data" / "geotheses.yml")
                             .read_text())
    added = 0
    for t in gaps:
        if any(e.get("uuid") and e.get("uuid") == t.get("uuid")
               for e in entries):
            continue
        surname, given = eg.split_full_name(t["author"])
        entry = {"surname": surname, "name": " ".join(given),
                 "title": t["title"], "year": t["year"],
                 "needs_review": True}
        if t.get("uuid"):
            entry["link"] = eg.RESOLVER_URL.format(uuid=t["uuid"])
            entry["uuid"] = t["uuid"]
            page = eg.fetch_record(t["uuid"], args.delay, args.offline)
            if page:
                rec = eg.parse_record(page)
                if rec.get("title"):
                    title = rec["title"]
                    if rec.get("subtitle") and rec["subtitle"] not in title:
                        title += " " + rec["subtitle"]
                    entry["title"] = title
                sups = rec.get("mentors") or rec.get("coaches")
                if sups:
                    entry["supervisors"] = "; ".join(sups)
                if rec.get("abstract"):
                    entry["abstract"] = rec["abstract"]
                if rec.get("graduation_date"):
                    try:
                        entry["graduation_date"] = datetime.strptime(
                            rec["graduation_date"],
                            "%d-%m-%Y").date().isoformat()
                    except ValueError:
                        entry["graduation_date"] = rec["graduation_date"]
        elif t.get("pdf"):
            entry["link"] = t["pdf"]  # no repository record; link the PDF
        entries.append(entry)
        added += 1
        print(f"  appended: {t['author']} ({t['year']})")
    if added:
        eg.write_yaml(entries)
    return added


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--add", action="store_true",
                    help="append confirmed gaps to _data/geotheses.yml "
                         "(flagged needs_review)")
    ap.add_argument("--offline", action="store_true",
                    help="work from the cache only, no network")
    ap.add_argument("--delay", type=float, default=20.0,
                    help="seconds between repository record fetches "
                         "(robots.txt asks for 20)")
    ap.add_argument("--no-pdf", action="store_true",
                    help="skip the thesis-PDF checks (large downloads)")
    ap.add_argument("--from-year", type=int, default=2013,
                    help="only consider theses from this year onwards "
                         "(the archive's coverage; default 2013)")
    args = ap.parse_args()

    archive = yaml.safe_load((REPO_ROOT / "_data" / "geotheses.yml")
                             .read_text())

    gdmc_html = load_source(GDMC_URL, SRC_GDMC, args.offline)
    dge_html = load_source(THREE_DGE_URL, SRC_3DGE, args.offline)
    if gdmc_html is None or dge_html is None:
        print("Source page(s) not in cache; run without --offline first.")
        return 2
    gdmc = parse_gdmc(gdmc_html)
    dge = parse_3dge(dge_html)
    if not gdmc or not dge:
        print(f"PARSING BROKE: gdmc={len(gdmc)} theses, 3dge={len(dge)} "
              "theses -- check the source pages' HTML structure.")
        return 2
    print(f"Sources: GDMC lists {len(gdmc)} MSc theses, 3d.bk.tudelft.nl "
          f"lists {len(dge)} completed MSc theses.")

    # union of both sources, keeping the most informative record
    theses = {}
    for src, items in (("gdmc", gdmc), ("3dge", dge)):
        for t in items:
            if t["year"] < args.from_year:
                continue
            t = dict(t, sources=[src])
            key = (t["uuid"] or f"{eg.foldcase(t['author'])}|{t['year']}|"
                   f"{eg.foldcase(t['title'])[:40]}")
            if key in theses:
                old = theses[key]
                old["sources"].append(src)
                for f in ("school", "pdf", "title"):
                    if not old.get(f) and t.get(f):
                        old[f] = t[f]
            else:
                theses[key] = t
    skipped_old = len(gdmc) + len(dge) - sum(
        1 for t in theses.values() for _ in t["sources"])
    skipped_old = max(0, skipped_old)

    covered_name, uncovered = [], []
    for t in theses.values():
        entry, basis = find_in_archive(archive, t)
        if entry:
            if basis == "name":
                covered_name.append(t)
            continue
        uncovered.append(t)
    print(f"Archive covers {len(theses) - len(uncovered)} of "
          f"{len(theses)} external theses; investigating {len(uncovered)}.")

    gaps, non_geo, candidates = [], [], []
    for i, t in enumerate(sorted(uncovered, key=lambda x: x["year"]), 1):
        print(f"[{i}/{len(uncovered)}] {t['author']} ({t['year']})",
              flush=True)
        {"gap": gaps, "non": non_geo, "cand": candidates}[
            investigate(t, args)].append(t)

    write_report(gaps, candidates, non_geo, covered_name, len(archive),
                 len(theses), args.from_year, skipped_old)

    if args.add and gaps:
        added = append_gaps(gaps, args)
        print(f"Appended {added} confirmed gap(s) to _data/geotheses.yml "
              "(needs_review: true).")

    print(f"\n{len(gaps)} confirmed gap(s), {len(candidates)} candidate(s) "
          f"for a manual look, {len(non_geo)} verified non-Geomatics; "
          f"report: {REPORT_FILE.name}")
    return 1 if gaps else 0


if __name__ == "__main__":
    sys.exit(main())
