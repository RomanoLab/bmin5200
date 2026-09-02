# Software setup

Everything in BMIN 5200 runs in **Google Colab**, in a browser. There is nothing to install and
nothing to configure. If you have a laptop and a Google account, you are already set up.

Read the first section. The rest is for people who want to work locally, or who hit a problem.

---

## The short version

1. Bring a laptop to every class.
2. Open the week's notebook from the [course website](https://bmin5200.jdr.bio) — the
   **Notebook** link on the schedule row.
3. It opens in Colab. Click **Copy to Drive** before you type anything.
4. Run the cells.

That is the whole setup.

---

## Colab

### Signing in

Colab needs a Google account. Your PennO365 account is *not* a Google account — if you do not
already have one, create a personal Google account, or use an existing one. Nothing in this
course is submitted through Colab, so it does not matter which account you use.

### Copy to Drive, first

Notebook links from the course website open the file **read-only, straight from GitHub**. You can
run it, but your edits are not saved anywhere, and closing the tab loses your work.

Click **Copy to Drive** (top-left, under the menu bar) before you start. That makes your own copy
in your Google Drive, under `Colab Notebooks/`, and that copy is what you should work in. Do this
first, every week — it is the single most common thing people forget.

### Running cells

- **Shift+Enter** runs the current cell and moves to the next.
- **Runtime → Run all** runs the notebook top to bottom.
- Cells depend on the ones above them. If something is undefined, you probably skipped a cell.

### If the runtime disconnects

Colab disconnects idle sessions. Reconnecting gives you a **fresh machine**: your variables are
gone and any package you installed is gone with them, though your notebook text is safe.

Fix: **Runtime → Restart and run all**. Do not debug a half-executed notebook — start it over.
Everything in these notebooks runs in well under a minute.

### Do I need a GPU?

No. Nothing in this course needs one, including the deep learning week. Leave the runtime on CPU.
Switching to a GPU costs you quota and makes the notebook slower to start.

---

## Working locally (optional)

You do not need this. It is here if you would rather use your own editor.

Requires **Python 3.10 or newer**. Check with `python3 --version`.

```bash
git clone https://github.com/RomanoLab/bmin5200.git
cd bmin5200/exercises

python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

jupyter lab
```

Use a virtual environment. Installing this into your system Python will eventually break
something else on your machine.

The dependency list is `exercises/requirements.txt`, annotated by which week needs what.

### Two things that install slowly

- **`torch`** (Week 10) is a large download — expect a gigabyte or more, and several minutes. If
  you only want Parts 1 and 2 of that notebook, `tokenizers` alone is enough; `requirements.txt`
  says so at the relevant line.
- **`clipspy`** (Week 7) builds a C extension. On macOS this needs the Xcode command line tools
  (`xcode-select --install`); on Debian/Ubuntu, `build-essential` and `python3-dev`. On Windows it
  is genuinely awkward — **use Colab for Week 7 and for Homework 3.** This is the one place where
  local setup is meaningfully harder than the browser, and it is not worth your time to fight.

---

## Homework

Homework is written in Jupyter notebooks (except Homework 3, which is a CLIPS `.clp` file) and
**submitted through Canvas** — not through Colab, not by email.

To submit a notebook you worked on in Colab: **File → Download → Download .ipynb**, then upload
that file to Canvas.

Before you submit, do a **Runtime → Restart and run all** on a fresh runtime and confirm it runs
clean top to bottom. A notebook that only works because of a variable you defined an hour ago and
deleted the cell for is the most common way to lose points for no reason.

Deadlines are **11:59pm on Wednesdays**, the night before the class that reviews the answers.
Because we go through the answers in class the next afternoon, late work receives a zero — see the
syllabus. If something comes up, email Joe *before* the deadline.

---

## Troubleshooting

**"ModuleNotFoundError" for something the notebook installed earlier.**
Your runtime restarted. Run the install cell again, or Runtime → Restart and run all.

**"Cannot save changes" / edits disappear.**
You are in the read-only GitHub copy. Click **Copy to Drive** and work in your copy.

**A cell runs forever.**
Interrupt it (Runtime → Interrupt execution). In these notebooks anything running more than about
a minute is a bug, usually an infinite loop in a search or chaining exercise — not slowness.

**The notebook produces obviously wrong output — zeros, or five search algorithms returning
identical answers.**
That is expected and intended. Exercise cells ship with placeholders that run but are visibly
wrong, so nothing crashes during class. Those are the `TODO`s. Wrong-looking output means there is
still one to fill in.

**Everything is broken and class starts in five minutes.**
Open a fresh copy of the notebook from the course website and re-copy to Drive. You lose your
edits, not the class.

---

## Getting help

Ask early rather than late — this is the whole policy.

- In class, before or after
- Office hours (scheduled by poll in the first week)
- Email Joe: <joseph.romano@pennmedicine.upenn.edu>

If you email about something not working, include what you ran, the full error message, and
whether you were in Colab or local. It saves a round trip.
