# BMIN 5200: Foundations of Artificial Intelligence in Health

**Fall 2026 semester**

Welcome to BMIN 5200. This syllabus outlines the logistical details of the course. All course
materials live on the course website; Canvas is used only for submitting assignments and
viewing grades.

Don't hesitate to ask if you have any questions about the information here or elsewhere — Joe
can be reached at joseph.romano@pennmedicine.upenn.edu, or you can ask before or after class.

---

## Course description

As a subfield of computer science, artificial intelligence (AI) is often used interchangeably
with the term 'machine learning', which is itself only a subfield of AI dealing with the
broader concept of *inductive reasoning*. However, a wealth of key prerequisite topics that
focus on *deductive reasoning* cover a large portion of biomedical informatics applications
being actively used today. These founding principles of AI and their intersection with
biomedical informatics are the focus of this first course on AI, and lay the groundwork for
future coursework on machine learning, artificial neural networks, and generative AI.

This course is divided into modules that cover (1) introductory/background materials,
(2) knowledge representation, (3) logic, (4) essentials of rule-based systems, (5) search,
(6) information structure and inference, and (7) special topics. These topics offer a global
foundation of branches of AI application and research in biomedical domains, including concepts
that will later support a deeper understanding of inductive reasoning and machine learning.

In a practical sense, this course focuses on how biomedical data can be organized, represented,
interpreted, searched, and applied in order to derive knowledge, make decisions, and ultimately
make predictions while mitigating bias.

*To reiterate: this course does not focus heavily on machine learning or generative AI, but it
does present critically important deductive and symbolic AI concepts that are necessary for a
deeper understanding of ML and GenAI. BMIN 5200 is the first in a 3-part course series on
artificial intelligence, followed by BMIN 5210 (AI 2: Machine Learning) and BMIN 5220 (AI 3:
Natural Language Processing).*

## Course objectives

Upon completion of this course, students will be able to:

- Describe the unique challenges of representing and applying human knowledge in an *in silico*
  environment
- Explain the conceptual differences between deduction and induction, and the role of both in AI
- Discuss the past and current challenges to developing and implementing AI in biomedical
  domains
- Demonstrate knowledge of how common AI approaches can be developed to address real-world
  biomedical problems
- **Implement** core AI methods in Python — inference engines, search algorithms, expert
  systems, and probabilistic models — rather than only describing them

## Prerequisites

It is expected that all students will be somewhat familiar with basic biomedical concepts and
terminology, as well as statistics and computer programming. It is suggested (but not strictly
required) that students have taken Introduction to Biomedical Informatics (BMIN 5010), Data
Science for Biomedical Informatics (BMIN 5030), and a programming course (any language is
fine). All programming in this course will be done in Python, and a brief introduction to the
language will be provided.

No previous exposure to artificial intelligence is assumed.

## Class meetings

**Thursdays, 3:30–6:30pm**, in person.
**3600 Civic Center Boulevard, Room 6E 031.**

First meeting **August 27, 2026**. Last meeting **December 3, 2026**.

Class will not meet on:

- **October 1, 2026** — Fall Break (October 1–4)
- **November 26, 2026** — Thanksgiving (November 26–29)

That leaves 13 meetings, one per lecture topic. No virtual option will be offered unless
otherwise indicated by Joe.

### Format of a typical meeting

| | |
| --- | --- |
| 0–30 min | Homework review |
| ~60 min | Weekly lecture |
| ~25 min | **In-class coding exercise** |
| 10 min | Break |
| ~25 min | Journal club |

The in-class coding exercise is new this year, and it replaces the second journal club paper.
Each week's exercise is a Jupyter notebook that runs in Google Colab — you click a link, and it
works. You will build a propositional inference engine, a forward and backward chaining rule
system, a search algorithm suite, an expert system in CLIPS, a Bayesian network, and a clinical
agent, among others. These are not graded, but they are where the course's ideas stop being
abstract, and several of them are direct on-ramps to the homework.

