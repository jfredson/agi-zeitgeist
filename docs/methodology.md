# Methodology

Status: written 2026-09-30 from the kickoff plan (`docs/2026-09-30-kickoff.md`). The
method is frozen from this date. Changes go in `docs/amendments.md` with a date and a
reason; this file is then updated and the amendment cited.

## 1. What is being measured

How expert and public opinion about artificial general intelligence (AGI: AI that can
do most intellectual work a person can) has moved from 2005 to the present.

The working hypothesis to test is that the main public question moved in three steps:
*whether* AGI is possible (about 2005 to 2015), *when* it will arrive (about 2016 to
2022), and *whether today's systems are already close or able to improve themselves*
(since about 2023). The method is built so the data can contradict this. If the shift
turns out smaller, earlier, or confined to one group, that is the finding.

The dataset covers statements made from 2005-01-01 onward. Earlier statements are out
of scope even when a speaker's record goes back further; they may be mentioned in
`notes` as context.

## 2. The files

All data is plain CSV (comma-separated, UTF-8, with a header row) in `data/`.

### speakers.csv: one row per person or source

| field | meaning |
|---|---|
| speaker_id | short lowercase slug, e.g. `hinton` |
| name | full name |
| speaker_type | `individual`, `survey`, `prediction_market`, `institution`, `poll` |
| role_summary | what they do, in one line |
| frontier_lab_tie | `yes` or `no`; see section 6 |
| panel_tier | `core` or `cohort_2020s` for individuals; blank for surveys, markets, institutions and polls |
| inclusion_note | why they are in, with the earliest and latest documented statement dates |

### statements.csv: one row per public statement

Fields as in the kickoff plan: `statement_id`, `speaker_id`, `date`, `date_precision`,
`source_url`, `source_type`, `quote`, `claim_summary`, `question_frame`,
`timeline_type`, `timeline_year`, `timeline_year_high`, `timeline_prob`,
`timeline_text`, `definition_note`, `stance`, `coding_confidence`, `coder`,
`retrieved`, `notes`. Allowed values and how to choose them are in
`docs/codebook.md`.

`statement_id` is `<speaker_id>-<year>-<NN>`, numbered from 01 in date order within a
speaker and year. `source_type` is one of `interview`, `talk`, `paper`, `blog`,
`podcast`, `social_post`, `book`, `survey_response`, `testimony`.

### aggregates.csv: one row per survey result, market reading or poll result

| field | meaning |
|---|---|
| aggregate_id | e.g. `aiimpacts-2023`; add a suffix when one source gives several numbers |
| speaker_id | the survey, market or pollster, in speakers.csv |
| date | when the survey ran or the market was read (form as for statements: `YYYY`, `YYYY-MM` or `YYYY-MM-DD`) |
| measure | what was measured, in plain words |
| value | the number |
| unit | `year`, `probability`, `percent_of_respondents`, `index` |
| n | sample size, if any |
| source_url | link |
| notes | the exact definition and question wording, response rate, anything that affects comparison |

### events.csv: dated events for chart labels

The plan asks for this file but does not list its fields. These are set here:

| field | meaning |
|---|---|
| event_id | short slug with year, e.g. `cais-statement-2023` |
| date | ISO date |
| date_precision | `day`, `month` or `year` |
| event_type | `open_letter`, `public_statement`, `government_action`, `report` |
| title | short name for a chart label |
| description | one or two plain sentences on what happened |
| source_url | link to the primary document |
| notes | exact wording of the key sentence where there is one; anything else |

Reports from Epoch AI (a research group that tracks computing power and AI
capability trends) go here as `report` events rather than in `aggregates.csv`. The
plan treats them as context rather than opinion, and their units (growth per year)
don't fit the aggregate units.

### search_log.csv: one row per search

| field | meaning |
|---|---|
| search_id | `<speaker_id>-<NNN>`, numbered in the order the searches were run |
| speaker_id | who or what the search was for |
| year | the year being searched, or blank for searches across the whole span |
| query | the exact query text |
| where_searched | the tool or site, e.g. `web search`, `garymarcus.substack.com archive`, `archive.org` |
| what_found | what came back that mattered: the statement ids recorded from it, "nothing qualifying", or a note on sampling |
| date_searched | ISO date |

A search is logged before any statement found through it is recorded.

