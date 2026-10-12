# Methodology

**The method is now [`methodology-v2.md`](methodology-v2.md)** (2026-09-30), adopted
after two outside reviews. The reasons for every change are in
[`amendments.md`](amendments.md); the coding rules with examples are in
[`codebook.md`](codebook.md).

The version 1 method (one `stance` code, six question frames, the "prominent enough"
panel rule) was written from the kickoff plan the same day and is retired. It remains
readable in git history (this file at commit `1508fde`) and in the method sections of
[`2026-09-30-kickoff.md`](2026-09-30-kickoff.md).

## Points of detail not spelled out in version 2

These come from version 1 and still apply; the agent implementation entry in
`amendments.md` lists the rest.

- **Dataset window:** statements from 2005-01-01 onward.
- **Fixed query set for each panel member** (logged in `data/search_log.csv`):
  discovery queries D1 `"<name>" AGI prediction`, D2 `"<name>" "artificial general
  intelligence"`, D3 `"<name>" "human-level" AI when`; then for every year from the
  first documented year to the present, Y1 `"<name>" AGI <year>`, Y2 `"<name>"
  "human-level" intelligence <year>`, Y3 `"<name>" superintelligence OR singularity OR
  "self-improving" <year>`; plus the person's own outlets. Quiet years are logged as
  rows with what_found "quiet year: no qualifying statement found".
- **Busy years:** more than ten qualifying statements → keep every timeline-bearing one,
  sample the rest at every third by date, tag `sampled`, log the sampling.
- **events.csv** fields: event_id, date, date_precision, event_type (`open_letter`,
  `public_statement`, `government_action`, `report`), title, description, source_url,
  notes. Epoch AI reports are `report` events. Searches behind it use speaker_id
  `events` in the search log.
- **aggregates.csv** holds the survey, market and poll rows collected in the seed. Under
  version 2 section 4, population survey items move to `data/surveys.csv` when the
  population stream starts; that move has not been made yet.
- **National outlet** (for the panel prominence test): a national newspaper,
  broadcaster, news agency or national magazine, including science and technology
  magazines such as Wired and New Scientist; not blogs, newsletters, trade press or the
  person's own outlets.
- **Frontier lab tie:** `frontier_lab_tie` is `yes` when the person led or ran a
  company building the most capable models of the time during any statement in the
  record; the years are given in `role_summary`.

### Practices adopted after the panel collection (ruled by John 2026-10-12, amendment A23)

The full collection for the frozen panel (pull request 4, October 2026) had to decide ten
points the method said nothing about, and departed from it on one. John ruled on
2026-10-12 that each practice below is the method from now on.

- **Start year for the 2020s group** (ruled by John 2026-10-12). The yearly searches for a
  2020s-group member start at the first year of any public comment by that person on AI,
  never before 2005. Each choice is logged as a `start year` row in `data/search_log.csv`.
  Core members are searched from 2005, the start of the dataset window, whatever their
  first documented year; that searches more years than "from the first documented year"
  above asks for, never fewer, and is accepted as a departure from that line.
- **Coder label** (ruled by John 2026-10-12). Rows coded during the collection carry
  `coder: claude-agent-v2.1`, the label the codebook gives to rows coded under the A14
  rulings, since those rulings are part of the rules the collection coded by.
- **"Probably", "likely" and "perhaps"** (ruled by John 2026-10-12). A position resting
  on one of these words is coded `accepts` with `ambiguous: yes` (field: endorsement),
  unless "may", "might" or "could" governs the same claim, which makes it `uncertain`.
  The rule is in the codebook, section 3.
- **A reporter's paraphrase in the reporter's own interview** (ruled by John
  2026-10-12). Words inside quotation marks are primary; the reporter's paraphrase of what
  the speaker said is secondhand, even when the reporter did the interview.
- **Reading through a reader service or an archive** (ruled by John 2026-10-12). Text
  read through a reader service (the r.jina.ai reader), the Wayback Machine, X's embed
  services, the PullPush Reddit archive or a third-party transcript site (spoken.md, The
  Singju Post, Thread Reader) counts as read at the source when it is the source's own
  text. Each row's notes say which route was used.
- **Statements found later for a year already logged** (ruled by John 2026-10-12). When a
  statement arrives after a member's trace is done (for example one found while tracing
  someone else), the quiet-year row for that year is corrected to say the year is not
  quiet and to name the statement, and the busy-year count for that year is redone with
  the new row.
- **Where the every-third count starts** (ruled by John 2026-10-12). In a busy year, the
  every-third sample of statements without a timeline is counted from the first such
  statement by date, so the first one is kept.
- **The self-improvement level** (ruled by John 2026-10-12). Amendment A14 ruling 12
  governs, with its reading: "the lowest level the words support" means `si_assist` when
  the words say nothing about who does the improving, and `si_modify` when the words say
  the AI improves itself. A rejection or doubt of runaway growth keeps the level the
  speaker is rejecting. Codebook section 1 has the rule and examples.
- **Date of an interview published later** (ruled by John 2026-10-12). An interview
  recorded well before it was published is dated at publication (for example Cotra's
  80,000 Hours episode, recorded 2025-10-20 and published 2026-02-17).
- **Co-written documents** (ruled by John 2026-10-12). A document with more than one panel
  author is recorded once for each panel author (for example the 2023 Superalignment post
  for both Leike and Sutskever; the 2016 AI100 report for both Brynjolfsson and Brooks).
