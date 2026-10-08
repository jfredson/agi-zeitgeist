# A measurable definition of "entering the singularity"

**Status: adopted 2026-10-08 (amendment A17 in `docs/amendments.md`), with four legs.**
The frozen values are in `docs/singularity-entry-thresholds.json`; the page at
agizeitgeist.com scores the gauges from that file. The draft this grew from
is kept unchanged as `docs/singularity-entry-definition-draft-2026-10-07.md`. Changing any
frozen value is an amendment entry, never a quiet edit.

It began when John noticed that a top comment on r/accelerate ("any prediction made right
now about the next 5 years is gonna look stupid in retrospect") matches one of the standard
definitions of the singularity, and asked whether the idea could be made into a definition, a
progress measure and a mark to cross.

## 1. The problem with the existing definitions

Three definitions have been in use since the 1990s (Yudkowsky's 2007 "three schools"), and
a fourth, economic one sits beside them:

| school | source | claim | what it measures |
|---|---|---|---|
| accelerating change | Kurzweil, 2005 | progress is super-exponential and predictable | pace of capability growth |
| event horizon | Vinge, 1993 | past some point our models stop working | how far ahead forecasts work |
| intelligence explosion | I. J. Good, 1965 | AI improves AI, so progress feeds on itself | share of progress produced by AI |
| growth mode | Hanson, 2000 | each new mode of the economy doubles output a hundred times faster than the last | doubling time of world output |

Each one, used alone, has a known false positive:

- **Accelerating change alone** fires on any sector having a fast decade. Moore's law
  was a steady exponential for fifty years and nobody called it a singularity.
- **Event horizon alone** fires in every technological revolution as felt from inside.
  Five-year forecasts about the internet made in 1995 look stupid in retrospect too.
  It is also a claim about the forecasters, not about the world.
- **Intelligence explosion alone** cannot be measured from outside the labs, and a
  high share of AI-written code in a slow-moving field would not be a singularity.
- **Growth mode alone** lags everything else by years and cannot say what caused it.

The definition: entry means all four being true at once, and staying true.

## 2. The four legs

One capability measure, chosen and frozen, anchors legs A and B: the length of software
task (in minutes an expert human needs for it) that the best public AI system finishes
half the time, as published by METR. It is chosen because it has not saturated the way
benchmarks do. Successor rule: when it stops moving, a replacement measure is named before
that happens, the overlap period is published, and the switch is an amendment.

Let C(t) be that measure at time t. The reference year for every leg is 2019.

### Leg A: pace is accelerating

Doubling time T(t) is how long C takes to double, estimated over a trailing window of
twelve months with at least three frontier readings in it:

    T(t) = ln 2 / (slope of ln C over the trailing twelve months)

A steady exponential has constant T. The singularity signature is T falling over time.
Windows that include a reading past 16 hours are not scored, because METR treats estimates
past 16 hours as beyond its task suite's reliable range and excludes them from its own fit.

- **Threshold:** T(t) at or below one month (30.44 days) and still falling over the last
  two windows.
- **Gauge (0 to 1):** g_A(t) = clip((T_ref − T(t)) / (T_ref − T\*), 0, 1), where T_ref is
  the doubling time anchored at the reference year. The trailing-window series cannot be
  computed in 2019 itself (one reading), so T_ref is METR's own fit over all frontier
  models from 2019 to early 2026, 187.8 days (agent decision, 2026-10-08).

### Leg B: forecasts have stopped working

For forecasts of C made at time s with lead d (that is, about C(s + d)), the skill score
against the trend-extrapolation baseline is

    S(s, d) = 1 − (mean squared error of the forecasts, log scale)
                / (mean squared error of extrapolating the trend as of s, log scale)

The baseline is trend extrapolation, not "no change". In a world of steady fast
progress, "no change" loses badly but the trend wins, and that world is Kurzweil's,
not Vinge's. The event horizon is the point where even the trend breaks.

The forecast horizon H(s) is the largest lead d at which S(s, d) is still above zero.

- **Threshold:** H(t) at or below one year.
- **Gauge:** g_B(t) = clip((H_ref − H(t)) / (H_ref − 1 year), 0, 1), with H_ref the
  horizon in the reference year.
- **Direction is recorded, not just size.** Were the forecasts too slow or too fast?
  Milestones from the 2016 Grace survey mostly arrived early. "Consistently too slow"
  is a claim about the world; "unpredictable" hides it.
- **Lag.** H(t) can only be computed once t + d has passed, so leg B is confirmed in
  arrears. The real-time stand-in is revision velocity: with M(t) the consensus
  arrival date for human-level AI (surveys, Metaculus, Manifold, all already in
  `data/aggregates.csv`), let D(t) = M(t) − t be the years remaining. If M is
  constant, D falls one year per year. Excess pull-in is

        v(t) = −dD/dt − 1

  which is zero when the date is standing still and positive when the date is being
  pulled in faster than time passes. Sustained positive v is the leading indicator
  that forecasts are failing in the slow direction. It is reported beside g_B, never
  substituted for it.
- **Not yet measurable.** The forecast-versus-outcome ledger is not built, so neither
  H(t) nor H_ref exists today. The gauge is shown as "not yet measurable" until it is.

### Leg C: AI is doing the improving

Let f(t) be the share of inputs to frontier AI progress (code, experiments, research
ideas) supplied by AI systems rather than people, from the best measurement available.
Candidate sources: lab self-reports of AI-written code share, surveys of frontier
researchers on time saved, and the AI-contribution disclosures that some venues now
require on papers.

- **Threshold:** f(t) at or above one half.
- **Gauge:** g_C(t) = clip(f(t) / 0.5, 0, 1).
- **This is the weakest-measured leg.** Today f is Anthropic's self-measured share of its
  own AI research work that its model "leads": one company, judged by the model itself.
  A company's share of all new code written by AI is a proxy at best and is shown but not
  scored. Every f value carries its source and whether it is a self-report.

### Leg D: the economy has changed mode

Let G(t) be world real output growth over the previous year (World Bank, world aggregate,
constant 2015 US dollars). Its doubling time is T_D(t) = ln 2 / ln(1 + G(t)).

Hanson's finding is that the world economy has had three growth modes (hunting, farming,
industry), each doubling output about a hundred times faster than the one before: about
230,000 years, 860 years and 15 years per doubling. A new mode would double output in years
or less. Leg D asks whether that has started.

- **Threshold:** G(t) at or above 30 percent a year, which is a doubling time of about 2.6
  years or less. This is Davidson's published line for "explosive growth" (Open
  Philanthropy, 2021), chosen so the number is not the project's own invention. It is far
  above anything in the modern record (the series peaks near 6.5 percent) and well short of
  Hanson's "days, not years", so it fires early in a new mode without firing on a boom.
