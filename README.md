# AGI Zeitgeist Tracker

A dated, sourced record of how expert and public opinion about artificial general
intelligence (AGI: AI that can do most intellectual work a person can) has moved
from 2005 to the present. Every row links to where it came from, every search that
produced a row is logged, and the coding rules are written down, so anyone can
check the record or extend it.

The working question: did the main public argument move from *whether* AGI is
possible, to *when* it arrives, to *whether today's systems are already close or
improving themselves*? The method is built so the data can say no.

**Status (2026-09-30):** seed phase. Five people traced (Ray Kurzweil, Geoffrey
Hinton, Yann LeCun, Gary Marcus, Sam Altman), plus surveys, prediction markets,
polls and dated events. The full panel is not frozen yet.

## What's here

| path | what it is |
|---|---|
| `data/speakers.csv` | one row per person, survey, market, pollster or institution |
| `data/statements.csv` | one row per public statement, with a verbatim quote, link and codes |
| `data/aggregates.csv` | survey results, prediction market readings and poll results |
| `data/events.csv` | dated events (open letters, government actions, reports) for chart labels |
| `data/search_log.csv` | every search run to build the record, and what it found |
| `docs/methodology.md` | the method: what counts, how people are sampled, how searches run |
| `docs/codebook.md` | how each statement is coded, with worked examples |
| `docs/amendments.md` | dated changes to the panel or the codes |
| `docs/2026-09-30-kickoff.md` | the original plan |
| `scripts/validate.py` | checks every row: codes, dates, sources, links between files |
| `scripts/charts.py` | builds the charts from the CSV files |
| `site/` | chart images, and later a static page |

## How to cite

> Fredrickson, J. (2026). *AGI Zeitgeist Tracker* [dataset]. Version of
> <commit date>, commit <short hash>. https://github.com/<to be published>

Cite a specific commit: the data changes as rows are added, and a commit pins the
version you used. To cite a single statement, give its `statement_id`
(e.g. `hinton-2023-02`) along with the commit.

Licence: not chosen yet. Until one is added, ask before reusing.

## How to add a row

1. Read `docs/methodology.md` (especially the sampling rule) and `docs/codebook.md`.
2. Log your search first: add a row to `data/search_log.csv` with the exact query,
   where you searched, and the date.
3. Add the statement to `data/statements.csv`:
   - `statement_id` is `<speaker_id>-<year>-<NN>`, numbered in date order.
   - The quote is verbatim, 60 words or fewer, from the linked source.
   - Code `question_frame`, `stance` and the timeline fields as the codebook says.
   - If you only found someone else's report of the statement, tag `notes` with
     `secondhand` and set `coding_confidence` to `low`.
   - Put your name in `coder` (add it to `CODERS` in `scripts/validate.py`).
4. Go back to the search log row and fill `what_found` with the new statement id.
5. Run the checks and fix anything they report:

   ```
   python3 scripts/validate.py
   ```

6. New people can't be added without a dated entry in `docs/amendments.md`
   saying why: the panel is fixed so that it can't drift toward the story.

## Building the charts

```
python3 -m venv .venv && .venv/bin/pip install matplotlib
.venv/bin/python scripts/charts.py
```
