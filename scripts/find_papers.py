#!/usr/bin/env python3
"""Find papers that were published on top of the archived theses.

The archive's `paper:` field links the journal/conference paper a thesis
grew into, but only a handful of entries carry one. This script hunts for
more by comparing every thesis without a paper link against two sources:

  1. The GDMC publication list (https://www.gdmc.nl/publications/pubs.php),
     which next to theses also lists the 3D geoinformation research
     group's scientific articles and conference papers.
  2. Crossref (https://api.crossref.org), queried per thesis on the
     thesis title (+ once with the student as author), date-bounded to
     the years a derived paper could appear in.
  3. OpenAlex (https://api.openalex.org), searched per person: each
     supervisor and student is resolved to an author profile (TU Delft
     affiliation required) and their works fetched once. OpenAlex's free
     daily budget is shared per network IP, so it is probed first and
     skipped (with a console note) when exhausted -- Crossref then
     carries the run alone.

Candidates are scored on co-authorship (the thesis's student -- preferably
as first author -- and/or its supervisors among the paper's authors),
title similarity and abstract
similarity (paper abstract vs the thesis abstract in the archive) and
bucketed into Likely and Possible for a manual look. Adding an accepted
paper is a hand edit of the entry's `paper:` field in
_data/geotheses.yml (optionally `paper_label:`; several at once as a
`papers:` list of {url, label} entries); candidates rejected by
hand go in scripts/verified_papers.yml ('verdict: not related') and are
never reported again.

As a built-in calibration the script re-searches the entries that already
carry a paper link and reports in the report's appendix whether they would
have been found -- a rough recall estimate for the thresholds below.

Output: reports/papers_report.md and a console summary.
Exit status is 2 when the GDMC page could not be fetched or parsed.

Usage:
  python3 scripts/find_papers.py               # full search
  python3 scripts/find_papers.py --offline     # work from the cache only
  python3 scripts/find_papers.py --limit 10    # first 10 theses only
  python3 scripts/find_papers.py --surname Xu  # debug: one family only
"""

import argparse
import difflib
import html
import json
import re
import sys
import time
import unicodedata
from collections import Counter
from datetime import datetime
from pathlib import Path

import requests
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import enrich_geotheses as eg  # noqa: E402  (shared helpers)

REPO_ROOT = eg.REPO_ROOT
REPORT_FILE = REPO_ROOT / "reports" / "papers_report.md"
VERIFIED_FILE = Path(__file__).resolve().parent / "verified_papers.yml"

GDMC_PUBS_URL = "https://www.gdmc.nl/publications/pubs.php"
SRC_GDMC = "src-gdmc-pubs.html"  # cache shared with find_missing_theses.py

CROSSREF = "https://api.crossref.org/works"

OPENALEX = "https://api.openalex.org"
OPENALEX_MAILTO = "k.ohori@tudelft.nl"
TUD_INST_ID = "I98358874"  # Delft University of Technology
OA_SELECT = ("id,title,publication_year,doi,type,authorships,"
             "abstract_inverted_index,primary_location")
OA_PER_PAGE = 200
OA_MAX_PAGES = 6  # ~1200 works per person is plenty
OA_STUDENT_PAGES = 2

# GDMC sections that hold papers a thesis could grow into, mapped to the
# paper_label wording used on the site.
GDMC_PAPER_SECTIONS = {
    "Scientific articles": "journal article",
    "Conference and Workshop papers": "conference paper",
    "Conference papers (in published book)": "conference paper",
}

YEAR_BACK = 1     # a paper can appear the year before the thesis date
YEAR_FORWARD = 9  # ... or years later (slow journals, extended versions)

# Similarity thresholds, calibrated on the entries that already carry a
# paper link (see the Calibration section of the report): title
# similarity t is max(token jaccard, string ratio of the folded titles)
# and tj (jaccard alone) backs the title-only rules, since unrelated
# titles with the same word order score high on string ratio; abstract
# similarity is a token cosine (None when either side has no abstract).
# A thesis's paper is authored by its student (preferably first), so a
# Likely requires the student among the authors; supervisor or
# title-only matches can only be a Possible.
T_LIKELY_STU_TITLE = 0.35  # student co-author + title similarity
T_LIKELY_STU_ABS = 0.40    # student co-author + abstract similarity
T_POSS_STU_TITLE = 0.20    # student + weak title similarity, near year
T_POSS_STU_ABS = 0.25      # student + weak abstract similarity, near year
T_POSS_SUP_TITLE = 0.30    # a supervisor + weak title similarity
T_POSS_SUP_ABS = 0.35      # a supervisor + abstract similarity
T_POSS_TITLE = 0.55        # title token overlap alone, near year

STOPWORDS = {
    "a", "an", "the", "and", "or", "of", "for", "in", "on", "to", "by",
    "with", "from", "using", "based", "via", "into", "its", "their",
    "this", "that", "these", "those", "as", "are", "be", "is", "was",
    "were", "been", "has", "have", "had", "at", "we", "our", "it", "can",
    "may", "new", "novel", "such", "than", "then", "also", "both", "each",
    "which", "what", "when", "where", "how", "between", "within", "under",
    "over", "after", "before", "during", "towards", "toward", "not", "no",
}

