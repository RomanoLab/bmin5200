#!/usr/bin/env python3
"""
extract_imscc.py - Turn a Canvas IMS Common Cartridge (.imscc) export into a
readable, version-controllable folder tree.

An .imscc file is just a ZIP archive containing IMS Common Cartridge XML plus
Canvas's own `cccv1p0` extension XML. Nothing in it is proprietary; this script
walks the manifest and writes out one Markdown file per piece of course content,
alongside the original course files.

Usage:
    python3 extract_imscc.py COURSE.imscc [-o OUTPUT_DIR]

Output layout:
    OUTPUT_DIR/
        README.md                     inventory of what was extracted
        syllabus.md
        schedule.md                   from course_settings/events.xml
        course-settings.md            grading scheme, weights, late policy
        assignments/<slug>.md         YAML frontmatter + body
        discussions/<slug>.md
        quizzes/<slug>.md
        files/...                     the original course files, folder structure intact

Canvas writes file links as `$IMS-CC-FILEBASE$/Some%20Folder/file.pdf`. Those
tokens are rewritten to real relative paths pointing into `files/`.
"""

from __future__ import annotations

import argparse
import html
import os
import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote
from xml.etree import ElementTree as ET

CANVAS_NS = "{http://canvas.instructure.com/xsd/cccv1p0}"
CP_NS = "{http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1}"
FILEBASE = "$IMS-CC-FILEBASE$"


# --------------------------------------------------------------------------
# small helpers
# --------------------------------------------------------------------------

def slugify(text: str) -> str:
    """'Homework 1 - Logic' -> 'homework-1-logic'"""
    text = re.sub(r"[^\w\s-]", "", text.strip().lower())
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-") or "untitled"


def tag(elem: ET.Element) -> str:
    """Strip the namespace from an element tag."""
    return elem.tag.split("}")[-1]


def child_text(parent: ET.Element | None, name: str, default: str = "") -> str:
    if parent is None:
        return default
    node = parent.find(f"{CANVAS_NS}{name}")
    if node is None:
        node = parent.find(name)
    return (node.text or default).strip() if node is not None else default


def rewrite_filebase(text: str, depth: int) -> str:
    """
    Replace $IMS-CC-FILEBASE$/Foo%20Bar/x.pdf with ../files/Foo Bar/x.pdf,
    where the number of '../' segments matches how deep the output file sits.
    """
    prefix = "../" * depth + "files"

    def repl(match: re.Match) -> str:
        path = unquote(match.group(1))
        # Canvas appends query strings like ?canvas_=1&canvas_qs_wrap=1
        path = path.split("?")[0]
        return prefix + path

    return re.sub(re.escape(FILEBASE) + r"([^\"'\s>)]*)", repl, text)


