# Draft: a measurable definition of "entering the singularity"

**Status: draft for me's review, 2026-10-07. Not adopted. Not part of methodology
version 2.** Written after I noticed that a top comment on r/accelerate ("any
prediction made right now about the next 5 years is gonna look stupid in retrospect")
matches one of the standard definitions of the singularity, and asked whether the idea
could be made into a definition, a progress measure and a mark to cross.

## 1. The problem with the existing definitions

Three definitions have been in use since the 1990s (Yudkowsky's 2007 "three schools"):

| school | source | claim | what it measures |
|---|---|---|---|
| accelerating change | Kurzweil, 2005 | progress is super-exponential and predictable | pace of capability growth |
| event horizon | Vinge, 1993 | past some point our models stop working | how far ahead forecasts work |
| intelligence explosion | I. J. Good, 1965 | AI improves AI, so progress feeds on itself | share of progress produced by AI |

Each one, used alone, has a known false positive:

- **Accelerating change alone** fires on any sector having a fast decade. Moore's law
  was a steady exponential for fifty years and nobody called it a singularity.
- **Event horizon alone** fires in every technological revolution as felt from inside.
  Five-year forecasts about the internet made in 1995 look stupid in retrospect too.
  It is also a claim about the forecasters, not about the world.
- **Intelligence explosion alone** cannot be measured from outside the labs, and a
  high share of AI-written code in a slow-moving field would not be a singularity.

The proposal: define entry as all three being true at once, and staying true.

## 2. The three legs

One capability measure, chosen and frozen in advance, anchors legs A and B. The
working candidate is the length of task (in human-hours) that the best public AI
system can complete unaided at a stated success rate, as published by METR. It is
chosen because it has not saturated the way benchmarks do. A successor rule is needed
for the day it does saturate: the replacement measure must be named before the old one
stops moving, and the overlap period published.

Let C(t) be that measure at time t.

### Leg A: pace is accelerating

Doubling time T(t) is how long C takes to double, estimated over a trailing window of
W months (W = 12 to start):

    T(t) = ln 2 / (slope of ln C over the trailing W months)

A steady exponential has constant T. The singularity signature is T falling over time.

- **Threshold:** T(t) at or below T\* (placeholder: one month) and still falling over
  the last two windows.
- **Gauge (0 to 1):** g_A(t) = clip((T_ref − T(t)) / (T_ref − T\*), 0, 1), where
  T_ref is the doubling time in a frozen reference year (placeholder: 2019).

### Leg B: forecasts have stopped working

For forecasts of C made at time s with lead d (that is, about C(s + d)), the skill
score against the trend-extrapolation baseline is

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

### Leg C: AI is doing the improving

Let f(t) be the share of inputs to frontier AI progress (code, experiments, research
ideas) supplied by AI systems rather than people, from the best measurement available.
Candidate sources: lab self-reports of AI-written code share, surveys of frontier
researchers on time saved, and the AI-contribution disclosures that some venues now
require on papers.

- **Threshold:** f(t) at or above one half.
- **Gauge:** g_C(t) = clip(f(t) / 0.5, 0, 1).
- **This is the weakest-measured leg** and the draft says so. Every f value carries
  its source and whether it is a self-report.

## 3. The mark

**We have entered the singularity, as defined here, when all three gauges equal one
for four consecutive quarters.** Any leg dropping back below its threshold resets the
count. This is the same shape as the three-month persistence rule in the vocabulary
ledger (methodology section 8).

The status at any date is one of: not entered; approaching (all three gauges above
one half); mark crossed, under persistence test (count in progress); entered (count
complete, with the quarter it completed).

## 4. Progress toward it

The three gauges are published separately, each in its own panel. If a single number
is wanted:

    P(t) = min(g_A(t), g_B(t), g_C(t))

The smallest gauge, not the average. The definition requires all three, so the weakest
leg is the honest distance remaining. An average would let one runaway leg hide two
stalled ones. This also keeps methodology section 9's rule: series are never combined
into an index. A minimum is not an index; it is the definition's own bottleneck.

## 5. Tests the definition must pass before adoption

1. **Backward test.** Run on every year from 1995 to 2019 with the best data
   available, it must return "not entered". Specifically, 1995 to 2000 (internet)
   should fire leg B and nothing else; 2012 to 2017 (deep learning) should fire leg A
   weakly and nothing else. If it fires on those periods, the thresholds are wrong.
2. **Preregistration.** The capability measure, the reference year, T\*, the one-year
   horizon, the one-half share and the four-quarter persistence are set and frozen
   before any current-period value is published. Changing any of them afterwards is
   an amendment entry.
3. **Self-reference.** If leg B is true, forecasts of *when the mark will be crossed*
   are themselves unreliable. The mark is therefore observed, never forecast. The
   project publishes status, not an arrival date.
4. **What it does and does not claim.** Crossing the mark establishes that the
   singularity *as defined here* has been entered. It does not settle which of the
   three schools was right, and it does not establish that the world is now
   unknowable. It establishes that three stated measurements crossed three stated
   lines and stayed there.

## 6. Relation to the tracker

The Zeitgeist tracker measures what people believe. This definition measures the
world. They are kept apart on purpose, and the interesting chart is the two side by
side: the share of statements claiming we are in or near the singularity (streams E,
F and the vanguard sub-series) against P(t). Divergence in either direction is a
finding. The hedging rule (R3) in the vanguard codebook already gives a proxy for a
community's sense of its own forecast horizon, and can be charted against g_B.

## 7. Open questions for me

- Is METR's task horizon the right anchor for C, and what is the successor rule?
- Placeholders to set: T\* (one month?), reference year (2019?), persistence (four
  quarters?). Each needs a one-line reason recorded here.
- Should an economic leg (Hanson's world-output doubling time) be added as a fourth,
  lagging confirmation, or does it belong in a separate "has it mattered yet" measure?
- Where does the data for leg C come from in a form that is not pure self-report?
