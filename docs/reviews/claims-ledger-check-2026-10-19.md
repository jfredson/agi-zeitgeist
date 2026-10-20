# Independent check of the widened claims ledger (pull request 23), 2026-10-19

**Final verdict (second pass, commit `cf8fec5`): merge after the named fixes below.**

- **The first pass failed the claim files and is kept below as found.** In it, 12 of 40 sampled
  files failed and about ten "came true" verdicts were in doubt.
- **What changed since.** John ruled the open readings, and the builder passed every file again.
- **The re-pass worked.**
  - In a fresh random sample, 3 of 40 files fail (first pass: 12 of 40).
  - Of the 35 claims now marked "came true", 2 fail.
  - Of the 33 first-pass failures, 27 are fixed, 4 were taken out properly, and 2 still need
    work.
  - The rules, the code, the search log, the ledger-only list and the page all pass.
- **What is left is specific:**
  - two verdicts that are wrong by their own tests;
  - a handful of tests that drift from the speaker's words, which must be fixed before
    publishing, because a test cannot change afterwards;
  - one quote whose speaker is uncertain;
  - one missed claim;
  - and Kai-Fu Lee's files, which were new this round and fail at 8 of 33.
- **None needs another full re-pass.** The managing session can merge once the "must fix" list
  in section A is done, without a third check, if the builder's commit for it is read by the
  managing session.

Checked by a session that did not build the work. Nothing was merged, pushed to the pull
request's branch or published. The per-claim notes for both passes are beside this file:
[`claims-ledger-check-2026-10-19-per-claim.md`](claims-ledger-check-2026-10-19-per-claim.md)
for the first pass and
[`claims-ledger-check-2026-10-19-per-claim-second.md`](claims-ledger-check-2026-10-19-per-claim-second.md)
for the second.

# Second pass (commit `cf8fec5`)

The branch was read at `cf8fec5`: 325 claims by 15 people, 109 due, 35 came true, 56 did not.

## What was checked: 138 files, plus the 4 taken out

- **The 33 files that failed the first pass.** 29 still exist and were read again; for the 4
  taken out, the search-log row that records each was found, and each says "taken out before
  merging" with its reason.
- **Every claim marked "came true": 35.**
- **Every forecast that something will not happen: 20.** These are scored under John's
  second reading, and the bare "human level" in them falls under his fourth.
- **All 33 of Kai-Fu Lee's files.**
- **A fresh random sample of 40 new files.** It was drawn with Python's
  `random.seed(2026101902)` from the 172 new files in none of the groups above and not read in
  the first pass.

The groups overlap, so 138 files were read at their sources.

| group | files | pass | fail | could not verify |
|---|---|---|---|---|
| first-pass failures, still present | 29 | 27 | 2 | 0 |
| first-pass failures, taken out | 4 | 4 (removal logged) | 0 | 0 |
| "came true" | 35 | 33 | 2 | 0 |
| forecasts that something will not happen | 20 | 16 | 4 | 0 |
| Kai-Fu Lee | 33 | 24 | 8 | 1 |
| fresh random sample | 40 | 37 | 3 | 0 |
| **all files read** (overlaps counted once) | **138** | **121** | **16** | **1** |

One count is my own call, not the helper's. The helper marked Suleyman's 2025
self-improvement experiment a pass with a flag. I count it as a failure, because its verdict
contradicts its own test (item A2).

## A. Must fix before merging

**Verdicts that are wrong by their own tests or records (change a count):**

