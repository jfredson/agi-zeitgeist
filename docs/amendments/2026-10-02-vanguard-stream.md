# Amendment: vanguard sub-series of stream F

Status: **ACCEPTED by John, 2026-10-02**, with his rulings on the seven open questions
applied. Drafted by John 2026-10-02 (original in git history, commit `d3a1e19`); reviewed
by Gemini 3.1 Pro and GPT-6 Astra Medium (verbatim in `docs/reviews/vanguard-stream-review-*.md`,
prompt `docs/reviews/vanguard-stream-review-prompt.md`); reconciled 2026-10-02 (commit
`d7482b2`).
Applies to: `docs/methodology-v2.md` section 6 (stream F), `docs/amendments.md` (log entry).

**Collection status:** only the retrievability check in section 5 may run. Nothing else is
collected until John has seen its result.

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
  without text are excluded.** Counts of each are reported.
- **Amplification:** posts reacting to the same announcement share an event identifier;
  results are reported with and without de-duplication.
- **Pilot window:** the 24 complete calendar months before the freeze month, so
  **2024-10 to 2026-09** (8 quarters). Rule set by the agent on 2026-10-02 before any data
  was inspected; John may change it. A small preregistered sample from earlier eras tests
  whether the codebook works on older posts.

## 7. Coding: each post sampled, each claim coded

The **post** is the sampling unit and the **claim** is the coding unit, weighted so long
posts don't count more. **No single ladder**: each claim is coded on separate fields,
mapped to the project codebook where one exists.

| field | values | maps to |
|---|---|---|
| claim target | specific capability; AGI or general capability; autonomous research or self-improvement; pace of progress or singularity; social or economic consequence | `target_capability` (including the four self-improvement levels) |
| temporal status | already achieved; under way; forecast; hypothetical; unspecified | `present_capability` plus timeline fields |
| forecast horizon | the exact date, range or wording | `timeline_*` |
| poster's stance | affirms; denies; questions; conditional; neutral relay; unclear | `endorsement` |
| epistemic qualification | unqualified; qualified; explicit probability; unclear | hedge rules (A14 ruling 10), with 5 to 10 worked examples of hedged and unhedged posts |
| rhetorical mode | literal; ironic or sarcastic; mixed; unclear | new; sarcasm is a mode, not a degree of uncertainty |
| development preference | supports; opposes; conditional; not expressed | new |
| attribution | original; repost of a panel member; of a lab or company; of a news outlet | panel reposts are logged as reposting events, not as the panel member's view |
| frame tags | "AGI", "singularity", "takeoff" and similar, as words used | lexical tags only; "math singularity" is not translated into "AGI achieved" |

Denials keep their target ("AGI is not imminent" = AGI, near-term, denied).

**Display only, AGI claims only:** a six-rung proximity ladder derived from the fields above
(1 impossible; 2 distant or theoretical; 3 approaching, needs new breakthroughs; 4
imminent on current scaling; 5 crossing the threshold now; 6 AGI achieved and
self-improvement under way). It is never applied to other claim targets and never used as
a coding field.

## 8. Outputs

**Shares only.** Per venue and quarter, separately for the rewarded and prevalence samples:
the share of eligible posts affirming each claim (AGI already achieved; AGI within a
stated horizon; self-improvement under way; singularity framing), the share disputing each,
and the share unclear or ironic, with both denominators reported (all eligible posts, and
posts on that target). **No medians, no quartiles, no subtraction between groups.**

## 9. Reliability

Two people independently code a preregistered pilot subset without seeing the model's
labels, including ambiguous, ironic and older posts. Agreement and confusion tables by
field; evidence spans recorded for each code; "unclear" allowed; prompts, model and
codebook frozen per run; a fresh holdout sample after any revision. A category that stays
unreliable is simplified or dropped. A model first pass is quality control, not a second
coder.

## 10. Presentation

- Every figure and section heading carries: **"Framing in sampled high-score posts from
  selected AI enthusiast venues; not representative of participants or the public."**
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
rhetorical-mode field and a higher human check rate).

## 12. Acceptance criteria for the pilot

1. Retrievability check (section 5) on r/singularity for the pilot window, reviewed by John.
2. Venue inventory, X selection script (or X deferred) and eligibility rule committed before
   the first coded pull.
3. Pilot plus the cross-era sample coded; blind two-person agreement reported; codebook
   revised if agreement is poor and checked on a fresh holdout.
4. Pilot figure under the presentation rules reviewed by John before any other venue is
   collected.
