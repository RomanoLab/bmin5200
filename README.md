# BMIN 5200 — Foundations of Artificial Intelligence in Health

Course materials for BMIN 5200, Perelman School of Medicine, University of Pennsylvania.

Fall 2026 moved this course off Canvas. Canvas is still used for assignment submission and
grades, because Penn requires it; everything else — the schedule, the slides, the papers, the
assignment specifications, and thirteen in-class coding notebooks — lives here and on Penn Box.

## Layout

```
new-course-site/       The public course site. One hand-written HTML file.
exercises/             13 Colab-ready notebooks, one per class meeting.
tools/                 extract_imscc.py, apply_links.py
old-canvas/            The Canvas export and a readable extraction of it.  [not committed]
links.tsv              Every Box URL in the project, in one table.
syllabus-2026.tex      Syllabus source. Run ./build-syllabus.sh, commit the PDF.
build-syllabus.sh      Compiles the syllabus into new-course-site/ (reproducibly).
journal-club-2026.md   Paper selection and format for the reduced journal club.
.github/workflows/     pages.yml — builds and deploys the site on push to main.
```

### What is not in the repository

`old-canvas/` is gitignored and stays in the Box folder only. It is 763 MB of copyrighted
journal club PDFs, the 2025 decks, assignment archives, and two 228 MB cartridge files — GitHub
rejects anything over 100 MB, and this repository is public because the Colab links require it.
It is source material for the refactor, not part of the course site.

Everything else is committed. In particular **`exercises/` must be**: the notebook links on the
site are `colab.research.google.com/github/RomanoLab/bmin5200/blob/main/exercises/weekNN.ipynb`,
which Colab resolves against the public repo. No notebooks in the repo means thirteen dead links.
`tools/` and `links.tsv` must be there too — the deploy workflow runs `apply_links.py` from the
repository root.

## Publishing the site

The site is live at **https://bmin5200.jdr.bio** (GitHub Pages, custom domain).

Pushing to `main` publishes it. `.github/workflows/pages.yml` runs
`tools/apply_links.py` — which fills the `LINK::` placeholders from `links.tsv` into `build/` —
and deploys `build/new-course-site/`. `build/` is generated and gitignored; nothing about the
deploy needs doing by hand.

To see which Box URLs are still unfilled:

```bash
python3 tools/apply_links.py --check
```

Details, including how the custom domain is wired up, are in `new-course-site/README.md`.

## What changed from Fall 2025

**Journal club halved.** 22 papers (two a week) became 11 (one a week). Students now present in
pairs, so everyone still presents exactly once. See `journal-club-2026.md`.

**Coding exercises added.** The reclaimed ~25 minutes each week goes to a hands-on notebook.
Previously the only code students wrote was in four take-home assignments; the first of those
contains no code at all. See `exercises/README.md`.

**Calendar rebuilt for 13 meetings.** Penn's Fall 2026 breaks (Oct 1–4, Nov 26–29) take out two
Thursdays. Thirteen meetings, thirteen lecture topics, one per week. No class time is spent on
final presentations — those remain recorded videos, as in 2025.

**Materials moved to Box.** Slides and journal club PDFs are behind PennKey SSO. Nothing
copyrighted is committed to this repository.

Lecture content itself is unchanged. The decks are the 2025 decks.

## The Canvas export

`old-canvas/` holds the original `.imscc` cartridge and `extracted/`, a readable copy produced
by `tools/extract_imscc.py`. An `.imscc` is a plain ZIP of IMS Common Cartridge XML — the
extractor walks the manifest and writes Markdown with the Canvas metadata preserved as YAML
frontmatter.

To regenerate:

```bash
python3 tools/extract_imscc.py old-canvas/*.imscc -o old-canvas/extracted
```

Two things the export did **not** contain, worth knowing if you ever need to go back to it: the
manifest's `<organizations>` block is empty, so the Canvas module structure did not survive, and
`wiki_content/` is empty, so there are no Pages. Student submissions and grades are never
included in a cartridge.
