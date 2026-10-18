# The weekly reading: how the record is checked against the news

Written 2026-10-16, adapted from The Upgrade Tree's weekly reading (`docs/weekly-reading.md`
and `docs/weekly-reading-prompt.md` in that repository, written the same day) and The Belt
Equation's scan procedure (`docs/scan-procedure.md`, ruled by John 2026-09-19, audited
2026-10-06). It answers a question John asked on 2026-10-16: how would a report like the
Anthropic Institute's expectations-gap survey, published that day, be caught by future scans
instead of by chance? The decisions at the end each carry a confidence and an alternative, as
the siblings' do, and the schedule is a proposal until John rules on it.

This is a working document, so it uses the project's own words (leg, gauge, row, verdict,
scanner). The scanner is the fresh Claude session that follows
`docs/weekly-reading-prompt.md` once a week.

## The idea in one paragraph

The tracker is a dated record built from named sources: four world measures that score the
singularity-entry definition, a fixed set of surveys, pollsters and prediction markets whose
results sit in `data/aggregates.csv`, and a list of dated events. Once a week a fresh Claude
session with no memory of earlier conversations reads each of those sources for what came out
in the past week, and writes a reading record: for each source, what it searched, what it
found, and one of four verdicts. Where a source has published a new reading of a series the
record already holds, the scanner appends a row; where something new or unclear turned up, it
writes the item up for John. It never changes anything that is already in the record, and it
never changes what is scored. The record of each run is one file, never edited, and every
search it ran is in the project's search log like every other search.

The difference from the two siblings: The Belt Equation's scanner may move a probability, and
The Upgrade Tree's may move a stage. This one moves nothing. It may only append rows and
flag. The tracker's rules for what counts (the codebook, the frozen panel, the frozen
thresholds) are deliberately hard to change, and a weekly automated pass is the wrong place to
change them.

## What the scanner may and may not do

It **may**:

- append a row to `data/world_measures.csv` when a named gauge source publishes a new reading
  of the series already in that file (a new METR model row, a new R&D Automation Index
  figure, a new World Bank year or a revision of one);
- append a row to `data/aggregates.csv` when an institution already in `data/speakers.csv`
  publishes a repeat of an item already in that file, with wording comparable to the series'
  `measure` text, and with the sample size and fieldwork dates to go with it;
- append a row to `data/events.csv` for an event of a kind that file already defines (an open
  letter, a public statement, a government action, a report, or an AI release under the rule
  of amendment A21);
- append rows to `data/search_log.csv` for every search and every fetch it ran;
- write the reading record and the commit.

It **may not**:

- edit or delete any existing row in any file;
- edit `docs/singularity-entry-thresholds.json`, `docs/singularity-entry-definition.md`,
  `docs/codebook.md`, `docs/methodology-v2.md`, `docs/amendments.md` or `data/speakers.csv`;
- swap a new measurement into the scoring in place of the series the definition names, or
  mark a row so that the site scores it (for leg C that means never ending an id in
  `-rd-leads` for a row that is not the R&D Automation Index itself);
- add a row with new question wording as though it were a repeat of an existing series;
- add a speaker, a statement by a panel member, or an AI release that amendment A21's rule
  does not admit;
- change the window, the parts or the verdicts of the reading; those change by editing this
  document, which is John's.

Anything it wants to do outside those limits becomes a `flagged` item: what it would have
added, the record it rests on, and why it stopped. John rules after the fact.

## The rule that matters most: a measurement is not the series

The definition scores each leg from one named series. The world keeps producing other
measurements of the same thing, often from the same source, often more striking. The scanner
records such a measurement as a row when it is a repeat of a series already in the file, and it
**always** flags it for John, and it **never** swaps it into the scoring.

