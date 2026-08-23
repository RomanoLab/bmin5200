# Journal club — Fall 2026

## What changed

Fall 2025 ran **22 papers**: two per week for eleven weeks, roughly 40 minutes of class time.
Fall 2026 runs **11 papers**: one per week for eleven weeks, roughly 25 minutes.

The reclaimed time goes to the in-class coding exercise. The reasoning: students were reading
two papers a week and writing no code, in a course whose syllabus promises that all programming
would be done in Python. One paper read properly beats two skimmed.

Two knock-on changes:

- **Presenters work in pairs.** With ~20 students and 11 slots, two students share each paper —
  one presents background and methods, the other results and critique, and both field
  discussion. Everybody presents exactly once.
- **The second-paper extra credit is retired.** It existed to cover 22 slots with ~20 students.
  There is nothing left for it to solve.

The LLM-driven critique stays. It remains the one sanctioned use of generative AI in the
course, and it works better with one paper than two.

## Papers

Each paper is matched to the week whose lecture it argues with. Every PDF was already in the
2025 course files; nothing new needs to be sourced.

| Week | Date | Lecture topic | Paper | Why this one |
| --- | --- | --- | --- | --- |
| 3 | Sep 10 | Semantic networks, frames, ontologies | Babalou et al. | Ontology matching and merging — the problem that appears the moment you have two vocabularies for one domain |
| 4 | Sep 17 | Heuristic, local & population-based search | Wolpert & Macready (1997) | No Free Lunch. The paper that says your favorite search algorithm has no general claim to being better |
| 5 | Sep 24 | Biologically-inspired search | Nagarajan & Babu | Evolutionary methods applied to a biomedical optimization problem |
| 6 | Oct 8 | Rules & knowledge-based systems | Shortliffe et al. (1973) | MYCIN. Still the clearest statement of what a clinical rule base was supposed to do, and why it did not deploy |
| 7 | Oct 15 | Building an expert system (CLIPS) | Michalowski et al. | A modern clinical decision support system built on explicit rules — the thing they are about to build in Homework 3 |
| 8 | Oct 22 | Bayesian networks; state machines | Leclerc et al. | Probabilistic graphical models on clinical data |
| 9 | Oct 29 | Information theory & machine learning | Shen et al. | The transition from deduction to induction, in a biomedical setting |
| 10 | Nov 5 | Deep learning & LLMs | Vaswani et al. (2017) | Attention Is All You Need. Read the actual paper, not a summary of it |
| 11 | Nov 12 | Explainable AI | Behrad et al. | Explainability methods surveyed specifically for medical applications |
| 12 | Nov 19 | Bias & fairness in AI | Pfohl et al. | Fairness in clinical prediction, with the metric trade-offs made concrete |
| 13 | Dec 3 | Agentic AI | Thirunavukarasu et al. | LLMs in medicine — the closest thing to a sober assessment of what is actually deployable |

> The 2025 PDF for the Week 13 paper is filed as `Thirunakukarasu et all.pdf`; the author is
> Thirunavukarasu. Worth renaming when the papers move to Box.

## Papers moved out of journal club

**Newell & Simon (1956)** and **Turing (1950)** are now assigned as short readings for Weeks 1
and 2 rather than presentations. Both decks already walk through these papers slide by slide
(the Logic Theorist section in Week 1, the Turing Test section in Week 1), so a presentation
largely restates the lecture. As readings they set up the Week 1 ELIZA exercise directly.

**Dropped entirely** (available if you want to swap one back in): Naz et al., Squires et al.,
Sung & Chi, Rodrigues de Araújo et al., Sadik et al., Shamshad et al., Balagopalan et al.,
Combi et al., Ladbury et al. Most are second surveys on a topic the paired paper already
covers.

## Format

Unchanged from 2025 except for length and pairing.

**~25 minutes total per week:**

- 12–15 minutes presentation: background, methods, results, the authors' conclusions
- 3 minutes: the LLM-driven critique (below)
- 8–10 minutes: discussion questions posed by the presenters, who then lead the discussion

All students are expected to have read the paper and to participate. The subject matter of each
paper is previewed in class two weeks before the presentation date.

### The LLM-driven critique

Presenters must run the paper past an LLM chatbot of their choice, ask it to critique the work,
and bring the result to class. They present:

1. What the model flagged
2. Which of those criticisms are actually correct
3. Which are confidently wrong, and how they could tell

Point 3 is the one that matters. This is the only place in BMIN 5200 where generative AI use is
permitted, and the point of permitting it is to make students practice catching it being wrong
on material they have read closely enough to check.

## Signup

The 2025 signup ran as a Canvas quiz where students entered their top five paper IDs. That
still works and requires no change — it is a Canvas gradebook artifact, not course content, so
it stays in Canvas rather than moving to the course site.

Assignments are distributed in the second week of the semester so that the Week 3 presenters
have two weeks of lead time.
