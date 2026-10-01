# Codebook, version 2

How each coded unit is coded. Written 2026-09-30 and revised 2026-10-01 (amendment A14) from `docs/methodology-v2.md`
section 2, which is the authority; this file turns its rules into decisions with
examples. Changes go in `docs/amendments.md` first.

Version 1 (the single `stance` code and the six-value `question_frame`) is retired.
Rows coded under version 1 were recoded from their sources, not mapped (amendment A2).

**About the examples.** Examples marked *constructed* are invented to show a rule and
must never be cited as quotes.

---

## 0. One unit, and how to read it

A unit is one statement by one speaker on one occasion. Code **only what the quoted
words and their immediate context say**. Don't use what the speaker is known for,
what they said elsewhere, or what the article around the quote implies.

Read the source, not just the stored quote. The stored quote (60 words or fewer) is
evidence for the codes. If a code depends on a sentence outside the stored quote,
either change the quote to include it or code `unexpressed` / `ambiguous`.

---

## 1. target_capability: what capability is the unit about?

| code | the capability | typical words |
|---|---|---|
| `conversation` | passes as human in conversation | Turing test, can't tell it from a person |
| `narrow_task` | one specific task or domain | chess, driving, radiology, coding contests |
| `broad_competence` | most economically valuable or intellectual work; "AGI", "human-level AI" when used this way | AGI, human-level, do any job a person can |
| `superintelligence` | exceeds humans broadly | superintelligence, smarter than us at everything, the Singularity (when it means AI beyond humans) |
| `si_assist` | AI helps **humans** build AI | AI speeds up our researchers, copilots for ML engineers |
| `si_research` | AI does **parts** of AI research on its own | AI runs experiments, writes the training code, automated AI researcher for some tasks |
| `si_modify` | AI changes **its own** code or weights | rewrites itself, modifies its own weights |
| `si_sustained` | successive improvements with little human involvement | intelligence explosion, recursive self-improvement, "takeoff", each generation builds the next |
| `none` | no capability is claimed | a statement about the word "AGI", about hype, about policy with no capability in view |

**Choosing among them.** Pick the capability the speaker's claim is about. If they
name two (for example "human-level by 2029, Singularity by 2045"), code the one the
unit leads with and record the other in `definition_note`.

**The four self-improvement levels.** Ask two questions in order:

1. *Who does the improving?* Humans with AI help → `si_assist`. The AI itself → go on.
2. *How far does it go?*
   - A part of the research pipeline, with humans still steering → `si_research`.
   - The system edits itself (its own code or weights) → `si_modify`.
   - Repeated rounds, each better system making the next, with little human role →
     `si_sustained`.

