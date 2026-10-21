# The weekly reading: the standalone instruction for the scheduled run

Written 2026-10-16. A fresh Claude session with no memory of any earlier conversation follows
this file from top to bottom. The scheduled task's own prompt, when one exists, only says to
open the repository and follow this file, so the procedure can change without touching the
task. When this file and `docs/weekly-reading.md` disagree, this file wins for the run and the
disagreement is a flag for me. Modelled on The Upgrade Tree's `docs/weekly-reading-prompt.md`
and The Belt Equation's `docs/scan-procedure.md`.

## 0. Orient

- Get the date in my time zone before anything else: `TZ=America/Los_Angeles date +%F`.
  That is the reading's `date`; every date you write is absolute (YYYY-MM-DD), never "today".
  The window is the seven days ending on that date: `window_start` is six days earlier.
- The repository is `/Users/john/Code/agi-zeitgeist` when you run on my Mac (the scheduled
  task), or a fresh clone of `https://github.com/jfredson/agi-zeitgeist` in a cloud workspace.
  On the Mac, do not work in any folder under `.claude/worktrees/`; those belong to my own
  sessions.
- Bring `main` up to date before anything else, in one command: `git fetch origin && git
  checkout -B main origin/main`. If the working tree has uncommitted changes that are not
  yours, stop: put the situation in the report and do not touch them.
- Record `git rev-parse --short HEAD` as `commit_before`.
- Read `docs/weekly-reading.md` (what you may and may not do, and the rule that a measurement
  is not the series), `docs/singularity-entry-definition.md` section 2 (the four legs and the
  source each names), the header line of every file under `data/`, and this file.
- Scope: if no file in `data/readings/` is dated this calendar month, scope is `monthly`;
  otherwise `weekly`. A monthly reading adds leg D, Google Trends and Müller and Bostrom.
- List what you will read, with the latest row of each series, so a repeat can be recognised:

      python3 -c "
      import csv, collections
      sp = [r for r in csv.DictReader(open('data/speakers.csv')) if r['speaker_type'] != 'individual']
      print('PART 2:'); [print(' ', r['speaker_id'], '|', r['speaker_type'], '|', r['name']) for r in sp]
      for f in ('aggregates.csv', 'world_measures.csv'):
          latest = {}
          for r in csv.DictReader(open('data/' + f)):
              k = (r['speaker_id'], r['measure']); latest[k] = max(latest.get(k, ''), r['date'])
          print(f.upper()); [print(' ', k[0], '|', k[1][:90], '| latest', d) for k, d in sorted(latest.items())]
      ev = list(csv.DictReader(open('data/events.csv'))); print('EVENTS: latest', max(r['date'] for r in ev), '| kinds', sorted({r['event_type'] for r in ev}))
      "

- Keep a running list of every search and fetch as you go (the query or address, what it was
  for, the one-line result); step 5 writes them to the search log, numbered in the order run.

## 1. Part 1: the four gauges

Read each leg's named source, and only that source counts as a reading of the gauge.

1. **Leg A (pace), METR.** Fetch `https://metr.org/assets/benchmark_results_1_1.yaml` and
   compare the model keys under `results:` with the "Model key in the file" phrases in the
   notes of the METR rows of `data/world_measures.csv`. A model in the file and not in the
   record is a `new-row`: date is METR's `release_date`, value is `p50_horizon_length.estimate`
   in minutes, and the notes follow the existing rows word for word (model key, 95% interval,
   frontier flag from `is_sota`, the standing definition sentence, retrieval date). Also fetch
   `https://metr.org/time-horizons/` and run one web search for a new release of the series or a
   successor suite (search terms: "METR time horizon 2.0", "Time Horizon 1.2"; added 2026-10-17
   under amendment A24, which records that the series has stopped updating, so do not flag that
   fact again, only a new version, a retired page or a changed fit); a change to the series
   itself is `flagged`, since the successor rule is an amendment.
2. **Leg B (forecasts).** Two web searches for new forecast-versus-outcome material about AI
   progress (a scored set of forecasts, a retrospective on a timeline prediction, a change in a
   consensus arrival date). The leg is unmeasured until the forecast ledger exists, so the
   verdict is `quiet` or `noted`; a candidate measure for the ledger is `flagged`.
