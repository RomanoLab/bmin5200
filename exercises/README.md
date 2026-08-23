# In-class coding exercises

Thirteen notebooks, one per class meeting. Each is designed for **25–30 minutes** of class
time immediately after the lecture, and each pairs with that week's slide deck.

These replaced the second journal club paper. The trade was deliberate: students were reading
two papers a week and writing no code, in a course whose syllabus promises that "all
programming in this course will be done in Python."

## Running them

Click the Colab badge at the top of any notebook. Nothing to install, nothing to configure —
each notebook's first code cell installs whatever it needs. A laptop and a browser is the
whole requirement.

To run locally instead:

```bash
pip install -r requirements.txt
jupyter lab
```

## The sequence

| Week | Date | Notebook | What students build |
| --- | --- | --- | --- |
| 1 | Aug 27 | `week01.ipynb` | ELIZA in ~20 lines of regex, then break it |
| 2 | Sep 3 | `week02.ipynb` | A propositional model checker; watch 2ⁿ bite |
| 3 | Sep 10 | `week03.ipynb` | Inheritance and inferential distance over an ontology |
| 4 | Sep 17 | `week04.ipynb` | BFS/DFS/UCS/greedy/A* as one algorithm with five priorities |
| 5 | Sep 24 | `week05.ipynb` | A genetic algorithm and a particle swarm |
| 6 | Oct 8 | `week06.ipynb` | A forward and backward chaining engine, from scratch |
| 7 | Oct 15 | `week07.ipynb` | A transfusion expert system in CLIPS / clipspy |
| 8 | Oct 22 | `week08.ipynb` | A clinical Bayes net, and a titration state machine |
| 9 | Oct 29 | `week09.ipynb` | Entropy and mutual information; a readable decision tree |
| 10 | Nov 5 | `week10.ipynb` | Tokenization, attention, contextual embeddings |
| 11 | Nov 12 | `week11.ipynb` | SHAP vs. LIME on the Week 9 model |
| 12 | Nov 19 | `week12.ipynb` | A fairness audit of the same model |
| 13 | Dec 3 | `week13.ipynb` | A clinical agent, and the three guardrails it needs |

## How they connect

The notebooks are not thirteen independent demos. Three threads run through them:

**The rule base.** Week 6 has students hand-build a forward/backward chaining engine. Week 7
shows them the same thing industrialized as CLIPS. Week 9 induces a rule base from data
instead of eliciting it from an expert, and says so. Week 13's "agent planner" is revealed to
be the Week 6 inference engine with a new name.

**One cohort, three weeks.** Weeks 9, 11, and 12 share a synthetic 30-day readmission dataset,
regenerated inline from the same seed. Week 9 trains a model on it. Week 11 explains that
model. Week 12 audits it — and finds a disparity that was planted in the generator back in
Week 9. Students discover it themselves rather than being told it exists.

**The opening question.** Week 1 ends with students writing down what they think it would take
for a system to actually understand a patient complaint. Week 13 hands that answer back to them
with a semester of symbolic AI behind it.

## Notes for teaching

Every exercise cell ships with a **runnable placeholder**, not a blank. Nothing raises, so a
student who freezes still has output on screen — but the placeholders are deliberately,
visibly wrong (mutual information that comes back 0.000, five search algorithms that return
identical answers, guardrails that block nothing). That is the diagnostic: if the numbers look
like the ones the notebook warns about, the TODO is still a TODO.

This means **a notebook run start-to-finish without the TODOs filled in will look broken on a
projector.** That is intended. Run them live.

Each notebook ends with a `## Solutions` section holding the completed code as Markdown blocks
rather than executable cells, so scrolling ahead does not accidentally run them.

Every notebook contains at least one **predict-before-you-run** moment. These are the highest
value 90 seconds in the exercise — do not skip them for time.