**"Takeoff" and loose self-improvement words (ruling 12, A14).** Code the lowest level
the words support and set `ambiguous: yes`; put any speed the speaker gives ("slow",
"fast", "gentle") in `timeline_text`. When the words don't say who does the improving
(a bare "takeoff", "the AI will improve itself"), the lowest level is `si_assist`.
Code `si_sustained` only when the words themselves describe repeated rounds with little
human role ("each generation builds the next", "an intelligence explosion with no one
in the loop"). The labels "recursive self-improvement" and "intelligence explosion"
alone don't do that.

- *Seed example, `altman-2023-04`:* Altman told the New York Times it would be a "very
  slow takeoff". The words don't say who improves the systems or how, so
  `target_capability: si_assist`, `ambiguous: yes`, `timeline_text: "very slow
  takeoff"`.

- *Constructed:* "Our engineers now write most of their code with model help." →
  `si_assist`.
- *Constructed:* "The model ran the ablation studies overnight without anyone." →
  `si_research`.
- *Constructed:* "Once a system can rewrite its own weights, all bets are off." →
  `si_modify`, `present_capability: hypothetical`.
- *Constructed:* "Each generation will design the next, faster than we can follow." →
  `si_sustained`.

---

## 2. frame_primary and frames_present: which questions does the unit raise?

| code | the question |
|---|---|
| `possibility` | Can it be built at all, in principle? |
| `timeline` | When will it arrive? |
| `capability_now` | Is a current system already it, or close? |
| `self_improvement` | Can current or imminent systems improve themselves? |
| `definition` | What would count? |
| `consequences` | What happens if or when it arrives (risk, economy, society)? |
| `governance` | What should be done about it (regulation, pauses, safety work, coordination)? |
| `other_concern` | A different AI question leads: jobs, reliability, privacy, bias, misinformation, military, consciousness, ownership |

- `frame_primary` is the question the unit **leads with**: what the speaker is mainly
  answering, usually what they were asked or what the headline claim is about.
- `frames_present` lists **every** question raised, separated by `;`, and always
  includes `frame_primary`. A question counts as present when the unit raises it,
  whatever answer is given ("it's not close" raises `capability_now`).
- `concern_tag` is required when `other_concern` is present (one of `jobs`,
  `reliability`, `privacy`, `bias`, `misinformation`, `military`, `consciousness`,
  `ownership`, `other`), and blank otherwise.
- A unit framed as self-improvement should normally have an `si_*` target; if it
  doesn't, say why in notes.

Test for `possibility` against `timeline`: delete every date from the unit. If the
claim still stands and is about whether it can be done, it's `possibility`.

---

## 3. endorsement: does the speaker endorse that the target capability will exist?

Endorsement is about the **future**: whether the capability will exist, ever or by the
horizon the speaker names (ruling 9, A14). Whether it exists **now** is a different
field, `present_capability`.

| code | meaning |
|---|---|
| `accepts` | says it will happen (or has already happened). Needs "will", "expect", "I think", a stated probability of 50% or more, a bet, or "decades away" (rulings 10 and 11) |
| `rejects` | says it won't happen, ever or by the horizon given. "It isn't here yet" is **not** a rejection (ruling 9) |
| `uncertain` | explicitly says they don't know, or gives even odds |
| `conditional` | endorses it only if a stated condition holds ("if scaling continues", "if we solve X") |
| `unexpressed` | discusses it without taking a position |

**Silence is never acceptance.** Endorsement is coded only from words the speaker
actually said. Every code other than `unexpressed` needs an anchor: the exact words
in the stored quote that carry the position, recorded in notes as
`basis: "<words copied from the quote>"`. `scripts/validate.py` checks that the
anchor appears in the quote. If you can't point to such words, the code is
`unexpressed`.

Rulings of 2026-10-01 (A14), with examples from the seed data:

- **Not here yet (ruling 9).** Denying that the capability exists now is
  `present_capability: disputed`. Endorsement then comes from what the speaker says
  about the future, or is `unexpressed` if they say nothing about it.
  *Seed example, `lecun-2017-02`:* "We're very far from having machines that can learn
  the most basic things about the world in the way humans and animals can do." This
  denies present capability and says nothing about whether such machines will come, so
  `present_capability: disputed`, `endorsement: unexpressed` (it was `rejects` before
  the ruling).
- **Hedged dates (ruling 10).** "May", "might" or "could" with a date is `uncertain`.
  Fill the timeline fields anyway and keep the hedge in `timeline_text`. When a hedge
  and an acceptance word govern the same date, the hedge decides (agent interpretation,
  noted in A14).
  *Seed example, `hinton-2023-06`:* "Now, I think we may be much closer, maybe only five
  years away from that." → `endorsement: uncertain` (basis `"maybe only five years
  away"`), `timeline_type: qualitative`, `timeline_year: 2028` (`computed: 2023 + 5`),
  `timeline_text: "maybe only five years away"`.
- **"Decades away" (ruling 11)** is `accepts` with `timeline_type: qualitative`; leave
  `timeline_year` blank unless a number of decades is given.
  *Seed example, `marcus-2022-04`:* "we are still likely decades away from
  general-purpose, human-level AI" → `endorsement: accepts` (basis `"still likely
  decades away"`), `present_capability: disputed`, `timeline_type: qualitative`,
  `timeline_text: "still likely decades away"`.
- **Self-improvement words (ruling 12):** see section 1.

Hard cases:

- **Giving a date usually carries endorsement, but check the words.** "AGI by 2029"
  with "will" or "I think" anchors `accepts`. "People say 2029; who knows" is
  `uncertain` (basis `"who knows"`) or `unexpressed`.
- **Worrying about something is not endorsing it.** "If superintelligence arrives it
  could end us" is `conditional` at most, and `unexpressed` if no arrival claim is
  made. Writing about regulation does not establish that the author accepts
  feasibility.
- **Rejecting a near date is not rejecting the capability.** "Not by 2027" →
  `rejects` for that horizon only; record the year with the `not_by` tag (section 5)
  and say in notes whether the speaker accepts it eventually. If the same unit also
  says "but it will come eventually", code `accepts` with the hedge in
  `timeline_text`; set `ambiguous: yes` if the two are balanced.
- **Probabilities.** A stated probability of 50% or more by a date → `accepts` with
  `timeline_prob` filled (ruling 10). Below 50%, or a wide spread stated as such →
  `uncertain`.
- **Jokes and sarcasm** → `unexpressed` and `ambiguous: yes`, unless the speaker
  explains the joke.

## 4. present_capability: does it exist now, in the speaker's view?

| code | meaning |
|---|---|
| `demonstrated` | the speaker says it already exists and points to it |
| `claimed` | the speaker says it exists, without pointing to evidence |
| `disputed` | the speaker says current systems do **not** have it |
| `hypothetical` | discussed as a future or possible capability |
| `na` | no capability in view (target `none`) |

`na` exactly when `target_capability` is `none`.

## 5. Timeline fields

As in version 1, with three tags (in notes) for claims that aren't arrival dates:

| field | rule |
|---|---|
| `timeline_type` | `point_year`, `range`, `prob_by_year`, `qualitative`, `none` |
| `timeline_year` | an absolute year; for "in 10 years" add it to the statement year and record `computed: 2023 + 10` in notes |
| `timeline_year_high` | only for `range` |
| `timeline_prob` | 0 to 1, only when the source gives a probability. "Soon" is never converted to a number |
| `timeline_text` | the speaker's own words for the timing, always filled when a hedge is present |

- **`not_by: YYYY`** for "it won't happen by YYYY". Leave `timeline_year` blank and code
  `timeline_type: qualitative`. These are not arrival dates and charts must not plot
  them as such.
- **`lower_bound`** for "at least N years" or "no sooner than YYYY". Fill
  `timeline_year` with the bound and add the tag.
- Proximity (distant, medium, near, present) is worked out when charts are drawn,
  never stored.

## 6. Consequences, affect and agency

| field | codes | rule |
|---|---|---|
| `consequence_type` | `existential`, `economic`, `social`, `mixed`, `unspecified` | the kind of consequence the unit expects. `unspecified` when none is named |
| `consequence_valence` | `beneficial`, `harmful`, `mixed`, `unspecified` | whether those consequences are good or bad in the speaker's words |
| `affect` | `enthusiasm`, `fear`, `resignation`, `neutral`, `mixed`, `unexpressed` | emotional posture, **only from explicit cues** ("exciting", "scary", "I'm worried", "nothing we can do"). A plain forecast is `unexpressed`, not `neutral`; use `neutral` only when the speaker signals detachment ("I'm just reporting the trend") |
| `agency` | `can_influence`, `cannot_influence`, `unexpressed` | does the speaker say the outcome can be shaped? "We must regulate" → `can_influence`; "it's coming whatever we do" → `cannot_influence` |

These are separate on purpose. Someone who expects AGI in five years can be thrilled,
frightened, resigned or organizing.

- *Constructed:* "AGI by 2030, and frankly it terrifies me, but good policy can still
  steer it." → `accepts` (basis `"AGI by 2030"`), `affect: fear`,
  `agency: can_influence`.
- *Constructed:* "It's coming whether we like it or not." → `accepts` (basis
  `"It's coming"`), `affect: resignation`, `agency: cannot_influence`.

## 7. elicitation: how did the statement come about?

| code | meaning |
|---|---|
| `unprompted` | the speaker chose to say it: their own blog, post, book, essay, talk |
| `interview` | answering a question in an interview, podcast or hearing |
| `survey` | answering a survey item |
| `quoted` | the unit is a claim quoted inside someone else's article, without the full exchange available |

Secondhand rows are usually `quoted`.

## 8. Other fields

- **`definition_note`**: what the speaker means by AGI in this unit, if they say.
- **`coding_confidence`**: `high` when the codes are clear and the source is primary;
  `medium` when one needed judgment; `low` when several did, or the source is
  secondhand.
- **`ambiguous`**: `yes` when the words support two codes equally. Kept as a code,
  never resolved by guessing. Say which field in notes.
- **`date`** must match `date_precision`: `YYYY-MM-DD`, `YYYY-MM` or `YYYY`.
- **`quote`**: verbatim, 60 words or fewer, "..." only within one passage.
- **Primary and secondhand.** Primary = the speaker's own words in something they
  produced or took part in (their writing, a transcript, a recorded talk, an interview
  with direct quotes by the outlet that did it). Secondhand = someone else's report or
  paraphrase, or a quote not traced to where it was said. Secondhand rows carry the
  `secondhand` tag and `coding_confidence: low`.
- **`coder`**: `john`, `claude-agent` (version 1, retired), or `claude-agent-v2`.

## 9. Notes tags

Notes start with any of these tags, separated by `; `, then free text:

| tag | meaning |
|---|---|
| `secondhand` | see section 8 |
| `incidental` | found while searching for a different speaker |
| `sampled` | kept under the every-third rule for a busy year |
| `computed: <working>` | how an absolute year was worked out |
| `basis: "<words>"` | the words carrying the endorsement (required unless `unexpressed`) |
| `not_by: YYYY` | "won't happen by YYYY" (section 5) |
| `lower_bound` | the timeline year is a minimum (section 5) |

## 10. Mapping to Fast and Horvitz 2017

Methodology-v2 section 5 asks for the categories of Fast and Horvitz's 2017 study of
New York Times AI coverage to be reconciled with these codes before the media stream
starts. That reconciliation belongs to the media stream and has not been done yet.
