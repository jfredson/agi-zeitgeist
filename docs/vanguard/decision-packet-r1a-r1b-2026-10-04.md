# Decision packet: rules R1a and R1b (posts passed on without comment)

Prepared 2026-10-04 for John, once all three models had coded the trial posts. The
recommendations below were the agent's.

**Ruled by John, 2026-10-04: R1a adopted with the reactions sentence; R1b rejected.** Now in
`docs/vanguard/codebook.md` and `docs/amendments.md`.

## What you are deciding

Two proposed codebook rules, each about posts where someone passes on a news item, a demo
video, a product launch or a screenshot of someone else's words and adds nothing of their
own. For each: **adopt**, **refine** (adopt with a change), or **reject**.

- **R1a, whether the poster agrees** (the `stance` field): such a post is coded "passes it on
  without taking a side" (`neutral_relay`) unless the poster adds words of their own
  accepting or rejecting the claim. Full text: `docs/vanguard/trial-rule-r1a-2026-10-03.md`.
- **R1b, whose claim it is** (the `attribution` field): such a post's claim is credited to the
  source shown (the news outlet, the company, or the person quoted), or to the poster if no
  source is shown. Full text: `docs/vanguard/trial-rule-r1b-2026-10-03.md`.

## Recommendation

| rule | recommendation | in one line |
|---|---|---|
| R1a | **Refine, then adopt** | Without it, "whether the poster agrees" fails your reliability test; with it, all three model pairs pass. Add back one sentence on reactions and jokes, which the split dropped. |
| R1b | **Reject** | "Whose claim it is" already passes comfortably without it, and the rule made no measurable difference. |

The sentence to add to R1a is already written. It was part of the original combined rule R1
and was lost when R1 was split into R1a and R1b:

> Jokes and reaction titles ("WTF", "Shots fired!", an emoji) are not endorsements; code
> the passed-on claim as neutral_relay and record the tone in rhetorical_mode.

## How the trial worked

- **Posts:** the same 112 r/singularity posts for every run (`data/vanguard/r1-split-trial-posts.csv`).
- **Coders:** three models from different companies (Claude, Gemini, GPT-6 Astra), each blind
  to the others' codes, as section 9 now requires.
- **Each rule tested alone.** One run had today's codebook plus R1a; a second run had today's
  codebook plus R1b. Each run is the other's comparison: the R1b run is "today's codebook
  without R1a" for stance, and the R1a run is "today's codebook without R1b" for attribution.
  Same posts, same day, same models; only the rule under test differs.
- **Measure:** Cohen's kappa for each pair of models, which is agreement corrected for what
  chance alone would produce (1 is perfect, 0 is chance). Your test: a field is unreliable if
  every pair is below 0.6, or if no two models agree on more than 15% of posts.
- **How much chance could move the numbers:** each comparison rests on about 65 posts that
  both models in a pair found eligible, so a difference of 0.1 can be noise. The posts were
  resampled 2,000 times (`scripts/vanguard_r1_bootstrap.py`); the ranges below are the middle
  90% of those resamples.

## R1a: whether the poster agrees

| model pair | without R1a | with R1a | change (90% range) | R1a higher in |
|---|---|---|---|---|
| Claude–Gemini | 0.45 | **0.78** | +0.32 (+0.13 to +0.51) | 100% of resamples |
| Claude–GPT | 0.50 | **0.74** | +0.24 (+0.05 to +0.44) | 97% |
| Gemini–GPT | 0.53 | **0.65** | +0.13 (−0.11 to +0.37) | 82% |

- **Without R1a the field fails your test** under today's codebook: every pair is below 0.6.
  With R1a every pair is at or above 0.65, and every post has at least two models agreeing
  (none left unsettled, against 4% without).
- **The gain is clear in the two pairs that include Claude** and likely, but not certain,
  between Gemini and GPT.
- **For reference**, under the original codebook (before R2 and R3, run 2026-10-03) the three
  pairs were 0.42, 0.35 and 0.71.

**Where the models still disagree with R1a (14 of 112 posts).** About nine of the fourteen are
posts whose only words are a reaction or a joke, and the models read them differently:

- Gemini counts a reaction as agreement where Claude and GPT don't: "HOLY SHIT" over a
  benchmark chart, "This little shit", "Grok, I wasn't familiar with your game.", "Grok is
  openly rebelling against its owner".
- GPT counts a reaction as passing it on where Claude and Gemini read agreement: "This… could
  be something…", "I'm not even excited for Grok 4 anymore", "AI is coming in fast".

The added sentence speaks to exactly these cases. It has not been tested on its own, so the
refined rule's agreement is expected to be at least as good as above but is not measured.

## R1b: whose claim it is

| model pair | without R1b | with R1b | change (90% range) | R1b higher in |
|---|---|---|---|---|
| Claude–Gemini | 0.77 | 0.83 | +0.06 (−0.07 to +0.20) | 77% of resamples |
| Claude–GPT | 0.75 | 0.72 | −0.02 (−0.17 to +0.12) | 38% |
| Gemini–GPT | 0.78 | 0.75 | −0.03 (−0.17 to +0.10) | 33% |

- **The field passes your test either way**, with every pair at 0.72 or above.
- **The rule doesn't move agreement:** one pair up a little, two down a little, every range
  spanning zero. Under the original codebook the pairs were 0.72, 0.66 and 0.80.
- **Its remaining disagreements are the same reaction posts** ("WTF", "What the hell bruh",
  "This is objectively hilarious"): the models can't agree on whether a screenshot with a
  one-word reaction has a source. A rule about sources doesn't settle that; the R1a sentence
  above may help indirectly.
- Rejecting R1b leaves attribution coded as the codebook already says, which is how it
  reached 0.75 or better here.

## Cautions

1. **Optimistic by construction.** These rules were written from disagreements on these same
   posts, so they will look better here than on new posts. Section 9 already requires any
   adopted rule to be checked again on a fresh sample.
2. **Small numbers.** About 65 posts per pair. The ranges above say how far that goes: the
   stance result is solid in two pairs and likely in the third; the attribution result is
   "no detectable effect", not "proven useless".
3. **The models vary from run to run.** Between Gemini and GPT, stance agreement was 0.71
   under the original codebook and 0.53 under today's codebook without R1a. Some of that is
   the R2 and R3 changes, some is chance; the trial design compares runs from the same day to
   keep it out of the R1a and R1b comparisons.

## Also from today: the first rules trial now has all 140 posts

Gemini coded the last 28 posts of the earlier trial (R1, R2 and R3 together). On all 140
posts, the results you ruled on yesterday mostly hold, with one change worth knowing:

- **Hedging under R3, between Gemini and GPT: 0.56 before, 0.56 after** (on 112 posts it had
  been 0.55 → 0.62). The field still passes your test because Claude–Gemini reaches 0.77, but
  the cleanest pair now shows no gain from R3. You adopted R3 on 2026-10-03; this doesn't
  call for reversing it, but the fresh-sample check should look at hedging closely.
- What the main claim is about (R2): 0.57 → 0.82, 0.62 → 0.85, 0.75 → 0.79. Unchanged in
  substance.

Full numbers: `docs/vanguard/pilot-report-r-singularity-2026-10.md`.

## What happens after your ruling

The full-sample run (all 390 posts, Gemini and GPT, under the final codebook) can start as soon
as you rule here, once the OpenAI account has about $15 more credit. Gemini's share is
about $9.80, inside the approved $15 for the first month. Today's trial runs cost $6.28
against the quote's $6.30 for this work.
