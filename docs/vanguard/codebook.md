# Codebook: vanguard sub-series (stream F)

How posts in the vanguard sub-series are coded. Written 2026-10-03 from section 7 of the
accepted amendment `docs/amendments/2026-10-02-vanguard-stream.md`, the rules applied in the
r/singularity pilot, and my rulings of 2026-10-03 on the pilot report. Changes go in
`docs/amendments.md` first. (Statements by named experts, stream E, use `docs/codebook.md`.)

Code what the post says, not what you know about the topic or the poster. Don't check
whether claims are true.

## 1. Content basis

| post type | coded from | `title_only` |
|---|---|---|
| text | title and body | blank; `yes` if the body was removed or deleted and only the title survives (`content_basis: text_title`) |
| image | title and the image. Coded if the image has legible text or a legible chart or screenshot; otherwise not eligible (`image_no_text`). A dead image file: not eligible (`content_unavailable`) | blank |
| meme | as an image: **the legible-text rule applies** (ruling 2026-10-03) | blank |
| video | **title only** (ruling 2026-10-02) | `yes` |
| link | title plus the linked page if it opens; title only if it doesn't | `yes` only if title only |
| gallery | not eligible (`content_unavailable`); content needs reddit.com | blank |

A post whose title itself reads "[ Removed by moderator ]" is not eligible
(`content_unavailable`).

## 2. Eligibility

**Eligible** = the post asserts, disputes or relays a claim about AI capability, timeline,
consequence, or the AI industry and its governance.

Rulings of 2026-10-03:
- **Posts that don't mention AI are not eligible** (`no_ai_claim`), even when the
  subreddit makes an AI reading likely. The post itself (title, body, legible image text or
  opened link) must refer to AI, a model, a lab, a robot or an AI product.
- **Video titles that only name a demo** ("Atlas does a backflip", "Will Smith eating
  spaghetti in Veo 3.1") **are eligible capability claims** (`specific_capability`,
  `temporal_status: achieved`).
- **AI company and policy drama** (disputes between labs, executives' public fights, a
  model's political answers as a news item, government action on AI companies) is eligible
  under the target `industry_governance`.
- Pure questions with no claim, slogans, off-topic posts and meta are not eligible
  (`no_ai_claim`).

## 3. Claims

The post is the sampling unit; each distinct claim is a row (`claim_n` 1, 2, ...), main
claim first. An ineligible post gets one row with `claim_n` 0 and the claim fields blank.

| field | codes |
|---|---|
| `claim_target` | `specific_capability` (a named task, model, benchmark, robot or demo); `agi` (AGI, human-level or general capability); `self_improvement` (AI doing AI research or improving itself, with `si_level`); `pace_singularity` (pace of progress, takeoff, "singularity"); `consequence` (social or economic effects of AI); `industry_governance` (AI companies, executives, labs' conduct and disputes, regulation and policy, government action on AI) |
| `si_level` | only for self_improvement: `si_assist`, `si_research`, `si_modify`, `si_sustained`; the lowest level the words support |
| `temporal_status` | `achieved`, `under_way`, `forecast`, `hypothetical`, `unspecified` |
| `forecast_horizon` | the exact date, range or words of a forecast; else blank |
| `stance` | `affirms`, `denies`, `questions`, `conditional`, `neutral_relay`, `unclear` |
| `epistemic_qualification` | `unqualified`, `qualified`, `explicit_probability`, `unclear` |
| `rhetorical_mode` | `literal`, `ironic`, `mixed`, `unclear` |
| `development_preference` | `supports`, `opposes`, `conditional`, `not_expressed` |
| `attribution` | `original`, `panel_member`, `lab_or_company`, `news_outlet`, `other_person` |
| `frame_tags` | words actually used, `;`-separated: agi, asi, superintelligence, singularity, takeoff, rsi, recursive, feel_the_agi, accelerate, e_acc, doom, hype, bubble, other. A benchmark or product name containing a word (ARC-AGI) is not a tag; a pun on a word ("singularity of sight") is not a tag |
| `extrapolates_to_horizon` | post level, repeated on each of the post's rows: **does the post infer a timeline or a consequence from a capability?** `yes` (e.g. "it solved six open problems, so the singularity is near"; "this robot will take warehouse jobs"); `no` (a capability is claimed but nothing is inferred from it); `na` (no capability claim in the post). Blank on ineligible rows. Ruling 2026-10-03 |
| `title_only` | `yes` when coded from the title alone |
| `evidence_span` | 25 words or fewer, verbatim, from the title, body or image text |

Denials keep their target ("AGI is not imminent" = agi, forecast, denies).

### Decision rules adopted by me, 2026-10-03

**R2: company and policy news, or capability.**

Decide the main claim's target by the subject of the main claim, not by which company is
named. Ask: who or what does the thing the claim is about?
- A model, robot or AI system (what it can or can't do, how it behaved, a new model or
  product with what it does, benchmark scores, a demo, a deployment such as robots now
  patrolling a stadium): specific_capability. This includes a model's own output shown in a
  screenshot, even when the output is about its owner.
- A company, executive, investor or government (deals, funding, hiring, firing, lawsuits,
  feuds, regulation, pricing, access, release or withholding decisions, leaks, advertising,
  spending): industry_governance.
- People, jobs, society or the economy (effects of AI on them): consequence.
If the post makes claims of more than one kind, code each as its own claim. The main claim
is the one stated in the title; if the title states none, the one the post spends most words
on.

**R3: hedging.**

Code epistemic_qualification from the words that state the main claim: the title, plus any
body, image or page text that states the same claim, including a quoted source's own words.
Code qualified only if those words contain a hedge that limits certainty: may, might, could,
probably, likely, possibly, perhaps, I think, I suspect, I believe, seems, appears, suggests,
early signs, if, or an equivalent phrase. Otherwise unqualified. Code explicit_probability
only for a stated number or odds. Code unclear only when no claim is stated in words at all
(a title that just names a topic, such as "X's thoughts on AI").

### Decision rule adopted by me, 2026-10-04

**R1a: stance of posts passed on without comment.**

When the poster passes on a news item, announcement, demo video, product launch or screenshot
of someone else's words, and adds no words of their own about whether the claim is true, the
post has no stated stance: code stance = neutral_relay. A title that only restates, names or
describes the item counts as no comment, even when the poster wrote it. Code affirms or
denies only when the poster adds words of their own that accept or reject the claim as true.
Jokes and reaction titles ("WTF", "Shots fired!", an emoji) are not endorsements; code the
passed-on claim as neutral_relay and record the tone in rhetorical_mode.

Attribution of such posts follows the field definition above; the proposed rule R1b was
rejected.

## 4. Measures (amendment section 8, as revised 2026-10-03)

- **Primary:** share of eligible posts making a **capability** claim (`specific_capability`)
  and a **consequence** claim (`consequence`), and the share of capability posts that
  **extrapolate** to a timeline or consequence.
- **Also reported:** `industry_governance` claims.
- **Headline claims, reported as near-absent:** AGI already achieved; AGI within a stated
  horizon; self-improvement under way; singularity framing (poster affirms each).
- Every share is reported with and without `title_only` rows.
- **Not reported:** whether the poster wants AI sped up or slowed down
  (`development_preference`). Ruled unreliable by me, 2026-10-03; still coded.
