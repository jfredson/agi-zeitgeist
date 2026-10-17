# Proposal: a headline that measures distance, not a verdict

*Written 2026-10-17 by the agent at John's request, relayed through the master session the same
afternoon. Nothing scored changes with this document: the frozen definition, the thresholds file,
the scored series and the verdict's wording all stay as they are. The numbered decisions at the
end each carry a confidence and the strongest alternative, as the ground rule of 2026-09-08
requires. If adopted, decision 5 says what gets numbered as an amendment and what does not.*

## 1. The ask, in John's words

"I think we should re-evaluate whether 'Not Yet' is the right headline number for the AGI
Zeitgeist tracker because it's just a binary. The more interesting question is how close are we
and what progress have we made on the path from 0-100% or 100 years away down to 0."

The occasion: the parent site's new Projects page (sentient-horizons.com/projects/) puts each
project's headline on one shelf. Beside "0.5%", "42%", "28 of 35" and "2058", the Zeitgeist's
reads "Not yet". The parent's fetch script makes that word itself from `status.json`: "Yes" if
the status is `entered`, otherwise "Not yet", with a label naming the part furthest from its
line.

## 2. What must not change

- **The definition and its frozen values** (`docs/singularity-entry-definition.md`,
  `docs/singularity-entry-thresholds.json`, adopted 2026-10-08 as amendment A19). The four
  legs, their thresholds, the reference year, the persistence rule and the scored series are
  preregistered; changing any of them is an amendment with its own reason, and this proposal
  gives none.
- **The verdict and its wording.** "Not yet." is the ruled answer to the ruled test, and the
  page's four status words (not entered; approaching; mark crossed, under persistence test;
  entered) stay. Whatever number goes above it, the test's answer stays on the page beneath.
- **Section 4 of the definition**, which already defines the one progress number: P(t), the
  smallest of the four gauges, reported as "at most" while a leg is unmeasured. The reason
  given there stands: the test needs all four, so the weakest leg is the honest distance left,
  and an average would let one runaway leg hide stalled ones. Methodology section 9 adds that
  series are never combined into an index.

So the question is not "what number is the singularity at" (the definition answers that: the
smallest gauge) but **which of the numbers the definition already produces should be the
headline, in what form, and with what words.**

## 3. What the legs give today (built 2026-10-17)