The worked example is the week this document was written. Leg C (AI doing the improving) is
scored from the Anthropic Institute's R&D Automation Index: the share of Anthropic's AI
research work that its model "leads", judged by the model itself. The scored row for August
2026 says 26% (`anthropic_institute-2026-08-rd-leads`). On 2026-10-16 the same Institute
published "The AI expectations gap", in which a poll of 1,334 Anthropic staff gave a median
estimate that AI does 51% of the work of building an early-2026 frontier model, for the same
month. Both are the same company talking about the same month, and the numbers differ by
half. They measure different things: the index counts tasks the model completes end to end
under supervision; the poll is staff opinion with no task list and no definition of "does".
The right handling, done by hand on 2026-10-16 before this reading existed, is what the
scanner must do by rule: the 51% is recorded as its own row in `data/world_measures.csv`
(`anthropic_institute-2026-08-staff-estimate-ai-share`, marked as a staff survey), its id does
not end in `-rd-leads`, so the site's leg C gauge ignores it, the thresholds file is untouched,
and a dated note under leg C says which should score is John's call. Had the reading found it,
the item's verdict would have been `new-row` for the survey rows and `flagged` for the
question of what scores, with both in the report.

## The three parts of the reading

### Part 1: the four gauges

For each leg, the scanner reads the source the definition names, and only that source counts
as a reading of the gauge. Anything else about the leg is noted or flagged.

- **Leg A, pace.** METR's time-horizon series: fetch METR's results file
  (`https://metr.org/assets/benchmark_results_1_1.yaml`, the file every METR row in
  `data/world_measures.csv` cites) and compare its model list with the record's. A model in the
  file and not in the record is a `new-row` (date, 50% horizon in minutes, METR's interval and
  frontier flag, in the notes form the existing rows use). Also read METR's time-horizons page
  and search for a new release of the series (Time Horizon 1.2, a successor suite); any change
  to the series itself is `flagged`, because the definition's successor rule is an amendment.
- **Leg B, forecasts.** Unmeasured until the forecast ledger exists, so there is no row to
  append. The scanner searches for new forecast-versus-outcome material (a scored set of AI
  forecasts, a retrospective on a timeline prediction, a new reading of a consensus arrival
  date) and notes it; the item is `noted` or `quiet`, never `new-row`, and anything that
  looks like a candidate measure for the ledger is `flagged`.
- **Leg C, AI doing the improving.** Three reads. First, the Anthropic Institute's R&D
  Automation Index page (`https://www.anthropic.com/institute/measuring-pace-of-ai-development`)
  for a new figure: a new month is a `new-row` on the scored series. Second, new Anthropic
  Institute publications that measure AI's share of AI work in any other way (a staff survey, a
  code-share figure): `new-row` if a repeat of a series in the file, and `flagged` in every
  case under the rule above. Third, measures from outside the company, which is what the
  roadmap step "Leg C second source" is waiting for: researcher surveys of AI's share of
  frontier research work, and the AI-contribution disclosures that venues (NeurIPS, ICLR,
  ICML, journals) now publish statistics on. Nothing from this third read is appended in the
  first version; a candidate second source is `flagged` with what it measures and how often.
- **Leg D, the economy.** The World Bank's annual world growth series, read on the first
  reading of each calendar month only: fetch the API address the existing rows cite and
  compare the values for the last four years with the record's. A new year is a `new-row`; a
  revision of an existing year is a `new-row` with the revision said in the notes, since an
  existing row is never edited; a change in the API's "last updated" stamp with no change in
  the values is `noted`. The IMF's outlook and other forecasts are not the source and are at
  most `noted`.

### Part 2: every institution in the record

Every row in `data/speakers.csv` whose type is not `individual`: the surveys, the prediction
markets, the pollsters and the institutions. The four gauge sources (METR, the Anthropic
Institute, the World Bank, and Google's code-share statements, which are shown beside leg C
but not scored) are read in part 1 and take their item there; Google gets its own item in
part 2 because it is not a gauge. For each of the rest, one or two web searches for releases
in the window, or one fetch of the source's own database where the record was built that way
(Manifold's market endpoint, Metaculus's question page), and:

