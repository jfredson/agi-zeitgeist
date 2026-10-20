# Leg C second source: the wider search, 2026-10-17

Written by the agent on 2026-10-17, in a cloud session on the roadmap step "Leg C second source:
find a measure of AI's share of frontier research work that is not a company's report on itself
(venue AI-contribution disclosures, researcher surveys), and add it to `data/world_measures.csv`".
It follows the reading note of the same day on the ICLR 2026 AI-disclosure audit
(`docs/leg-c-second-source-2026-10.md`), which found that audit to be context rather than a
second source, and it does not go over that ground again.

**Result: nothing found qualifies. No row was added to `data/world_measures.csv`.** The scored
series, the thresholds file (`docs/singularity-entry-thresholds.json`) and the definition are
untouched. Twenty-six candidates were judged; the three nearest misses, and two questions, are
set out for me at the end. This is a reading note, not an amendment.

## 1. What the step asks for, and the bar each candidate was held to

Leg C of the definition (`docs/singularity-entry-definition.md`, "AI is doing the improving") is
scored from f(t), "the share of inputs to frontier AI progress (code, experiments, research ideas)
supplied by AI systems rather than people, from the best measurement available". The definition
names three kinds of candidate source: lab self-reports of AI-written code share, surveys of
frontier researchers on time saved, and the AI-contribution disclosures that venues require on
papers. Today the leg is scored from one of the first kind, Anthropic's R&D Automation Index
(my ruling of 2026-10-17 keeps it scoring), with the company's staff poll and Google's
code-share statement beside it unscored.

A candidate qualifies as the second source the step wants when all four hold:

1. **It is a share of the work.** A share of code, experiments or research ideas done by AI, or
   something that can honestly be read as one. A count of papers that declare AI use, a
   productivity multiplier, or a capability test is not a share of the work.
2. **The work is frontier AI research.** The building of the most capable AI systems, not research
   in general and not software in general.
3. **It is measured by someone other than the company whose work it is.** A company's report on
   its own staff, models or customers is out, whatever its quality; an outside party's
   re-reading of a company's own figures is still the company's figures.
4. **It is dated, sourced to a primary document, and can be read again.** One-off numbers are
   recorded only as context; a second source has to be something the weekly reading can re-read.

Each candidate below is judged on these four. Where a candidate fails only one, the note says
which, because that is what a future reading should watch.

## 2. How the search was run, and one limit on it

Thirty-eight web searches were run on 2026-10-17 in the order the step sets: venue-level measures
first, then researcher surveys, then independent measurements of AI-generated content with a
method that separates substance from prose. Every search is logged in `data/search_log.csv` as
`leg-c-second-source-002` to `leg-c-second-source-039`, with `reading` as the speaker, as the
weekly reading's rule for searches that belong to a leg rather than to a speaker.

**The limit.** The session's network policy refused every direct fetch of a candidate document:
the proxy answered 403 for arxiv.org, neurips.cc, blog.neurips.cc, epoch.ai, nature.com and
uksg.org (logged as `leg-c-second-source-040`). Every document below was therefore read through
the search tool's extracts of its page, not the page itself. Figures are quoted as the extracts
gave them, each with the primary address, and where an extract disagreed with another the
disagreement is noted. None of these figures was turned into a row, so nothing in the record
rests on this partial reading; but any later session that does add a row from one of these
documents must read the page first. The ICLR audit note of the same day was written from the
paper itself, in a session that could fetch it.

## 3. Candidates and verdicts

The table gives the one-line verdict; the sections after it give what each measures, how, when,
on what sample, and why it does or does not meet the bar.

