#!/bin/sh
# Build the syllabus PDF and place it where the site serves it from.
#
# Run this after editing syllabus-2026.tex, then commit the resulting
# new-course-site/syllabus-2026.pdf. Nothing in CI compiles TeX -- that is
# deliberate, so a LaTeX error cannot fail the site deploy.
#
# SOURCE_DATE_EPOCH pins the timestamp PDFTeX embeds. Without it every rebuild
# produces a different 216 KB binary even when nothing changed, and since the
# PDF is committed that means a noisy diff on every run. With it, an unchanged
# .tex rebuilds to a byte-identical PDF and git sees no change at all.
set -e
cd "$(dirname "$0")"

export SOURCE_DATE_EPOCH=1756684800   # 2026-09-01T00:00:00Z, fixed on purpose
export FORCE_SOURCE_DATE=1

latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build-tex syllabus-2026.tex
cp build-tex/syllabus-2026.pdf new-course-site/syllabus-2026.pdf

echo "wrote new-course-site/syllabus-2026.pdf -- commit it if it changed"
