#!/usr/bin/env python3
"""Expand the initials-only student names in _data/geotheses.yml to full
given names, keeping surnames as they are.

The archive's name/surname come from the repository record pages, which
show students as initials ("S.A. Sablerolle"). This script replaces the
name field with the fullest known given name, gathered with evidence:

  1. MyCase (mycase/mycase_index.csv, closed cases) -- the graduation
     register, first choice for recent theses;
  2. the thesis PDF from the repository -- title pages and PDF metadata
     (the cover/title page carries the full name for older theses);
  3. corroboration from the cached GDMC publication list and GDMC PDF
     title pages (.geotheses_cache), never used as the sole source.

Every candidate must be initials-consistent with the archive's name:
its given-name initials must match the archive's initials position-wise
("S.A." matches "Steven Alexander", not "Eric"). Candidates that match
all initials win over partial ones, then fuller names, then the source
order above. PDFs are cached under .geotheses_cache/pdf/ (the
repository's robots.txt crawl-delay makes the first run take ~20 s per
thesis). Unresolved entries keep their initials and are reported.

Dry-run by default: prints the proposal and writes reports/student_names_report.md
with the evidence. Pass --write to apply to geotheses.yml.

Usage:
  python3 scripts/expand_student_names.py            # propose (fetch PDFs)
  python3 scripts/expand_student_names.py --write    # apply the proposal
  python3 scripts/expand_student_names.py --offline  # cached PDFs only
  python3 scripts/expand_student_names.py --uuid 00f12183...         # one
"""
import argparse
import re
import sys
import time
from pathlib import Path

import yaml

try:
    import pymupdf
except ImportError:  # older PyMuPDF installs
    import fitz as pymupdf

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from enrich_geotheses import (DATA_FILE, foldcase, mycase_closed,
                              names_match, split_full_name, write_yaml)
from thesis_covers import CACHE_DIR, choose_pdf, fetch_pdf, parse_files, \
    surname_key

REPORT_FILE = REPO_ROOT / "reports" / "student_names_report.md"
GDMC_PUBS = CACHE_DIR / "src-gdmc-pubs.html"

# tokens that may sit between a degree prefix and the surname without
# being given names, or that end the expansion ("Student:", a year, ...)
STOP_TOKENS = {
    "student", "author", "name", "door", "by", "of", "the", "and", "van",
    "delft", "technology", "university", "faculty", "department", "school",
    "geomatics", "geodesy", "supervisor", "professor", "graduation",
    "campus", "thesis", "report", "master", "bachelor", "copyright", "isbn",
    "january", "february", "march", "april", "may", "june", "july",
    "august", "september", "october", "november", "december",
}
DEGREE_TOKEN = re.compile(
    r"(?:(?:ing|ir|drs|dr|mr|ms|prof)|[bm]\.?[- ]?(?:sc|eng|a|ba|ma))\.?",
    re.IGNORECASE)


def is_initials_only(name):
    return not any(c.islower() for c in (name or ""))


def archive_initials(name):
    return [t[0].upper() for t in re.split(r"[\s.\u2019'-]+", name or "")
            if t]


def given_initials(given):
    """'Hoe-Ming' -> ['H', 'M'] (hyphenated parts each carry one)."""
    return [t[0].upper() for t in re.split(r"[\s.\u2019'-]+", given or "")
            if t]


def initials_tier(arch, cand):
    """0: candidate matches all the archive's initials ("Steven Alexander"
    for S.A.); 1: prefix ("Rian" for R.M., middle name not shown); 2:
    subsequence ("Cornelis" for D.C., the thesis shows a middle name);
    9: inconsistent -- a different person."""
    if cand == arch:
        return 0
    if cand and cand == arch[:len(cand)]:
        return 1
    it = iter(arch)
    if cand and all(c in it for c in cand):
        return 2
    return 9


def plausible_given_token(token):
    token = token.rstrip(",;:")
    if not token or token.lower() in STOP_TOKENS or \
            DEGREE_TOKEN.fullmatch(token):
        return False
    parts = re.split(r"[\u2019'-]", token)
    return all(p and p[0].isupper() and (len(p) == 1 or p[1:].islower())
               for p in parts)