| # | candidate | kind | what it gives | fails on |
|---|---|---|---|---|
| 1 | NeurIPS 2026 Position Paper Track detector audit (2026-06-02) | venue | 28.2% of submissions substantially AI-written | share of work; prose only |
| 2 | NeurIPS 2025 authors' LLM-use survey | venue | no results published that the search could find | nothing to read |
| 3 | ICML 2026 LLM policy and enforcement | venue | numbers about reviewers, none about authors' research use | share of work |
| 4 | ACL and EMNLP checklist item on AI assistants (EMNLP 2025 analysis) | venue | the AI-assistance item not broken out in the analysis found | nothing to read |
| 5 | Mohapatra and Pruthi, ICLR 2026 and EMNLP 2025 disclosure audit | venue | judged 2026-10-17 in the earlier note | unchanged |
| 6 | METR survey of 349 technical workers (2026-05-11) | survey | median value of work 1.4x to 2x with AI; speed 3x | share of work; frontier sample; one wave |
| 7 | METR Frontier Risk Report, February to March 2026 (2026-05-19) | survey of companies | company statements with no figure | no number |
| 8 | METR review of Anthropic's February 2026 risk report (2026-05-08) | outside review | judges a self-report; no figure of its own | no number |
| 9 | Epoch AI, AI acknowledgments in mathematics preprints (2026-09-18) | independent measurement | 25% of August 2026 math preprints acknowledge AI; 6% credit it with a substantial research contribution | frontier AI research; share of work |
| 10 | Epoch AI, OpenAI's public Codex codebase (late July 2026) | independent measurement | share of contributor-days with very high estimated effort, 2% to 8% | share of work; not research |
| 11 | Epoch AI, InnovationEval (2026-10-07) | capability test | best agent reached 15% of a human method's gain | share of work |
| 12 | Epoch AI, OpenAI researchers' coding-agent usage (2026-10-05) | company data re-read | usage doubling about monthly | company's own figures |
| 13 | OpenAI, "Research acceleration: the view inside OpenAI" (2026-09-06) | self-report | 3.1 agent-workdays per human workday | company's own report |
| 14 | GovAI, "Measuring AI R&D Automation" (March 2026) | framework | 14 proposed metrics, no data | not a measure |
| 15 | Springer Nature and Fudan, "AI for Science 2026" (fieldwork March 2026) | survey | frequent AI use per task, 10,480 researchers | frontier AI research; share of work |
| 16 | Wiley, ExplanAItions 2025 to 2026 | survey | 62% use AI for research or publication tasks | frontier AI research; share of work |
| 17 | Frontiers researcher survey (2025-12) | survey | about a quarter use AI for analysis, design or methodology (secondary) | frontier AI research; share of work |
| 18 | Google, "AI in Science: Early Insights" (September 2026) | company-run survey | 637 researchers, US and UK | company-run; not frontier AI research |
| 19 | Nature's reports on the Wiley 2024 survey and its own 2023 survey | survey | general adoption | frontier AI research; share of work |
| 20 | Stanford AI Index 2026, science chapter | report | AI's share of publications by field | not a share of work |
| 21 | International AI Safety Report 2026 (2026-02-03) | report | "evidence is mixed"; benchmark results | no share figure |
| 22 | AI Impacts expert survey | survey | no 2025 or 2026 wave found | nothing to read |
| 23 | Survey of 868 scientists who program (arXiv 2512.19644) | survey | adoption and perceived productivity | frontier AI research; share of work |
| 24 | Detector studies of AI-written prose in papers and reviews | independent measurement | 14% to 21% of papers; 21% of reviews | prose only |
| 25 | Daniotti, Wachs, Feng and Neffke, AI-written code on GitHub (Science) | independent measurement | 29% of Python functions by US developers | not research |
| 26 | Agents4Science 2025 | demonstration | 48 papers with an AI first author accepted of 315 submitted | not a share of the field's work |

### 3.1 Venue-level measures