| leg | what is measured | reading now | the line | reference (0% mark) | share of the way |
|---|---|---|---|---|---|
| A, pace | days per doubling of the longest task AI can finish, trailing twelve months | 120.8 days (window ending 2026-02-05) | 30.44 days | 187.8 days (METR's fit 2019 to early 2026) | 43% |
| B, forecasts | how far ahead forecasts of A still beat trend | not yet measurable (the forecast ledger is not built) | 1 year | none set | unmeasured |
| C, AI doing the improving | share of Anthropic's AI research its model leads (R&D Automation Index) | 26% (2026-08) | 50% | 0% | 52% |
| D, the economy | doubling time of world output, from annual growth | 24.1 years (2.92% growth in 2025) | 2.64 years (30% growth) | 19.9 years (mean 1961 to 2019, 3.54%) | 0% |

Two facts about this table decide most of what follows.

**Leg D sits at exactly zero, and will for years.** Its gauge measures how far the doubling time
has fallen from the 1961-to-2019 average toward 2.6 years. World growth today (2.9%) is slower
than that average (3.5%), so the doubling time is longer than the reference and the gauge
clips at zero. Growth has been flat to falling since 2010 (a trend of −0.05 points a year).
Until a year's growth beats 3.5%, leg D reads 0%, and P(t), the minimum, reads 0% whatever A
and C do. That is leg D doing exactly the job John gave it on 2026-10-08, against the agent's
recommendation: it is the one leg measured by people outside the AI field, and it stops a
"singularity on paper". A headline built on P(t) inherits that choice.

**The shares are not on one scale.** Leg A's 43% is linear in days per doubling; on a
logarithmic scale (each halving of the doubling time counts the same) it would be 24%. Leg C's
52% is a share of a share. Leg D's 0% is a clipped difference of doubling times. The gauges
were designed one by one so that each is 0 at its reference and 1 at its line; that is all
"share of the way" means here, and the text around any headline should say so.

## 4. Three forms, and what each would show today

### Form 1: share of the way, the furthest leg as the headline

This is P(t) from section 4, written as a percentage. Today: **"0%"**, with "at most" because
leg B is unmeasured, and the label naming the bottleneck: "at most 0% of the way: the world
economy grows 2.9% a year and would need 30%". The status file already publishes this
(`progress: 0.0`, `bottleneck: "D"`); only the words on the page and the shelf change.

- For: it is the definition's own number, needs no amendment, cannot be gamed by a fast leg,
  and the label says in one sentence why it is zero.
- Against: for the Projects shelf it is "Not yet" rewritten as a digit. It will read 0% until
  world growth passes 3.5%, which the record's 1961-to-2025 series has done in only about a
  third of years and not since 2021 (6.5%, the rebound year). The reader learns what is
  stalled, not what is moving.

A variant, **the mean of the measured legs** (43%, 52%, 0% → **32%**), would move with A and
C. It is ruled out by section 4's own argument and by methodology section 9: it is an index,
and it lets a runaway leg hide a stalled one. Not proposed; listed so the choice is visible.

### Form 2: years to the line, from each leg's trend

Extend each scored series along its recent trend and report when it reaches its line.

| leg | trend used | years to the line |
|---|---|---|
| A | the trailing doubling time is not falling: 88 days in 2025-04, 121 days in 2026-02; over all twelve clean windows it falls about 6% a year | about 21 years at that rate; 2 to 4 years if the 2024-to-2025 halving resumes; no date on the current direction |
| B | none | unmeasured |
| C | 1% in 2026-02 to 26% in 2026-08 | about 6 months if linear (spring 2027); already past if the growth stays proportional |
| D | 2010 to 2025, −0.05 points a year | never on the current trend |

Headline under this form, the slowest leg: **"no date"**, which is the verdict again in other
words. The per-leg readings are useful and honest ("the AI-research share could cross within a
year; the economy shows no sign of it"), but as a single number the form fails today for the
same reason form 1 does: the test needs all four, and one leg has no trend toward its line.
Every number in the table also rests on extending two to twelve points, and the pace leg's
answer swings from 2 years to 21 depending on which stretch is extended, so the uncertainty
would have to be carried in the words every time.

### Form 3: a count of parts past halfway (the siblings' "28 of 35" form)

The definition's own status words already use one half: "approaching" means every gauge is
above one half. Counting the legs past that point gives **"1 of 4"** today (leg C at 52%), and
the label "parts of the test past halfway; none at its line". It moves in steps of one, which
is coarse, but every step is an event the page can explain, and it never claims a precision the
gauges do not have. It is read straight off the status file's `gauges`.

- For: honest, moves when something real happens, reads naturally beside "28 of 35" on the
  shelf, no amendment needed (it reports the gauges, it does not combine them).
- Against: four steps from 0 to 4 is a thin scale, and "past halfway" is one line chosen for
  the status word, not a measured thing. A leg at 49% and one at 1% both count as 0.

## 5. Recommendation: the count as the number, the shares as the words, the verdict beneath

On the page and on the shelf:

> **1 of 4** parts of the test past halfway, none at its line.
> Pace 43% · Forecasts unmeasured · AI doing the research 52% · Economy 0%.
> **Not yet.** Four things would all have to be true, and stay true for a year. Today none of
> them is.

The count is the headline number because it is the only one of the three that is both faithful
to the definition and moves when a leg moves. The four shares beneath it are what John asked
for, "how far along the path", leg by leg, and they are already on the page as bars; they
become numbers in a row. P(t) stays published in the status file and in the definition's
section 4, and is written out in the "Are we in the singularity?" section as "at most 0% of
the way on the weakest part, the economy", so the one-number reader still gets the
definition's own answer. The years-to-the-line readings go into each leg's panel as a
sentence with its range, never into the headline.

What the weekly reading does with it: nothing new. It appends rows; the site rebuild recomputes
the gauges, the count and the shares. A leg crossing one half is already a `noted` or
`flagged` item under its rules, and would be the reading's report line that week.

What the status file publishes: three new fields beside the existing ones, `headline`
("1 of 4"), `headline_label` (the sentence above) and `parts_past_half` (1), with `gauges`,
`progress` and `bottleneck` unchanged. The parent's fetch script reads `headline` and
`headline_label` from the file instead of making "Not yet" itself, and keeps the verdict in the
`status` variable for its label. That is a one-line change in the parent's script and a
five-line change in `scripts/site.py`.

## 6. Decisions, with confidence and the strongest alternative

1. **The headline number is the count of legs past one half, "N of 4".** Moderate confidence.
   Strongest alternative: P(t) as a percentage with "at most" (form 1), the definition's own
   number, which reads 0% today and for as long as world growth stays under 3.5%.
2. **The four shares are printed as percentages in a row beneath the number, with "unmeasured"
   for leg B.** High confidence. Alternative: keep the bars only, as now; the bars show the
   same thing but cannot be quoted or carried to the shelf.
3. **The verdict "Not yet." and its sentence stay on the page, directly beneath, as the answer
   to the ruled test.** High confidence. Alternative: drop the words and let the count stand
   alone; rejected because the count is not the test, and a reader who sees "1 of 4" should
   also see that the test needs all four and a year of persistence.
4. **Years to the line are given per leg, in each leg's panel, as a sentence with its range,
   and never as a headline.** High confidence. Alternative: a years headline from the slowest
   leg, which reads "no date" today and so answers nothing the verdict does not.
5. **Numbering.** The headline is presentation, not method: the definition's section 4 and
   the frozen values do not change, so this lands as a dated note in section 4 ("published
   as ...") and a line in the README, not as an amendment. Moderate confidence. Alternative:
   number it anyway, as the next amendment, on the ground that what the parent site shows as
   this project's one number is part of the record; John has preferred the amendment file to
   be complete rather than minimal.
6. **While P(t) is zero, the label names the bottleneck and its number** ("the economy grows
   2.9% a year and would need 30%"). High confidence. Alternative: name only the leg; rejected
   because the number is what makes the sentence checkable.
7. **No leg's gauge is redefined to make the headline move.** High confidence. The tempting
   case is leg D, where a share by growth rate (2.9 of 30, about 10%) instead of by doubling
   time would read above zero today; that is a change to a frozen gauge, needs its own reason,
   and is not proposed.

## 7. What the shelf would show today under each form

| form | headline | label |
|---|---|---|
| as now | Not yet | is the answer. Four things would all have to be true and stay true for a year; today none of them is, and how fast the world economy grows is the part furthest from its line |
| 1, furthest leg's share | 0% | at most 0% of the way: the world economy grows 2.9% a year and would need 30% |
| 2, years to the line | no date | the economy shows no trend toward its line; the AI-research share could cross within a year; the pace is not currently speeding up |
| 3, count past halfway (recommended) | 1 of 4 | parts of the test past halfway, none at its line; pace 43%, forecasts unmeasured, AI doing the research 52%, economy 0% |

## 8. If adopted

1. `scripts/site.py`: the landing answer line becomes the count and the shares, the verdict
   beneath; `status.json` gains `headline`, `headline_label` and `parts_past_half`.
2. Definition section 4: a dated note saying how P(t) and the count are published.
3. The parent site's `fetch-projects.mjs` reads the two headline fields from the status file.
4. README: the "Live page" line says what the headline is.
5. A worklog decision entry naming the ruling and, if decision 5 goes the other way, an
   amendment entry.
