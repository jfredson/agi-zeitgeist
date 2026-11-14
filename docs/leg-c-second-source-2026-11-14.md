# Leg C second source: what is new since 2026-10-17

Written by the agent on 2026-11-14, on the roadmap step "Leg C second source: find a measure of
AI's share of frontier research work that is not a company's report on itself (venue
AI-contribution disclosures, researcher surveys), and add it to `data/world_measures.csv`". It
follows the wider search of 2026-10-17 (`docs/leg-c-second-source-2026-10-17.md`), uses the same
four tests, and covers only what has appeared or been found since.

**Result: nothing new qualifies. No row was added to `data/world_measures.csv`.** The scored
series, the thresholds file and the definition are untouched, and no number on the site moves.
Seven candidates were judged; the nearest miss is METR's outside assessment of Anthropic, and one
new policy (ICLR 2027) is the likeliest place for a real second source to appear. This is a
reading note, not an amendment.

## 1. The bar

Leg C ("AI is doing the improving") is scored from the share of the inputs to frontier AI progress
(code, experiments, research ideas) that AI systems supply rather than people. A second source
qualifies only when all four of the earlier note's tests hold:

1. **It is a share of the work**, not a count of papers that declare AI use, a speed-up multiplier
   or a capability test.
2. **The work is frontier AI research**, the building of the most capable AI systems, not research
   or software in general.
3. **Someone other than the company whose work it is measured it.**
4. **It is dated, sourced to a document anyone can open, and can be read again**, so that the
   weekly reading can follow it.

## 2. How the search was run

Nine web searches and one round of reading pages at their source, all on 2026-11-14, logged in
`data/search_log.csv` as `leg-c-second-source-041` to `leg-c-second-source-050`. Unlike the
search of 2026-10-17, every page below was opened and read, not only seen through search
extracts.

## 3. Candidates and verdicts

| # | candidate | what it gives | fails on |
|---|---|---|---|
| 1 | METR, independent assessment of AI's speed-up of research at Anthropic (2026-11-05) | progress about 1.9 times the earlier rate; "perhaps ≈80%" of the extra speed due to AI | share of work; one company, once |
| 2 | METR, review of the R&D section of Anthropic's August 2026 risk report (2026-11-05) | "slightly less than twice as fast" as without AI | share of work; reviews a company's own figures |
| 3 | Epoch AI, "AI use in research" explorer (updated 2026-11-09) | share of preprints that acknowledge AI, monthly | share of work; not AI research |
| 4 | ICLR 2027 policy on AI use by authors | every paper must carry an AI-use section, by research task | nothing to count yet |
| 5 | Forecasting Research Institute, expert panel wave 4 on AI research (published 2026-01-12) | forecasts of benchmarks, hiring, valuations | no question on share of work |
| 6 | FutureSearch, register on AI improving itself (pages of 2026-10-17) | forecasts, including a 50% median share of training environments written by AI | a forecast, not a measurement |
| 7 | Anthropic, "The AI expectations gap" | its staff's median guess of 51% (already in the record) | a company's report on itself |

