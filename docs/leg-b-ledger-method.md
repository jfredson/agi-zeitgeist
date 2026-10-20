# Leg B ledger: method for scoring the 2016 survey's milestone forecasts

**Status: method written 2026-10-09 by the agent, before any ledger row was built. Every
choice below is the agent's own and I can reverse any of them. Changing a rule after the
ledger is built is an amendment entry, never a quiet edit.**

## What this ledger is for

The singularity-entry definition (`docs/singularity-entry-definition.md`, leg B) says
that when forecasts were wrong we should record which way: did things come sooner or later
than predicted? It also says, without a source, that "milestones from the 2016 Grace survey
mostly arrived early". This ledger checks that sentence (which was amended on 2026-10-12,
amendment A23, after the ledger's first reading). It takes every milestone date the
2016 survey of machine learning researchers published, finds when each milestone actually
arrived, and scores each forecast by how far ahead it looked and how far off it was.

It does not compute the leg B gauge. That gauge is defined on forecasts of one number (the
length of software task an AI can finish, as measured by METR) and compares them with
simply extending the trend. The survey's milestones are yes-or-no events with no trend to
extend, so they cannot fill that formula. Whether this ledger should feed the gauge at all,
and how, is a question for me.

## Sources

**The forecasts.** Grace, Salvatier, Dafoe, Zhang and Evans, "When Will AI Exceed Human
Performance? Evidence from AI Experts", arXiv 1705.08807, version 3 (May 2018; the version
published in the Journal of Artificial Intelligence Research). Table S5 lists 32 milestones,
each with its full description, how many people answered it, and a median in years from
2016. That median is the year by which the combined answers give an even chance, averaged
over the survey's two ways of asking. The table is read from the paper's own source files
on arXiv, not retyped from a summary. AI Impacts' survey page gives different medians
because it reports only one of the two ways of asking; the paper's table is the published
figure and is the one used.

**When each milestone arrived.** A dated public demonstration: the paper, the maker's
own announcement, or the official result of a competition, read at its source. News
coverage and blog round-ups can point to a demonstration but are never the evidence for it.
Each row records the source, its date, and how that date was established.

**A comparison, not a source.** Patrick Levermore's scoring for AI Impacts (1 March 2023)
judged which milestones had been met by early 2023. His yes-or-no verdicts are recorded
beside ours so that disagreements show. They are never used to decide a row.

## The forecast date and the lead time

- **When the forecast was made:** 28 June 2016, the day the survey closed (answers came in
  between 3 May and 28 June 2016). Using the middle of that window instead would move every
  number below by about a month.
- **Forecast lead:** the Table S5 median, in years.
- **Forecast date for the milestone:** 28 June 2016 plus the forecast lead.
- **Actual lead:** the time from 28 June 2016 to the arrival date, in years (days divided by
  365.25).

## How "arrived" is decided

The survey asked when each milestone would be **feasible**, meaning "one of the best
resourced labs could implement it in less than a year if they chose to". Nobody can observe
feasibility from outside. What can be observed is the first public demonstration, which can
only come at or after feasibility. So every arrival date here means "no later than", and the
true lead times may be shorter, never longer. This leans every score towards "arrived late".

Each milestone's full description in Table S5 is split into its stated conditions (for
example, StarCraft: beat the best human players, at least half the time, given only a video
of the screen). Each row then gets one of four verdicts:

1. **Arrived.** A dated public demonstration meets every stated condition.
2. **Arguably arrived.** A demonstration meets the main capability, but one stated
   condition was not tested or was only nearly met (for example, judged by ordinary
   listeners where the milestone says expert listeners). The row names the gap.
3. **Not arrived.** No public demonstration meeting the main capability was found by
   9 October 2026. The nearest demonstration found is recorded, if there is one.
4. **No bar.** The description sets no bar a demonstration could be checked against (for
   example, "give good answers"), so the agent cannot decide it without inventing one.
   (Called "left for me" until 2026-10-12, when I ruled that these rows stay out of
   the scores rather than being given a bar after the fact; the verdict's meaning is
   unchanged.)

When more than one demonstration qualifies, the earliest found is used. Because the search
cannot prove nothing earlier exists, a later find can only move a date earlier.

## How each forecast is scored

For each milestone that arrived or arguably arrived:

- **Years early or late:** actual lead minus forecast lead. Below zero means it came sooner
  than forecast.
- **Ratio:** actual lead divided by forecast lead. A ratio of 0.5 means it came in half the
  forecast time; 2 means it took twice as long. The ratio is the main score, because a
  two-year miss on a three-year forecast is worse than a two-year miss on a thirty-year one.
- **Within a factor of two:** whether the ratio is between 0.5 and 2.

For a milestone that has not arrived, the actual lead is only known to be longer than the
time elapsed so far (10.28 years at 9 October 2026):

- If its forecast date has passed, it is **late**, by at least the elapsed time minus the
  forecast lead, and its ratio is at least elapsed divided by forecast.
- If its forecast date has not passed, it is **not yet due** and is not scored either way.

Rows with no bar are listed but not scored.

## What is reported

- Every row: milestone, the survey's forecast, the verdict, the demonstration and its date,
  the gap if arguably arrived, the scores, and the 2023 comparison verdict.
- Counts of early, late and not yet due, twice: once counting only "arrived" as arrived (the
  strict reading) and once also counting "arguably arrived" (the generous reading). The two
  are always shown together, because the agent's judgement sits between them.
- The same counts split by forecast lead: under five years, five to ten years, and ten years
  or more. A forecast horizon in the definition's sense would show up as forecasts going
  wrong past some lead. With 32 yes-or-no events this is a description, not a measurement.

## Files

- `data/leg_b_ledger.csv`: one row per milestone, with every source and date.
- `scripts/leg_b_ledger.py`: checks the rows against this method and prints the scores.
- `docs/leg-b-ledger-2026-10.md`: the first reading and the questions it leaves for me.
