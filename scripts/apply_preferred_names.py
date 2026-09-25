#!/usr/bin/env python3
"""Rewrite the supervisors fields in _data/geotheses.yml through the
canonical people table in scripts/preferred_names.yml: every alias
(initials variant, spelling variant) becomes the person's preferred
display name.

Dry-run by default: prints what would change. Pass --write to apply.

Strings that are not in the table are left untouched and reported, so
new theses with new supervisor spellings can never be silently dropped
-- add them to preferred_names.yml instead.
"""
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

try:
    from enrich_geotheses import DATA_FILE, write_yaml
except ImportError:  # pragma: no cover
    DATA_FILE = REPO_ROOT / "_data" / "geotheses.yml"

    def write_yaml(entries):
        """Fallback writer matching enrich_geotheses.py's format."""
        ordered = sorted(entries, key=lambda e: (-int(e.get("year") or 0),
                                                 str(e.get("surname", "")).lower(),
                                                 str(e.get("name", "")).lower()))
        body = yaml.safe_dump(ordered, allow_unicode=True, width=72,
                              sort_keys=False, default_flow_style=False)
        DATA_FILE.write_text(body, encoding="utf-8")


NAMES_FILE = Path(__file__).resolve().parent / "preferred_names.yml"


def load_mapping():
    table = yaml.safe_load(NAMES_FILE.read_text())["people"]
    mapping = {}
    for person in table:
        for alias in [person["name"], *person.get("aliases", [])]:
            if alias in mapping and mapping[alias] != person["name"]:
                raise SystemExit(f"alias {alias!r} maps to both "
                                 f"{mapping[alias]!r} and {person['name']!r}")
            mapping[alias] = person["name"]
    return mapping


def main():
    do_write = "--write" in sys.argv[1:]
    mapping = load_mapping()
    entries = yaml.safe_load(DATA_FILE.read_text())

    changed, unmapped = 0, set()
    for e in entries:
        sups = [s.strip() for s in (e.get("supervisors") or "").split("; ")
                if s.strip()]
        for s in sups:
            if s not in mapping:
                unmapped.add(s)
        deduped = list(dict.fromkeys(mapping.get(s, s) for s in sups))
        if deduped != sups:
            changed += 1
            print(f"{e.get('surname')} {e.get('year')}: "
                  f"{'; '.join(sups)}  ->  {'; '.join(deduped)}")

    print(f"\n{changed} of {len(entries)} entries would change; "
          f"{len(unmapped)} unmapped strings")
    for s in sorted(unmapped):
        print(f"  unmapped: {s}")
    if do_write:
        if unmapped:
            print("not writing: resolve the unmapped strings first "
                  "(add them to preferred_names.yml)")
            return 1
        for e in entries:
            sups = [s.strip() for s in (e.get("supervisors") or "").split("; ")
                    if s.strip()]
            e["supervisors"] = "; ".join(dict.fromkeys(mapping[s] for s in sups))
        write_yaml(entries)
        print(f"wrote {DATA_FILE}")
    elif changed:
        print("(dry run; re-run with --write to apply)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
