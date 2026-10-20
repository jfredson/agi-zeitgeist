# Leg B ledger: first reading, 9 October 2026

Method: `docs/leg-b-ledger-method.md` (committed before any row was built). Rows:
`data/leg_b_ledger.csv`. Numbers: `python3 scripts/leg_b_ledger.py`. Every verdict is the
agent's judgement; the rows record the evidence and the gap so I can overrule any one.
Revised the same day after an independent check of the pull request, and closed by my
rulings of 12 October 2026 (both at the end).

## The answer

The singularity definition said the 2016 survey's milestones "mostly arrived early". The
ledger does not support that as written. Every milestone that has arrived came early, but
more milestones are past their forecast date and still not here than have arrived at all.
(The sentence was amended on 12 October 2026, amendment A23 in `docs/amendments.md`; see
the rulings at the end.)

| verdict | count |
|---|---|
| arrived (every stated condition met) | 1 |
| arguably arrived (main capability met, exactly one condition unmet or untested) | 5 |
| not arrived | 22 |
| no bar (the description sets nothing a demonstration could be checked against) | 4 |

Of the 22 not arrived, 11 are past their forecast date, so they are already late, and 11
are not yet due.

Counting the 5 "arguably arrived" milestones as arrived, 17 forecasts can be judged so far:
**6 came early and 11 are late**, and all 11 late ones are milestones that are overdue and
have not arrived. Counting only the one clean arrival, 1 came early and 16 are late. So the
totals tip late only because overdue milestones count as late. Of the arrivals alone, all
came early.

The split is by kind of task:

- **Early:** transcribing speech, reading text aloud, writing simple code, answering
  open-ended questions from the internet, poker and Atari. Four arrived in about half to
  four-fifths of the forecast time (ratios 0.56 to 0.80). Two came far earlier: all Atari
  games (3.8 years against a forecast of 8.8) and poker (0.6 years against 3.6).
- **Late:** robots in the physical world (folding laundry, assembling LEGO), beating the
  best people at particular games (StarCraft, Angry Birds), learning a game from very little
  play, phone banking, translation, recognising an object from one picture, and two that
  have demonstrations with more than one gap (the high-school essay and answering factual
  questions from the internet). Angry Birds was forecast for 2019 and is at least seven
  years late.

So the experts were too slow on what speech and language models went on to do, and too
fast on robots and on narrow game-playing goals that the field stopped chasing.

## What the headline rests on

Four rows were "arguably arrived" in the first draft and are now "not arrived", because
each names more than one unmet or untested condition and the method allows only one:
video from a new viewpoint, the Putnam maths competition, the high-school essay, and
answering factual questions from the internet. Two of them (video and Putnam) are not yet
due, so moving them changes no early-or-late count. The other two are overdue either way
unless their dates count.

The factual-questions row matters most. Its only demonstration is from April 2025, and the
agent found nothing earlier that compares a system with people who had internet access on
simple factual questions. Its forecast date is 9 September 2023. If I count it as
arrived and an earlier demonstration dated before about September 2023 turns up, it moves
from late to early: 7 early and 10 late. If all four rows were counted with their current
dates, the totals go back to the first draft's 9 early and 10 late. Either way, the
milestones that arrived mostly came early, and the overdue ones are what tip the totals.

## Scored by lead time

The ratio is actual time divided by forecast time; under 1 is early.

| forecast lead | early | late, arrived | overdue, not arrived | not yet due | not scored |
|---|---|---|---|---|---|
| under 5 years | 1 | 0 | 1 | 0 | 0 |
| 5 to 10 years | 5 | 0 | 9 | 0 | 2 |
| 10 years or more | 0 | 0 | 1 | 11 | 2 |

(Generous reading. Four of the six arrivals came within a factor of two of their forecast;
the two outside it, Atari and poker, both came far earlier.)

The forecasts of five to ten years ahead are the ones that can be checked now: 5 arrived,
all early, and 9 are overdue. Most longer forecasts are not yet due. There are too few
yes-or-no events to find a lead beyond which the forecasts stop working, so this ledger
records which way the forecasts missed. It does not give a forecast horizon.

## Where the agent's judgement matters most

- **Every arrival date means "no later than".** The survey asked when a milestone would be
  *feasible* for a top lab within a year, and only demonstrations can be seen. This leans
  every row towards "late".