- a repeat of an item already in `data/aggregates.csv`, with wording comparable to the
  series' `measure` text, is appended as a `new-row` with the result, the sample size (`n`)
  and the fieldwork dates (in `date`, at the precision the source gives, and spelled out in
  the notes), in the notes form the existing rows of that series use;
- a release with new wording, or a repeat whose sample size or fieldwork dates the public page
  does not give, is `noted` or `flagged`, never added as though comparable;
- a source that has stopped publishing, closed, or changed its method is `flagged`, since
  what to do about its row is John's.

Sources John has ruled closed are not read at all, on any scope: Monmouth University's polling
institute (ceased operations 2025-07-01; ruled 2026-10-17). Metaculus is read only if a search
finds a public reading, since its question cannot be fetched without an account token (ruled
2026-10-17: the row stays with no series).

Series that are read yearly (Google Trends' yearly means, read in January) and one-off
surveys that will not recur (Müller and Bostrom's 2012 to 2013 questionnaire) are read on the
monthly scope only, and may be `quiet` with that reason and no search.

### Part 3: events

Events of the kinds `data/events.csv` already defines: open letters, public statements,
government actions, reports, AI releases. Two or more searches per kind for the window, read
against the primary record (the letter's own page, the government's own notice, the report
itself, the maker's own release). An event of one of those kinds, dated inside the window on
its own record, is a `new-row` in the form the existing rows use (the key sentence quoted, the
count at retrieval, the primary page as source). An AI release is appended only under
amendment A21's rule, that the system is named in at least one statement in
`data/statements.csv`; a release not so named is `noted`, and a reading that later finds a
statement naming it flags the release for adding. Whether a report or a statement is of the
record's kind is read strictly: when two readers could disagree, it is `flagged`, not added.

### Deferred: the frozen panel's new statements

The thirty-seven panel members (core and 2020s cohort) and the wide list are not read in the
first version, for two reasons. Full collection for the panel is not done, so a weekly pass
would be adding statements for 2026 to people whose 2017 to 2025 rows do not exist yet, and
the series would be dense at one end for no reason but the reading's start date. And the
codebook's quality bar is an agreement test (methodology section 10 and section 12: coding is
model-based with three model families and a two-of-three rule, and the seed phase required 80%
agreement on the main fields), which one session coding one statement a week cannot meet. When
full collection is done, the panel becomes part 4, and the reading's job for it is to find
and log the statement and leave coding to the collection pipeline.

## The window and the scope

The window is the seven days ending on the reading's date, Pacific. The scope is `monthly` on
the first reading of each calendar month (no file in `data/readings/` dated that month), and
`weekly` otherwise. A monthly reading adds leg D and the yearly and one-off series; nothing
else changes with scope.

An item found that is older than the window but newer than the series' latest row (a poll from
three weeks ago the record missed) is handled the same way as an in-window item, with "older
than the window" said in `found`; the record exists to be complete, and the row carries its
own dates. On the first reading, where the backlog is of unknown size, such items are
`flagged` rather than appended, so John can decide the catch-up in one piece.

## The searches

Two is a floor for every item that is searched at all: at least one search or fetch aimed at
the source's own pages and one at wider reporting, worded differently. A fetch of the source's
own database counts as one. Only a `quiet` item may list fewer, and then `found` has to say
why (a yearly series out of season, a one-off survey, a search tool that failed twice). No
more than four per item, except where a source's own page has to be fetched to settle a
candidate row.

Every search and every fetch is a row in `data/search_log.csv`, the tracker's existing rule
("log your search first"), with these particulars: `search_id` is `reading-YYYY-MM-DD-NN`
(the reading's date, then a two-digit counter in the order run); `speaker_id` is the speaker
the search was for, `events` for part 3, or `reading` for a search that belongs to no one
speaker (leg B's forecast material, leg C's outside measures; `reading` is a reserved value
the validator accepts, like `events`); `year` is the year searched for, or blank; `query` is
the search as typed or the address fetched; `where_searched` the engine or site;
`what_found` the one-line result; `date_searched` the reading's date. The reading record's
items point at these rows by id, and the validator refuses a reading whose search ids are not
in the log, and a log row with a `reading-` prefix that no reading item uses.

## Reading the results

Read literally against the record. A measurement is a repeat only when its wording matches
the series' `measure` text closely enough that the two would be plotted on one line; "AI will
cause the end of the human race" and "AI is a threat to the human race" are two series. A
number in a press report is not the record; the source's own page or file is, and the row's
`source_url` is that page. A sample size and fieldwork dates that the public page does not
give are a reason to flag, not to guess. A date the page does not give is taken from the
organiser's own dated post, said in the notes, as the existing event rows do.

## The four verdicts

- **`quiet`**: nothing in the window from this source bears on the record. No source needed.
- **`noted`**: something relevant was published and no row is appended: new wording, a
  publication that measures something adjacent, a release that A21's rule does not admit, a
  forecast that is not the source. `found` says what and why not; `sources` lists what was
  read.
- **`new-row`**: one or more rows appended to `data/world_measures.csv`, `data/aggregates.csv`
  or `data/events.csv`. `new_rows` lists their ids; `sources` lists the record they came from;
  `found` says in a sentence what each row is.
- **`flagged`**: anything the scanner may not do on its own, or anything two readers could
  disagree on: a measurement of a leg that is not the scored series (always, even when its
  rows were appended), a candidate second source for leg C, a change to a named series, a
  source that has closed or changed method, a new item older than the window on the first
  reading, a report or statement whose kind is unclear, a release that may qualify under A21,
  a validation error. `for_john` states what it would have done, the record, and why it
  stopped. A flagged item may also have appended rows; the flag is about what it did not do.

## The reading record

One file per run, `data/readings/YYYY-MM-DD.json`, appended to the folder and never edited; a
second run on the same day is `YYYY-MM-DD-2.json`. JSON rather than CSV because an item holds
lists (search ids, sources, new row ids) and CSV would force them into one cell; JSON rather
than the siblings' TOML because this repository's habit is CSV for tables and JSON for the
rest (`docs/singularity-entry-thresholds.json`, `site/status.json`), and because Python reads
JSON without a version question. The site copies only CSV files to `site/data/`, so the
readings are in the repository and not yet on the site; see decision 12.

    {
      "reading": {
        "date": "2026-10-16",              the Pacific date of the run; also the file name
        "ran_at": "2026-10-17T05:40:00Z",  when it finished, universal time
        "window_start": "2026-10-10",      the seven days ending on the date
        "window_end": "2026-10-16",
        "scope": "monthly",                "weekly", or "monthly" on the first run of a month
        "commit_before": "c79a4d1",        the record the reading read
        "by": "hand",                      "hand" for a run done in a session, "scheduled"
        "items_read": 19,
        "searches": 44,                    distinct search ids across the items
        "new_rows": ["..."],               every row appended, by id
        "flagged": 6
      },
      "items": [
        {
          "id": "leg-a-metr",              a slug, unique in the reading
          "part": "gauges",                "gauges", "institutions" or "events"
          "speaker_id": "metr",            optional; a speaker, "events" or "reading"
          "verdict": "flagged",            quiet, noted, new-row or flagged
          "search_ids": ["reading-2026-10-16-01", "reading-2026-10-16-02"],
          "found": "One to three plain sentences, absolute dates.",
          "sources": ["https://..."],      required for every verdict but quiet
          "new_rows": ["..."],             new-row only: the ids appended
          "for_john": "..."                flagged only: what it would have done, the
                                           record, and why it stopped
        }
      ]
    }

`scripts/validate.py` checks every file in the folder: the name is the date; every field above
is present and well formed; every item has a verdict; at least two search ids unless `quiet`
with a reason in `found`; sources for every verdict but `quiet`; every search id exists in
`data/search_log.csv` and carries the reading's date; every `new_rows` id exists in one of the
three data files; `for_john` on every flagged item; the counts in the header match the
items; and, the other way, every search-log row whose id starts `reading-` belongs to an
item in the reading of that date.

## The procedure, step by step

The standalone instruction is `docs/weekly-reading-prompt.md`; the scheduled task's prompt,
when one exists, only says to open the repository and follow that file. In brief:

0. **Orient.** Pacific date; clean `main` brought up to date; `commit_before`; read this
   file, the definition, the headers of the data files and the latest rows of each series;
   decide the scope.
1. **Part 1**, the four gauges, in order A, B, C, D.
2. **Part 2**, every non-individual speaker, in file order.
3. **Part 3**, events, by kind.
4. **Append rows** for every `new-row`, in the form the file's existing rows use, and run
   `python3 scripts/validate.py` after each file; a row that fails is removed and the item
   becomes `flagged` with the error.
5. **Log every search** in `data/search_log.csv`.
6. **Write the reading record.** `python3 scripts/validate.py` must pass.
7. **Changelog**: this repository has none; `docs/amendments.md` is for changes to the method
   and the reading makes none, so nothing is written there. The commit message is the log.
8. **Publish**: one commit on `main`, one push; the push deploys the site through
   `.github/workflows/deploy.yml`. A refused push falls back to `claude/reading-YYYY-MM-DD`.
9. **Report** to John: flagged items first, then new rows, then counts. No prose.

## The schedule: a proposal

The reading is meant to run once a week without John opening anything. Two slots in this
family are taken: The Upgrade Tree's reading runs on this Mac at 18:00 Pacific on Sundays,
and The Belt Equation's scan runs as a cloud routine (claude.ai/code/routines) on its own
schedule. Running two readings on the Mac at the same hour would have them contend for the
machine and land their reports together.

Proposed: **Monday 06:00 Pacific on this Mac**, so the week's reading is in John's hands with
the Monday digest and after the weekend's releases, and the Upgrade Tree's Sunday report has
had the evening to itself. Alternatives: Sunday 20:00 Pacific on the Mac, directly after the
Upgrade Tree's run, so both land on Sunday night; or a cloud routine with the repository
attached, which runs whether or not the Mac is open (The Belt Equation moved to one on
2026-10-08 after a Mac-scheduled scan landed 39 hours late) but needs the Claude GitHub App on
this repository and cannot be made from a Code session. The choice is John's; no task was
created with this document.

**Ruled 2026-10-16.** John chose the proposed slot. The scheduled task
`agi-zeitgeist-weekly-reading` (the tracker's weekly reading, on this Mac) was created the same
day for Mondays at 06:00 Pacific (the app adds a few minutes' delay), with its prompt pointing
at `docs/weekly-reading-prompt.md`; its first unattended run is 2026-10-19. It runs while the
Claude desktop app is open, and a run missed because the app was closed starts on the next
launch.

**Moved to a cloud routine on John's ruling of 2026-10-18.** The reading now runs as the cloud
routine "AGI Zeitgeist weekly reading" (routine id `trig_01P7b2icKe5hxxtBAmTpDTtq`, at
claude.ai/code/routines), Mondays at 06:00 Pacific as before, with this repository attached; it
runs whether or not the Mac is awake, and its prompt is the same as the Mac task's: open the
repository and follow `docs/weekly-reading-prompt.md`. The Mac task
`agi-zeitgeist-weekly-reading` is kept until the cloud routine's first reading has landed. The
Mac task runs on 2026-10-19; the cloud routine was created switched off on 2026-10-18 so that it
would not also fire that morning, and its first firing is Monday 2026-10-26 at 06:00 Pacific, so
the two never fire in the same week. Once that reading has landed and its record is on `main`,
the Mac task is switched off. As the paragraph above says, a cloud routine needs the Claude
GitHub App on this repository; whether it is installed is shown only by that first run, and
until then it is unconfirmed.

## Decisions, with confidence and alternatives

Per the ground rule of 2026-09-08. All proposed by Claude on 2026-10-16 while building; none
ruled yet unless the line says so.

1. **Three parts, and the panel deferred.** High confidence on the three; moderate on
   deferring the panel, for the two reasons under "Deferred". Alternative: read the panel's
   thirty-seven people weekly from the start, logging statements uncoded. Rejected because
   the collection pipeline would then inherit a partial, newest-first set.
2. **Four verdicts: quiet, noted, new-row, flagged.** High confidence. The siblings' moving
   verdicts (`moved`, `resolved`, `stage-change`) have no counterpart here because the
   scanner moves nothing; `new-row` is the one act it may take. Alternative: a fifth verdict
   `new-series` for a release with new wording. Rejected: new wording is John's to admit, so
   it is `flagged` or `noted`.
3. **A measurement that is not the scored series is recorded if it repeats a series in the
   file, always flagged, never swapped in.** High confidence; it is the hand-made handling of
   2026-10-16 written as a rule, and the definition says changing what scores is an amendment.
   Alternative: never record such measurements, flag only. Rejected because the record is
   also for readers who want to see the disagreement, and a row they can download is worth
   more than a line in a report.
4. **A repeat is appended only with comparable wording, sample size and fieldwork dates.**
   High confidence; it is what every existing `aggregates.csv` row carries, and a row without
   them cannot be compared. Alternative: append with what the page gives and leave `n` blank.
   Rejected: the validator allows a blank `n`, but a poll row without one is a press figure.
5. **AI releases only under amendment A21's rule.** High confidence; the rule exists and is
   mechanical (named in a statement). Alternative: append every frontier release. Rejected
   because "frontier" is a judgment and the record would fill with launches nobody in it
   reacted to.
6. **Two searches as a floor, with a fetch of the source's database counting as one.** High
   confidence; both siblings adopted the floor after their first audits found one-search
   items. Alternative: one fetch is enough for a database-built series. Rejected for the
   first version; the second search is cheap and catches a source announcing a change to its
   series.
7. **Every search in `data/search_log.csv` with a `reading-` prefix and a reserved speaker
   `reading`.** High confidence; the tracker's own rule is that every search is logged, and a
   second log would split the record. Alternative: a `searches` list inside the reading
   record, as the siblings do. Rejected because the siblings have no search log to join.
8. **A JSON record per run, never edited.** Moderate confidence; see "The reading record".
   Alternative: TOML as the siblings, so the three readings share a shape. Worth revisiting if
   a shared reading page across the family is ever built.
9. **Append, never edit; a revision is a new row.** High confidence; it is the tracker's
   existing habit (every row dated and sourced, amendments dated), and it keeps the scanner's
   work auditable by diff. Alternative: let the scanner correct a value it finds revised.
   Rejected: a corrected value with no trace is exactly what the record is built to prevent.
10. **Monthly scope adds leg D and the yearly and one-off series, and nothing else.** Moderate
    confidence. Alternative: no scope at all, read everything weekly. Costs a World Bank fetch
    and two pointless searches a week.
11. **Older items found by chance are appended, except on the first reading.** Moderate
    confidence; a judgment call made on the first reading, when the Ipsos AI Monitor 2026 and
    the State of AI Report 2026 turned up outside the window. Alternative: The Upgrade Tree's
    rule that an older record is always flagged. Rejected because the tracker's rows carry
    their own dates, so there is nothing for the scanner to guess.
12. **No site surface in the first version.** Moderate confidence. The site is written under
    the public-writing rule (no project language) and every page is a design pass; the
    readings are in the repository, and the three-surface pattern (a strip on the home page,
    a "this week's reading" page, each series' last readings) is the next step once four
    readings exist and John has audited them. Alternative: publish the JSON beside the CSV
    files now by extending `copy_data` in `scripts/site.py`. One line; not done because an
    unexplained file on the download page is worse than none.
13. **Monday 06:00 Pacific on the Mac, proposed.** Low confidence; see "The schedule". The
    alternatives are in that section, and the choice is John's. *Ruled 2026-10-16 as proposed;
    moved to a cloud routine in the same slot on John's ruling of 2026-10-18, first firing
    2026-10-26 (see "The schedule").*
14. **The scheduled run writes no worklog entry.** Moderate confidence; The Upgrade Tree
    decided the same on 2026-10-16 (the record is the log, and the Monday digest reads it).
    Alternative: one `progress` entry per run in the AGI Zeitgeist project. Cheap, but
    fifty-two near-identical entries a year would bury the real ones.
15. **A first audit after four readings**, John reading every scanner item to date. High
    confidence; both siblings' first audits changed their procedures.
16. **The scheduler commits on `main` and pushes, with a fallback branch.** High confidence;
    the deploy workflow runs the validator before building, so a bad row cannot reach the
    site, and the siblings do the same. Alternative: a pull request per reading. Costs John a
    merge a week for rows the validator has already checked.

## Deferred, and why

- **The frozen panel's new statements** (part 4): decision 1.
- **A site surface**: decision 12.
- **Online communities, media outlets, Wikipedia and Google Trends monthly**: the streams
  these belong to (methodology sections 5, 6 and 9) have not started, and their series are
  built by database pulls on their own schedule, not by a weekly news reading.
- **The scanner proposing new speakers or new series**: it may flag a candidate (a pollster
  that has begun a repeated AGI item, a second source for leg C); adding one is an amendment.
- **Fetching sources by API beyond the three already built that way** (METR's file,
  Manifold's market, the World Bank's indicator): add a fetch only once a reading has
  demonstrably missed something a fetch would have caught.

## Rulings on flagged items

Each reading's flagged items are John's to rule on. The rulings are recorded here, dated, so a
later reading can tell a settled question from an open one and does not flag it again.

**2026-10-17, on the first reading (2026-10-16), John ruling on the agent's recommendations:**

- *METR's time-horizon series has stopped updating (leg A anchor).* Ruled 2026-10-17 after John
  asked what METR is: ask METR whether a successor suite is planned, and record the question as
  an open amendment (A24) so the page says the gauge is running out. The switch itself waits on
  the answer and is a later amendment. The leg A item adds "Time Horizon 2.0" to its searches.
- *26% by the R&D Automation Index against 51% by the staff poll (leg C).* The index keeps
  scoring; the poll stays beside the gauge, unscored. Recorded under leg C in the definition.
- *Venue AI-disclosure audits as a second source for leg C.* Read the ICLR 2026 audit's results
  before deciding whether it is a second source or only context; a roadmap step, not a reading.
- *Metaculus cannot be fetched without a token.* The row stays with no series; noted on the row.
- *Monmouth's polling institute closed.* Confirmed on the university's own page (ceased
  operations 2025-07-01). The series ends with the 2023 poll; the row says so; not read again.
- *Ipsos AI Monitor 2026 has no public figures.* Read the full report by hand, as the 2024 and
  2025 rows were, and append the rows; a roadmap step, not a reading.
- *The OpenAI-led corporate letter on cyber defence (2026-08-27).* Not the record's kind of open
  letter: a company pledge about defence, not a statement about where AI is going. No row.
- *The White House Accord on Super Intelligence (2026-09-29).* Covered by the executive order's
  row of the same day; a sentence on that row names it. No row of its own (agent's call under
  the ruling).
- *The State of AI Report 2026 (2026-10-08).* Not the record's kind of report: an annual
  investor's survey of the field, not a research report. No row.

Two of these set precedent for later readings: a corporate pledge is not an open letter of the
record's kind, and an annual industry survey is not a report of the record's kind.
