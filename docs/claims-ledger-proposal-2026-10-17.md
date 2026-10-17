# Proposal: a dated-claims ledger per person, scored against delivery

*Written 2026-10-17 by the agent at John's request, relayed through the master session the same
day. Nothing is built and no record changes with this document: the panel, the statements, the
scored series, the thresholds, the definition and the verdict all stay as they are, and the
seed list in section 8 is a list in this file, not rows in `data/`. The numbered decisions in
section 9 each carry a confidence and the strongest alternative, as the ground rule of
2026-09-08 requires; the rulings John must make are in section 10. If adopted, section 9's
decision 12 says what gets numbered as an amendment.*

## 0. One correction before anything else

The brief this was written from says Jensen Huang is not on the frozen panel and that adding
him would take an amendment. The record says otherwise. `data/speakers.csv` carries him as a
member of the 2020s cohort ("Frozen 2026-10-06 (A18)"), and amendment A18 (the panel freeze)
lists him among the cohort's twelve, six of whom "pass thin", Huang first among them: both of
his statements on the panel are secondhand. So **no amendment is needed to give Huang claims**;
all four leaders John named (Musk and Altman in the core panel, Amodei and Huang in the
cohort) are already on it. Section 7 still sets his claims in a table of their own, because
John asked for it and because his panel row is the thinnest, but the reason is thin sourcing,
not panel membership. Huang is not tagged `frontier_lab` (the panel's note calls him a near
miss: he sells the chips, not the models), which matters for one decision in section 9.

## 1. What the ledger is for

John's question, 2026-10-17: the people who run the frontier AI companies both sell the story
and see further than anyone else, so is each of them a front-row seat or a salesman? His
ruling that day was that a dated-claims ledger per person, scored against delivery, be
proposed for his ruling, on the pattern of the sibling trackers' claims logs. The master
session's gloss: a hit rate per person, in public, as the honest answer.

The ledger answers one narrow question and says so. **For each named leader, of the
predictions they made that have since come due, how many came true, how many did not, and
which way the misses went (too soon or too late).** That is a score of their forecasting,
published with every claim in their words, the source, and the evidence for the verdict. It
does not say whether they are right about the future, whether they are sincere, or whether
the technology is good or bad. A leader with a poor record may still be right next time; a
leader with a good record may have been lucky. The page says that in so many words.

