# Amendment: Vanguard Sentiment Stream (reconciled draft)

Status: **RECONCILED DRAFT, not accepted.** Revised 2026-10-02 after two outside reviews,
saved verbatim in `docs/reviews/vanguard-stream-review-gemini-3.1-pro-2026-10.md` and
`docs/reviews/vanguard-stream-review-gpt-6-astra-2026-10.md` (prompt:
`docs/reviews/vanguard-stream-review-prompt.md`). John's original draft is in git history
(commit `d3a1e19`). **Nothing is collected until John rules on section 0 and accepts this
version.**
Applies to: `docs/methodology-v2.md` (a registered sub-study within stream F),
`docs/amendments.md` (log entry).

Where the two reviews agreed, their point is adopted below. Where they disagreed, both
positions are set out in section 0 with a suggestion marked as the agent's, for John to
rule.

## 0. Rulings needed from John

| # | question | Gemini 3.1 Pro | GPT-6 Astra Medium | agent suggestion |
|---|---|---|---|---|
| R1 | **Option A (paired skeptic stream) or B (enthusiast only)?** | A is mandatory; B would be dismissed as an "AI hype tracker"; the later start of skeptic venues is "a finding in itself" | B first; A only as a substantive comparison of how differently selected communities read the **same** events, never an unconditional gap; a pair "chosen for appearances" doesn't fix self-selection | B now, with a preregistered **event-conditional comparison** (A') added from the month the first qualifying skeptic venue exists: both sides coded on the same capability announcements, no monthly subtraction. This gives Gemini's pairing without GPT's objection to a manufactured opposition |
| R2 | **Ladder: replace with one dimension, or drop?** | Replace with a strict one-dimensional "proximity" ladder (impossible → distant → needs breakthroughs → imminent by scaling → crossing the threshold now → self-improvement under way), with consequence coded separately | No single ladder: code each claim on separate fields and report proportions; an ordering is defensible only within one claim target (beyond a horizon → within a horizon → already achieved) | Code claims on separate fields (section 6). Derive Gemini's proximity scale **only within the AGI target** as a display, which is the limited ordering GPT accepts |
| R3 | **Reddit sample: top 25 by score, or random 25 above a score threshold?** | Random 25 from posts above a score threshold, memes excluded first, seed stored | Top-N is acceptable if labelled as a "top-post" sample; make the ranking-then-exclusion order explicit | Keep a top-N "rewarded" series (as stream F already does, A6) **and** use stream F's existing random prevalence sample of the same venue rather than a second random design. No new sampling rule needed |
| R4 | **Memes** | Exclude | May carry the rhetoric being measured; include interpretable image-text posts or restrict the scope openly | Include image-text posts where the text is legible; exclude pure images; report counts |
| R5 | **"Leading indicator" wording** | Implicitly accepts the framing ("shifting Overton window") | Remove: an untested predictive claim; caption should say "framing in sampled high-score posts from selected AI enthusiast venues; not representative of participants or the public" | Adopt GPT's caption; keep "leading indicator" only as a hypothesis with a preregistered lead–lag test against the panel and survey streams |
| R6 | **Summary statistics** | Measure the "spread" between the two vanguards | Drop medians, upper quartiles and any subtraction; report proportions with stated denominators | Follows R1 and R2: proportions per claim target; no subtraction |
| R7 | **New stream or sub-study?** | (not addressed) | Sub-study within the existing online-community stream | Sub-study within stream F. Stream F already covers r/singularity with a random sample and a top-20 "rewarded" series per quarter (methodology-v2 section 6, A6), so a separate stream would duplicate it |

## 1. Purpose

Record how highly ranked posts in a fixed set of AI-enthusiast venues frame AI progress
over time: which capabilities are treated as already achieved, under way or near, and in
what terms. The construct is **framing in selected venues**. It is not a measure of what
people in general believe, nor of what the venues' members believe.