- **The one-condition rule decides four rows.** A row whose demonstration meets the main
  capability but has two or three gaps fits none of the method's four verdicts exactly:
  "arguably arrived" allows one gap, and "not arrived" is written for no demonstration of
  the main capability. The agent put these rows under "not arrived", with the demonstration
  recorded as the nearest. That is the strict reading of the method, and the method text is
  unchanged.
- **Which gaps count is itself a judgement.** Things the milestone does not state (for
  example, that a code model learned from public code including sorting routines) are
  noted in the rows but not counted as gaps.
- **Earlier demonstrations that did not qualify.** Microsoft's speech system matched
  professional transcribers on telephone conversations in October 2016, but leaves both
  noise and a variety of accents untested, so Whisper (September 2022) still sets the date.
  Microsoft's March 2018 translation system beat non-professional translators, the
  milestone's own bar, but for Chinese news only, so translation stays not arrived.
- **Three weak "not arrived" verdicts** (translation, phone banking, recognising an object
  from one picture) rest on not finding a published comparison with people, not on
  evidence the capability is missing.
- **Atari disagrees with the 2023 scoring** for AI Impacts, which said not met. The agent
  read "all Atari games" as the standard 57-game test set; Agent57 (March 2020) beat the
  professional games tester's scores on all 57. The 2023 page gives no reason, and that
  reading may be the difference.

## Rulings (2026-10-12)

These were the open questions put to me on 9 October. He ruled on 12 October 2026, in his
words "all as recommended": each answer below was the session's recommendation and I
approved it, so the authorship is mixed. The questions are kept as they were asked.

1. The four milestones left unscored (sorting long lists without the form of the solution,
   grouping unseen objects, answering questions with no definite answer, explaining game
   moves): give each a bar, or keep them out.

   **Ruling:** keep them out. They stay out of the scores and their verdict is recorded as
   "no bar" (it was "left for me" until this ruling). A bar set now would be chosen after
   seeing the answers, which is the thing the method was written to avoid.

2. The five "arguably arrived" rows: which count as arrived?

   **Ruling:** none is promoted. The five rows stay "arguably arrived", and the strict total
   (only clean arrivals count) and the generous total (arguably arrived counts too) both
   keep being reported, as the method says.

3. The one-condition rule: should the method get a fifth verdict (for example "partly
   arrived") for a demonstration of the main capability with more than one gap, or allow
   more than one gap under "arguably arrived"? Either is an amendment, and either would
   bring back the four rows moved on 9 October.

   **Ruling:** no fifth verdict. The one-condition rule stays as written, and the four rows
   moved on 9 October (video from a new viewpoint, the Putnam, the high-school essay,
   answering factual questions from the internet) stay "not arrived" with their nearest
   demonstration recorded.

4. The singularity definition's sentence "Milestones from the 2016 Grace survey mostly
   arrived early" holds for the milestones that arrived, but not for the survey as a whole.
   Reword it (an amendment), or wait for the rulings above?

   **Ruling:** amend it now, dated. The sentence now says that the milestones that arrived
   came early, that most of the survey's milestones have not arrived, and that eleven are
   overdue. Recorded as amendment A23 in `docs/amendments.md`, citing this ledger.

5. Leg B's gauge is defined on forecasts of METR's task-length measure, which this ledger
   cannot supply. Is this ledger the record of which way forecasts missed and nothing more,
   or should it feed the gauge somehow?

   **Ruling:** the record of which way forecasts missed, and nothing more. Leg B's gauge
   stays defined on the task-length measure, and this ledger does not feed it.

## Revisions after the independent check (9 October 2026)

- Poker re-dated to Libratus, whose match against four top heads-up professionals ended
  30 January 2017 (Carnegie Mellon's news release; Science paper). Pluribus (July 2019) is
  kept in the row as the later, broader result.
- Speech transcription checked against Microsoft's October 2016 human-parity paper and left
  on Whisper, because the Microsoft result leaves two conditions untested.
- Four rows moved from "arguably arrived" to "not arrived" under the one-condition rule.
- Translation now records Microsoft's March 2018 Chinese-to-English result as its nearest
  demonstration.
- Atari now states the 57-game reading.
- Putnam: the "top human score was 90" figure is the maker's comparison, found only in news
  coverage; the agent could not open the competition organiser's results page.
