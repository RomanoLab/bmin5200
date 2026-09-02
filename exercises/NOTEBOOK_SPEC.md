# BMIN 5200 in-class exercise notebooks — authoring spec

Read this before writing any notebook. Every notebook must follow it exactly so the
13 sessions feel like one course, not thirteen one-offs.

## The course

BMIN 5200 "Foundations of AI in Health", Perelman School of Medicine, University of
Pennsylvania. Instructor: Joseph D. Romano, PhD ("Joe"). Graduate course, ~20 students,
mixed doctoral / master's / professional. It is a **symbolic and deductive AI** course —
knowledge representation, logic, ontologies, search, rule-based expert systems, Bayesian
networks — with machine learning arriving only near the end as contrast. It is explicitly
*not* an ML course.

Students have some Python but are not software engineers. Many are clinicians or
clinically-oriented researchers. Assume they can read a `for` loop and call a function;
do not assume they know decorators, classes, generators, or `numpy` broadcasting.

Class meets Thursdays 3:30–6:30pm. These exercises occupy **25–30 minutes** of that
window, immediately after the lecture, and replace time that used to go to a second
journal club paper. They are done in class, together, on students' laptops.

## Non-negotiable technical constraints

1. **Runs in Google Colab with zero setup.** First code cell installs anything needed:
   `%pip install -q <packages>`. Nothing that requires a GPU, an API key, a paid service,
   or a login.
2. **Runs top-to-bottom in under 2 minutes on CPU.** It will be verified with
   `jupyter nbconvert --execute`. If a cell is slow, shrink the problem.
3. **No external data downloads** except where explicitly noted below (Week 3 uses the
   public RxNav REST API and must degrade gracefully to a bundled fallback if the
   network is unavailable). Generate data inline with a fixed seed
   (`rng = np.random.default_rng(5200)`) so every student sees identical numbers and Joe
   can refer to a specific value out loud.
4. **Self-contained.** No imports from sibling notebooks, no relative file paths, no
   `resources/` directory. One `.ipynb`, nothing else.
5. **Clinically framed.** Every example uses biomedical or health-system content —
   patients, labs, diagnoses, drugs, trial eligibility, EHR fields. Never `foo`/`bar`,
   never the iris dataset, never generic "customer churn". Synthetic data is fine and
   expected; say plainly in the notebook that it is synthetic.
6. **Python 3.11+.** Use `numpy`, `pandas`, `matplotlib`, `networkx` freely. Do not use
   `seaborn`. Plots use matplotlib defaults — no custom styling, no color cycling code.

## Required notebook structure

Cells in this order:

1. **Title cell** (markdown), exactly this shape:

   ```markdown
   # BMIN 5200 — Week N in-class exercise
   ## <Exercise title>

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LINK::github-repo/blob/main/exercises/weekNN.ipynb)

   **Time:** ~25 minutes · **Pairs with:** <lecture deck topic>

   ### Tasks
   - <bullet>
   - <bullet>
   - <bullet>

   ### Background
   <Two or three sentences connecting the exercise to real biomedical practice. Not
   filler — say something a clinician would find true.>
   ```

   Headings are descriptive noun phrases, not vivid ones. `## Part 4 — Combinatorial limits`,
   not `## Part 4 — Where this approach dies`; `Common errors`, not `Common gotchas`. The body
   prose can be as direct as it likes — the headings stay flat and academic.

      Leave `LINK::github-repo` verbatim. A separate script substitutes it at deploy time.
   `weekNN` is zero-padded: `week01.ipynb` … `week13.ipynb`.

2. **Setup cell** (code) — installs and imports, quiet:

   ```python
   %pip install -q <packages>          # omit this line entirely if only stdlib/numpy/pandas/matplotlib/networkx are needed
   import numpy as np
   ...
   rng = np.random.default_rng(5200)
   ```

   `numpy`, `pandas`, `matplotlib`, and `networkx` are preinstalled in Colab — do not
   install them.

3. **Body** — alternating short markdown cells and code cells. Rules for the body:
   - Markdown explanation cells are **3–6 sentences**. This is a live class; nobody reads
     a wall of text with the instructor talking.
   - Structure the body as **3 or 4 numbered parts** (`## Part 1 — ...`). Part 1 is
     worked *for* them (they run it and read the output). Later parts contain the actual
     exercise.
   - Every exercise cell is a real, runnable cell with a `# TODO:` comment marking exactly
     what to write, and enough scaffolding that a student who freezes still has something
     to run. Never leave a cell that raises on execution — use a working-but-naive
     placeholder the student improves, or complete the code and ask them to *predict* the
     output before running it. **This matters: `nbconvert --execute` must succeed.**
   - Include at least one **"predict before you run"** moment — ask the class to commit
     to an answer in a markdown cell, then reveal it in the next code cell. This is the
     single most useful thing you can do with 25 minutes.
   - Include at least one place where the naive approach visibly **fails or scales badly**,
     and the notebook says why. Students remember the failure, not the success.
   - Print output that is readable out loud. Prefer a small formatted table or a labeled
     print over a raw repr dump.

4. **Discussion cell** (markdown, near the end) — `## Discussion`, with 2–3 questions
   for the room. These should not have clean answers.

5. **Solutions cell(s)** (final section) — `## Solutions`, one markdown cell noting these
   are the completed versions of the TODOs, then the filled-in code as **markdown code
   blocks, not executable cells**, so students who scroll ahead don't accidentally run
   them and so the notebook's own execution stays fast.

## House style

- Comments explain *why*, not *what*. `# Entailment fails the moment one model satisfies
  KB but not the query` is useful; `# loop over rows` is not.
- Variable names are domain words: `patient`, `wbc`, `inclusion_met`, `posterior` —
  not `x`, `df2`, `temp`.
- No emoji. No exclamation marks. No "Great job!" or "Now let's have some fun!" — write
  the way a careful instructor talks to graduate students.
- Prefer plain Python that shows the mechanism over a library call that hides it, *unless*
  the point of the exercise is the library. Students are here to learn how deduction
  works, so a 15-line hand-rolled model checker beats `sympy.satisfiable` — then use the
  library afterward to check their answer.
- Where the lecture deck already covers something, say so: "This is the KB from slide 94."

## Verification before you report back

For each notebook you write:

```bash
cd /home/claude/bmin5200/exercises
jupyter nbconvert --to notebook --execute --inplace weekNN.ipynb --ExecutePreprocessor.timeout=180
```

It must exit 0. Then clear outputs so the committed notebook is clean:

```bash
jupyter nbconvert --ClearOutputPreprocessor.enabled=True --to notebook --inplace weekNN.ipynb
```

Report which notebooks executed cleanly and anything you had to compromise on.
