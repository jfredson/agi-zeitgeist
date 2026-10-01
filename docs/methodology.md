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
