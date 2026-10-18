# Leg C second source: the ICLR 2026 AI-disclosure audit, read 2026-10-17

Written by the agent on 2026-10-17 after John's ruling of the same day that the audit flagged by
the first weekly reading (2026-10-16) should be read before deciding whether it is the "second
source for leg C" the roadmap asks for. This is a reading note, not an amendment: no row was
added to `data/world_measures.csv`, and `docs/singularity-entry-thresholds.json` and the
definition are untouched. Naming a second source is an amendment and is John's call.

## What the roadmap step asks for

Leg C of the singularity-entry definition (`docs/singularity-entry-definition.md`) is "AI is doing
the improving": the share of the inputs to frontier AI progress (code, experiments, research
ideas) supplied by AI systems rather than people. Today it is scored from one number, Anthropic's
R&D Automation Index, which is a company's report on itself. The roadmap step "Leg C second
source" wants a measure of the same thing from outside the company.

## What was read

Arati Mohapatra and Danish Pruthi (Indian Institute of Science), "Expectations and Practices
around AI Disclosure in CS Research", arXiv 2608.23271, version 2 of 2026-08-25
(https://arxiv.org/pdf/2608.23271). The paper has three parts: a survey of disclosure policies at
65 computer-science conferences, a survey of 109 researchers on when disclosure is needed, and an
audit of the AI-disclosure statements in papers at two conferences. Only the audit (sections 6.1
and 6.2) bears on leg C, and that is the part read closely, with the conclusion and limitations.

## What the audit measures

It counts declarations. The authors pulled every paper submitted to ICLR 2026 (19,525 papers,
accepted, rejected and withdrawn alike, through OpenReview) and every paper accepted to EMNLP 2025
(3,216), used Gemini 2.5 Flash to find the AI-disclosure statement in each, and then tagged what
each statement says AI was used for. ICLR 2026 encouraged, but did not require, a separate
disclosure section; the authors say the policies are not strictly enforced.

So the unit is a paper, and the measure is whether its authors wrote a statement declaring AI use,
and what tasks that statement names. It is about the writing of papers by their authors. Peer
review is not covered: the authors removed all peer-review tasks from their task list because
they are "unrelated to manuscript preparation".

## What it found

| measure | ICLR 2026 | EMNLP 2025 |
|---|---|---|
| papers audited | 19,525 submitted | 3,216 accepted |
| papers with an AI-disclosure statement | 64% (12,577) | 40% (1,290) |
| of those statements: declare AI help editing the paper's text | 96.5% | 81.4% |
| of those statements: declare AI help creating or editing code | 16.1% | 23.3% |
| of those statements: declare AI-generated synthetic data | 2.1% | 2.5% |
| of those statements: declare AI translation of the paper | 1.6% | 2.0% |
| of those statements: include a statement of the authors' responsibility | 23% | 2% |

Other findings that matter for using the numbers: one disclosure statement appears word for word
in 95 unrelated ICLR submissions, which the authors read as boilerplate written to satisfy the
policy rather than to describe real use; and about half of the ICLR statements spend their words
on what AI was *not* used for. The tagging was done by a language model, checked against three
human annotators on 100 statements (agreement in the low to mid 90s percent).

## Can it be the second source for leg C?

No. It is context, not a measure of the thing leg C scores.

- **It measures whether people said they used AI, not how much of the work AI did.** A paper
  with no statement may have used AI and said nothing; a statement that names a task says the
  task was touched, not what share of it the tool did. Leg C asks for a share of the inputs to
  frontier progress, and no number in the audit is a share of work.
- **The dominant declared use is text editing**, which the definition does not count as an input
  to AI progress. The nearest thing to an input is declared help with code: 16.1% of the
  statements, which is about 10% of all ICLR 2026 submissions. Even that is the share of papers
  declaring some code help, not the share of code written by AI.
- **It is not frontier research.** ICLR submissions are the whole of one field's output,
  mostly from universities, not the work of building frontier models, which happens in a few
  companies and is largely unpublished. The leg is about the latter.
- **It is one audit of one year.** There is no series. The authors do not say they will repeat
  it, and ICLR's own policy has no published statistics. A second source has to be something the
  weekly reading can re-read.

What it is good for: it is the first large count of declared AI use in machine-learning papers
from outside any company, and a yearly repeat (by these authors or by the venues themselves)
would give a dated, outside-the-company trend in how openly the field says it uses AI for
writing and code. That belongs beside leg C as background, in the same way the code-share
statements from Google and the Anthropic staff poll sit beside the gauge unscored, and only if
John wants it recorded at all.

## What the roadmap step still needs

The step stays open. The kind of source it is waiting for is one of these, none of which exists
in the record yet:

1. A survey of researchers at frontier laboratories that asks what share of their research work
   (code, experiments, ideas) AI now does, repeated on a schedule, run by someone other than the
   laboratory.
2. A venue or journal statistic that reports the share of research work declared as AI-done, not
   the share of papers with a declaration.
3. A measurement of a company's AI research output that the company does not control, for
   example an outside audit of the R&D Automation Index.

Until one appears, the Anthropic index scores the leg alone, as John ruled on 2026-10-17, and the
weekly reading's third leg C read keeps flagging candidates.

**Later the same day.** The wider search for these three kinds of source, across venue
statistics, researcher surveys and independent measurements, is `docs/leg-c-second-source-2026-10-17.md`:
26 candidates judged, none qualifying, no row added.
