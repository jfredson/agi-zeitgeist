# Claims ledger: a dated record of what the industry's leaders predict

**Status: method written 2026-10-17 by the agent, from the proposal John adopted the same day
(`docs/claims-ledger-proposal-2026-10-17.md`, all ten rulings "as recommended"), before any
claim row was built. Amendment A27 in `docs/amendments.md` records the adoption. Changing a
rule here after rows exist is an amendment entry, never a quiet edit. Amendment A30 (2026-10-19)
widened the ledger from the panel to the industry's figureheads, with a ledger-only list for
the three who are not on the panel. Amendment A31 (decided 2026-10-19) turns the
ledger from a scorecard into a record of what the industry's leaders predict; the sections it
changes are marked below.**

## What this ledger is for

*(Rewritten under amendment A31, decided 2026-10-19; the text it replaces is in that entry.)*

John's ruling of 2026-10-19: "The goal is not to score people on their success at predicting the
future, the goal is to track the zeitgeist of what these people are saying to get a feel for
what the vanguard of the industry is predicting at any given time."

So this is a dated record of what the people who lead the companies building frontier AI say
the future holds: when they expect AI to match or pass people, and what they expect it to do
along the way. Who they are is set out under the admission rule. Each prediction is in their own
words, with the date, the occasion and the source. It is one of the tracker's two voices, beside
the academics and long-time thinkers on the frozen panel. John's ruling of the same day: "We need
to track both the traditional academics who have been talking about this for decades as well as
the new industry leaders who are actually making it happen but tend to run way out in front of
their skis with their predictions. Both of these are valuable for the Zeitgeist though." It is
read the same way as the panel: for what they are predicting now, how far that sits from the
academics, and how it has shifted. It is not a scorecard. Where a prediction's date has passed,
a small note on the claim says what happened.

It does not say whether a person is right about the future, whether they are sincere, or
whether the technology is good or bad.

It sits beside two records that already exist. The coded statements (`data/statements.csv`)
say what the frozen panel said and sort it, dated or not; the frontier-voices chart on the home
page draws the panel's dated guesses. This ledger covers the industry's figureheads only, takes
only predictions that carry a date, and keeps the verdict on each as context.

## The record: one file per claim

Each claim is one file, `data/claims/<id>.toml`, where the id is the date it was said, the
speaker id and a short slug: `2025-10-29-altman-automated-research-intern`. A file is never
renamed. The site build writes a flat table, `site/data/claims.csv`, from the files so the
ledger can be downloaded like every other table.

Why files and not a spreadsheet: a claim carries paragraphs of prose (how the words were
checked, why the verdict is what it is), which a cell holds badly; and two sessions adding
claims never edit the same file.

Every file holds one `[claim]` table with these fields.