3. **Leg C (AI doing the improving).** Three reads, each its own item.
   - The R&D Automation Index: fetch
     `https://www.anthropic.com/institute/measuring-pace-of-ai-development` and one web search
     for an update. A new month's "leads" share is a `new-row` on the scored series, id
     `anthropic_institute-YYYY-MM-rd-leads`, notes as the existing rows.
   - Other Anthropic Institute publications: two web searches (one limited to anthropic.com).
     A new measurement of AI's share of AI work that is not the index is recorded as a row if
     it repeats a series already in `data/world_measures.csv` or `data/aggregates.csv`, and is
     `flagged` in every case, with the scored figure and the new one side by side in
     `for_john`. Never give such a row an id ending `-rd-leads`.
   - Outside measures: two web searches for researcher surveys of AI's share of frontier
     research work and for venue AI-contribution disclosure statistics. Nothing is appended;
     a candidate second source for leg C is `flagged` with what it measures and how often.
4. **Leg D (the economy), World Bank. Monthly scope only.** Fetch
   `https://api.worldbank.org/v2/country/WLD/indicator/NY.GDP.MKTP.KD.ZG?format=json&per_page=10&date=2022:2030`
   and compare each year's value, rounded to two decimals, with the record's
   `worldbank-gdp-growth-YYYY` rows, and the response's `lastupdated` stamp with the one in the
   latest row's notes. A new year is a `new-row`; a changed value is a `new-row` with id
   `worldbank-gdp-growth-YYYY-rev-<reading date>` and the revision said in the notes (the old
   row stays); a new stamp with unchanged values is `noted`. One web search for the release
   itself. On a weekly scope, skip the leg and write no item for it.

## 2. Part 2: every institution in the record

For every speaker in the step 0 list, in file order, except METR, the Anthropic Institute and
the World Bank (read in part 1) and except Monmouth (its polling institute closed on 2025-07-01;
ruled 2026-10-17, see "Rulings on flagged items" in `docs/weekly-reading.md`, which also lists
the kinds of document I have ruled out, so they are not flagged again):

1. Compose one or two web searches for releases in the window, from the speaker's `name` and
   the `measure` text of its series in `data/aggregates.csv`; where the record was built by a
   fetch (Manifold: `https://api.manifold.markets/v0/market/hh2bXhwKDTioZ7KtGKfC`; Metaculus:
   the question page), the fetch is one of the two. Two is a floor for any item that is
   searched at all. Google Trends and Müller and Bostrom are read on the monthly scope only and
   may be `quiet` with that reason and no search.
2. Read what came out against the series' `measure` text. A repeat is appended as a `new-row`
   only when the wording is comparable (the two would be plotted on one line), the sample
   size and the fieldwork dates are on the source's own page, and the source's own page is the
   `source_url`. Follow the id pattern and the notes form of the series' existing rows
   (quote the question, say what the value is a share of, name the fieldwork dates). A Manifold
   reading's `date` is the reading date, `n` is the market's unique trader count, and the notes
   name the time of the last trade.
3. Give one verdict: `quiet`, `noted` (a release with new wording or adjacent subject; a repeat
   whose sample size or fieldwork dates are missing, if a later page may give them),
   `new-row`, or `flagged` (a source that has closed or changed method; a repeat the record
   missed that is older than the window, on the first reading; anything two readers could
   disagree on).
4. Google (`google`, code-share statements): one or two web searches for a new statement by the
   company's chief executive on the share of its new code written by AI. A new figure is a
   `new-row` in `data/world_measures.csv` in the existing row's form; it is never scored.

## 3. Part 3: events

For each kind in `data/events.csv` (`open_letter` and `public_statement` together,
`government_action`, `report`, `ai_release`), two or more web searches for the window, read
against the primary record. One item per kind.

- An open letter, statement, government action or report dated inside the window on its own
  record is a `new-row`: `event_id` a slug ending in the year, `date` at the precision the
  record gives, the key sentence quoted in `notes` with the signer count at retrieval, and the
  primary page as `source_url`, as the existing rows do. A date the page does not give is
  taken from the organiser's own dated post and said in the notes.
- An AI release is a `new-row` only when the system is named in at least one statement in
  `data/statements.csv` (amendment A21): `grep -i "<name>" data/statements.csv`. Otherwise
  `noted`, naming the release.
- Whether a report or statement is of the record's kind is read strictly. When two readers
  could disagree (an industry report, a corporate pledge, an announcement rather than an
  action), it is `flagged`, not added.
