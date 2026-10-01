# Codebook

How each statement in `data/statements.csv` is coded. Written from the kickoff plan
(`docs/2026-09-30-kickoff.md`, 2026-09-30). Any change to a code or a rule goes in
`docs/amendments.md` with a date and a reason.

**About the worked examples.** The examples below are made up to show how a code is
applied. They are not quotes from real people and must never be cited as quotes. Real
examples drawn from the seed data can replace them once the seed has passed its check.

---

## 1. question_frame: which question is the speaker answering?

One value per statement. When a statement touches several questions, code the one it
**leads with**: the one the speaker is mainly answering, usually the one the
interviewer asked or the one the headline claim is about. Write the others in `notes`
as `also: timeline, post_agi`.

### `possibility`: can AGI be built at all, in principle?

The statement is about whether machines can ever match general human intelligence,
not about when.

- *Example A (constructed):* "There is nothing magic about the brain. It is a physical
  system, and in principle we can build machines that do everything it does."
  → `possibility`, stance `cautious` or `expectant` depending on what follows. No date,
  so `timeline_type: none`.
- *Example B (constructed):* "Computers manipulate symbols; they will never understand
  anything, however fast they get."
  → `possibility`, stance `dismissive`, `timeline_type: qualitative`,
  `timeline_text: "never"`.

Test: if you deleted every date from the statement, would the claim still be the
whole point? If yes, and the claim is about whether it can be done at all, it is
`possibility`.

### `timeline`: when will it arrive?

The statement's main content is a date, a range, a probability by a year, or a
qualitative "soon" or "decades away".

- *Example A (constructed):* "I'd put it at about a 50% chance by 2040."
  → `timeline`, `timeline_type: prob_by_year`, `timeline_year: 2040`,
  `timeline_prob: 0.5`.
- *Example B (constructed, said in 2015):* "We're nowhere near it. Fifty years at the
  very least, maybe never."
  → `timeline`, `timeline_type: qualitative`, `timeline_year: 2065` (computed: 2015 + 50,
  and say so in `notes`), `timeline_text: "Fifty years at the very least, maybe never"`,
  stance `skeptical`.

A statement that both gives a date and argues that the thing is possible is coded
`timeline` if the date is the headline, `possibility` if the argument is.

### `capability_now`: is the current system already AGI, or close to it?

The statement is about a system that exists at the time of speaking.

- *Example A (constructed):* "Honestly, this model is a weak form of AGI already. It
  can do most office tasks I throw at it."
  → `capability_now`, stance `expectant`. `definition_note: "most office tasks"`.
- *Example B (constructed):* "These chatbots are autocomplete. They don't understand
  the world and they're not on the road to general intelligence."
  → `capability_now`, stance `dismissive` (or `skeptical` if the speaker allows that
  a different approach could get there).

Note: a statement that current systems are *not* close is still `capability_now`.
The frame is the question, not the answer.

### `self_improvement`: can the current system improve itself, or is it about to?

The statement is about AI doing AI research, building its successor, or a fast
feedback loop of self-improvement (often called an "intelligence explosion").

- *Example A (constructed):* "Our models are already writing a large share of the code
  for the next models. The loop is starting."
  → `self_improvement`, stance `expectant` or `alarmed` depending on tone.
- *Example B (constructed):* "The idea that a system will rewrite itself into a god
  overnight is science fiction. Progress needs data and hardware, not just cleverness."
  → `self_improvement`, stance `skeptical`.

Only code `self_improvement` when the speaker is talking about current or imminent
systems, or explicitly about the mechanism of self-improvement. A general warning
that "superintelligence could be dangerous" without that mechanism is `post_agi`.

### `post_agi`: what happens after, assuming it arrives?

Risk, the economy, control, meaning. These statements are collected only when they
also give a timeline or touch one of the collected questions (see the sampling rule
in `methodology.md`), so this frame will be under-counted on purpose.

- *Example A (constructed):* "When we get to superhuman AI, probably within 20 years,
  the hard problem will be keeping it under control."
  → `post_agi` if the control problem is the point, with `also: timeline` in notes and
  the timeline fields filled (`range` or `point_year`, 20 years from the statement
  date). Stance `alarmed`.
- *Example B (constructed):* "AGI will make goods and services nearly free within a
  generation of its arrival."
  → `post_agi`, stance `expectant`, `timeline_type: none` unless an arrival date is given.

### `definition`: what would even count as AGI?

The statement is mainly arguing about the term itself.

- *Example A (constructed):* "There's no such thing as general intelligence. Humans
  are specialised too. The right goal is human-level AI in specific respects."
  → `definition`, stance depends on the rest (often `skeptical`).
  `definition_note: "rejects 'general'; prefers human-level"`.
- *Example B (constructed):* "By AGI I mean a system that can do any job a remote
  worker can do, at the same quality."
  → `definition`, `definition_note: "any remote-worker job"`. If a date follows and
  is the headline, code `timeline` instead and keep the definition in `definition_note`.

