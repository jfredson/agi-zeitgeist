# How the backward test is run (1995 to 2019)

Written 2026-10-09, before any series was built, by an agent session working on John's
four-day weekend list. This file says how the test owed by
`docs/singularity-entry-definition.md` section 5, item 1, is run. The definition says what
the test must return ("not entered" for every year from 1995 to 2019) and what pattern it
expects (the internet years, 1995 to 2000, light up the forecasting condition and nothing
else; the deep-learning years, 2012 to 2017, light up the pace condition weakly and nothing
else). It does not say how to measure the conditions before 2019, so this file does.

The test uses the frozen values in `docs/singularity-entry-thresholds.json` exactly as they
stand. Nothing in that file is changed by this work, whatever the result. If the test
returns "entered" for any year, that is reported as a failure of the thresholds, which the
definition says is settled by an amendment, not by this session.

## The four conditions, one per leg

The definition calls its four conditions legs A to D. Each needs a series that reaches back
to 1995.

### Leg A, the pace of progress getting faster

The frozen measure, METR's task-length measure, starts in 2019 (its first reading is
GPT-2), so it cannot be used. The stand-in is **the training compute of record-setting AI
systems**: the amount of computing used to train each AI system that used more than any
system before it.

- Source: Epoch AI's "Notable AI Models" dataset, `https://epoch.ai/data/notable_ai_models.csv`
  (published under a Creative Commons attribution licence). The rows from 1990 to 2020 that
  carry a training compute figure are saved in the repo as
  `data/backward-test/epoch-notable-models-1990-2020.csv`, with the retrieval date, so the
  run does not depend on the live file.
- Why this series: it is the only published series that covers AI systems continuously
  from the 1990s to 2019 on a scale where "doubling" means something. Its weakness, stated
  plainly: it measures what went into AI systems, not what they can do. A doubling of
  training compute is not a doubling of capability. So this leg's backward result is a
  check on whether the pace rule fires on a fast-growing AI series, not a reading of the
  frozen measure.
- "Record-setting" stands in for METR's "best at release" flag: a system counts if its
  training compute is larger than that of every earlier system in the dataset.
- The doubling time is computed exactly as `scripts/site.py` computes it for the live
  measure: for each record-setting system, take every record-setting system released in
  the 365 days up to and including it; if there are at least three, fit a straight line to
  the logarithm of compute against time and turn the slope into days per doubling.
- The condition is met at a date when the latest such window is at or below 30.44 days
  and the last three windows each came in quicker than the one before (the live rule).
  The 16-hour exclusion is specific to METR's measure and has no counterpart here.
- The gauge uses the frozen reference doubling time (187.8 days) and the frozen line
  (30.44 days). The reference was fitted on METR's measure, not on compute, so the gauge
  values are shown for the record but carry less weight than the yes-or-no against the line.
- Also reported, as a stricter check: whether any single window anywhere in a year comes in
  at or below 30.44 days, even if the "getting quicker" part fails.

### Leg B, forecasts having stopped working

This leg needs forecasts of the capability measure made at past dates with known lead
times, scored against what happened and against extrapolating the trend. No such ledger
exists for 1995 to 2019 for any AI capability series, and building one from scratch is
outside this session (another session is building the ledger for the live measure). So:

- Leg B is recorded as **not measurable** for every year from 1995 to 2019.
- Under the definition's own rule (section 3), a leg that cannot be measured cannot be at
  its line, so the status can only be "not entered". The report says separately whether
  the verdict would still hold with leg B assumed to be at its line, so that the verdict
  does not rest on a missing leg.
- The expected pattern "the internet years light up leg B" therefore cannot be checked,
  and is reported as untested, not as passed.

### Leg C, AI doing the improving

No measurement of the share of AI research work done by AI systems exists for any year
before 2025. The record for 1995 to 2019 is therefore **not measurable**, with the
supporting context written down: the first widely released AI tool that wrote code
(GitHub Copilot, technical preview announced 2021-06-29) came after the test period, and
the main pre-2020 case of AI designing AI systems (automated design of network shapes,
Zoph and Le, 2016) covered a narrow part of the work. Nothing is estimated or interpolated
for this leg. As with leg B, the report also checks the verdict with leg C assumed met.

