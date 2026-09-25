#!/usr/bin/env python3
"""Generate cover thumbnails for the thesis archive from the thesis PDFs.

For each archive entry with a repository uuid, the cached record page
(.geotheses_cache/<uuid>.html, fetched by scripts/enrich_geotheses.py)
is scanned for the thesis file link (the download buttons carry the
file's real filename), the PDF is downloaded in memory and its first
page is rendered with PyMuPDF into theses/img/<image> as a small JPEG.
Entries without a repository record fall back to the PDF their link
points at (the GDMC thesis PDFs found by the pre-coverage sweeps).
PDFs are discarded after rendering (--keep-pdfs caches them under
.geotheses_cache/pdf/ instead), so the run needs no meaningful disk
space; the repository's robots.txt crawl-delay makes a full run take
~2 h. When a record has several files (thesis, slides, graduation
plan, ...) candidates are ranked by filename, page orientation and
page count, with the student's surname on page 1 as a tie-breaker, so
slides and proposal-stage milestone documents (P1–P4) don't win;
anything slides-like or short that still gets chosen is flagged.
Entries whose image field has an extension PyMuPDF cannot write (png,
webp, gif, ... — everything is rendered as JPEG) get a fresh name from
the scheme and the old file is deleted once its replacement is
rendered. Entries without an image field get one from the same scheme:
<year>_<Surname>.jpg, ASCII-folded and hyphenated (2026_Aalders.jpg,
2010_de-Koning.jpg, 2016_Felix-Aires.jpg); when that name is taken the
given name is appended (2015_Wu_Haoxiang.jpg). The image fields are
written back to geotheses.yml at the end of a run; rendered entries are
recorded in .geotheses_cache/covers_progress.yml so a re-run resumes
instead of re-downloading (--redo-all starts over).
reports/covers_report.md lists everything that needs a manual look; validate
with scripts/check_geotheses.py.

Usage:
  python3 scripts/thesis_covers.py                 # fetch + render (resumes)
  python3 scripts/thesis_covers.py --skip-existing # keep any existing thumbnails
  python3 scripts/thesis_covers.py --redo-all      # re-render everything
  python3 scripts/thesis_covers.py --limit 3       # first N entries (testing)
  python3 scripts/thesis_covers.py --uuid 675ee... # specific entries
  python3 scripts/thesis_covers.py --keep-pdfs --offline  # re-render offline
"""

import argparse
import html
import re
import sys
import time
import unicodedata
from pathlib import Path

import requests
import yaml

try:
    import pymupdf
except ImportError:  # older PyMuPDF installs
    import fitz as pymupdf

from enrich_geotheses import write_yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = REPO_ROOT / "_data" / "geotheses.yml"
CACHE_DIR = REPO_ROOT / ".geotheses_cache"
PDF_DIR = CACHE_DIR / "pdf"
PROGRESS_FILE = CACHE_DIR / "covers_progress.yml"
REPORT_FILE = REPO_ROOT / "reports" / "covers_report.md"
IMG_DIR = REPO_ROOT / "theses" / "img"

FILE_BLOCK = re.compile(
    r'href="(/file/File_[0-9a-f-]+)"[^>]*?onclick=\'[^\']*?'
    r'"File Download",\s*"[0-9a-f-]+\s*\|\s*([^"]+)"')
FILE_HREF = re.compile(r'href="(/file/File_[0-9a-f-]+)')
SLIDES_NAME = re.compile(
    r"present|slide|graduation[ _-]?plan|defen[cs]e|poster|pitch|proposal",
    re.IGNORECASE)
MILESTONE_NAME = re.compile(r"(?<![A-Za-z0-9])[Pp][1-4](?![0-9])")
THESIS_NAME = re.compile(r"thesis|scriptie", re.IGNORECASE)
SUPPORTED_EXTS = {"jpg", "jpeg"}  # what this script writes (JPEG only)
USER_AGENT = ("geo2022-site-maintainer/1.0 "
              "(https://geomatics.bk.tudelft.nl/geo2022/; one-off cover "
              "thumbnails for the thesis archive, honors robots.txt)")
BLANK_INK = 0.005  # fraction of non-white pixels below which page 1 counts
                   # as blank (minimal title pages sit around 0.01–0.05)
SHORT_PAGES = 40  # theses are longer; below this the pick is suspicious