def names_before_surname(page_text, surname):
    """Full-name candidates of the form 'Given [Middle] <surname>':
    for each surname occurrence on the page, walk left over plausible
    given-name tokens (up to 4) and emit every prefix of the walk, so a
    title word swept into the front ("...Logging Data Menno Bloemsma")
    still leaves "Menno" as a candidate for the initials check."""
    out = []
    for m in re.finditer(re.escape(surname), page_text,
                         flags=re.IGNORECASE):
        left = page_text[max(0, m.start() - 120):m.start()]
        tokens = left.split()
        given = []
        for token in reversed(tokens):
            if len(given) >= 4:
                break
            clean = token.rstrip(",;:")
            if not clean or clean.endswith(":") or \
                    not plausible_given_token(clean):
                break
            given.insert(0, clean)
            out.append(" ".join(given))
    return out


def names_after_comma(page_text, surname):
    """Candidates of the form '<surname>, Given [Middle]'."""
    return [m.group(1) for m in re.finditer(
        re.escape(surname) + r"\s*,\s*([A-Z][A-Za-z\u00c0-\u017e\u2019'-]+"
        r"(?:\s+[A-Z][A-Za-z\u00c0-\u017e\u2019'-]+){0,3})\s*(?:,|$)",
        page_text)]


def pdf_name_candidates(pdf_bytes, surname, tuss_less):
    """(given, where, quote) triples from the PDF's metadata and first
    pages. Searched with the archive's full surname and, failing that,
    the surname without tussenvoegsels."""
    cands = []
    with pymupdf.open(stream=pdf_bytes, filetype="pdf") as doc:
        meta = doc.metadata or {}
        pages = [doc[i].get_text() for i in range(min(4, doc.page_count))]
    for where, text in ([("metadata", meta.get("author") or "")] +
                        [(f"page {i}", t) for i, t in enumerate(pages)]):
        text = re.sub(r"\s+", " ", text)
        if not text:
            continue
        for name in dict.fromkeys((surname, tuss_less)):
            found = (names_before_surname(text, name) +
                     names_after_comma(text, name))
            for given in found:
                quote = text[max(0, text.find(name) - 60):
                             text.find(name) + len(name) + 10].strip()
                cands.append((given, where, quote))
    return cands


def mycase_candidates(entry, closed_rows):
    out = []
    for row in closed_rows:
        if names_match(entry, row["student_name"]):
            _surname, given = split_full_name(row["student_name"])
            if given:
                out.append((" ".join(given), "mycase",
                            f"MyCase student_name: {row['student_name']} "
                            f"(cohort {row['course_year']})"))
    return out


def corroborate(given, surname, tuss_less):
    """Count cached GDMC-list/PDF-text occurrences of '<given> <surname>'
    (evidence only, never the sole source)."""
    core = re.escape(tuss_less)
    pat = re.compile(r"\b" + re.escape(given.split()[0]) + r"(?:\s+\w+)?\s+"
                     r"(" + core + r"\b|\b" +
                     re.escape(surname) + r"\b)", re.IGNORECASE)
    hits = 0
    for f in CACHE_DIR.glob("pdftext-*.txt"):
        hits += len(pat.findall(f.read_text(errors="replace")))
    if GDMC_PUBS.exists():
        hits += len(pat.findall(GDMC_PUBS.read_text(errors="replace")))
    return hits


SOURCE_RANK = {"mycase": 0, "title page": 1, "metadata": 2}