## 3. Sampling rule (the defence against picking quotes that fit)

1. For each panel member, search year by year from their first documented statement
   (no earlier than 2005) to the present, using the fixed query set in section 4,
   and log every search in `data/search_log.csv`.
2. Collect **every** statement that gives a timeline, or answers the `possibility`,
   `capability_now` or `self_improvement` question. Do not skip ones that cut against
   the pattern. Once collected, a statement is coded with the frame it leads with,
   which may be `post_agi` or `definition`.
3. When a speaker made more than ten qualifying statements in one year, keep all that
   give a timeline and sample the rest at a fixed interval (every third, by date).
   Record the sampling in the search log and tag kept rows `sampled`.
4. Statements by another panel member found while searching for someone else are
   still recorded and tagged `incidental`.
5. Panel membership is frozen before collection starts. Adding or removing someone
   later needs a dated amendment in `docs/amendments.md` saying why.

**A known bias from rule 2.** Statements purely about risk, the economy or the meaning
of the word, with no timing and no answer to the collected questions, are not
collected. The `post_agi` and `definition` shares are therefore lower bounds. They
show when those questions came up alongside timing or possibility, not how often
they came up overall.

## 4. Fixed query set

Run with a general web search tool. Searching the speaker's own outlets (blog, social
media archive, books) is logged as a separate search.

**Discovery (once per speaker, `year` blank):**

- D1 `"<name>" AGI prediction`
- D2 `"<name>" "artificial general intelligence"`
- D3 `"<name>" "human-level" AI when`

**Year by year (every year from the first documented year to 2026):**

- Y1 `"<name>" AGI <year>`
- Y2 `"<name>" "human-level" intelligence <year>`
- Y3 `"<name>" superintelligence OR singularity OR "self-improving" <year>`

**Speaker's own outlets (once each, `year` blank):** each speaker's blog or newsletter
archive, books published in the window, and a search of their social media account
where it can be searched. The outlets searched are listed in the search log.

Follow-up searches (to find the original source of a quote found secondhand, or to
check a date) are logged too, with a short query description.

## 5. Panel inclusion rule

**Core panel:** a named person with sustained public commentary on whether or when
AGI arrives, with at least one documented statement on or before 2017 and at least
one in 2024 or later, prominent enough that their view shaped public discussion (not
just expert circles). Target 15 to 20 people, balanced across optimists, skeptics and
safety-focused thinkers.

**2020s cohort:** people who became central after 2020 and have no early record.
Tracked separately so that their arrival shows up in the data rather than being
blended into the core series.

The candidate list and the evidence for each candidate are in
`docs/panel-verification-2026-10.md`. The panel is frozen by John. During the seed
phase only the five seed speakers are in `speakers.csv`.

## 6. Frontier lab ties

`frontier_lab_tie` is `yes` when the person led or ran a company building frontier
AI models (the most capable models of their time) at the time of **any** statement in
the record. The years the tie held are written in `role_summary`, so a reader can see
which statements it applies to. Recorded because readers will ask about incentives.

The plan defines this field per statement time, but it sits in a per-speaker table.
Writing the years in `role_summary` is the stop-gap. If the charts need it per
statement, an amendment can add a column to `statements.csv`.

## 7. Aggregates

- Every figure is checked against its primary source (the paper, the survey report,
  the market's own page or data) before entry. Figures in the kickoff plan were from
  memory.
- `notes` carries the exact definition and the question wording. "Worried about AI"
  is not "expects AGI", and survey definitions of human-level AI differ.
- Prediction markets are recorded at yearly intervals where a history can be
  retrieved. Where it can't, what can be retrieved is recorded, and `notes` says what
  is missing.

## 8. Coding and agreement

Coding follows `docs/codebook.md`. Each row records its `coder`.

**Pass check before scaling to the full panel** (from the plan): the five seed traces
produce at least 60 statements with working sources; two independent codings of two
of the five speakers agree on `question_frame` and `stance` at least 80% of the time;
and the codes do not all land in one bucket. If agreement is low, the codebook is
revised and the five are recoded before anyone else is collected.

## 9. Checks

`scripts/validate.py` runs on every change. It fails on any row with an invalid code,
a badly formed date, a missing source, a `speaker_id` not in `speakers.csv`, a
duplicate id, a quote over 60 words, or a secondhand row not marked low confidence.