Why it belongs in this project and not another: the tracker already records what these people
said (`data/statements.csv`) and already scores forecasts against outcomes in one place (the
leg B ledger, which scores the 2016 researcher survey's 32 milestones). What it lacks is the
joint: a named person's own dated words, set against what happened, one claim at a time. The
family's tracker pattern (rule 6.4, talk and delivery side by side) says that is where a
tracker earns trust.

## 2. The record layout

### One file per claim

Proposed: **`data/claims/<date>-<speaker>-<slug>.toml`, one file per claim**, the layout of
The Upgrade Tree's claims folder, with the verdict fields The Outrunning Ageing's records
use. Python 3.11 and later read TOML in the standard library (`tomllib`), so
`scripts/validate.py` stays standard-library-only, as its first lines promise.

Why not the CSV this record otherwise uses: a claim carries three or four paragraphs of
prose (how the words were checked, why the verdict is what it is, what the speaker did not
say), which a spreadsheet cell holds badly and a reviewer cannot read in a diff; and two
sessions adding claims then never edit the same file. The cost is one more file kind beside
the CSVs. To keep the project's habit that every record can be downloaded as a table, the site
build writes a flat `site/data/claims.csv` from the files, as it does for the other tables.

### Fields

| field | required | meaning |
|---|---|---|
| `id` | yes | The file name without `.toml`: date, speaker id, a short slug. Never renamed. |
| `speaker_id` | yes | A `speaker_id` that exists in `data/speakers.csv`. A claim by anyone not in that file is refused (the panel is frozen; section 5). |
| `when` | yes | When it was said: `YYYY-MM-DD`, or `YYYY-MM` or `YYYY` where the record settles nothing finer. |
| `when_note` | if not a full date | How the date was settled (a post's timestamp, a page's date line, an event's date). |
| `occasion` | yes | Where: a post, an essay, a keynote, a named interview, a hearing, a filing. |
| `source_kind` | yes | `own_words` (the person's post, essay, filing or paper), `transcript` (an official or checked transcript or recording), `printed_qa` (a question-and-answer interview printed as their own words; the siblings' ruling of 2026-10-17), or `coverage_only` (a report of what they said). |
| `source_url`, `source_locator` | yes | The one address to open, and where in it (a timestamp, a section, a paragraph). |
| `checked_how` | yes | How the words were checked and on what date: read on the page, listened to, an official transcript, two automatic transcripts that agree (the siblings' rule of 2026-10-17 for quoted recordings, if John extends it here). |
| `quote` | unless `coverage_only` | The words, verbatim, at most 25 words. Forbidden on a `coverage_only` entry, which carries `reported_as` instead: what was reported, with the reporter named. |
| `statement_id` | no | The `statement_id` of the row in `data/statements.csv` this claim was seeded from, if there is one. The validator checks the speaker and the date match. |
| `prediction` | yes | What it commits to, in plain words, hedges and conditions kept ("probably", "may", "if"). |
| `kind` | yes | `capability` (a thing AI will be able to do), `timing` (a named stage arrives, such as AGI or superintelligence), or `deployment` (a product ships or a number is reached). |
| `bar` | yes | The test that will settle it, written before the due date and never changed afterwards except by a dated note: the speaker's own definition if the same source gives one; otherwise the plainest reading of the words. A claim with no bar is `unfalsifiable` (section 3). |
| `due` | yes | The year the claim can be judged by, from the speaker's own words, and `due_basis`: the words or the sum that gave the year (section 3 gives the rule). |
| `is_goal` | no | `true` where the words are a stated goal, not a forecast ("we have set internal goals of ...; we may totally fail"); the page marks it (decision 11). |
| `has_probability` | no | `true` where the speaker gave a number ("a 50% chance"); such a claim is kept and flagged but is not in the plain count (section 3). |
| `restates` | no | The `id` of an earlier claim by the same person that this repeats with a changed date or condition (section 3). |
| `repeated_on` | no | Dates of unchanged repeats of this same claim. |
| `status` | yes | One of five words (section 3). |
| `verdict_on`, `verdict_why`, `verdict_source` | once settled | The date it was settled, the reason in plain words, and the dated primary source for what happened (the maker's release, a regulator's notice, an official benchmark or competition result). |
| `evidence_by` | once settled | `outside` (someone other than the speaker's own company measured it) or `maker` (the only evidence is the speaker's company saying so). The page marks `maker`. |
| `notes`, `verify` | no | Anything else; and plain claims in the entry written from memory and not yet checked, as on the siblings' records (a later session clears each). |

### Worked example

`data/claims/2025-10-29-altman-automated-research-intern.toml`, as it would be written from
the seed list (the words and dates were read at the source on 2026-10-17; the verdict is the one
the seed pass proposes, and John can overrule it):

```toml
[claim]
id = "2025-10-29-altman-automated-research-intern"
speaker_id = "altman"
when = "2025-10-29"
when_note = "The post's timestamp is 17:19 UTC on 2025-10-29; it says the livestream was 'Yesterday'."
occasion = "Post on X summarising OpenAI's livestream of 2025-10-28"
source_kind = "own_words"
source_url = "https://x.com/sama/status/1983584366547829073"
source_locator = "the first paragraph after 'TL;DR:'"
checked_how = "Read through a mirror of the post's text on 2026-10-17; x.com itself was not opened."
quote = "We have set internal goals of having an automated AI research intern by September of 2026"
statement_id = "altman-2025-09"
prediction = "OpenAI's own goal: by September 2026, an automated AI research intern running on hundreds of thousands of GPUs. He adds 'We may totally fail at this goal'."
kind = "capability"
is_goal = true
bar = "OpenAI's own definition, from its post of 2026-09-06: a system that can carry out well-defined research tasks under human direction, including tasks that would take a skilled researcher a few days; and running on hundreds of thousands of GPUs, from the original words."
due = 2026
due_basis = "His words: 'by September of 2026'."
status = "hit"
verdict_on = 2026-09-06
verdict_why = "OpenAI's post says 'according to our measurements, we have now reached the goal'. The post as read does not say whether it ran on hundreds of thousands of GPUs, so one condition of the bar is unchecked; recorded as hit on the company's word, to be reopened if an outside check finds otherwise."
verdict_source = "https://openai.com/index/research-acceleration-view-inside-openai/"
evidence_by = "maker"
notes = "A goal, not a forecast, in his own words; the page marks goals as goals. The 2028 follow-on goal (an automated AI researcher by March 2028) is its own record."
```

Two things the example shows. A hit can rest on the maker's word, and the page then says so in
a chip beside the verdict, so a reader can weigh it. And a bar can have a condition nobody has
checked; the entry names it instead of hiding it.

## 3. The scoring rules

### Which claims get in (the admission rule)

A claim is admitted if all four are true, and the test never looks at whether it came true:

1. **The speaker is on the frozen panel** (`data/speakers.csv`).
2. **The words look forward**: they say AI will do, reach or ship something.
3. **The words carry a date or a length of time**: a year ("by 2030"), a span counted from the
   day it was said ("in five years", "the next ten years", "this president's term"), or a stage
   with its own end date ("by the end of this decade").
4. **There is a primary source** (own words, a transcript, or a printed question and answer).
   A claim found only in coverage may be entered as `coverage_only`, shown and marked, with no
   quote, as the siblings do.

Anything else stays what it is today, a coded statement in `data/statements.csv`: "AGI is
coming", "still many years away", "we are close". This is the record's answer to the
undated-claim question (decision 4 below, and ruling 2 in section 10): **an undated claim is not
a claim record.** The page says how many dated and how many undated forward-looking statements
each person has, so vagueness stays visible without being scored.

### The five status words

| word | meaning |
|---|---|
| `not_yet_due` | The due year has not ended (31 December of it, unless the words name an earlier date). Shown, not scored. |
| `hit` | By the due date, every condition in `bar` was met, shown by a dated primary source. |
| `missed` | The due date has passed and the bar was not met, or only part of it was. The record says which condition failed. A near miss is a miss with the gap named in `verdict_why`; there is no "partly" (decision 5). |
| `withdrawn` | The speaker later said the claim no longer holds, or replaced it. **Counted as missed in every total** (the siblings' ruling of 2026-10-17: a result claim its maker later withdrew keeps the verdict `missed`). The word is kept apart only so the page can show that they took it back, and when. |
| `unfalsifiable` | The claim has a date but no bar an outsider could test, or its only judge is the speaker (for example "we will have an internal system I would call AGI"). Shown and counted apart, left out of the rate, and a bar is never supplied after the fact. This is the rule John made for the leg B ledger on 2026-10-12: its four "no bar" rows stay out of the scores. |

### What counts as a hit, by kind

- **Capability** ("AI will be able to do X by Y"). A hit needs a dated public demonstration that
  meets every stated condition, from the paper, the maker's release, a benchmark's official
  result or a competition result. This is the leg B ledger's standard for "arrived", and a
  demonstration only shows the thing was possible by then, so a hit is "no later than". Where
  the only evidence is the maker saying so, the claim can still be settled, but `evidence_by`
  is `maker` and the page marks it. Where the claim's own test is a milestone the leg B ledger
  already judged, the claim's verdict follows that row; the same fact is never judged twice.
- **Timing** ("AGI by 2027", "superintelligence in a few thousand days"). The bar is the
  definition the speaker gives in the same source. With none, the claim is `unfalsifiable`
  unless the plainest reading supplies a bar before the due date; the ledger does not borrow
  the singularity test's thresholds for this, because that would let the ledger move the test
  (section 5).
- **Deployment** ("agents will join the workforce in 2025", "1 billion users by Y", "a robotaxi
  service by Y"). A hit is the maker's own release, a regulator's notice, or an independent
  count showing it shipped to the stated scale by the due date. A stated number must be met,
  not nearly met. A maker's own figure is evidence for a figure only the maker holds, and is
  marked.

### The due year

- A named year is judged at the end of it.
- A span ("in five years", said 2024-03-18) runs from the day it was said, to that date five
  years on, and is judged at the end of that year. A range of spans ("four or five years")
  takes the later end, the generous one, and says so.
- "By the end of this decade" is 31 December 2029 or 2030, whichever the speaker's own usage
  implies; where it does not, the later, and the entry says so.
- Where the claim itself is a range of years ("2027 to 2034"), the due year is the later end, and
  the earlier end is recorded, so the page can show that the claim was already late against its
  early end.
- A point year with a spread beside it ("roughly human level AGI in the year 2025", with a
  stated 90% range to 2036) is scored at the point year, and the spread is a second claim with
  its own due year. Otherwise a speaker could always say the range was the claim.
- A **goal** ("we have set internal goals of ... by September 2026; we may totally fail") is
  a dated public commitment with the hedge in the speaker's words. It is admitted, marked
  `is_goal`, and scored like any other claim; the page shows the mark. Decision 11.

### Numbers given as chances

A claim that states a probability ("a 50% chance by 2035") cannot be scored by one outcome. It is entered, flagged `has_probability`, given its verdict like any other, and kept
**out of the plain count**; it is listed for a later calibration check once a person has enough of them. Hedge words
("probably", "I'd be very surprised if not") are not probabilities: those claims are scored at
face value with the hedge written in `prediction`.

### Restatements

A leader who says the same thing again has not made a new prediction, and one who changes the
date has.

- **Unchanged repeat** (same prediction, same due year): one claim, keyed to the first date,
  with the later dates in `repeated_on`. Counting each repeat would let a repeated hit or miss
  inflate a record.
- **Changed repeat** (new due year or changed condition): a **new claim record** with `restates`
  naming the earlier one, as The Outrunning Ageing does for Kurzweil's 2032 restatement of his
  earlier date. The earlier record is never edited; its verdict is given on its own due date
  whatever was said later. The page groups a chain and shows the due years in order, so
  a date that keeps sliding is visible as a slide.

### The rate, and what stops it being gamed

- **Per person only, never pooled.** For each leader: hits, missed (including withdrawn),
  not yet due, unfalsifiable, with the number of due claims always printed beside the rate.
  The rate is hits over hits plus missed. The sibling pattern pools nothing, and a pooled
  "leaders' hit rate" would make three people answer for a fourth.
- **Which way the misses went.** For each missed claim, whether the thing came later than said,
  or has not come, against the few that came sooner. The leg B ledger reports direction for
  the same reason, and for these speakers it is the half of the question the rate alone hides.
- **A floor.** A person with fewer than five due claims shows "too few to rate" and the
  counts, not a percentage. Decision 7.
- **A collection pass before any rate.** The seed list below is the famous, checkable claims
  found for this proposal, not a complete record, and a rate computed from it would measure
  which claims were easy to find. Proposed: no percentage is published for anyone until a person has been
  traced year by year, as the panel's collection does, with the searches logged in
  `data/search_log.csv` and quiet years entered as rows. Until then the page shows the seed
  claims and counts under the plain label "seed only: not a rate".
- **Both directions of selection are logged.** The searches that found each claim, and the
  claims looked for and not found, are written down, as `docs/panel-verification-2026-10.md`
  does for the panel.

## 4. How it relates to the leg B ledger and the coded statements

**The leg B ledger** (`data/leg_b_ledger.csv`, method in `docs/leg-b-ledger-method.md`, first
reading in `docs/leg-b-ledger-2026-10.md`) scores the 2016 researcher survey's 32 milestone
forecasts: the combined forecast of the 352 researchers who answered (each milestone's even-chance year) against the date each
milestone was first publicly demonstrated. The claims ledger is the same operation on a named
person's own forecast. They share three things on purpose: the evidence standard (a dated public
demonstration from the paper, the maker's release or a competition's result, and "no later than"
because a demonstration can only follow feasibility), the verdicts' meaning (arrived and not
arrived become hit and missed; the "no bar" rows become `unfalsifiable`, with the same ruling
that a bar is never set after the answer is known), and the report of which way misses went.
They differ in two things. The ledger scores a crowd's median at one fixed date (28 June 2016);
the claims ledger scores individuals on many dates. And the ledger's rows are fixed once; claims keep
arriving. Neither feeds the other's numbers: the claims ledger never changes a leg B row, and it
never becomes input to leg B's gauge (section 5). Where a claim's test is a milestone the leg B
ledger already judged, the claim's verdict cites that row.

**The coded statements** (`data/statements.csv`, 159 rows) are the seed and the sibling in
the record. Of the 159, 43 carry a year in the timeline fields (`point_year`, `range` or
probability by year): Kurzweil 18, Altman 9, Hinton 6, LeCun 5, Marcus 5. Nobody else on the
panel has a coded row yet; Musk, Amodei, Huang, Hassabis and the rest of the panel have a speaker row and no
statement rows, which is why the seed list in section 8 draws on primary sources opened for this
proposal and not only on existing rows. Four rules keep the two records from tangling:

1. **A statement row is not a claim record.** A row says what was said and codes it. A claim
   record adds a bar, a due year and a verdict. A claim points at its row with `statement_id`
   and the validator checks that the speaker and the date match and that the claim's quote lies inside the row's quote (or says
   in `notes` why the span differs).
2. **Nothing is stored in two places.** The statement row is not edited when a claim is
   entered, and a claim's verdict is never copied back to the row.
3. **One source can seed several claims.** A coded row carries one timeline; a source such as
   Altman's "Reflections" post says more than one dated thing. Each dated thing is its own claim
   record pointing at the same row.
4. **Not every dated row becomes a claim.** The seed rule is: every row with a year in its
   timeline fields whose speaker is on the panel and whose elicitation is not `quoted`,
   each opened at its source and put through the admission rule. The 15 `quoted` rows among the 43 (a reporter's
   words around a remark) can enter only as `coverage_only`, until the primary source is found.
   Many of the 43 will fail the bar test (they say a stage arrives by a year but not what would
   count as arrival); those become `unfalsifiable`, which is the honest outcome for them.

## 5. What it must never touch

The ledger is a separate record kind beside the others, and the rule is the tracker pattern's
first claims rule (6.1): talk and delivery are never mixed. So, in writing:

- **The frozen panel** (`data/speakers.csv`, frozen by amendment A18, the panel freeze). A claim by someone not in it is
  refused by the validator. Adding anyone to the ledger's reach is an amendment to the panel
  first, as the README already says for any new person.
- **The coded statements.** No row is edited, added or deleted because of a claim.
- **The scored series**: `data/world_measures.csv`, `data/aggregates.csv`, the leg B ledger's
  rows, and everything `scripts/site.py` scores from. A claim's verdict is never a measure of
  the world.
- **The frozen thresholds** (`docs/singularity-entry-thresholds.json`) and **the definition**
  (`docs/singularity-entry-definition.md`), including leg B's gauge, which stays defined on
  forecasts of METR's task-length measure and cannot be filled by anyone's claims.
- **The verdict** ("Not yet.") and the headline of 2026-10-17 (amendment A25, the average share of the way). The headline's
  number is the average share of the way across the measured parts; nothing in the claims ledger
  enters it, and `status.json`'s headline fields do not change. The ledger may add its own
  fields to `status.json` (decision 9) but never a field the parent site could mistake for the
  headline.
- **The weekly reading's rule** (`docs/weekly-reading.md`): the reading may append rows and
  flag, never change what is scored. If John extends it to claims, it could flag a claim that
  has come due, and the verdict would still be entered by hand and dated.

## 6. Where it shows

Two choices.

**A page of its own, `/claims/`, with one line on the home page** (recommended). The home page
is already one long scroll with five jobs; a table of a few dozen claims, with a block of quote,
source and verdict under each, would bury the test. The page opens with the per-person table
(counts, the rate or "seed only", which way the misses went), then a list of claims by person in
date order, each showing the person's words, the date, the due year, the status word as a chip
in the family's yes/no colours, and the evidence. The home page's "current zeitgeist" section
gets one sentence and a link beside the experts' dates: "Of the predictions with a date that
the heads of the AI companies have made, N are now due, and M came true." Per rule 6.4 of
the tracker pattern (talk and delivery side by side), the claims page repeats the four gauges'
shares in a one-row strip at the top, drawn from the same figures, so the talk is seen against
the delivery; the strip is display only and has no link to any claim. The top bar gains a
"Claims" handle in the heavier tier (rule 4.7: short handles; the siblings that have a
claims page all call it "Claims"), which makes the bar four heavy handles and three light.

**The alternative is a section on the home page.** The pattern's own reasoning for one page
("the claims log as a page of its own with no delivery beside it would read as a collection of
quotations rather than as a test of them") argues for it. The cost is length: the home page
would carry a long table above the method section, and both siblings that keep claims
(The Upgrade Tree and The Outrunning Ageing) give them a page of their own. A middle way is built into the
recommendation: the page repeats the gauges strip.

**If built**, `scripts/site.py` reads `data/claims/*.toml`, writes `site/claims/index.html`
and `site/data/claims.csv`, adds `claims` counts to `status.json` (decision 9), and
`scripts/validate.py` gains a claims check. None of this is in this proposal's change.

## 7. Jensen Huang

**He is on the frozen panel already** (section 0): the 2020s cohort, by amendment A18 (the panel
freeze), and `data/speakers.csv` says so. The tracker's open question in TimeAssembler (the one
that asks whether to add him by amendment) rests on a premise the record does not support, and
should be closed or reworded. What adding him would have taken, had he been absent: an
amendment entry in `docs/amendments.md` giving the reason, his evidence against the cohort rule
(a timeline statement dated 2024 or later, none dated before 2018) and the panel counts after
the change, as the panel freeze (A18) did for the other eleven. None of that is needed.

What is true of his row is that it is thin, and the seed pass changes one fact about it. The row
says both of his statements on the panel are secondhand. Both were opened at the source for this
proposal: the "fairly competitive with humans in five years" remark is from the New York Times
DealBook event on 2023-11-29, and "I think we've achieved AGI" is from Lex Fridman's podcast of
2026-03-23, in answer to when an AI could run a company worth a billion dollars. He said it again
on Nvidia's earnings call of 2026-08-26 ("in a lot of ways, and for many tasks, we could say that
we've already achieved AGI"). The row's "latest 2026-03" is therefore out of date by five months;
I have not changed it (nothing in `data/` changes with this proposal), and it is a small fix for
the collection pass.

Why a table of his own, as John asked: his claims are a different kind. Most are about what
Nvidia will ship or sell (a chip platform in the second half of 2026, orders worth a trillion
dollars through 2027), which Nvidia's own results can settle, and the claims about AGI itself are
the loose kind (the "achieved AGI" remarks have no test). He is the clearest case of the
"salesman" half of John's question, since his company profits from the story whichever way the
models turn out. He is not tagged `frontier_lab` (the panel's note: chips, not models), so
decision 10 in section 9 asks whether a ledger of "frontier leaders" includes him. Ten claims:

10 claims: 2 hit, 1 missed, 5 not yet due, 2 unfalsifiable, 0 withdrawn. Seed only: not a rate.

| said | in their words | due | today | why |
|---|---|---|---|---|
| 2023-11-29 | "deliver results that are fairly fairly competitive to a Normal human, I would I would say that within the next five years." ([transcript](https://www.youtube.com/watch?v=Pkj-BLHs6dE)) | 2028 | **not yet due** | The window ends around November 2028. Note that on 2026-03-23 he said AGI had already been achieved, on a different definition (see the Lex Fridman row). |
| 2024-03-01 | "I'm guessing in 5 years time we'll do well on every single one of them" ([transcript](https://www.youtube.com/watch?v=cEg8cOx7UZk)) | 2029 | **not yet due** | Restates an earlier claim. The window ends around March 2029. |
| 2025-03-18 | "Vera ruin mvlink 144 is the second half of next year" ([transcript](https://www.youtube.com/watch?v=_waPvOwL9Z8)) | 2026 | **hit** | The evidence is nvidia's own results release. Nvidia's own results release of 2026-08-26 says the Vera Rubin platform is "ramping into full production" with racks running at CoreWeave, Google Cloud, Microsoft Azure, Oracle Cloud Infrastructure and Nebius. |
| 2025-03-18 | "100% of Nvidia software Engineers will be AI assisted by the end of this year" ([transcript](https://www.youtube.com/watch?v=_waPvOwL9Z8)) | 2025 | **hit** | The evidence is nvidia's own word only; "ai assisted" is a loose bar. The only evidence is Nvidia's own statement. In the Computex keynote on 2025-05-19 he said "A 100% of NVIDIA software engineers now have digital agents working with them", two months later. No outside check exists. |
| 2025-03-18 | "by the end of this decade the world is going to be at least 50 million workers short" ([transcript](https://www.youtube.com/watch?v=_waPvOwL9Z8)) | 2030 | **not yet due** | The deadline is about 2030. |
| 2025-05-19 | "this year we're deploying Mercedes around the world our self-driving car stack end to end stack." ([transcript](https://www.youtube.com/watch?v=TLzna9__DnI)) | 2025 | **missed** | Contested: loose wording ("deploying", "around the world"). Judgement call, flagged for John: the wording is loose ("deploying", "around the world"). |
| 2025-10-28 | "visibility into half a trillion dollars of cumulative Blackwell and early ramps of Rubin through 2026." ([transcript](https://www.youtube.com/watch?v=lQHK61IDFH4)) | 2026 | **not yet due** | Calendar 2026 is not over. On 2026-03-16 he said he now sees at least $1 trillion through 2027 (next row). Checking either figure needs Nvidia's own filings. |
| 2026-03-16 | "I see through 2027. At least $1 trillion." ([transcript](https://www.youtube.com/watch?v=jw_o0xr8MWU)) | 2027 | **not yet due** | Restates an earlier claim. 2027 has not been reached. |
| 2026-03-23 | "I think it’s now. I think we’ve achieved AGI." ([transcript](https://lexfridman.com/jensen-huang-transcript)) | 2026 | **unfalsifiable** | It rests on the interviewer's loose definition, which Huang read as allowing a short-lived success. |
| 2026-08-26 | "in a lot of ways, and for many tasks, we could say that we've already achieved AGI." ([transcript](https://www.webull.com/news/15497781742806016)) | 2026 | **unfalsifiable** | Restates an earlier claim. "For many tasks, we could say" has no test and no stated threshold; he then says the milestones do not matter. |

Reading it: three of the ten are due; two came true on Nvidia's own word and one (the Mercedes
claim) is contested. Five are not yet due. Two are `unfalsifiable`, both the "we have achieved
AGI" remarks: the speaker is the only judge. That is the record's ordinary rule, not a finding
against him; the page shows the two as a separate count.

## 8. The seed list

**What it is.** 79 dated claims by 11 people (Musk 14, Altman 16, Amodei 12, Huang 10, and 27
from Legg, Hassabis, Suleyman, Sutskever, Hinton, LeCun and Kai-Fu Lee, the other panel members
tied to the frontier labs who gave a dated, falsifiable claim). 17 point at an existing row of
`data/statements.csv` (eleven Altman, three Hinton, three LeCun); the rest come from primary sources opened for this proposal, because the
panel has no coded rows yet for Musk, Amodei, Huang, Hassabis, Legg, Suleyman or Sutskever. Each
claim in the full appendix (`docs/claims-ledger-seed-2026-10-17.md`) carries the source and
where in it, how the words were checked, the due year and how it was worked out, today's status
and the evidence, and any flag. The tables below are the compact view. Kurzweil is left out of
the seed on purpose: his 2029 date is the long chain the restatement rule is for (18 of the 43
statement rows carrying a year are his, seventeen of them pointing at 2029 and one at 2045) and is already in
the siblings' records for the escape-velocity date; it should be entered once, with its repeats
in `repeated_on`, when the ledger is built.

**Status today:** 45 not yet due, 16 missed, 10 hit, 8 unfalsifiable, none withdrawn. Only 26 of
the 79 are due at all.

**How to read the counts.** They are not rates, and the page would not show them as rates
(section 3, "a collection pass before any rate"). The seed was gathered by looking for the
famous, checkable claims, and for Musk that means self-driving and robot promises, which are the
ones most often quoted and most clearly late. Ten misses of fourteen for him says "the famous
claims", not "the record". The same is true in the other direction for people whose claims are
mostly hedged ranges (Hassabis, Sutskever, LeCun, Hinton: every claim is still ahead of them).
The honest summary of the seed is that the cases which can be scored so far are mostly the
deployment promises, and the AGI-timing claims have not come due.

**Who did the work and how far it is checked.** Four research passes opened the sources and
proposed each verdict; the quotes were cut from fetched pages or captions, not typed from memory.
I spot-checked: Altman's blog quotes against the live page, OpenAI's September 2026 announcement
of its research intern and Tesla's July 2026 call (both by search, which agreed). The quotes
taken from automatic YouTube captions have rough wording and the siblings' two-transcript check
has not been run on them. Every verdict here is the agent's and John can overrule any one. Where
a claim is contested the table says so in its last column.

**Sources that would not open** (the verdict does not depend on them unless said): Tesla's own
web pages, Axios, the World Economic Forum site, openai.com (read through a reader copy or the
Internet Archive), and, once, YouTube. Four claims are `coverage only` and carry no quote: Musk's
2020 "level 5 during 2020", Altman's reported "internal system he would call AGI by the end of
2026", Amodei's 2025 warning about entry-level white-collar jobs, and Kai-Fu Lee's 2017 "half of
jobs" remark.

**Findings about existing rows, none changed.** (1) `altman-2026-04` quotes TIME's paraphrase
as Altman's words; only "not quite yet" is his. (2) `altman-2023-06` (the governance post of
2023-05-22) has three authors. (3) The "Reflections" post is dated 2025-01-05 in Pacific time;
`altman-2025-03` has 2025-01-06, the UTC date. (4) `altman-2021-01` omits the explicit
five-year and ten-year points in the same passage. (5) The Huang row is out of date (section 7).
These are for the collection pass.

### The tables

The heads of the companies first, then the other panel members tied to the frontier labs. Huang's table is in section 7. "Today" is the verdict as of 2026-10-17, proposed from the sources named; John can overrule any one.

#### Elon Musk

14 claims: 2 hit, 10 missed, 2 not yet due, 0 unfalsifiable, 0 withdrawn. Seed only: not a rate.

| said | in their words | due | today | why |
|---|---|---|---|---|
| 2016-01-10 | "In ~2 years, summon should work anywhere connected by land & not blocked by borders, eg you're in LA and the car is in NY" ([own words](https://x.com/elonmusk/status/686279251293777920)) | 2018 | **missed** | Scored from a search excerpt of the owner's manual, not the page; open before use. Tesla's current owner's manual describes its successor feature, Actually Smart Summon, as working only within a few hundred feet of the owner's phone, not across the country. |
| 2019-04-22 | "next year for sure we will have over a million Robo taxis on the road" ([transcript](https://www.youtube.com/watch?v=Ucp0TTmvqOE)) | 2020 | **missed** | Tesla's own executives said on 2026-07-22 that the robotaxi program started about a year earlier, in Austin, with safety monitors in the passenger seats, and that it now runs across six cities in two states. |
| 2020-07-09 | (reported, no quote) As reported, he said he remained confident Tesla would have the basic functionality for 'level 5' autonomy (a car that drives itself anywhere, with no human needed) complete during 2020. ([coverage only](https://yicaiglobal.com/news/level-5-autonomous-driving-is-within-tesla-reach-elon-musk-tells-waic)) | 2020 | **missed** | On 2026-07-22 Tesla's executives described its driverless taxi service as running in six cities in two states, so driving anywhere with no human is not yet delivered. |
| 2021-08-19 | "we think we'll probably have a prototype sometime next year that basically looks like this" ([transcript](https://www.youtube.com/watch?v=j0z4FweCy4M)) | 2022 | **hit** | At Tesla AI Day on 2022-09-30 a Tesla robot walked on stage with no cranes or cables, and a second prototype, 'Bumble C', was shown. Musk called it 'humble beginnings'. |
| 2024-04-08 | "if you define AGI as smarter than the smartest human I think it's probably end of next year" ([transcript](https://www.youtube.com/watch?v=_rQBZ3vKRA0)) | 2025 | **missed** | Contested: no agreed test; he moved the date himself in 2026-01. No one has announced or shown AI smarter than the smartest human, and on 2026-01-22 Musk himself said it 'might' come by the end of 2026. |
| 2024-04-08 | "all humans working together uh who are also using computers to augment their output and that that I think is probably five years away" ([transcript](https://www.youtube.com/watch?v=_rQBZ3vKRA0)) | 2029 | **not yet due** | 2029 has not arrived. |
| 2024-07-01 | "Grok 2, which comes out in August, will be a giant improvement in this regard." ([own words](https://x.com/elonmusk/status/1807637096129241529)) | 2024 | **hit** | xAI's own announcement, dated 2024-08-13, releases an early preview of Grok-2 to X Premium and Premium+ subscribers. |
| 2024-07-01 | "Grok 3 end of year after training on 100k H100s should be really something special" ([own words](https://x.com/elonmusk/status/1807643760584708363)) | 2024 | **missed** | xAI's Grok 3 announcement page is dated 2025-02-19, after the end of 2024. |
| 2024-10-10 | "we do expect actually to to start uh fully autonomous unsupervised FSD uh in Texas and California next [Music] year" ([transcript](https://www.youtube.com/watch?v=6v6dbxPlsXs)) | 2025 | **missed** | Tesla's executives said on 2026-07-22 that safety monitors rode in the passenger seats when the Austin service began and that the first fully driverless rides came around the end of 2025. |
| 2025-01-29 | "initial launch of unsupervised no one in the car full self driving in Austin in June" ([transcript](https://www.youtube.com/watch?v=Gub5qCTutZo)) | 2025 | **missed** | On 2025-10-22 Tesla said it was still 'on track to remove the person from inside the car', and on 2026-07-22 its executives said the first fully driverless rides in Austin came around the end of 2025, after launching with safety … |
| 2025-01-29 | "will we succeed in making several thousand yes I think we will" ([transcript](https://www.youtube.com/watch?v=Gub5qCTutZo)) | 2025 | **missed** | Scored from his own later statements, not a unit count. On 2026-01-28 Musk said Optimus was 'still very much at the early stages', in an R&D phase, not in use in Tesla's factories 'in a material way', and that he did not expect significant production volume until probably the end of … |
| 2025-07-23 | "assuming we get regulatory approvals, it's probably addressing half the population of the US by the end of the year" ([transcript](https://www.youtube.com/watch?v=pLjG7a-NX7U)) | 2025 | **missed** | On 2026-07-22, a year later, Tesla's executives described unsupervised robotaxi service in six cities in two states, and on 2026-01-28 Musk reset the same goal ('between a quarter and half of the United States') to the end of … |
| 2025-10-22 | "we look forward to unveiling Optimus V3 um you know probably in Q1" ([transcript](https://www.youtube.com/watch?v=GQ9S7xbkGAY)) | 2026 | **missed** | On 2026-04-22, after the quarter ended, Musk said he wanted to 'push the Optimus 3 unveil maybe closer to production', which he put around late July or August. |
| 2026-01-22 | "we might have AI that is smarter than any human by the end of this year and I would say no later than next year" ([transcript](https://www.youtube.com/watch?v=IgifEgm1-e0)) | 2026 | **not yet due** | Restates an earlier claim. The year is not over (today is 2026-10-17), and he gave 2027 as the latest date. |

#### Sam Altman

16 claims: 5 hit, 1 missed, 8 not yet due, 2 unfalsifiable, 0 withdrawn. Seed only: not a rate.

| said | in their words | due | today | why |
|---|---|---|---|---|
| 2019-01-05 | "AGI will feel within reach to many people in the industry" ([own words](https://x.com/sama/status/1081584255510155264)) | 2025 | **unfalsifiable** | The claim is about how many people 'feel' AGI is close. There is no count or threshold in the post, so it cannot be scored true or false from the record. |
| 2021-03-16 | "In the next five years, computer programs that can think will read legal documents and give medical advice." ([own words](https://moores.samaltman.com/)) | 2026 | **hit** | Loose bar: the claim names no standard. Both activities exist at scale. OpenAI's technical report says GPT-4 passed a simulated bar exam with a score around the top 10% of test takers (arXiv 2303.08774, March 2023). |
| 2021-03-16 | "In the next decade, they will do assembly-line work and maybe even become companions." ([own words](https://moores.samaltman.com/)) | 2031 | **not yet due** | The ten years run to March 2031. Not scored. |
| 2023-05-22 | "it’s conceivable that within the next ten years, AI systems will exceed expert skill level in most domains" ([own words](https://web.archive.org/web/2023/https://openai.com/blog/governance-of-superintelligence)) | 2033 | **not yet due** | The ten years run to May 2033. Not scored. |
| 2024-03-18 | "I expect that by the end of this decade, and possibly somewhat sooner than that, we will have quite capable systems" ([transcript](https://lexfridman.com/sam-altman-2-transcript/)) | 2030 | **not yet due** | The decade has not ended. Not scored. |
| 2024-03-18 | "We will release an amazing new model this year." ([transcript](https://lexfridman.com/sam-altman-2-transcript/)) | 2024 | **hit** | OpenAI released o1-preview on 2024-09-12 and described it as a new series of reasoning models. 'Amazing' is a judgment word; the release itself is checkable. |
| 2024-09-23 | "It is possible that we will have superintelligence in a few thousand days (!); it may take longer, but I’m confident we’ll get there." ([own words](https://ia.samaltman.com/)) | 2034 | **not yet due** | Even the earliest reading (1,000 days) falls in June 2027. Not scored. |
| 2025-01-05 | "in 2025, we may see the first AI agents “join the workforce” and materially change the output of companies." ([own words](https://blog.samaltman.com/reflections)) | 2025 | **unfalsifiable** | Two parts. Agents doing paid work did ship in 2025, and he wrote in June 2025 that '2025 has seen the arrival of agents that can do real cognitive work' (his own assessment in The Gentle Singularity). |
| 2025-01-05 | "I think AGI will probably get developed during this president’s term, and getting that right seems really important." ([printed interview](https://brp-prod-bcc.bloomberg.com/features/2025-sam-altman-interview/)) | 2029 | **not yet due** | The term runs to January 2029. Not scored. |
| 2025-06-10 | "2026 will likely see the arrival of systems that can figure out novel insights." ([own words](https://blog.samaltman.com/the-gentle-singularity)) | 2026 | **hit** | On 2026-05-20 OpenAI announced that an internal model had disproved a long-standing conjecture on the planar unit distance problem (first posed by Erdős in 1946), and said the proof was checked by external mathematicians. |
| 2025-06-10 | "2027 may see the arrival of robots that can do tasks in the real world." ([own words](https://blog.samaltman.com/the-gentle-singularity)) | 2027 | **not yet due** | 2027 has not started. Not scored. |
| 2025-10-14 | "In December, as we roll out age-gating more fully ... we will allow even more, like erotica for verified adults." ([own words](https://x.com/sama/status/1978129344598827128)) | 2025 | **missed** | The verdict rests on press coverage; a primary source for the slip is still to be found. Coverage reports that the launch slipped from December to the first quarter of 2026 (Fidji Simo, OpenAI's head of applications, on 2025-12-11), was delayed again on 2026-03-06, and was paused indefinitely around 2026-03-26. |
| 2025-10-29 | "We have set internal goals of having an automated AI research intern by September of 2026 running on hundreds of thousands of GPUs" ([own words](https://x.com/sama/status/1983584366547829073)) | 2026 | **hit** | The evidence is openai's own word only. ONLY THE COMPANY'S OWN CLAIM. OpenAI's post of 2026-09-06 says: 'According to our measurements, we have now reached the goal, announced last fall, of having an automated research intern by September of this year.' It defines the … |
| 2025-10-29 | "a true automated AI researcher by March of 2028. We may totally fail at this goal" ([own words](https://x.com/sama/status/1983584366547829073)) | 2028 | **not yet due** | March 2028 has not arrived. OpenAI's 2026-09-06 post says 'We are making strong progress toward creating an automated AI researcher by March of 2028'; that is the company's own statement, not a result. |
| 2025-10-29 | "In 2026 we expect that our AI systems may be able to make small new discoveries; in 2028 we could be looking at big ones." ([own words](https://x.com/sama/status/1983584366547829073)) | 2026 | **hit** | Restates an earlier claim. Same evidence as the June 2025 claim: OpenAI's 2026-05-20 announcement that an internal model disproved the Erdős unit distance conjecture, checked by outside mathematicians. |
| 2026-08-26 | (reported, no quote) Per TIME's reporter: by the end of 2026 OpenAI would have an internal system that Altman would call AGI. At the time he said OpenAI was 'not quite yet' there. ([coverage only](https://time.com/article/2026/08/26/openai-sam-altman-interview/)) | 2026 | **not yet due** | The year has not ended. Not scored. Note that the test is that Altman himself would call it AGI, so the answer will rest on his word. |

#### Dario Amodei

12 claims: 1 hit, 2 missed, 7 not yet due, 2 unfalsifiable, 0 withdrawn. Seed only: not a rate.

| said | in their words | due | today | why |
|---|---|---|---|---|
| 2023-07-25 | "a straightforward extrapolation of today’s systems to those we expect to see in 2-3 years suggests a substantial risk" ([own words](https://www.judiciary.senate.gov/imo/media/doc/2023-07-26_-_testimony_-_amodei.pdf)) | 2026 | **unfalsifiable** | The claim is conditional ("if appropriate guardrails and mitigations are not put in place") and speaks of a "substantial risk", not of a certainty. Guardrails were put in place, so the case it describes never happened. |
| 2023-08-08 | "generally well educated human, that could be not very far away at all. I think that could happen in two or three years." ([transcript](https://www.dwarkesh.com/p/dario-amodei)) | 2026 | **unfalsifiable** | He gives no test. "Basically like a generally well educated human" after an hour of conversation is a judgement, and I found no study that used that test. It is also conditional on safety limits not slowing the industry. |
| 2024-10-11 | "I think it could come as early as 2026, though there are also ways it could take much longer." ([own words](https://darioamodei.com/essay/machines-of-loving-grace)) | 2026 | **not yet due** | 2026 is not over and the claim is hedged. His own essay of 2026-06-10 says that if the scaling trend "continues for only a year or two longer" we are "likely" to get Powerful AI, so he did not say it had arrived by June. |
| 2024-11-11 | "I would not be surprised at all if we hit ASL-3 next year." ([transcript](https://lexfridman.com/dario-amodei-transcript)) | 2025 | **hit** | The evidence is anthropic's own post, which says protections were switched on as a precaution. Anthropic's own post of 2025-05-22 says it activated the ASL-3 protections with the launch of Claude Opus 4. |
| 2025-01-29 | "and is most likely to happen in 2026-2027" ([own words](https://darioamodei.com/on-deepseek-and-export-controls)) | 2027 | **not yet due** | Restates an earlier claim. 2027 has not been reached. His 2026-06-10 essay still talks of "a year or two longer" for Powerful AI. |
| 2025-03-10 | "I think we’ll be there in three to six months—where AI is writing 90 percent of the code." ([transcript](https://www.cfr.org/event/ceo-speaker-series-dario-amodei-anthropic)) | 2025 | **missed** | Contested: whose code is unstated, and only company statements bear on it. Judgement call, flagged for John. Read as written (code in general), nothing shows 90 percent: I found no reliable measure for all code, and the best outside estimate (Redwood Research, 2025-10-22) put AI-written lines of code … |
| 2025-03-10 | "in twelve months, we may be in a world where AI is writing essentially all of the code." ([transcript](https://www.cfr.org/event/ceo-speaker-series-dario-amodei-anthropic)) | 2026 | **missed** | Contested: whose code is unstated, and only company statements bear on it. Judgement call, flagged for John. On 2026-02-13 he listed "100% of code is written by the model" as a further step on a spectrum and put full end-to-end software engineering "one or two years" out; |
| 2025-05-28 | (reported, no quote) AI could eliminate half of all entry-level white-collar jobs and push US unemployment to 10-20 percent within one to five years. ([coverage only](https://www.axios.com/2025/05/28/ai-jobs-white-collar-unemployment-anthropic)) | 2030 | **not yet due** | The window runs to 2030. For context only: the US unemployment rate was 4.2 percent in September 2026 (Bureau of Labor Statistics release of 2026-10-02), and an NPR report of 2026-08-18 gives the New York Fed rate for recent … |
| 2026-01-20 | "We might be six to twelve months away from when the model is doing most, maybe all, of what software engineers do end-to-end." ([transcript](https://aletteraday.substack.com/p/letters-314315-demis-hassabis-and)) | 2027 | **not yet due** | The window runs to January 2027. On 2026-02-13 he gave a longer span for end-to-end coding: "I think we'll be there in one or two years" (apart from irreducible uncertainty). |
| 2026-01-26 | "powerful AI could be as little as 1–2 years away, although it could also be considerably further out." ([own words](https://www.darioamodei.com/essay/the-adolescence-of-technology)) | 2028 | **not yet due** | Restates an earlier claim. 2028 has not been reached. His 2026-06-10 essay says: "If these scaling laws continue for only a year or two longer, we are likely to get what I've called Powerful AI". |
| 2026-02-13 | "It is hard for me to see that there won’t be trillions of dollars in revenue before 2030." ([transcript](https://www.dwarkesh.com/p/dario-amodei-2)) | 2029 | **not yet due** | The deadline is the end of 2029. The slower case he describes would put trillions at about 2030, so the claim is not clearly settled even then. |
| 2026-09-12 | "it’s my worry that in 6–12 months such a swarm could be capable of taking over the entire internet with a persistent botnet" ([own words](https://www.darioamodei.com/post/we-must-pace-the-frontier)) | 2027 | **not yet due** | The window runs to about September 2027. It is stated as a worry ("it's my worry that ... could"), not a flat forecast. |

#### Shane Legg

4 claims: 0 hit, 1 missed, 2 not yet due, 1 unfalsifiable, 0 withdrawn.

| said | in their words | due | today | why |
|---|---|---|---|---|
| 2009-12-07 | "my prediction for the last 10 years has been for roughly human level AGI in the year 2025" ([own words](https://www.vetta.org/2009/12/tick-tock-tick-tock-bing/)) | 2025 | **missed** | Contested: 2025 was his most likely year inside a stated range to 2036. On 2025-12-11 Legg said on Google DeepMind's own podcast that AI is not yet at his bar for AGI ('an artificial agent that can at least do the kinds of cognitive things people can typically do'): he says of today's systems … |
| 2011-12-31 | "I expect to see an impressive proto-AGI within the next 8 years." ([own words](https://www.vetta.org/2011/12/goodbye-2011/)) | 2019 | **unfalsifiable** | Restates an earlier claim. Legg himself says a list of specific capabilities 'would somewhat miss the point'. |
| 2023-10-26 | "I think there's a 50% chance that we have AGI by 2028." ([transcript](https://www.dwarkesh.com/p/shane-legg)) | 2028 | **not yet due** | Restates an earlier claim. 2028 has not arrived. He gave a probability of one in two, so even a miss would not by itself show the estimate was wrong. |
| 2025-12-11 | "Hannah Fry: are you still 50/50 by 2028? Shane Legg: Yes," ([transcript](https://www.youtube.com/watch?v=l3u_FAv33G0)) | 2028 | **not yet due** | Restates an earlier claim. 2028 has not arrived. |

#### Demis Hassabis

4 claims: 0 hit, 0 missed, 4 not yet due, 0 unfalsifiable, 0 withdrawn.

| said | in their words | due | today | why |
|---|---|---|---|---|
| 2025-04-20 | "In the next five to ten years, I think." ([transcript](https://www.cbsnews.com/news/artificial-intelligence-google-deepmind-ceo-demis-hassabis-60-minutes-transcript/)) | 2035 | **not yet due** | Neither end of the range has arrived. |
| 2025-04-20 | "I think that's within reach. Maybe within the next decade or so, I don't see why not." ([transcript](https://www.cbsnews.com/news/artificial-intelligence-google-deepmind-ceo-demis-hassabis-60-minutes-transcript/)) | 2035 | **not yet due** | 2035 has not arrived. Heavily hedged ('maybe', 'or so', 'I don't see why not'). |
| 2026-01-20 | "I think I'm still on the same kind of timeline." ([transcript](https://www.youtube.com/watch?v=NnVW9epLlTM)) | 2030 | **not yet due** | Restates an earlier claim. The decade has not ended. A 50% chance, not a certainty. |
| 2026-04-20 | "No, 2030. I've been pretty consistent about that." ([transcript](https://www.youtube.com/watch?v=AFpeWo1GTeg)) | 2030 | **not yet due** | Restates an earlier claim. 2030 has not arrived. |

#### Mustafa Suleyman

4 claims: 0 hit, 0 missed, 3 not yet due, 1 unfalsifiable, 0 withdrawn.

| said | in their words | due | today | why |
|---|---|---|---|---|
| 2023-07-14 | "Something like this could be as little as two years away." ([own words](https://www.technologyreview.com/2023/07/14/1076296/mustafa-suleyman-my-new-turing-test-would-see-if-ai-can-make-1-million/)) | 2025 | **unfalsifiable** | A lower bound ("as little as"), so missing the date proves nothing. 'Could be as little as' names the earliest date it might happen, so missing 2025 does not contradict it. |
| 2024-12-09 | "I do think it is going to be plausible at some point in the next two to five generations." ([transcript](https://www.theverge.com/24314821/microsoft-ai-ceo-mustafa-suleyman-google-deepmind-openai-inflection-agi-decoder-podcast)) | 2031 | **not yet due** | Neither end of the range has arrived. |
| 2026-02-12 | "this year I think there are going to be models that can, you know, achieve that artificial capable intelligence and satisfy the modern Turing test." ([transcript](https://www.youtube.com/watch?v=YTrBz6Z5c0E)) | 2026 | **not yet due** | Restates an earlier claim. 2026 has not ended (2.5 months remain) and I found no report that any AI has done it. |
| 2026-02-12 | "most of those tasks will be fully automated by an AI within the next 12 to 18 months." ([transcript](https://www.youtube.com/watch?v=YTrBz6Z5c0E)) | 2027 | **not yet due** | The window has not closed (earliest end February 2027). |

#### Ilya Sutskever

3 claims: 0 hit, 0 missed, 3 not yet due, 0 unfalsifiable, 0 withdrawn.

| said | in their words | due | today | why |
|---|---|---|---|---|
| 2023-07-05 | "we believe it could arrive this decade." ([own words](https://web.archive.org/web/2023/https://openai.com/blog/introducing-superalignment)) | 2029 | **not yet due** | The decade has not ended. 'Could' makes it a possibility, not a firm forecast. |
| 2023-07-05 | "Our goal is to solve the core technical challenges of superintelligence alignment in four years." ([own words](https://web.archive.org/web/2023/https://openai.com/blog/introducing-superalignment)) | 2027 | **not yet due** | The deadline (July 2027) has not arrived. But OpenAI dissolved the Superalignment team in May 2024 after Sutskever and co-lead Jan Leike left, so the effort as described has ended; |
| 2025-11-25 | "I think like 5 to 20." ([transcript](https://www.dwarkesh.com/p/ilya-sutskever-2)) | 2045 | **not yet due** | Neither end of the range has arrived. |

#### Geoffrey Hinton

4 claims: 0 hit, 1 missed, 3 not yet due, 0 unfalsifiable, 0 withdrawn.

| said | in their words | due | today | why |
|---|---|---|---|---|
| 2016-10-27 | "people should stop training Radiologists now it's just completely obvious that within 5 years um deep learning is going to do better than Radiologists" ([transcript](https://www.youtube.com/watch?v=2HMPRXstSvQ)) | 2021 | **missed** | Contested: "do better than" has been met in narrow studies; the practical outcome (stop training them) is what failed. Five years on (2021) radiologists had not been replaced, and demand has kept rising: the American College of Radiology reported on 2026-02-05 that workforce shortage is the field's biggest threat and that the workforce is … |
| 2023-05-03 | "I now predict 5 to 20 years but without much confidence." ([own words](https://twitter.com/geoffreyhinton/status/1653687894534504451)) | 2043 | **not yet due** | Neither end of the range has arrived. |
| 2023-10-08 | "I think in five years' time it may well be able to reason better than us." ([transcript](https://www.cbsnews.com/news/geoffrey-hinton-ai-dangers-60-minutes-transcript/)) | 2028 | **not yet due** | 2028 has not arrived. 'May well' is hedged, and 'reason better than us' has no agreed test; some will say today's reasoning models already do on some tasks. |
| 2024-12-06 | "My guess is in between five and 20 years from now, there's a good chance, a 50% chance, we'll get AI smarter than us." ([transcript](https://www.nobelprize.org/prizes/physics/2024/hinton/1925103-interview-transcript/)) | 2043 | **not yet due** | Restates an earlier claim. Neither end of the range has arrived. |

#### Yann LeCun

4 claims: 0 hit, 0 missed, 4 not yet due, 0 unfalsifiable, 0 withdrawn.

| said | in their words | due | today | why |
|---|---|---|---|---|
| 2024-10-16 | "I said that reaching Human-Level AI "will take several years if not a decade."" ([own words](https://x.com/ylecun/status/1846574605894340950)) | 2034 | **not yet due** | 2034 has not arrived. He gave a long-tailed distribution, so a miss would not settle it. |
| 2024-10-16 | "In any case, it's not going to be in the next year or two." ([own words](https://x.com/ylecun/status/1846574605894340950)) | 2026 | **not yet due** | The two years ended on about 2026-10-16 but the due year, 2026, has not finished. On the evidence I found it is on course to hold: Legg said on 2025-12-11 current AI is 'not there yet', and Hassabis on 2026-01-20 said 'one or two … |
| 2025-01-23 | "within five years nobody in the right mind would use them anymore at least not as kind of the central component of an AI system" ([transcript](https://www.youtube.com/watch?v=MohMBV3cTbg)) | 2030 | **not yet due** | 2030 has not arrived. |
| 2025-01-23 | "within 3 to 5 years we'll have system that are complete different Paradigm they may have some level of Common Sense" ([transcript](https://www.youtube.com/watch?v=MohMBV3cTbg)) | 2030 | **not yet due** | Neither end of the range has arrived. It is conditional on his own team's plan working. |

#### Kai-Fu Lee

4 claims: 0 hit, 0 missed, 4 not yet due, 0 unfalsifiable, 0 withdrawn.

| said | in their words | due | today | why |
|---|---|---|---|---|
| 2017-04-27 | (reported, no quote) As CNBC reports it: robots and AI will 'probably' replace about 50 percent of human jobs, and he expected that displacement 'to occur in the next 10 years'. ([coverage only](https://www.cnbc.com/2017/04/27/kai-fu-lee-robots-will-replace-half-of-all-jobs.html)) | 2027 | **not yet due** | 2027 has not arrived. |
| 2019-01-13 | "all together in 15 years that's going to uh displace uh about 40% of jobs in the world" ([transcript](https://www.youtube.com/watch?v=aZ5EsdnpLMI)) | 2034 | **not yet due** | 2034 has not arrived. He softens it to 'displaceable' jobs, not jobs that will disappear. |
| 2019-01-13 | "if you're talking about AGI artificial general intelligence I would say not within the next 30 Years and possibly never" ([transcript](https://www.youtube.com/watch?v=aZ5EsdnpLMI)) | 2049 | **not yet due** | 2049 has not arrived. In September 2026 he said the opposite in substance: AI is 'at the footsteps of AGI' and about two years from his bar for AGI (see the 2026 claim). |
| 2026-09-23 | "But answering questions and doing things are quite different. I think we're probably still maybe two years away from that." ([transcript](https://www.youtube.com/watch?v=c4w3njBhYVk)) | 2028 | **not yet due** | 2028 has not arrived. Hedged: 'probably', 'maybe'. |

## 9. The decisions, each with confidence and the strongest alternative

1. **Build a dated-claims ledger at all.** Moderate-to-high confidence that the question is
   worth answering and that this project is where (it holds the panel, the statements and the
   leg B ledger). Moderate that it will stay honest, because the ledger is only as good as its
   admission rule and the collection pass (decisions 4 and 8). *Strongest alternative:* do not
   build it; leave the leaders' dated words as coded statements and let the page keep showing
   their dates beside the test. That costs nothing and risks nothing, but it cannot say whether
   any of them was right, which is the question John asked.
2. **One TOML file per claim in `data/claims/`, with a flat `claims.csv` written for download.**
   Moderate confidence; a judgment call. *Strongest alternative:* one `data/claims.csv`, the
   form this record otherwise uses. Simpler to read as a table and no new file kind, at the
   cost of long prose in cells, harder diffs, and two sessions editing the same file.
3. **Five status words; `withdrawn` counts as missed in every total.** Moderate confidence.
   The count rule is the siblings' ruling of 2026-10-17; keeping the word is mine, so a
   retraction shows. *Strongest alternative:* the siblings' four words (not yet due, hit, missed,
   unfalsifiable) with a `withdrawn_on` date field on a missed claim; identical family
   vocabulary and one fewer word, at the cost of the retraction being less visible.
4. **A claim with no date or length of time in the words is not a claim record**; it stays a
   coded statement, and the page counts each person's undated forward-looking statements so
   vagueness is visible. Moderate confidence. *Strongest alternative:* the siblings' rule, score
   undated claims at a fixed year (2050 there). It keeps family vocabulary and loses nothing at
   entry, but it makes "soon" and "close" unscorable for 24 years, so the ledger could not
   answer John's question inside the project's life; and 2050 is those sites' own horizon, not
   this one's. A third option, enter them all as `unfalsifiable`, buries the scored claims.
5. **A hit needs every condition of the bar; there is no "partly".** A near miss is a miss with
   the gap named. Moderate confidence. *Strongest alternative:* the leg B ledger's two readings,
   strict and generous, printed together, which reflects that the judgement sits between them
   and costs a second status word.
6. **The due year is the end of the named year, a span runs from the day it was said, a range
   takes its later end, a point year with a spread is scored at the point.** Moderate-to-high
   confidence. *Strongest alternative:* take the earlier end of ranges, which is harsher and
   closer to what a reader hears ("5 to 20 years" as "5"), but turns every hedge into a miss.
7. **No percentage for a person with fewer than five due claims.** Low-to-moderate confidence;
   five is a convention, not a derivation. *Strongest alternative:* no floor, always print the
   counts, never a bare percentage. Both show the counts; the floor only stops a headline like
   "100%" from one claim.
8. **No rate is published for anyone until that person has been traced year by year**, as the
   panel's collection does, with the searches logged and quiet years entered. Until then the
   page says "seed only: not a rate". Moderate-to-high confidence; without it the rate measures
   which claims were easy to find. *Strongest alternative:* publish the rate from the seed
   labelled as such; faster and answers the question sooner, at the risk that the label is lost
   when the number is quoted.
9. **Per person, never pooled; the ledger adds its own block to `status.json` and nothing to
   the headline.** High confidence on not pooling (the pattern pools nothing); moderate on the
   file block. *Strongest alternative:* no addition to `status.json`, so the parent site cannot
   read the claims at all; safer, but then the family's Projects page cannot show the ledger.
10. **Scope of people: everyone on the frozen panel, begun with the four leaders and the other
    lab-tied members in the seed**, and Huang included on the same footing although he is not
    tagged `frontier_lab`. Moderate confidence. *Strongest alternative:* the four leaders only;
    a cleaner answer to John's question, but it leaves Hassabis, Legg and the rest out, who
    gave some of the most checkable dated claims in the seed.
11. **A stated goal ("we have set internal goals of X by Y; we may totally fail") is admitted,
    marked as a goal and scored like any other claim.** Moderate confidence. *Strongest
    alternative:* exclude goals as not forecasts; avoids punishing a hedge, but a company's
    dated public commitments are what the hit rate is for, and leaving them out hands every
    leader a way to phrase a forecast as a goal.
12. **Numbering and order of work.** Adopt as the next amendment (A26, the next number after the headline amendment A25: the
    ledger's existence, the five status words, the admission rule, the undated rule, the due-year
    rule, what it never touches), with a method document `docs/claims-ledger-method.md` written
    and committed before any row, as the leg B ledger's method was. Moderate confidence.
    *Strongest alternative:* no amendment and a note in the README, on the ground that it adds
    a record without touching the panel or the test; John has preferred the amendment file to
    be complete.
13. **A probability stated as a number (a 50% chance) is kept and flagged but left out of the
    plain count**, for a later calibration check. Moderate confidence. *Strongest alternative:*
    score such claims with a probability score (the squared distance between the stated chance
    and what happened), which treats them properly but needs many claims per person before it
    means anything.
14. **Where it shows: `/claims/` with one line on the home page and the four gauges repeated
    in a strip at the top of the page.** Moderate confidence. *Strongest alternative:* a
    section on the home page (the pattern's rule 6.4 argues for it).

## 10. The rulings John must make

The first four are the ones the master session named; the rest each have a default I would take
if John answers "as recommended".

1. **Adopt the ledger or not.** Recommended: adopt, on the terms below, and write the method
   document first (decisions 1 and 12).
2. **The status words and the undated-claim rule.** Recommended: the five words with
   `withdrawn` counted as missed (decision 3); undated claims stay coded statements, counted but
   not scored (decision 4); every condition must be met for a hit (decision 5). The alternatives
   are the siblings' four words, and scoring undated claims at 2050.
3. **Huang first or not.** Correction first: he is already on the panel, so no amendment is
   needed. Recommended: not first. Begin with Altman (eleven of his sixteen seed claims
   already point at coded rows, nearly all with primary sources) and Musk (the most dated
   claims), then Amodei, and Huang after them, since his panel row is the thinnest and
   his dated claims are mostly Nvidia's own sales and shipping. The alternative is Huang first
   because his claims are the easiest to settle from the company's own releases.
4. **Where it lives.** Recommended: a page of its own, `/claims/`, with a home-page line, a
   "Claims" handle in the top bar's heavier tier, and the gauges repeated at the top
   (decision 14). The alternative is a home-page section.
5. **Scope of people.** Recommended: everyone on the frozen panel, starting with the leaders
   and the lab-tied members (decision 10). Or the four leaders only.
6. **The record's form.** Recommended: one TOML file per claim (decision 2). Or one CSV.
7. **No rate before a person is traced; no percentage under five due claims** (decisions 7
   and 8). Or a labelled seed rate.
8. **Goals and probabilities.** Recommended: admit goals, keep numeric chances out of the plain
   count (decisions 11 and 13).
9. **Numbering** (decision 12): an amendment, with the method document first.
10. **The open TimeAssembler question about adding Huang** rests on a premise the record does
    not support (section 0). Recommended: close it with a note that he is on the panel, and
    open a smaller question only if John wants a note on the thinness of his row.

**If John rules "as recommended" on all ten**, the next steps are, in order: the method document
and the amendment entry; the validator's claims check; the first rows for Altman and Musk with
their searches logged; then the page. Nothing in this proposal starts any of them.