**1. [METR, "Independent Assessment of AI R&D Acceleration at Anthropic in October
2026"](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment)** (2026-11-05).
[METR](https://metr.org/), a non-profit that evaluates AI systems, worked with Anthropic's internal
data from 2026-08-12 to 2026-10-29. Its main finding is that since October 2025 Anthropic's
benchmark scores have grown at about 1.9 times the rate of March 2024 to October 2025 (95%
interval 1.5 to 2.8), which it reads as roughly two years of progress in one. It adds a judgement
about the cause: "We guess that a majority (perhaps ≈80%) of the current (October 2026)
acceleration is due to AI." It also reports that Anthropic "redacted a majority of the evidence we
found most informative", and calls the staff's own speed-up polls, which reach 12 times, "only very
loose evidence". *Verdict: no, but the nearest miss so far.* It passes tests 2 and 3: it is about
frontier AI research and was measured from outside the company. It fails test 1, because a speed-up
of progress is not the share of the work AI does, and the 80% is a guess about what caused the
extra speed, not a share of the inputs. It fails test 4 as a series, because it is one engagement
with one company and no stated repeat. The weekly reading of 2026-11-09 already put the companion
review (candidate 2) to me as a possible leg C source.

**2. [METR, review of the "Risks from automated R&D" section of Anthropic's Risk Report (August
2026)](https://metr.org/blog/2026-11-05-rd-section-anthropic-risk-report-august-2026-review)**
(2026-11-05). METR's reading of the company's own report: Anthropic's public figure is "less than a
factor of 2", METR's preferred wording is "slightly less than twice as fast as it would be without
AI assistance", and METR says it is plausible the company's twice-as-fast threshold was crossed by
July 15th. *Verdict: no.* A speed-up, not a share, and a review of a company's own figures, which
the earlier note's third test treats as the company's figures.

**3. [Epoch AI, "AI use in research"](https://epoch.ai/data/ai-research-use)** (explorer, updated
2026-11-09; [method](https://epoch.ai/data/ai-research-use-documentation)). [Epoch
AI](https://epoch.ai/), an independent research group, now runs its method from the mathematics
note of September across physics, mathematics and statistics preprints on arXiv and biology
preprints on bioRxiv, monthly, with a human check of the model's readings. It does not cover
computer science: papers are filed by their main arXiv category and no computer-science category is
counted. The nearest slice is statistics' machine-learning category, which is part of the
statistics series, not a series of its own. *Verdict: no*, on tests 1 and 2, as before. It remains
the series a future reading should most want extended to computer science.

**4. [ICLR 2027, "Policy on LLM use for research and writing
papers"](https://iclr.cc/Conferences/2027/AIPolicyForAuthors).** [ICLR](https://iclr.cc/), one of
the main machine-learning conferences, now requires every paper to carry an AI-use section, outside
the page limit, and asks for some of the same information on the submission form. The policy lists
research tasks for which disclosure is required (among them proposing or refining hypotheses,
designing experiments, implementing methods and interpreting results) and tasks for which it is
recommended (among them writing or editing code and drafting text). The conference says these
disclosures "may be a source of useful information to the community about how AI is affecting
research workflows". *Verdict: nothing to count yet.* Once the 2027 papers are public, these
sections could be counted by task by anyone, and the conference could publish its own counts from
the form. That would still be a count of papers declaring AI help with each task, not a share of
the work, so it would fail test 1 unless someone also asks how much of each task AI did. It is the
likeliest source of a venue-level series, and the weekly reading should watch for it.

**5. [Forecasting Research Institute, "What Experts and Superforecasters Think About the Future of
AI Research and
Development"](https://forecastingresearch.substack.com/p/what-experts-and-superforecasters)**
(2026-01-12). The fourth wave of its [Longitudinal Expert AI
Panel](https://forecastingresearch.substack.com/p/introducing-leap), fielded 2025-11-20 to
2025-12-20. It asks experts and superforecasters to forecast coding-benchmark scores, entry-level
hiring at large technology firms, company value per employee and data-centre capacity. *Verdict:
no.* No question in the published results asks what share of AI research work AI does today.
Because the panel repeats, it would be a strong second source if it ever added that question.

**6. [FutureSearch, "Recursive Self-Improvement at Frontier AI
Labs"](https://futuresearch.ai/recursive-self-improvement-forecast/)** (pages dated 2026-10-17).
A forecasting company's register of questions about AI improving itself. One
[question](https://futuresearch.ai/app/p/a/rsi-shares-of-research) forecasts the share of
reinforcement-learning training environments at the largest AI company that AI will have written
by 2026-12-31, with a median of 50%, and notes there is no public measurement. *Verdict: no.* A
forecast, not a measurement.

**7. [Anthropic, "The AI expectations
gap"](https://www.anthropic.com/research/ai-expectations-gap).** Anthropic's own staff poll, with a
median guess that AI does 51% of the work of building a frontier model; this figure is already in
the record beside leg C, unscored. *Verdict: excluded by test 3.*

## 4. Why it is still empty

Four weeks on, the three shapes the earlier notes listed are still missing. Nobody outside a
company has surveyed frontier researchers on the share of their work AI does. No venue has yet
published the share of research work declared as AI-done, although ICLR 2027 has now built the
form that could produce a count by task. The one new outside measurement of a frontier company
(METR's) measures how much faster progress is, not how much of the work AI does, and most of its
evidence is held back. The definition's measure, a share of the inputs, is still published only by
a company about itself.

## 5. For me

1. **METR's 1.9 times.** The weekly reading of 2026-11-09 asked whether METR's review belongs in
   the record. The agent's recommendation is to keep it out of `data/world_measures.csv`, because
   a row there is read as a measure of the leg and a speed-up is not a share, and to name it in the
   leg C text on the page as outside context if I want readers to see it. Either change is mine to
   make; neither is made here.
2. **What the step waits for.** The step can stay a standing watch, or narrow to the two shapes
   most likely to appear: counts from ICLR 2027's disclosure sections (from the conference or from
   someone counting the published papers), and Epoch's explorer extended to computer science. The
   agent's recommendation is to narrow it to those two and to METR repeating its assessment, so
   that the weekly reading knows exactly what to look for.
3. **Nothing here proposes a scored series** and no amendment is drafted.

## 6. What a future reading should watch

- **ICLR 2027:** any statistics the programme chairs publish from the disclosure form, and any
  count of the disclosure sections once papers are public.
- **Epoch AI:** the "AI use in research" explorer adding computer science or machine learning.
- **METR:** a repeat of the Anthropic assessment, or the same assessment of another company.
- **Forecasting Research Institute:** a panel wave that asks what share of AI research work AI
  does today.
- **NeurIPS:** results of its authors' survey on AI use, still unpublished.
