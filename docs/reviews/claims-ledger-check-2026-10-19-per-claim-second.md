# Claims ledger check, second pass, per-claim results (2026-10-19)

138 claim files from pull request 23 at commit cf8fec5, read at their sources by ten helpers of the checking session: the 33 first-pass failures (4 since taken out), every 'came true' (35), every forecast that something will not happen (20), all 33 of Kai-Fu Lee's files, and a fresh sample of 40 drawn with Python's random.seed(2026101902) from the 172 new files in none of those groups and not read in the first pass. Summary and verdict: claims-ledger-check-2026-10-19.md beside this file. One count differs from the helper's: Suleyman's 2025 self-improvement experiment is counted as a failure in the summary (item A2), though batch 9 below marks it a pass with a flag.

## Batch 1

# Second-pass check, batch b2-1 (14 files), 2026-10-19

Sources read this pass: YouTube captions through yt-dlp for five videos (Ezra Klein Gi_t3v53XRU, In Good Company xm6jNMSFT7g, WSJ Davos snkOMOjiVOk, Economist Davos uvMolVW_2v0, Hard Fork YhGUSIvsn_Y), with upload dates; anthropic.com pages (Paris statement, Claude 4, computer use, ASL-3 activation); the Senate testimony PDF (text read with PDFKit); moores.samaltman.com; the Lex Fridman transcript page; Internet Archive copies of OpenAI's GPT-4o and ChatGPT Health pages; the LMSYS post and Altman's post through api.fxtwitter.com; the LiveBench paper, arXiv 2406.19314 v1 (HTML).

The seven calls the builder made without a ruling from John (a to g) do not come up in any file in this batch.

### 2021-03-16-altman-five-years-legal-documents-medical-advice.toml  (fails, hits)  — PASS
- first-pass problem: fixed. The verdict date is now 2026-01-07 and the record is the ChatGPT Health page. The direction is now `on_time`, the `verify` field is gone, the locator is corrected and the role note is added.
- quote: ok. Verbatim on moores.samaltman.com, in the opening section.
- date: ok. The byline reads "by Sam Altman · March 16, 2021".
- role: ok. He was chief executive of OpenAI.
- admission: ok.
- due: ok. Five years from the day said gives 2026-03-16.
- verdict: ok. The Internet Archive copy of "Introducing ChatGPT Health" is dated January 7, 2026. It has "over 230 million people globally ask health and wellness related questions on ChatGPT every week" and "It is not intended for diagnosis or treatment". The GPT-4 report settles the legal half.
- notes: The Health page reports a count of something already happening: "health is one of the most common ways people use ChatGPT today". So AI was giving medical advice in public use well before 2026-01-07. That date is when a dated record shows it, not when it first happened. The wording "the second [half met] on 2026-01-07" would be more exact as "shown by a record dated 2026-01-07". `on_time` probably understates how early it came. Neither point changes the count.

### 2024-03-18-altman-amazing-new-model-this-year.toml  (hits)  — PASS
- quote: ok. On the transcript at 01:06:30, "We will release an amazing new model this year. I don't know what we'll call it."
- date: ok as entered. Small note: the page's date is in universal time; in US time it was the evening of 2024-03-17. The method says the ledger uses the speaker's own time. YouTube also gives 20240318. The verdict is unaffected.
- role: ok.
- admission: ok.
- due: ok. Judged at 2024-12-31.
- verdict: ok. The Archive copy of "Hello GPT-4o" is dated May 13, 2024. It calls GPT-4o "our new flagship model" and says its text and image capabilities "are starting to roll out today in ChatGPT". `evidence_by = maker` is honest.

### 2025-10-29-altman-automated-research-intern-by-september-2026.toml  (fails)  — PASS
- first-pass problem: fixed. The status is now `unfalsifiable` ("cannot be tested"), on John's ruling. The test no longer borrows the definition OpenAI wrote on the day it declared success.
- quote: ok. Verbatim from api.fxtwitter.com; the post's time is Wed Oct 29 17:19:00 +0000 2025.
- date: ok.
- role: ok.
- admission: ok. It is a goal, and `is_goal` is set.
- due: ok. `due_date` is 2026-09-30.
- verdict: ok. It is an internal system whose only judge is its maker, which matches the method's own example "an internal system I would call AGI". Search-log row altman-claims-021 (the re-read made for this correction) exists and records it.
- notes: The `verify` field ("Whether the system ran on hundreds of thousands of GPUs") is stale now the claim cannot be tested. Remove it, or say it no longer bears on the verdict.

### 2023-07-25-amodei-senate-science-insights-two-to-three-years.toml  (sample)  — PASS
- quote: ok. Verbatim on PDF page 3, in the paragraph the locator names. The header reads "July 25th, 2023".
- date: ok.
- role: ok. He was co-founder and chief executive of Anthropic.
- admission: ok, with one note. The sentence is introduced by "a straightforward extrapolation of the pace of progress suggests that". He goes on to endorse it ("This will cause a revolution..."). It is not an extrapolation he disowns, so the hypothetical exclusion does not apply.
- due: ok. "2-3 years" from 2023-07-25 gives 2026, with `due_early` 2025.
- verdict: ok. "Extraordinary insights in broad swaths" gives no test, so `unfalsifiable` is right. By the method it does not count among the due until 2026-12-31.

### 2024-04-12-amodei-agents-take-actions-3-to-18-months.toml  (hits)  — PASS
- quote: ok. Captions at 8:42–8:49: "all of that is coming in the next I would say I don't know 3 to 18 months with increasing levels of ability". The words before it, "going to websites or taking actions on your computer for you", match.
- date: ok. YouTube upload_date is 20240412.
- role: ok.
- admission: ok.
- due: ok. 3 to 18 months from 2024-04-12 runs to 2025-10, judged at the end of 2025.
- verdict: ok. Anthropic's page is dated Oct 22, 2024. Computer use was released "in public beta... Available today on the API", with Claude "looking at a screen, moving a cursor, clicking buttons, and typing text". Every condition of the test is met. `evidence_by = maker` is honest.

### 2024-04-12-amodei-asl3-this-year-or-next.toml  (fails)  — PASS
- first-pass problem: fixed. The test is now his own definition from the same interview, the status is `missed` ("did not come true"), and the judgement call is flagged for John.
- quote: ok. Captions at 1:02:27–1:02:32: "I think asl3 is is you know could easily happen this year or next year".
- date: ok.
- role: ok.
- admission: ok. "Could easily" is a hedge, scored at face value.
- due: ok. Due 2025, with `due_early` 2024. The repeats dated 2024-11-11 and 2025-03-10 have the same due year.
- verdict: ok. The definition at 59:09–1:00:21 matches the test: "relative to use of a Google search there's a substantial increase in risk as would be evaluated by say the National Security community of misuse of biology creation of bioweapons". The page "Activating ASL-3 protections" has "a precautionary and provisional action" and "we have not yet determined whether Claude Opus 4 has definitively passed the Capabilities Threshold". Search-log rows amodei-claims-074 and -075 (the Opus 4.5 and Sonnet 4.5 safety reports) say the same.
- notes: The test allows "by Anthropic or an outside evaluator", but only Anthropic's records were searched. Outside work in 2025 was not looked at: SecureBio's virology test of April 2025, and OpenAI's own "High" biology rating for ChatGPT Agent in July 2025, which was also a precaution. As far as I know, neither is a finding that the line was crossed, so the verdict holds. Saying so would close the gap. The judgement call is already flagged for John.

### 2024-amodei-new-model-most-intelligent-by-airing.toml  (fails)  — FAIL
- first-pass problem: fixed but new problem. The outside leaderboard is now weighed, but the verdict text states something the outside record contradicts.
- quote: ok. Captions at 0:49–0:55: "by the time this podcast airs a new model will be out from anthropic that will probably be the most intelligent and Powerful model in the world". The ellipsis stands for "and Powerful model".
- date: ok as "2024". YouTube upload_date is 20240626.
- role: ok.
- admission: ok.
- due: ok. `due_date` is 2024-06-26.
- verdict: problem.
  - The LMSYS post is correct as cited: 2024-06-24 19:59 universal time, "#1 spot in Coding Arena, Hard Prompts Arena, and #2 in the Overall leaderboard".
  - But `verdict_why` says the lead "rests only on Anthropic's word". That is not so. LiveBench is an outside benchmark by an academic and industry team, paper arXiv 2406.19314 v1, submitted 2024-06-27. It reads: "claude-3-5-sonnet-20240620 performs the best across all six categories and performs the best overall, 6% better than all other models". The scores are 61.2 against GPT-4o's 55.0.
  - That record is dated one day after the due date, but it measures the model as released. A Manifold page from about 2024-06-21 says the LiveBench leaderboard already showed this; I could not check that, because the Internet Archive was offline.
  - So the outside record is split: second on the Chatbot Arena overall, first on LiveBench overall.
- fix: Rewrite `verdict_why` to name both outside comparisons, and add search-log rows for the LiveBench record. Then send the status to John.
  - Under the test's "leads ... on the main published comparisons" (plural), `missed` can still be argued: it did not lead on the Chatbot Arena.
  - But "a near miss, second overall" is no longer the whole story.
  - Until John rules, it should not be published with the current reason.
- notes:
  - The test drops "powerful" from "most intelligent and powerful". Minor.
  - On a miss, `direction = not_come` fits poorly; a later Anthropic model did lead outside leaderboards. That is a judgement for the same ruling.

### 2025-01-21-amodei-better-than-us-almost-everything-two-three-years.toml  (sample)  — PASS
- quote: ok. The supplied captions at 12:23–12:41 read: "over the next 2 or 3 years I am relatively confident that we are indeed going to see models that show up in the workplace that consumers use that are, yes, assistance to humans but are. Gradually get better than us at at almost everything". The automatic track drops "we".
- date: ok. YouTube upload_date is 20250121.
- role: ok.
- admission: ok. "Better than us" is a stated comparison, so under reading 4 it gives a plain test.
- due: ok. 2 or 3 years gives 2028, with `due_early` 2027.
- verdict: ok, not yet due.
- notes: Just before it (11:41–11:57), he describes his own earlier view, "better than almost all humans at almost everything ... probably mid 2020s". That describes a past view, not a new claim, and rightly is not entered.

### 2025-01-amodei-five-to-ten-percent-nothing-by-2100.toml  (sample)  — PASS
- quote: ok. Captions at 42:50–42:59: "I would give a five maybe 10% chance that we you know that we get to 2100 uh uh and none of these things that I've I've I've described uh happen".
- date: ok as "2025-01". Uploaded 20250127.
- role: ok.
- admission: ok.
- due: ok, 2100.
- verdict: ok. It is `unfalsifiable` and carries `has_probability`.
- notes: `prediction` says a 90 to 95 percent chance that "the things ... will have happened". The opposite of "none of these things happen" is "at least some happen", not all of them. Suggest "that at least some of the things he described will have happened". No count changes.

### 2025-01-amodei-virtual-collaborator-parts-in-2025.toml  (hits)  — PASS
- quote: ok. Captions at 7:21–7:27.
- date: ok as "2025-01".
- role: ok.
- admission: ok.
- due: ok, 2025-12-31.
- verdict: ok. Anthropic's "Introducing Claude 4" is dated May 22, 2025. It has "with the ability to work continuously for several hours" and "Claude Code is now generally available". His words are "maybe it checks in with you every once in a while", so checking in is a "maybe". The test makes it firm, and Claude Code does ask the user along the way, so it is met either way. `evidence_by = maker` is honest.
- notes: The file points to the Wall Street Journal claim of 2025-01-21 as the earlier claim it changes (its `restates` field), while saying which came first is uncertain. That is acceptable, since it changes no count. The linked file exists.

### 2025-02-11-amodei-paris-country-of-geniuses-2026-or-2027.toml  (sample)  — PASS
- quote: ok. Verbatim in the second paragraph. The page is dated "Feb 11, 2025".
- date: ok.
- role: ok.
- admission: ok, hedged with "possibly".
- due: ok. Due 2027, with `due_early` 2026.
- verdict: ok, not yet due. "An entirely new state populated by highly intelligent people" is a stated comparison, so a plain-reading test is right.
- notes: The test's "each copy at least as capable as a highly intelligent person" is a fair plain reading. It goes slightly past the words of this one statement, but not in a direction that suits a verdict.

### 2025-02-11-amodei-paris-country-of-geniuses-by-2030.toml  (sample)  — PASS
- quote: ok. The words "(and almost certainly no later than 2030), the capabilities of AI systems will be best thought of as akin to an entirely new state" are verbatim.
- date, role, admission: ok.
- due: ok, 2030.
- verdict: ok, not yet due.

### 2025-02-28-amodei-70-80-percent-before-end-of-decade.toml  (sample)  — PASS
- quote: ok. Captions at 33:09–33:13: "70 80% we get that before the end of the decade and my guess is 2026 or 2027". What "that" refers to is at 33:01–33:06: "a very large number of AI systems that are much smarter than humans at almost everything".
- date: ok. YouTube upload_date is 20250228.
- role: ok.
- admission: ok.
- due: ok. "Before the end of the decade" with no usage given takes the later year, 2030.
- verdict: ok, not yet due. `has_probability` is set. The point guess "2026 or 2027" is listed among the repeats of the DeepSeek essay record of 2025-01-29, which I confirmed.

### 2025-02-28-amodei-coding-near-best-humans-end-2026.toml  (sample)  — PASS
- quote: ok. Captions at 42:33–42:40: "by the end of 2026 it might it might be you know everything you know close to the level of the best humans". It follows "for coding".
- date: ok.
- role: ok.
- admission: ok, hedged with "might".
- due: ok, 2026-12-31, still ahead.
- verdict: ok, not yet due.

## Counts
PASS 13 / FAIL 1 / COULD NOT VERIFY 0

- FAIL: 2024-amodei-new-model-most-intelligent-by-airing. Its `verdict_why` says the "most intelligent" lead rests only on Anthropic's word. The outside LiveBench benchmark (arXiv 2406.19314 v1, 2024-06-27) put Claude 3.5 Sonnet first overall, ahead of GPT-4o. The outside record is split, so the reason needs rewriting and the "did not come true" verdict needs John's ruling.

## Batch 2

# Second-pass results, batch b2-2 (Amodei 4, Hassabis 10)

Checked 2026-10-19. I read the captions with yt-dlp, each video into its own new folder
`dl2-b22-<video id>`. I fetched the pages with curl into `dl2-b22-pages`. For the Kantrowitz
video, the first two caption requests were refused (HTTP 429, too many requests). The third
request, for the original-language track only, worked. Every search-log row that these files
cite exists in `data/search_log.csv`.

### 2025-05-22-amodei-one-person-billion-dollar-company-2026  (fails)  — PASS
- first-pass problem: fixed. The test now reads "its other work done by AI systems in place of employees". That condition is grounded in his own words: in "Policy on the AI Exponential" (June 2026; I read it on darioamodei.com) he writes "I've predicted that AI will enable single individuals to create billion-dollar companies".
- quote: ok. The captions at 16:10 to 16:14 read "when do you think there'll be the first billion dollar company with one human employee? 2026." The captions do not mark speakers. The words are the interviewer's question plus the one-word answer, and the file says so.
- date: ok. The event was on 2025-05-22. The re-upload is dated 20250529, by Techusiness.
- role: ok. He was chief executive of Anthropic.
- admission: ok now. The lead-in, "the 5 to 10 year time horizon ... in AI", and the later post both tie the answer to AI.
- due: ok. "2026" gives 2026-12-31.
- verdict: `not_yet_due` is right.
- notes: there is still no Anthropic upload; the file's `verify` field already records that. "or earning" slightly widens the plain sense, which is "valued at". It changes nothing in practice.

### 2025-07-30-amodei-same-cost-much-more-capable-two-years  (sample)  — FAIL
- quote: ok. It is verbatim in the captions at 31:16 to 31:25: "two two years from now my guess is that we'll have models that cost of the same order of magnitude that they cost today except they'll be much more capable".
- date: ok. The upload date is 20250730.
- role: ok.
- admission: acceptable but borderline. Half of it is a price forecast, close to the business-forecast exclusion. The capability half carries it.
- due: ok. 2027-07-30 is judged at 2027-12-31.
- verdict: `not_yet_due` is right.
- what must change: the test waters down his words. He said "much more capable of doing work much more autonomously much more broadly than they are capable of today" (31:22 to 31:29). The test says only "scoring clearly higher on public tests". Any rise in a benchmark score would pass it. The test should keep "much more capable", and the conditions "much more autonomously" and "much more broadly". This is the same fault the first pass found in the swarm test.

### 2025-08-06-amodei-cheeky-pint-country-of-geniuses-one-to-three-years  (sample)  — PASS
- quote: ok. It is verbatim in the supplied English caption track at 55:14 to 55:22. The "..." leaves out "I don't know exactly how long it's gonna be,", as the notes say.
- date: ok. The upload date is 20250806.
- role: ok.
- admission: ok. It is a hedged bet ("if I were to bet").
- due: ok. It runs 2026 to 2028, with `due` 2028 and `due_early` 2026.
- verdict: `unfalsifiable` is right. "Country of geniuses" comes up only once in the captions and is never defined. The other talk of "genius" (34:25) is about discoveries, not a definition.
- notes: the earlier claim it restates (`2025-02-11-amodei-paris-country-of-geniuses-2026-or-2027`) exists. Moving the end from 2027 to 2028 makes this a changed repeat. The statement row it was seeded from (`amodei-2025-08`) exists and matches the date.

### 2026-09-12-amodei-pace-swarm-could-take-over-internet-six-to-twelve-months  (fails)  — PASS
- first-pass problem: fixed. The test now keeps "such a swarm" (greater abilities, similar level of misbehaviour) and "taking over the entire internet with a persistent botnet".
- quote: ok. It is verbatim in the paragraph beginning "My second concern is the OpenAI-Hugging Face incident".
- date: minor. The page says only "September 2026", and 2026-09-12 is the date of the first Hacker News submission. The notes explain this. The format `YYYY-MM` would be more exact. No count changes.
- role: ok.
- admission: acceptable. It is a worry with "could", scored at face value.
- due: ok. The window runs to September 2027, judged at 2027-12-31.
- verdict: `not_yet_due` is right.

### 2011-01-hassabis-human-level-agi-twenty-plus-years  (neg)  — PASS
- quote: ok. Captions at 0:24 to 0:30: "reaching human level AGI even by the most optimistic um kind of estimates is probably a 20year plus project". He repeats it at 39:57 to 40:02 ("probably ... 20 plus years away um for human level AGI"), which shows it is his own forecast.
- date: ok. The conference ran 2011-01-14 to 17. The upload is dated 20111212.
- role: ok. He co-founded DeepMind in 2010 and was its chief executive.
- admission: ok. It is a forecast that something will not happen by a date, so reading 2 admits it.
- due: minor. Reading 2 scores at the stated date. Twenty years from January 2011 is January 2031, and the file judges it at 2030-12-31, about two weeks short. No count changes before 2030.
- verdict: `unfalsifiable` follows reading 4. I re-read the talk. "Toddler AGI" (19:47 to 20:58) is an interim goal. Human-level AGI is drawn as "the entire circle" (21:34). No comparison or test is given anywhere.
- notes: none.

