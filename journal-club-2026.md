# Journal club — Fall 2026

## What changed

Fall 2025 ran **22 papers**: two per week for eleven weeks, roughly 40 minutes of class time.
Fall 2026 runs **11 papers**: one per week for eleven weeks, roughly 25 minutes.

The reclaimed time goes to the in-class coding exercise. The reasoning: students were reading
two papers a week and writing no code, in a course whose syllabus promises that all programming
would be done in Python. One paper read properly beats two skimmed.

Three knock-on changes:

- **Each paper covers the _previous_ week's lecture topic.** In 2025 a paper was matched to the
  week whose lecture it argued with, which meant presenters had to prepare on material they had
  not yet been taught. Shifting by one week means the lecture always comes first. It also means
  the Week 13 lecture topic (agentic AI) has no paper, and Weeks 1 and 2 have none because
  there is no preceding lecture to draw on.
- **One presenter per paper.** With 11 students and 11 slots, everybody presents exactly once,
  alone. The 2025 pairing scheme existed to fit ~20 students into 11 slots and is retired.
- **The second-paper extra credit is retired.** It existed to cover 22 slots. There is nothing
  left for it to solve.

The LLM-driven critique stays. It remains the one sanctioned use of generative AI in the
course, and it works better with one paper than two.

## Papers

No reviews or surveys. Each paper is either a seminal statement of the method or a strong
example of applying it to a health problem. Six carry direct clinical or biomedical content;
five are foundational computer science.

| Wk | Date | Covers (previous week) | Paper | Why this one |
| --- | --- | --- | --- | --- |
| 3 | Sep 10 | Knowledge representation & logic | McCarthy (1959), *Programs with Common Sense* | The founding argument for representing knowledge as logic a program can reason over. Seven pages; the Advice Taker is the ancestor of everything in Weeks 2–7 |
| 4 | Sep 17 | Semantic networks, frames, ontologies | Ashburner et al. (2000), *Gene ontology: tool for the unification of biology*, Nat Genet 25(1):25–29 | The most consequential biomedical ontology ever built, described by the people building it |
| 5 | Sep 24 | Heuristic, local & population-based search | Wolpert & Macready (1997), *No Free Lunch Theorems for Optimization*, IEEE Trans Evol Comput 1(1):67–82 | The result that says your favourite search algorithm has no general claim to being better. Forces the question of what a heuristic is actually buying you |
| 6 | Oct 8 | Biologically-inspired search | Kennedy & Eberhart (1995), *Particle Swarm Optimization*, ICNN'95:1942–1948 | Origin of PSO, half of the Week 5 notebook. Strikingly informal for a foundational paper — good discussion fodder |
| 7 | Oct 15 | Rules & knowledge-based systems | Shortliffe et al. (1973), *An artificial intelligence program to advise physicians regarding antimicrobial therapy*, Comput Biomed Res 6(6):544–560 | MYCIN. Still the clearest statement of what a clinical rule base was supposed to do |
| 8 | Oct 22 | Building an expert system (CLIPS) | Miller, Pople & Myers (1982), *Internist-1*, N Engl J Med 307(8):468–476 | A systematic evaluation of a large knowledge base that concludes it is not clinically reliable, and says exactly why. The honest counterweight to MYCIN, read while they build Homework 3 |
| 9 | Oct 29 | Bayesian networks; state machines | de Dombal et al. (1972), *Computer-aided diagnosis of acute abdominal pain*, Br Med J 2(5804):9–13 | A controlled prospective trial of Bayesian diagnosis in 304 patients with acute abdominal pain: 91.8% accuracy against 79.6% for the senior clinician on each case. Read after INTERNIST-1 it poses the obvious question — one narrow system worked, one broad one did not, and neither deployed |
| 10 | Nov 5 | Information theory & machine learning | Quinlan (1986), *Induction of decision trees*, Machine Learning 1:81–106 | Information gain doing actual work — the entropy-and-trees notebook, in its original form |
| 11 | Nov 12 | Deep learning & large language models | Vaswani et al. (2017), *Attention Is All You Need* | Read the actual paper, not a summary of it |
| 12 | Nov 19 | Explainable AI | Caruana et al. (2015), *Intelligible Models for HealthCare*, KDD:1721–1730 | The asthma/pneumonia paradox: an accurate model that would have killed people, caught only because it was intelligible |
| 13 | Dec 3 | Bias & fairness in AI | Obermeyer et al. (2019), *Dissecting racial bias in an algorithm used to manage the health of populations*, Science 366(6464):447–453 | Racial bias in a deployed algorithm affecting millions, traced to a single proxy-variable choice |

