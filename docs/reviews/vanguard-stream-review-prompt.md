# Review request: an added evidence stream for a dataset on how opinion about AGI has moved, 2005 to 2026

I am building a public, citable dataset on how expert and public opinion about artificial general intelligence (AGI) has changed from 2005 to the present, plus an essay with charts built from it. The expert half is a fixed panel of named thinkers whose dated public statements are coded by which question they answer (is AGI possible, when will it arrive, is the current system already capable, can it improve itself), their timeline estimate, and whether they endorse the capability arriving, with a written sampling rule to prevent cherry-picking. The method has already been through one outside review, which split the work into separate streams (named experts, population surveys, published articles, online communities), each reported on its own with its own unit.

The constraint is unchanged: every source must be publicly re-pullable by a reader; no personal recollection, no private data.

I now want to add one more stream, described in the draft amendment below, and I would like your critique before anything is collected.

## The draft amendment

# Amendment: Vanguard Sentiment Stream

Status: DRAFT, pending outside review (Gemini 3.1 Pro, GPT-6 Astra Medium) per the 2026-09-30 ruling. Not to be collected until the review gate below is cleared and John has accepted the reconciled version.
Date: 2026-10-02
Applies to: docs/methodology-v2.md (adds one evidence stream), docs/amendments.md (log entry)
Destination: agi-zeitgeist/docs/amendments/2026-10-02-vanguard-stream.md

## 1. Purpose

Add a separate evidence stream that tracks how the self-selected AI-acceleration community (r/accelerate, r/singularity, the enthusiast cluster on X) frames AGI progress over time. This community moves earlier and further than both the named-thinker panel and the general public. That makes it useful as a leading indicator of framing and useless as a measure of what people in general believe. The stream exists to capture the first property and is presented so it cannot be mistaken for the second.

Motivating observation (2026-10-02): an r/accelerate post titled "We are in the MATH singularity!!!!!" reposting Alexandr Wang's claim that mathematicians and an AI system solved six open problems. The signal in that post is not optimism level. It is which claim is treated as already settled. Twenty years ago the live question in these spaces was whether AGI was possible; today a solved-problems list is read as evidence that a singularity is in progress. The thing that moves is the milestone frame, and the coding scheme below is built to track that rather than mood.

## 2. What this stream is and is not

Is:
- A record of the furthest claim asserted without hedge by the most-engaged posts in a fixed set of enthusiast venues, sampled on a fixed rule, per month.
- Re-pullable: every datapoint is a public post retrievable by ID with a stored query.

Is not:
- A measure of public opinion. The venues are self-selected by belief; a spike here says nothing about the population.
- A measure of expert opinion. Panel members who are reposted here are already counted in the panel stream; their appearance here is coded as a reposting event, not as their own view.
- A truth claim about the underlying events. Whether six open problems were in fact solved is irrelevant to this stream; what is coded is that the community asserted it as a singularity marker.

## 3. Even-handedness: the vanguard pair

A stream that samples only accelerationists will drift upward by construction and reviewers will rightly call it cherry-picked. Two options, to be put to the outside reviewers as an open question:

- Option A (recommended): collect a mirrored skeptic vanguard on the same rules, from venues self-selected by AI skepticism or deceleration (candidates: r/BetterOffline, r/artificial_intelligence critics threads, a fixed list of prominent critic accounts on X). Present both as a pair. The interesting quantity becomes the distance between the two vanguards over time, and whether it widens or narrows.
- Option B: collect the enthusiast side only, label it unambiguously as one-sided, and rely on the panel and public streams for balance.

Option A costs roughly double the collection effort and the skeptic venues are smaller and younger, so the backfilled skeptic series will be thinner before 2023. That asymmetry must be stated in the essay if Option A is chosen. The default recommendation is A with the asymmetry disclosed, because the pair is the only presentation that does not read as advocacy.

## 4. Source set and inclusion rule

Named up front, frozen before collection, changes logged as amendments.

Enthusiast venues:
- Reddit: r/singularity (primary, exists since 2008, gives the longest series), r/accelerate (secondary, newer), r/artificial as a lower-intensity comparator.
- X: a fixed account list of 20 to 30 accounts, chosen by a written rule (for example, accounts with over N followers whose bio or pinned post self-identifies with acceleration, e/acc or singularity framing as of the freeze date), plus a fixed hashtag set. The list is forward-only from the freeze date. No backfilled X series is claimed; X archive access is too poor to re-pull reliably.

Skeptic venues (if Option A):
- Reddit: r/BetterOffline, plus any skeptic-aligned subreddit meeting a minimum-size threshold on the freeze date.
- X: mirrored account list built by the same rule with skeptic self-identification.