### 2011-01-hassabis-transfer-learning-concepts-five-years  (sample)  — FAIL
- quote: ok. It is verbatim in the captions at 39:07 to 39:16.
- date and role: ok, as in the file above.
- admission: ok.
- due: ok. Five years from January 2011 is judged at 2016-12-31.
- verdict: problem. The reason given is that "conceptual knowledge acquisition has no agreed test" and that "some kind of" sets no level. But the same talk defines both terms:
  - Conceptual knowledge (22:32 to 24:29): information abstracted above the perceptual level ("it's a mammal ... good for guarding things"), below the symbolic level.
  - Transfer learning, in the psychology sense (35:10 to 35:42): extracting "the underlying rules" learned in one perceptual context and applying them "correctly in a completely new perceptual context".
  
  The method says the test is the speaker's own definition when the same source gives one. "Cannot fail" is also not the same as "cannot be tested": if the words are easy to meet, the claim is an easy hit, not untestable. As filed, the entry takes a likely-scored claim out of Hassabis's rate.
- what must change: write the test from his own definitions: by 2016-12-31, AI systems shown to transfer learned rules to a completely new-looking perceptual context, and to acquire abstract conceptual knowledge. Then score it with a dated record. Or bring the call to John as a judgement. Either way, drop the "no agreed test" reason.

### 2023-12-06-hassabis-bard-advanced-early-next-year  (hits)  — PASS
- quote: ok. It is verbatim in "Gemini Ultra coming soon", in the section written "By Demis Hassabis ... on behalf of the Gemini team". The post is dated Dec 06, 2023.
- date, role, admission: ok.
- due: ok. "Early next year" gives 2024-03-31 under reading 1.
- verdict: ok. The post of Feb 08, 2024 says "Today we're launching Gemini Advanced — a new experience that gives you access to Ultra 1.0", "available today in more than 150 countries and territories". Every condition is met before 2024-03-31. `verdict_on` 2024-02-08 is right, and `evidence_by` "maker" is honest.

### 2023-12-06-hassabis-gemini-ultra-developers-enterprise-early-next-year  (fails)  — PASS (judgement noted)
- first-pass problem: fixed. The claim is rescored as missed, with `not_come`. The Workspace record of 2024-02-21 is added for the business half. The test now names the limited stage that the sentence itself sets apart. I confirmed each record:
  - The Cloud post of 2024-02-15 says "generally available on Vertex AI for customers via allowlist".
  - The Workspace post of 2024-02-21 says the standalone chat for business customers is "built on our 1.0 Ultra model".
  - The archived Gemini API model lists of 2024-03-25 and 2024-04-18 name 1.5 Pro (preview only), 1.0 Pro and 1.0 Pro Vision. "Ultra" appears in neither page's HTML.
- quote: ok. The words are verbatim, and the full sentence is in the notes.
- date, role, admission, due: ok.
- verdict: defensible. One judgement should stay visible to John. The miss sets aside the chief executive's own note of 2024-02-15: "Today, developers and Cloud customers can begin building with 1.0 Ultra too — with our Gemini API in AI Studio and in Vertex AI". The method lets a maker's word settle a claim, and Bard Advanced was settled that way. Here the maker's own model list and allowlist post contradict the note, which is a fair reason to prefer them. The file already states this.
- notes: `verdict_on` 2024-04-18 is the date of the archive snapshot. The due date, 2024-03-31, or the 2024-03-25 snapshot would be a closer date for a "not come" miss. Minor.

### 2024-05-14-hassabis-astra-capabilities-gemini-app-later-this-year  (sample)  — FAIL (judgement for John)
- quote: ok. Subtitles at 28:52 to 29:02: "Some of these agent capabilities will come to Google products like the Gemini app later this year." It is inside his segment, which starts at 20:58 ("DEMIS HASSABIS").
- date, role, admission: ok.
- due: ok, 2024-12-31.
- verdict: problem. The test reads "available to the public in a Google product such as the Gemini app". On 2024-12-11 Google released the Multimodal Live API, with "real-time audio, video-streaming input" (the Gemini 2.0 post, which I read). Google AI Studio's "Stream Realtime" let anyone share a camera or screen and talk with Gemini live in December 2024 (TestingCatalog, Tom's Guide, and Google's AI Studio forum threads of that month). AI Studio is a Google product open to the public. That looks like "live camera or video understanding in conversation" by 2024-12-31. The verdict sets it aside as "a developer demonstration" because the maker described the Astra capabilities as still to come. That adds a condition the test does not state: a consumer product. His "some of these agent capabilities" is also a low bar.
- what must change: read the test as written and score a hit, with `verdict_on` 2024-12-11 and evidence by the maker. Or put to John whether a developer tool counts as "Google products like the Gemini app". The test is fixed, so it must not be narrowed now to keep the miss.

### 2024-12-11-hassabis-gemini-2-more-google-products-early-next-year  (hits)  — PASS
- quote: ok. "Early next year, we'll expand Gemini 2.0 to more Google products." It sits under "Gemini 2.0 available in Gemini app", in the section by Hassabis and Kavukcuoglu. The post is dated Dec 11, 2024.
- date, role, admission: ok.
- due: ok, 2025-03-31 under reading 1.
- verdict: ok. The post of Mar 05, 2025 says "we've launched Gemini 2.0 for AI Overviews in the U.S." `evidence_by` "maker" is honest.
- notes: "more Google products" is plural, and the test asks for "at least one further". That is generous but defensible. The same December post, in Pichai's section, says AI Overviews testing on 2.0 had already started "this week". The March launch is the broad roll-out that post promised, so it does count.

### 2025-04-20-hassabis-ai-poses-scientific-conjecture  (sample)  — PASS
- quote: ok. It is verbatim in the archived CBS transcript (April 20, 2025): "I think actually in the next maybe five to ten years. I think we'll have systems that are capable of not only solving an important problem or conjecture in science but coming up with it in the first place."
- date, role, admission: ok.
- due: ok. Five to ten years gives 2035, with an early end of 2030.
- verdict: `not_yet_due` is right.

### 2025-04-20-hassabis-robotics-breakthrough-couple-of-years  (sample)  — PASS
- quote: ok. It is verbatim in the same transcript.
- date, role, admission: ok.
- due: ok. April 2027 is judged at 2027-12-31.
- verdict: `not_yet_due` is right.
- notes: two minor points. The test adds "general-purpose", which is not in his words ("humanoid robots or other types of robots that can start really doing useful things"); it should be dropped. The Fortune repeat at Davos, January 2026, is described only in the notes and is not entered in `repeated_on`.

### 2025-05-20-hassabis-gemini-25-flash-generally-available-early-june  (fails)  — PASS
- first-pass problem: fixed. "Early June" is now read as by 2025-06-10, the first third of the month, and the status is `missed`, direction `later`. This is the builder's call (b), flagged for John.
- quote: ok. Captions at 20:21 to 20:25: "I'm excited to say that Flash will be generally available in early June with Pro soon after."
- date, role, admission: ok.
- due: reasonable. Reading 1 takes the first quarter of a year. Taking the first third of a month is slightly more generous than the strict match, which would be about the 7th or 8th. The verdict does not depend on it: general availability on 06-17 misses every reading except the whole month, including a first-half reading (the 15th).
- verdict: ok. The post of Jun 17, 2025 says "Gemini 2.5 Flash and Pro are now generally available".
- notes: Pro came the same day, not "soon after". The verdict says so. Minor.

### 2026-01-20-hassabis-physical-intelligence-breakthrough-18-months-to-two-years  (sample)  — PASS
- quote: ok. Captions at 4:06 to 4:11: "of uh a kind of breakthrough moment in physical intelligence. I still think we're about 18 months two years away". The quote starts at "a kind" and is fine.
- date: ok. The upload date is 20260120 (Bloomberg Live).
- role, admission: ok.
- due: ok. The range runs from July 2027 to January 2028, giving `due` 2028 and `due_early` 2027. It is a changed repeat of the April 2025 claim, which keeps its 2027 date.
- verdict: `not_yet_due` is right.
- notes: it copies the April 2025 test, so drop "general-purpose" here too.

## The builder's own calls, where these files touch them
- (a) "The coming months" and "the coming weeks" are treated as undated, in search-log rows 034 (the Gemini launch post of December 2023) and 037 (the I/O 2024 keynote). This is a reasonable extension of reading 3. "Few" and "coming" name no length.
- (b) "Early" in a month is read as by the 10th. Reasonable, and slightly more generous than reading 1's proportion. It changes no verdict here, since 06-17 misses any reading but the whole month.

## Summary

PASS 11, FAIL 3, COULD NOT VERIFY 0.

- **Amodei, models costing the same in two years (2025-07-30):** the test drops "much more autonomously, much more broadly" and softens "much more capable" to "clearly higher on public tests". Restore his words.
- **Hassabis, transfer learning and conceptual knowledge within five years (2011):** it is marked "cannot be tested", but the same talk defines both terms. Write the test from his definitions and score it, or put the call to John.
- **Hassabis, Astra capabilities in Google products in 2024 (2024-05-14):** it is scored missed, but AI Studio's public live camera and screen sharing (2024-12-11) meets the test as written. Score it a hit, or get John's ruling on whether a developer tool counts.

## Batch 3

# Second-pass check, batch 2-3 (14 files), 2026-10-19

Sources fetched fresh into `dl2-3-yt/` (captions via yt-dlp) and `dl2-3-web/` (curl, r.jina.ai for cnbc.com and openai.com). Repository not touched.

### 2026-01-hassabis-agi-five-to-ten-years-defined  (sample)  — PASS
- quote: ok. Automatic captions, 8:52 to 8:54: "And I think, you know, we're 5 to 10 years away from that." His definition is at about 7:09 to 8:50, in his own words ("a system that um can exhibit all the cognitive capabilities humans can and I mean all", new theories of physics, a new genre of art, physical intelligence at elite-sports level).
- date: ok. Uploaded 2026-01-23 (Alex Kantrowitz channel); recorded at Davos, day not given. `when = 2026-01` is honest.
- role: ok (chief executive of Google DeepMind).
- admission: ok.
- due: ok (2036, early end 2031).
- verdict: ok. Not yet due. The test is his own definition from the same answer, so it is testable under reading 4.
- notes: `restates` points to the Davos panel claim of 2026-01-20, and that file's notes say this interview was "days later". The recording day is not known and could be before 2026-01-20, so the order of the chain is not shown. This does not change any count. Better wording would say "the same week".

### 2026-04-07-hassabis-flourishing-could-happen-within-fifty-years  (sample)  — PASS
- quote: ok. Captions 57:40 to 57:45: "That would be I think an amazing outcome and I think could happen within the next 50 years."
- date: ok (upload 2026-04-07; Cleo Abram channel).
- role: ok.
- admission: borderline, but acceptable. Cleo Abram's question sets it up as a story ("Could you play out for me the plot of the sci-fi movie in your head..."). He then steps out of the story ("But I think even 50 years some of this could happen where we've got through the AGI moment safely") and gives a real, dated forecast of what AI will help achieve. The builder's call (c in the brief) to treat "could happen within" as a hedge and score it is a reasonable reading, because "within" sets an upper limit. It is not "as little as". The owner may still want to know that the question was framed as a story.
- due: ok (2076).
- verdict: ok. "Maximum human flourishing" has no measure, so it cannot be tested.
- notes: the locator "57:20 to 57:44" is right (the quoted words end at 57:45).

### 2016-09-28-huang-self-driving-cars-on-road-couple-of-years  (hits)  — PASS
- quote: ok. Captions (official NVIDIA upload of 2016-09-29) read the run verbatim: "we're going to see some self-driving cars get on the road here in the next next year or make no no more than next year and no more than the next couple of years".
- date: ok. Uploaded 2016-09-29; the keynote was on 2016-09-28.
- role: ok.
- admission: ok.
- due: ok (2018, early end 2017).
- verdict: ok. Waymo's post, dated "November 7, 2017", says: "Waymo's fully self-driving vehicles ... are test-driving on public roads, without anyone in the driver's seat ... a subset of our fleet will operate in fully autonomous mode". That meets every part of the test before the early end. The record is from outside Nvidia.
- notes: two judgement calls, neither changing the verdict. (1) The sentence sits inside a pitch for Nvidia's DriveWorks software ("even though we're going to see some self-driving cars get on the road ... we're going to continue to enhance the software"). A reader could take it to mean cars on Nvidia's platform. The file takes it as cars in general, which is the plainer reading. (2) The test adds "with nobody at the wheel". He did not say that, but it makes the test harder, not easier, and without it the claim would already have been true when he said it.

### 2018-05-10-huang-self-driving-cars-2020-to-2021  (fails)  — PASS
- first-pass problem: fixed.
- quote: ok. Motley Fool transcript, fetched directly with a browser user agent: "I expect that driverless taxis will start going to market about 2019 and self-driving cars probably somewhere between 2020 and 2021."
- date: ok. The transcript header reads "May 10, 2018, 5:00 p.m. ET".
- role: ok.
- admission: ok.
- due: ok (2021, early end 2020).
- verdict: ok. The test now takes his usage from the sentence just before: "the ASPs for Level 2 could be a few hundred dollars to a Level 5 self-driving car, taxi, or driverless taxi being a few thousand dollars". That is what the first pass asked for. Honda's release ("March 4, 2021") shows that the most automated car on sale was the Legend: Level 3 "conditional automated driving in limited area", leased in Japan from 2021-03-05, limited production of 100 units. That is far short of a car that needs no driver. Missed, direction "has not come"; both are right.
- notes: the bracketed gloss in the test ("one that drives itself with no driver needed") is looser than Level 5, which means driving anywhere, in all conditions. It is close to Level 4. No car of either level was sold to the public by 2021, so the verdict holds either way. The test change is recorded in the notes and in search-log row huang-claims-107 (the re-read of the transcript).

### 2021-04-12-huang-multi-trillion-parameter-models-2022  (hits)  — PASS
- quote: ok. Uploaded captions, 00:50:04: "We expect to see multi-trillion-parameter models by next year, and 100 trillion+ parameter models by 2023."
- date: ok (upload 2021-04-12).
- role: ok.
- admission: ok. It is about the size of AI models, not hardware.
- due: ok (2022).
- verdict: ok. arXiv 2110.03888 was "Submitted on 8 Oct 2021". Its title is "M6-10T: A Sharing-Delinking Paradigm for Efficient Multi-Trillion Parameter Pretraining", and it reports "pretraining unprecedented 10-trillion-parameter model ... on solely 512 GPUs within 10 days". The record is from outside Nvidia, and "sooner" is right.
- notes: M6-10T is a sparse "mixture-of-experts" model (only part of it runs for each input). He did not say the models had to be dense, so the test is fair.

### 2021-11-09-huang-most-new-evs-substantial-av-capability-2024  (sample)  — PASS
- quote: ok. Captions, 01:31:41 to 01:31:46: "By 2024, the vast majority of new EVs will have substantial AV capability." The locator says 1:31:35, close enough.
- date, role, admission, due: ok.
- verdict: ok. "Substantial" has no measure, so "cannot be tested" is a fair call. The line before it ("everything that moves will be autonomous either fully or mostly autonomous") has no date and does not define the term.

### 2022-02-16-huang-all-new-jlr-vehicles-nvidia-drive-2025  (sample)  — PASS
- quote: ok. Motley Fool transcript (header "Feb 16, 2022, 5:30 p.m. ET"): "Starting in 2025, all new Jaguar and Land Rover vehicles will have next-generation automated driving systems, plus AI-enabled software and services built on the NVIDIA DRIVE platform."
- date: ok.
- role: ok.
- admission: ok, but compare with another case. Search-log row huang-claims-104 left out BYD's adoption of the DRIVE Orin computer as "a customer's production date". This claim names automated-driving systems and AI software, so it is about deploying AI, and keeping it is defensible.
- due: ok (2025).
- verdict: ok, with a soft spot. The newmobility report of 2025-07-22 says "deliveries originally planned for the end of 2025 will now not commence until 2026". It is a forward-looking report that relays The Guardian, not a record made after the due date. Nothing suggests a JLR car on Nvidia DRIVE reached customers in 2025.
- notes: (1) The test's line "'All new' vehicles is the condition; at least the first such vehicle must reach customers in 2025" is muddled, but the claim is a miss under either reading. (2) For the owner: the sibling claim from 2022-03-22 (Hyperion 8, the Nvidia platform of computers, sensors and software, to ship in JLR cars in 2025) is a second miss for the same JLR 2025 event. It was kept as a "changed condition", but the two are close to an unchanged repeat with the same due year. Counting both could double a miss on Huang's record. That file is not in this batch, so this is flagged here, not failed.

### 2024-03-01-huang-ai-does-well-on-every-human-test-five-years  (sample)  — PASS
- quote: ok. Captions verbatim: "I'm guessing in 5 years time we'll do well on every single one of them".
- date: ok. 2024-03-01 was a Friday (Reuters says "on Friday"); uploaded 2024-03-07.
- role: ok.
- admission: ok. "If I gave an AI..." is the setup of a definition, not a hypothetical.
- due: ok (2029).
- verdict: ok, not yet due.
- notes: the test turns "do well" into "at or above a passing human score". That is a fair plain reading.

### 2024-06-02-huang-mercedes-self-driving-production-2025  (fails,hits)  — PASS
- first-pass problem: fixed. `evidence_by` is now `maker` and `verdict_source` is Nvidia's blog. The test now names "the entire stack" from his own sentence. The quote now comes from the clean caption track.
- quote: ok. The English (US) captions, about 1:42:2x: "NVIDIA again builds the entire stack. Next year we're going to go to production with the Mercedes fleet. And after that, in 2026, the JLR fleet".
- date, role, admission, due: ok.
- verdict: ok as a hit on the maker's word. Nvidia's blog is dated "January 5, 2026" and headlined "NVIDIA DRIVE AV Software Debuts in All-New Mercedes-Benz CLA". It says the CLA "introduces advanced driver-assistance features powered by NVIDIA's full-stack DRIVE AV software". Production in 2025 comes from electrive (2025-06-04), which is outside Nvidia.
- notes: the softness is stated honestly in the notes. Nvidia's point-to-point system comes to US roads only "by end of this year" (2026). In China the system is Momenta's. Electrive says Europe is only "potentially" in the future. `verdict_on` (2025-06-04, the electrive date) is not the date of the named `verdict_source` (2026-01-05). That is acceptable, because `verdict_on` is the date the event happened.

### 2025-03-18-huang-all-nvidia-software-engineers-ai-assisted-2025  (hits)  — PASS
- quote: ok. Captions verbatim: "100% of Nvidia software Engineers will be AI assisted by the end of this year".
- date, role: ok.
- admission: ok. It is about deploying AI in work, which comes under ruling (g): forecasts that AI will change jobs are admitted. It is in his own company's control, but it is not a budget or headcount figure.
- due: ok (2025-12-31).
- verdict: ok. CNBC's transcript is dated 2025-10-08 ("Published Time: 2025-10-08"). It reads: "every one of our engineers, 100% is now assisted by AI coders". Later in the same interview he says "Almost every one of them are going to use it" about Cursor (an AI coding tool), as the file says. It is marked `maker`, which is right.

### 2026-01-05-huang-large-share-of-cars-autonomous-ten-years  (sample)  — PASS
- quote: ok. Captions verbatim: "In in the next 10 years, I'm fairly certain a very, very large percentage of the world's cars will be autonomous or highly autonomous."
- date, role, admission, due: ok (2036).
- verdict: ok. "Cannot be tested" is consistent with his 2021 "substantial AV capability" claim.

