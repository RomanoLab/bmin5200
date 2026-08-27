#!/usr/bin/env python3
"""
apply_links.py - Fill the LINK:: placeholders in the course site and notebooks.

The site and the exercise notebooks are written with placeholder tokens like
`LINK::slides-week03` instead of real URLs. This keeps Box URLs (which are long,
ugly, and change whenever a file is re-uploaded) in exactly one place:
`links.tsv`.

Workflow:

    1. Open links.tsv, paste the real URL next to each key.
    2. Run:  python3 tools/apply_links.py
    3. Check the report, commit, push.

The script never edits the source files in place. It writes resolved copies to
`build/`, which is what you publish. Re-run it any time a link changes.

Commands:

    python3 tools/apply_links.py            build into ./build
    python3 tools/apply_links.py --check    report what is still missing, write nothing
    python3 tools/apply_links.py --strict   build, but exit non-zero if anything is unfilled
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

TOKEN = re.compile(r"LINK::([A-Za-z0-9][A-Za-z0-9._-]*)")

# An <a> whose href still holds an unresolved placeholder. Matched after
# substitution, so anything left here has no URL in links.tsv yet.
DEAD_ANCHOR = re.compile(
    r'<a\s(?P<attrs>[^>]*href="[^"]*LINK::[^"]*"[^>]*)>(?P<label>.*?)</a>',
    re.DOTALL,
)


def _inert_span(m: "re.Match") -> str:
    """Replace a dead link with inert text, preserving deadline emphasis.

    A deadline is still a deadline even when the file has not been posted, so
    due-item survives the rewrite; the item shows as bold grey "HW 1 due (TBA)".
    """
    classes = "tba due-item" if "due-item" in m.group("attrs") else "tba"
    return f'<span class="{classes}">{m.group("label")}</span>'


def deactivate_dead_links(text: str, suffix: str) -> tuple[str, int]:
    """Turn links to unposted material into inert text.

    A placeholder left in an href would render as an ordinary link that 404s
    when a student clicks it, which is worse than showing nothing. In HTML the
    anchor becomes <span class="tba">, styled grey and unclickable by the
    stylesheet. In notebooks there is no styling to lean on, so the token is
    replaced with a plain marker.
    """
    if suffix == ".html":
        return DEAD_ANCHOR.subn(_inert_span, text)
    if suffix == ".ipynb":
        return TOKEN.subn("(not yet posted)", text)
    return text, 0

# Files the script rewrites, relative to the repo root.
TARGETS = [
    "new-course-site/index.html",
    "exercises/*.ipynb",
    "exercises/README.md",
]

# Copied into build/ untouched.
#
# CNAME binds the custom domain (bmin5200.jdr.bio). build/ is deleted and
# rebuilt on every run, so anything not listed here vanishes from the published
# tree -- and a published tree with no CNAME makes GitHub drop the domain.
PASSTHROUGH = [
    "new-course-site/CNAME",
    "new-course-site/.nojekyll",
    "exercises/requirements.txt",
]


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def load_links(path: Path) -> dict[str, str]:
    """Read links.tsv. Two whitespace-separated columns: key, url.

    Tab is the convention, but any spacing works. # starts a comment.
    """
    if not path.is_file():
        sys.exit(f"error: {path} not found. Copy links.tsv.example and fill it in.")

    links: dict[str, str] = {}
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        # Split on ANY run of whitespace, not just a tab. Neither a key nor a
        # URL can contain whitespace, so this is unambiguous -- and an editor
        # that silently converts tabs to spaces used to make the key look
        # unfilled with no error at all.
        parts = line.split()
        if len(parts) == 1:
            continue  # key present, URL still blank
        if len(parts) != 2:
            sys.exit(f"error: {path}:{lineno}: expected 'key<TAB>url', got: {raw!r}")
        key, url = parts
        if key in links:
            sys.exit(f"error: {path}:{lineno}: duplicate key {key!r}")
        links[key] = url
    return links


def collect_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for pattern in TARGETS:
        if "*" in pattern:
            files.extend(sorted(root.glob(pattern)))
        else:
            candidate = root / pattern
            if candidate.is_file():
                files.append(candidate)
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true",
                        help="report unfilled placeholders, write nothing")
    parser.add_argument("--strict", action="store_true",
                        help="exit non-zero if any placeholder is unfilled")
    parser.add_argument("--links", type=Path, default=None, help="path to links.tsv")
    parser.add_argument("--out", type=Path, default=None, help="output directory (default: build/)")
    args = parser.parse_args()

    root = repo_root()
    links = load_links(args.links or root / "links.tsv")
    outdir = args.out or root / "build"

    files = collect_files(root)
    if not files:
        sys.exit("error: no target files found. Are you running this from the repo?")

    # Longest keys first, so `paper-week10` is never eaten by a prefix match.
    ordered = sorted(links, key=len, reverse=True)

    used: set[str] = set()
    missing: dict[str, list[str]] = {}
    written = 0
    deactivated = 0

    if not args.check:
        if outdir.exists():
            shutil.rmtree(outdir)
        outdir.mkdir(parents=True)

    for path in files:
        text = path.read_text(encoding="utf-8")

        for key in ordered:
            token = f"LINK::{key}"
            if token in text:
                text = text.replace(token, links[key])
                used.add(key)

        for leftover in sorted(set(TOKEN.findall(text))):
            missing.setdefault(leftover, []).append(str(path.relative_to(root)))

        # Unposted material must never ship as a clickable link that 404s.
        text, killed = deactivate_dead_links(text, path.suffix)
        deactivated += killed

        if not args.check:
            dest = outdir / path.relative_to(root)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(text, encoding="utf-8")
            written += 1

    if not args.check:
        for pattern in PASSTHROUGH:
            src = root / pattern
            if src.is_file():
                dest = outdir / pattern
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dest)
                written += 1

    # ---- report --------------------------------------------------------

    total_keys = len(links) + len(missing)
    print(f"links.tsv     : {len(links)} filled, {len(missing)} still blank "
          f"({total_keys} total)")
    if not args.check:
        print(f"wrote         : {written} files -> {outdir.relative_to(root)}/")
    if deactivated:
        print(f"deactivated   : {deactivated} link(s) to unposted material "
              f"(shown greyed as TBA, not clickable)")

    unused = sorted(set(links) - used)
    if unused:
        print(f"\nunused keys (in links.tsv but not referenced anywhere):")
        for key in unused:
            print(f"  {key}")

    if missing:
        print(f"\nSTILL NEEDED - {len(missing)} link(s):")
        width = max(len(k) for k in missing)
        for key in sorted(missing):
            where = ", ".join(sorted(set(missing[key])))
            print(f"  {key:<{width}}  ({where})")
        print("\nAdd these to links.tsv and re-run.")
        if args.strict:
            return 1
    else:
        print("\nAll placeholders resolved.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