# OpenAlex dead-call counter for the run (see openalex()).
_OA_FAILURES = 0


# ------------------------------------------------------------------ utils

def http_get(url, timeout=120):
    r = requests.get(url, headers={"User-Agent": eg.USER_AGENT},
                     timeout=timeout)
    r.raise_for_status()
    return r.content


def openalex(path, params, cache_name, offline):
    """One OpenAlex API GET (polite pool), cached as parsed JSON. Returns
    None when offline without a cache file or after repeated failures.
    After a few dead calls in one run the API is given up on entirely
    (its free daily budget is shared per network IP and can run out
    mid-run)."""
    global _OA_FAILURES
    if _OA_FAILURES >= 3:
        return None
    cache = eg.CACHE_DIR / cache_name
    if cache.exists():
        return json.loads(cache.read_text())
    if offline:
        return None
    params = dict(params, mailto=OPENALEX_MAILTO)
    for attempt in range(3):
        try:
            r = requests.get(f"{OPENALEX}{path}", params=params,
                             headers={"User-Agent": eg.USER_AGENT},
                             timeout=120)
            if r.status_code in (429, 500, 502, 503):
                time.sleep(2 ** attempt + 1)
                continue
            r.raise_for_status()
            data = r.json()
            break
        except (requests.RequestException, ValueError) as e:
            print(f"    openalex {path}: {e}", flush=True)
            _OA_FAILURES += 1
            return None
    else:
        _OA_FAILURES += 1
        if _OA_FAILURES == 3:
            print("    openalex: giving up for this run (rate-limited); "
                  "continuing with GDMC + Crossref only.", flush=True)
        return None
    eg.CACHE_DIR.mkdir(exist_ok=True)
    cache.write_text(json.dumps(data))
    time.sleep(0.2)
    return data


def openalex_author_id(name, offline):
    """The OpenAlex author profile for a display name, chosen among the
    search hits as the first one with a TU Delft affiliation and a
    matching surname; None when there is no convincing profile."""
    slug = "oa-author-" + eg.foldcase(name) + ".json"
    data = openalex("/authors", {"search": name, "per-page": 25}, slug,
                    offline)
    if not data:
        return None
    query_surname = surname_key(name.split()[-1] if name.split() else "")
    for a in data.get("results", []):
        insts = {inst.get("id", "") for inst in
                 (a.get("affiliations") or [])} | {
                     i.get("id", "") for i in
                     (a.get("last_known_institutions") or [])}
        prof_surname = surname_key(
            (a.get("display_name") or "").split()[-1])
        if (TUD_INST_ID in insts and query_surname
                and prof_surname == query_surname):
            return a.get("id", "").rsplit("/", 1)[-1]
    return None


def page_works(params, cache_name, offline, max_pages=OA_MAX_PAGES):
    """All works of a paged OpenAlex works query, slimmed; None when the
    data is not (fully) available."""
    works, cursor = [], "*"
    for page in range(max_pages):
        data = openalex("/works", dict(params, per_page=OA_PER_PAGE,
                                       cursor=cursor, select=OA_SELECT),
                        cache_name if page == 0 else f"{cache_name}.{page}",
                        offline)
        if data is None:
            return None
        for w in data.get("results", []):
            works.append(slim_work(w))
        cursor = (data.get("meta") or {}).get("next_cursor")
        if not cursor:
            break
    return works


def slim_work(w):
    authors = [(a.get("raw_author_name")
                or (a.get("author") or {}).get("display_name") or "")
               for a in (w.get("authorships") or [])]
    venue = (((w.get("primary_location") or {}).get("source") or {})
             .get("display_name") or "")
    return {"source": "OpenAlex",
            "id": w.get("id") or "",
            "title": w.get("title") or "",
            "year": w.get("publication_year"),
            "doi": (w.get("doi") or "").replace("https://doi.org/", "").lower(),
            "url": "",
            "type": w.get("type") or "",
            "authors": [a for a in authors if a],
            "venue": venue,
            "abstract": abstract_text(w.get("abstract_inverted_index"))}


def openalex_works_for(name, offline, role, year=None):
    """Works of one person (supervisor or student): via their resolved
    author profile when possible, else a raw-author-name search (for
    students bounded to the thesis year window and two pages)."""
    aid = openalex_author_id(name, offline)
    if aid:
        works = page_works({"filter": f"authorships.author.id:{aid}"},
                           f"oa-works-{aid}.json", offline)
        if works is not None:
            return works
    filt = f"raw_author_name.search:{name}"
    if role == "student" and year:
        filt += f",publication_year:{year - YEAR_BACK}-{year + YEAR_FORWARD}"
    pages = OA_STUDENT_PAGES if role == "student" else OA_MAX_PAGES
    works = page_works({"filter": filt},
                       f"oa-works-raw-{eg.foldcase(name)}.json",
                       offline, max_pages=pages)
    return works or []