def rank(entry, given, where):
    tier = initials_tier(archive_initials(entry.get("name")),
                         given_initials(given))
    return (tier, -len(given_initials(given)), SOURCE_RANK.get(where, 3))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--write", action="store_true",
                    help="apply the proposal to geotheses.yml")
    ap.add_argument("--offline", action="store_true",
                    help="use cached PDFs only, no network")
    ap.add_argument("--discard-pdfs", action="store_true",
                    help="do not keep the PDFs under "
                         ".geotheses_cache/pdf/")
    ap.add_argument("--delay", type=float, default=20.0,
                    help="seconds between PDF fetches (robots.txt)")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--uuid", action="append", default=[])
    ap.add_argument("--report", default=None)
    args = ap.parse_args()

    entries = yaml.safe_load(DATA_FILE.read_text())
    closed = mycase_closed()
    todo = [e for e in entries if is_initials_only(e.get("name"))]
    if args.uuid:
        todo = [e for e in todo if e.get("uuid") in args.uuid]
    if args.limit:
        todo = todo[: args.limit]

    report = [f"# student name expansion ({time.strftime('%Y-%m-%d')})\n"]
    applied = 0
    for n, e in enumerate(todo, 1):
        who = f"{e.get('name')} {e.get('surname')} ({e.get('year')})"
        surname = str(e.get("surname", ""))
        tuss_less = re.sub(r"^(van|de|den|der|ter|te|het|'t) ", "",
                           surname, flags=re.IGNORECASE)
        arch = archive_initials(e.get("name"))
        print(f"[{n}/{len(todo)}] {who}", flush=True)

        cands = mycase_candidates(e, closed)
        if e.get("uuid"):
            record = CACHE_DIR / f"{e['uuid']}.html"
            if record.exists():
                files = parse_files(record.read_text(errors="replace"))
                if files:
                    pick = choose_pdf(
                        files,
                        lambda p: fetch_pdf(p, args.delay, args.offline,
                                            not args.discard_pdfs),
                        surname_key(surname))
                    if pick:
                        cands += pdf_name_candidates(
                            pick["data"], surname, tuss_less)
                    else:
                        report.append(f"NO PDF FOUND: {who}")
            else:
                report.append(f"NO RECORD PAGE: {who} uuid={e['uuid']}")

        # keep only initials-consistent candidates (tier < 9), and drop
        # candidates that are still initials-only (no expansion)
        good = [(g, w, q) for g, w, q in cands
                if initials_tier(arch, given_initials(g)) < 9]
        good = [(g, w, q) for g, w, q in good if any(c.islower() for c in g)]
        tier = lambda g: initials_tier(arch, given_initials(g))

        seen, all_cands = set(), []
        for c in cands:
            if c not in seen:
                seen.add(c)
                all_cands.append(c)
        lines = [f"## {who}", ""]
        for g, w, q in sorted(all_cands, key=lambda c: (rank(e, *c[:2]), c)):
            mark = "OK  " if tier(g) == 0 else \
                   f"part({tier(g)})" if tier(g) < 9 else "REJ "
            lines.append(f"- [{mark}] {w}: \"{g}\" -- {q}")
        if not good:
            lines.append("- no consistent full name found; initials kept")
            report += lines + [""]
            print("    unresolved", flush=True)
            continue

        best_given, best_where, _ = sorted(good,
                                           key=lambda c: (rank(e, *c[:2]),
                                                          c))[0]
        best_tier = tier(best_given)
        conflicts = {g for g, w, q in good
                     if tier(g) == best_tier
                     and len(given_initials(g)) ==
                     len(given_initials(best_given))
                     and foldcase(g) != foldcase(best_given)}
        if best_tier:
            lines.append(f"- NOTE: partial initials match -- \"{best_given}\" "
                         f"covers {''.join(given_initials(best_given))} of "
                         f"{e['name']}; the archive's other initial(s) are "
                         f"not shown on the thesis/MyCase")
        if conflicts:
            lines.append(f"- NOTE: competing forms {sorted(conflicts)}; "
                         f"\"{best_given}\" chosen (source: {best_where})")

        corrob = corroborate(best_given, surname, tuss_less)
        if corrob:
            lines.append(f"- corroborated {corrob}x in the cached GDMC "
                         f"lists/PDF texts")

        new_name = f"{e['name']} {surname} ({e['year']})"
        lines.append(f"- PROPOSED: {new_name} -> {best_given} {surname} "
                     f"[{best_where}]")
        report += lines + [""]
        print(f"    {e['name']} -> {best_given}  [{best_where}]",
              flush=True)
        if args.write:
            e["name"] = best_given
            applied += 1

    if args.write:
        write_yaml(entries)
        print(f"wrote {DATA_FILE.name}: {applied} name(s) updated")
        report.insert(1, f"\n{applied} name(s) written to "
                         f"{DATA_FILE.name}.\n")
    else:
        report.insert(1, "\nDry run: nothing written to geotheses.yml.\n")
    report_file = Path(args.report or REPORT_FILE)
    report_file.parent.mkdir(parents=True, exist_ok=True)
    report_file.write_text("\n".join(report), encoding="utf-8")
    print(f"report: {report_file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
