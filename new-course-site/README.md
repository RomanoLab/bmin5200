# Course site

One hand-written HTML file. No build system, no dependencies, no framework. Open
`index.html` in a browser and it works.

## Publishing

The site is live at **https://bmin5200.jdr.bio**, on GitHub Pages.

Publishing is automatic. `.github/workflows/pages.yml` runs on every push to `main`: it runs
`tools/apply_links.py` to resolve the `LINK::` placeholders, then publishes
`build/new-course-site/`. To change anything — a link, a schedule row, a heading — edit the
source, push, and the site updates in about a minute. Watch the **Actions** tab if it doesn't.

`build/` is generated, never committed. It is in `.gitignore`. Do not edit anything inside it;
the next build deletes the whole directory and writes it again.

Two files in this directory exist only for the deploy and are not part of the page:

- **`CNAME`** — contains `bmin5200.jdr.bio`. Note that this file does **not** bind the domain in
  the current setup: GitHub ignores a `CNAME` file when publishing from a custom Actions
  workflow, and reads one only when publishing from a branch. The live domain is set under
  Settings -> Pages -> Custom domain. The file is kept as documentation and as a fallback for
  branch publishing, and `PASSTHROUGH` in `apply_links.py` copies it into `build/`.
- **`.nojekyll`** — stops GitHub running the published files through Jekyll, which would
  otherwise ignore anything starting with an underscore.

### `favicons/`

The browser tab icon: the same biohazard mark as `jdr.bio`, of which this site is a subdomain.
The files were copied from `JDRomano2/jdr.bio` (`src/assets/icons/`) and are referenced by the
`<link rel="icon">` tags at the top of `index.html`. `PASSTHROUGH` in `apply_links.py` copies the
whole directory into `build/`, so adding another size needs no change to the script.

The directory is named `favicons`, not `icons`, on purpose: `.gitignore` carries an `Icon?` rule
for the marker files Box and the macOS Finder leave behind, and git's case-insensitive matching on
macOS makes that rule swallow a directory named `icons`.

### The DNS side

The repo is owned by the **RomanoLab** organization. `bmin5200` is a CNAME record pointing at
`romanolab.github.io.`, managed in **Netlify DNS** (`jdr.bio` uses Netlify's nameservers,
`dns1–4.p01.nsone.net`). The apex `jdr.bio` is a separate Netlify-hosted site and is not
affected by anything in this repo.

`romanolab.github.io` itself returns 404 — that is expected and fine. There is no organization
Pages site; the CNAME target only routes the request to GitHub's Pages infrastructure, which
then matches it to this repo by the `CNAME` file above.

**Domain verification belongs to the org, not to a personal account.** Verifying a domain
protects it *and its immediate subdomains* from other GitHub accounts — and verifying a domain
already in use elsewhere immediately releases it from that account's Pages sites. So if
`jdr.bio` is ever verified, verify it under **RomanoLab**. Verifying it under `jdromano2`
would knock this site offline.

## Editing

### The schedule

Every class meeting is one `<tr>` in the table at the bottom of `index.html`. To change a week,
edit the four cells. To add one, copy an existing row.

Rows have three shapes:

- normal — a regular meeting
- `class="off"` — no class (Fall Break, Thanksgiving); greyed and italicized
- `class="due"` — a meeting where something is due (kept as a semantic marker)

The links cell holds up to four links, in this order: **Slides · Notebook · Paper · Homework**.
Leave out any that don't apply.

Bold marks a deadline, and only the deadline. Put `class="due-item"` on the link itself — the
`HW N due` entries have it — not on the row. An earlier version bolded the whole links cell of a
`tr.due` row, which emphasised that week's slides and paper too and left the bold pointing at
nothing in particular. The emphasis survives the TBA rewrite, so a deadline still reads as a
deadline before its file is posted.

### The sidebar nav

The nav on the left is a plain nested `<ul>` of `#anchor` links, hard-coded near the top of
`<body>`. Every `<h2>` and `<h3>` in the content column carries an `id`; the nav points at those
ids. If you rename or add a heading, add or change its `id` and the matching nav entry — nothing
generates the list. Below 60rem the sidebar drops to a row of top-level links above the content
and the sub-entries are hidden.

There is no scroll-spy highlight of the current section, because that needs JavaScript and this
page has none.

### One column

The content column is single-column on purpose — no side-by-side text blocks, at any width. The
old `.cols` grid is gone. If you add a section, add it as ordinary stacked content inside
`<main>`.

### Links

Do not paste Box URLs into the HTML. Every link is written as a placeholder — `LINK::` followed
by a key — and the real URLs live in `links.tsv` at the repo root. There are around 40 of them,
and a Box URL changes whenever a file is re-uploaded, so keeping them in one table saves a lot
of hunting.

Until a key has a URL, its link is **not rendered as a link**. `apply_links.py` rewrites any
anchor whose href still holds a placeholder into `<span class="tba">`, which the stylesheet shows
greyed with a "(TBA)" suffix and no click target. So the schedule stays complete and readable all
semester, and nothing ever ships as a link that 404s. Fill the key in `links.tsv`, push, and that
entry becomes a live link on the next deploy — this is the intended week-by-week workflow.

### Releasing a notebook

The 13 in-class notebooks are a special case: they live in this repo, so there is no upload to
wait for. Their Colab URLs are already written into `links.tsv`, but **commented out**, which
leaves them greyed as "(TBA)" like everything else. To release one week's notebook, delete the
leading `#` on its `notebook-weekNN` line, commit, and push. To pull it back, restore the `#`.

To see what is still missing:

```bash
python3 tools/apply_links.py --check
```

It prints every unfilled key and the file it appears in. `--strict` makes it exit non-zero,
which is useful if you ever wire this into CI.

One key is not a URL: `github-repo` is just `owner/repo`, because it gets substituted into both
`github.com/...` and the Colab notebook links.

### Styling

All CSS is in a single `<style>` block at the top, driven by a handful of custom properties at
the very start. Change `--accent` to recolor the whole page.

The page is light-only: dark text on a light background in every browser, no matter what the
reader's OS theme is set to. There is one palette, so a color change happens in one place.
`color-scheme: light` on `:root` keeps scrollbars and form controls light to match. If you ever
want the OS theme respected again, add a `@media (prefers-color-scheme: dark)` block overriding
the same custom properties and drop the `color-scheme` line.

## Next year

Four things change:

1. **Dates.** Every `<td class="date">`, plus the header and the two Fall Break / Thanksgiving
   rows. Check Penn's academic calendar; the break weeks move.
2. **`links.tsv`.** New Box uploads mean new URLs. Blank the file and refill it.
3. **Journal club papers.** The `<span class="jc">` line inside each topic cell, and the
   corresponding `paper-weekNN` keys.
4. **Homework due dates.** In the Resources section and in the schedule's links cells.

Nothing else should need touching.

## What deliberately is not here

- **No syllabus copy.** The Course Information section carries what students actually look up —
  format, grading, policies, dates. The authoritative syllabus is a PDF on Box, generated from
  `syllabus-2026.md` at the repo root. Keeping the full text in two places guarantees they
  drift apart.
- **No file hosting.** Slides and papers stay on Box behind PennKey. The papers are copyrighted;
  they must not be committed to a public repository.
- **No JavaScript.** Nothing on the page needs it.