def abstract_text(inv):
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[i] for i in sorted(pos))


def probe_openalex(offline):
    """True when OpenAlex answers at all (its free daily budget is shared
    per network IP and is regularly exhausted; Crossref then carries the
    run alone). Not cached: a stale probe would mislead for a whole day."""
    if offline:
        return True  # harmless: offline runs only see cached data anyway
    try:
        r = requests.get(f"{OPENALEX}/works",
                         params={"per-page": 1, "select": "id",
                                 "mailto": OPENALEX_MAILTO},
                         headers={"User-Agent": eg.USER_AGENT}, timeout=60)
        if r.status_code == 200:
            return True
        print(f"OpenAlex unavailable (HTTP {r.status_code}: "
              f"{(r.json() or {}).get('error', 'unknown')}); "
              "using GDMC + Crossref only.", flush=True)
    except (requests.RequestException, ValueError) as e:
        print(f"OpenAlex unavailable ({e}); using GDMC + Crossref only.",
              flush=True)
    return False


# ---------------------------------------------------------------- sources

def load_gdmc_pubs(offline):
    """(papers, ok): all scientific/conference papers in the GDMC
    publication list (all years); (None, False) when unavailable."""
    cache = eg.CACHE_DIR / SRC_GDMC
    if cache.exists():
        text = cache.read_text(encoding="utf-8", errors="replace")
    elif offline:
        return None, False
    else:
        text = http_get(GDMC_PUBS_URL).decode("utf-8", errors="replace")
        eg.CACHE_DIR.mkdir(exist_ok=True)
        cache.write_text(text, encoding="utf-8")
    papers, year, sec = [], None, None
    for m in re.finditer(r'<h2>(\d{4})</h2>|<h3>(.*?)</h3>'
                         r'|<li class="bibline">(.*?)</li>', text, re.S):
        if m.group(1):
            year = int(m.group(1))
        elif m.group(2) is not None:
            sec = m.group(2).strip()
        elif sec in GDMC_PAPER_SECTIONS:
            blk = re.sub(r'<a class="bibanchor"[^>]*></a>', "", m.group(3))
            ti = re.search(r'<span class="bibtitle">(.*?)</span>', blk, re.S)
            if not ti:
                continue
            authors = [a.strip() for a in re.sub(r"<[^>]+>", "",
                                                 blk[:ti.start()]).split(",")
                       if a.strip()]
            title = html.unescape(re.sub(r"\s+", " ", ti.group(1))).strip()
            doi, url, pdf_url = "", "", ""
            for href, label in re.findall(r'<a[^>]*href="([^"]+)"'
                                          r'[^>]*>([^<]*)</a>', blk):
                label = label.strip()
                href = ("https:" + href) if href.startswith("//") else href
                if "doi.org/" in href and not doi:
                    dm = re.search(r"(10\.\d{4,9}/[^\"\s]+)", href)
                    if dm:
                        doi = dm.group(1).rstrip(".").lower()
                elif label == "link" and not url:
                    url = href
                elif label == "pdf" and not pdf_url:
                    pdf_url = href
            if not url and doi:
                url = f"https://doi.org/{doi}"
            if not url:
                url = pdf_url
            rest = re.sub(r"\s+", " ", html.unescape(
                re.sub(r"<[^>]+>", " ", blk[ti.end():].split("<br")[0])))
            rest = rest.strip().strip(",").strip()
            rest = re.sub(r",?\s*(?:pp\. \d+|In press|\d{4})\.?$", "",
                          rest).strip().strip(",").strip()
            papers.append({"source": "GDMC", "title": title, "year": year,
                           "doi": doi, "url": url,
                           "type": GDMC_PAPER_SECTIONS[sec],
                           "authors": authors,
                           "venue": rest.replace("In: ", "", 1),
                           "abstract": ""})
    return papers, bool(papers)


def crossref_get(params, cache_name, offline):
    """One Crossref works query (polite pool), cached as the raw item
    list. Returns None when offline without a cache file or after
    repeated failures."""
    cache = eg.CACHE_DIR / cache_name
    if cache.exists():
        return json.loads(cache.read_text())
    if offline:
        return None
    params = dict(params, mailto=OPENALEX_MAILTO, rows=25,
                  select="DOI,title,author,issued,type,container-title,"
                         "abstract,URL")
    for attempt in range(4):
        try:
            r = requests.get(CROSSREF, params=params,
                             headers={"User-Agent": eg.USER_AGENT},
                             timeout=120)
            if r.status_code in (429, 500, 502, 503):
                time.sleep(2 ** attempt + 1)
                continue
            r.raise_for_status()
            items = r.json().get("message", {}).get("items", [])
            break
        except (requests.RequestException, ValueError) as e:
            print(f"    crossref: {e}", flush=True)
            return None
    else:
        print("    crossref: kept failing", flush=True)
        return None
    eg.CACHE_DIR.mkdir(exist_ok=True)
    cache.write_text(json.dumps(items))
    time.sleep(0.3)
    return items