- A `flagged` item opens the primary page that would settle it before it is written up (for a
  bill, the legislature's own register, such as congress.gov; for an organisation's figure, its
  own page), so the question put to me rests on the record, not on a news report. Added
  2026-10-19 after the audit of the first cloud reading (`docs/readings/audit-2026-10-19.md`).
- A bill counts as a `government_action` only when it has passed a chamber of a legislature or
  become law, dated from the legislature's own record; an introduced bill is `noted` (ruled by
  me 2026-10-19).
- An aggregator page is never the cited source for a date. For an AI release or any dated
  event, the date comes from the maker's or the institution's own announcement; an aggregator
  may point the way. Added 2026-10-19, same audit.

Search economy: no fewer than two searches per item that is searched, no more than four, plus
the fetches a candidate row needs. If a search tool fails twice, mark the item `quiet` with
`found` saying the search was unavailable and move on.

## 3b. Part 4: every person on the panel

Added 2026-10-21 under amendment A32 (my ruling of that day: every tip counts, and every other
person gets "ample search time" so that what I happen to read does not decide who is heard).
Every week, every person with tier `core` or `cohort_2020s` in `data/speakers.csv` (37 people),
and the three industry leaders with tier `claims_only`, is searched for new words. One item per
person, `part` `"panel"`, `speaker_id` the person.