Inclusion rule for a post: it must assert or dispute a claim about AI capability, timeline or consequence. Memes, meta, moderation and off-topic posts are excluded and the exclusion count is reported.

## 5. Sampling

Reddit, backfilled: for each venue and each calendar month, the top N posts by score (N = 25 proposed), pulled via the Reddit API or a Pushshift-derived archive with the exact query, timestamp and archive snapshot ID stored alongside the data. Where the archive is incomplete for a month, the month is marked as such rather than filled from memory or browsing.

X, forward-only: for each account on the list, all posts in the month with over a stated engagement floor, pulled on a fixed day each month and stored by post ID.

Browsing, screenshots and "posts I noticed" are not data. The post that motivated this amendment enters the dataset only if it is captured by the top-N rule for October 2026.

## 6. Coding scheme

Each included post is coded by two passes (model-assisted first pass, human spot-check on a stated fraction, disagreements logged) on:

- Milestone frame: the furthest capability or consequence the post treats as already achieved or imminent without hedge. Ordinal ladder to be finalized with reviewers, roughly: AGI impossible or far off; narrow progress only; AGI plausible within career horizon; AGI imminent; recursive self-improvement under way; singularity in progress; post-singularity framing.
- Hedge level: unhedged, hedged, ironic or sarcastic. Sarcasm is common in both vanguards and miscoding it inverts the signal, so this field is mandatory.
- Claim source: original to the poster, repost of a panel member, repost of a lab or company announcement, repost of a news outlet. This separates what the community generates from what it amplifies.
- Stance toward the claim: endorsing, contesting, neutral relay. Needed so skeptic-venue posts that quote enthusiast claims in order to mock them are not coded as enthusiast assertions.
- Engagement: score and comment count at pull time, stored as-is.

Time series reported: median and upper-quartile milestone frame per venue per month, share of unhedged posts, share of posts that are reposts of panel members, and the enthusiast-minus-skeptic gap if Option A.

## 7. Presentation rules

- Separate figure, separate section, never on the same axis as the panel or public streams.
- Section heading and figure captions carry the phrase "leading indicator of framing, not a measure of belief" or equivalent plain-English wording, on every appearance.
- Any sentence of the form "by 2023 people thought X" must cite the public stream, not this one.
- The vanguard pair is shown together whenever both exist; the enthusiast series is never shown alone in the essay if Option A is adopted.
- The post that motivated the amendment may be used as an illustrative example in the essay only if it also appears in the sampled dataset.

## 8. Known validity threats, stated in the methodology

- Self-selection: addressed by framing and the pair, not solvable.
- Venue drift: r/singularity in 2012 and r/singularity in 2026 are different communities under the same name. Report subscriber counts per year alongside the series.
- Survivorship: deleted or removed posts are missing from archives in ways that correlate with content. Report removal rates where the archive exposes them.
- Platform change: Reddit API restrictions in 2023 and X access changes create discontinuities. Mark them on every time axis.
- Coder drift: the model used for first-pass coding is fixed per collection run and named; a recode under a new model is a new run, not an overwrite.
- Sarcasm and in-group irony: handled by the mandatory hedge field and a higher human spot-check fraction for this stream than for the panel.

## 9. Review gate

Before any collection:
1. Send this amendment to Gemini 3.1 Pro and GPT-6 Astra Medium with the same prompt used for the v1 review, asking specifically for (a) a ruling on Option A versus B, (b) critique of the milestone ladder, (c) any venue or sampling choice that would read as cherry-picking to a hostile reader.
2. Save both reviews verbatim under docs/reviews/.
3. Reconcile into a final version of this file and a one-line entry in docs/amendments.md.
4. John accepts or amends the reconciled version. Only then does the seed-phase session begin collection.

## 10. Acceptance criteria for the seed run

- Frozen source list and inclusion rule committed before the first pull.
- One venue (r/singularity) backfilled for a 24-month pilot window, with stored queries, before scaling to the full span or other venues.
- Inter-coder agreement on the pilot reported; the ladder revised if agreement is poor.
- Pilot figure produced under the presentation rules above and reviewed by John before any other venue is collected.


## What I want from you

1. **Option A versus Option B (section 3).** Should the stream collect a mirrored skeptic vanguard alongside the enthusiast one, or the enthusiast side only, clearly labelled? Give a ruling and the reason, and say what would have to be true for the other option to be better.
2. **The milestone ladder (section 6).** Critique the ordinal ladder: is it one dimension or several mixed together, are the rungs ordered correctly, can a coder place a real post on it reliably, and what would you change? Propose a revised ladder if you think it needs one.
3. **Cherry-picking.** Which venue, account-list, sampling or presentation choice would a hostile reader call cherry-picking, and how would you close each gap before collection?

Please be direct. I would rather hear that the stream is unsalvageable now than after it is collected.