def slim_crossref(it):
    year = ((it.get("issued") or {}).get("date-parts") or [[None]])[0][0]
    authors = [" ".join(x for x in (a.get("given", ""),
                                    a.get("family", "")) if x).strip()
               for a in (it.get("author") or [])]
    abstract = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ",
                                          it.get("abstract") or "")).strip()
    titles = it.get("title") or []
    containers = it.get("container-title") or []
    return {"source": "Crossref",
            "id": it.get("URL") or "",
            "title": html.unescape(re.sub(r"\s+", " ", titles[0])).strip()
                     if titles else "",
            "year": year,
            "doi": (it.get("DOI") or "").lower(),
            "url": "",
            "type": it.get("type") or "",
            "authors": [a for a in authors if a],
            "venue": containers[0] if containers else "",
            "abstract": abstract}


def crossref_candidates(entry, offline):
    """Crossref works for one thesis: a bibliographic query on the thesis
    title and one with the student as author, both date-bounded. Results
    of both queries are merged per DOI."""
    y = int(entry.get("year") or 0)
    slug = "crossref-" + eg.foldcase(
        f"{entry.get('surname')} {entry.get('name')} {y}") + ".json"
    filt = (f"from-pub-date:{y - YEAR_BACK},"
            f"until-pub-date:{y + YEAR_FORWARD}")
    title = (entry.get("title") or "").strip()[:400]
    items = crossref_get({"query.bibliographic": title, "filter": filt},
                         slug + ".q1", offline) or []
    student = f"{entry.get('name', '')} {entry.get('surname', '')}".strip()
    if student:
        items2 = crossref_get({"query.bibliographic": title[:200],
                               "query.author": student,
                               "filter": filt},
                              slug + ".q2", offline) or []
    else:
        items2 = []
    merged, seen = [], set()
    for it in items + items2:
        doi = (it.get("DOI") or "").lower()
        if doi and doi in seen:
            continue
        seen.add(doi)
        merged.append(slim_crossref(it))
    return merged



# --------------------------------------------------------------- matching

def tokens(text):
    """Lowercased, accent-folded content tokens with light plural folding."""
    text = unicodedata.normalize("NFKD", text or "")
    text = "".join(c for c in text if not unicodedata.combining(c))
    out = []
    for t in re.findall(r"[a-z0-9]+", text.lower()):
        if len(t) < 3 or t in STOPWORDS:
            continue
        if len(t) >= 5 and t.endswith("ies"):
            t = t[:-3] + "y"
        elif len(t) >= 4 and t.endswith("s") and not t.endswith("ss"):
            t = t[:-1]
        out.append(t)
    return out


def title_sims(a, b):
    """(token jaccard, string ratio) between two titles."""
    ta, tb = set(tokens(a)), set(tokens(b))
    jac = len(ta & tb) / len(ta | tb) if ta and tb else 0.0
    seq = difflib.SequenceMatcher(
        None, eg.foldcase(a or ""), eg.foldcase(b or "")).ratio()
    return jac, seq


def title_sim(a, b):
    return max(title_sims(a, b))


def abs_sim(a, b):
    ca, cb = Counter(tokens(a)), Counter(tokens(b))
    if not ca or not cb:
        return None
    dot = sum(n * cb.get(t, 0) for t, n in ca.items())
    na = sum(n * n for n in ca.values()) ** 0.5
    nb = sum(n * n for n in cb.values()) ** 0.5
    return dot / (na * nb)


def surname_key(s):
    return eg.foldcase(eg.strip_tussenvoegsel(s or ""))


def author_surnames(names):
    """Folded surnames of a list of display names, tolerating
    family-name-first orders."""
    out = set()
    for nm in names:
        out.add(surname_key(eg.split_full_name(nm)[0]))
        toks = nm.split()
        if toks:
            out.add(surname_key(toks[-1]))
    out.discard("")
    return out


def supervisor_surnames(entry):
    return {surname_key(eg.split_full_name(s.strip())[0])
            for s in (entry.get("supervisors") or "").split(";") if s.strip()}


