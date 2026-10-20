# Amendment: vanguard sub-series of stream F

Status: **ACCEPTED by me, 2026-10-02**, with his rulings on the seven open questions
applied. Drafted by me 2026-10-02 (original in git history, commit `d3a1e19`); reviewed
by Gemini 3.1 Pro and GPT-6 Astra Medium (verbatim in `docs/reviews/vanguard-stream-review-*.md`,
prompt `docs/reviews/vanguard-stream-review-prompt.md`); reconciled 2026-10-02 (commit
`d7482b2`).
Applies to: `docs/methodology-v2.md` section 6 (stream F), `docs/amendments.md` (log entry).

**Collection status:** only the retrievability check in section 5 may run. Nothing else is
collected until I have seen its result.

## 1. Purpose

Record how highly ranked posts in a fixed set of AI-enthusiast venues frame AI progress
over time: which capabilities are treated as already achieved, under way or near, and in
what terms. The construct is **framing in selected venues**. It is not a measure of what
people in general believe, nor of what the venues' members believe.

The idea that these venues move "earlier and further" than the panel or the public is a
**hypothesis**. The phrase "leading indicator" appears only in the essay, labelled as a
hypothesis to test later (a preregistered lead–lag comparison against stream E, named
experts, and stream P, surveys). Stable framing, recurring hype cycles or no historical
shift are allowed results.

The motivating post (r/accelerate, "We are in the MATH singularity!!!!!", reposting a
claim about six solved open problems) illustrates the question and is not evidence. It
enters the data only if the sampling rule selects it, and any description of it attributes
the claim rather than presenting it as verified.

## 2. Place in the method

A **labelled vanguard sub-series of stream F** (specialist discourse), with its own
figure. Vanguard venues are **never pooled with stream F's other venues in any figure or
table**, and the sub-series is never shown on the same axis as streams E, P or M. It reuses
stream F's coverage audit and sampling design (section 6) and adds the claim-level coding
in section 7.

## 3. Scope

- **Enthusiast venues only** (Option B), labelled as a purposive selection.
- **Event-by-event comparison:** from the month the first qualifying skeptic venue exists,
  a preregistered list of capability events (model releases, benchmark claims, announced
  results) is coded in both enthusiast and skeptic venues with the same instrument, to show
  how each reads the same events. Comparisons are per event and claim type. **No monthly
  gap metric** and no subtraction between groups. Skeptic coverage starts when skeptic
  venues start; it is not backfilled from general forums.
- Capability expectations and development preferences are kept apart: expecting AGI soon is
  not the same as wanting it, and doubting a capability is not the same as opposing AI.

## 4. Venues and accounts: frozen selection

Before any collection beyond the retrievability check, publish: the candidate-venue
inventory and how it was found; inclusion and exclusion criteria; reasons for each venue
chosen and each rejected; verified creation dates and usable coverage dates; documented
changes in purpose or moderation. The same for skeptic venues when the comparison starts.
Whole venues are compared only with whole venues, never with stance-filtered threads.

**Enthusiast venues (proposed, to be confirmed by the inventory):** r/singularity (from
2008), r/accelerate (newer), r/artificial as a lower-intensity comparator.

**X accounts:** chosen by a published script, not by hand: accounts whose bio contains a
frozen keyword list, ranked by follower count on the freeze date, top K, with the script,
date, account IDs and qualifying bio text published before collection, and rules for
renames, suspensions and inactivity fixed in advance. Hashtag samples are kept separate
from account samples. Forward-only. If the qualifying evidence and posts can't meet the
public re-pull requirement, X is deferred.

## 5. Retrievability check before any historical series

For each venue, show that a public reader can: reach the exact versioned source; list a
period's candidate posts; reproduce the eligibility screening and the ranking; and
retrieve the text needed to check the coding. If the archive supports only "highest
recorded-score posts among archived records", that is the label used, not "the period's
top posts". Coverage per period is recorded as known incomplete, assessed, or unknown.
Score observation timestamps are kept, and scores are not called endorsement. The November
2023 change in how the Arctic Shift archive captures scores is marked as a measurement
break.

**First check:** r/singularity over the 24-month pilot window (section 6), reporting the
share of top posts whose text is recoverable. Results go in
`docs/feasibility/vanguard-retrievability-2026-10.md`.

## 6. Sampling: stream F's design

- **Rewarded series:** stream F's top 20 posts by recorded score per quarter, labelled
  "what the community rewarded", ranked after eligibility screening, with a written rule
  for ties and low-volume quarters; candidate, screened, included and excluded counts
  reported.
- **Prevalence sample:** stream F's seeded random sample of posts and, separately, of
  comments per quarter, drawn without regard to score, with inclusion probabilities
  recorded.
