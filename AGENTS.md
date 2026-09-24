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
python3 scripts/check_geotheses.py
```

## Structure

| Path | Purpose |
|---|---|
| `_data/theses_*.yml` / `.yaml` | Thesis data files by cohort |
| `_posts/*.md` | News items (rendered on homepage) |
| `_layouts/` | Jinja-like HTML templates (default, page, post) |
| `_includes/` | Reusable partials (head, thesis_entries) |
| `assets/css/` | Bulma + FontAwesome + custom `geo2022.css` |
| `rules/`, `templates/`, `faq/`, etc. | Content pages (markdown) |
| `scripts/fetch_mycase.py` | MyCase metadata fetcher (output gitignored) |
| `_data/geotheses.yml` | Completed-thesis archive data (2013–today) |
| `scripts/enrich_geotheses.py` | Cleans/enriches the archive from repository records + MyCase |
| `scripts/check_geotheses.py` | Validates the archive data |

## Conventions

- Permalinks: `pretty` (no `.html` suffix)
- `future: true` in `_config.yml` — future-dated posts are visible
- Base URL: `/geo2022` (not root)
- CI (GitHub Actions) runs `jekyll build --trace` on push to `main`
- The `jekyll-redirect-from` plugin is available
- No package manager (Gemfile), no asset bundler — raw CSS in `assets/css/`
