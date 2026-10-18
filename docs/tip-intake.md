# Tip intake: how a statement John comes across enters the record

Written 2026-10-18. Status: **PROPOSED**, pending John's rulings on the three open decisions
at the end and the amendment draft in `docs/amendments/2026-10-18-tip-intake.md`. Until he
rules, nothing here changes what the collection or the weekly reading may do.

It answers a question John asked on 2026-10-18, after sending a link to Nick Bostrom's
interview on The Roman Forum (published 2026-10-16): when a prominent figure is heard
discussing exactly the questions the tracker asks, what place does that have in the project,
and how is it handled the same way every time?

## The idea in one paragraph

A tip is evidence only if the project's own rule would have found it. So a tip never adds a
statement the fixed queries would miss; it only gets a statement into the record sooner, with
its source archived and checksummed. Each tip goes through the same steps whoever sends it:
archive the primary source, check who is speaking against the frozen panel, run that person's
logged queries to see whether the rule finds the source, extract the candidate statements,
and hand them to coding under the codebook like any collected row. Separately, and only as a
draft, it can produce a short dated "panel watch" note for Sentient Horizons' social channels.
The data step and the commentary step never feed each other: a note can cite a row, but a row
never exists because a note wanted one.

## One procedure, two triggers

The weekly reading already reserves part 4 for the frozen panel's new statements, deferred
until full collection lands, with the job to "find and log the statement and leave coding to
the collection pipeline" (`docs/weekly-reading.md`, "Deferred"). Tip intake is that job with a
different trigger: John sends a link instead of a schedule finding it. When part 4 goes live
it follows this file for every item it finds, so there is one way in for a panel statement
found between full passes, not two.

Trigger cues for a session: `zeitgeist:` followed by a link, or "log this for the zeitgeist
tracker", or a link to a panel member speaking about AI's future sent with a request to save it.

## Steps

### 1. Get the primary source and archive it

- The words, not a summary. For video, pull the transcript with
  `sentient-horizons/ops/scripts/yt_transcript.py` and its recovery ladder; when YouTube blocks
  the shell, the player route worked on 2026-10-18 (in the browser pane, capture the caption
  file the player itself loads; the transcript panel and a direct refetch both came back empty).
  For text, the page as published, with its date.
- Save it under `sources/<kind>/<published-date>-<speaker>-<outlet>-<id>.md` with a header:
  title, outlet, speakers, panel speaker id, URL, published date, duration or length, retrieved
  date, and how the text was obtained (machine captions, publisher transcript, page text).
- Add one line to `sources/manifest.csv` (`path,url,published,retrieved,sha256,obtained_by`).
  This meets methodology section 10's "snapshots with checksums where the source permits".
- Machine captions are not quotes. Any quote taken from them is checked against the audio at
  its timestamp before it goes in a row. A quote that cannot be checked goes in with
  `coding_confidence` no higher than `medium` and the notes tag `asr_unverified`.

### 2. Who is speaking?

Check `data/speakers.csv`:

- **Core panel or 2020s cohort:** go on.
- **Wide list:** go on only if the person has no row yet for the era the statement falls in
  (light capture is one statement per person per era, methodology section 3).
- **Not on any tier:** do not code. Add the person, the source and the date to
  `docs/panel-candidates.md` for the next panel review (a panel change needs an amendment,
  A18). The source is still archived.

### 3. Would the rule have found it?

Run the person's fixed year queries for the statement's year (Y1 `"<name>" AGI <year>`,
Y2 `"<name>" "human-level" intelligence <year>`, Y3 `"<name>" superintelligence OR
singularity OR "self-improving" <year>`) plus a check of their own outlets, as the collection
does. Log every search in `data/search_log.csv` with ids continuing the person's series.

- **The rule finds it** (the source, or a report of the same appearance, is in the results):
  rows are ordinary rows. Notes start with `tip`.
- **The rule does not find it:** rows go in with the notes tags `tip; tip_only`. Under open
  decision 1 they are kept in the record but left out of every figure and every share.

### 4. Extract the candidate statements

Read the whole source. A candidate is any passage that bears on possibility, timing, present
capability, self-improvement or consequences, under codebook section 0's unit rule and
amendment A15's one-row-per-capability rule. Section 3's busy-year rule applies to the
person's year as a whole, and amendment A26 keeps every statement on the "now" question.
Skip the cold-open montage of an episode when it repeats passages from the body; code the
passage where it is said in full.

### 5. Code them the way the collection codes

Same codebook, same coder label and same agreement procedure as the full collection that
produced the person's other rows. A tip is not coded by a lighter process because it arrived
by hand. Where the person already has rows, write one line in the notes saying how the new
statement compares with their latest row on the same question, quoting both ids. That is the
within-person comparison methodology section 3 reports separately.

### 6. Draft the panel watch note (optional, drafts only)

A short dated note for Sentient Horizons' social channels, saved to
`docs/panel-watch/<date>-<speaker>.md`: who the person is in one line, what they said (one
quote under fifteen words, attributed, with timestamp), how it compares with their earlier
rows, and a link to the tracker. Rules:

- It cites rows that exist; it never claims more than the rows show.
- A `tip_only` row can be the subject of a note, labelled as outside the measured record.
- It passes the Voice Calibration Protocol as the final gate, like all public writing.
- Once the Sentient Horizons Outreach process is ratified (`outreach/` in the
  sentient-horizons repository, proposed 2026-10-17), a note is posted as one of its trials:
  stated before posting, with what came back recorded there.
- Claude drafts; John edits and posts. Nothing is posted automatically.

### 7. Hand over

One commit (or pull request) per tip: the archived source line in the manifest, the search
log rows, the statement rows, and the draft note if any. The reply to John is a short list of
what he needs to rule on or post, and nothing else.

## Open decisions for John

1. **Rows the rule would not have found.** Recommended: keep them, tagged `tip_only`, left out
   of figures and shares, listed on the site's changelog as "noted, outside the measured
   record". Alternative: code them as ordinary rows. Confidence: high. Without the exclusion,
   John's own feed becomes a sampling frame, and it leans toward whatever the enthusiast
   venues are amplifying, which is the bias the vanguard sub-series is kept apart for.
2. **Archived transcripts in a public repository.** Recommended: keep the files local (add
   `sources/*/` to `.gitignore`) and commit only `sources/manifest.csv`, so a reader can see
   what was archived, when, and its checksum, without the repository republishing a full
   transcript of someone else's interview. Alternative: commit the files. Confidence: medium.
3. **Where panel watch notes live.** Recommended: drafts here, in `docs/panel-watch/`, next to
   the rows they cite, with the posting record kept by the Outreach process once it is
   ratified. Alternative: draft them in the Outreach folder from the start. Confidence: medium.