def student_author_match(entry, name):
    """Whether a paper author looks like the thesis's student: overlapping
    surname tokens (a Spanish/Portuguese compound surname is often
    shortened to one part) plus, when both sides spell given names out, a
    given-name prefix agreement (initials alone are too weak: 'Agata
    Manolova' is not student 'Manuela Manolova', and 'Qingdong Wang' is
    not 'Qu Wang'); when either side uses initials, an initial overlap
    decides. Family-first orders ('Xu Weilin', 'W. Qiuxian') are handled
    explicitly."""
    def sur_toks(s):
        return {eg.foldcase(t) for t in s.split()
                if eg.foldcase(t) and t.lower() not in eg.TUSS_ENVGESELLS}

    def is_initial(tok):
        return bool(re.fullmatch(r"[A-Za-z]\.?", tok or ""))

    if not (entry.get("surname") and name):
        return False
    own_given = [g for g in re.split(r"[\s.]+",
                 (entry.get("name") or "").strip()) if g]
    surname, given = eg.split_full_name(name)
    given = [p for tok in given for p in re.split(r"[\s.]+", tok) if p]
    own_toks, auth_toks = sur_toks(entry["surname"]), sur_toks(surname)
    if auth_toks and (auth_toks == own_toks or auth_toks < own_toks):
        gi, oi = set(eg.initials(given)), set(eg.initials(own_given))
        if not gi or not oi:
            return True  # one side has no usable given name
        if is_initial(given[0]) or is_initial(own_given[0]):
            return bool(gi & oi)
        a, b = eg.foldcase(given[0]), eg.foldcase(own_given[0])
        return a == b or (len(a) >= 3 and len(b) >= 3
                          and (a.startswith(b[:3]) or b.startswith(a[:3])))
    toks = name.split()
    if len(toks) == 2:
        # family name first: "Xu Weilin" or "W. Qiuxian"
        if (surname_key(toks[0]) == surname_key(entry["surname"])
                and eg.foldcase(toks[1]) == eg.foldcase(entry.get("name")
                                                        or "")):
            return True
        if (re.fullmatch(r"[A-Za-z]\.", toks[0])
                and eg.foldcase(entry["surname"])[:1] ==
                eg.foldcase(toks[0])[:1]
                and eg.foldcase(toks[1]) == eg.foldcase(entry.get("name")
                                                        or "")):
            return True
    return False


def year_weight(dy):
    if 0 <= dy <= 3:
        return 1.0
    if dy == -1 or dy in (4, 5):
        return 0.85
    if 6 <= dy <= YEAR_FORWARD:
        return 0.6
    return 0.3


def evaluate(entry, cand, sup_keys):
    """Score one candidate against one thesis: the similarity components
    plus a verdict of 'likely'/'possible'/None. A Likely requires the
    student among the paper's authors (first authorship boosts the
    ranking); supervisor or title-only matches stay a Possible."""
    tj, ts = title_sims(entry.get("title") or "", cand.get("title") or "")
    t = max(tj, ts)
    b = abs_sim(entry.get("abstract") or "", cand.get("abstract") or "")
    authors = cand.get("authors") or []
    stu = any(student_author_match(entry, nm) for nm in authors)
    # the paper's first listed author (merged sources keep primary order)
    first = bool(authors) and student_author_match(entry, authors[0])
    surs = author_surnames(authors) & sup_keys
    dy = (cand.get("year") or 0) - int(entry.get("year") or 0)
    yw = year_weight(dy)
    near = 0 <= dy <= 6

    if stu and (t >= T_LIKELY_STU_TITLE
                or (b is not None and b >= T_LIKELY_STU_ABS)):
        verdict = "likely"
    elif stu and near and (t >= T_POSS_STU_TITLE
                           or (b is not None and b >= T_POSS_STU_ABS)):
        verdict = "possible"
    elif surs and near and (t >= T_POSS_SUP_TITLE
                            or (b is not None and b >= T_POSS_SUP_ABS)):
        verdict = "possible"
    elif tj >= T_POSS_TITLE and yw >= 0.85:
        verdict = "possible"
    else:
        verdict = None
    score = (2.0 * stu + 0.5 * first
             + 1.5 * (len(surs) / max(1, len(sup_keys)))
             + t + (b or 0.0) + 0.3 * yw)
    return {"stu": stu, "first": first, "surs": surs, "t": t, "b": b,
            "dy": dy, "yw": yw, "verdict": verdict, "score": score}


def pool_for(entry, gdmc, works_cache, offline, with_student, oa_ok):
    """Candidate pool for one thesis: GDMC papers and the works of the
    thesis's supervisors (and optionally student) in the year window, plus
    the per-thesis Crossref results, deduplicated by DOI or title+year
    (merging abstracts/authors/urls)."""
    y = int(entry.get("year") or 0)
    pool = [p for p in gdmc
            if p.get("year") and y - YEAR_BACK <= p["year"] <= y + YEAR_FORWARD]
    people = [(s.strip(), "supervisor")
              for s in (entry.get("supervisors") or "").split(";")
              if s.strip()]
    if with_student:
        people.append((f"{entry.get('name', '')} {entry['surname']}".strip(),
                       "student"))
    if oa_ok:
        for name, role in people:
            key = "p:" + eg.foldcase(name)
            if key not in works_cache:
                print(f"      OpenAlex works for {name} ({role})...",
                      flush=True)
                works_cache[key] = openalex_works_for(
                    name, offline, role,
                    year=y if role == "student" else None) or []
            pool.extend(works_cache[key])
    pool.extend(crossref_candidates(entry, offline))
    by_ident, out = {}, []
    for cand in pool:
        ident = (eg.foldcase(cand.get("doi") or "")
                 or eg.foldcase(cand.get("title") or "")[:60]
                 + str(cand.get("year") or ""))
        if ident in by_ident:
            old = by_ident[ident]
            if not old.get("abstract") and cand.get("abstract"):
                old["abstract"] = cand["abstract"]
            if not old.get("doi") and cand.get("doi"):
                old["doi"] = cand["doi"]
            if not old.get("url") and cand.get("url"):
                old["url"] = cand["url"]
            have = set(old.get("authors") or [])
            old["authors"] = list(old.get("authors") or []) + [
                a for a in cand.get("authors") or [] if a not in have]
        else:
            by_ident[ident] = dict(cand)
            out.append(by_ident[ident])
    return out