def foldcase(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def ascii_fold(s):
    """Surnames/given names for filenames: ASCII only, spaces -> hyphens.
    Combining marks are stripped (Köbben -> Kobben); letters without a
    decomposition get an explicit map."""
    s = (s or "").strip()
    for src, dst in (("ł", "l"), ("Ł", "L"), ("ø", "o"), ("Ø", "O"),
                     ("đ", "d"), ("Đ", "D"), ("ß", "ss"), ("æ", "ae"),
                     ("Æ", "AE"), ("œ", "oe"), ("Œ", "OE"), ("þ", "th"),
                     ("Þ", "TH"), ("ð", "d"), ("Ð", "D")):
        s = s.replace(src, dst)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[\s_]+", "-", s.strip())
    return re.sub(r"[^A-Za-z0-9-]", "", s)


def scheme_name(e, taken):
    """Canonical thumbnail filename for an entry: <year>_<Surname>.jpg,
    ASCII-folded; the given name is appended when that name is taken
    (2015_Wu_Haoxiang.jpg), then a counter. `taken` is updated."""
    year = e.get("year") or 0
    base = "-".join(filter(None, (ascii_fold(t) for t in
                                  re.split(r"\s+", e.get("surname") or ""))))
    given = ascii_fold(e.get("name"))
    first = re.sub(r"-.*", "", given) if given else ""
    candidates = [f"{year}_{base}.jpg"]
    if first:
        candidates += [f"{year}_{base}_{first}.jpg"]
    if given and given != first:
        candidates += [f"{year}_{base}_{given}.jpg"]
    for c in candidates:
        if c.lower() not in taken:
            taken.add(c.lower())
            return c
    n = 2
    stem = candidates[0][:-4]
    while f"{stem}-{n}.jpg".lower() in taken:
        n += 1
    final = f"{stem}-{n}.jpg"
    taken.add(final.lower())
    return final


def surname_key(surname):
    """Surname minus tussenvoegsels, for matching against page text."""
    return foldcase(re.sub(r"^(van|de|den|der|ter|te|het|'t) ", "",
                           surname or "", flags=re.IGNORECASE))


def load_progress():
    if PROGRESS_FILE.exists():
        return yaml.safe_load(PROGRESS_FILE.read_text()) or {}
    return {}


def save_progress(progress):
    CACHE_DIR.mkdir(exist_ok=True)
    PROGRESS_FILE.write_text(yaml.safe_dump(progress, sort_keys=True))


def assign_filenames(entries):
    """Give every entry without an image field a name from the canonical
    scheme (scheme_name). Returns the entries that got a new name;
    main() rolls those back if they end up not rendered, so no entry
    keeps a dangling image field."""
    taken = {str(e.get("image", "")).lower() for e in entries}
    fresh = []
    for e in entries:
        if e.get("image"):
            continue
        e["image"] = scheme_name(e, taken)
        fresh.append(e)
    return fresh


def normalize_extensions(todo, taken):
    """Entries whose image extension the script cannot write (it only
    renders JPEG) get a fresh scheme name; main() deletes the old file
    after the replacement is rendered. Returns {entry: old name}."""
    renames = {}
    for e in todo:
        image = str(e.get("image", ""))
        ext = image.rsplit(".", 1)[-1].lower() if "." in image else ""
        if not image or ext in SUPPORTED_EXTS:
            continue
        renames[id(e)] = image
        e["image"] = scheme_name(e, taken)
    return renames


def parse_files(page):
    """(path, filename) pairs from a record page's download buttons,
    falling back to bare /file/ links when the markup differs."""
    out = [(path, html.unescape(name.strip()))
           for path, name in FILE_BLOCK.findall(page)]
    if not out:
        out = [(p, "") for p in dict.fromkeys(FILE_HREF.findall(page))]
    return list(dict.fromkeys(out))


def name_score(name):
    s = 0
    if SLIDES_NAME.search(name) or MILESTONE_NAME.search(name):
        s -= 4
    if THESIS_NAME.search(name):
        s += 2
    return s


def fetch_pdf(path, delay, offline, keep):
    """Download one thesis PDF, given the /file/... path from its record
    page (or an absolute URL, for entries linked to GDMC PDFs directly).
    Returns bytes or None; cached when keep is set."""
    url = path if path.startswith("http") else \
        f"https://repository.tudelft.nl{path}"
    stem = path.rsplit("/", 1)[-1]
    cache = PDF_DIR / f"{stem}.pdf"
    if cache.exists():
        return cache.read_bytes()
    if offline:
        return None
    PDF_DIR.mkdir(exist_ok=True)
    for attempt in (1, 2):
        try:
            r = requests.get(url, headers={"User-Agent": USER_AGENT},
                             timeout=300)
        except requests.RequestException as e:
            print(f"    pdf {stem}: {e}", flush=True)
            time.sleep(delay)
            continue
        if r.status_code == 200 and r.content[:5] == b"%PDF-":
            if keep:
                cache.write_bytes(r.content)
            time.sleep(delay)
            return r.content
        print(f"    pdf {stem}: HTTP {r.status_code} "
              f"(attempt {attempt})", flush=True)
        time.sleep(delay)
    return None


def choose_pdf(candidates, fetch, surname_k):
    """Pick the thesis PDF among a record's files. Candidates are tried
    thesis-named first; each downloaded file is scored on filename,
    portrait orientation, page count and the surname on page 1, and a
    confident score stops the search. Returns the best as a dict, or
    None."""
    best = None
    for path, name in sorted(candidates, key=lambda c: name_score(c[1]),
                             reverse=True):
        if name_score(name) <= -4 and best is not None:
            break  # obvious slides or milestone doc; don't download it
        data = fetch(path)
        if not data:
            continue
        with pymupdf.open(stream=data, filetype="pdf") as doc:
            pages = doc.page_count
            rect = doc[0].rect if pages else None
            text = foldcase(doc[0].get_text()) if pages else ""
        portrait = bool(rect and rect.width < rect.height)
        s = name_score(name)
        if surname_k and surname_k in text:
            s += 3
        if portrait:
            s += 2
        elif rect:
            s -= 3  # landscape: slide deck
        if pages >= 60:
            s += 2  # a real MSc thesis; also beats text-layer-less picks
        elif pages >= SHORT_PAGES:
            s += 1
        else:
            s -= 1
        if best is None or s > best["score"]:
            best = {"score": s, "data": data, "path": path, "name": name,
                    "pages": pages, "portrait": portrait}
        if s >= 4 and portrait and name_score(name) >= 0:
            break  # thesis-named, portrait, right pages: good enough
    return best


def render(pdf_bytes, out_path, width, quality):
    """Render page 1 to out_path as JPEG (page 2 when page 1 is blank,
    as with old theses); returns (nearly_blank, size, page_used)."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with pymupdf.open(stream=pdf_bytes, filetype="pdf") as doc:
        used = 0
        pix = None
        for pageno in range(min(2, doc.page_count)):
            used = pageno + 1
            page = doc[pageno]
            zoom = width / page.rect.width
            pix = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom),
                                  alpha=False)
            samples, n = pix.samples, pix.n
            ink = sum(
                1 for j in range(0, len(samples), n)
                if (samples[j] + samples[j + 1] + samples[j + 2]) / 3 < 245)
            if ink / (pix.width * pix.height) >= BLANK_INK:
                break
        out_path.write_bytes(pix.tobytes("jpeg", jpg_quality=quality))
    return ink / (pix.width * pix.height) < BLANK_INK, \
        out_path.stat().st_size, used


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--offline", action="store_true",
                    help="render from cached PDFs only, no network "
                         "(needs a previous --keep-pdfs run)")
    ap.add_argument("--keep-pdfs", action="store_true",
                    help="cache the PDFs under .geotheses_cache/pdf/ "
                         "(GBs; default is to discard after rendering)")
    ap.add_argument("--skip-existing", action="store_true",
                    help="keep existing thumbnails, rendered or not")
    ap.add_argument("--redo-all", action="store_true",
                    help="ignore the progress file and re-render "
                         "everything")
    ap.add_argument("--limit", type=int, default=None,
                    help="only process the first N entries (testing)")
    ap.add_argument("--uuid", action="append", default=[],
                    help="only process these entry uuids (repeatable)")
    ap.add_argument("--delay", type=float, default=20.0,
                    help="seconds between PDF fetches "
                         "(repository robots.txt asks for 20)")
    ap.add_argument("--width", type=int, default=256,
                    help="thumbnail width in px (display is 96x96)")
    ap.add_argument("--quality", type=int, default=85, help="JPEG quality")
    ap.add_argument("--out-dir", default=None,
                    help="write thumbnails here instead of theses/img "
                         "(previews; nothing is written back)")
    ap.add_argument("--report", default=None,
                    help="report file (default reports/covers_report.md)")
    args = ap.parse_args()

    entries = yaml.safe_load(DATA_FILE.read_text())
    real_run = args.out_dir is None
    out_dir = Path(args.out_dir) if args.out_dir else IMG_DIR
    report_file = Path(args.report) if args.report else REPORT_FILE
    report_file.parent.mkdir(parents=True, exist_ok=True)

    progress = load_progress() if real_run else {}
    if real_run:
        for e in entries:
            key = e.get("uuid") or str(e.get("link", ""))
            # names from an interrupted earlier run
            if key in progress and not e.get("image"):
                e["image"] = progress[key]
            elif key in progress and \
                    e["image"] != progress[key] and \
                    (IMG_DIR / progress[key]).is_file():
                e["image"] = progress[key]  # adopt the rendered name
    fresh = assign_filenames(entries)

    todo = []
    for e in entries:
        # entries without a repository record fall back to a linked
        # PDF (the GDMC page the pre-coverage sweeps found)
        if not e.get("uuid") and not str(e.get("link", "")).endswith(".pdf"):
            continue
        key = e.get("uuid") or str(e.get("link", ""))
        if args.uuid and e.get("uuid") and e["uuid"] not in args.uuid:
            continue
        if real_run and not args.redo_all and not args.uuid and \
                key in progress:
            continue
        if args.skip_existing and e.get("image") and \
                (out_dir / e["image"]).is_file():
            continue
        todo.append(e)
    if args.limit:
        todo = todo[: args.limit]

    taken = {str(e.get("image", "")).lower() for e in entries}
    renames = normalize_extensions(todo, taken)

    print(f"{len(todo)} entr(y/ies) to do, {args.delay}s between fetches.")
    reports, renamed, mb = [], [], 0.0
    done, rendered = 0, set()
    for n, e in enumerate(todo, 1):
        who = f"{e.get('name', '')} {e.get('surname', '')}" \
            f" ({e.get('year', '')})".strip()
        print(f"[{n}/{len(todo)}] {who}", flush=True)

        if e.get("uuid"):
            record = CACHE_DIR / f"{e['uuid']}.html"
            if not record.exists():
                reports.append(f"NO RECORD PAGE: {who} uuid={e['uuid']}")
                continue
            candidates = parse_files(record.read_text(errors="replace"))
            if not candidates:
                reports.append(f"NO FILE ON RECORD: {who} uuid={e['uuid']}")
                continue
        else:
            candidates = [(e["link"],
                           e["link"].rsplit("/", 1)[-1].replace("%20", " "))]

        surname_k = surname_key(e.get("surname"))
        pick = choose_pdf(candidates,
                          lambda p: fetch_pdf(p, args.delay, args.offline,
                                              args.keep_pdfs),
                          surname_k)
        if pick is None:
            reports.append(f"NO PDF: {who} uuid={e['uuid']} "
                           f"files={len(candidates)}")
            continue
        label = pick["name"] or "unnamed file"
        if SLIDES_NAME.search(label):
            reports.append(f"CHOSEN FILE LOOKS LIKE SLIDES "
                           f"({label}, {pick['pages']} pages): {who}")
        elif MILESTONE_NAME.search(label):
            reports.append(f"CHOSEN FILE IS A MILESTONE DOCUMENT "
                           f"({label}, {pick['pages']} pages): {who}")
        elif not pick["portrait"]:
            reports.append(f"CHOSEN FILE IS LANDSCAPE "
                           f"({label}, {pick['pages']} pages): {who}")
        elif pick["pages"] < SHORT_PAGES:
            reports.append(f"CHOSEN FILE IS SHORT "
                           f"({label}, {pick['pages']} pages): {who}")
        mb += len(pick["data"]) / 1e6

        image = e["image"]
        blank, size, used = render(pick["data"], out_dir / image,
                                   args.width, args.quality)
        if used > 1:
            reports.append(f"PAGE 1 BLANK, USED PAGE {used}: {who} -> {image}")
        elif blank:
            reports.append(f"PAGE 1 NEARLY BLANK: {who} -> {image}")
        if id(e) in renames:
            renamed.append(f"{who}: {renames[id(e)]} -> {image}")
            if real_run and (IMG_DIR / renames[id(e)]).is_file():
                (IMG_DIR / renames[id(e)]).unlink()
        done += 1
        rendered.add(id(e))
        if real_run:
            progress[e.get("uuid") or str(e.get("link", ""))] = image
            save_progress(progress)
        print(f"    -> {image} {size // 1024} KB ({label}, "
              f"{pick['pages']} pages) [{mb:.0f} MB downloaded]", flush=True)

    if real_run:
        for e in fresh:
            if id(e) not in rendered:
                e.pop("image", None)
        write_yaml(entries)
        print(f"Wrote image fields for "
              f"{len(rendered & set(map(id, fresh)))} new entr(y/ies) to "
              f"{DATA_FILE.name}.")

    with report_file.open("w") as f:
        f.write(f"# cover thumbnails report ({time.strftime('%Y-%m-%d')})\n\n")
        f.write(f"{done} thumbnail(s) rendered"
                + (f", {len(todo) - done} not" if done != len(todo) else "")
                + ".\n")
        if renamed:
            f.write("\n## Renamed image fields\n\n")
            for line in renamed:
                f.write(f"- {line}\n")
        f.write("\n## Needs a manual look\n\n")
        for line in reports:
            f.write(f"- {line}\n")
    print(f"Done: {done} thumbnail(s); {len(renamed)} rename(s), "
          f"{len(reports)} note(s) in {report_file.name}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