- No new sampling design is added for the vanguard sub-series.
- **Eligibility:** the post asserts, disputes or relays a claim about AI capability,
  timeline or consequence. **Image posts with legible text are included; image-only posts
  without text are excluded.** **Video posts are coded from their title only** (my ruling,
  2026-10-02): the video itself is not watched or coded, and a video post is eligible only
  if its title makes such a claim. Counts of each are reported. Rows coded from the title
  alone carry `title_only: yes` (section 7).
- **Retrievability in r/singularity** (stream F's top 20 per quarter; details in
  `docs/feasibility/vanguard-retrievability-2026-10.md`). Two figures are always reported
  together: **fully recoverable** (text, links, images that still load) and **including
  video posts coded by title only**. Over the full pilot window, 2024Q4 to 2026Q3: **55%
  and 90%**; over the first six quarters: 57% and 88%.

  | quarter | top posts | fully recoverable | video, title only | incl. title-only | lost | unverified |
  |---|---|---|---|---|---|---|
  | 2024Q4 | 20 | 11 (55%) | 6 | 17 (85%) | 2 | 1 |
  | 2025Q1 | 20 | 14 (70%) | 3 | 17 (85%) | 2 | 1 |
  | 2025Q2 | 20 | 9 (45%) | 10 | 19 (95%) | 1 | 0 |
  | 2025Q3 | 20 | 12 (60%) | 7 | 19 (95%) | 0 | 1 |
  | 2025Q4 | 20 | 11 (55%) | 3 | 14 (70%) | 4 | 2 |
  | 2026Q1 | 20 | 11 (55%) | 9 | 20 (100%) | 0 | 0 |
  | 2026Q2 | 20 | 8 (40%) | 11 | 19 (95%) | 0 | 1 |
  | 2026Q3 | 20 | 12 (60%) | 7 | 19 (95%) | 0 | 1 |
  | **2024Q4 to 2026Q1 (six quarters)** | **120** | **68 (57%)** | **38** | **106 (88%)** | **9** | **5** |
  | **full pilot window, 2024Q4 to 2026Q3** | **160** | **88 (55%)** | **56** | **144 (90%)** | **9** | **7** |

  "Lost" = image file deleted (HTTP 404); "unverified" = galleries, whose content needs
  reddit.com, which refused the lookup.
- **Amplification:** posts reacting to the same announcement share an event identifier;
  results are reported with and without de-duplication.
- **Pilot window:** the 24 complete calendar months before the freeze month, so
  **2024-10 to 2026-09** (8 quarters). Rule set by the agent on 2026-10-02 before any data
  was inspected; I may change it. A small preregistered sample from earlier eras tests
  whether the codebook works on older posts.

## 7. Coding: each post sampled, each claim coded

The full instrument, with the eligibility rulings of 2026-10-03 (posts not mentioning AI
are ineligible; video titles naming only a demo are eligible capability claims; memes
follow the legible-text rule; company and policy drama is coded `industry_governance`),
is `docs/vanguard/codebook.md`.

The **post** is the sampling unit and the **claim** is the coding unit, weighted so long
posts don't count more. **No single ladder**: each claim is coded on separate fields,
mapped to the project codebook where one exists.

| field | values | maps to |
|---|---|---|
| claim target | specific capability; AGI or general capability; autonomous research or self-improvement; pace of progress or singularity; social or economic consequence; industry and governance (AI company and policy drama; ruling 2026-10-03) | `target_capability` (including the four self-improvement levels) |
| temporal status | already achieved; under way; forecast; hypothetical; unspecified | `present_capability` plus timeline fields |
| forecast horizon | the exact date, range or wording | `timeline_*` |
| poster's stance | affirms; denies; questions; conditional; neutral relay; unclear | `endorsement` |
| epistemic qualification | unqualified; qualified; explicit probability; unclear | hedge rules (A14 ruling 10), with 5 to 10 worked examples of hedged and unhedged posts |
| rhetorical mode | literal; ironic or sarcastic; mixed; unclear | new; sarcasm is a mode, not a degree of uncertainty |
| development preference | supports; opposes; conditional; not expressed | new |
| attribution | original; repost of a panel member; of a lab or company; of a news outlet | panel reposts are logged as reposting events, not as the panel member's view |
| frame tags | "AGI", "singularity", "takeoff" and similar, as words used | lexical tags only; "math singularity" is not translated into "AGI achieved" |
| extrapolates_to_horizon | post level: does the post infer a timeline or consequence from a capability? `yes`, `no`, `na` (no capability claim) | new; ruling 2026-10-03 |
| title_only | `yes` when the post was coded from its title alone (video posts, section 6); blank otherwise | new; lets analysis exclude the hedge (epistemic qualification) and claim fields of these rows, or report them separately |