# --------------------------------------------------------------- verdicts

def load_verified():
    if not VERIFIED_FILE.exists():
        return []
    return yaml.safe_load(VERIFIED_FILE.read_text()) or []


def verified_keys(verified):
    keys = set()
    for v in verified:
        if (v.get("verdict") or "").strip().lower() != "not related":
            continue
        ident = (v.get("doi") or eg.foldcase(v.get("url") or ""))[:80]
        keys.add((eg.foldcase(v.get("author") or ""),
                  int(v.get("year") or 0), ident))
    return keys


def no_papers_keys(verified):
    """(author, year) pairs with an entry-level 'verdict: no papers':
    the whole thesis is skipped, not individual candidates (used when a
    former student's papers belong to their later PhD work, which no
    single candidate list captures)."""
    keys = set()
    for v in verified:
        if (v.get("verdict") or "").strip().lower() in ("no papers",
                                                        "no paper"):
            keys.add((eg.foldcase(v.get("author") or ""),
                      int(v.get("year") or 0)))
    return keys


def entry_is_skipped(entry, no_papers):
    year = int(entry.get("year") or 0)
    keys = {(eg.foldcase(entry.get("surname", "")), year),
            (eg.foldcase(f"{entry.get('name', '')} "
                         f"{entry.get('surname', '')}"), year)}
    return bool(keys & no_papers)


def candidate_keys(entry, cand):
    """Verdict-matching keys for one candidate. The verdict file's
    `author:` may be written as the bare surname or as the student's
    full name, so both forms are offered."""
    ident = (cand.get("doi") or eg.foldcase(cand.get("url")
                                            or cand.get("id") or ""))[:80]
    year = int(entry.get("year") or 0)
    return {(eg.foldcase(entry["surname"]), year, ident),
            (eg.foldcase(f"{entry.get('name', '')} "
                         f"{entry.get('surname', '')}"), year, ident)}


# ------------------------------------------------------------ calibration

def paper_doi(url):
    if not url:
        return ""
    m = re.search(r"(10\.\d{4,9}/[^\"\s]+)", url)
    return m.group(1).rstrip(".,)") if m else ""


def calibrate(entry, scored, sup_keys, args):
    """(status, how, components) with status 'surfaced', 'missed' or
    'uncheckable': would the search have surfaced the entry's linked
    paper? By DOI when the link carries one, by title match against the
    linked repository record when it points at one. `scored` holds
    (candidate, components) for the whole pool, verdict-filtered or not;
    the components of the matched candidate are returned so the
    thresholds stay calibrated."""
    want = paper_doi(entry.get("paper")).lower()
    matched = None
    if want:
        how = f"doi {want}"
        matched = next(((c, s) for c, s in scored
                        if c.get("doi") == want), None)
        if matched is None:
            return "missed", how + " (not among the candidates)", None
    else:
        um = re.search(r"uuid[:%3A]+([0-9a-fA-F-]{36})",
                       entry.get("paper") or "")
        if not um:
            return "uncheckable", "non-DOI, non-record link", None
        page = eg.fetch_record(um.group(1).lower(), args.delay, args.offline)
        rec = eg.parse_record(page) if page else {}
        title = rec.get("title") or ""
        if not title:
            return "uncheckable", "linked repository record unreadable", None
        best = 0.0
        for c, s in scored:
            ts = title_sim(title, c.get("title") or "")
            if ts > best:
                best, matched = ts, (c, s)
        how = f"record title (best similarity {best:.2f})"
        if best < 0.6:
            return "missed", how + " — no matching candidate", None
    (c, s) = matched
    sups = f"{len(s['surs'])}/{len(sup_keys)}"
    desc = (f"title {s['t']:.2f}, abstract "
            + ("n/a" if s["b"] is None else f"{s['b']:.2f}")
            + f", student co-author: {'yes' if s['stu'] else 'no'}"
            + f" (first author: {'yes' if s['first'] else 'no'})"
            + f", supervisors among authors: {sups}")
    status = "surfaced" if s["verdict"] else "missed"
    return status, f"{how} — {desc}", s


# ------------------------------------------------------------------ main

def paper_label(cand):
    t = (cand.get("type") or "").lower()
    if "journal" in t or t == "article":
        return "journal article"
    if "proceedings" in t or "conference" in t:
        return "conference paper"
    return cand.get("type") or "paper"