**The searches, for each person** (the year is the reading's year):

1. Y1 `"<name>" AGI <year>`
2. Y2 `"<name>" "human-level" intelligence <year>`
3. Y3 `"<name>" superintelligence OR singularity OR "self-improving" <year>`
4. One recent-news search: `"<name>" AI` restricted to the past week where the search tool allows
   it, otherwise with the month and year added.
5. Their own outlets: the blog, newsletter, site or channel their earlier search-log rows list as
   "own outlet" (`grep -i "own outlet" data/search_log.csv | grep "^<speaker_id>"`), fetched. A
   person with none listed gets one search for a personal site or newsletter, and `found` says so.
6. Every search in `data/added_searches.csv`, in file order, with `<name>` and `<year>` filled in:
   searches added because the regular searches missed a tip, run for every person from the week
   after they were added (amendment A32, item 4). Name the added search in `what_found` (for
   example "Y4: ...").

Up to two more fetches per person to read a candidate. Log every one in step 5 with
`speaker_id` the person and `year` the reading's year, exactly as a full pass logs them; this is
what `scripts/panel_status.py` reads to say through what date each person was searched.

**Keep the run within one session.** Hand the people to subagents in batches of about eight, in
file order, each batch told to run the five searches per person and return, for every search,
the query, where it ran and a one-line result, plus any candidate: a source (address, date,
speaker) where the person speaks about AI's possibility, timing, present capability,
self-improvement or consequences. The subagents do not write files. You log and decide.

**What is new.** A candidate is new if its address is not already in `data/statements.csv`
(`source_url`) or in the search log, and it is dated inside the window, or after the person's
latest row and not more than a year old. Anything older is `noted`.

**Verdicts.**

- `quiet`: nothing new.
- `noted`: something new that is not a statement of the record's kind, or older material.
- `new-row`: a new statement, taken in by `docs/tip-intake.md` steps 1, 2, 4 and 5 (archive the
  source with its checksum in `sources/manifest.csv`, check the tier, extract the candidates,
  code them under the codebook, then have a separate subagent code the same passages blind from
  the codebook and the source and record any disagreement in the notes, as tip intake does).
  These rows are found by the rule's own searches, so they are not tips: notes say
  `found by the weekly reading of YYYY-MM-DD` and the search ids. Append to
  `data/statements.csv` and run the validator, as in step 4.
- `flagged`: a new statement you cannot take in as the rules require: the words cannot be got
  (no transcript, a paywall, a page that refuses), the year is a busy year for the person
  (methodology section 3) and the sampling is not clear, or two readings are possible. Also every
  new dated forecast by one of the fifteen industry leaders, `for_john` naming the source, so a
  session can add it to the claims ledger under `docs/claims-ledger-method.md`. The reading never
  writes a claim file.

**Then run `python3 scripts/panel_status.py`.** It prints the date through which every panel
member has been searched, anyone overdue (not searched in the last eight days), and how tips are
spread across people. Both go in the report (step 9).

## 4. Append the rows

For every `new-row`, append the row to the end of the file (`data/world_measures.csv`,
`data/aggregates.csv`, `data/events.csv`, or for part 4 `data/statements.csv`), quoting fields with commas as the file does, in
the form of the existing rows of that series; part 4's statements go to
`data/statements.csv` in the form of the person's existing rows. Say in `notes` that the row was appended by the
weekly reading of YYYY-MM-DD and name the search ids it rests on. Run `python3
scripts/validate.py` after each file. If it fails on your row, remove the row, mark the item
`flagged` with the error in `for_john`, and continue. Never edit any existing row. Never touch
`docs/singularity-entry-thresholds.json`, `docs/singularity-entry-definition.md`,
`docs/codebook.md`, `docs/methodology-v2.md`, `docs/amendments.md` or `data/speakers.csv`.

## 5. Log every search

Append one row per search or fetch to `data/search_log.csv`, in the order run:
`search_id` = `reading-YYYY-MM-DD-NN` (two-digit counter from 01); `speaker_id` = the speaker
it was for (in part 4, the panel member), `events` for part 3, or `reading` for leg B and leg C's outside measures; `year` =
the year searched for (the reading's year) or blank; `query` = the search as typed, or the
address fetched with "(fetch)"; `where_searched` = the search engine or the site;
`what_found` = one line; `date_searched` = the reading's date.

## 6. Write the reading record

Write `data/readings/YYYY-MM-DD.json` exactly in the shape given in `docs/weekly-reading.md`
under "The reading record": a `reading` object with `date`, `ran_at` (universal time, from
`date -u +%Y-%m-%dT%H:%M:%SZ`), `window_start`, `window_end`, `scope`, `commit_before`,
`by` (`"scheduled"`; `"hand"` for a run done in a session), `items_read`, `searches` (distinct
search ids), `new_rows` (every id appended) and `flagged` (count); then `items`, one per read
target in the order read, each with `id`, `part`, `speaker_id` where there is one, `verdict`,
`search_ids`, `found` (one to three plain sentences, absolute dates), `sources` for every
verdict but `quiet`, `new_rows` on a `new-row`, `for_john` on a `flagged`. If the folder
already has a file with the date, suffix `-2`. Then run `python3 scripts/validate.py`; it must
pass. If it refuses the record, fix the record, not the rule.

## 7. Changelog

This repository has no changelog, and `docs/amendments.md` is for changes to the method. Write
nothing there. The commit message is the log.

## 8. Publish

The site rebuild recomputes the headline (the average share of the way with the slowest part
named, and the on-current-trends crossing sentence; amendment A25) from the rows, so nothing is
written for them by hand. A new row that moves a leg's share by five points or more, or changes
which leg is slowest, or changes a crossing year, is a line in the report.

One commit, one push:

    python3 scripts/validate.py && git add -A && git commit -m "YYYY-MM-DD: weekly reading, N read, M rows appended, F flagged" -m "<one line per row appended, by id; or 'No rows appended.'>" -m "<the attribution lines this session was given>" && git push origin main

The commit-message hook refuses dates that are not year-month-day; write them that way. A
refused push: push the same commit once to `claude/reading-YYYY-MM-DD` and say so in the
report; the site does not update until I merge it. If that push is refused too, do not
retry: put the reading record's contents in the report and stop. Never force-push, never
rebase, never touch any other branch. The deploy workflow on GitHub runs the validator, builds
and deploys the site from the push to `main`; do not deploy by any other road.

## 9. Report

Send me one short message, a numbered list and nothing else: each flagged item with its
`for_john` line, first; then one line per row appended, with its id and what it is; then one
line with the counts (items read, searches, verdicts); then the two lines from
`scripts/panel_status.py`: the date through which every panel member was searched, with anyone
overdue named (a comparison of people is not shared while anyone in it is overdue), and the
spread of tips across people; then the push refusal if there was one.
No prose, no summary of quiet items. Do not write a worklog entry.

## Standing rules

- Plain language, absolute dates, commas rather than dashes, every id with a plain phrase
  beside it.
- Read, do not infer: a row is appended on the source's own record, not on a press figure.
- Append, never edit. A revision is a new row; a disagreement is a flag.
- Nothing the reading finds changes what is scored. The thresholds file, the definition, the
  codebook, the amendments and the speakers file are not yours.
- One reading, one commit, on `main` (and the one fallback branch in step 8).
- If anything in this file cannot be followed as written, do the parts that can, flag the rest
  for me in the report, and never improvise an edit outside the limits in
  `docs/weekly-reading.md`.