| field | required | what it holds |
|---|---|---|
| `id` | yes | The file name without `.toml`. |
| `speaker_id` | yes | A `speaker_id` in `data/speakers.csv` whose tier is `core` or `cohort_2020s` (the frozen panel, amendment A18) or `claims_only` (the ledger-only list, amendment A30). The validator refuses a claim by anyone else. |
| `when` | yes | When it was said: `YYYY-MM-DD`, or `YYYY-MM` or `YYYY` where the record settles nothing finer. |
| `when_note` | if `when` is not a full date, else optional | How the date was settled (a post's timestamp, a page's date line, an event's date). |
| `occasion` | yes | Where it was said: a post, an essay, a keynote, a named interview, a hearing, a filing. |
| `source_kind` | yes | `own_words` (the person's own post, essay, filing or paper), `transcript` (an official or checked transcript or recording), `printed_qa` (a question-and-answer interview printed as their own words), or `coverage_only` (a report of what they said). |
| `source_url` | yes | The one address to open. |
| `source_locator` | yes | Where in it: a timestamp, a section, a paragraph. |
| `checked_how` | yes | How the words were checked and on what date: read on the page, listened to, an official transcript, automatic captions read as a run of words. |
| `quote` | unless `coverage_only` | The words, verbatim, at most 25 words. Forbidden on a `coverage_only` entry. |
| `reported_as` | only on `coverage_only` | What was reported, with the reporter or outlet named. |
| `statement_id` | no | The `statement_id` of the row in `data/statements.csv` the claim was seeded from, if any. The validator checks the row exists, its speaker matches, and its date matches `when` (to the month, since the statements table carries some dates in universal time and this ledger in the speaker's own time). |
| `prediction` | yes | What it commits to, in plain words, with the hedges and conditions kept ("probably", "may", "if"). |
| `kind` | yes | `capability` (a thing AI will be able to do), `timing` (a named stage arrives, such as AGI or superintelligence, or a named thing comes out by a date), or `deployment` (a product ships or a number is reached). |
| `bar` | yes | The test that will settle it, written at entry and never changed afterwards except by a dated note: the speaker's own definition if the same source gives one, otherwise the plainest reading of the words. The test uses the speaker's words and the speaker's own usage in the same source, adds no condition he did not state and drops none he did, and is never shaped to fit a verdict. A claim whose words give no test an outsider could run has `bar` saying so, and the status `unfalsifiable`. |
| `due` | yes | The year the claim can be judged by, from the speaker's own words (the rule below). A whole number. |
| `due_basis` | yes | The words or the sum that gave the year. |
| `due_date` | no | A full date, where the words name a point earlier than the end of the year ("by September of 2026" gives `2026-09-30`; "in June" gives the last day of June). |
| `due_early` | no | Where the claim is a range of years, the earlier end, so the page can show the claim was already late against it. |
| `is_goal` | no | `true` where the words are a stated goal, not a forecast ("we have set internal goals of ...; we may totally fail"). Admitted and scored like any other claim; the page marks it. |
| `has_probability` | no | `true` where the speaker gave a number ("a 50% chance"). Kept, scored, flagged, and left out of the plain count. |
| `restates` | no | The id of an earlier claim by the same person that this one repeats with a changed date or condition. |
| `repeated_on` | no | Dates on which the same person repeated this claim unchanged. |
| `status` | yes | One of the five words below. |
| `verdict_on` | on `hit`, `missed`, `withdrawn` | The date the record settled it: the date of the demonstration, release or count, or of the words that withdrew it. |
| `verdict_why` | on every status but `not_yet_due` | The reason in plain words. On a miss, which condition of the bar failed and by how much. On `unfalsifiable`, why no outsider could test it. |
| `verdict_source` | on `hit`, `missed`, `withdrawn` | The dated primary source for what happened: the maker's release, a regulator's notice, an official benchmark or competition result, the speaker's own later words. |
| `evidence_by` | on `hit`, `missed`, `withdrawn` | `outside` (someone other than the speaker's own company measured it) or `maker` (the only evidence is the speaker's company, or the speaker, saying so). The page marks `maker`. |
| `direction` | on `missed`; optional on `hit` | Which way it went: `later` (the thing came, after the due date), `not_come` (it has not come as of the verdict), `sooner` (a hit that came well before the date), `on_time`. |
| `search_ids` | yes | The ids in `data/search_log.csv` of the searches and fetches that found the words and settled the verdict. Every one must exist. |
| `notes` | no | Anything else a reader needs: the judgement calls, the words left out, the flags. |
| `verify` | no | Plain claims in the entry made from memory or a search excerpt and not yet checked at the source. A later session clears each. |

A worked example is in the proposal, section 2.

### What a timing claim says arrives (amendment A31)

Every timing claim carries, entered by hand:

- `arrives`: what the forecast says comes. `agi` (AGI or human-level AI, in whatever term the
  person uses), `superintelligence`, `beyond_people` (AI better than people at most or all
  things, smarter than any human, "a country of geniuses"), or `other` (a model, a product, a
  robot, a feeling in the industry).
- `arrives_term`: for anything but `other`, the person's own term, short ("minimal AGI",
  "powerful AI").
- `form`: for anything but `other`, the shape of the date: `year` (about a single year), `range`
  (`due_early` to `due`), `by` (no later than `due`), `not_before` (not before `due`), or
  `chance_tail` (the far end of a stated chance, such as a 10% or a 90% year, which marks the edge
  of a spread rather than the forecast and is not drawn).

Only forecasts with `arrives` other than `other` and `form` other than `chance_tail` are drawn.
The validator refuses a timing claim without these fields, and any other kind of claim with
them.

### Undated words (amendment A31)

A leader's words on when AGI or beyond arrives that carry no year and no length of time ("AGI is
close", "we are nowhere near it") are not claims. Since 2026-10-19 they are kept, as words only,
in `data/claims_undated/`, one file per passage, `[words]` table: `id` (the date said, the
speaker and a slug, equal to the file name), `speaker_id`, `when`, `occasion`, `source_kind`
(own words, a transcript or a printed Q&A; never news coverage), `source_url`,
`source_locator`, `checked_how`, `quote` (and `translation` where the words are not in English),
`arrives`, `about` (one plain sentence), `search_ids`, and optionally `when_note`,
`statement_id` and `notes`. The same people and the same role-at-the-time rule apply as for
claims. Each person's search for them runs back from the present to their latest dated forecast
(or two years, for those with none), every search logged. The page shows a person's latest undated
words when they are newer than their latest dated forecast, or the person has none, so that no
one is shown as silent; they are never drawn and never scored. The validator refuses a passage
that names a year.

## Which claims get in (the admission rule)

A claim is admitted when all four are true. The test never looks at whether it came true.

1. **The speaker is on the frozen panel or on the ledger-only list, and held a qualifying role
   when the words were said** (`data/speakers.csv`; amendment A30). The ledger covers the
   industry's figureheads: **a figurehead is the chief executive, founder-leader or chair of a
   company that builds frontier AI models or the chips they are trained on, or that company's
   named chief scientist speaking for it.** A claim counts only if it was made while the
   person held that role. A claim made before or after it, or in a gap between two such roles,
   is left out, and the search-log row that found it says why. Each claim's `notes` name the
   role that applied. The fifteen figureheads are listed under "Order of work". Tesla counts as
   such a company for Elon Musk's claims as its chief executive from 2019 to 2021 (ruled by John
   2026-10-19).
2. **The words look forward and are about AI**: they say AI will do, reach or ship something,
   or that it will not by a stated date (see "Readings ruled by John" below). A company's
   spending, revenue, order book, headcount, chip count, computing or data-centre build-out,
   training costs and labour-market forecasts that are not about what AI will do ("50 million
   workers short") are business forecasts, not claims about AI, and stay out; a forecast that AI
   will displace, change or create jobs is about AI and is admitted. A product shipping counts only when the product is an AI system and the words claim
   something about what the AI will do or about its deployment; a plain hardware date stays out.
   A line framed as a hypothetical ("let's imagine", "suppose", "I could imagine", or a date
   given only for an extrapolation the speaker says he does not believe) is not a prediction.
   A truly borderline case stays out and is logged as borderline. (Given by the managing
   session on 2026-10-19 while the ledger was widened; amendment A30.)
3. **The words carry a date or a length of time**: a year ("by 2030"), a span counted from the
   day it was said ("in five years", "the next ten years", "this president's term"), or a stage
   with its own end ("by the end of this decade").
4. **There is a primary source**: own words, a transcript or recording, or a printed question
   and answer. A claim found only in coverage may be entered as `coverage_only`, shown and
   marked, with no quote.

Anything else stays what it is, a coded statement: "AGI is coming", "still many years away",
"we are close", "in a few years", "could be as little as two years away". **An undated claim is
not a claim record.** Since amendment A31 a leader's latest undated words on when AGI or beyond
arrives are kept as words only (above, "Undated words"), so vagueness stays visible without
being dated or charted.

## Readings ruled by John

John ruled four readings on 2026-10-19, each as the independent check of the widened ledger
recommended (`docs/reviews/claims-ledger-check-2026-10-19.md`):

1. **"Early" in a year means its first quarter.** "Early next year" or "early 2025" sets
   `due_date` to 31 March of that year. "Early" in a month ("early June") is not ruled; the
   ledger reads it the same way, as the first third, so the tenth of the month, and flags it for
   John.
2. **A forecast that something will not happen by a date is a claim.** "Not in the next two
   years", "not before 2030", "it will take at least a decade" are scored at the stated date:
   it came true if there is no public record of the thing by then, and did not if there is.
   The test names the thing in the speaker's words; `due` is the stated date.
3. **"A few years" and "as little as X" are undated.** "A few years" names no length; "could be
   as little as two years away" names only the earliest the thing could come, so missing it
   proves nothing. Neither is a claim record; each is left out and logged. The ledger applies the
   same reading to "the next few months" and "the coming months", which name no length either
   (an application by the agent on 2026-10-19, flagged for John).
4. **Bare "human level" is a named stage.** With no comparison in the same source, "human-level
   AI" cannot be tested, like an undefined "AGI". A stated comparison ("better than humans at
   X", "smarter than the smartest human", "can do the cognitive tasks people can typically do")
   gives a plain-reading test.

## The five status words

| word | meaning |
|---|---|
| `not_yet_due` | The due date has not passed: 31 December of the due year, or `due_date` where the words name an earlier point. Shown, not scored. A claim stays `not_yet_due` until its date passes even where the thing has already happened; the notes may say what has been seen so far, and the verdict is entered when the date passes. |
| `hit` | By the due date, every condition in `bar` was met, shown by a dated primary record of the event itself (the release, the count, the demonstration), not by an argument that it had become possible (given by the managing session on 2026-10-19). For a forecast that something will not happen, a hit is no public record of the thing by the date (reading 2 above). |
| `missed` | The due date has passed and the bar was not met, or only part of it was. The record says which condition failed. A near miss is a miss with the gap named; there is no "partly". |
| `withdrawn` | The speaker later said the claim no longer holds: a retraction, not a new date. **Counted as missed in every total.** The word is kept apart only so the page can show that they took it back, and when. A claim the speaker re-dates is not withdrawn: it is a changed repeat (see Restatements), and the earlier claim keeps its own due date and gets its verdict then (ruled by John 2026-10-19). |
| `unfalsifiable` | The claim has a date but no bar an outsider could test, or its only judge is the speaker ("we will have an internal system I would call AGI"). Decided at entry, when `bar` is written; shown and counted apart, left out of the rate, and a bar is never supplied after the fact. This is the rule the leg B ledger uses for its "no bar" rows. |

Verdicts are entered by hand and dated. Nothing scores a claim automatically.

## What counts as a hit, by kind

- **Capability** ("AI will be able to do X by Y"). A dated public demonstration that meets every
  stated condition: the paper, the maker's release, a benchmark's official result or a
  competition result. A demonstration only shows the thing was possible by then, so a hit is
  "no later than". Where the only evidence is the maker saying so, the claim can still be
  settled, with `evidence_by` set to `maker` and the page marking it. Where the claim's own test
  is a milestone the leg B ledger already judged, the verdict follows that row; the same fact is
  never judged twice.
- **Timing** ("AGI by 2027", "superintelligence in a few thousand days", "Grok 3 by the end of
  the year"). For a named stage, the bar is the definition the speaker gives in the same source;
  with none, the claim is `unfalsifiable` unless the plainest reading supplies a bar at entry.
  A named comparison gives a plain reading; a named stage does not. Musk's "smarter than the
  smartest human" keeps a bar because it names a comparison that can be checked (better than
  the best person at thinking work), while Altman's "superintelligence in a few thousand days"
  is `unfalsifiable` because it names a stage he never defines in the source (ruled by John
  2026-10-19).
  The ledger never borrows the singularity test's thresholds for this, because that would let
  the ledger move the test. For a named thing coming out, the bar is its release.
- **Deployment** ("a robotaxi service by Y", "a billion users by Y"). The maker's own release, a
  regulator's notice, or an independent count showing it shipped to the stated scale by the due
  date. A stated number must be met, not nearly met. A maker's own figure is evidence for a
  figure only the maker holds, and is marked.

## The due year

- A named year is judged at the end of it.
- A span ("in five years", said 2024-03-18) runs from the day it was said to that date five
  years on, and is judged at the end of that year. A range of spans ("four or five years") takes
  the later end, the generous one, and `due_basis` says so.
- "By the end of this decade" is 31 December 2029 or 2030, whichever the speaker's own usage
  implies; where it does not, the later, and `due_basis` says so.
- Where the claim itself is a range of years ("2027 to 2034"), `due` is the later end and
  `due_early` the earlier, so the page can show the claim was already late against its early end.
- A point year with a spread beside it ("roughly human-level AGI in 2025", with a stated range
  to 2036) is scored at the point year, and the spread is a second claim with its own due year.
  Otherwise a speaker could always say the range was the claim.
- A month or a quarter in the words ("in June", "by September of 2026", "in Q1") sets
  `due_date` to the last day of it.
- A **goal** ("we have set internal goals of X by Y; we may totally fail") is a dated public
  commitment with the hedge in the speaker's own words. It is admitted, marked `is_goal`, and
  scored like any other claim.
- A **condition** in the words ("assuming we get regulatory approvals") is kept in
  `prediction` and `bar`. The claim is still scored on its date; the verdict says whether the
  condition held, so a reader can weigh it.

## Numbers given as chances

A claim that states a probability ("a 50% chance by 2035") cannot be scored by one outcome. It is
entered, flagged `has_probability`, given its note like any other, and marked as a stated chance
on the page. (Until amendment A31 such claims were kept out of the plain count behind a hit rate;
there is no rate now.) Hedge
words ("probably", "I'd be very surprised if not") are not probabilities: those claims are
scored at face value with the hedge written in `prediction`.

## Restatements

Saying the same thing again is not a new prediction; changing the date is.

- **Unchanged repeat** (same prediction, same due year): one claim, keyed to the first date, with
  the later dates in `repeated_on`. Counting each repeat would let a repeated hit or miss
  inflate a record.
- **Changed repeat** (new due year or changed condition): a new claim record with `restates`
  naming the earlier one. The earlier record is never edited; its verdict is given on its own due
  date whatever was said later. The page groups a chain and shows the due years in order, so a
  date that keeps sliding is visible as a slide.

## Verdicts as small notes, and no rate

*(Rewritten under amendment A31, decided 2026-10-19. John's words that day: "Sure, we can keep the
verdicts as small notes, but they are not the point of the tracker.")*

- **Each claim keeps its verdict** (the five status words and the evidence, as above). On the
  page it is a small note on the claim: whether its date has passed, and what happened.
- **Verdicts appear in no headline, summary, count, chart title or share post.** The claims
  page carries no table of counts, the home page no total, and the `claims_ledger` block of
  `site/status.json` no verdict counts (it keeps the number of claims and people, and a `now`
  block). The downloadable table keeps each claim's status, which is that claim's note.
- **When a claim's date has passed:** 31 December of `due`, or `due_date` where set, whatever its
  status (amendment A30).
- **No hit rate,** per person or pooled.
- **The year-by-year search stays.** A person's latest forecast is only their latest if their
  recent years have been searched, so each person is traced from their most recent year back,
  with every search logged and quiet years entered as rows. The finished trace is still the row
  `<speaker_id>-claims-traced` in the search log; it records that the search is complete and
  no longer unlocks anything.
- **Both directions of selection are logged,** as before.


## Searches and the search log

Every fetch of a source and every search is a row in `data/search_log.csv` before the claim is
written, with the speaker's id, the address or query, where it was run, what it found and the
date. A claim names its rows in `search_ids`, and the validator refuses a claim naming a row
that is not there. Ids are `<speaker_id>-claims-NNN`, numbered in the order the work was done.

## What the ledger must never touch

The ledger is a separate record kind beside the others. Talk and delivery are never mixed.

- **The frozen panel** (`data/speakers.csv`, amendment A18). A claim by someone neither on it
  nor on the ledger-only list is refused. Adding anyone to the panel is an amendment to the
  panel first.
- **The ledger-only list** (tier `claims_only` in `data/speakers.csv`, amendment A30): the
  figureheads who are not on the panel, so that their claims can be recorded without widening
  it. These rows are never panel members. They never enter `data/statements.csv`, the opinion
  charts, the experts' dates or the panel's counts, and they carry no panel quota tag; the
  validator refuses each of these. Adding a name to the list, or taking one off, is itself an
  amendment.
- **The coded statements** (`data/statements.csv`). No row is edited, added or deleted because
  of a claim. A claim points at its row with `statement_id`; nothing is copied back.
- **The scored series**: `data/world_measures.csv`, `data/aggregates.csv`, the leg B ledger's
  rows, and everything `scripts/site.py` scores from. A claim's verdict is never a measure of
  the world.
- **The frozen thresholds** (`docs/singularity-entry-thresholds.json`) and **the definition**
  (`docs/singularity-entry-definition.md`), including leg B's gauge, which stays defined on
  forecasts of METR's task-length measure and cannot be filled by anyone's claims.
- **The verdict and the headline** (amendment A25). Nothing in the claims ledger enters the
  headline, and the headline fields in `site/status.json` do not change. The ledger adds its own
  `claims` block to that file, never a field the parent site could mistake for the headline.
- **The weekly reading's rule** (`docs/weekly-reading.md`): the reading may flag a claim that
  has come due; the verdict is still entered by hand and dated.

## Where it shows

*(Rewritten under amendment A31, decided 2026-10-19.)*

A page of its own at `/claims/`, headed "What the industry's leaders predict", in this order:

1. **What they say now.** A figure (`site/claims-now.png`, drawn by `scripts/charts.py`) of each person's latest dated forecasts of AGI, superintelligence or AI
   better than people at most things, in their own term, on one shared timeline (a range, a
   year, or a forecast that it will not come before a date), set against a band for the middle
   half of the academics' dated guesses since 2023 (the frontier-voices rows), with the date it was said and a
   mark where it comes from news reports rather than their own words. Under it, a line per
   person: those forecasts in their own terms; their latest undated words when newer than that
   forecast or when they have none (words only, never drawn); and their latest dated prediction of
   any kind. The figure's title and the home-page sentence are computed from the same figures
   (`scripts/chart_style.py`, `leaders_now` and `academics_band`), so they stay true as claims are
   added.
2. **How it has moved.** A figure (`site/claims-moved.png`) of every such forecast since 2023,
   placed by the day it was said and the year it named, one small panel per person, with a link to the frontier-voices chart on the home page.
   The three on the ledger-only list appear here, never in that chart (A30).
3. **Every claim,** by person, in date order: the words, the date, the occasion, the source, the
   test, and the verdict as a quiet note.

One sentence on the home page, about the present (what the leaders who name a year say now,
beside the academics), never a total of verdicts. `scripts/site.py` reads `data/claims/*.toml`, writes
`site/claims/index.html` and `site/data/claims.csv`, and adds a `claims_ledger` block to
`site/status.json` with the number of claims and people, the academics' band, and a `now` block
(each person's latest forecasts and undated words), with no verdict counts;
`scripts/validate.py` checks every file.


## Order of work

Ruled by John on 2026-10-17: Altman and Musk first, then Amodei, then Huang, then the other
panel members tied to the frontier labs, then anyone else on the panel with a dated claim.

Widened by John on 2026-10-19 (amendment A30) to the fifteen figureheads. On the frozen panel:
Sam Altman, Elon Musk, Dario Amodei, Jensen Huang, Demis Hassabis, Mustafa Suleyman, Ilya
Sutskever, Liang Wenfeng, Arthur Mensch, Shane Legg, Yann LeCun and Kai-Fu Lee (his claims
count only from 2023, as founder and chief executive of 01.AI). On the ledger-only list:
Mark Zuckerberg, Sundar Pichai and Satya Nadella. After Altman and Musk the order is Amodei and
Huang, then Hassabis, Suleyman, Sutskever, Legg, LeCun, Liang Wenfeng, Mensch, Zuckerberg,
Pichai and Nadella, then Kai-Fu Lee, added by John later the same day. Panel members who never held a qualifying role (Geoffrey Hinton, Ray
Kurzweil) are not entered; any other name is added only by amendment.
