# Working on this repo with Claude

Context for BMIN 5200 (Foundations of AI in Health), Penn, Fall 2026. Read this before changing
anything — several things here look like oversights and are actually decisions.

## What this is

A course taught Thursdays 3:30–6:30pm, Aug 27 – Dec 3 2026, 3600 Civic Center Blvd room 6E 031.
Fall 2026 moved it off Canvas; Canvas is kept only for assignment submission and grades, because
Penn requires it. Everything else is this repo plus Penn Box.

Published at **https://bmin5200.jdr.bio** from `RomanoLab/bmin5200`.

## Decisions — do not silently reverse these

**The site is light-only.** Dark text on a light background in every browser, regardless of the
reader's OS theme. There is one palette and a `color-scheme: light` on `:root`. Do not add a
`prefers-color-scheme: dark` block; one was deliberately removed.

**One column.** No side-by-side text blocks at any width. A `.cols` grid was removed on purpose.
New sections stack as ordinary content inside `<main>`.

**Headings and copy are blunt.** No flowery language, no corporate speak, nothing that reads as
AI-generated. "A typical meeting" became "Example lecture itinerary" — that is the register.
Prefer plain nouns over marketing phrasing, and cut rule-of-three flourishes and filler openers
("In practical terms,").

**No JavaScript on the site.** Nothing on the page needs it. This is why the sidebar nav has no
scroll-spy highlight — that would require JS. Do not add a framework, a build system, or a
dependency; `index.html` is one hand-written file that works when opened directly.

**Lecture content is unchanged from 2025.** Topics and the PowerPoint decks must not be
significantly altered. The refactor changed structure, not subject matter.

## Things that will bite you

**Never commit anything copyrighted.** `old-canvas/` is gitignored: 763 MB of publisher
copyrighted journal club PDFs, the 2025 decks, and two 228 MB cartridge files. This repo is
public — it has to be, or the Colab links break. Papers and slides live on Box behind PennKey.

**`links.tsv` is the only place Box URLs go.** The site and notebooks use `LINK::key`
placeholders; `tools/apply_links.py` resolves them into `build/`. Never paste a Box URL into
`index.html`. Box URLs change whenever a file is re-uploaded, which is the whole point.

**`build/` is generated.** `apply_links.py` deletes and rebuilds the entire directory every run.
Editing anything inside it is throwing work away. It is gitignored; the Actions workflow builds
it at deploy time.

**`new-course-site/CNAME` is load-bearing.** It binds the custom domain, and it only survives
into `build/` because it is listed in `PASSTHROUGH` in `apply_links.py`. If it stops being
copied, GitHub drops the custom domain on the next deploy.

**Domain verification belongs to RomanoLab.** Verifying a domain protects it and its immediate
subdomains from other GitHub accounts, and verifying a domain already in use elsewhere
immediately releases it from that account's Pages sites. Verifying `jdr.bio` under the personal
account `jdromano2` would knock this site offline.

**Do not keep a working copy inside Box or another sync folder.** Box's sync client corrupts
`.git` internals. This repo was deliberately moved out of Box for that reason.

## Layout

```
new-course-site/   The site. index.html (one file), CNAME, .nojekyll.
exercises/         13 Colab notebooks, one per meeting. Must stay in the repo —
                   the site's links resolve against the public repo.
tools/             apply_links.py (link resolver), extract_imscc.py (Canvas export reader)
links.tsv          Every Box URL, in one table.
syllabus-2026.md   Source for the syllabus PDF on Box.
journal-club-2026.md
.github/workflows/ pages.yml — builds and deploys on push to main.
old-canvas/        [gitignored] Canvas export. Source material, kept locally only.
```

## Editing the site

Details are in `new-course-site/README.md`: how schedule rows work, the sidebar nav anchors, the
link placeholders, and what changes each year (dates, `links.tsv`, journal club papers, homework
due dates). Read it before restructuring anything.

## Deploying

Push to `main`. The workflow resolves links and publishes `build/new-course-site/`. To see what
is still unfilled: `python3 tools/apply_links.py --check`. Once `links.tsv` is complete, add
`--strict` to the workflow's build step so an unfilled placeholder fails the build instead of
shipping a dead link.