def describe_candidate(entry, cand, s, n):
    sup_full = {surname_key(eg.split_full_name(x.strip())[0]):
                eg.split_full_name(x.strip())[0]
                for x in (entry.get("supervisors") or "").split(";")
                if x.strip()}
    au, seen = [], set()
    for i, nm in enumerate(cand.get("authors") or []):
        mark = ""
        if student_author_match(entry, nm):
            mark = " (student; first author)" if i == 0 else " (student)"
        else:
            key = surname_key(eg.split_full_name(nm)[0])
            if key in s["surs"] and key in sup_full:
                mark = f" (supervisor: {sup_full[key]})"
        # the same person often appears twice after merging sources
        # ("J. Stoter" and "Jantien Stoter"); keep the marked variant
        ded = (surname_key(eg.split_full_name(nm)[0]), mark)
        if ded in seen:
            continue
        seen.add(ded)
        au.append(nm + mark)
    label = paper_label(cand)
    link = cand.get("url") or (f"https://doi.org/{cand['doi']}"
                               if cand.get("doi") else cand.get("id") or "")
    lines = [f'  {n}. "{cand.get("title")}" — '
             f'{(cand.get("venue") or "?")[:70]}, {cand.get("year")} — '
             f"[{label}]({link})"]
    lines.append("     - authors: " + ", ".join(au))
    bits = [f"title similarity {s['t']:.2f}",
            "abstract similarity "
            + ("n/a" if s["b"] is None else f"{s['b']:.2f}"),
            f"year {s['dy']:+d}"]
    lines.append("     - " + "; ".join(bits)
                 + f"  (source: {cand.get('source')})")
    return "\n".join(lines)


