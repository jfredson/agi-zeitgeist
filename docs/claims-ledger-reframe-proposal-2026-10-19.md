# What the claims ledger is for: a reframe for John's ruling

**Status: a draft written on 2026-10-19 by the session that manages this tracker, for John to
rule on. Nothing on the live site has changed. The method's changes, and amendment A31, are on
the same branch and are marked as proposed. The page itself will only be rebuilt once John
rules.**

## John's ruling

Given on 2026-10-19 and relayed by the master session, in his words:

> "I don't think we hit the mark yet with what this ledger is for. The goal is not to score
> people on their success at predicting the future, the goal is to track the zeitgeist of what
> these people are saying to get a feel for what the vanguard of the industry is predicting at
> any given time."

## The change in one paragraph

The ledger stops being a scorecard and becomes a dated record of what the people leading the
industry say the future holds. The page leads with what they are predicting now. Next it shows
how that has moved over time. Every claim is still there in their own words, with its source.
Whether a claim's date has passed, and what happened, stays as a quiet note on that claim. It is
never totalled into a headline, and no one gets a hit rate. The checking already done is not
wasted: it is what makes each claim trustworthy as a record of what was said.

## 1. The purpose, as the method and the page would state it

Draft text for the top of the method (`docs/claims-ledger-method.md`, "What this ledger is
for") and the opening of the claims page:

> **What the industry's leaders predict.** This is a dated record of what the people who lead
> the companies building frontier AI say the future holds: when they expect AI to match or pass
> people, and what they expect it to do along the way. Each prediction is in their own words,
> with the date, the occasion and a link to the source. The page is read for what they are
> predicting now and how that has shifted. It is not a scorecard. Where a prediction's date has
> passed, a note says what happened, so a reader can see each forecast in the light of events.
> No one is given a score.

## 2. The page, from top to bottom

**First, what they say now.** For each person, their most recent dated forecast of AGI,
superintelligence or AI that is better than people at most things, drawn as a range or a year
on one shared timeline. Each forecast keeps the person's own term, because each of them means
something different by it. Beside it, a short line: their most recent dated prediction of any
kind, so the four who have never named a year for AGI (Jensen Huang, Arthur Mensch, Mark
Zuckerberg and Satya Nadella) still have a current view on the page. Below is a first picture,
drawn from the claims already recorded:

![What they say now (draft)](claims-ledger-reframe-2026-10-19/now-draft.png)

Its title is computed, as the frontier-voices chart's is, so it stays true as claims are added:
on today's record, eight of the eleven who name a year put it by 2031. Two cautions are drawn
from the record. Sam Altman's latest forecast (end of 2026, of an internal system he would call
AGI) comes from news reports, not his own words, and the page would mark it so. Liang Wenfeng's
latest is from July 2024, and the page would show its age.

**Second, how it has moved.** The same forecasts placed by the day they were said and the year
they named, one small panel per person, so a reader can see who has moved their date nearer, who
has held it and who has pushed it back. Under it, a link to the frontier-voices chart on the
home page, which draws the whole panel's dated guesses the same way. The two stay separate
charts: the frontier-voices chart is the opinion record, which the three people on the
ledger-only list never enter (amendment A30).

![How it has moved (draft)](claims-ledger-reframe-2026-10-19/moved-draft.png)

Both pictures are drafts. Their claims were picked by keyword for this proposal
(`claims-ledger-reframe-2026-10-19/tag_draft.py` and `draw_draft.py`); the built page would use
a field entered by hand on each claim (section 3).

**Third, every claim, by person, in date order.** As now: the words, the date, the occasion, the
source, and the test. The verdict becomes a quiet note at the end of each claim, in grey. For
example: "Its date passed on 2020-12-31. There were not a million robotaxis on the road." Or:
"Its date has not come." Or: "It names nothing an outsider could check." The coloured status
chips go, and so does the table of counts per person.

**What leaves the top of the page and the home page.** No totals of came true or did not, in
any headline or summary. The home-page sentence ("Of the 325 predictions ... 36 came true")
becomes a sentence about the present, also computed. On today's record it would read: "The
industry's leaders who name a year for AGI mostly put it between 2026 and 2031; see what each of
them says now."

## 3. What the record needs

One new field on each timing claim, entered by hand: **what arrives** (AGI, superintelligence,
AI better than people at most things, or something else, in the person's own term). Two more
facts are already in the record: whether the forecast is a year, a range (`due_early` to `due`),
or a forecast that it will not come before a date. The draft pictures guessed the first field
from keywords. About 84 timing claims need it entered. The validator would check that every
timing claim has it.

The year-by-year searches the method already plans stay. Their purpose changes: they make the
"now" view complete, so a person's latest forecast is really their latest. They start from each
person's most recent year and work back, not from the first year forward.

## 4. What stays and what goes

| | Proposed |
|---|---|
| Each claim, in their words, with source and test | Stays |
| Admission rule (figureheads, a date, a primary source, only claims about AI) | Stays |
| Status on each claim (came true, did not, not yet due, cannot be tested, took it back) | Stays in the data and as a quiet note on the page; no chips, no totals |
| Per-person table of counts | Goes from the page; the counts stay in the downloadable table for anyone who wants them |
| Per-person hit rate, its floor of five, the "seed only: not a rate" label | Goes (option 1 below) |
| The "claims traced" search-log row | Stays, as the record that a person's search is complete, no longer as the key to a rate |
| The `claims` block in `site/status.json` | Keeps its counts for data users, and gains a `now` block (each person's latest forecast) |
| The home-page sentence | Rewritten about the present |
| The news post of 2026-10-19 | Reframed once John rules; the story rewrite in pull request 26 is on hold |

## 5. Choices for John

**1. Hit rates: drop them, or keep a quiet one?**
- **Recommended: drop them.** Your ruling says the goal is not scoring. A rate, however
  guarded, is a score, and readers would quote it as one. The verdict on each claim already lets
  a reader see what happened.
- **The alternative:** keep a per-person line, low on the page, once that person's search is
  complete ("of the 21 forecasts whose date has passed, 9 came true"), as context, not a
  headline. The case for it is your question of 2026-10-17, whether each of them is "a
  front-row seat or a salesman". The record can partly answer it, but only if counts are shown
  somewhere.

**2. What leads the page: AGI forecasts, or the latest of everything?**
- **Recommended: AGI forecasts lead**, with each person's latest prediction of any kind on a
  line beside them. The question this site exists to ask is when the singularity comes, and the
  AGI dates are what moves.
- **The alternative:** lead with each person's latest dated prediction of any kind (products,
  robots, jobs, medicine), with the AGI dates second. This is broader, but less comparable from
  person to person.

**3. Undated predictions: keep them out, or let them in?** "AGI is close" carries the mood of
the moment but has no date.
- **Recommended: keep them out.** The ledger stays a record of dated predictions, so that
  every mark on its charts sits at a year someone named. The panel's undated talk is already in
  the coded statements and the home page's other charts.
- **The alternative:** admit undated predictions by the fifteen as their own kind of row, shown
  in the "now" section as words only, never on a chart.

## 6. What happens next

Once John rules, the work is: amendment A31 as ruled; the method as ruled (the draft is on this
branch); the new field entered on every timing claim, checked by a second reader; the page
rebuilt; the home-page sentence rewritten; and the news post reframed by the session that
drafted the story version, then put to John before it goes up. The share task stays on hold
until then.