1. `2025-04-24-pichai-waymo-atlanta-later-this-summer` (the builder's own call f). It is
   entered as a separate record, a hit, for narrowing Atlanta to "later this summer". But on the
   same earnings call Pichai also says "first paid rides in Atlanta, via Uber, later this year"
   (official transcript, page 19). So the date was not clearly narrowed, and one Atlanta launch
   now scores two hits. Take it out as borderline, and add 2025-04-24 as a repeat date on the
   February Austin-and-Atlanta record. **Pichai: 10 came true becomes 9.**
2. `2024-10-suleyman-teams-experiment-with-self-improvement-in-2025` (the builder's call d).
   - It is scored "did not come true" because the Darwin Gödel Machine paper mentions "human
     oversight".
   - But the file's own test reads his words "doesn't have a human directly overseeing it" as
     no person approving each change. Its own reason grants that the paper meets that; the
     paper's safety line is about oversight of the whole experiment.
   - By its test it came true on 2025-05-29, and the test cannot be changed now. **Suleyman: 3
     came true becomes 4, and 6 did not becomes 5.**
   - Then check `2024-04-suleyman-self-improving-ai-five-to-ten-years` ("not before 2029") does
     not later read the same paper the other way.
3. `2024-05-14-hassabis-astra-capabilities-gemini-app-later-this-year`. It is scored "did not
   come true", but its test asks for the capabilities "available to the public in a Google
   product such as the Gemini app". From 2024-12-11 Google AI Studio's "Stream Realtime" let
   anyone talk to Gemini over a live camera or shared screen. That rests on outside coverage and
   Google's developer forum; Google's own Gemini 2.0 post confirms the live video interface
   underneath it. Rescore it as came true, or put the "is a developer tool a Google product"
   question to John. Either way, the reason must deal with it.
4. `2011-01-hassabis-transfer-learning-concepts-five-years`. It is marked "cannot be tested",
   but the same 2011 talk defines conceptual knowledge (22:32) and transfer learning (35:10). By
   the rule that the speaker's own definition in the same source is the test, write the test
   from them and score it (due 2016).
5. `2024-amodei-new-model-most-intelligent-by-airing`. The re-pass made it "did not", saying the
   lead "rests only on Anthropic's word". That is wrong, and so was my first pass, which cited
   only the Chatbot Arena leaderboard (second place). An outside benchmark of the same week,
   LiveBench (arXiv 2406.19314, version 1, 2024-06-27), put Claude 3.5 Sonnet first overall.
   The outside record is split. Rewrite the reason to name both, log the LiveBench search, and
   put the status to John. "Did not" is defensible under "leads on the main published
   comparisons", but it should be his call with both facts in front of him.

**Tests that do not hold the speaker's words** (a test is fixed at entry, so these cannot wait):

6. `2026-01-lecun-smarter-than-humans-not-within-two-years`: the test adds "at thinking work
   across the board" to his "smarter than humans". The same addition was taken out of his London
   file in the re-pass, so the two now disagree.
7. `2025-07-30-amodei-same-cost-much-more-capable-two-years`: the test asks only for "scoring
   clearly higher on public tests". He said "much more capable of doing work much more
   autonomously much more broadly".
8. `2024-10-kaifulee-agi-better-at-almost-everything-five-to-ten-years`: the test narrows his
   "almost everything we do" to "thinking work". Its timestamp also stops about 20 seconds
   before the quote.
9. `2024-10-kaifulee-robot-cannot-clean-a-room-within-three-years`. The test changes his words
   twice:
   - it widens "this robot" (the home humanoid robots from Tesla and Figure the host had just
     named) to any household robot;
   - it raises "cannot even begin to do" to full cleaning across homes.

   As written, Physical Intelligence's π0.5 robot, shown on 2025-04-22 cleaning in homes it had
   never seen, may already defeat it. Write the test in his words.
10. `2025-10-30-kaifulee-company-run-by-ai-agents-five-to-ten-years`: "we won't get there for
    another perhaps 5 or 10 years" is the shape of John's second reading (his own example is "it
    will take at least a decade"). Score it as a forecast that something will not happen, as
    Lee's GPT-5 file does with the same construction.

**Kai-Fu Lee: a speaker, a missing claim, and the record:**

11. `2026-09-23-kaifulee-embodied-agi-five-to-ten-more-years`: could not be verified. In the
    Endgame podcast's captions a speaker-change mark falls at the start of this line (1:40:51),
    so it may be the host, Gita Wirjawan, speaking. Listen to 1:40:48 to 1:41:05. If it is the
    host, take the file out and correct its search-log row (Lee's sixth claims search,
    `kaifulee-claims-006`). If it cannot be settled, take it out as borderline.
12. **A missing claim.** In the dialogue of 2026-02-04 (the Fudan University repost, Lee's 60th
    claims search, `kaifulee-claims-060`), section 04, Lee says that within two to three years
    an AI will appear that does 90% of human tasks better than 90% of people, and that this
    will certainly happen.
    - It is dated, about AI, and testable by his own comparison.
    - It is the middle step between his October 2025 "about five years" and September 2026
      "maybe two years", and neither the ledger nor the search log has it.
    - Enter it (due 2029, early end 2028, restating the 2025-10-02 claim), and point the
      September 2026 file's `restates` at it.
    - Log two lines of the same dialogue as left out: the conditional "if ... we can multiply
      the value humans create a hundredfold within five years", and the undated peak of AI
      hardware.
13. `2024-11-10-kaifulee-gpt5-not-within-six-months` and
    `2024-11-10-kaifulee-consumer-ai-apps-explode-first-half-2025`: a printed Chinese text of the
    full conversation exists. Recode China AI links it, and Tencent Tech's WeChat account posted
    it on 2024-11-05. So these are not coverage only, and the words were said by 2024-11-05, not
    on 2024-11-10 (the podcast page). The file names cannot change and the validator ties `when`
    to them. So say it in `when_note` and the source fields, and upgrade the source kind to the
    printed interview. The GPT-5 verdict stands.
14. `2024-11-26-kaifulee-ai-apps-proliferate-within-two-years` and
    `2024-11-26-kaifulee-flood-of-ai-apps-in-2025`. The notes say the WIRED column is signed as
    01.AI's chief executive. Its byline calls him chief executive of Sinovation Ventures, and it
    never names 01.AI. He held the 01.AI role that day, so the claims still count; correct the
    stated fact.
15. `2024-03-kaifulee-hallucination-solved-in-eighteen-months`. The verdict stands, but its
    reason misreports Vectara's table: it says frontier models make things up 3 to 6.5% of the
    time, but those figures are small models. The frontier models run about 6.5 to 14%. Correct
    the figures, and prefer OpenAI's post of 2025-09-05 ("Hallucinations remain a fundamental
    challenge"), which is dated before the due date.
16. `2024-02-20-suleyman-hallucinations-largely-eliminated-next-year`. The verdict stands (the
    European Broadcasting Union study), but the reason gives the GPT-5 system card's error rate
    as "11.6% to 22%" and leaves out its 4.8% for gpt-5-thinking, the figure most favourable to
    him. State the full range and why the miss still stands.

**Fixes that change no verdict but were asked for and not fully made:**

17. **The Grok 2 and Microsoft 365 Copilot dates.**
    - Musk's Grok 2 post (`2024-07-01-musk-grok-2-in-august`) was made on 2024-06-30 in his own
      time.
    - Nadella's shareholder letter (`2023-10-nadella-m365-copilot-generally-available-this-year`)
      is signed 2023-10-16.
    - Both files explain this in `when_note`, but `when` cannot change while the validator ties
      it to the file name and the method forbids renaming.
    - Accept the notes for now; whether the validator should allow it is a question for John.

## B. The search log, the page and the counts

- **The search log.**
  - Every search id named by every claim exists, with no duplicates and none borrowed from
    another speaker.
  - Kai-Fu Lee has 77 new rows.
  - No row says "withdrawn" any more.
  - The four files taken out after the first pass are each logged with their reason.
  - **One wording fault (not blocking).** In 22 rows a new reason is appended after an old
    label, "under the strict reading of the admission rule's second condition (the managing
    session's ruling: only claims about AI):". The reason after it is right: undated, "as little
    as", a hypothetical, or a borrowed span. But the label in front of it is wrong.
  - The rows include Amodei's 14th, 17th, 28th and 49th claims searches, and several of
    Suleyman's and Zuckerberg's. Drop the label where the reason is not a business forecast.
- **The ledger-only list still does not leak.**
  - The home page says "the 37 people on the expert panel".
  - The experts' dates come from 27 experts.
  - The frontier-voices chart reads no row by Zuckerberg, Pichai or Nadella.
  - `data/statements.csv` is unchanged by the pull request.
  - Kai-Fu Lee is on the panel already (tier core), so his statements belonging there is
    right.
- **The page.**
  - The summary reads "325 dated predictions by 15 people. 109 are due ...: 35 came true, 56 did
    not and 18 cannot be tested".
  - The counts table's "cannot be tested" column now gives the due ones in brackets, so every
    row adds up (Altman: due 6 = 2 + 1 + 3).
  - The coined label "ledger-only list" is gone from the page.
  - At 375 pixels wide nothing scrolls the page sideways. At 1,280 the table still scrolls
    inside itself, as before.
- **The checks.** `validate.py` passes (325 claims, 4,906 search-log rows), and so do
  `check_news.py` (3 posts) and `test_check_news.py` (8 tests).
- **The method and amendment A30** now carry, with the date and John's words:
  - the four readings;
  - the managing session's rulings;
  - the rule that a test uses the speaker's words;
  - the change to when a claim is due, as A30 item 8, with the first thirty's 17 due;
  - Musk's Tesla years;
  - Kai-Fu Lee.

  The stale Kurzweil line is gone.
- **Every first-pass item in "Wrong words, dates or records" is fixed** except item 17 above.
  That includes Pichai's YouTube-chapters quote, now in his words.

## C. The news post

The live post still says "twenty are due" in its summary, its `after:` line and its table,
with Altman at 9. After the merge the page will say 17 for the first thirty, and 6 for Altman.
Amendment A30 item 8 records why.

Main's correction already moved "five came true" to four, and the page agrees: Altman 2, Musk
2. The dated note the managing session adds at the merge must also give 17 due and say that
the counting of "due" changed. Otherwise the post's table disagrees with the page it links to.

The home-page sentence ("325 predictions ... 109 are now due, and 35 came true") will move with
items A1 to A5, and only from the merged files.

## D. The builder's seven calls, which John has not ruled

| call | reasonable reading meanwhile? | note |
|---|---|---|
| a. "the next few months", "the coming months" undated | Yes: it follows the reason behind John's "a few years". | It took out a Zuckerberg claim that had come true (multimodal Llama "over the next few months"), and "a few months" plainly ends within about a year. Put it to John soon; it is flagged in the method. |
| b. "early" in a month means by the 10th | Yes. | It decides Hassabis's Gemini 2.5 Flash ("early June", generally available 2025-06-17), which misses under every reading but "the whole month". |
| c. "It's conceivable that within the next ten years" is a hedge, scored | Yes: "within" sets an upper limit. | |
| d. Suleyman's 2025 experiment "did not" | **No.** | The verdict contradicts its own test: item A2. |
| e. Pichai's personalised smart replies "not come" | Yes. | Not re-read at the source in this pass. No record shows them by 2025-09-22, and the later Suggested Replies (2026-01-08) came after the date anyway. |
| f. Pichai's Atlanta "later this summer" as its own record | **No.** | It double-counts one launch: item A1. |
| g. Forecasts that AI will displace or change jobs are admitted | Yes. | The method says "displace or change" but not "create"; one Lee file forecasts jobs created. Add the word. |

## E. Open for John after the merge (no change needed first)

1. **Seasons.** "This summer" is taken to end at the September equinox, applied the same way
   to hits and misses. Two hits rest on it: Pichai's Ask Photos (2024-09-05) and Docs Live
   (2026-09-03).
2. **"A few thousand days".** Altman's superintelligence line is still a dated claim (cannot be
   tested), though it names no length any more than "a few years" does. Under reading 3 it
   would be an undated statement. No due count changes, and the live post uses it as its
   example of a claim that cannot be tested.
3. **Floors.** "At least" floors are taken at the later end in one Suleyman file (no scaling
   slowdown for "at least two to three years", due 2027) and at the earlier end in another
   (self-improvement "a good five to 10 years", due 2029). One rule is needed. Forecasts that
   something will not happen "within N years" are judged at the end of the year, slightly later
   than the stated date; the tests carry the exact date, so nothing is wrong today.
4. **Roles.**
   - LeCun's chair of AMI Labs, a company that has released no model, decides every LeCun
     claim from 2026.
   - Legg counts as "Chief AGI Scientist", a co-founder in Google DeepMind's leadership.
   - Zuckerberg counts from 2013.
   - Lee: by his own account in February 2026, 01.AI now works only for businesses and leaves
     large base models to the big firms. His claims since then stay in (the ruling has no end
     date), but the role notes should say so.
5. **"PhD level"** is read as an undefined stage, like bare "human level"; it changes no count.
6. **Restatements and repeats.**
   - Whether a repeat that adds a definition becomes its own scored record: Legg's 2028
     cannot be tested in its first source but is defined in 2023 and 2025.
   - Whether Huang's Jaguar Land Rover and Hyperion 8 misses count the same 2025 event twice.
7. **The validator and dates**, as in item A17.
8. **Links inside the claim records' own text**, as for the first thirty.

The other smaller points (caption mishearings, a verdict date set at the due date, a `verify`
field left on the research-intern file, a podcast's channel name) are in the second-pass
per-claim notes.

# First pass (commit `2b66e6a`), kept as found

Verdict then: **do not merge yet.** The rules, the code and the ledger-only list were sound; the claim files were not. The rest of this part is as written then, and its "Kai-Fu Lee" placeholder is answered in the second pass.

## 1. Claims checked against their sources

**What was checked: 90 files.**

- **A random sample of 40** of the 278 new files, drawn with Python's `random.seed(20261019)`
  from the 233 that are neither "came true" nor coverage-only (the other two groups were
  checked in full).
- **Every claim marked "came true": 45**, the 40 new ones and the 5 among the original thirty.
- **Every coverage-only claim: 6**, one of which is also a "came true" (LeCun's "not next
  year"), so 5 more.

For each one the source was opened (captions through `yt-dlp`, pages directly or through an
archive copy), and the quote, the date, the role on that date, the admission rule, the due
date, the verdict and its record, and the maker-or-outside mark were checked.

**Result: 57 pass, 33 fail, none left unverified.** Every quote but one is in the speaker's
own words where the file says. The one exception is listed under "Wrong words, dates or
records" below.

| group | checked | pass | fail |
|---|---|---|---|
| random sample | 40 | 28 | 12 |
| "came true", new | 40 | 24 | 16 |
| "came true", among the original thirty | 5 | 1 | 4 |
| coverage-only, not already above | 5 | 4 | 1 |

Not every failure changes a number. They fall into four kinds.

### "Came true" verdicts that do not hold as written (change a count, or need John)

1. `2025-10-29-altman-automated-research-intern-by-september-2026` (one of the live thirty).
   The test includes "running on hundreds of thousands of GPUs". OpenAI's post of
   2026-09-06 says nothing about that, and the file admits the condition is unchecked. Under
   the ruling that a hit needs every condition, it is not a hit. The test was also taken from
   OpenAI's own announcement of success, not from Altman's words. **This changes the live
   news post's "five came true".**
2. `2024-04-12-amodei-asl3-this-year-or-next`. Anthropic switched on its Level 3 protections in
   May 2025 "as a precaution", saying it had not determined the model crossed the line. In the
   same interview Amodei defines the level as a real rise in bioweapons risk. By his own
   definition the record shows no crossing: a miss, or a call for John.
3. `2024-amodei-new-model-most-intelligent-by-airing`. "Most intelligent in the world" rests
   only on Anthropic's word. The main outside leaderboard of the time (LMSYS Chatbot Arena) put
   Claude 3.5 Sonnet second, behind GPT-4o. A miss, or a call for John.
4. `2023-12-06-hassabis-gemini-ultra-developers-enterprise-early-next-year`. The record cited
   (Google Cloud, 2024-02-15) offers Ultra only "via allowlist", the same by-invitation access
   the promise said would come before the wider roll-out. No record of open developer access
   by 2024-03-31 was found.
5. `2018-05-10-huang-self-driving-cars-2020-to-2021`. In the sentence just before, Huang sets
   Level 2 against "a Level 5 self-driving car". The test ignores that same-source usage and
   asks only for Honda's Level 3 traffic-jam car (about 100 leased in Japan). On his own usage
   it is likely a miss.
6. `2023-09-27-zuckerberg-glasses-multimodal-ai-early-next-year`,
   `2024-10-30-zuckerberg-smaller-llama-4-early-next-year`, and
   `2024-12-05-suleyman-copilot-vision-general-availability-early-2025`. All three read "early
   next year" as the first half and are hits only on that reading (releases on 2024-04-23,
   2025-04-05 and 2025-06-12). The Hassabis and Huang files read the same words as the first
   quarter, where that produced a miss (Huang's Mercedes date) or a hit anyway. A generous
   reading that appears only where it makes a hit looks like choosing the reading by outcome.
   See the open readings below.
7. `2024-07-23-zuckerberg-meta-ai-most-used-by-end-of-year`. Meta's own counts show its size.
   "More people than any other assistant" rests only on Meta's statement about its rivals,
   which is not a figure only Meta holds.
8. `2025-01-24-zuckerberg-meta-ai-leading-assistant-billion-people`. The billion is shown;
   "leading" is not. On the same call of 2025-07-30 Zuckerberg named becoming "the leading
   personal AI" as a goal still ahead, and OpenAI reported about 800 million weekly ChatGPT
   users that October. A miss.
9. `2023-10-17-legg-agi-not-next-year-or-year-after` and
   `2024-04-09-lecun-not-surpass-human-intelligence-next-year`. Both are hits for a forecast
   that something will *not* happen. Whether such words are admitted at all is open point 4,
   and a "did not happen" can only be shown by a later statement, not by "a dated record of
   the event itself". They should not go out as hits before John rules on point 4.
10. `2024-06-02-huang-mercedes-self-driving-production-2025` (the hit may stand). The record
    cited (electrive, 2025-06-04) never mentions Nvidia; only Nvidia's own blog of 2026-01-05
    says the car runs its software. The mark should be "maker", not "outside", and the blog
    should be the record. electrive also says Nvidia's system reaches the US in 2026 and only
    "potentially" Europe.

### "Did not" or "cannot be tested" verdicts that do not hold as written

11. `2023-01-25-lecun-teenagers-train-image-models-within-two-years` (changed from "came
    true" to "did not" before the pull request). The test adds conditions not in his words:
    home equipment, built from scratch, adapting a model not counting. The dated sentence says
    only "any teenager in the parents basement is going to be able to do this". Hugging Face's
    guide of 2023-01-26 fine-tunes Stable Diffusion on one consumer graphics card. Read
    plainly, it arguably came true. Leave it out as borderline or put the test to John.
12. `2024-02-20-suleyman-hallucinations-largely-eliminated-next-year` (coverage-only).
    "As accurate as any content that you can find on the web" is a named comparison, so under
    John's ruling it gives a plain-reading test, not "cannot be tested". Scored, it is very
    likely a miss.
13. `2011-12-31-legg-proto-agi-within-eight-years`. Marked "cannot be tested" on his remark
    that it "might be impossible to falsify", but his reason there is military secrecy. The
    post defines proto-AGI as a list of abilities an outsider could check, so it can be
    scored, probably as a miss.
14. `2023-07-14-suleyman-modern-turing-test-as-little-as-two-years`. "Could be as little as two
    years away" is an earliest date, not a deadline, and his test is well defined. "Cannot be
    tested" is the wrong status: leave it out as borderline, or score it.
15. `2022-05-11-pichai-youtube-auto-chapters-80-million-goal`. The miss rests only on finding
    no record. The record cited ("tens of millions" of videos) does not rule out 80 million, so
    "has not come" claims more than the record shows. (Its quote is also wrong; see below.)
16. `2025-05-20-pichai-gemini-25-to-search-this-week`. The file's own source shows Gemini 2.5
    in Search by July 2025, so the direction is "came later", not "has not come". The record
    only repeats Google's announcement, so the mark is "maker".

### Admitted when the rules say leave out, or with a test that misreads the words

17. `2024-11-11-amodei-lex-2026-or-2027-straight-line`. The date is conditional on a straight
    line he says he does not fully believe ("if you believe the straight line
    extrapolation"). It is closer to a hypothetical: leave it out.
18. `2025-05-23-hassabis-agent-fleets-four-or-five-years`. "I could imagine that in the next
    four or five years", posed as a question for economists. A possibility, not a forecast:
    leave it out.
19. `2026-01-14-mensch-not-superhuman-in-every-domain-within-two-years`. A forecast that
    something will not happen, with its two-year span borrowed from the sentence before. Leave
    it out, or hold it for point 4.
20. `2025-05-22-amodei-one-person-billion-dollar-company-2026`. The test never requires AI to
    do the work; a one-employee holding company worth a billion would pass. Add that condition
    (from the question he was answering) or leave it out as borderline.
21. `2026-09-12-amodei-pace-swarm-could-take-over-internet-six-to-twelve-months`. The test
    weakens "taking over the entire internet with a persistent botnet" to "at large scale".
    It must use his words. A test is fixed at entry, so fix it before publishing.
22. `2024-04-suleyman-self-improving-ai-five-to-ten-years`. His words ("still a good five to
    10 years before") are a floor, "not before about 2029", but the test is "by the end of
    2034". Work arriving early, such as the Darwin Gödel Machine paper the ledger uses
    elsewhere, could then score as a hit, the opposite of what he said.
23. `2021-08-19-musk-tesla-bot-prototype-next-year` (one of the live thirty; John has now
    ruled that the Tesla years count). The test is only that a physical robot prototype is
    shown, with no AI condition: a plain hardware date under the managing session's ruling. Give
    the test an AI condition or put it to John. It is one of the live five "came true".

### Wrong words, dates or records (no count changes unless noted)

24. `2022-05-11-pichai-youtube-auto-chapters-80-million-goal`. **The quote drops words without
    marking it**: "the number of videos with from eight million". The captions read "the number
    of videos with auto generated chapters from eight million". Restore the words (start at "a
    goal to 10x" to stay under 25 words).
25. `2021-03-16-altman-five-years-legal-documents-medical-advice` (live thirty; the hit
    stands). The medical half was settled by OpenAI's ChatGPT Health page of 2026-01-07, not by
    the 2023 GPT-4 report cited. The verdict date, record and direction ("on time", not
    "sooner") need changing, and the quote is in the opening section, not "near the end".
26. `2024-07-01-musk-grok-2-in-august` (live thirty). The post went out on the evening of
    2024-06-30 in the speaker's own time, so `when` is 2024-06-30. The file name stays.
27. `2023-10-nadella-m365-copilot-generally-available-this-year`. The shareholder letter is
    signed "October 16, 2023", so `when` is 2023-10-16, not just the month.
28. `2023-07-25-nadella-security-copilot-early-access-this-fall`. The record should be
    Microsoft's own post of 2023-10-19 (not a news article relaying it), with that verdict
    date and the mark "maker". "Paid", which Nadella said, should go back into the test.
29. `2023-10-24-pichai-gemini-models-throughout-2024`. The test needs more than one model
    released in 2024, but the one record cited shows one. Cite the 2024-02-08 Ultra launch or
    the May 2024 Flash preview; it also calls Gemini 1.5 Pro a February public release, while
    Google called it a limited preview.
30. `2024-06-25-suleyman-real-time-interruptible-voice-by-end-of-year` (the hit stands). The
    record cited never says the user can interrupt the AI. Google's Gemini Live post of
    2024-08-13 ("You can even interrupt mid-response") does.
31. `2024-10-suleyman-permanent-ai-memory-done-in-2025` (the hit probably stands). In context
    "we" is Microsoft's Copilot, not the field. Test it on Copilot's 2025 memory feature, marked
    as the maker's word.
32. `2024-12-05-suleyman-copilot-vision-all-apps-always-on-2025` (the miss stands). The reason
    describes mid-2025; Microsoft's post of 2025-10-16 says Vision went worldwide with full
    desktop sharing. What failed is the always-on part; rewrite the reason.

Smaller notes that change nothing (the darioamodei.com posts carry only a month; Pichai took
office as Google's head on 2015-10-02, not the announcement date of 2015-08-10; caption
mishearings in two Huang quotes; LeCun's AMI Labs title given as "executive" chairman where
AFP says "non-executive") are in the per-claim file.

### What the sample says about the files not checked

Of the 40 sampled files, 12 fail, and 7 of those 12 would change a status or take a file out.
That rate, applied to the roughly 190 new files nobody has re-checked, means dozens more
problems of the same kinds. That is why the verdict is a re-pass, not only the fixes above.

## 2. The search log

- **Every search id named by every claim exists** in `data/search_log.csv`; there are no
  duplicate ids, and each claim names only rows for its own speaker.
- **577 new rows**, all dated 2026-10-19, none with an empty finding. Nothing earlier in the
  log was changed or removed.
- **Every logged drop has a reason.** About 200 rows record something left out. Each was read
  for a reason: business forecast, hardware date, borderline, hypothetical, not the speaker's
  words, role at the time, no length named, no test, a hope.
- **The lead's 31 later drops** (Amodei 18, Zuckerberg 11, Hassabis 1, LeCun 1) each appear in
  the row that first recorded them, with "later left out" and the reason, and none of their
  files remains.
- One wording note: those rows say a file "was withdrawn before merging". "Withdrawn" is one
  of the ledger's five status words (a speaker's retraction). "Taken out before merging" would
  not collide with it.

## 3. The ledger-only list does not leak

The site was built on the branch (`.venv/bin/python scripts/site.py`: "claims page: 308 claims
by 14 people").

- **The home page's panel count is 37**: "This rests on the 37 people on the expert panel".
- **The experts' dates still come from 27 experts.**
- **The frontier-voices chart** reads 144 rows from 27 speakers, none of them Zuckerberg,
  Pichai or Nadella (checked by calling `frontier_rows()`). The tier filter is now the shared
  `PANEL_TIERS`.
- **`data/statements.csv` is unchanged** by the pull request (807 rows, no row by any of the
  three). The validator now refuses one if added.
- **The three names appear in built files** only on the claims page, the claims and search-log
  tables, `speakers.csv` and the docs, plus files that already held them on main and that this
  pull request did not touch. Those are the wide list of candidates, the Reddit pilot's codes,
  and one Google self-report in `world_measures.csv`.
- **The claims page** says plainly that the three are not on the list of experts. Their
  column of coded statements reads "none recorded: not on the list of experts".

**Pass.**

## 4. The change to how "due" is counted

**Is the new counting right? Yes.** A "cannot be tested" claim used to count as due from the
day it was entered; now it counts only once its own date has passed. That matches the method's
status table, which defines a claim's date as 31 December of its due year or its `due_date`.

- The page's summary now reads: "106 are due, their dates passed: 45 came true, 46 did not
  and 15 cannot be tested. Of those still ahead, 60 cannot be tested either".
- The per-person counts match the pull request's table.
- No claim is past its date and still "not yet due", and no claim got a verdict before its date.

**Is it written down?**

- **Not in the method.** The method nowhere says when a "cannot be tested" claim counts as
  due.
- **Not in amendment A30.** A30 does not mention the change at all. Its "Applies to" list
  covers `site.py` only for the tier filters.
- **Fix:** add one sentence to the method (under "The rate") and a numbered point to A30 (or
  its own amendment). It changes a published number.

**Does it change the live numbers? Yes, and the news post would contradict the page.**

| | live news post (2026-10-19) | the page after merging |
|---|---|---|
| Sam Altman, due | 9 | 6 (3 of his 5 "cannot be tested" fall due only at the end of 2026, 2030 and 2034) |
| Elon Musk, due | 11 | 11 |
| the thirty, due | "twenty are due" (summary, table and `after:` line) | 17 |
| the thirty, came true | "five came true" | 5 as the files stand; 4 if the research-intern verdict (item 1) changes, and 3 if the Tesla robot (item 23) does too |

The dated note the managing session adds to the post must say that the counting of "due"
changed, giving 17 due for the original thirty, and must carry any change to "five came true".
Otherwise the post's table disagrees with the page it links to. The new home-page sentence
("Of the 308 predictions with a date recorded so far from 14 of the people who run the AI
companies, 106 are now due, and 45 came true") matches the page. Its 45 will move with the
fixes in section 1.

## 5. The ten points left for John

John ruled points 1 and 2 on 2026-10-19:

- **Point 1:** Musk's Tesla-years claims count.
- **Point 2:** Kai-Fu Lee is added, for claims made while he led 01.AI.

For the other eight, the question is only whether any must change before the merge.

| point | do the files follow a reasonable reading meanwhile? | must anything change before merging? |
|---|---|---|
| 3. Roles that are a judgement | Yes. LeCun's FAIR years out, AMI Labs in (chair), Legg from DeepMind's incorporation. Two more the list leaves out: Zuckerberg's claims count from 2013 because Facebook opened an AI lab (consistent with John's Tesla ruling); Legg since 2023 is "Chief AGI Scientist", not Google DeepMind's named chief scientist (that is Jeff Dean), so he counts as a co-founder in its leadership. | No, but add those two to the list for John. Two Legg files (`2025-12-11-legg-full-agi-within-a-decade`, `2025-12-11-legg-minimal-agi-one-to-five-years`) and all thirty original Altman and Musk files lack the role note A30 point 5 asks for in every claim's notes. Add them. |
| 4. Forecasts that something will not happen | No: as written, two of the 45 hits (Legg, LeCun) rest on an open question, and "a dated record of the event" cannot show a non-event. | **Yes.** Until John rules, hold the "will not happen" claims as not scored (or out), not as hits. That is 2 hits and the Mensch file, plus LeCun's and Legg's other floors. |
| 5. "A few years" | No. Five files admit it (Suleyman's two pandemic-pathogen claims and his closed-loop self-improvement claim at two to four years; Zuckerberg's business-agent and superintelligence claims at two to five), while Hassabis's "a few short years" and others are left out as undated. None is due yet. | **Yes**, one reading for all. The rule that borderline cases stay out points to leaving the five out. |
| 6. Seasons and month spans | Yes for month spans, which follow the span rule as written. Seasons (to the equinox) are generous and applied the same way in all five "this summer" files; Pichai's Docs Live hit (2026-09-03) depends on it. | No, if John accepts the equinox reading. **But "early" has no rule and is read three ways** (first quarter, first half, whole month), which decides three hits (item 6). That one must be settled before merging. |
| 7. Overshoot | Yes (the only case was left out). | No. |
| 8. Figures only the company holds | Yes, mostly left out. The related problem in the files is a maker's word about its *rivals* (Meta "most used", item 7) treated as a maker-held figure. | Fix item 7; nothing else. |
| 9. Two restatements | Yes; keeping them apart is reasonable. But LeCun's two chains show a different problem: the same words "human level" are a testable comparison in Legg's 2010 file and LeCun's "surpass" chain, and an untestable stage in LeCun's other chain (12 of his 24 files are "cannot be tested", mostly this). | No for point 9. Add "human level" as a reading for John to rule, since it moves "cannot be tested" counts. |
| 10. Link what you name | Partly. The page links each person and company. The prose of the claim records names products, studies and people unlinked, against the rule John set on 2026-10-18 for "the visible prose of records". | Not a blocker (the live thirty have the same gap), but a named follow-up. One link to check: LeCun's AMI Labs links a TechCrunch article. Use the company's own page if it has one. |

## 6. Checks and the page

- `python3 scripts/validate.py`: OK (speakers 53, statements 807, search log 4,744 rows, claims 308).
- `python3 scripts/check_news.py`: OK, 3 posts.
- `python3 scripts/test_check_news.py`: 8 tests, OK.
- **`/claims/` at 1,280 pixels wide.** It reads correctly and nothing scrolls the page
  sideways. The counts table (1,318 pixels wide in a 760-pixel column) scrolls inside itself,
  so the rate and "which way the misses went" columns are off-screen until scrolled. That is
  the site-wide table style, and the same as on main.
- **`/claims/` at 375 pixels wide.** Nothing scrolls the page sideways, and the claims read
  well.
- **The counts table's "due" column no longer adds up** from the columns beside it. "Cannot
  be tested" counts all such claims, so Amodei shows due 8 = 4 + 3 + 1 but "cannot be tested"
  13. Showing that column as "13 (1 due)", as the pull request's own table does, would let a
  reader add it up.
- **Plain language.** The page names "(the ledger-only list)" in parentheses, a coined label.
  "On this page only" already says it.
- **The method contradicts itself on Kurzweil.** It now says panel members who never held a
  qualifying role, Kurzweil among them, are not entered. The next line, carried over from
  main, still says Kurzweil's 2029 date "is entered once ... when his turn comes". Delete that
  line.

## 7. Named fixes, in order

1. **Settle the open readings John has not ruled.** One rule each for: "early" (and "early
   June"); forecasts that something will not happen; "a few years"; earliest dates such as "as
   little as" and "at least"; "I could imagine"; and "human level" as a comparison or a stage.
   Then re-pass all 308 files against them.
2. **Correct items 1 to 32 above**, each a separate dated change to its file, with a dated
   note wherever a test changes.
3. **Write the due-counting change** into the method and into A30, and delete the stale
   Kurzweil line.
4. **Add the role notes** to the thirty original files and the two Legg files.
5. **Check a fresh sample of the files** after the re-pass; one helper per person is enough.
6. **Write the news post's dated note** from the merged counts: due for the thirty is 17, not
   20, and say so; carry any change to "five came true"; and give the new totals.

*Kai-Fu Lee's claims are checked in the second pass above.*
