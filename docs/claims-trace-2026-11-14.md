# Claims trace: Sam Altman and Elon Musk, 2026-11-14

**Status: written 2026-11-14 by the agent, for the claims-ledger search task. Nothing in it is
ruled by John yet. It merges after pull request 58, which also adds rows to the end of
`data/search_log.csv`.**

## What was done

The claims ledger (`docs/claims-ledger-method.md`) keeps every dated prediction the industry's
leaders make about AI. Until today each person's claims were the ones earlier sessions happened
to find. The method says a person's latest forecast only counts as their latest if their record
has been searched year by year, every search written down, years with nothing found entered as
rows, and a final row, `<speaker_id>-claims-traced`, written when the search is complete. This
note records that search for the first two people, as the order of work says: Sam Altman, then
Elon Musk.

The task's wording, from before amendment A31 of 2026-10-19, says the search lets the claims page
show a hit rate in place of "seed only: not a rate". A31 dropped hit rates and that label, so no
rate appears anywhere, before or after this work. What changes on the page is set out below.

| | Altman | Musk |
|---|---|---|
| Claims before | 23 | 17 |
| Claims added | 26 | 87 |
| Claims now | 49 | 104 |
| Search-log rows added | 71 (`altman-claims-037` to `-106`, and `altman-claims-traced`) | 112 (`musk-claims-035` to `-145`, and `musk-claims-traced`) |
| Groups held for John | 4 | 8 |

Six existing Musk records gained a `repeated_on` date (he said the same thing again unchanged),
as the method's rule on repeats asks. No existing claim's words, test, date or verdict was changed.

## How the search ran

**Fixed searches, every year.** For each year the person held a qualifying role, the same
searches were run, whether or not an earlier one that year found anything:

- Altman, 2015 to 2026: `"Sam Altman" predicts AI <year>`; `"Sam Altman" "next year" AI <year>`;
  `"Sam Altman" AGI OR superintelligence "years" <year>`; `"Sam Altman" OpenAI release "this year" OR "next month" <year>`.
- Musk, 2015 to 2026: `"Elon Musk" predicts AI <year>`; `"Elon Musk" "next year" AI <year>`;
  `"Elon Musk" AGI OR superintelligence "years" <year>`; `"Elon Musk" self-driving "end of the year" OR "next year" <year>`;
  and a fifth on robotaxis, the Tesla robot and Grok.

**His own outlets and recordings.** Altman's blog was read post by post from December 2015.
Musk's recorded events were read in full: Tesla's earnings calls in his qualifying years (those
of late 2016 and early 2017 had no recording to be found), its shareholder meetings, Autonomy
Day, Battery Day, AI Day, "We, Robot", xAI's Grok launches, and the interviews the searches turned
up. Posts on X were read through a mirror of the post (api.fxtwitter.com), never x.com itself.

**A cross-check.** Every dated statement of each man already in `data/statements.csv` was
checked against the claim files. That found one Altman claim the searches had missed (TIME,
December 2023) and a dozen of Musk's dated forecasts of AGI or beyond that the ledger had not yet entered (row `musk-claims-144`).

**How the words were read.** YouTube refused direct caption downloads from this machine during
the session, so most recordings were read through the transcript panel on the video page in the
built-in browser. These are YouTube's automatic captions; nobody listened to any recording, and
where the captions are garbled the claim's notes say so. No paid service was used.

**Whose words count.** A claim counts only while the speaker held a qualifying role:

- Altman: from OpenAI's founding (2015-12-11), first as co-chair, then as chief executive.
- Musk: co-chair of OpenAI, 2015-12-11 to 2018-02-21; chief executive of Tesla in 2019, 2020 and
  2021 (John's ruling of 2026-10-19); head of xAI from its incorporation on 2023-03-09. xAI was
  announced only on 2023-07-12, so two claims from the four months between rest on a company that
  was not yet public. That is flagged for John.

**Words reported second-hand.** Where the person's own words could not be opened, but a named
news outlet reported them from a dated public occasion, the claim is entered as `coverage_only`,
with no quote, as the method allows. That is three of Altman's and seven of Musk's. Where even
that was missing (a paraphrase with no source, a private meeting, a staff message), the words
were left out and the row in the search log says why.

## What changes on the claims page

- **Altman: no change.** His latest dated forecast is still TIME's report of 2026-08-26 ("an
  internal system he would call AGI" by the end of 2026). Nothing he said later carries a date
  for AGI or beyond.
- **Musk: his line changes.**
  - Before: "Latest dated forecast (2026-01-22): AI smarter than any human, 2026 to 2027".
  - After: "Latest dated forecast (2026-08-31): superhuman at anything digital, by 2027".
  - The new date is his post on X of 2026-08-31: "AI will be able to do anything digital ... at
    a superhuman level by the end of next year". Its nearest year moves from 2026 to 2027.
- **Unchanged:** the home-page sentence, the counts beside it (eight leaders ahead of the
  academics, twelve with a date), the headline and every scored series. The two claims figures
  are redrawn with the new forecasts when the site is next built; the build runs on every push
  to main, so this pull request does not carry built pages.

## Held for John

These are dated claims that were found and read, but whose verdict, or whose entry at all,
needs a ruling. None is entered.

Altman:

1. "If we are right, by the end of 2028, more of the world's intellectual capacity could
   reside inside of data centers than outside of them". He said this at the India AI Impact
   Summit on 2026-02-19. The ledger already holds the same claim from his BlackRock talk of
   2026-03-11. The method keys a repeat to its first date, but files are never renamed, so the
   question is which record carries it.
2. "people in 2025 will mostly spend their time in the same way they did in 2024" (Three
   Observations, 2025-02-09). The date has passed, but judging "mostly the same way" is a ruling.
3. "Anyone in 2035 should be able to marshall the intellectual capacity equivalent to everyone in
   2025" (same post). It reads as what ought to be, not as a forecast.
4. Smaller calls flagged inside the files:
   - where "summer" ends (2025-09-22 was taken);
   - whether DALL·E's beta from a waitlist counts as its "product launch";
   - whether "we are not gonna deploy AGI next month" is untestable, as entered.

Musk (the full list, with times, is search-log row `musk-claims-142`):

1. "safer than a person" or "better than human" by a date, said three times. Settling these
   needs a ruling on whether Tesla's own crash figures count as evidence.
2. Optimus "doing useful tasks" in Tesla's factory by the end of 2024, and "limited production"
   from early 2025. Tesla's own statements conflict.
3. Ride-hailing in California and Texas, and "driverless" paid rides, in 2025. Does the June 2025
   Austin service count? It ran with a safety monitor in the passenger seat.
4. The first car driving itself to a customer, and cars delivering themselves by default, in 2025.
   No Tesla source was opened.
5. Texting while driving allowed "in the next month or two" (2025-11-06).
6. Grok 5 "in Q1" 2026, and Grok leading at coding by mid-2026. No xAI release or agreed
   scoreboard was opened.
7. Supervised self-driving approved in Europe "next month" (2026-01-22). Approvals came country
   by country. Also Optimus V3 shown by mid-2026; no record of the showing was opened.
8. Advanced Summon "probably next month" (2019-01-30). The release date was not found.

Also flagged inside Musk's files:

- Verdicts that rest only on his own later words, such as his remark at Davos that AI "might" be
  smarter than any human by the end of 2026, used to settle his earlier forecasts for 2025.
- A three-day slip: the self-driving test version for drivers with perfect safety scores, set for
  2021-10-08, rolled out on 2021-10-11.
- Reading "a quarter of the United States" as a quarter of its people.

## Not verified

- No recording was listened to. Every quote from a recording is the automatic captions' wording,
  and the speaker on earnings calls is judged from context.
- Musk's posts on X that the press never reported, and interviews the fixed searches did not
  surface, are not covered. This is the main limit on calling either record complete.
- The Reddit thread of Altman's 2024-10-31 answer was not opened. Only TechCrunch's report of it
  was read.
- Rev's transcript of the DealBook interview of 2023-11-29 was not checked against the
  recording.

## Next

Dario Amodei is next in the order of work, then Jensen Huang.