**You must bring a laptop to every class.** You do not need to install anything: the exercises
run in a browser through Colab. If you would rather work locally, a `requirements.txt` is
provided in the course repository.

## Course units

This is a 1.0cu course.

## Where course materials live

**Course website:** the schedule, links to every lecture deck, the in-class notebooks, the
journal club papers, and the assignment specifications. This is the first place to look.

**Penn Box:** lecture slides, journal club PDFs, and assignment files. Box links from the course
website require Penn SSO — sign in with your PennKey.

**Canvas:** assignment submission and grades only. Nothing else in the course depends on it.

**GitHub:** the in-class exercise notebooks, in a public repository, each with an "Open in
Colab" link.

## Office hours

TBD — a poll will go out in the first week, and the time that works for the greatest number of
students will be selected. One-on-one meetings with the course director or TA may be scheduled
on an as-needed basis.

## Course director

**Joseph D. Romano, PhD, MPhil, MA** (please feel free to call me Joe)
Assistant Professor of Informatics and Pharmacology
3600 Civic Center Blvd, 5E 300A, Philadelphia, PA 19104
(+1) 215-573-5571
joseph.romano@pennmedicine.upenn.edu

## Teaching assistant

TBD — will be announced before the first class meeting.

## Student expectations

Students are expected to come to class prepared for the day's content, and to ask questions and
discuss that content following the lectures. Reviewing lecture slides before coming to class is
strongly recommended.

Students are expected to read all assigned materials, participate during class sessions, and
complete the required assignments. This course requires the use of a laptop computer.

## Student evaluation

### Assignments — 40% of final grade

Four graded submissions, weighted equally. Assignments are submitted via Canvas. Since we are on
a fairly tight schedule, no late submissions will be accepted without prior approval.

| Assignment | Topic | Assigned | Due |
| --- | --- | --- | --- |
| Homework 1 | Logic | Sep 3 | Sep 17, 11:59pm |
| Homework 2 | Semantic networks & search | Sep 24 | Oct 8, 11:59pm |
| Homework 3 | Expert system in CLIPS | Oct 15 | Nov 5, 11:59pm |
| Homework 4 | Bayesian networks | Oct 22 | Nov 19, 11:59pm |

### Final project — 40% of final grade