Every citation above was verified against PubMed or the publisher record. Where to obtain each
PDF is listed in the next section.

## Obtaining the PDFs

Only Shortliffe and Vaswani carry over from the 2025 course files; the other nine need sourcing.
Four are free to anyone. The rest need the Penn subscription — use the library proxy or an
on-campus connection.

| Wk | Paper | Where | Access |
| --- | --- | --- | --- |
| 3 | McCarthy (1959) | http://www-formal.stanford.edu/jmc/mcc59.html | Free |
| 4 | Ashburner et al. (2000) | https://pmc.ncbi.nlm.nih.gov/articles/PMC3037419/ | Free (PMC) |
| 5 | Wolpert & Macready (1997) | https://doi.org/10.1109/4235.585893 | IEEE — Penn |
| 6 | Kennedy & Eberhart (1995) | https://doi.org/10.1109/ICNN.1995.488968 | IEEE — Penn |
| 7 | Shortliffe et al. (1973) | https://doi.org/10.1016/0010-4809(73)90029-3 | Elsevier — Penn. **Already in the 2025 files** |
| 8 | Miller, Pople & Myers (1982) | https://doi.org/10.1056/NEJM198208193070803 | NEJM — Penn |
| 9 | de Dombal et al. (1972) | https://pmc.ncbi.nlm.nih.gov/articles/PMC1789017/ | Free (PMC) |
| 10 | Quinlan (1986) | https://doi.org/10.1007/BF00116251 | Springer — Penn |
| 11 | Vaswani et al. (2017) | https://arxiv.org/abs/1706.03762 | Free (arXiv). **Already in the 2025 files** |
| 12 | Caruana et al. (2015) | https://doi.org/10.1145/2783258.2788613 | ACM DL — Penn |
| 13 | Obermeyer et al. (2019) | https://doi.org/10.1126/science.aax2342 | Science — Penn |

Upload each to Box, set the share audience to **People in your company**, and paste the link
into the matching `paper-weekNN` key in `links.tsv`. The keys are unchanged from before — only
the paper behind each one has changed.

## Papers no longer used

**Newell & Simon (1956)** and **Turing (1950)** remain short readings for Weeks 1 and 2 rather
than presentations. Both decks already walk through them slide by slide, so a presentation
largely restates the lecture. As readings they set up the Week 1 ELIZA exercise directly.

**Dropped from the 2025 set.** Babalou et al. and Behrad et al. are surveys and fail the
no-review rule outright. Nagarajan & Babu, Leclerc et al., Shen et al., Michalowski et al.,
Pfohl et al. and Thirunavukarasu et al. are displaced by stronger papers on the same topics —
Pfohl by Obermeyer, Thirunavukarasu by the removal of the agentic-AI slot. Also unused, from
2025: Naz et al., Squires et al., Sung & Chi, Rodrigues de Araújo et al., Sadik et al.,
Shamshad et al., Balagopalan et al., Combi et al., Ladbury et al.

Heckerman, Horvitz & Nathwani (1992), *Pathfinder*, was the original Week 9 pick and remains a
reasonable substitute, as does Shwe et al. (1991), the QMR-DT reformulation of the Week 8 paper's
knowledge base; both sit behind the same Thieme paywall with no registered DOI.

Michalowski et al. (2020), *MitPlan* — first-order logic applied to conflicting clinical
practice guidelines — is the strongest of the dropped papers and is the obvious substitute for
Week 3 if a clinical application is wanted ahead of McCarthy.

## Format

**~25 minutes total per week:**

- 12–15 minutes presentation: background, methods, results, the authors' conclusions
- 3 minutes: the LLM-driven critique (below)
- 8–10 minutes: discussion questions posed by the presenter, who then leads the discussion

All students are expected to have read the paper and to participate. Because each paper follows
the lecture it draws on, presenters prepare on material already covered in class.

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

Assignments are distributed in the second week of the semester so that the Week 3 presenter has
two weeks of lead time.