### Leg D, the economy changing gear

The series is already in the repo: World Bank world real output growth, one row a year,
`worldbank-gdp-growth-*` in `data/world_measures.csv`. It is used exactly as the live page
uses it: the condition is met in a year whose growth is at or above 30 percent, and one
annual reading covers that year's four quarters. The gauge uses the frozen reference (the
mean growth from 1961 to 2019 turned into a doubling time).

## Turning legs into a verdict

For each quarter from the first quarter of 1995 to the last quarter of 2019, each leg is
"met", "not met" or "not measurable" as of the last day of the quarter. The status for the
quarter is "entered" only after four consecutive quarters with all four legs met. A year's
verdict is "entered" if any quarter in it is "entered".

## What a pass and a fail look like

- **Pass:** "not entered" for every quarter from 1995 to 2019. The report also says
  whether the pass holds on the measured legs alone (that is, with legs B and C assumed met),
  which is the stronger form.
- **Fail:** "entered" for any quarter. Reported plainly as a failure, with the leg and
  quarter that caused it. No threshold, window, series choice or rule in this file is
  changed afterwards to make a fail go away.
- **Pattern check (secondary):** for 1995 to 2000, which legs are met (the definition
  expects leg B only); for 2012 to 2017, whether leg A's gauge is above zero but its line
  is not crossed (the definition's "weakly"). A mismatch here is reported as a finding, not
  a fail.

## Files

- `scripts/backward_test.py`: the whole run, standard library only. With no arguments it
  reads the saved extract and writes the results. With `--refresh PATH` it rebuilds the
  extract from a full copy of Epoch's file.
- `data/backward-test/epoch-notable-models-1990-2020.csv`: the saved compute extract.
- `data/backward-test/results-by-quarter.csv` and `results-by-year.csv`: the outputs.
- `data/backward-test/leg-a-windows.csv`: every twelve-month window and its doubling time.

## Result of the first run (2026-10-09)

Written after the run; nothing above this section was changed after seeing the result.
Reproduce with `python3 scripts/backward_test.py`.

**Pass: "not entered" in every quarter from 1995 to 2019**, and it holds on the measured
legs alone (with legs B and C assumed met, the answer is the same). What carries it is leg
D: world growth peaked at 4.57 percent (2000) in the period, against a line of 30 percent.
Leg D's gauge peaks at 0.26 (2000), on a scale where 1 is the line.

The internet years (1995 to 2000): leg A cannot be scored (only two record-setting systems
in Epoch's list fall in those six years, LSTM in 1997 and a neural language model in 2000,
so no twelve-month window holds three); legs B and C are not measurable; leg D is far below
its line. The expected pattern ("leg B and nothing else") is **untested**, because leg B has
no series for those years.

The deep-learning years (2012 to 2017) do **not** match the expected pattern of leg A
"firing weakly". Four record-setting systems came within six months in 2014 (SPPNet, VGG16,
Seq2Seq LSTM, SNM-skip), and the twelve-month doubling time of training compute came in at
26.5 days and then 25.8 days, below the 30.44-day line. The gauge reads 1.00 from late 2014
to mid-2016. Leg A was not met only because the rule also asks for three windows in a row
each quicker than the last, and there were only two windows before the record-setting
stopped for a while. The same thing happens in late 2019 (24.3 days, from Megatron-BERT,
T5 and AlphaStar within six weeks). Two cautions on reading this: the series measures what
went into AI systems, not what they could do; and with only three or four systems in a
window, one large system can swing the fitted doubling time a long way.

What this means for the thresholds is a question for John, not for this run. The pass does
not depend on leg A: it rests entirely on leg D. On this stand-in series, the pace line on
its own would have been crossed in 2014, and the "getting quicker" part of the rule plus
the three-system minimum are what held it.

Files written: `data/backward-test/leg-a-windows.csv` (6 scored windows from 21
record-setting systems), `results-by-quarter.csv` (100 quarters), `results-by-year.csv`.
