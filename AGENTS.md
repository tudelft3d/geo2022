# AGENTS.md — geo2022

## What this is

Jekyll static site for TU Delft MSc Geomatics graduation thesis info (GEO2022).  
Hosted at `https://geomatics.bk.tudelft.nl/geo2022/`.

## Commands

```sh
# Local dev (requires Ruby + jekyll, jekyll-redirect-from gems)
jekyll serve --trace

# Production build
jekyll build --trace

# Pull thesis metadata (title, supervisors, planning, agreements, ...) for
# all open + closed cases from MyCase into mycase/ (gitignored; requires
# NetID + MFA login in a browser window on first run, python requests +
# playwright). Use to check whether _data/theses_*.yml is complete.
python3 scripts/fetch_mycase.py

# Clean + enrich the completed-thesis archive (_data/geotheses.yml) from the
# repository record pages (cached in .geotheses_cache/, gitignored; the
# repository's robots.txt asks for a 20 s crawl-delay, so the first full run
# takes ~1.5 h and later runs only fetch new records) and from MyCase's
# closed cases. Writes geotheses.yml.original (backup) and
# geotheses_report.md (issues needing a manual look).
python3 scripts/enrich_geotheses.py           # add --fetch-only / --offline

# Validate the archive data (required fields, canonical links, duplicate
# people; image files when given --img-dir). Exit code is CI-usable.
python3 scripts/check_geotheses.py --img-dir theses/img

# Cross-check the archive against the MSc theses on 3d.bk.tudelft.nl and
# gdmc.nl (both cached in .geotheses_cache/). Investigates archive gaps
# via the repository's Programme field and the GDMC thesis PDFs' title
# pages, and writes missing_theses_report.md (confirmed gaps, candidates
# for a manual look, verified non-Geomatics). Exit 1 while confirmed
# gaps remain; --add appends them to the archive flagged needs_review.
# Hand verdicts go in scripts/verified_theses.yml.
python3 scripts/find_missing_theses.py          # add --offline / --no-pdf

# Sweep the repository for pre-coverage theses (the GDMC / 3dge lists only
# reach back to the archive's start) by supervisor surname: searches the
# repository's search API for MSc theses whose supervisors include someone
# from scripts/geomatics_supervisors.yml, fetches record pages for the
# older ones and writes old_theses_report.md (confirmed gaps, likely,
# name collisions). --add appends the first two buckets flagged
# needs_review; hand verdicts go in scripts/verified_theses.yml.
python3 scripts/find_old_theses.py          # add --offline / --from-year / --all-years

# Sync _data/ongoing_theses.yml (Current Theses page) with MyCase's open
# cases: adds new starters (flagged needs_summary), syncs phases/
# supervisors/official titles, reports who is no longer open. --prune
# removes entries without an open case. Read-only without MyCase data.
python3 scripts/update_theses.py
```

## Per-quarter maintenance workflow

After each graduation round (or whenever, really):

1. `python3 scripts/fetch_mycase.py` — refresh MyCase data (login needed).
2. `python3 scripts/update_theses.py` — sync the Current Theses page:
   write a proposal summary (+ image in `theses/img/`, name it in the
   entry) for each `needs_summary` starter and drop the flag; check the
   COHORT notes (February starts are ambiguous in MyCase).
3. When students have their final thesis: run
   `python3 scripts/enrich_geotheses.py` — it appends closed cases that
   are missing from the archive, fetches their repository records
   (abstract, supervisors, graduation date) and writes
   `geotheses_report.md` for anything needing a manual look. Then
   `python3 scripts/update_theses.py --prune` to drop them from the
   ongoing page.
4. `python3 scripts/check_geotheses.py --img-dir theses/img` —
   validate the archive (errors should stay at zero).
5. `python3 scripts/find_missing_theses.py` — cross-check the archive
   against the GDMC and 3d.bk.tudelft.nl lists (writes
   `missing_theses_report.md`; exit 1 while confirmed gaps remain).
   Add the confirmed gaps (or re-run with `--add`, which flags them
   `needs_review`) and work through the report's candidates.
6. Cover images for new archive entries go into `theses/img/` under the
   entry's `image` filename (salvaged proposal-era images are already
   there for many entries; replace them with final-thesis covers as
   they arrive). Ongoing-thesis images go into `ongoing/img/`.

## Structure

| Path | Purpose |
|---|---|
| `_data/ongoing_theses.yml` | Current theses (open MyCase cases), synced by `scripts/update_theses.py` |
| `_data/geotheses.yml` | Completed-thesis archive data (2013–today) |
| `_posts/*.md` | News items (rendered on homepage) |
| `_layouts/` | Jinja-like HTML templates (default, page, post) |
| `_includes/` | Reusable partials (head, thesis_current, thesis_archive) |
| `assets/css/` | Bulma + FontAwesome + custom `geo2022.css` |
| `rules/`, `templates/`, `faq/`, etc. | Content pages (markdown) |
| `ongoing/` | Current Theses page (`/ongoing/`); images in `ongoing/img/` |
| `theses/` | Thesis archive page (`/theses/`); cover images in `theses/img/` |
| `scripts/fetch_mycase.py` | MyCase metadata fetcher (output gitignored) |
| `scripts/update_theses.py` | Syncs ongoing theses with MyCase open cases |
| `scripts/enrich_geotheses.py` | Cleans/enriches the archive from repository records + MyCase |
| `scripts/check_geotheses.py` | Validates the archive data |
| `scripts/find_missing_theses.py` | Cross-checks the archive with the GDMC + 3dge thesis lists |
| `scripts/find_old_theses.py` | Sweeps the repository for pre-coverage theses by supervisor surname |
| `scripts/geomatics_supervisors.yml` | Supervisor list feeding `find_old_theses.py` (status `yes`/`pending`) |

## Conventions

- Permalinks: `pretty` (no `.html` suffix)
- `future: true` in `_config.yml` — future-dated posts are visible
- Base URL: `/geo2022` (not root)
- CI (GitHub Actions) runs `jekyll build --trace` on push to `main`
- The `jekyll-redirect-from` plugin is available
- No package manager (Gemfile), no asset bundler — raw CSS in `assets/css/`