- **Gauge:** g_D(t) = clip((T_ref − T_D(t)) / (T_ref − T_D\*), 0, 1), with T_ref the doubling
  time at the mean growth rate from 1961 to the reference year 2019 (about 20 years) and
  T_D\* the threshold doubling time.
- **Timing.** World output is reported once a year and revised. One calendar year whose
  growth crosses the line counts as all four of its quarters holding; persistence is met by
  one full year above the line, confirmed when the following year's first estimate is
  published. A revision that pulls a year back below the line resets the count.
- **Why a fourth leg.** John's ruling (2026-10-08), against the agent's recommendation to
  publish it beside the mark rather than inside it: it is the only leg measured by people
  outside the AI field, so it guards against a singularity on paper, where benchmarks and
  lab self-reports fire and nothing in the world changes. The cost, accepted knowingly:
  output lags capability by years, so this leg will usually be the bottleneck, and the
  progress number below will track the economy until it moves.

## 3. The mark

**We have entered the singularity, as defined here, when all four gauges equal one for
four consecutive quarters.** Any leg dropping back below its threshold resets the count.
This is the same shape as the three-month persistence rule in the vocabulary ledger
(methodology section 8).

The status at any date is one of: not entered; approaching (all four gauges above one
half); mark crossed, under persistence test (count in progress); entered (count complete,
with the quarter it completed). A leg that is not yet measurable cannot be at its
threshold, so the status can only be "not entered" while any leg is unmeasured.

## 4. Progress toward it

The four gauges are published separately, each in its own panel. If a single number is
wanted:

    P(t) = min(g_A(t), g_B(t), g_C(t), g_D(t))

The smallest gauge, not the average. The definition requires all four, so the weakest leg
is the honest distance remaining. An average would let one runaway leg hide stalled ones.
This also keeps methodology section 9's rule: series are never combined into an index. A
minimum is not an index; it is the definition's own bottleneck. While a leg is not yet
measurable, P(t) is reported as "at most" the minimum of the measured legs, since the
missing one can only lower it.

## 5. Tests the definition owes

1. **Backward test, owed.** Run on every year from 1995 to 2019 with the best data
   available, the definition must return "not entered". Specifically, 1995 to 2000
   (internet) should fire leg B and nothing else; 2012 to 2017 (deep learning) should fire
   leg A weakly and nothing else. The leg A series starts in 2019 and leg C in 2026, so
   the test cannot run yet. **Adopted without it, by John's ruling of 2026-10-08, with this
   gap stated on the page.** Older capability series must be built before it can run; if
   it then fires on those periods, the thresholds are wrong and get amended.
2. **Preregistration.** The capability measure, the reference year, the four thresholds and
   the persistence window were frozen on 2026-10-08, before any gauge was published.
   Changing any of them afterwards is an amendment entry.
3. **Self-reference.** If leg B is true, forecasts of *when the mark will be crossed* are
   themselves unreliable. The mark is therefore observed, never forecast. The project
   publishes status, not an arrival date.
4. **What it does and does not claim.** Crossing the mark establishes that the singularity
   *as defined here* has been entered. It does not settle which school was right, and it
   does not establish that the world is now unknowable. It establishes that four stated
   measurements crossed four stated lines and stayed there.

## 6. Relation to the tracker

The Zeitgeist tracker measures what people believe. This definition measures the world.
They are kept apart on purpose, and the interesting chart is the two side by side: the
share of statements claiming we are in or near the singularity (streams E, F and the
vanguard sub-series) against P(t). Divergence in either direction is a finding. The hedging
rule (R3) in the vanguard codebook already gives a proxy for a community's sense of its own
forecast horizon, and can be charted against g_B.

## 7. Record of the rulings (2026-10-08)

Proposed by the agent, approved by John unless marked otherwise:

| question | ruling | reason |
|---|---|---|
| anchor for legs A and B | METR 50% time horizon, with the successor rule above | the one capability series that has not saturated |
| thresholds | the draft's placeholders as written: one month, one year, one half, reference year 2019, four quarters | preregistered before any gauge; placeholders had been published in the draft a day earlier |
| backward test | adopt without it, gap stated | the data to run it does not exist yet; waiting would mean never publishing |
| economic leg | **added as leg D (decided by John, against the agent's recommendation)** | the only leg measured outside the AI field |
| leg D line | 30 percent a year (Davidson 2021); reference the 1961 to 2019 mean | a published line, not an invented one |
| leg D timing | one annual reading covers its four quarters; revisions reset | the series is annual and revised |