### 2024-03-kaifulee-ai-capabilities-dwarf-humans-two-to-three-years  (lee)  — PASS
- quote: ok. Automatic captions: "I think in the next two to three years uh if the human circle of what human capabilities is this big uh you know the AI will be the size of Earth but it still may not do what everything we can do".
- date: ok. Fortune (2024-05-25): "the Fortune Innovation forum in Hong Kong in March". In the video the host says 01.AI was "spun up about exactly a year ago". The video was uploaded 2024-05-23.
- role: ok. He was introduced as 01.AI's chief executive and founder, after 2023-03-19.
- admission: ok. It is about what AI will be able to do. The "if" is a figure of speech, not a hypothetical. Earlier in the same answer he says "AGI is defined to be a superset of human intelligence", but the dated line is the circle image, not that stage.
- due: ok (2027, early end 2026). "Two to three years" is a stated length, so reading 3 does not apply.
- verdict: ok. A picture with no quantity cannot be tested.

### 2024-03-kaifulee-hallucination-solved-in-eighteen-months  (lee)  — FAIL (the verdict text misstates its own source's figures)
- quote: ok. Captions about 19:2x: "many of the problems that plague these systems like hallucination we we I can predict uh that they will be more or less solved in a year and a half or so".
- date: ok (March 2024, as above).
- role: ok.
- admission: ok. It is about what AI will be able to do, with a length of time.
- due: ok (about September 2025; judged 2025-12-31 under the span rule).
- verdict: the status `missed` is right, but the text must change. OpenAI's post ("Why language models hallucinate", 2025-09-05) says "GPT‑5 has significantly fewer hallucinations ... but they still occur. Hallucinations remain a fundamental challenge for all large language models". That is a dated record before the due date and enough on its own. The problem is the Vectara figures. Its README ("Last updated on October 16, 2026") does show 1.8% for the best model, but that model is antgroup/finix_s1_32b, not a frontier model. The phrase "3 to 6.5% for current frontier models" is wrong. The 3.1% is gpt-5.4-nano and the 6.5% is gpt-6-sol. Other current frontier models run higher: gpt-5.4 7.0%, gpt-5.5 9.3%, gemini-3.1-pro-preview 10.4%, claude-opus-4-7 12.0%, gemini-3-pro-preview 13.6%. What must change: correct the figure, for example to "about 6.5 to 14% for current frontier models". Better still, make OpenAI's 2025-09-05 post the `verdict_source`, since it is dated before the due date. The Vectara table is a snapshot from ten months after the due date, on a dataset Vectara has changed since. The verdict and the counts do not change; the mistake makes the miss look narrower than it is.
- notes: "more or less solved" has no number. The test turns it into "apart from rare slips", which is a fair plain reading. A reader could argue it cannot be tested, as with Huang's "substantial". It is scorable here because the leading maker's own words say the problem "remains a fundamental challenge".

### 2024-06-14-kaifulee-every-app-rewritten-with-ai-in-two-years  (lee)  — PASS
- quote: ok. Captions verbatim: "one and a half to two years we will see jni blossom in every application every existing app will be Rewritten with Gen uh inside".
- date: acceptable. Uploaded 2024-06-14. The interviewer mentions "big news this week from Apple" (WWDC, 2024-06-10). The day of the session is not confirmed; it may be 2024-06-13. The `when_note` says the day is not given, but `when` is still a full date. Better: `when = "2024-06"`, or say plainly that the date is the upload date.
- role: ok (01.AI chief executive; he opens with "rather than investing in someone I would do it myself this time").
- admission: ok.
- due: ok (2026, early end 2025). Not yet due by its own date in any case.
- verdict: acceptable, and consistent with his other app claims (the 2024-11-26 "proliferation" and "flood" claims, and the 2025 "rewritten" claim, all "cannot be tested"). A note for the owner: "every existing app" taken literally could be tested, and it would plainly fail. The ledger treats it as an image with no count.
- notes: the repeat on the Diamandis podcast is verbatim ("in about two years every app we use will be replaced by another app or super upgraded by the same app"). It sits at about 1:03:2x in the current upload, not 1:02:59. That is minor.

## Builder's own calls (a to g) touched by this batch
- (c) A hedge with "within" is scored, not treated as a hypothetical: touched by the Hassabis flourishing claim. A reasonable reading.
- (g) Jobs forecasts admitted: touched only at the edge, by the Nvidia engineers claim, where it is consistent.
- (a), (b), (d), (e), (f): not touched by these files.

## Counts
PASS 13 / FAIL 1 / COULD NOT VERIFY 0.
- FAIL: 2024-03-kaifulee-hallucination-solved-in-eighteen-months. The verdict text gives "3 to 6.5% for current frontier models" from Vectara's leaderboard; current frontier models there are about 6.5 to 14%, and the 1.8% best is not a frontier model. The status `missed` stands. Correct the figure and name OpenAI's 2025-09-05 post as the source.

## Batch 4

# Second-pass check, batch b2-4 (Kai-Fu Lee's claim files), 2026-10-19

Sources opened this pass: the Moonshots podcast captions (YouTube n1BVlDPercI, uploaded 2024-12-05) and the Astana Hub talk captions (YouTube nNtan_n1BD0, uploaded 2025-10-30), both read with yt-dlp; Recode China AI's translation (via r.jina.ai); the Chinese original text of the Qianwang interview on WeChat (mp.weixin.qq.com/s/o8ZGtKLs1CbFXtgbFQK56g, linked from the Recode page) and the podcast page on page.om.qq.com; WIRED's column; the People's Daily app interview; the Kazinform report; OpenAI's "Introducing GPT-5"; Physical Intelligence's π0.5 post (pi.website/blog/pi05).

Two findings run across several files:

- **The Qianwang interview was first published on 2024-11-05, not 2024-11-10.** Tencent Tech's WeChat account (Zhang Xiaojun's byline) published the full printed text of the conversation ("以下是对话全文", lightly edited by the author) with creation and send timestamps of 1730785897, which is 2024-11-05 05:51 UTC (13:51 Beijing time). The 2024-11-10 date belongs to the audio podcast page. Recode's translation links this WeChat article as "the original Chinese story". So the builder's statement that the original is "a Chinese audio podcast with no captions or transcript" is wrong. A printed Chinese question-and-answer text in his own words exists, and both lines are in it (details under each file).
- **WIRED does not sign the column as chief executive of 01.AI.** The byline on the page reads "Kai-Fu Lee is the CEO of Sinovation Ventures and author of AI Superpowers", and the column never names 01.AI. Its one example is a team he says he is "backing" (Rhymes.ai). He did hold the 01.AI role on 2024-11-26, so the claims still qualify under the role rule. But the `occasion` sentence states a false fact about the source.

None of my files was a `fails` file, so there is no "first-pass problem" line. Of the builder's seven unruled calls, only (g), admitting jobs forecasts, touches this batch (two files). I judge it reasonable; see those files.

---

### 2024-10-kaifulee-agi-better-at-almost-everything-five-to-ten-years.toml  (lee)  — FAIL
- quote: ok. The captions read "then I think it's highly likely that it will arrive in the next 5 to 10 years", verbatim.
- date: ok. The upload is 2024-12-05. "Founded it 17 months ago" is at 30:02, and the host says the FII summit is "in just 10 days or so" at 55:27. Two more clues support October 2024: "congrats to him [Hinton] on his Nobel" at 52:07, and "we just saw a number of Nobel prizes related to AI". The Nobel prizes were announced 2024-10-08 and 2024-10-09.
- role: ok. 01.AI founder and chief executive, after 2023-03-19.
- admission: ok. It looks forward, is about AI, is dated and is not a hypothetical.
- due: ok. 2029 to 2034, with 2034 as the due year and 2029 as the early end.
- verdict: not_yet_due is correct. **But the test narrows his words.** His definition is AI that "does almost everything we do so much better, even the most challenging intellectual tasks like inventing a new theorem or something in physics or chemistry". The bar turns "almost everything we do" into "almost all the thinking work people do". The only thing he set aside was love (and doing "absolutely everything"), not physical work, so the bar drops a condition he stated. Fix: the bar should read "almost everything people do, much better than people, including the hardest intellectual work ...". It must be fixed at entry, because the bar is never changed afterwards.
- notes: The locator "55:47 to 56:45" stops before the quote. The definition starts at about 56:19, and the quoted sentence runs from about 57:00 to 57:09. Suggested locator: "56:19 to 57:09". (Search row kaifulee-claims-048, which records the podcast fetch, gives the same 55:47 start.)

### 2024-10-kaifulee-ai-replaces-white-collar-work-in-five-years.toml  (lee)  — PASS
- quote: ok. Verbatim at 59:51 to 1:00:00, including the doubled "work work".
- date: ok, as above.
- role: ok.
- admission: ok. It is a forecast that AI ("just software") will replace white-collar work. That is a jobs forecast about what AI will do, admitted under the method's amended condition 2. On builder call (g), admitting jobs forecasts: a reasonable reading, and in fact what the method text now says.
- due: ok. "In the next 5 years" from about 2024-10-19 gives 2029.
- verdict: ok. Unfalsifiable: "a lot of the routine and even non-routine work" names no quantity.
- notes: none.

### 2024-10-kaifulee-five-percent-chance-ai-disaster-in-ten-years.toml  (lee)  — PASS
- quote: ok. Verbatim at 52:44 to 52:57. The locator's end, 52:50, is a few seconds early.
- date, role: ok.
- admission: ok. `has_probability` is correctly set.
- due: ok, 2034. One wording point: `due_basis` says the ten-year horizon was "taken up from the host's question". The captions show Lee proposed it ("if we assume it's like a 10-year Horizon is that reasonable"), the host agreed, and Lee then gave the figures. This changes no date.
- verdict: ok. Unfalsifiable: the disaster is undefined, and the claim is a stated chance.
- notes: `kind = "capability"` is an odd fit, but it is harmless.

### 2024-10-kaifulee-robot-cannot-clean-a-room-within-three-years.toml  (neg, lee)  — FAIL
- quote: ok. Verbatim at 1:01:58 to 1:02:05.
- date, role: ok.
- admission: ok. It is a forecast that something will not happen within three years, which reading 2 makes a claim. No "human level" wording is involved.
- due: ok. Three years from about 2024-10-19 is October 2027, judged at 2027-12-31.
- verdict: scored under reading 2, not_yet_due. **But the test changes his words in two places:**
  1. "This robot" means the home humanoid robots the host had just named (Figure's and Tesla's, at about $30,000). The bar widens it to "a humanoid or household robot".
  2. "Cannot even begin to do" is refuted by a robot that can even begin to clean a room. The bar instead requires a robot "that can clean an ordinary person's room across different homes", a higher threshold that makes his forecast easier to come true.

  The widening matters already. Physical Intelligence's π0.5 post of 2025-04-22, the maker's own record, shows a wheeled two-armed robot (not a humanoid) cleaning up bedroom floors and kitchens "in entirely new homes" not seen in training. That is arguably enough to defeat the bar as written, with two years to run. Fix: write the bar in his words: a home humanoid robot of the kind Tesla and Figure build, shown (by its maker or an outside test) at least beginning to clean an ordinary room it was not trained in, by 2027-12-31. Then record in `notes` what has been seen so far (π0.5 is not a humanoid, so on his words it does not settle the claim).
- notes: If the builder decides "household robot" was his meaning, the bar must say why from the source, and the notes must record π0.5.

### 2024-11-10-kaifulee-consumer-ai-apps-explode-first-half-2025.toml  (lee)  — FAIL
- quote (`reported_as`): ok against the Recode translation ("For 2C (consumer-facing) applications, likely within the first half of next year."). The Chinese original text has the same answer in his own words: 《潜望》："全球来看应用会什么时候大爆发？" 李开复："2C应用应该就是明年前半年。" ("When will applications explode globally?" / "For consumer apps it should be the first half of next year.")
- date: **problem.** The words were first published on 2024-11-05 in Tencent Tech's WeChat text of the interview. `when` should be 2024-11-05, and `when_note` should name that article and its timestamp. The id can stay as it is, since files are never renamed.
- role: ok.
- admission: ok.
- due: ok. The first half of 2025 gives `due_date` 2025-06-30.
- verdict: ok. Unfalsifiable: an "explosion" is not measured.
- notes: `checked_how` and search row kaifulee-claims-051 (the podcast-page fetch) both say there is no transcript. That is wrong: the WeChat article is a printed question-and-answer of the conversation. The file could become `printed_qa`, quoting the Chinese words or a faithful translation. At the least, `checked_how` must stop saying the words could not be checked. The `verdict_why` is boilerplate shared with other files and mentions apps being "rewritten", which this claim does not say; it should be trimmed to this claim.

