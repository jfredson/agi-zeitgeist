# Independent check of the widened claims ledger (pull request 23), 2026-10-19

**Verdict: do not merge yet.** The rules, the code and the ledger-only list are sound. The
claim files are not ready. In a random sample of 40 new files, 12 fail; of the 45 claims marked
"came true", about ten verdicts are in doubt, one of them among the thirty already live. The
fixes are named below. Most come from a handful of reading rules that the files apply in
different ways, so the right repair is to settle those readings, re-pass every file against
them, and check a fresh sample, not only to patch the files named here.

Checked by a session that did not build the work, on the pull request's branch
(`claude/epic-haibt-dc6bf6`, last commit `2b66e6a`, the merge of main). Nothing was merged,
pushed to that branch or published. The per-claim notes behind every line below are in
[`claims-ledger-check-2026-10-19-per-claim.md`](claims-ledger-check-2026-10-19-per-claim.md),
beside this file.

Kai-Fu Lee's claims, which John added on 2026-10-19 after this check began, are covered in
the section on him at the end, once the builder's commits reached the branch.

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

## Kai-Fu Lee

*(Written when the builder's commits adding him reach the branch.)*