def html_to_markdown(raw: str, depth: int = 1) -> str:
    """
    A deliberately small HTML -> Markdown converter. Canvas's rich-text output
    is a narrow subset of HTML (p, ul/ol/li, h1-h6, strong/em, a, img, table,
    br, hr), so a handful of regexes beats pulling in a dependency here.
    """
    if not raw:
        return ""

    text = raw
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", text, flags=re.S | re.I)

    # Drop the document scaffolding; keep only the body if one is present.
    body = re.search(r"<body[^>]*>(.*?)</body>", text, flags=re.S | re.I)
    if body:
        text = body.group(1)
    text = re.sub(r"</?(html|head|meta|title|body)[^>]*>", "", text, flags=re.I)

    # Links and images first, before generic tag stripping eats the attributes.
    text = re.sub(
        r'<img[^>]*?src="([^"]*)"[^>]*?alt="([^"]*)"[^>]*?>',
        lambda m: f"![{m.group(2)}]({m.group(1)})",
        text,
        flags=re.I,
    )
    text = re.sub(
        r'<img[^>]*?src="([^"]*)"[^>]*?>',
        lambda m: f"![]({m.group(1)})",
        text,
        flags=re.I,
    )
    text = re.sub(
        r'<a[^>]*?href="([^"]*)"[^>]*?>(.*?)</a>',
        lambda m: f"[{re.sub(r'<[^>]+>', '', m.group(2)).strip() or m.group(1)}]({m.group(1)})",
        text,
        flags=re.S | re.I,
    )

    # Tables -> pipe tables. Handled row by row so the header separator lands
    # in the right place.
    def table_repl(match: re.Match) -> str:
        rows = re.findall(r"<tr[^>]*>(.*?)</tr>", match.group(1), flags=re.S | re.I)
        out: list[str] = []
        for i, row in enumerate(rows):
            cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, flags=re.S | re.I)
            cleaned = [
                re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", c)).strip() for c in cells
            ]
            if not cleaned:
                continue
            out.append("| " + " | ".join(cleaned) + " |")
            if i == 0:
                out.append("|" + "|".join([" --- "] * len(cleaned)) + "|")
        return "\n\n" + "\n".join(out) + "\n\n"

    text = re.sub(r"<table[^>]*>(.*?)</table>", table_repl, text, flags=re.S | re.I)

    # Block and inline elements.
    for level in range(1, 7):
        text = re.sub(
            rf"<h{level}[^>]*>(.*?)</h{level}>",
            lambda m, lv=level: f"\n\n{'#' * lv} " + re.sub(r"<[^>]+>", "", m.group(1)).strip() + "\n\n",
            text,
            flags=re.S | re.I,
        )
    text = re.sub(r"<(strong|b)[^>]*>(.*?)</\1>", r"**\2**", text, flags=re.S | re.I)
    text = re.sub(r"<(em|i)[^>]*>(.*?)</\1>", r"*\2*", text, flags=re.S | re.I)
    text = re.sub(r"<code[^>]*>(.*?)</code>", r"`\1`", text, flags=re.S | re.I)
    text = re.sub(r"<li[^>]*>(.*?)</li>", r"\n- \1", text, flags=re.S | re.I)
    text = re.sub(r"</?(ul|ol)[^>]*>", "\n", text, flags=re.I)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"<hr\s*/?>", "\n\n---\n\n", text, flags=re.I)
    text = re.sub(r"</p>", "\n\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)

    text = html.unescape(text)
    text = text.replace("\xa0", " ")
    text = rewrite_filebase(text, depth)

    # Tidy whitespace.
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    lines = [line.rstrip() for line in text.split("\n")]
    return "\n".join(lines).strip() + "\n"


def frontmatter(fields: dict[str, str]) -> str:
    out = ["---"]
    for key, value in fields.items():
        if value in (None, ""):
            continue
        value = str(value).replace('"', "'")
        out.append(f'{key}: "{value}"' if re.search(r"[:#]", value) else f"{key}: {value}")
    out.append("---")
    return "\n".join(out) + "\n\n"


# --------------------------------------------------------------------------
# extraction
# --------------------------------------------------------------------------

class CartridgeExtractor:
    def __init__(self, cartridge: Path, outdir: Path) -> None:
        self.zip = zipfile.ZipFile(cartridge)
        self.outdir = outdir
        self.names = set(self.zip.namelist())
        self.manifest = ET.fromstring(self.zip.read("imsmanifest.xml"))
        self.counts = {"assignments": 0, "discussions": 0, "quizzes": 0, "files": 0}
        self.groups = self._assignment_groups()

    # -- course settings ---------------------------------------------------

    def _assignment_groups(self) -> dict[str, dict[str, str]]:
        path = "course_settings/assignment_groups.xml"
        if path not in self.names:
            return {}
        root = ET.fromstring(self.zip.read(path))
        groups = {}
        for node in root:
            ident = node.get("identifier", "")
            groups[ident] = {
                "title": child_text(node, "title"),
                "weight": child_text(node, "group_weight"),
            }
        return groups

    def write_course_settings(self) -> None:
        path = "course_settings/course_settings.xml"
        if path not in self.names:
            return
        root = ET.fromstring(self.zip.read(path))
        lines = ["# Course settings\n"]
        lines.append(f"- **Title:** {child_text(root, 'title')}")
        lines.append(f"- **Course code:** {child_text(root, 'course_code')}")
        lines.append(f"- **Time zone:** {child_text(root, 'time_zone')}")
        lines.append(f"- **Grading standard enabled:** {child_text(root, 'grading_standard_enabled')}")

        lines.append("\n## Assignment groups\n")
        lines.append("| Group | Weight |")
        lines.append("| --- | --- |")
        for group in self.groups.values():
            weight = group["weight"]
            lines.append(f"| {group['title']} | {weight}% |" if weight else f"| {group['title']} | — |")

        late = "course_settings/late_policy.xml"
        if late in self.names:
            lroot = ET.fromstring(self.zip.read(late))
            lines.append("\n## Late policy\n")
            for node in lroot:
                lines.append(f"- **{tag(node)}:** {(node.text or '').strip()}")

        standards = "course_settings/grading_standards.xml"
        if standards in self.names:
            sroot = ET.fromstring(self.zip.read(standards))
            lines.append("\n## Grading standard\n")
            for node in sroot.iter():
                if tag(node) == "title":
                    lines.append(f"- {(node.text or '').strip()}")

        (self.outdir / "course-settings.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    def write_syllabus(self) -> None:
        path = "course_settings/syllabus.html"
        if path not in self.names:
            return
        raw = self.zip.read(path).decode("utf-8", "replace")
        body = html_to_markdown(raw, depth=0)
        (self.outdir / "syllabus.md").write_text("# Syllabus\n\n" + body, encoding="utf-8")

    def write_schedule(self) -> None:
        path = "course_settings/events.xml"
        if path not in self.names:
            return
        root = ET.fromstring(self.zip.read(path))
        rows = []
        for event in root:
            title = child_text(event, "title")
            start = child_text(event, "start_at")
            if not title:
                continue
            rows.append((start, title))
        rows.sort()
        lines = ["# Calendar events (as exported)\n", "| Start | Event |", "| --- | --- |"]
        for start, title in rows:
            lines.append(f"| {start.replace('T', ' ')} | {title} |")
        (self.outdir / "schedule.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # -- content types -----------------------------------------------------

    def write_assignments(self) -> None:
        target = self.outdir / "assignments"
        target.mkdir(exist_ok=True)
        for name in sorted(self.names):
            if not name.endswith("assignment_settings.xml"):
                continue
            root = ET.fromstring(self.zip.read(name))
            title = child_text(root, "title") or "Untitled assignment"
            folder = name.rsplit("/", 1)[0]

            body_file = next(
                (n for n in sorted(self.names)
                 if n.startswith(folder + "/") and n.endswith(".html")),
                None,
            )
            body = ""
            if body_file:
                body = html_to_markdown(self.zip.read(body_file).decode("utf-8", "replace"), depth=1)
                # The exported HTML repeats the title as an <h1>; drop it.
                body = re.sub(r"^#\s*Assignment:.*?\n", "", body).strip() + "\n"

            group_ref = child_text(root, "assignment_group_identifierref")
            group = self.groups.get(group_ref, {})

            meta = frontmatter({
                "title": title,
                "type": "assignment",
                "points_possible": child_text(root, "points_possible"),
                "grading_type": child_text(root, "grading_type"),
                "assignment_group": group.get("title", ""),
                "group_weight": f"{group['weight']}%" if group.get("weight") else "",
                "due_at": child_text(root, "due_at"),
                "unlock_at": child_text(root, "unlock_at"),
                "lock_at": child_text(root, "lock_at"),
                "submission_types": child_text(root, "submission_types"),
                "allowed_extensions": child_text(root, "allowed_extensions"),
                "workflow_state": child_text(root, "workflow_state"),
                "canvas_identifier": root.get("identifier", ""),
            })
            out = target / f"{slugify(title)}.md"
            out.write_text(meta + f"# {title}\n\n" + body, encoding="utf-8")
            self.counts["assignments"] += 1

    def write_discussions(self) -> None:
        target = self.outdir / "discussions"
        target.mkdir(exist_ok=True)

        # Canvas splits each discussion across two files: a `topicMeta` record
        # holding the settings, and a plain IMS `topic` holding the text. The
        # meta file points at the topic file via <topic_id>.
        metas: dict[str, ET.Element] = {}
        topics: dict[str, ET.Element] = {}
        for name in self.names:
            if "/" in name or not name.endswith(".xml"):
                continue
            try:
                root = ET.fromstring(self.zip.read(name))
            except ET.ParseError:
                continue
            stem = name[:-4]
            if tag(root) == "topicMeta":
                metas[stem] = root
            elif tag(root) == "topic":
                topics[stem] = root

        for meta_root in metas.values():
            title = child_text(meta_root, "title") or "Untitled discussion"
            topic_id = child_text(meta_root, "topic_id")
            topic_root = topics.get(topic_id)

            body = ""
            if topic_root is not None:
                for node in topic_root.iter():
                    if tag(node) == "text":
                        body = html_to_markdown(node.text or "", depth=1)
                        break

            meta = frontmatter({
                "title": title,
                "type": "discussion",
                "discussion_type": child_text(meta_root, "discussion_type"),
                "workflow_state": child_text(meta_root, "workflow_state"),
                "posted_at": child_text(meta_root, "posted_at"),
                "canvas_identifier": meta_root.get("identifier", ""),
            })
            out = target / f"{slugify(title)}.md"
            # Two 2025 threads share a title; keep both rather than clobbering.
            counter = 2
            while out.exists():
                out = target / f"{slugify(title)}-{counter}.md"
                counter += 1
            out.write_text(meta + f"# {title}\n\n" + body, encoding="utf-8")
            self.counts["discussions"] += 1

    def write_quizzes(self) -> None:
        target = self.outdir / "quizzes"
        for name in sorted(self.names):
            if not name.endswith("assessment_meta.xml"):
                continue
            target.mkdir(exist_ok=True)
            root = ET.fromstring(self.zip.read(name))
            title = child_text(root, "title") or "Untitled quiz"
            description = child_text(root, "description")
            meta = frontmatter({
                "title": title,
                "type": "quiz",
                "quiz_type": child_text(root, "quiz_type"),
                "points_possible": child_text(root, "points_possible"),
                "due_at": child_text(root, "due_at"),
                "unlock_at": child_text(root, "unlock_at"),
                "lock_at": child_text(root, "lock_at"),
                "canvas_identifier": root.get("identifier", ""),
            })
            body = html_to_markdown(description, depth=1)
            (target / f"{slugify(title)}.md").write_text(
                meta + f"# {title}\n\n" + body, encoding="utf-8"
            )
            self.counts["quizzes"] += 1

    def write_files(self) -> None:
        target = self.outdir / "files"
        for name in self.names:
            if not name.startswith("web_resources/") or name.endswith("/"):
                continue
            rel = name[len("web_resources/"):]
            dest = target / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            with self.zip.open(name) as src, open(dest, "wb") as out:
                while chunk := src.read(1 << 20):
                    out.write(chunk)
            self.counts["files"] += 1

    def write_readme(self, cartridge: Path) -> None:
        title = ""
        for node in self.manifest.iter():
            if tag(node) == "string" and not title:
                title = (node.text or "").strip()
        lines = [
            f"# {title or cartridge.stem}",
            "",
            f"Extracted from `{cartridge.name}` by `tools/extract_imscc.py`.",
            "",
            "This is a **reference copy** of the Canvas export, not the live course site.",
            "Everything here came out of the IMS Common Cartridge; nothing was authored by hand.",
            "",
            "## What was recovered",
            "",
            f"- {self.counts['assignments']} assignments -> `assignments/`",
            f"- {self.counts['discussions']} discussion threads -> `discussions/`",
            f"- {self.counts['quizzes']} quiz -> `quizzes/`",
            f"- {self.counts['files']} course files -> `files/`",
            "- Syllabus -> `syllabus.md`",
            "- Calendar events -> `schedule.md`",
            "- Grading scheme, weights, late policy -> `course-settings.md`",
            "",
            "## What the export did not contain",
            "",
            "- **Modules.** The manifest's `<organizations>` block is empty, so the weekly",
            "  module structure did not survive the export.",
            "- **Pages.** `wiki_content/` is present but empty.",
            "- **Student data.** Submissions, grades, and roster are never included in an",
            "  `.imscc`; those stay in Canvas.",
            "",
            "File links that Canvas wrote as `$IMS-CC-FILEBASE$/...` have been rewritten to",
            "relative paths into `files/`.",
            "",
        ]
        (self.outdir / "README.md").write_text("\n".join(lines), encoding="utf-8")

    def run(self, cartridge: Path) -> None:
        self.outdir.mkdir(parents=True, exist_ok=True)
        self.write_syllabus()
        self.write_schedule()
        self.write_course_settings()
        self.write_assignments()
        self.write_discussions()
        self.write_quizzes()
        self.write_files()
        self.write_readme(cartridge)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("cartridge", type=Path, help="path to the .imscc file")
    parser.add_argument("-o", "--output", type=Path, default=None,
                        help="output directory (default: ./extracted)")
    args = parser.parse_args()

    if not args.cartridge.is_file():
        print(f"error: no such file: {args.cartridge}", file=sys.stderr)
        return 1

    outdir = args.output or Path("extracted")
    extractor = CartridgeExtractor(args.cartridge, outdir)
    extractor.run(args.cartridge)

    counts = extractor.counts
    print(f"Extracted to {outdir}/")
    print(f"  assignments : {counts['assignments']}")
    print(f"  discussions : {counts['discussions']}")
    print(f"  quizzes     : {counts['quizzes']}")
    print(f"  files       : {counts['files']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