Denials keep their target ("AGI is not imminent" = AGI, near-term, denied).

**Display only, AGI claims only:** a six-rung proximity ladder derived from the fields above
(1 impossible; 2 distant or theoretical; 3 approaching, needs new breakthroughs; 4
imminent on current scaling; 5 crossing the threshold now; 6 AGI achieved and
self-improvement under way). It is never applied to other claim targets and never used as
a coding field.

## 8. Outputs

**Primary measures (ruling 2026-10-03):** the share of eligible posts making a capability
claim and a consequence claim, and the share of capability posts that extrapolate to a
timeline or consequence. The four claims below are kept and reported as near-absent where
they are (the r/singularity pilot found them in under 5% of eligible posts).

**Not reported (ruling 2026-10-03):** whether the poster wants AI sped up or slowed down
(`development_preference`) is still coded but listed as unreliable and kept out of results.

**Shares only.** Per venue and quarter, separately for the rewarded and prevalence samples:
the share of eligible posts affirming each claim (AGI already achieved; AGI within a
stated horizon; self-improvement under way; singularity framing), the share disputing each,
and the share unclear or ironic, with both denominators reported (all eligible posts, and
posts on that target). **No medians, no quartiles, no subtraction between groups.**

**Title-only rows.** Coding from a title alone likely **overstates unhedged claims**:
titles are short and written to attract attention, and the hedges, caveats and irony that
would sit in a post's body or a video's narration are missing. Every share is therefore
reported twice, with and without `title_only: yes` rows, and the hedge and claim fields of
title-only rows are excluded from any claim about how hedged the venue's framing is.

## 9. Reliability (revised by me, 2026-10-03; human step removed the same day)

Coding is fully model-based. There is no human coder: the earlier requirement that two
people code a subset blind, and the later plan for a 40-post check by me, are both
withdrawn.

1. **Three models from different companies code the same preregistered subset blind**, each
   seeing only the codebook and the post. In the r/singularity pilot (140 posts):
   `claude-opus-5-5` (Anthropic); `gemini-3.1-pro-preview`, version `3.1-pro-preview-01-2026`
   (Google); `gpt-6-astra`, reasoning effort medium, pinned by the creation time OpenAI lists
   (1787853604; OpenAI publishes no dated snapshot) (OpenAI).
2. **Final code by majority vote per field.** A value needs at least two of the three models
   to give it. Where no two agree, the field is marked unresolved for that post.
3. **Cohen's kappa (agreement corrected for chance) for all three pairs of models, per field.**
4. **Reliability test.** A field unresolved on more than 15% of posts, or with every pairwise
   kappa below 0.6, is excluded from figures and listed as unreliable.
5. **Recurring disagreements** get a proposed codebook rule, tested by recoding the subset
   with the rule and comparing kappa before and after. I rules on each rule. A rule tested
   on the posts it was written from will look better than it is, so an adopted rule is
   checked again on a fresh sample.

Evidence spans recorded for each code; "unclear" allowed; prompts, models and codebook
frozen per run.

## 10. Presentation

- Every figure and section heading carries: **"Framing in sampled high-score posts from
  selected AI enthusiast venues; not representative of participants or the public."**
- Figures also carry **"model-coded"**, and show only fields that pass the section 9
  reliability test (ruling 2026-10-03).
- Its own figure; never pooled with stream F's other venues; never on the same axis as
  streams E, P or M.
- Any sentence of the form "by 2023 people thought X" cites stream P, not this sub-series.
- The event-by-event comparison is shown per event, never as a single gap line.

## 11. Validity threats (stated in the methodology)

Self-selection (bounded by framing, not solvable); venue drift (membership composition
unknown unless evidenced; subscriber counts are context, not a correction); survivorship
and deletion (removal rates where exposed; availability re-audited; what happens when
evidence disappears defined in advance); platform changes (2023 Reddit API, X access, the
2023 Arctic Shift score break) marked on every time axis; unequal score-observation
windows; amplification; coder drift (a recode under a new model is a new run); sarcasm (the
rhetorical-mode field; it failed the three-model reliability test in the pilot, so it is
kept out of figures).

## 12. Acceptance criteria for the pilot

1. Retrievability check (section 5) on r/singularity for the pilot window, reviewed by me.
2. Venue inventory, X selection script (or X deferred) and eligibility rule committed before
   the first coded pull.
3. Pilot plus the cross-era sample coded; blind two-person agreement reported; codebook
   revised if agreement is poor and checked on a fresh holdout.
4. Pilot figure under the presentation rules reviewed by me before any other venue is
   collected.