### 2024-11-10-kaifulee-gpt5-not-within-six-months.toml  (hits, neg, lee)  — FAIL (date only; the hit stands)
- quote (`reported_as`): ok against Recode. The Chinese original: "本来GPT-5应该现在已经出来。现在看，即便出来，最快也是半年后了。" ("GPT-5 should have been out by now. As things look, even if it comes out, it will be half a year from now at the earliest.") This is his own answer in the printed question-and-answer.
- date: **problem.** As above, it was first published 2024-11-05, so `when` should be 2024-11-05.
- role: ok.
- admission: ok. A forecast that an AI system will not ship before a date, so reading 2 applies.
- due: acceptable. Six months from 2024-11-05 is 2025-05-05. The builder's `due_date` of 2025-05-31 (rounding to the end of May) is a little later than the stated date. For a "will not happen" claim that makes the test slightly stricter on him, not looser, and it changes nothing here. `due_basis` should say "by 2024-11-05".
- verdict: ok. It is scored under reading 2, as a hit. OpenAI released no model called GPT-5 before 2025-08-07 (GPT-4.5 came in February 2025 and GPT-4.1 in April), so no GPT-5 existed on 2025-05-31 (or on 2025-05-05). Every condition of the bar is met. `verdict_source` (OpenAI's announcement) is the dated primary record of when the thing first came. `evidence_by = "outside"` is right: OpenAI is not his company.
- notes: The same `checked_how` correction as the previous file applies: a printed Chinese transcript exists.

### 2024-11-26-kaifulee-ai-apps-proliferate-within-two-years.toml  (lee)  — FAIL
- quote: ok, verbatim on the WIRED page. Published 2024-11-26T06:35-05:00.
- date: ok.
- role: he held the 01.AI chief executive role that day, so the claim is admissible. **But `occasion` is wrong:** it says "signed as chief executive of 01.AI", while WIRED's byline reads "Kai-Fu Lee is the CEO of Sinovation Ventures", and the column never names 01.AI and speaks partly as an investor ("I'm backing a team"). Fix: correct the `occasion` sentence, and say in `notes` that WIRED signs him as head of Sinovation Ventures and that the role that applies is the 01.AI one he held that day.
- admission: ok.
- due: ok. Two years from 2024-11-26, judged at 2026-12-31.
- verdict: ok. Unfalsifiable: "proliferation" is not measured. The `verdict_why` boilerplate ("rewritten", "flooded", "exploded") is not this claim's wording and should be trimmed.
- notes: none.

### 2024-11-26-kaifulee-flood-of-ai-apps-in-2025.toml  (lee)  — FAIL
- quote: ok, verbatim in the first paragraph.
- date: ok.
- role: the same `occasion` error as the previous file ("signed as chief executive of 01.AI"). The claim is still admissible on the role held.
- admission: ok.
- due: ok, 2025-12-31.
- verdict: ok, unfalsifiable. `restates` points correctly at the Qianwang record. Its notes call that forecast "of 2024-11-10", which needs updating to 2024-11-05 with the fix above.
- notes: The `verdict_why` boilerplate mentions "rewritten", which this claim does not say.

### 2025-01-16-kaifulee-agi-smarter-than-any-human-within-decade.toml  (lee)  — PASS
- quote: ok, verbatim on the People's Daily page.
- date: ok. The page timestamp is 1737039890000, which is 2025-01-16.
- role: ok. The editor's note calls him "now the CEO of 01.AI and chairman of Sinovation Ventures".
- admission: ok. "Gives us hope that we'll reach ..." is a hedged forecast and is scored at face value under the method's hedge rule. This is a borderline reading worth one line in the notes, but it is not wrong.
- due: ok. Within the coming decade from 2025-01-16 gives 2035.
- verdict: ok, not_yet_due. "Overall smarter than any human being" is a stated comparison, so it gets a plain test (reading 4 / the Musk precedent), and the bar keeps it.
- notes: `restates` the October 2024 record: acceptable as a changed repeat.

### 2025-01-16-kaifulee-ai-creates-tenfold-new-jobs-in-five-years.toml  (lee)  — PASS
- quote: ok, verbatim. The page has "data laborers that exist throughout the world"; the quote stops before that.
- date, role: ok.
- admission: ok under builder call (g), admitting jobs forecasts. The method's text says "displace or change jobs" and this is about AI *creating* jobs. Creation is a change in jobs caused by AI, and search row kaifulee-claims-069 (the re-read of the admission rule) records the reading explicitly ("displace, replace, create or change"). A reasonable reading. It would be cleaner if the method's sentence said "create" too.
- due: ok, 2030.
- verdict: ok, not_yet_due. The bar uses his own usage (data labelling as the example of a job AI created) and his number. The flag that settling it may be hard is honest.
- notes: none.

### 2025-01-16-kaifulee-chinese-ai-apps-among-best-in-2025.toml  (lee)  — PASS
- quote: ok, verbatim.
- date, role: ok.
- admission: ok, though "I look forward to 2025 as the year when ..." is a soft forecast.
- due: ok, 2025-12-31.
- verdict: ok. Unfalsifiable, and the same answer gives no measure of "among the best". The change from the first entry (which scored it a hit on "most used") correctly follows the rule that the test uses his words.
- notes: none.

### 2025-10-02-kaifulee-ai-better-than-ninety-percent-in-five-years.toml  (lee)  — PASS
- `reported_as`: ok, matching Kazinform word for word ("18:00, 2 October 2025"). Correctly entered as coverage.
- date: ok.
- role: ok. Kazinform: "CEO of Sinovation Ventures and 01.ai".
- admission: ok. `statement_id` kaifulee-2025-01 (the coded statement from the same Kazinform report) exists, with the same speaker and month 2025-10.
- due: ok. About five years gives 2030.
- verdict: ok, not_yet_due. "Better than 90% of people at 90% of tasks" is a stated comparison and gives a plain test.
- notes: none.

### 2025-10-30-kaifulee-company-run-by-ai-agents-five-to-ten-years.toml  (neg, lee)  — FAIL
- quote: ok, verbatim at about 6:53 to 7:01. The locator "6:44 to 6:55" ends before the sentence does.
- date: acceptable. The upload is 2025-10-30 and the day of the talk is unknown, which `when_note` says. "01.ai AI is my company" at 10:39 confirms the role.
- role: ok.
- admission: ok.
- due / verdict: **reading 2 is not applied.** "In reality we won't get there for another perhaps 5 or 10 years" has the same shape as the method's own example of reading 2 ("it will take at least a decade"). It is also the same shape the builder treated as a "will not happen" claim in the GPT-5 file ("it won't be for another six months at the earliest"). The file instead reads it as an arrival forecast scored at 2035. The two readings give opposite tests: a hit if an agent-run company exists by 2035, against a hit if none exists by the stated date. The notes see the alternative but choose without a ruling. Fix: score it under reading 2. The test would be: no public record, by the stated date, of a company whose departments' work is done by AI agents directed by its chief executive. Take 2030, the earlier end, as the generous date for a "will not happen" claim, or else put the choice of end to John. Alternatively, put the whole reading to John as an open flag before publishing. Either way, the two Lee files should not read the same construction in two ways.
- notes: "But we'll get there step by step" carries no date of its own, so it adds no second claim.

### 2025-10-30-kaifulee-one-person-agent-unicorn-in-five-years.toml  (lee)  — PASS
- quote: ok, verbatim caption words, including the misheard "built by one company". `checked_how` explains it, and the sentence before ("one person build a company from completely AI agents") supports "one person". Consider showing it as "built by one [person]", as search row kaifulee-claims-041 (the Astana talk caption fetch) does, so the public quote does not read wrongly.
- date: acceptable, as for the previous file.
- role: ok.
- admission: ok. It is about AI agents doing a company's work, with the valuation as the measure, so not a plain business forecast.
- due: ok. "Perhaps 5 years from now" from October 2025 gives 2030.
- verdict: ok, not_yet_due. The bar is a plain reading of "unicorn" and "one person and a bunch of agents".
- notes: none.

---

## Counts

PASS 7 · FAIL 7 · COULD NOT VERIFY 0

FAILs, one line each:
1. Lee's October 2024 AGI forecast (five to ten years, almost everything done better): the test narrows "almost everything we do" to "thinking work". Restore his words.
2. Lee's forecast that robots cannot clean a room within three years: the test widens "this robot" (home humanoids) to any household robot and raises "cannot even begin to" to full cleaning. Physical Intelligence's π0.5 of 2025-04-22 may already meet the bar as written.
3. Lee's forecast that consumer AI apps explode in the first half of 2025: `when` should be 2024-11-05, the date Tencent Tech's WeChat printed the full text. `checked_how` is wrong to say there is no transcript.
4. Lee's forecast that GPT-5 would not come within six months: the same date fix (2024-11-05) and transcript correction. The hit itself stands.
5. Lee's WIRED forecast of a proliferation of AI apps within two years: `occasion` says he signed the column as 01.AI's chief executive, but WIRED signs him as CEO of Sinovation Ventures. The role still holds.
6. Lee's WIRED forecast of a flood of AI apps in 2025: the same `occasion` error, and its notes carry the old 2024-11-10 date.
7. Lee's forecast that a company run by AI agents will take five to ten years: "won't get there for another perhaps 5 or 10 years" is not scored under reading 2, though the GPT-5 file reads the same construction under it. Rescore it, or put it to John.

## Batch 5

# Second-pass check, batch b2-5 (Kai-Fu Lee's new claims, 14 files)

Checked 2026-10-19. Sources read:
- the Taldau mektebi (School of Analytics) lecture, YouTube `-QJmhF3ZZH0`, automatic English captions via yt-dlp, uploaded 2025-06-10;
- the CCTV dialogue text reposted on Fudan University's Institute for Development site (fddi.fudan.edu.cn, posted 2026-02-19), read with curl;
- The Mishal Husain Show, YouTube `fVS1PY32pTc`, captions, uploaded 2026-09-04;
- Endgame #279, YouTube `c4w3njBhYVk`, captions, uploaded 2026-09-23;
- Astana Hub's news item of 2025-01-13 (his visit on 2025-01-11), read with curl.

Role, the same for every file: the notes say founder and chief executive of 01.AI. The Fudan text introduces him as 01.AI's chief executive (and chairman of Sinovation Ventures) on 2026-02-04. The two podcasts and the lecture introduce him the same way. Every file is dated after 2023-03-19. One point for John, not a fail: in the 2026-02-04 dialogue Lee says 01.AI is now "All In To B" (working only for businesses), and that only the big firms can carry the cost of training large base models. Since 2025, 01.AI does not appear to train frontier base models of its own. The ruling counts Lee "from 2023-03-19 as founder and head" with no end date, so his claims stay in. The notes' "to build large language models ... still leads it" may need a line saying so.

---

### 2025-kaifulee-agents-and-embodied-ai-within-five-years.toml  (lee)  — PASS
- quote: ok. The captions at 38:38–38:46 read "humanoid robots embodied AI world / models will emerge. All of this will / happen uh in the next five years."
- date: ok. Placing it in 2025 is well supported. The upload is dated 2025-06-10. Astana Hub's item confirms the visit on 2025-01-11. He says "in the hub" at 37:01, and "the first year of LLMs ... that was two years ago" at 38:20. Against that, "this year Nobel prize" at 20:18 leans to 2024. The choice of 2025 is flagged and is the generous one.
- role: ok (see above).
- admission: ok. It is about AI, looks forward, carries a span and is not a hypothetical.
- due: ok. 2025 + 5 = 2030.
- verdict: ok. "Unfalsifiable" is reasonable: "emerge", "appear" and "come around" set no level, and humanoid robots and agents already existed.
- notes: none.

### 2025-kaifulee-ai-2041-forecasts-in-five-to-eight-years.toml  (lee)  — PASS
- quote: ok. The captions at 38:46–38:55 match word for word.
- date: ok (as above).
- role: ok. The 2021 book is rightly left out; this is his re-dating of it in 2025.
- admission: ok.
- due: ok. The range 2030–2033 takes its later end, with 2030 as the early end.
- verdict: ok. "Unfalsifiable" holds, because "all of that" points at a book of stories.
- notes: none.

### 2025-kaifulee-ai-cures-for-incurable-diseases-five-to-ten-years.toml  (lee)  — PASS
- quote: ok. The captions at 21:51–22:12 match. The ellipsis leaves out "because one where we've never been able to train these thousands and millions of super AI Nobel quality AI agents. This is all going to happen uh not just not in 30 years". Joining the two parts does not change what he says, because "this is all" includes the cures.
- date: ok (as above).
- role: ok.
- admission: ok.
- due: ok. The range 2030–2035 takes its later end.
- verdict: ok. Not yet due.
- notes: the test's "found mainly by AI" and "come into use, as shown by regulators' approvals" are a fair plain reading of "cures" in a passage where AI produces them. Reading "many" as "more than a handful" is a judgement call, and the file states it.

### 2025-kaifulee-ai-wins-more-nobel-prizes-in-two-to-three-years.toml  (lee)  — PASS
- quote: ok. The captions at 20:59–21:09 match word for word.
- date: ok (as above).
- role: ok.
- admission: ok. It is hedged with "likely".
- due: ok. The range 2027–2028 takes its later end.
- verdict: ok. Not yet due. No Nobel Prize in 2025 was for AI work (physics: quantum tunnelling in circuits; chemistry: metal–organic frameworks; medicine: immune tolerance). The 2026 prizes are beyond what this checker knows.
- notes, recommended before the test is frozen: the test says "for a breakthrough made with AI, as the 2024 chemistry prize was". In the same passage, though, he counts both 2024 prizes, Hinton's physics prize (for work on AI itself) as well as Hassabis's chemistry prize, as "two AI scientists made breakthroughs and won Nobel Prize in nonAI areas". To follow his own usage, the test should read "for work done with or on AI, as both 2024 prizes were". As written, the test is narrower than his words. Separately, "more Nobel prizes" is plural, while the test asks for "at least one". That is a defensible plain reading, but it should be said in the notes.

### 2025-kaifulee-apps-rewritten-ai-first-within-two-years.toml  (lee)  — PASS
- quote: ok. The captions at 23:52–24:01 match word for word.
- date: ok (as above).
- role: ok.
- admission: ok.
- due: ok. 2025 + 2 = 2027.
- verdict: ok. "Unfalsifiable" is consistent with the earlier claim it restates (his June 2024 forecast that every app would be rewritten with AI within two years), which is also unfalsifiable.
- notes, wording only: `verdict_why` is shared boilerplate with the other app claims. It speaks of apps "flooded" or that "have exploded", words that are not in this claim. It would read better as "No count or measure exists of how many apps have been 'rewritten' in an AI-first way ...".

### 2026-02-04-kaifulee-agents-explode-in-2026.toml  (lee)  — PASS
- quote: ok. It matches the Fudan text word for word ("（企业级）" is split across lines on the page).
- date: ok. The page says the programme aired on 2026-02-04, and the timestamp in the original video link (ts=1770159600) is the morning of 2026-02-04, Beijing time.
- role: ok. He is introduced as 01.AI's chief executive.
- admission: ok. It is hedged with "可能" (may).
- due: ok. Judged at 2026-12-31.
- verdict: ok. "Unfalsifiable" is reasonable, since an "explosion" names no quantity.
- notes: none.

### 2026-02-04-kaifulee-ai-entertainment-breakthrough-in-2026.toml  (lee)  — PASS
- quote: ok. It matches word for word, as the fifth of his 2026 forecasts.
- date / role: ok.
- admission: ok. It is about AI that generates images, video and sound.
- due: ok. The forecasts are given in answer to "what 2026 means for AI 2.0".
- verdict: ok. "Unfalsifiable" holds.
- notes: none.

### 2026-02-04-kaifulee-ai-for-science-explosive-invention-in-2026.toml  (lee)  — PASS
- quote: ok. It matches word for word, as the second forecast.
- date / role / admission / due: ok.
- verdict: ok. "Unfalsifiable" is reasonable. The "explosive period" is stated flatly, but it has no measure, and the breakthroughs are only "可能" (may).
- notes: none.

### 2026-02-04-kaifulee-few-person-agent-unicorns-emerge-in-2026.toml  (lee)  — PASS
- quote: ok. It matches word for word, as the third forecast.
- date / role / admission: ok.
- due: ok. Judged at 2026-12-31.
- verdict: ok. Not yet due. The test follows his own correction: five or ten people creating a unicorn's value (a company worth a billion US dollars) by managing many agents. The `restates` link to his 2025-10-30 claim (one person, about five years) is right, since this changes both the date and the condition.
- notes: "whose work is done mostly by AI agents" adds a small degree to his "通过管理大量智能体" (by managing large numbers of agents). That is acceptable. The test does not say whether the company must be new in 2026 ("将开始涌现", will begin to emerge). That is worth a line in the notes before 2026-12-31, so the verdict is not argued after the fact.

### 2026-09-04-kaifulee-ai-changes-jobs-in-five-years.toml  (lee)  — PASS
- quote: ok. The captions at 6:22–6:31 match word for word.
- date: ok. The upload date is 2026-09-04.
- role: ok.
- admission: ok under the jobs ruling, which admits forecasts that AI will change jobs (the builder's call g). The context makes it about AI: "because AI workers are becoming better and cheaper, faster" (6:40–6:43). Call g is a reasonable reading, and here it is John's ruling anyway.
- due: ok. 2026 + 5 = 2031.
- verdict: ok. "Unfalsifiable" holds, because "change" and "quite different" have no measure.
- notes: none.

### 2026-09-23-kaifulee-agi-about-two-years.toml  (lee)  — PASS
- quote: ok. The captions at 1:40:35–1:40:46 match word for word.
- date: ok. The upload date is 2026-09-23.
- role: ok.
- admission: ok.
- due: ok. September 2028, judged at 2028-12-31.
- verdict: ok. Not yet due. The test is his own definition from the same answer ("for cognitive tasks when AI can do 90% of the human tasks better than 90% of the people", 1:40:09–1:40:21). Under reading 4 this is a stated comparison, so it can be tested.
- notes: the `restates` field names his October 2025 five-year forecast. A dated claim between the two is missing from the ledger (see the finding at the end). Once it is entered, this file's `restates` should name it.

### 2026-09-23-kaifulee-ai-fakes-sentience-in-five-years.toml  (lee)  — PASS
- quote: ok. The captions at 1:29:43–1:29:54 match word for word ("sensions" is the captions' spelling).
- date / role / admission: ok. It is hedged with "probably".
- due: ok. 2031.
- verdict: ok. Not yet due.
- notes: the test limits "almost all the people" to "the people who use it". He said "almost all the people", which is general. Dropping "who use it" (for example, almost all people in a published test of whether they take it for a feeling being) would follow his words more closely. This is minor, and the claim is not yet due.

### 2026-09-23-kaifulee-blue-collar-displacement-five-to-ten-years.toml  (lee)  — PASS
- quote: ok. The captions at 1:07:19–1:07:27 match word for word. His restatement at 1:11:19–1:11:25 ("there's a little bit more time um so 5 to 10 years") is as described.
- date / role: ok.
- admission: ok under the jobs ruling (call g). It is a forecast that AI will displace physical work, and it is about AI ("AI's ability to overcome the clumsiness of their body and fingers").
- due: ok. Counting from the day said is reasonable: he speaks of cognitive displacement as under way now ("the writing is on the wall"). The range 2031–2036 takes its later end.
- verdict: ok. "Unfalsifiable" holds.
- notes: none.

### 2026-09-23-kaifulee-embodied-agi-five-to-ten-more-years.toml  (lee)  — COULD NOT VERIFY
- quote: the words are in the captions at 1:40:51–1:41:02. But the captions put a speaker-change mark (">>") at 1:40:51, at the very start of "And then of course one could say AGI should also include uh physical robotics and embodied AI. So that adds another 5 to 10 years in my opinion." The next mark is at 1:41:05, before the host's "Last question". So the line may be the host, Gita Wirjawan, speaking, not Lee. These marks are not fully reliable in this file: there are stray ones at 1:38:33–1:38:36 and 1:15:41–1:15:44. "One could argue" at 1:29:20 is Lee's phrasing, which points to him. Captions alone cannot settle this. Someone needs to listen to 1:40:48–1:41:05 before this file goes public. No outside transcript was found (one web search). I did not download the audio, because that goes beyond the caption reading the brief allows.
- date / role: ok, if it is Lee.
- admission: ok, if it is Lee. It is a conditional definition ("one could say AGI should also include ...") followed by his own estimate, not a hypothetical about the future.
- due: ok. September 2028 plus 5 to 10 years gives 2033–2038.
- verdict: not yet due. The test is his own definition extended, which is fine.
- notes: if the host said it, the file must be taken out, and the line in the search-log row for the Endgame captions (row `kaifulee-claims-006`) corrected.

---

## Finding outside the batch: a dated claim in the 2026-02-04 source is neither entered nor logged

The Fudan text of the 2026-02-04 dialogue, section 04 ("AGI之争"), has Lee saying:

> 在未来两到三年内，将出现一个"令人惊艳的AI"，它能够完成人类90%的任务，并且比90%的人类做得更好。我认为这一定会发生。

In English: within the next two to three years an "amazing AI" will appear that can do 90% of human tasks better than 90% of people, and he says this will certainly happen.

This is dated, about AI, not a hypothetical, and testable by his own stated comparison (reading 4). It is the middle link of his chain: about five years (2025-10-02), then two to three years (2026-02-04, due 2029), then maybe two years (2026-09-23).

The search-log row for the Fudan page (row `kaifulee-claims-060`) lists the four claims entered and three lines left out, but not this one. It must be entered, due 2029 with early end 2028, `restates` the 2025-10-02 claim, status not yet due. The 2026-09-23 two-year file's `restates` should then point to it.

The same section's "如果我们能基于AI，在5年内将人类能创造的价值放大100倍" (if, with AI, we can multiply the value humans create a hundredfold within five years) is conditional ("如果", if) and rightly not entered, but it is not logged either. The hardware line "未来数年必将迎来高潮" (AI hardware will peak in the coming several years) is undated. Neither is logged; adding both to row 060's "left out" list would complete the record.

## Builder's own calls touched by this batch
- g (jobs forecasts admitted): applies to the jobs-in-five-years file and the blue-collar file. It is reasonable, and it is also John's ruling in the method.
- The other calls (a to f) are not touched by these files.

## Counts
PASS 13, FAIL 0, COULD NOT VERIFY 1.
- COULD NOT VERIFY: 2026-09-23-kaifulee-embodied-agi-five-to-ten-more-years. A speaker-change mark in the captions means the line may be the host's; someone must listen at 1:40:48–1:41:05.
- Must fix outside the batch: the 2026-02-04 "two to three years, 90% of tasks better than 90% of people, will certainly happen" claim is missing from the ledger and from its search-log row.

## Batch 6

# Batch 2-6 results: second-pass check of claim files (2026-10-19)

Sources opened on 2026-10-19: YouTube automatic captions read with yt-dlp for seven videos (Endgame
#279 with Kai-Fu Lee; Big Technology Podcast 2023-01-25 and 2025-03-19; the third-party upload of
LeCun's Paris talk of February 2025; Sky News's VivaTech 2025 upload; Forbes's Davos upload; the
World Economic Forum's Musk conversation of 2026-01-22), with upload dates from `yt-dlp --print
upload_date`; the Lex Fridman transcript page, the Shaastra interview page, the AI Inside episode
page, the Hugging Face LoRA blog and waxy.org with curl; The Next Web and MIT Technology Review
through the r.jina.ai reader; LeCun's X post through the api.fxtwitter.com mirror. All quotes
below were found at their stated places. The repository was not edited.

### 2026-09-23-kaifulee-kazakhstan-ai-teaching-pisa-in-a-year.toml  (lee)  — PASS
- quote: ok. Captions at 0:53:14 read "others who want to wait a year uh will see the Pisa scores in in a year and I think they will be significantly better." 24 words. The later line at about 0:55:50 ("the AI um teaching assistant product can show improved visa score within one year") is quoted correctly in `prediction`.
- date: ok. Upload date 20260923.
- role: ok. The host introduces him as "founder, CEO and chairman of zero one 01.ai", and just before the quote he says "my company 01.ai ... is currently working with ... a joint venture in the country of Kazakhstan", so the system is 01.AI's. Said after 2023-03-19.
- admission: ok. About what an AI system will do (raise test scores), dated ("within one year"), not a hypothetical, not a business forecast.
- due: ok. "in a year" from 2026-09-23, judged 2027-12-31.
- verdict: ok. Cannot be tested is a fair call: the international test he names (PISA) runs every three years, so no sitting falls a year after the system starts, "significantly better" has no size, and no group of pupils is named. A reader could argue it will simply fail, but no outsider could ever run the test he set, so it is decided at entry, as the method requires.
- notes: none.

### 2026-09-23-kaifulee-no-ai-sentience-for-a-century.toml  (neg, lee)  — PASS
- quote: ok. Captions at 1:30:25 to 1:30:40: "95% confident. um that our definition of our sensions will not likely be uh replicated by AI in the next 100 years." Verbatim.
- date: ok. Upload 20260923.
- role: ok, as above.
- admission: ok. A forecast that something will not happen by a date (reading 2), about AI.
- due: ok. 2126.
- verdict: ok. Reading 2 is applied (a "will not happen" claim), and cannot be tested is right: at 1:39:17 in the same talk he says of sentience and self-awareness "we don't even have a clear scientific definition", so no record of the thing could exist either way. `has_probability = true` for the "95%" is right, so it stays out of the plain count anyway.
- notes: none.

### 2023-01-25-lecun-teenagers-train-image-models-within-two-years.toml  (fails, hits)  — PASS
- first-pass problem: fixed. The test no longer adds "home equipment", "from scratch" or "adapting a released model does not count"; it is built from his words, with "this" read from the sentences around it, and `prediction` no longer borrows "train their own models" from the later, undated sentence (the notes say that sentence is not the claim). This follows the ruling that the test uses the speaker's own words.
- quote: ok. Captions around 59:28: "why should like a large tech company in California profit from my my art ... this is the wrong way to frame this because within a year or two you know any teenager in the parents basement is going to be able to do this ... the big tech company are just the first ones to have the technology to do this". The reading of "this" is fair to the passage.
- date: ok. Upload 20230125.
- role: ok. Meta's Chief AI Scientist.
- admission: ok. About what AI tools will let a person do, dated ("within a year or two"), not a hypothetical.
- due: ok. 2024 to 2025, later end taken.
- verdict: ok. Hugging Face's blog "Using LoRA for Efficient Stable Diffusion Fine-Tuning", "Published January 26, 2023", says "We could create a full fine-tuned model in a 2080 Ti with 11 GB of VRAM!" and its run "took about 5 hours in a 2080 Ti GPU (11 GB of RAM)". waxy.org (Andy Baio, posted 2022-11-01) says a Reddit user fine-tuned Stable Diffusion on 32 of Hollie Mengert's illustrations, about "2.5 hours on a GPU at Vast.ai", for "less than $2". Both meet the test (one person, cheap or home equipment, a model trained on chosen art, used to make images), and the Hugging Face record falls inside the window. `verdict_on` 2023-01-26, `evidence_by` outside and `direction` sooner are right.
- notes: small wording, no count changes: `verdict_why` calls the Hugging Face run "a full further training"; it was a LoRA fine-tune (a light method that trains small added layers; the blog itself uses the words "full fine-tuned model"), on a Pokémon picture set rather than one artist's work. Suggest "fine-tuning with the LoRA method on a chosen set of pictures". The search-log row for the find (lecun-claims-048) still glosses the quote with "('train their own models')", the borrowed words; harmless in the log but worth tidying.

### 2024-03-07-lecun-human-level-at-least-a-decade.toml  (neg)  — PASS
- quote: ok. The transcript at 02:05:37 reads "all of this is going to take at least a decade and probably much more".
- date: ok. Episode of 2024-03-07.
- role: ok. Meta's Chief AI Scientist.
- admission: ok. A forecast that it will not happen within a decade (reading 2).
- due: ok. 2034-03-07, judged at 2034-12-31; the test itself carries the exact date 2034-03-07.
- verdict: ok. `not_yet_due` is right. Reading 4: the same answer (02:04:35 to 02:06:30) describes "AGI or human-level AI or AMI" ability by ability, with "the scale and performance that we observe in humans" and "the way the human brain can", so treating it as having a stated comparison is a reasonable reading. The file flags the judgement call (a reader could take the list as too loose and mark it cannot be tested); I agree it is a call for John, not an error.
- notes: none.

### 2024-04-09-lecun-not-surpass-human-intelligence-next-year.toml  (hits, neg)  — PASS
- quote (`reported_as`): ok. The Next Web, published 2024-04-10T10:10 UTC, "At an event on Tuesday in London", quotes him: "Eventually, machines will surpass human intelligence… it's gonna take a while though ... It's not just around the corner — and it's certainly not next year like our friend Elon has said." Marked coverage only.
- date: ok. Tuesday before 2024-04-10 is 2024-04-09.
- role: ok. Meta's Chief AI Scientist.
- admission: ok. A dated "will not happen" forecast.
- due: ok. Not in 2025, judged 2025-12-31.
- verdict: ok. Scored under reading 2. "Surpass human intelligence" is a comparison, so reading 4 gives a plain test, and the test now uses his own words. No maker or outside body has shown an AI surpassing human intelligence by 2025-12-31; the World Economic Forum upload of 2026-01-22 has Musk at about 30:33 saying "we might have AI that is smarter than any human by the end of this year", which supports that the thing had not happened. Hit, `verdict_on` 2025-12-31, `evidence_by` outside: right.
- notes: none.

### 2024-10-16-lecun-human-level-ai-not-in-next-year-or-two.toml  (neg)  — PASS
- quote: ok. The post (created Wed Oct 16 15:31:08 UTC 2024) ends "In any case, it's not going to be in the next year or two."
- date: ok.
- role: ok.
- admission: ok. A "will not happen" forecast with a date (reading 2).
- due: ok. 2026.
- verdict: ok. The post names "Human-Level AI" and gives no definition or comparison, so reading 4 makes it cannot be tested. Right.
- notes: none.

### 2024-10-lecun-human-level-within-the-decade-if-lucky.toml  (sample)  — PASS
- quote: ok. Shaastra page: "And then, if we are lucky, human-level intelligence within the decade."
- date: ok. The page says the interaction was at IIT Madras "in October 2024"; month only is right.
- role: ok.
- admission: ok. Forward-looking, dated, hedged but not a hypothetical.
- due: ok. 2034 (generous reading of "within the decade"), and `due_basis` says so.
- verdict: ok. "Human-level intelligence" is named, never defined or compared in the interview (I read the whole answer and the one before it), so reading 4 applies.
- notes: none.

### 2025-02-lecun-not-phd-level-intelligence-next-year.toml  (neg)  — PASS
- quote: ok. Captions at about 9:55 to 10:05: "telling us we're going to reach you know PhD level intelligence by next year it's just not happening". The opening introduces him as Meta's chief AI scientist, and the host mentions "Bernard" (Schölkopf), consistent with the Institut Polytechnique de Paris conference.
- date: ok. Upload 20250210; month only is right as the day is not given.
- role: ok.
- admission: ok. His own forecast that a thing will not happen by a date, not a report of others' views.
- due: ok. Not in 2026, judged 2026-12-31 (still ahead).
- verdict: ok, but a judgement call. Treating "PhD level intelligence" as an undefined level like bare "human level" is reasonable: he gives no test, and he himself allows "PhD level in some subfield", so the general thing has no edge. The file flags the other reading (a comparison with people who hold doctorates, which would be scored). This is the kind of call John should see, since reading 4 covers only "human level".
- notes: small: the notes quote him as "just training on text"; the captions read "just turning on text" (likely a mishearing of "training"). Say it is the captions' rendering, or quote the captions.

### 2025-03-19-lecun-human-level-not-within-two-years.toml  (neg)  — PASS
- quote: ok. Captions at 18:39 to 18:45: "it's not going to happen within the next two years there's absolutely no way in hell".
- date: ok. Upload 20250319.
- role: ok.
- admission: ok.
- due: ok. 2027.
- verdict: ok. In the answer (16:00 to 19:30) "human level AI" is named without a definition or comparison of his own; "a country of genius in the data center" is another's phrase he rejects. Reading 4 applied correctly. `restates` the post of 2024-10-16, correct.
- notes: none.

### 2025-04-09-lecun-as-smart-as-humans-not-within-two-years.toml  (neg)  — PASS
- quote: ok. AI Inside transcript: "It's not going to happen next year. It's not going to happen two years from now."
- date: ok. Episode page "April 09, 2025".
- role: ok.
- admission: ok.
- due: ok. 2027-04-09 in the test, judged at 2027-12-31.
- verdict: ok. The same answer defines the thing: "machines that are at least as smart as humans in all the domains where humans are smart", called "human level intelligence if you want", so reading 4 gives a plain test in his words. `not_yet_due` right.
- notes: none.

### 2025-06-11-lecun-cat-level-prototypes-within-five-years.toml  (sample)  — PASS
- quote: ok. Captions at 18:33 to 18:42, verbatim ("understand if he's world" is the captions' rendering of "the world", as the notes say).
- date: ok. Upload 20250611, VivaTech's first day.
- role: ok. Introduced as "chief AI scientist at Meta".
- admission: ok. Conditional ("if all the planets lined up"), not a hypothetical.
- due: ok. 2030.
- verdict: ok. Understanding the world "at the level of a cat or a rat" has no measure an outsider could run, so cannot be tested is right.
- notes: none.

### 2025-06-11-lecun-world-model-applications-within-five-years.toml  (sample)  — PASS
- quote: ok. Captions at 19:15 to 19:22: "we're going to start seeing kind of the most the more tangible applications of this maybe within five years or so".
- date, role, admission: ok.
- due: ok. 2030.
- verdict: ok. `not_yet_due`.
- notes: the test is a fair plain reading but drifts slightly from his words: he says "tangible applications of this", where "this" is the joint embedding predictive architecture (JEPA) approach; the test says "world models of the kind he describes" and adds "products or services in real use (not research demonstrations)". Neither changes any count now. Suggest the test name "this approach (JEPA world models)" and keep "tangible applications" as his words, so the test is not loosened or tightened later.

### 2026-01-22-lecun-human-level-not-next-year-or-two.toml  (neg)  — PASS
- quote: ok. MIT Technology Review (published 2026-01-22T05:00-05:00): "We are going to have AI systems that have humanlike and human-level intelligence, but they're not going to be built on LLMs, and it's not going to happen next year or two years from now."
- date: ok.
- role: flagged, not wrong. In the same interview he says "I am going to be the executive chairman of the company", so the title is sourced (the first pass's request to name the source is met). Whether AMI Labs, a weeks-old company that had not yet released a model, counts as "a company that builds frontier AI models" is a judgement call; the file flags it for the lead. John should rule on it, because it decides all of LeCun's claims after 2025.
- admission: ok.
- due: ok. 2028.
- verdict: ok. "Humanlike and human-level intelligence" is named with no definition or comparison in the interview (I read the whole answer), so reading 4 applies.
- notes: small: `repeated_on` 2026-02-19 is the India summit line about "super intelligent systems within within two years", a different stage from human-level. Both are cannot be tested, so no count changes, but "repeated unchanged" overstates it; a note saying the stage word differs would be more exact.

### 2026-01-lecun-smarter-than-humans-not-within-two-years.toml  (neg)  — FAIL
- quote: ok. Captions at 0:30 to 0:45: "machines that would be smarter than humans at some point. It's not going to happen next year. It's not going to happen in two years".
- date: ok. Forbes upload 20260128; Davos week, month only.
- role: flagged as in the file above (AMI Labs chair).
- admission: ok. A "will not happen" forecast with a named comparison (reading 4 gives a plain test).
- due: ok. 2028.
- verdict: status `not_yet_due` is right, but the test is not in his words. It reads "smarter than humans at thinking work across the board". He said only "machines that would be smarter than humans"; "at thinking work across the board" is the gloss the method uses for Musk's "smarter than the smartest human", and it narrows the thing to thinking work, when in this talk he ties intelligence to understanding the physical world. The same gloss was removed from the London file (2024-04-09-lecun-not-surpass-human-intelligence-next-year) for exactly this reason before merging, so this file is left inconsistent. What must change: rewrite `bar` in his words, e.g. "the claim holds if no AI is shown, by its maker or an outside body, to be smarter than humans before the end of January 2028", before publishing, since the test cannot be changed later without a dated note.
- notes: the repeat at Brown University on 2026-04-01 was not checked here.

## The agent's own unruled calls touching this batch

- None of the seven listed calls (a to g) is applied in these files. The nearest judgement calls are
  the builder's reading of "PhD level intelligence" as a named level like "human level" (the
  PhD-level file), the reading of the ability list in the Lex Fridman answer as a stated
  comparison (the at-least-a-decade file), and treating AMI Labs as a qualifying company (the two
  2026 files). All three are reasonable and all are flagged in the files; each wants John's ruling.

## A pattern worth noting (no file fails on it)

For a forecast that something will not happen within a span ("not within two years" from
2025-04-09), the span rule judges the claim at the end of the year, 2027-12-31, while the stated
date is 2027-04-09. For a positive claim that rounding is generous; for a "will not happen" claim
it is the harsh direction, because a thing arriving between April and December would count
against him. The files avoid this by putting the exact date in the test ("before 2027-04-09",
"before 2034-03-07", "before the end of January 2028"), which is right under reading 2 ("scored
at the stated date"). Setting `due_date` to the stated date on these files would make the page's
"due" count match the test.

## Counts

PASS 13, FAIL 1, COULD NOT VERIFY 0.

- FAIL: 2026-01-lecun-smarter-than-humans-not-within-two-years: the test adds "at thinking work across the board" to his "smarter than humans", the same added gloss already removed from the London file; rewrite the test in his words.

## Batch 7

# Second-pass check, batch 2-7 (14 claim files), 2026-10-19

Sources opened this pass: YouTube captions through yt-dlp (7 videos, in `dl2-7-yt/` and `dl2-7-yt2/`), pages through curl (in `dl2-7-web/`), Microsoft transcript Word files through textutil, the two Build transcript PDFs through PDFKit. Nothing in the repository was edited. All `search_ids` in all 14 files exist in `data/search_log.csv`; the `restates` target of the LeCun file exists.

None of the builder's seven unruled calls (a to g) is used by any file in this batch, so I have no judgement to give on them from these files.

### 2026-04-01-lecun-not-human-level-within-five-years  (neg)  — PASS
- quote: ok. Captions 24:33 to 24:44: "at the very best, we might be convinced that we're on a good path towards human level intelligence, but not yet at human intelligence within five years". The quote is a verbatim run of these words.
- date: ok. Brown's news page is dated 2026-04-01 and says the talk was "on Wednesday, April 1"; the upload is dated 2026-04-02.
- role: doubtful, already flagged in the file. Brown's page calls him "executive chairman of the AI startup AMI Labs". Whether a new world-model lab counts as "a company that builds frontier AI models" is a judgement John has not ruled on. It is the same judgement as in the January 2026 LeCun claim, so the two files agree.
- admission: ok. This is a forecast that something will not happen by a date, so it is admitted under reading 2. Reading 4 is handled correctly: the same passage gives a comparison, "machines will eventually surpass humans in all domains where humans are intelligent" (24:08), so the test does not rest on bare "human level".
- due: ok. Five years from 2026-04-01 is 2031-04-01, judged at 2031-12-31 under the span rule.
- verdict: not yet due; ok.
- notes: The test (`bar`) quotes his "surpass humans in all domains" but then tests for reaching "human level across all those domains". That is the right thing to test, because the claim is "not yet at human intelligence", but the wording could say so. The test's cut-off (before 2031-04-01) and the judging date (2031-12-31) differ; the file is consistent with itself, and no count is affected. The caption also has "it is going to happen next year" (24:19), a mis-hearing between two "not going to happen" lines; nothing rests on it.

### 2011-06-17-legg-ten-percent-by-2018  (sample)  — PASS
- quote: ok. The greaterwrong copy of the LessWrong post reads "Shane Legg: 2018, 2028, 2050" in answer to Q1. The date line reads "17 Jun 2011 8:58 UTC".
- date: ok.
- role: doubtful, already flagged in the file. He co-founded DeepMind (2010) and was answering as a researcher; the post never names DeepMind.
- admission: ok. It is dated and stated as a chance (`has_probability`), so it is out of the plain count.
- due: ok (2018).
- verdict: ok, cannot be tested. Q1 asks about "human-level machine intelligence" with no comparison. His Q3 answer says "'human level' is a rather vague term". The Q8 milestone (learning a wide range of games) is a sign he would look for, not a definition. Reading 4 applies correctly.
- notes: The record of the change from "missed" is clear.

### 2011-12-31-legg-proto-agi-within-eight-years  (fails)  — PASS
- first-pass problem: fixed. (1) The misreading of "might be impossible to falsify" is gone. The notes now give his actual reason (a military might keep such a system secret), which matches his comment of 2 January 2012 on the page. (2) The claim is now tested against the definition the post itself gives, as the method's rule on tests requires. That moves one claim from "cannot be tested" to "missed". This is the builder applying the method, not a ruling by John; the lead may want John to see the change.
- quote: ok. "I expect to see an impressive proto-AGI within the next 8 years." The definition that follows is quoted verbatim in the test. The page reads "Posted on 31 December, 2011".
- date: ok.
- role: doubtful, already flagged in the file (as for the other 2011 claim).
- admission: ok.
- due: ok (2019-12-31).
- verdict: missed is sound on the test as written. No single learnt system with vision, sound processing, movement control and language had been shown by the end of 2019. Gato (arXiv 2205.06175, first version 2022-05-12) has vision, language and movement control but no sound. `evidence_by = maker` and `direction = not_come` are honest.
- notes (minor, no count changes):
  - `verdict_why` says the Gato paper "presents as new" a single generalist network. The abstract only says "we apply a similar approach towards building a single generalist agent". It makes no claim to be first, so "presents as new" overstates it slightly.
  - `verdict_on` is Gato's date, 2022-05-12, though the miss is a miss at 2019-12-31, and Gato is only indirect evidence about 2019. Other misses that rest on nothing being found use the due date (the YouTube auto-chapters record uses 2023-12-31). I suggest `verdict_on = 2019-12-31` for consistency.

### 2023-10-17-legg-agi-not-next-year-or-year-after  (fails, hits, neg)  — PASS
- first-pass problem: fixed. Whether a "not by" claim is admitted is now settled by John's reading 2, and the file cites it.
- quote: ok. Verbatim in the TED transcript (ted.com, curl): "I don't think it's coming next year or the year after. It's probably a little bit further out than that." It comes just before Chris Anderson's "2028?". The page data has recordedOn 2023-10-17 and publishedAt 2023-12-07.
- date: ok.
- role: ok as flagged. Co-founder and chief AGI scientist of Google DeepMind; the founder-leader reading is a judgement for John.
- admission: ok under reading 2. Reading 4 does not bite: his definition in the same talk ("a system that can do all the cognitive kinds of tasks that people can do ... at least ... the sorts of cognitive tasks that people can typically do") gives a plain test, and the test uses it.
- due: ok (2025-12-31).
- verdict: ok. In his podcast (upload 2025-12-11, video l3u_FAv33G0) at 1:55 he defines minimal AGI the same way. At 7:03 he says "we're not there yet, but it could be one year". No public record shows such a system by 2025-12-31. `verdict_on` 2025-12-31 suits a "not by" claim. `evidence_by = maker` is honest.
- notes: none.

### 2024-05-22-mensch-robots-human-speed-within-five-years  (sample)  — PASS
- quote: ok. French auto-captions 1:11:18 to 1:11:25: "d'ici 5 ans euh on va pouvoir enfin même avant que ça avant ça largement mettre des modèles Mistral ou des modèles de concurrents", then "dans des robots qui euh se déplacent à vitesse humaine qui ont une dextérité qui proche de celle d'un humain". This matches the quote and the French in `prediction`. In the context he speaks for Mistral ("nous c'est pas vraiment notre sujet").
- date: ok (upload dated 2024-05-22).
- role: ok (co-founder and chief executive of Mistral AI).
- admission: ok. It is a capability claim about AI models in robots, with a span.
- due: ok (2029).
- verdict: not yet due; ok.
- notes (minor): The test adds two words he did not say. "Language-based" AI model: he said "Mistral's models or competitors' models", which in context means the same thing, but the word is added. "Human walking speed": he said "se déplacent à vitesse humaine", which is move at human speed. The method says the test adds no condition the speaker did not state, so I suggest "an AI model of Mistral's or a competitor's" and "moving at human speed".

### 2021-08-19-musk-tesla-bot-prototype-next-year  (fails, hits)  — PASS
- first-pass problem: fixed. The role note is now there (Tesla's chief executive, under John's ruling on Tesla), and the test now carries an AI condition taken from his own words in the same talk.
- quote: ok. Captions 2:07:48 to 2:07:57: "we think we'll probably have a prototype sometime next year that basically looks like this". The AI words in the test are verbatim in the same passage: 2:07:24 to 2:07:39 ("full self-driving computer ... neural nets recognizing the world understanding how to navigate through the world ... it kind of makes sense to put that onto a humanoid form") and 2:09:01 to 2:09:17 ("got the autopilot system in it ... cameras ... full-size driving computer and making use of all of the same tools that we use in the car").
- date: ok (live stream 2021-08-19, Pacific time).
- role: ok under John's ruling of 2026-10-19.
- admission: ok now that the test makes the robot an AI system.
- due: ok (2022).
- verdict: ok. AI Day 2022 captions (upload 2022-10-01 in universal time, event 2022-09-30): 17:03 "the first time we try this robot without any backup support"; 18:23 "essentially the same self-driving computer that runs in your Tesla cars"; 19:52 "the autopilot neuronet networks running as is just retrained for the bot"; 21:01 Bumble C; 21:16 to 21:37, the Optimus with Tesla's own actuators, "fairly close to what will go into production". Every condition was met by the date. `evidence_by = maker` is honest.
- notes: The test was rewritten after the verdict was known, but the rewrite only adds conditions in his own words (it makes the test harder), so it was not shaped to fit the verdict.

### 2024-07-01-musk-grok-2-in-august  (fails, hits)  — PASS
- first-pass problem: partly fixed. The role note was added. `when` still says 2024-07-01, not 2024-06-30. The `when_note` now says plainly that he said it on 2024-06-30 in his own time, and gives the reason: the validator (`scripts/validate.py`, lines 654-655) requires the date in the file name to equal `when`, and files are never renamed. I confirmed the validator does this. The conflict is between two of the ledger's own rules, not a mistake in the file. No count or due date changes. The lead or John should decide whether the validator should allow `when` to differ from the name when `when_note` explains it.
- quote: ok. The fxtwitter mirror returns "@beffjezos Sadly quite true. ... Grok 2, which comes out in August, will be a giant improvement in this regard.", created Mon Jul 01 04:47:22 +0000 2024, in reply to beffjezos.
- date: see above.
- role: ok (founder and head of xAI).
- admission: ok.
- due: ok (`due_date` 2024-08-31).
- verdict: ok. x.ai/news/grok-2 reads "Aug 13, 2024 Grok-2 Beta Release ... We are excited to release an early preview of Grok-2". `evidence_by = maker`.
- notes: none.

### 2023-07-25-nadella-security-copilot-early-access-this-fall  (fails, hits)  — PASS
- first-pass problem: fixed. All four requested changes are made: Microsoft's own post is the record, `verdict_on` is 2023-10-19, `evidence_by` is `maker`, and "paid" is in the test with a source.
- quote: ok. The transcript, in Satya Nadella's prepared remarks (headed "Tuesday, July 25, 2023"), reads "Finally, our Security Copilot – the first product to apply this next generation of AI to SecOps – will be available to customers via a paid early access program this fall." The ellipsis is described correctly.
- date: ok.
- role: ok.
- admission: ok.
- due: ok. The end of autumn, 2023-12-21, is a judgement, but a harmless one.
- verdict: ok. Microsoft's post (published 2023-10-19, per the page metadata) has "Today as we announce our Early Access Program is now open to qualified customers"; the word "paid" does not appear on that page. "Paid" rests on Directions on Microsoft: "Security Copilot has been in paid, private testing via Microsoft's Early Access Program since October 2023." I confirmed that on the page. Its metadata date is 2025-01-16, but the text says "At release next month", so it was written in March 2024.
- notes: `evidence_by = maker` is the cautious choice, since the "paid" part comes from an outside firm. The verdict text says so.

### 2023-10-nadella-m365-copilot-generally-available-this-year  (fails, hits)  — PASS
- first-pass problem: partly fixed. `when_note` now gives the signature date correctly, but `when` stays "2023-10" instead of 2023-10-16. The reason is the same rule clash as the Grok 2 record (the validator requires the name's date to equal `when`). That `when` is less precise than it could be, but it is not wrong, and nothing else changes.
- quote: ok. Verbatim in the 2023 annual report letter (microsoft.com, curl): "Just last month, I was excited to announce that we will make Microsoft 365 Copilot generally available to our commercial customers later this year." The signature reads "Satya Nadella Chairman and Chief Executive Officer October 16, 2023".
- date: ok, apart from the precision point above.
- role: ok.
- admission: ok. It was a forecast made only about two weeks ahead, of a date Microsoft had already announced, but it still meets the rule.
- due: ok (2023).
- verdict: ok. Microsoft's post of 2023-11-15 reads "On November 1, 2023, Copilot for Microsoft 365 became generally available for enterprises". `verdict_on` 2023-11-01 is right.
- notes: none.

### 2024-01-30-nadella-ai-first-class-part-of-every-pc  (sample)  — PASS
- quote: ok. In the FY24 Q2 transcript, inside SATYA NADELLA's remarks (dated "Tuesday, January 30, 2024"): "In 2024, AI will become a first class part of every PC." The next sentence is about PCs with built-in neural processing units at CES, as the notes say.
- date: ok.
- role: ok.
- admission: ok, though close to the line: it is close to a hardware forecast, and "borderline cases stay out" could also be applied. Either way it is out of the rate.
- due: ok (2024).
- verdict: ok. "A first class part" has no measure, so the claim cannot be tested.
- notes: none.

### 2024-05-21-nadella-team-copilot-preview-later-this-year  (hits)  — PASS
- quote: ok. Page 14 of the Build 2024 transcript ("Tuesday, May 21, 2024"), Satya Nadella speaking: "These capabilities will all come to you all and be available in preview later this year." Just before it he names three roles: meeting facilitator, collaborator and project manager.
- date: ok.
- role: ok.
- admission: ok.
- due: ok (2024).
- verdict: ok, with a judgement already flagged in the notes. The Ignite 2024 Book of News (news.microsoft.com, curl) has "Facilitator agent ... works within Teams meetings and chats ... In chats, the Facilitator shares a summary of important information ... This agent is in preview" and "Project Manager agent ... in Planner ... This agent is in preview."
- notes: Two points, minor. (1) He listed tasks under each role: for the facilitator, "creating agendas, tracking time, taking notes"; for the collaborator, "writing chats ... tracking action items, addressing unresolved issues". The Book of News shows only note-taking and chat summaries. The test names the roles, not every task, so the hit stands on the test as written, but a reader might call it a partial delivery. (2) He also said it would work "in Loop". The test leaves that out; it is a place he named rather than a capability, so leaving it out is defensible.

### 2025-05-19-nadella-sora-on-azure-next-week  (hits)  — PASS
- quote: ok. Page 9 of the Build 2025 transcript ("Monday, May 19, 2025"), SATYA NADELLA: "giving same-day access when a new model drops and Sora is coming next week."
- date: ok.
- role: ok.
- admission: ok.
- due: ok (`due_date` 2025-06-01).
- verdict: ok. The devblogs post "Go from prompt to playback with Sora ... in Azure AI Foundry" is dated May 29th, 2025 (datePublished 2025-05-29T20:38Z) and introduces Sora in the Foundry video playground. That falls inside the following week. `evidence_by = maker`.
- notes: none.

### 2022-05-11-pichai-youtube-auto-chapters-80-million-goal  (fails)  — PASS
- first-pass problem: fixed. The quote now restores "auto generated chapters" and is verbatim. The locator runs to 00:11:42. `verdict_why` now says plainly that the June 2023 figure fits either outcome, and that "has not come" means only that no record shows it came.
- quote: ok. Official en-US captions, 00:11:33 to 00:11:42: "With this, we now have a goal to 10x the number of videos with auto generated chapters from eight million today to 80 million over the next year." The words fall in Pichai's segment, which runs from 2:01 until "Thanks, Sundar" at 15:55.
- date: ok (upload 20220511).
- role: ok.
- admission: ok, and `is_goal` is right.
- due: ok (2023).
- verdict: ok on the test as written. DeepMind's post of June 16, 2023 says chapters have been applied to "tens of millions of videos (and counting)". My own web search found no later count. With no dated record of 80 million, "missed" follows the method, which has no "unknown" status.
- notes: `direction = not_come` stays, with the caveat now written into the verdict. That is acceptable. The page should show `verdict_why` beside the claim, so the caveat is seen.

### 2023-05-10-pichai-magic-editor-later-this-year  (hits)  — PASS
- quote: ok. Captions 00:09:19 to 00:09:24: "We are excited to roll out Magic Editor in Google Photos later this year." This is inside Pichai's segment (from 2:00 until "SISSIE HSIAO: Thanks, Sundar" at 18:01).
- date: ok (upload 20230510).
- role: ok.
- admission: ok.
- due: ok (2023).
- verdict: ok. The Google post of 2024-04-10 (published_time 2024-04-10) reads "Last year, we launched Magic Editor on Pixel 8 and Pixel 8 Pro." The Pixel 8 went on sale 2023-10-12, as the 2023-10-04 post the file cites says. `evidence_by = maker`.
- notes: The first-pass source fix (pointing at the post that records the launch) is done.

## Summary

PASS 14, FAIL 0, COULD NOT VERIFY 0.

Not FAILs, but worth the lead's attention:
- Two records keep a `when` that is less precise than it could be (the Microsoft 365 Copilot letter) or a day off under the speaker's-own-time rule (Grok 2). In both, the validator's rule that the name's date must equal `when` blocks the fix the first pass asked for. That is a rule question for the lead or John.
- The proto-AGI record moved from "cannot be tested" to "missed" by the builder applying the method's rule on tests. Its `verdict_on` would be more consistent as 2019-12-31, and "presents as new" slightly overstates what the Gato abstract says.
- In the Mensch robots record, the test adds "language-based" and "walking", which he did not say.
- LeCun's chair role at AMI Labs still needs John's ruling on whether AMI Labs counts as a company building frontier AI models.

## Batch 8

# Second-pass results, batch 2-8 (Sundar Pichai, 14 claim files), checked 2026-10-19

Sources opened on 2026-10-19, all saved under `dl2-8-*` in the scratchpad:
- Captions (yt-dlp) and upload dates for four videos: I/O 2024 (20240514), DealBook 2024 (20241206), I/O 2025 (20250520) and I/O 2026 (20260519). The I/O 2024 and 2026 caption tracks, and the I/O 2025 described-audio track, carry "SUNDAR PICHAI:" speaker labels.
- Alphabet's official call transcripts as PDFs, read as text: the third quarter of 2023 and the first quarter of 2025.
- Pichai's posted earnings remarks: the fourth quarter of 2024 and the first, second and third quarters of 2025, plus the first quarter of 2026.
- Every `verdict_source`.
- Other pages: Google's posts of 2024-02-08, 2024-05-14 and 2024-12-11 on Gemini models; the AI Mode post of 2025-05-20; Google's I/O 2025 recap and quiz pages (2025-05-21 and 2025-05-22); the Gemini 2.5 family post of 2025-06-17; Google's support thread on moving Assistant users to Gemini; YouTube's post of 2026-10-12; and the Lex Fridman transcript page.

### 2023-10-24-pichai-gemini-models-throughout-2024.toml  (fails, hits)  — PASS
- quote: ok. Verbatim on page 12 of the official transcript, in Pichai's labelled answer: "laying the foundation of what I think of as the next-generation series of models we'll be launching all throughout 2024."
- date: ok (2023-10-24).
- role: ok.
- admission: ok. It looks forward, it is about AI models, and it is dated.
- due: ok (2024).
- verdict: ok. `verdict_source` is now Google's post of 2024-02-08 ("Today we're launching Gemini Advanced ... access to Ultra 1.0", "available today in more than 150 countries"). The second public release is the post of 2024-05-14, logged in the search log (row `pichai-claims-065`): "introducing 1.5 Flash", "available today in more than 200 countries and territories in preview", and "Give 1.5 Pro and 1.5 Flash a try in Google AI Studio today". The bar of more than one public release in 2024 was met on 2024-05-14, so `verdict_on` is right. Gemini 2.0 Flash on 2024-12-11 ("available to all Gemini users") is a third.
- first-pass problem: fixed. There is now a primary record for a second public release, the 1.5 Pro wording is corrected (a limited preview, not counted), and `verdict_on` is the date the bar was first met.
- notes: 1.5 Flash in May was a public "preview" for developers. That differs from 1.5 Pro's waitlisted February preview, so counting the one and not the other holds up. A leftover: the search-log row for the December 2024 post (`pichai-claims-042`) still says "Gemini 1.0 Ultra and 1.5 Pro released in February 2024". That is the old wrong framing, and it is worth correcting if the log is published.

### 2024-05-14-pichai-ai-overviews-us-this-week.toml  (hits)  — PASS
- quote: ok. Verbatim in the captions at 00:05:35 to 00:05:42, inside Pichai's labelled segment (he is labelled at caption line 83, and no other speaker is labelled before line 662).
- date: ok.
- role: ok.
- admission: ok. It is a same-week launch, close to trivial but admissible.
- due: ok (2024-05-19).
- verdict: ok. Liz Reid's post of 2024-05-14 says "today, AI Overviews will begin rolling out to everyone in the U.S." The claim was only to begin the launch, and the maker's launch-day post is the record of that.
- notes: Consistency with the Gemini 2.5 in Search miss below. Both rest on a maker's same-day post. This one says "today ... will begin rolling out", while that one says "Starting this week, we're bringing ...". Scoring this one a hit and that one a miss is defensible, because only this post dates the start to the day itself, but the line is thin. The page should say why the two differ.

### 2024-05-14-pichai-ask-photos-this-summer.toml  (hits)  — PASS
- quote: ok. Verbatim in the captions at 00:07:37 to 00:07:40, in Pichai's segment.
- date: ok.
- role: ok.
- admission: ok.
- due: ok under the equinox reading (2024-09-22).
- verdict: ok. Google Photos' post dated Sep 05, 2024 says "early access to Ask Photos is rolling out to select U.S. users". "We're rolling out" promises a start, so a start for some users meets it.
- notes: This hit depends on reading "summer" as ending at the September equinox. If summer ended on 31 August, this would be a miss, and so would Docs Live. The ledger applies the reading the same way to the summer misses (computer use through the Gemini API, personalised smart replies), so it is not chosen by outcome. Still, it is not in the method, and it decides two hits. It should be written into the method, or ruled by John, before publishing.

### 2024-12-04-pichai-progress-harder-in-2025.toml  (sample)  — PASS
- quote: ok. Verbatim in the automatic captions ("think the progress is going to get / harder when I look at 25 the lwh hanging / fruit is gone"). The upload is dated 20241206, and the event was 2024-12-04.
- date: ok.
- role: ok.
- admission: ok. It looks forward, it is about AI progress, and it names 2025.
- due: ok (2025).
- verdict: ok. "Cannot be tested" fits, because the words name no measure of progress.
- notes: none.

### 2024-12-04-pichai-waymo-ten-us-cities-next-year.toml  (sample)  — PASS
- quote: ok. It is a verbatim run of the captions ("I think in the US / by next year we'll be in like 10 cities / robustly right and like in 10 of the / major market").
- date: ok.
- role: ok. Waymo belongs to Alphabet.
- admission: ok. Driverless-car deployment is the method's own example of a deployment claim.
- due: ok (2025).
- verdict: ok. Pichai's remarks of Apr 29, 2026 say "six new cities so far in 2026, and operations in 11 major U.S. cities in total". That leaves five at the end of 2025, against "like 10", so it was missed and came later.
- notes: In the same answer he says "we are in six to seven cities already by the end of this year" (2024). So his loose "in N cities" counted places where Waymo was testing or had announced service. The bar's "driverless ride service" rests on his "robustly" and "major market[s]", which is a fair reading, and the notes could say so. Under the loose usage the 2025 count would be higher, but nothing he said in the same source supports that reading.

### 2025-02-04-pichai-mariner-astra-features-gemini-app.toml  (hits)  — PASS
- quote: ok. Verbatim in the remarks dated Feb 04, 2025: "We expect to bring features from both to the Gemini app later this year."
- date: ok.
- role: ok.
- admission: ok.
- due: ok (2025).
- verdict: ok. The I/O 2025 remarks (2025-05-20) say "Gemini Live now incorporates Project Astra's camera and screen-sharing capabilities ... already available to all Android users". The first-quarter 2025 remarks of 2025-04-24 already say this was rolling out to all Android devices. The post of 2025-11-18 says Gemini Agent is "Built on insights from Project Mariner", rolling out to Google AI Ultra members first. Both halves came in 2025, and `verdict_on` 2025-11-18 is the date the second one landed.
- notes: The judgement call that "built on insights from Mariner" counts as a Mariner feature is named in the notes. It is fair.

### 2025-02-04-pichai-waymo-austin-atlanta-2025.toml  (hits)  — PASS
- quote: ok. Verbatim in the fourth-quarter 2024 remarks.
- date: ok.
- role: ok.
- admission: ok.
- due: ok (2025).
- verdict: ok. Austin opened on Uber on 2025-03-04 and Atlanta on 2025-06-24. The second-quarter 2025 remarks of 2025-07-23 say "Last month, Waymo launched in Atlanta". The exact days come from press reports, which matches what is generally known.
- notes: On the call of 2025-04-24, Pichai's own answer to an analyst (official transcript, page 19) says "We look forward to offering the first paid rides in Atlanta, via Uber, later this year." That is an unchanged repeat of this claim, so 2025-04-24 belongs in `repeated_on`. The note says the repeat date was removed, and it should be restored on the strength of that answer. This changes no count. See also the next file.

### 2025-04-24-pichai-gemini-tablets-cars-headphones-watches.toml  (sample)  — PASS
- quote: ok. Verbatim in the remarks dated Apr 24, 2025.
- date: ok.
- role: ok.
- admission: ok. Replacing Assistant with Gemini is a deployment of an AI system.
- due: ok (2025).
- verdict: ok. Google's support thread says: "our plans to upgrade the Assistant experience to Gemini on most mobile devices by the end of 2025. We're adjusting our previously announced timeline ... into 2026." Its later update sets Sept. 4th, 2026, with paired watches, headphones and cars following. Missed, came later, on the maker's word.
- notes: The bar's line "a start on some devices ... is not the upgrade" is a reading of "we'll upgrade" (a finished change), set against "rolling out" (a start) in the Ask Photos and Docs Live files. That is consistent. I did not re-confirm the partial-start dates (Wear OS on 2025-07-09, Android Auto on 2025-11-20) at a primary source, and they do not change the verdict. The support thread as read carries no visible post date. The file's date of December 2025 rests on Thurrott's report of 2025-12-20.

### 2025-04-24-pichai-waymo-atlanta-later-this-summer.toml  (hits)  — FAIL
- quote: ok. Verbatim in the posted remarks and in the official transcript (page 18): "Through our partnership with Uber, we expanded in Austin and are preparing for our public launch in Atlanta later this summer."
- date: ok.
- role: ok.
- admission: problem. This is the builder's call (f), and it is not a clear changed repeat. In the same call, answering an analyst a few minutes later, Pichai said: "We look forward to offering the first paid rides in Atlanta, via Uber, later this year" (official transcript, page 19). The builder's own search log (row `pichai-claims-026`) records that line as "a repeat of the Atlanta claim". So on the same day he gave both "later this summer" and "later this year". The record cites only the narrower wording and does not mention the other. Also, the restatement rule speaks of a "new due year or changed condition". This narrowing keeps the same due year, and the same call restates the original span. As it stands, one launch (Atlanta, 2025-06-24) is scored as two hits.
- due: ok if admitted (2025-09-22, equinox reading).
- verdict: ok if admitted. Atlanta opened on 2025-06-24, which is inside the summer.
- notes: Change before publishing. Either take the record out as borderline (logged in the search log) and list 2025-04-24 in `repeated_on` of the February record, or keep it only after John rules, with the page-19 answer quoted in its notes. My judgement of call (f): not a reasonable reading as entered, because the same source's other wording is left out.

### 2025-05-20-pichai-gemini-25-to-search-this-week.toml  (fails)  — PASS
- quote: ok. In the automatic captions at 00:47:41 to 00:47:49 ("And starting this week, Gemini 2.5, our most intelligent model series, is coming to search."). The labelled track marks the speaker as SUNDAR PICHAI, just before "here's Liz".
- date: ok (upload 20250520).
- role: ok.
- admission: ok.
- due: ok (2025-05-25).
- verdict: ok under the rule. I found no dated record that Gemini 2.5 was running in Search during that week. Google's own pages from that week stay in the future tense: the AI Mode post of 2025-05-20, the recap of 2025-05-21 ("starting this week, Gemini 2.5 is coming to Search") and the quiz of 2025-05-22 ("starting this week, we're bringing a custom version of Gemini 2.5"). The post of Jun 17, 2025 says "We've also brought custom versions of 2.5 Flash-Lite and Flash to Search", and Pichai's remarks of 2025-07-23 say "AI Overviews are now powered by Gemini 2.5". So it is missed, came later, on the maker's word.
- first-pass problem: fixed. `direction` is `later`, `evidence_by` is `maker`, the record is now Google's own post, and the Gigazine report on Gemini 2.5 Pro is gone.
- notes: This is a miss for want of a record. The `verify` field says so honestly. The thing may well have arrived within the week. See the consistency note under the AI Overviews file.

### 2025-06-05-pichai-agi-slightly-after-2030.toml  (neg)  — PASS
- quote: ok. Verbatim on the transcript page (posted June 5, 2025) at 00:41:24: "I don't think we'll quite get there by 2030, so my sense is it's slightly after that".
- date: ok.
- role: ok.
- admission: ok.
- due: ok. 2031 as the earliest year it could be judged is fair for "slightly after" 2030. Because the claim cannot be tested, the due year only sets when it counts among the due.
- verdict: ok. The "not by 2030" half is a forecast that something will not happen by a date (reading 2), and the notes record that. The thing it names, AGI, is never defined by him: "we constantly move the line of what it means to be AGI", "it doesn't matter what that definition is". He even frames it as "Will the AI think it has reached AGI". So it cannot be tested, and that follows the rule for an undefined named stage. The words contain no "human level", so reading 4 does not arise. Keeping both halves in one record is reasonable, since they are one sentence about one undefined thing.
- notes: none.

### 2025-10-29-pichai-gemini-3-later-this-year.toml  (hits)  — PASS
- quote: ok. Verbatim in the remarks dated Oct 29, 2025.
- date: ok.
- role: ok.
- admission: ok.
- due: ok (2025).
- verdict: ok. The post of Nov 18, 2025 says "releasing Gemini 3 Pro in preview and making it available today across a suite of Google products".
- notes: none.

### 2026-05-19-pichai-ask-youtube-broadly-us-this-summer.toml  (hits)  — PASS
- quote: ok. The labelled caption track at 00:08:44 to 00:08:52 reads "We are starting to test ask YouTube now / and it will roll out broadly in the US this summer". It sits in Pichai's segment, between his label at line 101 and Demis Hassabis's at line 1109.
- date: ok.
- role: ok.
- admission: ok.
- due: ok under the equinox reading (2026-09-22). The verdict does not depend on that reading.
- verdict: ok. Social Media Today, Published July 7, 2026, quotes YouTube: "finally available for all signed-in users in the U.S. aged 13 and older" on desktop. YouTube's own post of Oct 12, 2026 confirms "we launched Ask YouTube on search" and adds mobile. `evidence_by` is `maker`, which is honest.
- notes: The dated record is a trade report quoting the maker, not the maker's own dated page. YouTube's support thread could not be read (my direct fetch also returned only page furniture). That is acceptable but weaker than the method's "primary record", and the file says so. The TV line is now consistent with YouTube's post ("Earlier this year").

### 2026-05-19-pichai-docs-live-this-summer.toml  (hits)  — PASS
- quote: ok. Verbatim in the captions at 00:11:03 to 00:11:09 ("... will come to Gmail and Google Keep then too"), in Pichai's labelled segment.
- date: ok.
- role: ok.
- admission: ok.
- due: the equinox reading (2026-09-22) decides this hit. Google's post is dated Sep 03, 2026, which is after 31 August.
- verdict: ok under that reading. The post of Sep 03, 2026 says the features are "rolling out this week ... available in Gmail and Keep for Google AI Plus, Pro, and Ultra subscribers, and in Docs for Pro and Ultra subscribers".
- notes: Two points.
  - Small wording error in `verdict_why`: it says "Docs Live and Keep Live for Pro and Ultra". In fact Docs Live is for Pro and Ultra, while Gmail Live and Keep Live are for Plus, Pro and Ultra.
  - `checked_how` says the captions do not name speakers. The labelled track does name them (SUNDAR PICHAI at caption line 101). It is worth correcting, since the labels make the speaker certain.
  - As under Ask Photos, the summer reading should be ruled or written into the method before publishing.

## The builder's unruled calls that these files touch
- (f) The Atlanta "later this summer" record: not a reasonable reading as entered. The same call has Pichai saying "later this year" for the same launch, so this is at best borderline and it scores one launch twice. See the FAIL above.
- (a) "Coming months" taken as undated: these files touch it only through search-log row `pichai-claims-026`, where "'soon' and 'coming months' lines" are left out as undated. That is a reasonable extension of reading 3.
- The "summer ends at the September equinox" reading is not on the list of seven calls, but it decides two hits here (Ask Photos, Docs Live). It is applied evenly to the summer misses as well, so it is not chosen by outcome, but it is not in the method.
- (b), (c), (d), (e) and (g) do not arise in these files.

## Counts
PASS 13, FAIL 1, COULD NOT VERIFY 0.
- FAIL: `2025-04-24-pichai-waymo-atlanta-later-this-summer` (the Atlanta "later this summer" record). In the same call, Pichai's answer to an analyst says "first paid rides in Atlanta, via Uber, later this year", so the call did not clearly narrow the date. As entered, one launch gives two hits. Take it out as borderline (and list 2025-04-24 as a repeat on the February record), or put it to John with that line in its notes.

## Batch 9

# Second-pass results, batch 2-9 (Mustafa Suleyman, 14 claim files), checked 2026-10-19

Sources opened for this pass. I re-downloaded the captions of all 11 YouTube uploads with yt-dlp into `dl2-9-<id>/`, read their upload dates with yt-dlp (all 11 match `when` or `when_note`), and read them as timestamped text in `tools2-9/`. I also fetched these with curl: Communications Today (datePublished 2024-02-21T01:55:17Z), the BBC media centre page (published 22 October 2025), the GPT-5 system card PDF (page 13, Figure 1), OpenAI's release notes (through the r.jina.ai reader copy; help.openai.com itself refuses scripted readers), and the Internet Archive copies of Microsoft's Copilot post of 2025-10-23 and the Windows Experience Blog post of 2025-10-16. Google's Gemini post of 2024-08-13 was read with WebFetch.

Role, for all 14: Suleyman was co-founder and chief executive of Inflection AI until 2024-03-19, and chief executive of Microsoft AI from that date. Every claim's date falls inside one of these roles, and each file's notes name the right one.

---

### 2023-06-29-suleyman-greatest-productivity-leap-10-to-20-years  (sample)  — PASS
- quote: ok. The captions at 0:03:41 to 0:03:50 read "over the next 10 to 20 years this is going to be the greatest Leap Forward in productivity that our species has ever known probably more so than the Industrial Revolution", word for word.
- date: ok. CNBC Television uploaded it on 2023-06-29.
- role: ok. He was chief executive of Inflection AI.
- admission: ok. The subject of the sentence is AI ("the potential to take ... our intelligence and try to automate that"). It is a forecast of what AI will do to the economy, the same kind of forecast as the jobs ruling (a forecast that AI will displace or change jobs is admitted).
- due: ok. The range gives 2043, with 2033 as the earlier end.
- verdict: ok. It is not yet due.
- notes: the notes call this "a borderline case" and enter it anyway, but the method says "a truly borderline case stays out". The wording should say instead why it is not borderline (AI is the cause, as with the jobs ruling). This changes no count. The same wording problem appears in the 2025-10-20 and 2025-09-18 files below.

### 2023-09-07-suleyman-human-level-action-tasks-five-years  (sample)  — PASS
- quote: ok. The captions at 0:43:55 to 0:44:01 read "it's going to get over the next five years to human level performance across a very wide range of of AQ tasks", word for word. Just before it he names the tasks: using software interfaces (APIs), phoning a person to book a restaurant, buying, planning, organising a schedule.
- date: ok. Metis Strategy uploaded it on 2023-09-07.
- role: ok. He was chief executive of Inflection AI.
- admission: ok. Under reading 4 this is not bare "human level": it is human-level performance at tasks he names in the same answer, which is a stated comparison and gives a plain test.
- due: ok. 2028.
- verdict: ok. It is not yet due.
- notes: "very rudimentary ... late next year" and "in the next few years it's going to get exceptional" sit beside it. The first is its own record (the Pi actions file). The second is undated under reading 3 and rightly left out.

### 2023-09-07-suleyman-personal-ai-practical-tasks-two-to-three-years  (neg)  — PASS
- quote: ok. The captions at 0:17:01 to 0:17:09 read "it isn't going to be quite ready this year or next but certainly in the next you know two to three years it's going to get really really good at some of those very practical tasks", word for word.
- date: ok. Washington Post Live uploaded it on 2023-09-07.
- role: ok.
- admission: ok.
- due: ok. 2026, with 2025 as the earlier end.
- verdict: "cannot be tested" is right for the main claim. "Really really good" at "some of" the tasks has no measure.
- reading 2 (a forecast that something will not happen): the first half, "isn't going to be quite ready this year or next", is a forecast that something will not happen by the end of 2024. The builder chose not to enter it as its own record, because "quite ready" names nothing an outsider could check, and logged that choice in the search log (row `suleyman-claims-065`, the Washington Post re-read). That is a reasonable reading. Reading 2 still needs a thing a record could show, and readiness is a judgement, not an event.
- notes: `kind = deployment` could as well be capability. This changes no count.

### 2024-02-20-suleyman-hallucinations-largely-eliminated-next-year  (fails)  — FAIL (the miss stands; one sentence of the reason misreports its source)
- first-pass problem: fixed but new problem. The test is now a plain reading of his comparison with "any content that you can find on the web", and the claim is scored as missed, as the first pass asked. The new problem is that the reason misquotes the GPT-5 system card (below).
- quote: n/a, since the file is marked press coverage only. `reported_as` matches the article. Communications Today quotes "I'm very convinced that we're going to largely eliminate hallucinations over the next year. And they're going to be as accurate as any content that you can find on the web."
- date: ok. The article was published 2024-02-21 01:55 UTC, the night of the forum's first day.
- role: ok. He was chief executive of Inflection.
- admission: ok.
- due: ok. 2025.
- verdict: the miss stands on the outside record. The BBC media centre page, published 22 October 2025, says journalists judged "more than 3,000 responses from ChatGPT, Copilot, Gemini, and Perplexity"; "45% of all AI answers had at least one significant issue"; and "20% contained major accuracy issues, including hallucinated details and outdated information". Those are answers measured against the news they draw on, which fits the test. `evidence_by = outside` and `direction = not_come` are right.
- problem: the `verdict_why` says OpenAI's GPT-5 system card found "11.6% to 22% of answers with at least one major factual error, depending on the model". Figure 1 (page 13, "Factuality on ChatGPT Production Traffic (Browsing Enabled)") gives 22.0% for o3, 20.6% for GPT-4o, 11.6% for gpt-5-main and **4.8% for gpt-5-thinking**. The search-log row for the system card (`suleyman-claims-009`) records the 4.8% figure too. The sentence leaves out the very figure that most favours him.
- must change: correct the range to "4.8% to 22%" and say why even 4.8% is not "as accurate as" the reliable web content the test names. Otherwise, drop the OpenAI sentence and let the BBC and European Broadcasting Union study carry the verdict on its own. The status does not change.
- notes: the 20% figure counts outdated information as well as made-up details. The reason says "made-up details were not largely eliminated", which the study's wording supports but does not separate out. That is acceptable.

### 2024-04-suleyman-self-improving-ai-five-to-ten-years  (fails, neg)  — PASS
- first-pass problem: fixed. The test is now a floor scored under reading 2: the claim holds if no AI system has been shown to "independently self-improve, update its own code, explore an environment without oversight, and ... without a human in control" by the end of 2029. An early arrival can no longer be scored as a hit.
- quote: ok. TED's captions at 0:20:09 read "I think it's still a good five to 10 years before we have to really confront that.", preceded at 0:19:49 to 0:20:06 by the self-improvement description quoted in the test, and "we're still some way away from that".
- date: ok. TED uploaded it on 2024-04-22, from TED2024, so recording only the month is right.
- role: ok. He was chief executive of Microsoft AI.
- admission: ok. It is a forecast that something will not happen by a date (reading 2). "Human level" does not come into it.
- due: acceptable. The floor is taken at the earlier end (five years), which is the generous end for a forecast that something will not happen. The year-end convention then stretches that window by about eight months against him, from April 2029 to December 2029. For a forecast that something will not happen, a `due_date` of 2029-04-30 would be the fairer reading of "five years". The method does not settle this, so it is a point for John, not a fault. Leaving the ten-year end unscored is a defensible reading of his emphasis ("still some way away").
- verdict: ok. It is not yet due. The note on the Darwin Godel Machine (sandboxed, with human oversight) correctly decides nothing, and it fits this test, which needs exploring "without oversight".
- notes: none further.

### 2024-06-25-suleyman-real-time-interruptible-voice-by-end-of-year  (fails, hits)  — PASS
- first-pass problem: fixed. The settling record is now Google's post of 2024-08-13, which states the interrupt condition outright.
- quote: ok. The captions at 0:44:36 to 0:44:45 read "literally by the end of this year we'll have realtime voice-based interfaces that allow full Dynamic interrupt and it feels like just talking", word for word. He is answering a New Jersey teacher's general question, and no Microsoft product is named, so reading "we" as the whole field is fair.
- date: ok. NBC News uploaded it on 2024-06-25. The `when_note` now gives the right festival dates (2024-06-23 to 2024-06-29).
- role: ok.
- admission: ok.
- due: ok. 2024-12-31.
- verdict: confirmed. Google's post (datePublished 2024-08-13T17:00Z) says "Gemini Live begins rolling out today in English to our Gemini Advanced subscribers on Android phones" and "You can even interrupt mid-response to dive deeper on a particular point". That meets every condition of the test: public, real time, interruptible, and before the due date. `verdict_on` 2024-08-13 is right. `evidence_by = outside` is right, since Google is not his company. `direction = on_time` is right.
- notes: none.

### 2024-09-18-suleyman-ai-memory-workable-in-18-months  (hits)  — PASS
- quote: ok. The captions at 0:25:11 to 0:25:15 read "I I think that we're 18 months away from really getting that to a workable level". "That" is an AI that "really does remember everything that You' said and it's able to retrieve from that history of your conversations accurately" (0:25:02 to 0:25:08). Kara Swisher asked about the timeline in general, so it is about the field.
- date: ok. At 0:36:09 to 0:36:13 Swisher says Microsoft and BlackRock announced their fund "yesterday". That fund was announced 2024-09-17. The upload is dated 2024-10-23.
- role: ok.
- admission: ok.
- due: ok. 2026-03-18.
- verdict: confirmed. OpenAI's release notes have a "January 15, 2026" entry, "Improved memory for finding details from past chats": "ChatGPT can now more reliably find specific details from your past chats when you ask. Any past chat used to answer your question now appears as a source". Together with Altman's post of 2025-04-10 ("reference all your past conversations", search-log row `suleyman-claims-054`), every condition is met before the due date. `verdict_on` 2026-01-15 is right.
- notes: `evidence_by = outside` meets the letter of the method, since OpenAI is not his company. But the method describes "outside" as someone else having *measured* it, and here no one measured it: it is OpenAI describing its own product, as the reason itself admits. The sister file (the 2025 permanent memory claim) is now marked as the maker's word. A reader would be served better if this ledger had one consistent label for "the product's own maker, not the speaker's company". This changes no count.

### 2024-09-18-suleyman-capable-ai-free-to-everybody-by-2030  (sample)  — PASS
- quote: ok. The captions at 0:37:49 to 0:37:58 read "if you roll that forward to 2030 then you know you've got real value like real capability that is fundamentally free", word for word. It goes on "if not zero marginal cost and available to everybody".
- date: ok. Same session as the claim above.
- role: ok.
- admission: ok. "Roll that forward" is an extrapolation he believes ("that Dynamic is almost certainly going to continue"), not a hypothetical. It is about how widely AI is deployed, not a business forecast.
- due: ok. 2030.
- verdict: ok. It is not yet due.
- notes: reading "real capability" as the 2024 frontier follows his own GPT-3 analogy (free on a phone three years after release). That is a fair plain reading.

### 2024-10-suleyman-no-scaling-slowdown-two-to-three-years  (neg)  — PASS
- quote: ok. The captions at 0:16:31 to 0:16:37 read "I don't see any sort of slowdown at least for the next two to three years in Scale Models delivering outsize performance", word for word.
- date: ok. Masters of Scale uploaded it on 2024-11-02, from the October 2024 summit.
- role: ok.
- admission: ok.
- reading 2: this is a forecast that something (a slowdown) will not happen. Keeping it as "cannot be tested" is a reasonable call. Reading 2 scores a forecast that something will not happen by whether there is a public record of the thing, and a "slowdown" in "outsize" gains is not an event that any record could show. The `verdict_why` should say in one clause why reading 2 does not supply a test, so a reader does not think the reading was missed.
- due: inconsistent with the self-improvement floor file above. "At least for the next two to three years" is a floor. The 2024-04 file takes a floor at its earlier end, but this file takes the later end (2027, with 2026 as the earlier end). Under the rule that a claim that cannot be tested counts among the due only from its own date, the two choices make it due at different times. Neither date has passed yet (today is 2026-10-19), so no count changes now. The two files should follow one rule.
- verdict: ok.

### 2024-10-suleyman-permanent-ai-memory-done-in-2025  (fails, hits)  — PASS
- first-pass problem: fixed. The test now names Microsoft's Copilot, it is scored on Microsoft's own record, and `evidence_by` is `maker`.
- quote: ok. The captions at 0:14:24 to 0:14:29 read "I'm I'm really confident 2025 memory is done permanent memory". The words that follow ("we already have memory on the web ... co-pilot has really good citations ... we're just kind of compressing that to do it for your personal Knowledge Graph") make it a claim about Copilot.
- date: ok.
- role: ok.
- admission: ok.
- due: ok. The end of 2025.
- verdict: confirmed on the archived Microsoft post, dated Oct 23, 2025 and written by Mustafa Suleyman: "Copilot now has long term memory"; "you can ask Copilot to remember important information ... then recall it during future interactions"; "We're also beginning to roll out the ability to reference past conversations"; "edit, update, or delete memories at any time". A lasting memory that is used in later conversations shipped in 2025, so the test is met. `evidence_by = maker` and `direction = on_time` are right.
- notes: the judgement call (reading "done" as shipped, not perfect) is disclosed. Memory was first announced on 2025-04-04, so `verdict_on` could be that earlier date. Either date is inside 2025 and changes no count. The `restates` link to the 18-month claim is acceptable as a changed repeat, though the subject has narrowed from the field to Copilot.

### 2024-12-05-suleyman-copilot-vision-all-apps-always-on-2025  (fails)  — PASS
- first-pass problem: fixed. The reason now describes the end-of-2025 position from Microsoft's post of 2025-10-16, and the miss rests on the always-on condition.
- quote: ok. The captions at 0:17:36 to 0:17:40 read "yeah I mean that is definitely coming uh you know next year", answering Rowan Cheung's question (quoted correctly in the notes) about "fully functioning Vision across all their apps across all their screens 24/7 and no limitations on websites and apps and possibly even infinite memory". He adds "might be the back end of next year might be the summer might be a bit earlier".
- date: ok. The Rundown AI uploaded it on 2024-12-05.
- role: ok.
- admission: ok.
- due: ok. The end of 2025.
- verdict: confirmed on the archived post, dated October 16, 2025 and written by Yusuf Mehdi: "Copilot Vision on Windows is now available worldwide"; "available in all markets where Copilot is offered", with "Full desktop and app sharing: When you share ..."; "with your permission, Copilot Vision can analyze what's on your screen"; "This opt-in experience". It ran in sessions the user starts, not 24/7. `evidence_by = maker` and `direction = not_come` are right.
- notes: the miss depends on reading the interviewer's "24/7" as always on (watching all the time), not "available whenever you want it". The always-on reading fits his own answer, which names the cost of seeing "your screen in real time" as the constraint, and the test was not rewritten to fit the verdict (only the reason changed). But the other reading would bring this near a hit, so the notes should say this is the judgement the verdict rests on. The test drops the interviewer's "possibly even infinite memory", which is right.

### 2025-09-18-suleyman-ai-long-horizon-actions-by-end-of-2026  (sample)  — PASS
- quote: ok. The captions at 1:01:06 to 1:01:09 read "And I think that we basically have that by the end of next year." "That" is "take actions over infinitely long time horizons" (1:00:48 to 1:00:59), which follows the description of storing "persistent state" to act "over very very very long sequences of activity".
- date: ok. Trevor Noah's channel uploaded it on 2025-09-18.
- role: ok.
- admission: ok. "Now imagine when it's able to ..." introduces the capability, and the dated sentence after it is his own flat forecast, so this is not a hypothetical of the kind the rule excludes. As in the first file, the notes should not call it "a borderline case", since the method says borderline cases stay out. They should say why it is not borderline.
- due: ok. 2026-12-31, still ahead.
- verdict: ok. It is not yet due.
- notes: "days, not minutes" in the test is the builder's gloss on "infinitely long". That is a fair plain reading of "very very very long sequences", but it is the condition the 2026 verdict will turn on.

### 2025-10-20-suleyman-greatest-productivity-boost-next-couple-of-decades  (sample)  — PASS
- quote: ok. The captions at 0:03:53 to 0:04:02 read "this AI moment is going to deliver the greatest boost to productivity in the history of our species in the next couple of decades", word for word, followed by "That to me is unquestionable."
- date: ok. Young and Profiting uploaded it on 2025-10-20.
- role: ok.
- admission: ok, for the same reason as the 2023 productivity claim. The same wording note applies to "Close to the line ... entered".
- due: ok. "A couple of decades" is read as 20 years, giving 2045. "Couple" names two, unlike "a few", so reading 3 does not make it undated.
- verdict: ok. It is not yet due.
- notes: the `restates` link to the 2023-06-29 file is right.

### 2025-12-12-suleyman-goal-setting-self-improving-ai-emerges-5-to-10-years  (neg)  — PASS
- quote: ok. The captions at 0:07:22 to 0:07:32 read "we all predict a time in the next 5 years maybe in the next 10 years where these capabilities do start to emerge", word for word.
- date: ok. Bloomberg Podcasts uploaded it on 2025-12-12.
- role: ok.
- admission: ok. He counts himself in "we all predict". This is not a forecast that something will not happen: it is a deadline, so reading 2 does not apply. The sentence before it ("I don't see any indication that these things are improving themselves") is a statement about the present, not a forecast. Bare "human level" does not come up.
- due: ok. 2035, with 2030 as the earlier end.
- verdict: ok. It is not yet due.
- notes: his words are "systems like this could set their own goals **or** they could improve their own code **or** they could act autonomously". The test requires all three ("setting its own goals, improving its own code **and** acting autonomously"). "These capabilities" (plural), and his "close we are to those three capabilities", support the reading that all three are needed. But the rule that a test "adds no condition he did not state" makes this worth a sentence in `due_basis` or `notes` saying how his "or" is read, since the test is fixed at entry. This changes no count now.

---

## The builder's own calls (a to g), where these files touch them

- **(d) Suleyman's 2025 self-improvement experiment "did not"** (the file `2024-10-suleyman-teams-experiment-with-self-improvement-in-2025`, which is not in this batch but is cited by the 2024-04 file). **I judge this not a reasonable reading.** The file's own test reads his "doesn't have a human directly overseeing it" as "no person reviewing or approving each one" (each change). The file's own reason says the Darwin Godel Machine ran "with no person approving each change". By its own test, then, the record meets the condition. The miss rests on the paper's general safety line, "All experiments were done with safety precautions (e.g., sandboxing, human oversight)". That is oversight of the experiment as a whole, not a person directly overseeing the loop. So the verdict contradicts the test it is scored against. Either the status should be came true (an outside record, `verdict_on` 2025-05-29), or the file should say plainly that the test itself is being read differently, which the rule against changing a test to fit a verdict forbids. The 2024-04 file's use of the same paper is fine, because its test needs exploring "without oversight" and "without a human in control", which is a stricter condition.
- **(g) jobs forecasts admitted:** not directly in this batch. The two productivity claims rest on the same reasoning (a forecast of what AI will do to the economy), which I find consistent with the ruling.
- (a), (b), (c), (e) and (f) do not touch these files.

## Summary

PASS 13, FAIL 1, COULD NOT VERIFY 0.

- **2024-02-20-suleyman-hallucinations-largely-eliminated-next-year:** the `verdict_why` gives the GPT-5 system card's error range as "11.6% to 22%". The card's Figure 1 shows 4.8% for gpt-5-thinking, so the reason leaves out the figure most favourable to him. Correct the range or drop the sentence. The miss stands on the BBC and European Broadcasting Union study.

Cross-file points that change no count:
- Three files call themselves "borderline" yet are entered, which contradicts the method's "a truly borderline case stays out": the two productivity claims and the Trevor Noah long-horizon claim. The wording should say why each is not borderline.
- The no-slowdown claim takes a floor at its later end, while the self-improvement claim takes a floor at its earlier end. They should follow one rule.
- The `evidence_by` label for the field-wide memory hit is `outside`, though the only record is the product maker's own description.
- Call (d) above contradicts its own test, and in my view that file's status should be reconsidered.

## Batch 10

# Second-pass check, batch 10 (Suleyman, Sutskever, Zuckerberg): results

Checked 2026-10-19. Sources were read fresh: YouTube captions through yt-dlp (into `dl2-10-yt/`), Meta's call transcripts as PDFs from its investor-relations file host, the Meta newsroom pages, Lex Fridman's transcript page, the Threads posts (read as a link-preview bot sees them, and dated from the post ids), Pew's chart and TechCrunch (into `dl2-10-web/`). Nothing in the repository was edited.

### 2025-12-12-suleyman-machines-better-than-humans-at-most-work-20-to-30-years  (sample)  — PASS
- quote: ok. Bloomberg Podcasts upload, captions 0:12:10 to 0:12:19: "it is inevitable that at some point over the next 20 or 30 years um machines are going to be more capable than humans at doing most work and that might come much sooner". The quote is a verbatim run that starts at "over".
- date: ok. Uploaded 2025-12-12.
- role: ok. Chief executive of Microsoft AI.
- admission: ok. About AI, looks forward, carries a span, not a hypothetical.
- due: ok. A range of spans: 2045 at the earlier end, 2055 at the later.
- verdict: ok. Not yet due.
- notes: the test says "most kinds of paid work". He said "most work". "Paid" is a fair reading, since the next sentences are about displacement and funding people, but it is the builder's word, not his.

### 2025-12-16-suleyman-ai-diagnosis-free-to-everybody-by-2030-or-2035  (sample)  — PASS
- quote: ok. Mayim Bialik's upload, captions 0:31:48 to 0:31:54: "it is basically going to be zero marginal cost and free to everybody in the world by 2030 or 2035."
- date: ok. Uploaded 2025-12-16.
- role: ok.
- admission: ok.
- due: ok (2035, earlier end 2030).
- verdict: ok. Not yet due. "It" refers back to the Microsoft AI diagnostic orchestrator (0:31:12 to 0:31:31), so the narrowed test follows his words.
- notes: the note's quotation drops "four or five months ago" with an ellipsis. That is harmless.

### 2026-02-12-suleyman-agents-write-own-code-one-or-two-years  (sample)  — PASS
- quote: ok. Financial Times upload (2026-02-12), captions 0:10:24 to 0:10:30: "in a year or 2 years' time, these systems truly are going to be capable of writing their own code."
- date: ok.
- role: ok.
- admission: ok. It looks forward and carries a span. He adds "they can do that today", and the notes say so.
- due: ok (2028, earlier end 2027).
- verdict: ok. Not yet due.
- notes: the test adds two things he did not say: "and running" their code, and "with no person directing each step". The second is a fair reading of the autonomous Moltbook agents he is describing, but under the bar rule ("adds no condition he did not state") it is better tied to his words or dropped. Do this before the claim comes due in 2028. No count changes now. He said "arbitrary APIs", and the test's "arbitrary software interfaces" is a fair plain rendering.

### 2023-03-22-sutskever-reliability-progress-next-two-years  (sample)  — PASS
- quote: ok. Captions 0:48:19 to 0:48:21: "so I think we'll see a lot of that in the next two years". He says it in answer to Huang's "pick your horizon a year or two". The preface "predictions are hard" is in the file.
- date: ok. The GTC 2023 fireside chat aired 2023-03-22. The YouTube copy is a third-party re-upload of 2024-10-13, and the file says so.
- role: ok. OpenAI's chief scientist.
- admission: ok.
- due: ok (2025).
- verdict: ok. "A lot of" progress on reliability sets no level, so "cannot be tested" is right.
- notes: the source is a re-upload of the full recording by someone other than NVIDIA. That is disclosed. NVIDIA's own on-demand copy would be the stronger link if it can be found.

### 2023-02-01-zuckerberg-generative-ai-launches-this-year  (hits)  — PASS
- quote: ok. Meta's transcript of the fourth-quarter 2022 call (dated February 1st, 2023), his first answer, to Brian Nowak's question on generative AI: "So I think you'll see us launch a number of different things this year".
- date: ok.
- role: ok.
- admission: ok. The things are generative AI products ("large language models and diffusion models for generating images and videos and avatars").
- due: ok (2023-12-31).
- verdict: ok. The release is dated 2023-09-27 (datePublished 2023-09-27T17:47 UTC). It says AI stickers are "starting to roll out", Meta AI is introduced "in beta", and 28 AIs are rolling out "in beta in the United States today". That is three launches, so more than two. Restyle and backdrop are "coming soon to Instagram" and are now correctly left out. Every condition is met by the date. Maker evidence, honestly marked.
- notes: the first pass's wording fix is done.

### 2023-09-27-zuckerberg-glasses-multimodal-ai-early-next-year  (fails)  — PASS
- first-pass problem: fixed. "Early next year" is now read under John's reading 1 (first quarter, due 2024-03-31). Only the date in the test changed; the git diff of the re-pass commit shows "in the first half of 2024" became "by the end of March 2024". "In beta" is now in the reasons.
- quote: ok. The Decoder (The Verge) upload of 2023-09-27, captions 0:45:56 to 0:46:00: "sometime early next year we're also going to have this multimodality so you're going to be able to ask the AI".
- date: ok.
- role: ok.
- admission: ok.
- due: ok (due_date 2024-03-31).
- verdict: ok. Missed, came later. The release is dated 2024-04-23 (datePublished 2024-04-23T15:34 UTC). It says "We started testing a multimodal AI update in December" and "Starting today, we're rolling this functionality out to all Ray-Ban Meta smart glasses in the US and Canada in beta". That is 23 days after the due date. The December test was not a release to owners in general, so it does not meet "for ordinary owners".
- notes: the reasons say the December test was "with a small number of owners who opted in". The cited release does not say that. Meta's December 2023 early-access announcement does, so either cite it or drop the phrase. This is a wording fix only.

### 2023-09-28-zuckerberg-creator-ais-next-year  (hits)  — PASS
- quote: ok. Lex Fridman transcript page (published 2023-09-28T17:10 UTC), in his turn after the (00:42:59) marker: "So that one I think will probably start releasing sometime next year." "That one" is the AI that embodies a real creator, the subject of the turn before.
- date: ok.
- role: ok.
- admission: ok.
- due: ok (2024).
- verdict: ok. The AI Studio release is dated 2024-07-29 (datePublished 2024-07-29T22:00 UTC). It says it is "starting to roll out AI Studio in the US" and "allows creators to build an AI as an extension of themselves to reach more fans". That is a public release within 2024 meeting every condition. Maker evidence.
- notes: the page now carries an update of 2026-08-10 saying no new AI characters can be created. It has no bearing on the 2024 verdict.

### 2024-07-23-zuckerberg-meta-ai-most-used-by-end-of-year  (fails)  — PASS
- first-pass problem: fixed. It is no longer scored as came true on Meta's own word about its rivals; it is now "did not come true" because the comparison is not shown. The test's dated note records the change, and the change applies the method's existing rule (a maker's own figure counts as evidence only for a figure only the maker holds). It is not shaped toward a verdict.
- quote: ok. The Rundown AI (Rowan Cheung) upload of 2024-07-23, captions at about 0:27:35: "my goal was for it to be the most used AI assistant in the world by the end of the year". He follows it with "we'll probably hit ... that Milestone ... few months before the end of the year", which is in the prediction.
- date: ok.
- role: ok.
- admission: ok. A goal, marked.
- due: ok (2024).
- verdict: ok. The third-quarter 2024 transcript (October 30th, 2024) has "Meta AI now has more than 500 monthly actives" (sic) and "over 500 million". The fourth-quarter 2024 transcript has "Meta AI is already used by more people than any other assistant" and "more than 700 million monthly actives". The comparison rests only on Meta's word. The Pew chart (published 2026-06-17, survey of US adults 2026-02-17 to 23) has ChatGPT at 44% and Meta AI at 14% for "ever use", and the file correctly calls it later context and US only.
- notes: (1) `direction = "not_come"` is the nearest of the allowed words, but what failed is that the lead was not shown, not a record that it did not happen. The reasons say this plainly, so readers are not misled. (2) `verdict_on` is the due date. With no record of the event, that is acceptable.

### 2024-10-30-zuckerberg-smaller-llama-4-early-next-year  (fails)  — PASS
- first-pass problem: fixed. It is now due 2025-03-31 under John's reading 1 and scored missed, came later. The diff shows only the date in the test changed.
- quote: ok. Third-quarter 2024 transcript, opening remarks: "I expect that the smaller Llama 4 models will be ready first, and they'll be ready, we expect sometime early next year".
- date: ok.
- role: ok.
- admission: ok.
- due: ok (due_date 2025-03-31).
- verdict: ok. The Threads post reads "New drop: llama.com/4", and its post id decodes to 2025-04-05 18:58 UTC: five days late. Maker record of the release.
- notes: none.

### 2025-01-24-zuckerberg-llama-4-leading-model-2025  (sample)  — PASS
- quote: ok. The Threads link preview reads "... Llama 4 will become the leading state of the art model ...". The post id decodes to 2025-01-24 14:00 UTC.
- date: ok.
- role: ok.
- admission: ok. The link to the earlier claim it repeats with a change exists (`2024-07-23-zuckerberg-llama-most-advanced-next-year`).
- due: ok (2025).
- verdict: ok. The fourth-quarter 2025 transcript (January 28th, 2026) has "In '25 we rebuilt the foundations of our AI program". The Sources Podcast upload of 2025-09-18 (the search log calls it "Access") has, in its captions at about 1:00:12, "I didn't feel like we were on the trajectory that we needed to be on to to basically like be at the frontier". Missed, has not come.
- notes: the search log names the show "Access", but the upload's channel is "Sources Podcast". Check the name before it is published anywhere. The verdict rests on his own words (`maker`), which is honest. Outside leaderboards of 2025 would make it `outside` if a stronger source is wanted.

### 2025-01-24-zuckerberg-meta-ai-leading-assistant-billion-people  (fails)  — PASS
- first-pass problem: fixed. It is now missed: the billion condition is met on Meta's count, the "leading" condition is not shown.
- quote: ok. Threads preview: "In 2025, I expect Meta AI will be the leading assistant serving more than 1 billion people".
- date: ok.
- role: ok.
- admission: ok. The link to the earlier "most used" claim, as a changed repeat, is right.
- due: ok (2025).
- verdict: ok. The second-quarter 2025 transcript (July 30th, 2025) has "Its reach is already quite impressive with more than a billion monthly actives. Our focus is now deepening the experience and making Meta AI the leading ..." TechCrunch (2025-10-06) quotes Altman: "More than 800 million people use ChatGPT every week". Neither shows a lead.
- notes: the same `direction = "not_come"` point as the "most used" file. Reading "leading" as most used is argued in the notes and is the plainest reading of the sentence.

### 2025-04-30-zuckerberg-coding-agents-substantial-ai-research-2026  (sample)  — PASS
- quote: ok. First-quarter 2025 transcript (April 30th, 2025): "So I'd expect that by the middle to end of next year, AI coding agents are going to be doing a substantial part of AI research and development."
- date: ok.
- role: ok.
- admission: ok.
- due: ok (2026-12-31, the later end).
- verdict: ok. "A substantial part" sets no level, so "cannot be tested" is right. It is consistent with the scored "most of the code" claim (`2025-04-29-zuckerberg-most-ai-research-code-by-ai`), where "most" does set a level. The claim counts as due only from 2026-12-31.
- notes: none.

## The builder's own calls, where these files touch them

- **a. "The next few months" and "the coming months" read as undated.** These files do not use the call directly. The search-log rows they cite record three Zuckerberg removals under it: the multimodal Llama "next few months" claim, a former hit (row `zuckerberg-claims-062`); "Little Llama" (row `-018`); and new models "over the coming months" (row `-031`). The call is consistent with the reason behind reading 3 (the words name no length), so it is a defensible reading. It is weaker than for years, though: "a few months" plainly ends within about a year, and one could instead judge such claims at twelve months. It removes at least one hit for Zuckerberg, so John should rule on it, as the method already flags.
- **g. Jobs forecasts admitted.** Touched only loosely, by Suleyman's "more capable than humans at doing most work", which is a capability claim and is admitted either way.
- **b to f.** Not touched by these files.

## Summary

PASS 12, FAIL 0, COULD NOT VERIFY 0.

All four files that failed the first pass are fixed in line with John's rulings. The two "early next year" claims are now first-quarter misses (later), with only the date in the test changed. The two "most used" and "leading assistant" claims are now misses, because nothing outside Meta shows the lead.

Wording fixes that change no verdict:
- **Copilot agents writing their own code** (`2026-02-12-suleyman-agents-write-own-code-one-or-two-years`): the test adds "with no person directing each step" and "running", which he did not say.
- **Multimodal AI on the glasses** (`2023-09-27-zuckerberg-glasses-multimodal-ai-early-next-year`): the "small number of owners who opted in" detail is not in the cited release.
- **Meta AI most used, and leading assistant** (both Meta AI files): `direction = "not_come"` stands for "not shown".
- **Llama 4 leading in 2025** (`2025-01-24-zuckerberg-llama-4-leading-model-2025`): the search-log row for the 2025-09-18 podcast (`zuckerberg-claims-073`) calls it "Access", but the upload is on the "Sources Podcast" channel.
