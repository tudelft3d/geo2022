#!/usr/bin/env python3
"""Validate _data/geotheses.yml (the completed-thesis archive data).

Checks that every entry has the required fields, that links are
well-formed (no leftover "missing" notes, repository links use the
canonical resolver form), that there are no duplicate person/year
combinations, and — when the thesis images have been added — that every
image field points to a file that exists.

Warnings cover quality (missing abstract/supervisors); errors are things
that break the site or the data. Exit status is non-zero on errors, so
this can double as a CI check once the images are in.

Usage:
  python3 scripts/check_geotheses.py
  python3 scripts/check_geotheses.py --img-dir theses/archive/img --strict
"""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = REPO_ROOT / "_data" / "geotheses.yml"

REQUIRED = ["surname", "name", "title", "year"]  # link is checked separately
UUID_RE = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-"
                     r"[0-9a-f]{12}$")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--img-dir", default=None,
                    help="directory with the thesis images (e.g. "
                         "theses/archive/img); image files are checked "
                         "when given")
    ap.add_argument("--strict", action="store_true",
                    help="treat missing images as errors")
    args = ap.parse_args()

    entries = yaml.safe_load(DATA_FILE.read_text())
    errors, warnings = [], []

    people = Counter()
    for i, e in enumerate(entries, 1):
        who = f"entry {i} ({e.get('surname', '?')} {e.get('year', '?')})"
        for field in REQUIRED:
            if not str(e.get(field, "")).strip():
                errors.append(f"{who}: missing required field '{field}'")

        link = str(e.get("link", ""))
        if link.lower().startswith("missing"):
            errors.append(f"{who}: link still starts with 'missing'")
        elif not link:
            msg = f"{who}: missing required field 'link'"
            (warnings if e.get("needs_review") else errors).append(msg)
        elif "uuid" in link:
            if not link.startswith("https://resolver.tudelft.nl/uuid:"):
                warnings.append(f"{who}: link not in canonical resolver "
                                f"form: {link}")
            uuid = link.rsplit(":", 1)[-1]
            if not UUID_RE.match(uuid):
                errors.append(f"{who}: malformed uuid in link: {link}")
        elif not link.startswith("http"):
            errors.append(f"{who}: unrecognised link: {link}")

        if not isinstance(e.get("year"), int):
            errors.append(f"{who}: year is not an integer")

        image = e.get("image")
        if image and args.img_dir:
            if not (REPO_ROOT / args.img_dir / image).is_file():
                msg = f"{who}: image '{image}' not in {args.img_dir}"
                (errors if args.strict else warnings).append(msg)
        elif not image:
            warnings.append(f"{who}: no image field")

        if not e.get("abstract"):
            warnings.append(f"{who}: no abstract")
        if not e.get("supervisors"):
            warnings.append(f"{who}: no supervisors")

        key = (str(e.get("surname", "")).lower(),
               str(e.get("name", "")).lower(), e.get("year"))
        people[key] += 1

    for (surname, name, year), n in people.items():
        if n > 1:
            errors.append(f"duplicate entry: {surname} {name} {year} "
                          f"appears {n} times")

    years = Counter(e.get("year") for e in entries)
    print(f"{len(entries)} entries, "
          f"{len(errors)} error(s), {len(warnings)} warning(s)")
    print("entries per year:",
          ", ".join(f"{y}: {years[y]}" for y in sorted(years, reverse=True)))
    for msg in errors:
        print(f"ERROR: {msg}")
    for msg in warnings:
        print(f"warn:  {msg}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