**1. NeurIPS 2026 Position Paper Track, "AI-Generated Papers in the NeurIPS 2026 Position Paper
Track"** (NeurIPS blog, 2026-06-02,
https://blog.neurips.cc/2026/06/02/ai-generated-papers-in-the-neurips-2026-position-paper-track/).
The track's chairs ran the Pangram detector (version 3.3.2) over the 969 submissions: a window of
text is flagged when the detector's probability exceeds 0.75, and a paper's score is the share of
its windows flagged. They report that 28.2% (273 of 969) "substantially used AI for writing", and
compare earlier tracks: the 2025 position track at 28.5% of 536 papers and the 2025 datasets and
benchmarks track at 5.6% of 996. Secondary reports say 178 papers (18.4%) were desk-rejected on
the scores and 123 (12.7%) given conditional notice, and that the rate depends strongly on the
window size (42.7% at the default, 12.7% at 100-word windows); those figures were not confirmed
against the post. *Verdict: no.* It measures prose, by a detector whose false-positive rate for
this population is disputed, and it says nothing about ideas, experiments or code. Context for
how much of the field's writing is machine-written, nothing more.

**2. NeurIPS 2025 authors' LLM-use survey.** The NeurIPS 2025 LLM policy
(https://neurips.cc/Conferences/2025/LLM) does not require declaring LLM use that only supports
writing, editing or formatting, and instead asks authors to report such use "in a statistical
analysis survey". No published results of that survey were found, on the NeurIPS blog or
elsewhere. The one NeurIPS 2025 survey found (datasets and benchmarks track, 851 authors and 155
reviewers) asked about the review process, not about LLM use in the research. *Verdict: nothing
to read yet.* If the results are published they will be the field's own count of declared use by
task, worth reading on the same terms as the ICLR audit.

**3. ICML 2026.** The policy (https://icml.cc/Conferences/2026/Intro-LLM-Policy) allows LLMs "to
assist in writing or research" with responsibility on the authors, and publishes no author
disclosure statistic. The numbers the conference did publish are about reviewers: hidden
watermarks caught 506 reviewers using AI against their declaration, and 497 papers tied to 398 of
them were desk-rejected, out of 23,918 submissions. The randomized experiment and survey of LLM
use in ICML 2026 peer review (arXiv 2609.19420) is likewise about reviewing. A third-party blog
puts authors' self-reported AI use at 9% against 36% detected, with no stated source. *Verdict:
no.* Nothing here is a share of research work.

**4. ACL and EMNLP.** The Responsible NLP Checklist item E1 asks authors to disclose "the use of
AI assistants in research, coding, or writing". The large-scale analysis of EMNLP 2025 checklists
(arXiv 2608.09280; 41,607 responses to 23 questions) was found, but the extracts do not break out
item E1. The EMNLP 2025 half of the Mohapatra and Pruthi audit (candidate 5) already gives the
nearest figure: 40% of accepted papers carry a disclosure statement, and 23.3% of those declare
help with code. *Verdict: nothing new to read.*

**5. Mohapatra and Pruthi, "Expectations and Practices around AI Disclosure in CS Research"**
(arXiv 2608.23271). Read from the paper on 2026-10-17 and judged context, not a second source, in
`docs/leg-c-second-source-2026-10.md`. Unchanged.

### 3.2 Researcher surveys

**6. METR, "Measuring the Self-Reported Impact of Early-2026 AI on Technical Worker
Productivity"** (2026-05-11, https://metr.org/blog/2026-05-11-ai-usage-survey/). METR, a
non-profit that evaluates AI systems and is not an AI company, surveyed 349 technical workers
between February and April 2026: 87 software engineers, 71 researchers, 129 academics and PhD
students, and 48 founders and managers. Respondents put the median change in the value of their
work due to AI at 1.4x to 2x (METR's own announcement says 1.6x to 2.1x "on average"; the two are
different summaries of the same data), and the median change in speed at 3x. Asked about the
past and future, they put the value multiplier at 1.3x in March 2025, 2x in March 2026 and 2.5x
forecast for March 2027. METR flags that self-reports have overstated AI's effect before, that
its own staff give the lowest answers of any subgroup, and that its randomized trial of
open-source developers found gains of about 4% to 20%. It asks "those interested in tracking the
potential automation of AI R&D, such as frontier AI companies" to run surveys building on this
one. No question about the share of the respondent's work done by AI was found; how respondents
were recruited was not found. *Verdict: no, on three of the four tests.* A multiplier is not a
share and cannot feed the gauge's formula; the sample is technical workers at large, with no
frontier-laboratory subgroup reported; and it is one wave with no stated repeat. It is, all the
same, the nearest thing found to the definition's "surveys of frontier researchers on time saved"
run by someone other than the company, and the first of the three near misses for me.

**7. METR, Frontier Risk Report, February to March 2026** (2026-05-19,
https://metr.org/blog/2026-05-19-frontier-risk-report/, written with Anthropic, Google, Meta and
OpenAI). On AI's part in the companies' own research it reports statements, not figures:
Anthropic that "a large percentage of code written at Anthropic is written by AI", Google that AI
is used "in almost all work that involves writing code or configuration, technical design,
research ideation, to different degrees depending on the task", OpenAI that AI assistance is
"embedded in day-to-day R&D workflows". METR's own reading is that agents "probably made
researchers more productive" with the size "very uncertain", and that no company relies on agents
for setting research agendas, hiring or budgets. *Verdict: no.* An outside party's report with no
number in it; useful as the plainest statement that the companies themselves have not published
a share.

**8. METR, review of the "Risks from automated R&D" section of Anthropic's February 2026 risk
report** (2026-05-08,
https://metr.org/blog/2026-05-08-rd-section-anthropic-risk-report-feb-2026-review/). An outside
review of a company self-report (an internal survey METR says gives "little evidence", on sample
size, question granularity and framing). *Verdict: no.* It produces no figure of its own, but it is
the kind of outside audit of a self-report that the earlier note listed as one of three shapes a
second source could take, and it says the self-report it audited is weak.

**15. Springer Nature, Fudan University and the Shanghai Academy of AI for Science, "AI for
Science 2026"** (https://www.nature.com/immersive/partnercontent/fudan/aiforscience/index.html)
and the white paper "The State of AI Use Among Researchers" drawn from the same survey. Fieldwork
2026-03-02 to 2026-03-30; 10,480 qualified responses from 117 countries and 12 disciplines,
weighted by country. It asks how often AI is used for each research activity. Using AI "every
time" or "most times": information gathering 43.8%, improving or editing papers 44.6%, planning
research 40.9%, reviewing papers 23.5%, deciding where to submit 25.7%. Frequent use falls with
seniority. No item on the share of work done by AI, and no breakdown for computer science or AI
researchers, was found in the extracts. *Verdict: no.* All fields, usage frequency rather than
share, and the publisher's own survey of its market. The largest researcher survey of 2026, and
context for how far AI use in research generally has gone.

**16. Wiley, ExplanAItions 2025 to 2026**
(https://www.wiley.com/en-us/about-us/ai-resources/ai-study/). 2,430 researchers worldwide; 84%
use AI for some aspect of their work (57% a year earlier), 62% for research or publication tasks
(45% a year earlier); coding assistants are among the most frequently used tools but the
coding-tool subsample is 150 people. *Verdict: no*, for the same reasons as 15.

**17. Frontiers, survey of 1,645 researchers** (field note of 2025-12-15,
https://www.frontiersin.org/field-notes/2025/12/15/ai_in_peer_review_dec-25). A secondary
write-up says about 70% use AI for writing papers and "nearly a quarter" for analysis, design or
methodology; the quarter was not confirmed against the publisher's own report. *Verdict: no.*

**18. Google, "AI in Science: Early Insights"** (Codreanu and Imas, September 2026,
https://ai.google/static/documents/AI-in-Science.pdf). A survey of 637 active researchers in the
United States and United Kingdom in July and August 2026, run by a company. *Verdict: no.* Not
frontier AI research, and company-run; noted so that it is not re-found.

**19. Nature's reports on researcher surveys.** "How are researchers using AI? Survey reveals
pros and cons for science" (2025-02-04, https://www.nature.com/articles/d41586-025-00343-5)
reports the Wiley survey of close to 5,000 researchers in more than 70 countries; Nature's own
2023 survey of 1,600 researchers (https://www.nature.com/articles/d41586-023-02980-0) found about
30% using AI in their research. *Verdict: no.* General adoption, superseded by 15 and 16.

**22. AI Impacts, Expert Survey on Progress in AI.** The last wave is 2023 (2,778 respondents at
six AI venues); no 2025 or 2026 wave was found, and the 2023 instrument has no item on the share
of the respondent's work done by AI. *Verdict: nothing to read.* The one standing survey of
AI researchers themselves, and the natural home for such an item if it were ever added.

**23. "A survey of generative AI adoption and perceived productivity among scientists who
program"** (arXiv 2512.19644; 868 scientists recruited through mailing lists). Adoption and
perceived productivity; the strongest predictor of perceived productivity is how many lines of
generated code the person accepts at once. No share figure found. *Verdict: no.*

### 3.3 Independent measurements of AI's contribution to research

**9. Epoch AI, "In August, 25% of math preprints acknowledged AI use, up from 4% in April"**
(data insight, 2026-09-18, https://epoch.ai/data-insights/math-preprints-disclosed-ai-use; data
and code at https://github.com/epoch-research/ai-math-arxiv, updated 2026-10-06). Epoch, an
independent research group, read every mathematics preprint on arXiv from January 2025 to August
2026: papers containing an AI keyword were classified by a language model (GPT-5.6 Sol, with
Claude Fable 5 as a validator) into six kinds of acknowledged use (substantial research, research
assistance, writing, code and computation, literature review, formalization), with a verbatim
quote kept for each tag; human reviewers agreed with the classification on 93% of 200
acknowledgments. The share of preprints acknowledging any AI use rose from 4% in April 2026 to
25% in August 2026, and 6% credited AI with a "substantial research contribution", defined as
"approximately at the level of a coauthor". The rise holds, within 1.5 percentage points each
month, when restricted to papers with at least one author who published regularly before 2023.
Epoch says the trend "reflects changes in disclosure behavior in addition to changes in AI use".
*Verdict: no, on two tests.* The field is mathematics, not frontier AI research, and the measure
is the share of papers that acknowledge a contribution, not the share of the work AI did. But it
is the only outside measurement found that separates substantive contribution from prose, has a
published method with a human check, open data, a monthly series and an explorer that is being
updated. It is the second near miss, and the thing a future reading should most want extended:
the same method run on the machine-learning and AI categories of arXiv would be the venue-level
measure the step describes, still subject to the "share of work" point.

**10. Epoch AI, "Contributions to OpenAI's Codex codebase show signs of AI uplift"** (data
insight, late July 2026 by the Epoch Brief of 2026-07-31; exact date not confirmed;
https://epoch.ai/data-insights/codex-engineer-effort). Epoch took the 7,524 merged pull requests of
41 core contributors to OpenAI's public Codex repository and had an ensemble of three frontier
models estimate how long each change would take an experienced engineer without AI. The share of
contributor-days with at least 24 hours of estimated unassisted effort rose from about 2% in the
second quarter of 2025 to about 8% in the second quarter of 2026 (7.2% in the 24-to-48-hour band
and 1.0% above). Epoch calls the figure noncausal and an upper bound on time saved. *Verdict:
no.* It is an uplift proxy on a product codebase, not a share of research work, and Codex is a
tool rather than frontier model research. It is the third near miss because of what it shows is
possible: an outside party measuring a company's AI-assisted output from public artefacts, with
no company figure involved.

**11. Epoch AI, "Can AI automate AI R&D yet? Early evidence from InnovationEval: No"** (2026-10-07,
David Owen, https://epoch.ai/publications/innovationeval). Two frontier agents, 3,000 GPU-hours
each, were asked to invent a post-training method matching a recent human one without seeing the
paper; the best reached 15% of the human method's gain after out-of-scope changes were removed
(about 35% under generous grading), and both overstated their results. *Verdict: no.* A
capability test on one research problem, not a measure of the share of work. Context for leg C
in the same way METR's benchmarks are context for leg A.

**12. Epoch AI, data insight on OpenAI researchers' coding-agent usage doubling about monthly**
(2026-10-05). Built on OpenAI's own published figures (candidate 13). *Verdict: no.* An outside
party's reading of a company's numbers is still the company's numbers.

**14. Alan Chan, Ranay Padarath, Joe Kwon, Hilary Greaves and Markus Anderljung (GovAI and the
University of Oxford), "Measuring AI R&D Automation"** (arXiv 2603.03992, March 2026, with later
versions to v3). A framework of 14 metrics for the extent of AI R&D automation, among them the
capital share of AI R&D spending, researcher time allocation and staff surveys, with the finding
that existing evidence is thin and that no single metric suffices; it recommends that companies
and third parties such as non-profits start tracking them. *Verdict: not a measure.* It is the
clearest statement of what the step is waiting for, from outside the companies, and it says that
as of March 2026 nobody was publishing it.

**20. Stanford AI Index 2026, chapter 5, Science** (with Schmidt Sciences,
https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_5_science.pdf). Reports AI's
share of scientific publications by field (5.8% to 8.8% in 2025, up from under 1% in 2010) and
benchmark results on research tasks. No survey of researchers on AI's share of their work was
found in the chapter. *Verdict: no.*

**21. International AI Safety Report 2026** (2026-02-03, arXiv 2602.21012). States that "current
empirical evidence on AI-assisted research automation is mixed" and gives benchmark results and
expert forecasts, no share of work. *Verdict: no.*

**24. Detector studies of AI-written prose.** arXiv 2601.17036 estimates LLM-generated content in
21.4% of computer-science review papers and 14.0% of non-review papers on arXiv; a Pangram Labs
analysis puts about 21% of ICLR 2026 reviews as fully AI-generated (76,139 reviews, per a
third-party report); an earlier study put NeurIPS 2024 at 0.7% of papers and 20.9% of reviews
LLM-aided. *Verdict: no.* Prose and reviews, not research work.

**25. Simone Daniotti, Johannes Wachs, Xiangnan Feng and Frank Neffke, "Who is using AI to code?"**
(Science). A classifier run over more than 30 million GitHub commits finds that 29% of Python
functions committed by developers in the United States look AI-written, with data to the end of
2024. *Verdict: no.* All public software, not research, and not frontier AI; the independent
counterpart of the Google code-share row's kind of measure, and context for it.

**26. Agents4Science 2025** (https://www.nature.com/articles/s41587-025-02963-8). A conference of
papers with an AI as first author, held online on 2025-10-22 and reported by its five organizers
in Nature Biotechnology (published 2025-12-17). It received 315 submissions; 62 were incomplete and
turned away unread, and each of the other 253 was scored by three AI reviewers. The 79 that scored
best were also read by a human expert, and the organizers accepted 48, weighing both kinds of
review. Every accepted paper named an AI as first author, and humans could be coauthors. *Verdict:
no.* A demonstration of what AI authors can get through review, not a share of any field's work.
(Counts checked against the full text on 2026-10-20; the earlier "about 315" is exactly 315.)

**13. OpenAI, "Research acceleration: the view inside OpenAI"** (2026-09-06,
https://openai.com/index/research-acceleration-view-inside-openai/). Found on the way. By
mid-August 2026 OpenAI's research organization was running 3.1 eight-hour agent-workdays for
every human workday, and experiments per active experimenter reached a high in August 2026, which
OpenAI links to Codex adoption while noting that compute had also grown. *Verdict: excluded by
the rule.* A company's report on itself, and a runtime ratio rather than a share. It is recorded
here because it is the first OpenAI self-report of the same kind as the Google and Anthropic
rows, and whether to record it beside the gauge is my call (section 5).

## 4. Why the search came up empty, in one paragraph

The three shapes of second source the earlier note listed are all still missing. No one outside a
frontier laboratory has surveyed its researchers on the share of their work AI does: METR's
survey is of technical workers at large and asks about value, not share. No venue publishes the
share of research work declared as AI-done: the venues publish detector rates on prose and
counts of declarations, and the one standing audit (Mohapatra and Pruthi) counts declarations.
No outside audit of a company's R&D automation figure exists: METR reviewed Anthropic's survey
and found it weak, and GovAI's framework says the metrics are not yet collected by anyone. The
nearest outside measurements are of the wrong field (mathematics), the wrong unit (a multiplier,
a count of acknowledgments, an effort estimate), or the wrong work (a product codebase, public
software in general).

## 5. For me

1. **Whether any near miss should sit beside the gauge as context, unscored.** The three are the
   METR survey (a 1.4x to 2x median value multiplier, February to April 2026), the Epoch
   mathematics series (6% of August 2026 math preprints crediting AI with a substantial research
   contribution) and the Epoch Codex measurement (8% of contributor-days at very high estimated
   effort in the second quarter of 2026). None is a measure of f, so none would be scored, and
   the earlier note's rule was followed: context rows go in only if I want them. Two of the
   three would need a unit the validator does not yet accept for `data/world_measures.csv`
   (a multiplier; a share of contributor-days), which is a small validator change, not a
   method change. The agent's recommendation is to add none of them: a row in that file is read
   on the page as a measure of the leg, and each of these would need a sentence of explanation
   to stop it being read that way.
2. **The OpenAI self-report** (3.1 agent-workdays per human workday, 2026-09-06). It is excluded
   from this step by the rule but is the same kind of row as Google's code share. Under the
   weekly reading's rules it would be flagged, not appended, because it is not a repeat of a
   series in the file. I can have it recorded as a self-report row with its own speaker, or
   left out.
3. **Whether the roadmap step is waiting for something that may not come.** As of 2026-10-17 the
   measure the step describes is not published by anyone, and the two outside groups closest to
   it (METR, GovAI) say so. The step can stay open as a standing watch (section 6), or I can
   narrow it to the one shape most likely to appear first: Epoch's acknowledgment method run on
   AI preprints, or a second wave of METR's survey with a frontier-laboratory subgroup.
4. **Nothing here proposes a scored series.** A qualifying measure would have been proposed as an
   amendment for me to rule on; none qualified, so there is no amendment to propose.

## 6. What a future reading should watch

- **NeurIPS.** Results of the 2025 authors' LLM-use survey, if published; the 2026 main-track
  policy and any disclosure statistics with it; a repeat of the position-track detector audit.
- **ICLR 2027.** ICLR's disclosure policy and any statistics the programme chairs publish; a
  repeat of Mohapatra and Pruthi's audit, which would make the ICLR count a series.
- **Epoch AI.** The mathematics series' monthly updates in the explorer, and above all any
  extension of the same method to the machine-learning and AI categories of arXiv. Also any
  repeat of the Codex measurement on other public repositories of frontier companies.
- **METR.** A second wave of the technical-worker survey, or the company surveys it asked for if a
  third party runs them; the next Frontier Risk Report's section on R&D automation.
- **GovAI.** Any third party adopting the "Measuring AI R&D Automation" metrics.
- **AI Impacts.** A 2026 or 2027 wave of the expert survey, and whether it adds an item on the
  share of the respondent's own work done by AI.
- **Search terms** that found the most in this reading: "AI R&D automation" with "measure" or
  "survey"; "acknowledged AI" with "preprints"; "LLM policy" with the conference name and year;
  "disclosure statements" with "ICLR" or "NeurIPS". The weekly reading's leg C item may want
  them; that document is the reading's own and is not changed here.