---

## 2. stance: how is the speaker positioned toward the prospect?

Independent of the timeline. Two people who both say "2030" can hold opposite stances.
Code the stance shown **in this statement**, not the speaker's reputation.

### `dismissive`: AGI talk is hype or confusion

- *Constructed:* "AGI is a marketing term. Nobody serious works on it."
- *Constructed:* "Asking when AGI arrives is like asking when the perpetual motion
  machine arrives."

### `skeptical`: far off, or much harder than claimed

The speaker takes the goal seriously but thinks it is distant or that current methods
will not get there. Differs from `dismissive` in that the question is treated as real.

- *Constructed:* "We'll get there eventually, but not with scaling up today's models.
  Several breakthroughs are missing."
- *Constructed:* "Not in my lifetime, and probably not in my children's."

### `cautious`: plausible but uncertain, resists firm dates

- *Constructed:* "It could be ten years or fifty. Anyone giving you a date is guessing."
- *Constructed:* "I wouldn't rule out something like it this decade, but I wouldn't
  bet on it either."

### `expectant`: it is coming, and that is good

- *Constructed:* "By the end of this decade we'll have systems smarter than us, and
  they'll cure diseases we've struggled with for centuries."
- *Constructed:* "We're on track. I'm excited about what it means for people."

### `alarmed`: it is coming, and that is worrying

- *Constructed:* "I think it's coming much sooner than I thought, and I don't think we
  know how to control it."
- *Constructed:* "There's a real chance this goes very badly, and soon."

### `resigned`: it is coming whatever anyone wants

The speaker treats arrival as inevitable and outside anyone's control, without a clear
welcome or alarm, or with both cancelling out.

- *Constructed:* "Whether we like it or not, someone is going to build it. The
  incentives are too strong to stop."
- *Constructed:* "You can't put this back in the box. It's going to happen; the only
  question is who does it."

**Ties between stances.** When a statement mixes welcome and worry (common for lab
leaders), code the one given more weight and set `coding_confidence: medium`. Do not
invent a blend.

---

## 3. timeline fields

| field | rule |
|---|---|
| `timeline_type` | `point_year` (one year), `range` (low and high year), `prob_by_year` (a probability by a year), `qualitative` (words only, e.g. "soon", "never", "decades"), `none` (no timing claim at all) |
| `timeline_year` | an absolute year. When the speaker says "in 10 years", add it to the year of the statement and say so in `notes` (`computed: 2023 + 10`). For `qualitative`, fill it only when the words imply a number ("a decade" yes, "soon" no). |
| `timeline_year_high` | only for `range`. |
| `timeline_prob` | a number from 0 to 1. "Even odds" is 0.5. Leave blank if none given. |
| `timeline_text` | the speaker's own words for the timing, short, verbatim. Always fill it when a hedge is present, even if the year fields are filled. |

**Which arrival?** Record the timeline for the thing the speaker calls AGI, human-level
AI, or equivalent. If they give a date for something else (passing a test,
superintelligence, the Singularity), record it, and say exactly what in
`definition_note`, e.g. "Turing test pass" or "Singularity, not AGI".

---

## 4. Other fields and conventions

- **`date`** is when the statement was made, if known; otherwise when it was published.
  Its form must match `date_precision`: `YYYY-MM-DD` for `day`, `YYYY-MM` for `month`,
  `YYYY` for `year`.
- **`quote`** is verbatim, 60 words or fewer. Use "..." for cuts inside the quote.
  Never stitch together sentences from different places.
- **`definition_note`** records what the speaker seems to mean by AGI in this
  statement, if they say. Leave blank rather than guess.
- **`coding_confidence`** is `high` when the frame and stance are obvious and the
  source is primary; `medium` when one of them needed judgment; `low` when both did,
  or the source is secondhand.
- **Primary and secondhand.** A source is *primary* when it carries the speaker's own
  words in something they produced or took part in: their book, paper, blog, post, a
  recorded talk, a transcript, or an interview with direct quotes. It is *secondhand*
  when it is someone else's report or paraphrase ("Hinton reportedly believes"), or a
  quote we could not trace back to where it was said. Secondhand rows must carry the
  tag `secondhand` in `notes` and `coding_confidence: low`, and get replaced when the
  primary source turns up. `scripts/validate.py` enforces this.
- **`notes` tags.** Notes start with any of these tags, separated by `; `, followed by
  free text:
  - `secondhand`: see above.
  - `incidental`: found while searching for a different speaker (sampling rule 4).
  - `sampled`: kept under the every-third rule for a busy year (sampling rule 3).
  - `also: <frame>, <frame>`: the other questions the statement touches.
  - `computed: <working>`: how an absolute year was worked out from a relative one.
- **`coder`** is `john` or `claude-agent`.
