# Leg B ledger: first reading, 9 October 2026

Method: `docs/leg-b-ledger-method.md` (committed before any row was built). Rows:
`data/leg_b_ledger.csv`. Numbers: `python3 scripts/leg_b_ledger.py`. Every verdict is the
agent's judgement; the rows record the evidence and the gap so John can overrule any one.

## The answer

The 2016 survey's milestones did not mostly arrive early. Of the 32:

| verdict | count |
|---|---|
| arrived (every stated condition met) | 1 |
| arguably arrived (main capability met, one condition untested or nearly met) | 9 |
| not arrived | 18 |
| left for John (the description sets no bar to check against) | 4 |

Of the 18 not arrived, 9 are past their forecast date, so they are already late, and 9 are
not yet due.

Counting the 9 "arguably arrived" milestones as arrived, 19 forecasts can be judged so far:
**9 came early and 10 came late** (one arrived late, nine are overdue and still not here).
Counting only the one clean arrival, 1 came early and 16 are late. Either way, the sentence
in the singularity definition, that the survey's milestones "mostly arrived early", is not
supported by this ledger.

What does show is a split by kind of task:

- **Early:** speech, writing code, answering open-ended questions, exams, poker, Atari,
  video and maths. Six arrived in about half to four-fifths of the forecast time (ratios
  0.56 to 0.84). Three came far earlier: all Atari games (3.8 years against a forecast of
  8.8), realistic video from a new viewpoint (3.7 against 11.6) and the Putnam maths
  competition (9.4 against 33.8). The one arrival that came late was answering factual
  questions from the internet (8.8 years against 7.2), and that date may be too late, see
  below.
- **Late:** robots in the physical world (folding laundry, assembling LEGO), beating the
  best people at particular games (StarCraft, Angry Birds), learning a game from very little
  play, and phone banking. Angry Birds was forecast for 2019 and is at least seven years
  late.

So the experts were too slow on what large language and speech models went on to do, and
too fast on robots and on narrow game-playing goals that the field stopped chasing.

## Scored by lead time

The ratio is actual time divided by forecast time; under 1 is early.

| forecast lead | early | late | overdue, not arrived | not yet due | not scored |
|---|---|---|---|---|---|
| under 5 years | 1 | 0 | 1 | 0 | 0 |
| 5 to 10 years | 6 | 1 | 7 | 0 | 2 |
| 10 years or more | 2 | 0 | 1 | 9 | 2 |

(Generous reading. Seven of the ten arrivals came within a factor of two of their
forecast; the three outside it all came early: Atari, video from a new viewpoint, and the
Putnam.)

The forecasts of five to ten years ahead are the ones that can be checked now, and they
split evenly: 7 arrived (6 early, 1 late) against 7 overdue. Most longer forecasts are not
yet due. There are too few yes-or-no events to find a lead beyond which the forecasts stop
working, so this ledger records which way the forecasts missed. It does not give a
forecast horizon.

## Where the agent's judgement matters most

- **Every arrival date means "no later than".** The survey asked when a milestone would be
  *feasible* for a top lab within a year, and only demonstrations can be seen. This leans
  every row towards "late".
- **The nine "arguably arrived" rows decide the picture.** Each names its gap: poker beat
  elite professionals but never won the World Series tournament; the Putnam score was the
  maker's own grading of a past exam without the time limit; text-to-speech was judged by
  ordinary listeners rather than experts.
- **Three weak "not arrived" verdicts** (translation as good as an amateur bilingual, phone
  banking, recognising an object from one picture) rest on not finding a published
  comparison with people, not on evidence the capability is missing. The factual-questions
  date (April 2025) is weak in the same way: an earlier demonstration may exist.
- **Atari disagrees with the 2023 scoring** for AI Impacts, which said not met. Agent57
  (March 2020) beat the professional games tester's scores on all 57 games; the 2023 page
  gives no reason.

## Open questions for John

1. The four milestones left unscored (sorting long lists without the form of the solution,
   grouping unseen objects, answering questions with no definite answer, explaining game
   moves): give each a bar, or keep them out.
2. The nine "arguably arrived" rows: which count as arrived?
3. The singularity definition's sentence "Milestones from the 2016 Grace survey mostly
   arrived early" is not supported by this ledger. Change it (an amendment), or wait for his
   ruling on question 2?
4. Leg B's gauge is defined on forecasts of METR's task-length measure, which this ledger
   cannot supply. Is this ledger the record of which way forecasts missed and nothing more,
   or should it feed the gauge somehow?