The working idea that these venues move "earlier and further" than the panel or the
public is a **hypothesis**, not a design property. It can be tested later with a
preregistered lead–lag comparison against stream E (named experts) and stream P
(surveys). Results such as stable framing, recurring hype cycles or no historical shift
are allowed outcomes.

The motivating post (r/accelerate, "We are in the MATH singularity!!!!!", reposting a
claim about six solved open problems) is an illustration of the question, not evidence.
It enters the data only if the sampling rule selects it, and any description of it in
the essay attributes the claim rather than presenting it as verified.

## 2. Place in the method

A registered sub-study within stream F (specialist discourse). It reuses stream F's
coverage audit, its random prevalence sample and its "what the community rewarded"
series where venues overlap, and adds claim-level coding (section 6) and the venue set in
section 4. Never shown on the same axis as streams E, P or M.

## 3. Scope: enthusiast venues, with an event-conditional comparison (pending R1)

- **Primary (Option B):** enthusiast venues only, labelled as a purposive selection.
- **Comparison (A', pending R1):** from the month the first qualifying skeptic venue
  exists, a preregistered list of capability events (model releases, benchmark claims,
  announced results) is coded in both enthusiast and skeptic venues with the same
  instrument. Comparisons are made per event and claim type, never as a monthly
  enthusiast-minus-skeptic gap. Skeptic coverage starts when skeptic venues start; it is
  not backfilled from general forums (both reviews).
- Capability expectations and development preferences are kept apart: believing AGI is
  near is not the same as wanting it, and doubting a capability is not the same as
  opposing AI (GPT).

## 4. Venues and accounts: frozen selection

Before any pull, publish:
- the candidate-venue inventory and how it was found; inclusion and exclusion criteria;
  reasons for each venue chosen and each rejected; verified creation dates and usable
  coverage dates; documented changes in purpose or moderation (GPT);
- for the comparison, the same for skeptic venues. Whole venues are compared only with
  whole venues, never with stance-filtered threads (GPT).

**Enthusiast venues (proposed, to be confirmed by the inventory):** r/singularity
(from 2008), r/accelerate (newer), r/artificial as a lower-intensity comparator.

**X accounts:** selected by a script, not by hand (both reviews): accounts whose bio
contains a frozen keyword list, ranked by follower count on the freeze date, top K, with
the script, the date, the account IDs and the qualifying bio text published before
collection. Rules for renames, suspensions and inactivity frozen in advance; hashtag
samples kept separate from account samples. Forward-only. **If the qualifying evidence and
posts can't meet the public re-pull requirement, X is deferred** (GPT).

## 5. Feasibility gate before any historical series

A technical demonstration, for each venue, that a public reader can: reach the exact
versioned source; enumerate a month's candidate posts; reproduce the eligibility
filtering and ranking; and retrieve the text needed to check the coding (GPT). If the
archive supports only "highest recorded-score posts among archived records", that is the
label used, not "the month's top posts". Coverage per month is recorded as known
incomplete, assessed, or unknown. Score observation timestamps are kept, and scores are
not called endorsement. The November 2023 change in how the Arctic Shift archive captures
scores is marked as a measurement break (as in stream F).

## 6. Sampling (pending R3, R4)

- **Rewarded series:** per venue and month, the top N eligible posts by recorded score
  (N = 25), ranked after eligibility screening, with ties and low-volume months handled by
  a written rule; candidate, screened, included and excluded counts reported.
- **Prevalence:** stream F's seeded random sample for the same venue, so the rewarded
  series can be compared with ordinary posts.
- **Eligibility:** the post asserts, disputes or relays a claim about AI capability,
  timeline or consequence. Image-text posts with legible text are eligible (pending R4).
- **Amplification:** posts reacting to the same announcement share an event identifier;
  results are reported with and without de-duplication (GPT).
- **Pilot window:** the rule for choosing the 24-month pilot is frozen before any data is
  inspected, plus a small preregistered sample from other eras to test whether the
  codebook works on older posts (GPT).

## 7. Coding: one post sampled, each claim coded (pending R2)

The **post** is the sampling unit and the **claim** is the coding unit, with weights so
that long posts don't count more (GPT). Fields, mapped to the project codebook where one
exists:

| field | values | maps to |
|---|---|---|
| claim target | specific capability; AGI or general capability; autonomous research or self-improvement; pace of progress or singularity; social or economic consequence | `target_capability` (including the four self-improvement levels) |
| temporal status | already achieved; under way; forecast; hypothetical; unspecified | `present_capability` plus timeline fields |
| forecast horizon | the exact date, range or wording | `timeline_*` |
| poster's stance | affirms; denies; questions; conditional; neutral relay; unclear | `endorsement` |
| epistemic qualification | unqualified; qualified; explicit probability; unclear | hedge rules (A14 ruling 10), with 5 to 10 worked examples of hedged and unhedged posts (Gemini) |
| rhetorical mode | literal; ironic or sarcastic; mixed; unclear | new. Sarcasm is a mode, not a degree of uncertainty (GPT) |
| development preference | supports; opposes; conditional; not expressed | new |
| attribution | original; repost of a panel member; of a lab or company; of a news outlet | panel reposts are logged as reposting events, not as the panel member's view |
| frame tags | "AGI", "singularity", "takeoff" and similar, as words used | lexical tags only. "Math singularity" is not translated into "AGI achieved" (GPT) |

Denials keep their target ("AGI is not imminent" = AGI, near-term, denied). A display
ordering (beyond a horizon → within a horizon → already achieved) is derived only within
the AGI target (pending R2).

## 8. Outputs

Per venue and month, separately for the rewarded and prevalence samples: the share of
eligible posts affirming each claim (AGI already achieved; AGI within a stated horizon;
self-improvement under way; singularity framing), the share disputing each, and the share
unclear or ironic, with both denominators reported (all eligible posts, and posts on that
target). No medians, quartiles or subtraction (pending R6).

## 9. Reliability

Two people independently code a preregistered pilot subset without seeing the model's
labels, including ambiguous, ironic and older posts. Agreement and confusion tables by
field; evidence spans recorded for each code; "unclear" allowed; prompts, model and
codebook frozen per run; a fresh holdout sample after any revision (GPT). A category that
stays unreliable is simplified or dropped. A model first pass is quality control, not a
second coder.

## 10. Presentation

- Separate section and figure. Caption on every appearance: "Framing in sampled
  high-score posts from selected AI enthusiast venues; not representative of participants
  or the public" (pending R5).
- Any sentence of the form "by 2023 people thought X" cites stream P, not this one.
- If the comparison (A') is adopted, it is shown per event, alongside the primary series,
  never as a single gap line.

## 11. Validity threats (stated in the methodology)

Self-selection (bounded by framing, not solvable); venue drift (membership composition
unknown unless evidenced; subscriber counts are context, not a correction); survivorship
and deletion (removal rates where exposed; availability re-audited; what happens when
evidence disappears is defined in advance); platform changes (2023 Reddit API, X access,
the 2023 Arctic Shift score break) marked on every time axis; unequal score-observation
windows; amplification; coder drift (a recode under a new model is a new run); sarcasm
(the rhetorical-mode field and a higher human check rate).

## 12. Acceptance criteria for the pilot

1. John's rulings on section 0 and acceptance of this version.
2. Venue inventory, X selection script (or X deferred), eligibility rule and pilot-window
   rule committed before the first pull.
3. Feasibility gate (section 5) passed for r/singularity.
4. 24-month pilot plus the cross-era sample coded; blind two-person agreement reported;
   codebook revised if agreement is poor and checked on a fresh holdout.
5. Pilot figure under the presentation rules reviewed by John before any other venue is
   collected.