Either an AI-based research project (for doctoral students) or a knowledge-based system
implementation (for master's, professional, and other students), addressing a biomedical
problem of your choice. Full details below, and discussed in class. The 40% breaks down as:

| Component | Weight | Due |
| --- | --- | --- |
| Proposal | 5% | Oct 22, 11:59pm |
| Implementation and code | 10% | Dec 11, 11:59pm |
| Written report | 17% | Dec 11, 11:59pm |
| Recorded presentation | 8% | Dec 11, 11:59pm |

### Class participation — 20% of final grade

| Component | Weight |
| --- | --- |
| Journal club presentation | 10% |
| Journal club discussion | 4% |
| In-class exercises and preparation | 6% |

The journal club presentation is worth as much as one homework assignment, which is roughly
what it costs to prepare. Discussion credit is for the other ten weeks — everyone reads the
paper, not only the pair presenting it. In-class exercise credit is for engagement and
completion, not for correct answers.

Attendance is expected rather than credited. There are no points for showing up, so it is not
listed above. If you need to miss class for an appropriate reason, please contact Joe as soon as
possible to let him know. Each unexcused absence will be penalized by deducting 5% from your
final number grade for the course, separately from the categories above.

## Journal club

Each week from Week 3 onward, we dedicate roughly 25 minutes to discussing one journal paper on
that week's topic. **This is half of what the course ran in previous years** — one paper per
week instead of two — so that we can spend the reclaimed time writing code.

A **pair** of students is assigned to each paper. One presents background and methods, the
other results and critique, and both lead the discussion afterward. With eleven papers and
roughly twenty students, everyone presents exactly once.

Paper presentations should include an overview of the paper (background, methods, results, and
the authors' conclusions), followed by a set of discussion questions posed to the rest of the
class. Presenters then lead the class in discussion and critique.

All students are expected to have read the paper and to participate actively in the discussion.
All papers are available in PDF format through the course website. The subject matter of each
paper is briefly discussed in class two weeks before the presentation date, to allow students
time to prepare.

### LLM-driven critique

As part of each presentation, presenters must run the paper past an LLM chatbot of their
choice, ask it to critique the work, and report back on: what it flagged, which of those
criticisms are actually correct, and which are confidently wrong. The third question is the
important one.

## Final project

The final project ties together multiple topics covered in this course, with a specific focus
on one or more sources or types of biomedical data. There are two types of final project,
selected based on your degree program or registration status.

### Research project (doctoral students; others may opt in)

Students use the concepts taught over the semester to complete an original research project
addressing an area of interest or need in medicine. Examples include designing and evaluating a
new clinical decision support algorithm, developing an ontology or knowledge base to support a
specific domain along with use cases, or applying Bayesian networks to accomplish a novel task
on a biomedical dataset. All projects should be applied to either a real or synthetic dataset,
and should be cleared with Joe before work begins.

Note that **deductive inference must be used** in this project. A project that exclusively or
primarily focuses on machine learning is not acceptable.

### Implementation project (master's and professional students)

Students propose and implement their own software tool to address a target biomedical task —
for example, an expert system that makes deductions toward a clinical task, such as a decision
support system, an alert or reminder system, or one that proposes a diagnosis.

Students conduct a literature search targeting a specific biomedical task or problem, identify
relevant data, databases, experts, and resources for developing the tool, and complete an
initial implementation. The tool does not have to be production-ready, but should demonstrate
the intended functionality. This tool should be implemented in CLIPS (e.g., via clipspy).

### Proposal

A one-page proposal is due **October 22, 2026, 11:59pm**, and is worth 5% of the final grade. It
states the biomedical problem, where deductive inference enters, the data or resources you plan
to use, and which of the two project types you are doing. This is how your topic gets cleared
before you start building. It falls the week after CLIPS is covered in class, so implementation
students propose a tool having already worked with it.

### Final report

Both project types involve a report with the same sections. The report should be an 8–10 page
description of the project, including:

- **Background** — synthesize relevant literature and the need for AI-based approaches to the
  problem. Include descriptions of any existing or previous deductive AI solutions in the area.
- **Materials and Methods** — data, databases, and other resources used by and for the creation
  of the system.
- **Design** — the high-level design of the proposed tool and how it integrates multiple topics
  covered in this course.
- **Demonstration** — application of the tool to your task of interest and the results. If the
  tool is not completely implemented, or does not function as intended, discuss the current
  stage of implementation and your troubleshooting attempts.
- **Discussion and Conclusions** — challenges you overcame, advantages and disadvantages of the
  tool, and how it could be improved or applied more broadly.
- **References** — relevant citations. No specific format is required, but consistency and
  completeness both matter. Zotero or similar citation management software is recommended.

The report must be typeset in LaTeX using the
[AAAI template](https://www.overleaf.com/latex/templates/aaai-press-latex-template/jymjdgdpdmxp).

**Code submission.** Everyone additionally submits the code accompanying their project, either
(preferred) in a GitHub repository linked from the text of the paper, or as a documented,
well-structured directory alongside the report, compressed into a ZIP file.

### Oral presentation

A 10-minute presentation structured around the format of the written report. Slides will be
helpful. The presentation is recorded as a video and uploaded to the Box folder linked from the
course website.

Your slides should include a brief introduction to the biomedical problem, how you approached
solving it using a deductive reasoning approach, and images (or a live demonstration) showing
your program's input and output. Research projects should also briefly describe the evaluation
approach and key takeaways.

Please stick to the 10-minute limit. Since you can edit and re-record, there is no reason to run
over, and points may be deducted for videos that do.

**Both the report and the presentation video are due December 11, 2026.**

## Course materials

No textbooks are strictly necessary, but the following are recommended:

- Cawsey A. *The Essence of Artificial Intelligence.* Pearson, 2nd ed., 2010.
- Russell S and Norvig P. *Artificial Intelligence: A Modern Approach.* Pearson, 4th ed., 2020.

Both may be found affordably online.

## Academic honesty

All work submitted for credit is expected to be your own work. In the preparation of all papers
and other written work, you should always take great care to distinguish your own ideas and
knowledge from information derived from other sources. The term "sources" includes not only
published primary and secondary material, but also information and opinions gained directly
from other people. The responsibility for learning the proper forms of citation lies with you.
You must acknowledge any collaboration and its extent in all submitted work. You are expected
to follow Penn's standards of academic integrity as found in the
[Code of Academic Integrity](https://catalog.upenn.edu/pennbook/code-of-academic-integrity).

### Violations

All violations of academic honesty and integrity are taken very seriously and will result in
disciplinary action. Depending on the seriousness of the violation, action will be taken at the
discretion of the course director, and may include reduction of grades, additional assignments,
a failing grade for the course, and/or reporting the incident to the University for further
evaluation.

## Statement on the use of artificial intelligence in assignments

Although this is a course on AI, all work completed as part of the assignments, journal club,
and final project must be completed on your own volition, without the assistance of generative
AI tools (or similar), unless otherwise instructed by the course director. Any and all
violations of this policy will be treated similarly to other forms of plagiarism.

**Two exceptions:**

1. The **LLM-driven critique** portion of each journal club, in which you are expected to use
   the LLM chatbot of your choice to assist in critiquing the article.
2. The **in-class coding exercises**, which earn credit for engagement rather than for correct
   answers. Use whatever tools help you learn there — though you will get more out of them by
   typing the code yourself.

The homework assignments and the final project are covered by the policy without exception.

Please direct any and all questions to Joe — if you have any doubts, it is better to ask in
advance.

## Students with disabilities

The University of Pennsylvania provides reasonable accommodations to students with disabilities
who have self-identified and been approved by the office of Student Disabilities Services
(SDS). Please make an appointment to meet with me as soon as possible in order to discuss your
accommodations and your needs. If you have not yet contacted SDS and would like to request
accommodations or have questions, you can make an appointment by calling (215) 573-9235. The
SDS office is located in the Weingarten Learning Resources Center at Stouffer Commons, 3702
Spruce Street, Suite 300. All SDS services are free and confidential. Please visit the
[SDS website](https://www.vpul.upenn.edu/lrc/sds/) for more information.

---

## Schedule at a glance

| # | Date | Topic | Journal club | Due |
| --- | --- | --- | --- | --- |
| 1 | Aug 27 | Course intro; history of AI | — | |
| 2 | Sep 3 | Knowledge representation & logic | — | |
| 3 | Sep 10 | Semantic networks, frames, ontologies | Babalou et al. | |
| 4 | Sep 17 | Heuristic, local & population-based search | Wolpert & Macready | **HW 1** |
| 5 | Sep 24 | Biologically-inspired search | Nagarajan & Babu | |
| — | Oct 1 | *No class — Fall Break* | | |
| 6 | Oct 8 | Rules & knowledge-based systems | Shortliffe et al. | **HW 2** |
| 7 | Oct 15 | Building an expert system: CLIPS / clipspy | Michalowski et al. | |
| 8 | Oct 22 | Bayesian networks; state machines | Leclerc et al. | **Project proposal** |
| 9 | Oct 29 | Information theory & machine learning | Shen et al. | |
| 10 | Nov 5 | Deep learning & large language models | Vaswani et al. | **HW 3** |
| 11 | Nov 12 | Explainable AI | Behrad et al. | |
| 12 | Nov 19 | Bias & fairness in AI | Pfohl et al. | **HW 4** |
| — | Nov 26 | *No class — Thanksgiving* | | |
| 13 | Dec 3 | Agentic AI | Thirunavukarasu et al. | |
| — | Dec 11 | | | **Final report + video** |