def write_report(archive, targets, results, calibration, n_gdmc, args):
    def has(e_cs, verdict):
        _, cs = e_cs
        return any(c[1]["verdict"] == verdict for c in cs)

    likely = [ec for ec in results if has(ec, "likely")]
    possible = [ec for ec in results
                if not has(ec, "likely") and has(ec, "possible")]
    nothing = [ec for ec in results
               if not has(ec, "likely") and not has(ec, "possible")]
    with_paper = sum(1 for e in archive
                     if e.get("paper") or e.get("papers"))
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with REPORT_FILE.open("w", encoding="utf-8") as f:
        f.write(f"# Paper cross-check ({datetime.now():%Y-%m-%d})\n\n")
        f.write(f"The archive holds {len(archive)} theses, {with_paper} of "
                f"which already link a paper. The other {len(targets)} "
                "were compared against the GDMC publication list "
                f"({n_gdmc} scientific/conference papers), Crossref "
                "(searched per thesis on title and student author) "
                + ("and OpenAlex works of their supervisors and students"
                   if args.openalex_used else "")
                + ", scoring candidates on co-authorship, title "
                "similarity and abstract similarity.\n\n"
                "Accepted papers go into the entry's `paper:` field in "
                "_data/geotheses.yml (optionally `paper_label:`), several "
                "at once as a `papers:` list of {url, label} entries; "
                "rejected candidates go into scripts/verified_papers.yml "
                "with `verdict: not related`, and a thesis to skip "
                "entirely with `verdict: no papers`.\n\n")

        def write_thesis(f, e, cs, cap, verdict):
            f.write(f"- **{e['name']} {e['surname']} ({e['year']})** — "
                    f"{(e.get('title') or '')[:80]}\n")
            top = [x for x in sorted(cs, key=lambda x: -x[1]["score"])
                   if x[1]["verdict"] == verdict]
            shown = top[:cap] if cap else top
            for n, (c, s) in enumerate(shown, 1):
                f.write(describe_candidate(e, c, s, n) + "\n")
            if len(top) > len(shown):
                f.write(f"  … and {len(top) - len(shown)} more "
                        f"{verdict} candidates; re-run with "
                        "--limit/--surname to see them all.\n")

        f.write(f"## Likely ({len(likely)} theses)\n\n"
                "Strong signals: the thesis's student as co-author "
                "(preferably first author) plus a clear title or "
                "abstract overlap.\n\n")
        if not likely:
            f.write("None.\n")
        for e, cs in likely:
            write_thesis(f, e, cs, cap=10, verdict="likely")

        f.write(f"\n## Possible ({len(possible)} theses)\n\n"
                "Weaker evidence; most of these are probably unrelated "
                "(a supervisor's other work, a namesake). Top candidates "
                "only.\n\n")
        if not possible:
            f.write("None.\n")
        for e, cs in possible:
            write_thesis(f, e, cs, cap=args.max_possible,
                         verdict="possible")

        f.write(f"\n## No candidates ({len(nothing)})\n\n")
        recent = [e for e, _ in nothing if int(e.get("year") or 0) >= 2025]
        older = [e for e, _ in nothing if int(e.get("year") or 0) < 2025]
        if older:
            f.write(", ".join(f"{e['surname']} ({e['year']})"
                              for e in older) + "\n")
        if recent:
            f.write(f"\nNo candidates found for {len(recent)} theses from "
                    "2025–2026 either, but those rarely have papers yet: ")
            f.write(", ".join(f"{e['surname']} ({e['year']})"
                              for e in recent) + "\n")

        n_surfaced = sum(1 for _, st, _, _ in calibration
                         if st == "surfaced")
        n_checkable = sum(1 for _, st, _, _ in calibration
                          if st in ("surfaced", "missed"))
        n_uncheckable = sum(1 for _, st, _, _ in calibration
                            if st == "uncheckable")
        f.write(f"\n## Calibration\n\nOf the {n_checkable} entries that "
                "already link a paper and can be checked automatically, "
                f"the search surfaced {n_surfaced} as a candidate "
                "(the rest had a title too far from the thesis's, or "
                "were not in the sources for this run)"
                + (f"; {n_uncheckable} more have a paper link this "
                   "script cannot verify automatically" if n_uncheckable
                   else "") + ":\n\n")
        for e, st, how, s in calibration:
            mark = {"surfaced": "surfaced", "missed": "**missed**",
                    "uncheckable": "not automatically checkable"}[st]
            f.write(f"- {mark} — {e['surname']} ({e['year']}): {how}\n")
    return likely, possible, nothing


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--offline", action="store_true",
                    help="work from the cache only, no network")
    ap.add_argument("--limit", type=int, default=0,
                    help="only check the first N theses (in year order)")
    ap.add_argument("--surname", default="",
                    help="debug: only check theses of this surname")
    ap.add_argument("--max-possible", type=int, default=4,
                    help="candidates reported per thesis in Possible")
    ap.add_argument("--no-students", action="store_true",
                    help="skip the per-student OpenAlex searches")
    ap.add_argument("--no-openalex", action="store_true",
                    help="skip OpenAlex entirely (GDMC + Crossref only)")
    ap.add_argument("--delay", type=float, default=20.0,
                    help="seconds between repository record fetches "
                         "(calibration only; robots.txt asks for 20)")
    args = ap.parse_args()

    archive = yaml.safe_load((REPO_ROOT / "_data" / "geotheses.yml")
                             .read_text())
    known = [e for e in archive if e.get("paper")]
    targets = [e for e in archive
               if not e.get("paper") and not e.get("papers")]
    if args.surname:
        targets = [e for e in targets
                   if args.surname.lower() in e.get("surname", "").lower()]
        known = [e for e in known
                 if args.surname.lower() in e.get("surname", "").lower()]
    targets.sort(key=lambda e: (int(e.get("year") or 0),
                                eg.foldcase(e.get("surname") or "")))
    if args.limit:
        targets = targets[:args.limit]

    gdmc, ok = load_gdmc_pubs(args.offline)
    if not ok:
        print("GDMC publication list unavailable or unparseable."
              if gdmc is not None else
              "GDMC publication list not in cache; run without --offline.")
        return 2
    print(f"Sources: GDMC lists {len(gdmc)} scientific/conference papers; "
          f"checking {len(targets)} theses without a paper link "
          f"(+{len(known)} known links for calibration).", flush=True)

    verified = verified_keys(load_verified())
    no_papers = no_papers_keys(load_verified())
    skipped = [e for e in targets if entry_is_skipped(e, no_papers)]
    if skipped:
        targets = [e for e in targets if not entry_is_skipped(e, no_papers)]
        print(f"Skipping {len(skipped)} thesis(es) with a 'no papers' "
              f"verdict: "
              + ", ".join(f"{e['surname']} ({e['year']})"
                          for e in skipped), flush=True)
    works_cache = {}
    oa_ok = (not args.no_openalex) and probe_openalex(args.offline)
    args.openalex_used = oa_ok

    def search_one(entry, with_student, keep_all=False):
        sup_keys = supervisor_surnames(entry)
        cands = []
        for cand in pool_for(entry, gdmc, works_cache, args.offline,
                             with_student, oa_ok):
            if candidate_keys(entry, cand) & verified:
                continue
            s = evaluate(entry, cand, sup_keys)
            if keep_all or s["verdict"]:
                cands.append((cand, s))
        return cands

    results = []
    for i, e in enumerate(targets, 1):
        print(f"[{i}/{len(targets)}] {e['surname']} ({e['year']})",
              flush=True)
        cands = search_one(e, with_student=False)
        if not any(c[1]["verdict"] == "likely" for c in cands) \
                and not args.no_students:
            cands = search_one(e, with_student=True)
        results.append((e, cands))
        if cands:
            print("      likely: %d, possible: %d" % (
                sum(1 for c in cands if c[1]["verdict"] == "likely"),
                sum(1 for c in cands if c[1]["verdict"] == "possible")),
                flush=True)
        else:
            print("      no candidates", flush=True)

    calibration = []
    for e in known:
        scored = search_one(e, with_student=True, keep_all=True)
        status, how, _ = calibrate(e, scored, supervisor_surnames(e), args)
        calibration.append((e, status, how, _))
        print(f"[calibration] {e['surname']} ({e['year']}): {status} — {how}",
              flush=True)

    write_report(archive, targets, results, calibration, len(gdmc), args)
    print(f"\nReport: {REPORT_FILE.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
