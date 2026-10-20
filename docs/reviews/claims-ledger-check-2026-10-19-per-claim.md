# Claims ledger check, per-claim results (2026-10-19)

Ninety claim files from pull request 23, checked against their sources by nine helpers of the checking session. Sample drawn with Python's random.seed(20261019) from the 233 new files that are neither 'came true' nor coverage-only. Summary and verdict: claims-ledger-check-2026-10-19.md beside this file.

## Batch 1

# Batch 1 results: independent check of ten claim files (2026-10-19)

Sources were opened 2026-10-19: the text pages with curl, the YouTube captions with yt-dlp (automatic English captions, upload dates from yt-dlp), and the OpenAI pages through Internet Archive copies, because openai.com returned 403.

One problem runs across the whole batch. The method says "Each claim's notes name the role that applied". None of the three Altman files has a role note, and neither do any of the 16 Altman files in `data/claims/`. A grep finds 131 claim files in the folder with no role note at all. The roles themselves are correct: Altman was OpenAI's chief executive on every date in this batch. The notes are missing, though, and the validator does not check for them.

---

### 2021-03-16-altman-five-years-legal-documents-medical-advice.toml  (oldhits)  — FAIL
- quote: ok. Verbatim on moores.samaltman.com; the byline reads "by Sam Altman · March 16, 2021".
- date: ok.
- role: ok. Chief executive of OpenAI since 2019. The role note is missing (see above).
- admission: ok.
- due: ok. Five years from 2021-03-16 gives a due date of 2026-03-16.
- verdict: problem. The status `hit` can stand, but the record behind it is wrong.
  - The bar has two halves, and `verdict_on = 2023-03-15` (the GPT-4 report, arXiv v1 submitted 15 Mar 2023, which says "around the top 10% of test takers" on the simulated bar exam) settles only the legal half.
  - The medical half rests on OpenAI's "Introducing ChatGPT Health" page. The Internet Archive copy of 2026-01-11 dates it **January 7, 2026** and has the 230 million figure and the "not intended for diagnosis or treatment" line.
  - So the whole bar was settled on 2026-01-07, not 2023-03-15.
  - Fix: set `verdict_on = 2026-01-07`. Cite the ChatGPT Health page (`https://openai.com/index/introducing-chatgpt-health/`) alongside the GPT-4 report, or as the main `verdict_source`, since it is the later of the two. Change `direction` from `sooner` to `on_time`: the whole bar was met only about ten weeks before the due date. Clear `verify`, which the January 7, 2026 date answers.
- notes:
  - `source_locator` says the paragraph is "near the end". It is in the essay's opening section, about 800 characters into a page of about 17,500. Change it to "in the opening section, the paragraph beginning 'In the next five years'".
  - The bar is loose, as the file itself says. Both halves rest on OpenAI's word (`maker` is honest).

### 2024-03-18-altman-amazing-new-model-this-year.toml  (oldhits)  — PASS
- quote: ok. Verbatim at 01:06:30 on the lexfridman.com transcript.
- date: ok. The page's datePublished is 2024-03-18T01:13 UTC, which is the evening of 2024-03-17 on US Pacific time. That is minor; the recording date is not given.
- role: ok. Chief executive of OpenAI. The role note is missing.
- admission: ok. It is a product promise about OpenAI's own release, dated "this year".
- due: ok. Judged at 2024-12-31.
- verdict: ok. OpenAI's o1-preview page (Archive copy) is dated September 12, 2024.
- notes: `verdict_on` should arguably be **2024-05-13**, the day GPT-4o came out, which OpenAI called a new flagship model. That release was public in 2024 and met the bar four months before o1-preview. The verdict does not change, but the date the record settled the claim is the earlier release. `when_note` says "Same transcript page and date as the claim above", which points at a neighbouring file and reads oddly on its own.

### 2025-10-29-altman-automated-research-intern-by-september-2026.toml  (oldhits)  — FAIL
- quote: ok. Verbatim in the post text from api.fxtwitter.com; created_at is Wed Oct 29 17:19:00 +0000 2025.
- date: ok.
- role: ok. Chief executive of OpenAI. The role note is missing.
- admission: ok. It is a goal, flagged as `is_goal`.
- due: ok. The words "by September of 2026" give a due date of 2026-09-30, which has passed.
- verdict: problem, on two grounds.
  1. **Not every condition is shown.** The bar includes "running on hundreds of thousands of GPUs". OpenAI's post of 2026-09-06 (Archive copy, dated "September 6, 2026") says "we have now reached the goal ... of having an automated research intern by September of this year" and defines a research intern. It says nothing about the system running on hundreds of thousands of GPUs; the only GPU passage is about how compute was split between model types. The file admits this condition is unchecked, yet records a hit. Under the owner's rule ("EVERY condition in the bar met ... shown by a dated primary record") that is not a hit.
  2. **The bar comes from the wrong source.** The intern half of the bar is OpenAI's own definition, published on the day it declared success. The method takes the speaker's definition only from the same source; otherwise the bar is the plainest reading of the words. Letting the maker define the test in its success announcement is the gaming the method is meant to prevent.
  - Fix: write the bar as the plain reading of the October 2025 words, with a dated note. Then either find a dated record that OpenAI's system ran on hundreds of thousands of GPUs, or re-decide the status. On the current evidence it cannot be `hit`. The method's word for a bar met in part is `missed`. Whether that applies here, where one condition is unshown rather than shown false, is for John to rule.
- notes: `evidence_by = "maker"` is honest.

### 2024-04-12-amodei-agents-take-actions-3-to-18-months.toml  (hits)  — PASS
- quote: ok. Verbatim run of captions at 8:42–8:49 in Gi_t3v53XRU, uploaded 20240412 ("What if Dario Amodei Is Right About A.I.?").
- date: ok.
- role: ok. Co-founder and chief executive of Anthropic.
- admission: ok.
- due: ok. Three to 18 months from 2024-04-12 runs from July 2024 to October 2025, so `due = 2025` with `due_early = 2024`.
- verdict: ok. Anthropic's page dated October 22, 2024 says computer use was in "public beta", with Claude using a computer "by looking at a screen, moving a cursor, clicking buttons, and typing text".
- notes:
  - The same page also says computer use was "still experimental" and "at times cumbersome and error-prone", and it was offered to developers only. The bar does not test quality, and he said "with increasing levels of ability", so the hit holds. The verdict text could say "for developers, in beta".
  - "All of that" in his words also covered booking an Uber, reserving a restaurant and talking to the other people on the trip. The bar keeps only the website and computer part. That is defensible, but worth a line in the notes.

### 2024-04-12-amodei-asl3-this-year-or-next.toml  (hits)  — FAIL
- quote: ok. Captions at 1:02:27–1:02:32: "I think asl3 is is you know could easily happen this year or next year".
- date: ok.
- role: ok.
- admission: ok. "Could easily" is a hedge word, so the claim is scored at face value.
- due: ok. Due 2025, with `due_early = 2024`. The repeats on 2024-11-11 and 2025-03-10 carry the same due year, and the March 2025 repeat ("We may actually hit that this year") is verbatim on the Council on Foreign Relations transcript.
- verdict: problem.
  - **His own definition in the same interview** (58:59–1:00:21): AI Safety Level 3 (ASL-3) "is triggered by risks related to misuse of biology and Cyber Technology", defined as "a substantial increase in risk" of bioweapons misuse relative to a Google search. Under the method, a definition in the same source is the bar.
  - Anthropic's post of 2025-05-22 says the step was "precautionary and provisional". It says "we have not yet determined whether Claude Opus 4 has definitively passed the Capabilities Threshold", and that "clearly ruling out ASL-3 risks is not possible". A quick search found no later finding before 2025-12-31 that any model had crossed the threshold.
  - Protections switched on because the risk could not be ruled out are an argument that the risk was possible, not a record that it happened. The owner's rule says that is not enough for a hit.
  - The file's bar ("Anthropic applying its ASL-3 standard to a model because of that risk") was written after the event in a way that counts the precaution. That departs from the speaker's own definition.
  - Fix: judge the claim against his stated definition. As the record stands, that is `missed`, unless a dated Anthropic finding that a model crossed the threshold by 2025-12-31 turns up. The file flags this judgement call itself; it should go to John and not be published as a hit.

### 2024-11-11-amodei-lex-2026-or-2027-straight-line.toml  (sample)  — FAIL
- quote: ok. Verbatim on the lexfridman.com transcript at 02:20:00. The page is dated 2024-11-11T19:18 UTC.
- date: ok.
- role: ok.
- admission: problem.
  - The dated words are a conditional on a premise he disowns: "So I don't fully believe the straight line extrapolation, but if you believe the straight line extrapolation, we'll get there in 2026 or 2027."
  - His own most likely case is "some mild delay relative to that. I don't know what that delay is", so he gives no date of his own.
  - That fails the admission rule twice. It is a hypothetical ("if you believe"), and it carries no date of his own, so the dated-claim test fails. Under "borderline cases stay out" it should not be a claim record.
  - The file's reason for `unfalsifiable` ("no date exists by which a miss could be called") is really an admission failure, not one of the method's two grounds. The source does define the stage: Lex Fridman read out the powerful-AI definition at 02:17:24, including "smarter than a Nobel Prize winner in every relevant discipline", which is a named comparison.
- due: arithmetic ok (2027, early end 2026), but moot.
- verdict: problem. Leaving it in adds one to Amodei's "cannot be tested" count.
- notes: Fix: remove the record and log in the search log why it was left out, as the method says for other refused claims. The same applies to `restates` on any later record that points at this one. The record it restates, the 'Machines of Loving Grace' essay record (`2024-10-11-amodei-mlg-powerful-ai-as-early-as-2026`), is out of scope for this batch.

### 2024-amodei-new-model-most-intelligent-by-airing.toml  (hits)  — FAIL
- quote: ok. Captions at 0:49–0:55 in xm6jNMSFT7g, uploaded 20240626. The ellipsis stands for "and Powerful model".
- date: ok as "2024". The recording day is not given, and the interview came before the 2024-06-21 launch.
- role: ok.
- admission: ok, with the hedge "probably" scored at face value.
- due: ok. `due_date = 2024-06-26`, the day the episode went up.
- verdict: problem.
  - The release date is fine: Anthropic's page is dated Jun 21, 2024.
  - The page says Claude 3.5 Sonnet "raises the industry bar for intelligence, outperforming competitor models and Claude 3 Opus on a wide range of evaluations". The bar, though, is "leads the other companies' models on the main published comparisons", and the file admits outside leaderboards were not checked.
  - Checked now, the outside record goes against it. LMSYS Chatbot Arena, the main outside comparison of the time, put Claude 3.5 Sonnet **#2 overall behind GPT-4o** at launch (#1 only in Coding and Hard Prompts). VentureBeat reported it and quoted LMSYS's own announcement.
  - Anthropic's own table also had GPT-4o ahead on MATH (76.6 to 71.1, per several secondary reports; the table is an image and was not read directly).
  - So "the most intelligent model in the world" is shown only on the maker's word, while an outside dated record says otherwise.
  - Fix: weigh the LMSYS standing in the verdict. On the plain reading and "a near miss is a miss", this looks like `missed`, with the gap named: second overall on the main outside leaderboard. At minimum it needs John's ruling before it is published as a hit.
- notes: Another claim from the same podcast, the better-than-most-humans claim (`2024-06-26-amodei-better-than-most-humans-2025-2027`), uses the airing date (2024-06-26) as `when`, while this one uses "2024". Choose one rule for both.

### 2025-01-amodei-critical-window-better-than-humans-2026-2027.toml  (sample)  — PASS
- quote: ok. Captions at 14:34–14:43 in uvMolVW_2v0, uploaded 20250127. Verbatim.
- date: ok as "2025-01".
- role: ok.
- admission: ok.
- due: ok. Due 2027, with an early end of 2026.
- verdict: ok. Not yet due.
- notes:
  - His words are "the models **start** getting better than humans at everything". The bar ("perform better than people at essentially every kind of task") is a little stronger than "start", so it is worth a note.
  - "In other interviews I've said 2026 2027" marks this as a repeat. If an earlier record with the same comparison and due year exists, this should be a `repeated_on` date on it, not a separate record. The earlier records I checked differ: the straight-line conditional and the "almost everything" claim due 2028. So keeping it separate looks right.

### 2025-01-amodei-virtual-collaborator-parts-in-2025.toml  (hits)  — PASS
- quote: ok. Captions at 7:21–7:29, verbatim. The words that follow describe the collaborator: "works on that task for you know several hours maybe it checks in with you every once in a while".
- date: ok as "2025-01".
- role: ok.
- admission: ok.
- due: ok. Judged at 2025-12-31.
- verdict: ok. Anthropic's Claude 4 page is dated May 22, 2025 and says "with the ability to work continuously for several hours" and "Claude Code, now generally available". The page does not literally say the model checks in with the user, but Claude Code's edit review fits the plain reading.
- notes: He says "I've talked about" this, and the Wall Street Journal Davos claim of 2025-01-21 (`2025-01-21-amodei-virtual-collaborator-strong-version-this-year`, marked missed) is the same vision with a stronger condition. This record is a changed repeat of it under the method and should carry `restates = "2025-01-21-amodei-virtual-collaborator-strong-version-this-year"`, so the page groups the two. No count changes, but a reader should see that the hit is the weaker version said days later, beside the miss.

### 2025-03-10-amodei-cfr-ninety-percent-of-code-in-three-to-six-months.toml  (sample)  — PASS
- quote: ok. Verbatim on the Council on Foreign Relations event page, which carries "March 10, 2025 6:00 p.m. (EDT)" and the "uncorrected transcript" mark.
- date: ok.
- role: ok.
- admission: ok.
- due: ok. Three to six months from 2025-03-10 ends in 2025, so the claim is judged at 2025-12-31.
- verdict: ok. The status `missed` stands. Redwood Research (Ryan Greenblatt, 2025-10-22) estimates AI wrote "more like 50%" of the code merged at Anthropic, with about 90 percent only on some teams. It also says that read as all professional software work, "the prediction looks substantially worse".
- notes:
  - The bar is "code being written ... across programming generally". Redwood's estimate covers only Anthropic and is an outside estimate, not a count, so it is weak evidence for the general bar.
  - Dated first-person records of the general share exist and would be stronger: Pichai at Alphabet, April 2025, said about 30 percent of new code at Google; Nadella said 20 to 30 percent at Microsoft on 2025-04-29. Both are from memory and not opened in this check. Adding one would make the miss rest on a record of the event, not only on an absence.
  - `evidence_by = "outside"` is honest for Redwood.

---

## Summary

PASS 5, FAIL 5, COULD NOT VERIFY 0.

The five FAILs:
- **Altman, legal documents and medical advice in five years:** the hit stands, but the medical half was settled by OpenAI's ChatGPT Health page of 2026-01-07, not the 2023 GPT-4 report. Change `verdict_on`, add that page to `verdict_source`, change `direction` from `sooner` to `on_time`, and clear `verify`. The `source_locator` is also wrong: the paragraph is in the opening section, not near the end.
- **Altman, automated research intern by September 2026:** recorded as a hit with one bar condition (hundreds of thousands of GPUs) admitted unshown, and with the intern half of the bar taken from OpenAI's own success announcement, not the original words.
- **Amodei, AI Safety Level 3 this year or next:** a hit on precautionary protections. Anthropic said it had "not yet determined" the threshold was crossed, and his own definition in the interview was a real increase in bioweapons risk. On the record this is a miss, or a ruling for John.
- **Amodei, Lex Fridman "2026 or 2027" on the straight line:** the date is a conditional he disowns ("if you believe the straight line extrapolation"), with no date of his own. It should be left out under the hypothetical and borderline rules, not counted as "cannot be tested".
- **Amodei, new model "most intelligent" by airing:** the hit rests on the maker's word, while LMSYS Chatbot Arena put Claude 3.5 Sonnet #2 overall behind GPT-4o at launch. It looks like a miss, or a ruling for John.

Across the batch, the role note the method requires is missing from all 16 Altman files and from 131 claim files overall, and the validator does not check for it.

## Batch 2

# Batch 2 results: independent check of claim files against their sources (2026-10-19)

Sources were fetched on 2026-10-19: YouTube captions with yt-dlp, and pages with curl (the Axios page through the r.jina.ai reader copy, because axios.com refuses direct requests). Every quote below was matched against the downloaded text.

### 2025-05-22-amodei-one-person-billion-dollar-company-2026  (sample)  — FAIL
- quote: ok. The captions at 16:10 to 16:14 read "when do you think there'll be the first billion dollar company with one human employee? 2026." The captions do not mark who is speaking. The question is Krieger's, followed by "Yeah, I absolutely buy that". Press coverage of the event (Benzinga and others) gives the "2026" answer to Amodei, which fits the file.
- date: ok. The event was 2025-05-22. The Techusiness re-upload is dated 20250529 by yt-dlp.
- role: ok. He was chief executive of Anthropic.
- admission: doubtful. The words do not mention AI. The AI reading comes only from context: the event, and Krieger's lead-in about "relativistic" AI time. The claim is also about a company's value, which is close to the business-forecast exclusion. It is defensible as a claim about what AI will let one person do, but it is near the "borderline stays out" line.
- due: ok. "2026" gives 2026-12-31.
- verdict: not_yet_due is right.
- notes: **what must change.** The `bar` never says that AI has to be doing the work. As written, any billion-dollar company with one employee would count, for example a holding company, a patent shell or a token project, and some of those may already exist. Since the bar is fixed at entry, it needs a clause along the lines of "whose work is done mainly by AI systems in place of employees" before publishing. Otherwise, drop the claim as borderline. The 70 to 80 percent figure from the press session is rightly left out.

### 2025-05-28-amodei-axios-half-of-entry-level-white-collar-jobs  (cov)  — PASS
- quote (`reported_as`): ok. The reader copy of Axios has, in its first bullet, "AI could wipe out half of all entry-level white-collar jobs — and spike unemployment to 10-20% in the next one to five years, Amodei told us". That matches the file. It is the reporters' paraphrase, as the file says.
- date: ok. The article address is 2025/05/28.
- role: ok.
- admission: ok. It is about AI's effect on jobs, forward-looking and dated. "could" is a hedge, and the method scores hedges at face value.
- due: ok. One to five years from May 2025 gives 2026 to 2030, so `due` 2030 and `due_early` 2026. The bar uses the low end of 10 to 20 percent, which is the generous reading.
- verdict: not_yet_due is right.
- notes: the 2026-01-20 Davos repeat in `repeated_on` covers only the jobs half. In the Davos captions, Minton Beddoes (13:53) quotes "half of entry-level white collar jobs could be gone within the next one to five years" with no unemployment figure, and at 16:40 he says "one to five years as of six months ago I would stick with that". It is a fair repeat, but the notes could say it repeats the jobs half only. Minor.

### 2025-07-30-amodei-20-25-percent-models-stop-improving  (sample)  — PASS
- quote: ok. It is a verbatim run of the captions at 4:43 to 4:51: "20 or 25% chance that sometime in the next 2 years the models just start getting stop getting better".
- date: ok. The upload date is 20250730 (Alex Kantrowitz's channel). The "sitting here in the middle of 2025" remark is at 7:58.
- role: ok.
- admission: ok. It is a dated forecast about AI capability with a stated chance, and `has_probability` is set, so it stays out of the plain count.
- due: ok. Two years from 2025-07-30 runs to July 2027, judged at 2027-12-31.
- verdict: not_yet_due is right.
- notes: none.

### 2026-01-20-amodei-davos-software-engineers-end-to-end-six-to-twelve-months  (sample)  — PASS
- quote: ok. It is verbatim in the World Economic Forum upload's captions at 2:03 to 2:12: "we might be 6 to 12 months away from when the model is doing most maybe all of what SWES do end to end".
- date: ok. The upload is dated 20260120 on the World Economic Forum channel.
- role: ok.
- admission: ok. It is hedged ("I don't know, we might be"), and hedges are scored at face value.
- due: ok. The span ends in July 2026 to January 2027, so `due` 2027 and `due_early` 2026.
- verdict: not_yet_due is right.
- notes: the bar's list ("setting up, testing, deploying and documenting") spells out "end to end". It is reasonable and should stay as written.

### 2026-02-13-amodei-continual-learning-next-year-or-two  (sample)  — PASS
- quote: ok. It is verbatim in the episode transcript under "00:29:42 - Is continual learning necessary? How will it be solved?". The line ends his answer that begins "Two, is this idea of continual learning".
- date: ok. The page says "Feb 13, 2026".
- role: ok.
- admission: ok.
- due: ok. February 2027 to February 2028, so `due` 2028 and `due_early` 2027.
- verdict: not_yet_due is right.
- notes: right after the quote he says one route is "just to make the context longer". When this comes due, someone may argue that a very long memory within one conversation counts as "solving" learning on the job. The bar ("keeps learning from its own work after deployment ... over weeks without being retrained") is worded tightly enough to decide that case, and should be left as it is.

### 2026-06-10-amodei-policy-powerful-ai-if-scaling-continues-one-or-two-years  (sample)  — PASS
- quote: ok. It is verbatim in the second paragraph (curly apostrophe included).
- date: problem, minor. The page says only "June 2026", and the page source carries no published date. 2026-06-10 is the first Hacker News submission, which is the latest date it could have been posted, not a confirmed one. Under the method, `when = "2026-06"` with the Hacker News date in `when_note` would be more honest. This changes no count.
- role: ok.
- admission: ok.
- due: ok. June 2027 to June 2028.
- verdict: unfalsifiable stands under the ruling, because the post names powerful AI without defining it in its own text. Two points:
  1. The second reason in `verdict_why` ("conditional on scaling laws continuing, which has no agreed test") goes against the method's rule on conditions: a condition is kept in the bar, the claim is scored on its date, and the verdict says whether the condition held. That reason should be dropped, leaving the undefined stage as the only one.
  2. For John's awareness: the post links "a country of geniuses in a datacenter" to his essay Machines of Loving Grace, where powerful AI is defined in detail. The same post also describes it in passing: "If AI achieves the ability to do most cognitive tasks far better than humans". Under "defines in that source", a link is not a definition, so the status holds. The ledger already treats the 2025-04-24 interpretability post's "country of geniuses" claim the same way, so it is consistent. But it is a close call.
- notes: none.

### 2026-09-12-amodei-pace-swarm-could-take-over-internet-six-to-twelve-months  (sample)  — FAIL
- quote: ok. It is verbatim in the paragraph beginning "My second concern is the OpenAI-Hugging Face incident (OAI-HF)".
- date: problem, minor. The page says only "September 2026", and 2026-09-12 is the Hacker News submission date. The same point as the policy post above applies.
- role: ok.
- admission: acceptable. It is framed as a worry ("it's my worry that in 6–12 months such a swarm could be capable"). The method scores hedges at face value, so it gets in, though it is near the edge.
- due: ok. March to September 2027 gives 2027, and `due_early` is not needed.
- verdict: not_yet_due is right.
- notes: **what must change.** The `bar` waters down the words. He said "taking over the entire internet with a persistent botnet". The bar says "taking control of computers across the internet at large scale and keeping that control". A large botnet would meet the bar as written but not his words. The bar should keep "the entire internet" (or at least "most of the internet"), and should keep "such a swarm", meaning one with similar misbehaviour, since the bar is fixed at entry. The OpenAI-Hugging Face incident he describes is still unchecked, as the notes say.

### 2023-05-02-hassabis-agi-few-years-maybe-decade  (cov)  — PASS
- quote (`reported_as`): ok. Fortune (Tristan Bove, May 3, 2023, 5:32 PM ET) prints "So I think we could be just a few years, maybe within a decade away." as his direct quote. The words before it are "I think we'll have very capable, very general systems in the next few years". "AGI" is Fortune's framing; it is not in the quoted words.
- date: ok. Fortune says he spoke "Tuesday", and Tuesday before 2023-05-03 is 2023-05-02. No recording from the Wall Street Journal was found by me either.
- role: ok. He was chief executive of DeepMind, which became Google DeepMind in April 2023.
- admission: ok, as coverage only.
- due: ok. "within a decade" gives 2033.
- verdict: unfalsifiable is right, because AGI is not defined in the report. But the first reason in `verdict_why` ("A possibility ('could be'), not a forecast") goes against the method: hedges such as "could" are scored at face value. The same file set scores Amodei's Axios "could" claim, so this is inconsistent. That reason should be dropped, keeping only the undefined stage. It changes no count.
- notes: none.

### 2023-12-06-hassabis-bard-advanced-early-next-year  (hits)  — PASS
- quote: ok. It is verbatim in "Gemini Ultra coming soon", inside the section headed "By Demis Hassabis, CEO and Co-Founder of Google DeepMind, on behalf of the Gemini team". The page is dated Dec 06, 2023.
- date: ok.
- role: ok.
- admission: ok. It is a dated product launch.
- due: ok. "Early next year" gives 2024-03-31.
- verdict: ok. The Google blog post of Feb 08, 2024 says "Today we're launching Gemini Advanced — a new experience that gives you access to Ultra 1.0", and "available today in more than 150 countries and territories". Every condition is met: a public launch, access to Ultra, before 2024-03-31. `verdict_on` 2024-02-08 is right, and `evidence_by` "maker" is honest.
- notes: none.

### 2023-12-06-hassabis-gemini-ultra-developers-enterprise-early-next-year  (hits)  — FAIL (judgement call for John)
- quote: ok. It is verbatim in the same section. The full sentence: "we'll make Gemini Ultra available to select customers, developers, partners and safety and responsibility experts for early experimentation and feedback before rolling it out to developers and enterprise customers early next year."
- date: ok.
- role: ok.
- admission: ok.
- due: ok, 2024-03-31.
- verdict: problem. The verdict source, Google Cloud's post of February 15, 2024, says only "Gemini 1.0 Ultra ... is now generally available on Vertex AI for customers via allowlist". The promise contrasts limited access for "select customers, developers" with a later roll-out to developers in general. Access by allowlist is still the limited, by-invitation kind, so the developer condition is not shown met by this record. I found no record of open developer access to 1.0 Ultra (through the Gemini API or AI Studio) by 2024-03-31. The business half is better supported by another record: Google Workspace's post of 2024-02-21 says Gemini Business and Gemini Enterprise include a chat "built on our 1.0 Ultra model" (https://workspaceupdates.googleblog.com/2024/02/gemini-for-google-workspace.html). That record should be added either way. **What must change:** either find a dated record of open developer access by 2024-03-31, or score the claim `missed`, naming the gap (developers got Ultra only by allowlist) with direction `not_come`. If John accepts allowlist access as a staged roll-out, keep it as a hit, but the verdict should then cite the Workspace record for the business half.
- notes: `evidence_by` "maker" is honest.

## Summary

PASS 7, FAIL 3, COULD NOT VERIFY 0.

- **The one-person billion-dollar company claim (Amodei, 2025-05-22):** the bar does not require that AI does the work, so a non-AI one-employee company would count. Add that condition, or drop the claim as borderline: the words never mention AI.
- **The AI swarm taking over the internet claim (Amodei, 2026-09-12):** the bar softens "taking over the entire internet" to "at large scale". Restore his words.
- **The Gemini Ultra for developers and businesses claim (Hassabis, 2023-12-06):** the hit rests on allowlist-only developer access, which is the limited access the post said would come before the roll-out. Find a record of open developer access by 2024-03-31, or rescore as missed. Either way, add the Workspace record of 2024-02-21 for the business half.

Minor fixes that change no count:
- The two darioamodei.com posts carry Hacker News submission dates as full `when` dates. The pages give only the month, so `YYYY-MM` would be more honest.
- Two unfalsifiable `verdict_why` texts give a reason the method does not allow: the policy post's "conditional" reason and Hassabis's "could be" reason. Drop those reasons and keep the undefined-stage reason in each.

## Batch 3

# Batch 3 results: independent check of ten claim files (Hassabis 4, Huang 6)

Checked 2026-10-19. Sources opened with curl, the r.jina.ai reader (electrive, CNBC) and
yt-dlp captions (official uploads). Nothing in the repository was edited.

### 2024-12-11-hassabis-gemini-2-more-google-products-early-next-year  (hits)  — PASS
- quote: ok. Verbatim on the page, in the section under the byline "By Demis Hassabis, CEO of Google DeepMind and Koray Kavukcuoglu, CTO of Google DeepMind on behalf of the Gemini team", heading "Gemini 2.0 available in Gemini app, our AI assistant". It is not in Sundar Pichai's opening message (which is a separate section of the same post).
- date: ok (page date line "Dec 11, 2024").
- role: ok (chief executive of Google DeepMind).
- admission: ok (a product ship with a date).
- due: ok under the Q1 reading of "early next year" (see the note on "early" under the Gemini 2.5 claim below).
- verdict: ok. The AI Mode post, dated "Mar 05, 2025" (Robby Stein, Google Search), says "we've launched Gemini 2.0 for AI Overviews in the U.S." Search is a further Google product; inside Q1; evidence is Google's own (maker), correctly marked.
- notes: the post is co-signed and written "on behalf of the Gemini team"; `own_words` is a fair label but the notes could say it is a team post under his byline. The verdict date is the announcement date of a launch that may have happened a little earlier; that only helps the hit.

### 2025-04-20-hassabis-2030-system-understands-everything  (sample)  — PASS
- quote: ok. Verbatim in the Internet Archive copy of 2025-04-23, as Hassabis's answer to Pelley's "And in 2030 you will have what?".
- date: ok (60 Minutes broadcast 2025-04-20).
- role: ok.
- admission: ok (dated, forward, about AI).
- due: ok (2030).
- verdict: ok. "Really understands everything around you in very nuanced and deep ways" names no comparison or measure; "embedded in your everyday life" has no scale. `unfalsifiable` follows the rule.
- notes: none.

### 2025-05-20-hassabis-gemini-25-flash-generally-available-early-june  (hits)  — FAIL (needs a ruling on "early" before publishing)
- quote: ok. Captions at 00:20:21–00:20:25: "I'm excited to say that Flash will be generally available in early June with Pro soon after." The segment runs from Pichai's handover (about 18:03) to "Thanks, Demis" (22:15), so it is Hassabis speaking.
- date: ok (upload 2025-05-20, the keynote day).
- role: ok.
- admission: ok.
- due: problem. The method's month rule covers "in June"; the words are "in early June", a narrower point, and the method has no rule for "early". The ledger reads "early" three different ways: Hassabis's own "early next year" claims (this batch's Gemini 2.0 claim, and the Bard Advanced and Gemini Ultra claims of 2023-12-06) are read as the first quarter, the narrow reading; Zuckerberg's two "early next year" claims and Suleyman's Copilot Vision claim are read as the first half, the generous one; and here "early June" is read as the whole month, the most generous of all. Read the way his own "early next year" is read (the first part of the period, so roughly 2025-06-10), general availability on 2025-06-17 is a week late and the status would be `missed`, direction `later`.
- verdict: the Google post of 2025-06-17 does say "Gemini 2.5 Flash and Pro are now generally available" (maker, correctly marked). Before 06-17 Flash was in preview only. Whether that is a hit depends wholly on the reading of "early".
- notes: what must change: the owner rules once how "early <period>" is read, and this claim and the six "early next year" claims are brought into line. This claim's verdict may flip.

### 2025-05-23-hassabis-agent-fleets-four-or-five-years  (sample)  — FAIL
- quote: ok. Captions at 01:02:14–01:02:22: "does that become part of the normal job process? I could imagine that in the next four or five years."
- date: ok (upload 2025-05-23).
- role: ok.
- admission: problem. In context (01:02:00 onward) he is listing what "economists and other experts should be working on": "does everyone have ... a fleet of agents ... does that become part of the normal job process? I could imagine that in the next four or five years." That is a question for others to study plus "I could imagine", which is a possibility and not a forecast. The file says this itself ("A possibility ('I could imagine') ... missing the date would prove nothing"). The rulings say hypotheticals are out and borderline cases stay out. Entering it as `unfalsifiable` is not the same as leaving it out, because it adds one to his "cannot be tested" count.
- due: arithmetic ok (2030, early end 2029), but moot.
- verdict: should not be scored at all.
- notes: what must change: remove the claim record and say in its search-log row (the Hard Fork episode row, `hassabis-claims-006`) that it was left out as a possibility, not a forecast. This lowers Hassabis's "cannot be tested" count by one.

### 2016-09-28-huang-self-driving-cars-on-road-couple-of-years  (hits)  — PASS
- quote: ok. Captions at 01:53:00–01:53:07: "going to see some self-driving cars get on the road here in the next next year or make no no more than next year and no more than the next couple of years". The quote is a verbatim run of those caption words.
- date: ok (upload 2016-09-29; the keynote was 2016-09-28).
- role: ok (Nvidia chief executive).
- admission: ok, though it is an aside inside a DriveWorks software announcement ("even though we're going to see..."). It looks forward and gives a length of time.
- due: ok (range 2017 to 2018; due 2018, early end 2017).
- verdict: ok. Waymo's post dated November 7, 2017 says "fully self-driving vehicles ... are test-driving on public roads, without anyone in the driver's seat". This is outside Nvidia, so `outside` is right.
- notes: the same Waymo post says Waymo made a "world's first fully self-driving trip on public roads" with nobody in the driver's seat in 2015, before the claim was made. The bar's "operating on public roads" (a fleet, not a single demonstration) is what keeps this from being a thing that had already happened; the notes could say so. The words ("some self-driving cars get on the road") are loose, which makes the hit an easy one.

### 2018-05-10-huang-self-driving-cars-2020-to-2021  (hits)  — FAIL (bar does not use the speaker's own usage in the same source)
- quote: ok. Verbatim in the Motley Fool transcript (fetched directly with a browser user agent), in Huang's answer to Blayne Curtis of Barclays.
- date: ok (call of 2018-05-10, 5:00 p.m. ET).
- role: ok.
- admission: ok.
- due: ok (2021, early end 2020).
- verdict: problem. The sentence just before the quote, in the same answer, reads: "the ASPs for Level 2 could be a few hundred dollars to a Level 5 self-driving car, taxi, or driverless taxi being a few thousand dollars." So in this source he sets "Level 2" against "a Level 5 self-driving car", and then dates "driverless taxis" (2019) and "self-driving cars" (2020 to 2021). The method says the bar is "the speaker's own definition if the same source gives one". His own usage points to a highly automated car (Level 5, or at least far above driver assistance), not a Level 3 system that works only in expressway traffic jams. The bar (Level 3 "at least in some conditions") was written on 2026-10-19, after the Honda result was known, and it is the reading that makes this a hit. Honda's release (dated 2021-03-04) does show lease sales of the Legend with "Traffic Jam Pilot", "qualifying for Level 3 automated driving", beginning 2021-03-05, about 100 cars, in Japan only. Under the same-source reading, no such car was on the market by 2021-12-31, so the status would be `missed`, direction `later` or `not_come`.
- notes: what must change: rewrite the bar from the same-source usage, or get an owner ruling, and record that the Level 5 sentence was weighed. The file's notes already admit a stricter reader "would mark it missed", but they do not mention that the stricter reading comes from his own words. Also minor: the verdict source is a release issued the day before sales began. It announces the event in advance and is not a record of the sale itself.

### 2021-04-12-huang-multi-trillion-parameter-models-2022  (hits)  — PASS
- quote: ok. The uploaded captions at 00:50:04 give it exactly: "We expect to see multi-trillion-parameter models by next year, and 100 trillion+ parameter models by 2023."
- date: ok (upload 2021-04-12).
- role: ok.
- admission: ok, a forecast about AI models, not hardware. It is close to a compute-scale forecast, but it names models.
- due: ok (2022).
- verdict: ok. arXiv 2110.03888 (M6-10T), "Submitted on 8 Oct 2021", reports "pretraining unprecedented 10-trillion-parameter model ... on solely 512 GPUs within 10 days". It comes from Alibaba, so `outside`; `sooner` is fair.
- notes: "multi-trillion" read as at least two trillion is a fair plain reading.

### 2024-03-18-huang-self-driving-in-mercedes-end-2024-early-2025  (sample)  — PASS
- quote: ok. Captions at 01:45:05–01:45:11: "self-driving application at the end of this year or I guess beginning of next year we will be shipping in Mercedes".
- date: ok (upload 2024-03-18).
- role: ok.
- admission: ok.
- due: ok. "Beginning of next year" is read as the first quarter, 2025-03-31. That matches the Q1 reading used for Hassabis's "early next year", subject to the same ruling on "early" asked for above. A first-half reading would not change the verdict.
- verdict: ok. The Mercedes release of 2025-04-29 opened CLA orders in Germany and Europe; electrive (2025-06-04, via the reader; the direct page is behind Cloudflare) reports the confirmation of series production at Rastatt. Both are after 2025-03-31. `missed`, `later` is right.
- notes: the earlier Mercedes chain claim this one restates (Hyperion 8 in Mercedes cars in 2024, `2022-03-22-huang-hyperion-8-in-mercedes-cars-2024`) exists.

### 2024-06-02-huang-mercedes-self-driving-production-2025  (hits)  — FAIL (evidence mark and verdict source)
- quote: ok in substance, at 01:42:30–01:42:40. The punctuated English (US) caption track of the official upload reads "Next year we're going to go to production with the Mercedes fleet. And after that, in 2026, the JLR fleet". The file's "the jlr Fe Fleet" is the automatic captions' mishearing. Prefer the clean track.
- date: ok (upload 2024-06-02).
- role: ok.
- admission: ok.
- due: ok (2025-12-31).
- verdict: problem. The verdict source named, electrive of 2025-06-04, shows CLA series production but never mentions Nvidia. The Mercedes release of 2025-04-29 does not mention Nvidia either; the search-log row's phrase "with Nvidia's driving software" is the helper's wording, not the release's. The only record that the production CLA runs Nvidia's software is Nvidia's own blog of 2026-01-05 ("introduces advanced driver-assistance features powered by NVIDIA's full-stack DRIVE AV software"). The file's own notes say so ("rests on Nvidia's own blog"), and the sibling claim of 2025-05-19 (Mercedes self-driving stack around the world in 2025), which rests on the same blog, is marked `maker`. Under the method, `evidence_by` must be `maker` here, not `outside`.
- notes: what must change: set `evidence_by = "maker"`, and name the Nvidia blog in `verdict_source` beside electrive. Also flag for the owner that the hit is softer than it looks. The same Nvidia post is headlined "NVIDIA DRIVE AV Software Debuts in All-New Mercedes-Benz CLA" and speaks of a "production launch ... in the US this year" (2026). Electrive of 2026-01-07 says that in China the CLA's system is Momenta's, and that "in the US, and potentially in Europe in the future, Mercedes is partnering with Nvidia". So no source outside Nvidia shows Nvidia's software in cars produced in 2025. The bar also adds "(driver-assistance)" to a sentence about Nvidia building "the entire stack" for self-driving cars; that reading should be stated as a judgement in the notes. The CES repeat in `repeated_on` drops "starting with this" from the caption run ("coming with Nvidia starting with this starting this year going to production"). That is harmless, but an ellipsis is owed.

### 2025-03-18-huang-all-nvidia-software-engineers-ai-assisted-2025  (hits)  — PASS
- quote: ok. Captions at 01:45:59–01:46:04: "100% of Nvidia software Engineers will be AI assisted by the end of this year".
- date: ok (upload 2025-03-18).
- role: ok.
- admission: ok, though borderline. It is a forecast about AI use inside his own company, a goal wholly in Nvidia's control. It is not a budget or headcount figure, so it is not excluded.
- due: ok (2025-12-31).
- verdict: ok on the maker's word, correctly marked `maker`. The CNBC transcript (published 2025-10-08) has Huang saying "every one of our engineers, 100% is now assisted by AI coders".
- notes: the same interview, a few answers later, says of Cursor: "All of our engineers use it. We have some 40,000 engineers. Almost every one of them are going to use it". That can be squared with the bar (it is about Cursor in particular, while the 100% is about "AI coders" in general), but `verdict_why` should mention it so a reader does not find it first. "Engineers" there is all engineers, not only software engineers; that is harmless.

## Summary

PASS 6, FAIL 4, COULD NOT VERIFY 0.

- Gemini 2.5 Flash generally available "in early June" (Hassabis): the hit depends on reading "early June" as the whole month, while his own "early next year" claims are read narrowly (first quarter) and others' broadly (first half). This needs one ruling on "early"; under the narrow reading, availability on 2025-06-17 is a miss.
- Fleets of agents "I could imagine ... in the next four or five years" (Hassabis): a possibility put as a question for economists, so it should be left out under the hypothetical and borderline rules, not counted as "cannot be tested".
- Self-driving cars "between 2020 and 2021" (Huang): in the same answer he calls them "a Level 5 self-driving car" in contrast to Level 2. The bar (Level 3 in traffic jams, met by about 100 leased Honda Legends) ignores that usage; read from his own words, it is likely a miss.
- Mercedes fleet "to production" in 2025 (Huang): the evidence that the cars run Nvidia's software is Nvidia's blog alone, so `evidence_by` must be `maker`, not `outside`, and that blog belongs in `verdict_source`. The hit is also softer than shown, since electrive says Nvidia's system launches in the US in 2026 and only "potentially" in Europe.

## Batch 4

# Batch 4 results: Yann LeCun claims (checked 2026-10-19)

Captions were read from yt-dlp downloads (automatic English captions) into the scratch area; upload dates from `yt-dlp --print upload_date`. Web pages read with WebFetch and curl. All search-log ids named by the ten files exist in `data/search_log.csv`.

One finding touches the three files from his AMI Labs period (2026-01, 2026-03-10, 2026-04-01): the notes call him AMI's "executive chairman". His own post of December 2025, as quoted in coverage (TechCrunch, Fortune), says "I'm the Executive Chairman". But the AFP report this batch uses as a source (2026-03-10, carried by Macau Business) says "He now serves as AMI's non-executive chairman". Either way he is a chair, so admission does not change. But the sources disagree, so the notes should cite the source for the title, or simply say "chairman". The authors already flagged whether AMI Labs counts as "a company building frontier AI models"; that question is still open for the lead.

---

### 2023-01-25-lecun-teenagers-train-image-models-within-two-years.toml  (sample)  — FAIL
- quote: ok. The captions at 59:28 read "because within a year or two you know any teenager in the parents basement is going to be able to do this". The locator is right.
- date: ok. Upload date 20230125.
- role: ok. Meta's Chief AI Scientist.
- admission: problem (borderline). "Do this" refers to what "a large tech company in California" does with artists' work, said as an aside in an argument about copyright policy. The `prediction` says "train their own image-making models on art found on the internet". Those words come from a later, undated sentence about 30 seconds on ("eventually everybody is going to be able to use this ... and train their own models"), not from the dated "within a year or two" sentence.
- due: ok. A range from 2024 to 2025: due 2025, early end 2024.
- verdict: problem. The miss depends on conditions the bar adds that are not in his words: "home equipment", a model "of their own", and "adapting someone else's released model ... does not meet it". The words say a teenager will "be able to" do it. On a plain reading, the verdict source shows that ability: Hugging Face's guide of 2023-01-26 fine-tunes Stable Diffusion on one consumer card (an 11 GB 2080 Ti) in about five hours, and in 2023 individuals widely fine-tuned the model on particular artists' styles. The `missed` / `not_come` verdict rests on finding no record of a person training a model from scratch at home, which is a narrower test than "be able to do this". The notes also say the verdict was flipped from hit to missed before merging, and the bar's exclusion clause reads as written to fit that flip.
- What must change: either drop the claim as borderline (an aside that does not say clearly what AI will do), or bring the bar to the lead or John as a ruling. Under the plain reading of "be able to do this", the claim is arguably a hit, from outside evidence, dated 2023-01-26.
- notes: `evidence_by = outside` is fine.

### 2024-04-09-lecun-not-surpass-human-intelligence-next-year.toml  (hits, cov)  — PASS
- quote (reported_as): ok. TNW, Thomas Macaulay, published 2024-04-10 10:10 UTC, has verbatim: "Eventually, machines will surpass human intelligence… it's gonna take a while though," and "It's not just around the corner — and it's certainly not next year like our friend Elon has said." These are direct quotes of LeCun.
- date: ok. "On Tuesday", in a piece published 2024-04-10 (a Wednesday), gives 2024-04-09. The statement row is dated 2024-04-10, the same month.
- role: ok. Meta's Chief AI Scientist.
- admission: ok. A dated negative claim about a named comparison; coverage only, and marked so.
- due: ok. "Not next year", said in April 2024, means 2025; judged 2025-12-31.
- verdict: ok, with a caveat. The World Economic Forum video (IgifEgm1-e0, uploaded 20260122) has Musk at 30:33–30:38 saying "we might have AI that is smarter than any human by the end of this year and I would say no later than next year". That matches the file. For a "will not happen" claim the verdict has to rest on absence, so a later statement by the leading claimant is a reasonable dated record. Still, it is a statement, not "a dated primary record of the event itself", so the lead may want a note saying a negative claim is settled by absence.
- notes: `evidence_by = outside` is honest (Musk is not at Meta).

### 2024-10-16-lecun-human-level-ai-not-in-next-year-or-two.toml  (sample)  — PASS
- quote: ok. The fxtwitter mirror shows the post created "Wed Oct 16 15:31:08 +0000 2024", and its last line is verbatim "In any case, it's not going to be in the next year or two."
- date: ok.
- role: ok.
- admission: ok.
- due: ok. Two years from the day said runs to 2026-10, judged 2026-12-31. The repeat on 2024-11-27 is confirmed in the People by WTF captions at 1:15:40 ("it's not going to happen next year. It's not going to happen in two years"), with the same due year.
- verdict: ok. "Human-Level AI" is not defined in the post, so the claim cannot be tested.
- notes: none.

### 2024-10-16-lecun-human-level-ai-several-years-if-not-decade.toml  (sample)  — PASS
- quote: ok. This is the first line of the same post, verbatim.
- date: ok.
- role: ok.
- admission: ok.
- due: ok. Due 2034, early end 2027, by the range rule.
- verdict: ok. The claim cannot be tested: the stage is undefined, and the words set a minimum time, not a deadline.
- notes: none.

### 2024-11-27-lecun-open-source-platforms-dominate-in-five-years.toml  (sample)  — PASS (admission flagged)
- quote: ok. The captions at 1:26:47–1:26:50 read "So five years from now the world is going to be dominated by open source platforms", followed by the Linux comparison.
- date: ok. Upload date 20241127.
- role: ok.
- admission: borderline, for the lead. He gives this answer to "what would an investor benefit from investing into", and it is a forecast of market structure (which kind of AI platform wins), not of what AI will do or reach. By the "borderline cases stay out" rule it could reasonably be left out, as the Zuckerberg, Pichai and Nadella passes left out market forecasts. If it stays in, the bar's "share of usage or deployments ... clearly more than half" should name one measure. As written it leaves a later reader free to choose the count.
- due: ok. 2029.
- verdict: ok. Due 2029, so not yet due.
- notes: none.

### 2025-01-23-lecun-llms-not-central-within-five-years.toml  (sample)  — PASS
- quote: ok. The captions at 26:01–26:17 read "the shelf life of the current Paradigm uh large language model is fairly short probably 3 to five years I think within five years nobody in the right mind would use them anymore at least not as kind of the central component of an AI system". The quote is verbatim.
- speaker: ok. The caption "my colleagues and I ADM" is a mishearing of "at Meta", which confirms it is LeCun speaking.
- date: ok. Upload date 20250123.
- role: ok.
- admission: ok.
- due: ok. Due 2030, early end 2028.
- verdict: ok. Not yet due.
- notes: the repeat on 2025-10-27 ("within five years or so") gives the same due year, so treating it as an unchanged repeat is right. The Seoul source was not opened in this check.

### 2025-03-18-lecun-world-models-small-scale-three-to-five-years.toml  (sample)  — PASS
- quote: ok. The captions at 9:09–9:14 read "probably going to have a good handle on getting this to work at least at a small scale within three years three to five years". The quote is verbatim.
- date: ok in substance, but the record is weak. The day rests on a TechCrunch preview that was not opened. A search confirms GTC ran 2025-03-17 to 2025-03-21 and that TechCrunch put the talk on the Tuesday, which was 2025-03-18. Nvidia's upload is dated 20250410.
- role: ok.
- admission: ok.
- due: ok. Due 2030 (2028 to 2030).
- verdict: ok. "A good handle" is his own judgement, and "small scale" names no size, so the claim cannot be tested.
- notes: none.

### 2026-01-lecun-smarter-than-humans-not-within-two-years.toml  (sample)  — PASS
- quote: ok. The captions at 0:31–0:40 read "machines that would be smarter than humans at some point. It's not going to happen next year. It's not going to happen in two years".
- date: ok. A month only. The Forbes upload is 20260128 and says the talk was recorded at the Davos summit.
- role: see the AMI note at the top (executive or non-executive chairman). He was chair in either case.
- admission: ok.
- due: ok. 2028.
- verdict: ok. Not yet due. Reading "smarter than humans" as a comparison follows the ruling.
- notes: minor. The bar says "before the end of January 2028", but the claim is judged at 2028-12-31. That is fine for a "will not happen" claim, but the page should make clear the test window ends January 2028.

### 2026-03-10-lecun-ami-fairly-universal-systems-three-to-five-years.toml  (cov)  — PASS
- reported_as: ok. The Macau Business carry of AFP, dated 10 Mar 2026, has verbatim: "Within three to five years, AMI plans to produce 'fairly universal intelligent systems' that could be used for almost any task requiring intelligent machines, such as autonomous driving and robotics, LeCun said."
- date: ok.
- role: problem in the notes. The same AFP article calls him "AMI's non-executive chairman", but the notes say "executive chairman" (see the top note). He qualifies as chair either way.
- admission: ok as a company plan (`is_goal`), marked coverage only.
- due: ok. Due 2031, early end 2029.
- verdict: ok. Not yet due.
- notes: none.

### 2026-04-01-lecun-not-human-level-within-five-years.toml  (sample)  — PASS
- quote: ok. The captions at 24:33–24:44 read "at the very best, we might be convinced that we're on a good path towards human level intelligence, but not yet at human intelligence within five years." The quote is verbatim.
- date: ok. Upload date 20260402, and 2026-04-01 was a Wednesday.
- role: the AMI note at the top applies.
- admission: ok. The same passage defines the stage ("surpass humans in all domains where humans are intelligent").
- due: ok. 2031.
- verdict: ok. Not yet due.
- notes: minor. The same passage repeats "not going to happen in two years" (due 2028 from April 2026), an unchanged repeat of the January 2026 claim. That claim should get `repeated_on = [2026-04-01]` rather than be treated as absorbed. Also, "restates ... with the date moved from 2028 to 2031" overstates it: he kept the two-year claim and added a longer five-year floor. This does not change any count.

---

## Summary
- PASS: 9 (one has an admission question flagged for the lead: the open-source claim of 2024-11-27)
- FAIL: 1
- COULD NOT VERIFY: 0

FAIL:
- The teenagers and image models claim of 2023-01-25: its "missed" verdict depends on bar conditions not in his words (home equipment, built from scratch, fine-tuning excluded), and its prediction borrows "train their own models" from a later, undated sentence. Either drop it as borderline or rule on the bar; under the plain reading of "be able to do this" it is arguably a hit (Hugging Face's guide of 2023-01-26 shows a model fine-tuned on one consumer card).

Also fix: the three AMI-period files call him "executive chairman", but the AFP source they use says "non-executive chairman". Name the source for the title, or just say "chairman".

## Batch 5

# Batch 5 results: claims-ledger source check (2026-10-19)

All sources were opened on 2026-10-19: vetta.org (curl with a full browser user agent, since the
short one got a 403 refusal), greaterwrong.com, the TED transcript (r.jina.ai reader copy) and the
TED page data, chinatalk.media, 36kr.com, the Internet Archive copy of the New York Times,
podscripts.co, YouTube captions (yt-dlp) for four videos, the api.fxtwitter.com mirror, x.ai,
Microsoft's transcript (Word file), BleepingComputer and Microsoft's own security blog (reader copy).

### 2010-12-10-legg-human-level-agi-mean-2028  (sample)  — PASS
- quote: ok. "decided to play it safe and keep the prediction unmoved at 2028." is verbatim in the paragraph named.
- date: ok. The header reads "Posted on 10 December, 2010".
- role: doubtful, already flagged for John. DeepMind was about four weeks past its launch and a handful of people. Calling it "a company building frontier AI models" in 2010 is a judgement. The rule says borderline cases stay out. This applies to all four 2010–2011 Legg claims, and John should rule on it once for all of them.
- admission: ok, apart from the role question. It looks forward, carries a year, and is his own words.
- due: ok (2028, judged 2028-12-31).
- verdict: not yet due; ok.
- notes: The bar says "The post defines nothing beyond 'roughly human level'". But the same page carries Legg's own comment of 2010-12-18. In it he describes the test he expects: people's intuitive verdict that the system is "actually fairly intelligent", with "a significant proportion of the population" saying so "by the late 2020's or early 2030's". This should be mentioned in the notes. It changes no count, since the claim is not yet due. The bar's last clause, "or his own word that it has arrived", makes the speaker a judge of his own claim. The method treats that as a sign of an untestable claim, so it is better dropped from the bar. Three repeats were checked at their sources: TED (recorded 2023-10-17), the post on X (2024-12-13 07:49 UTC) and the 2025 podcast at 49:31. The Dwarkesh repeat (2023-10-26) was found in its transcript. All four are as stated.

### 2011-06-17-legg-ninety-percent-by-2050  (sample)  — PASS
- quote: ok. "Shane Legg: 2018, 2028, 2050" is his answer to Q1. Q1 asks for the 10%/50%/90% chance years and carries the "no global catastrophe" condition, which the prediction keeps.
- date: ok. The post's date line is "17 Jun 2011 8:58 UTC". It was an email question-and-answer, so the answers were written on or shortly before that date.
- role: same doubt as above. The notes give the role only as "Role as in 2011-06-17-legg-ten-percent-by-2018" (a pointer to another claim file), but the method says each claim's notes name the role. They should name it here.
- admission: ok.
- due: ok (2050).
- verdict: not yet due; ok.
- notes: In his Q3 answer in the same source, Legg says "'human level' is a rather vague term". The plain-reading bar stands under the named-comparison ruling, but the notes could mention this. The restatement link to the 2010 "95% at 2045" claim is fair. That target file's name says "90-percent-by-2045" while the 2010 post puts 2045 at the 0.95 point; this is outside my batch but worth checking.

### 2011-12-31-legg-proto-agi-within-eight-years  (sample)  — FAIL
- quote: ok, verbatim. The date line and his comments of 2011-12-31 and 2012-01-02 are there.
- date: ok.
- role: same doubt as the 2010 claim.
- admission: ok, apart from the role question.
- due: ok (2019).
- verdict: problem, on two counts.
  1. The `verdict_why` uses his 2012-01-02 remark that the prediction "might be impossible to falsify" as support for "no outsider can test it". His stated reason in that comment is different: a military that built such a system would keep it secret. He is not saying the claim has no test. As written, the remark is misrepresented and must be reworded.
  2. The post itself defines "proto-AGI" in the same source. It is one system with basic vision, sound processing, movement control and language, all learnt rather than programmed, able to solve a range of simple problems, including new ones. His comment of the same day ("a list of specific capabilities ... would somewhat miss the point") refuses a more detailed list. It does not withdraw the post's definition. The method takes the speaker's own definition from the same source as the bar. That definition is a test an outsider could run, even if it is loose. Under the 2026-10-19 bar ruling, then, `unfalsifiable` is doubtful, and the claim may need scoring. The file's own notes say it would "likely" be missed. This moves a claim from "cannot be tested" to a scored miss, so it needs John's ruling before publishing. If it is scored, a settling record has to be opened; none has been.
- notes: The "acid test" quote is accurate.

### 2023-10-17-legg-agi-not-next-year-or-year-after  (hits)  — FAIL
- quote: ok. TED's official transcript has "I don't think it's coming next year or the year after. It's probably a little bit further out than that." just before Anderson's "2028?".
- date: ok. The TED page data has "recordedOn":"2023-10-17" and "publishedAt":"2023-12-07".
- role: ok. Co-founder and chief AGI scientist of Google DeepMind.
- admission: problem. Admission rule 2 needs words saying AI will do, reach or ship something. These words say only that it will not come in 2024 or 2025. That is a lower bound, scored here as a hit. The file itself flags this as a judgement for John, against an earlier brief that treats lower bounds as untestable. Under "borderline cases stay out" it should not be counted as a hit until John rules. As it stands it adds one hit to Legg's count.
- due: ok (2025-12-31).
- verdict: if admitted, the evidence holds up. The `verdict_source`, the Google DeepMind podcast (uploaded 2025-12-11, video l3u_FAv33G0), has "we're not there yet" at 7:03 for minimal AGI. `evidence_by = maker` is honest, since it is the speaker's own later word. The `verdict_on` (2025-12-31) is the due date rather than the date of the record (2025-12-11), which suits a "not before" claim.
- notes: The bar uses his definition from the same talk, which is right if the claim is admitted.

### 2024-07-22-liangwenfeng-agi-two-five-or-ten-years  (sample)  — PASS
- quote: ok. ChinaTalk's English, verbatim: "It could be two, five, or ten years–in any case, it will happen in our lifetimes." The 36Kr original has "可能是2年、5年或者10年，总之会在我们有生之年实现", which matches.
- date: ok. The 36Kr page is dated 2024-07-22, and ChinaTalk's post_date is 2024-11-27.
- role: ok. Founder and chief executive of DeepSeek.
- admission: ok. It is dated (the spans), and the hedge "could" is kept in the prediction.
- due: ok. 2034 is the later end, with due_early 2026.
- verdict: ok. The interview never defines AGI; "natural AGI testing grounds" and "might also be a requirement for AGI" are not definitions. So `unfalsifiable` follows the ruling.

### 2024-04-12-mensch-workplace-revolution-in-two-years  (cov)  — PASS
- quote: ok. The `reported_as` text matches the archived Times article word for word, and the byline is Alderman and Satariano.
- date: ok as the publication date (datePublished 2024-04-12T04:01 UTC). As the `when_note` says, the interview was earlier and undated.
- role: ok. Co-founder and chief executive of Mistral AI.
- admission: ok for a coverage-only entry. It is framed as "AI's biggest risk", but "it's coming ... more like in two" is a dated forecast.
- due: ok (2026).
- verdict: `unfalsifiable` ok. There is no measure of a "workplace revolution".
- notes: kind `deployment` is an odd fit, but it changes nothing.

### 2026-01-14-mensch-not-superhuman-in-every-domain-within-two-years  (sample)  — FAIL
- quote: ok. Podscripts at 00:32:55 and the YouTube captions at 30:59 both have "we are / we're not going to make it superhuman in every domain at the same time". The caption has "we're", so the quote's "we are" follows podscripts. That is a small difference.
- date: ok. Episode Date January 14, 2026; YouTube upload 2026-01-16.
- role: ok.
- admission: problem, a borderline case that should stay out or go to John.
  - It is a negative ("we are not going to"), not a claim that AI will do, reach or ship something.
  - The two-year span is read in from the sentence before. That sentence is about the field's focus ("the next two years is going to be about ... a certain skill set"). The superhuman sentence reads as a general view, and the host's follow-up ties it to his undated "you're not going to have a model that can do everything".
  - The date is therefore an inference, not in the words.
  Not yet due, so it does not move a rate, but it adds a claim to Mensch's published list.
- due: follows the method if admitted (2028).
- verdict: not yet due.
- notes: If kept, the notes should say plainly that the span is inferred.

### 2021-08-19-musk-tesla-bot-prototype-next-year  (oldhits)  — FAIL
- quote: ok. The captions have "we think we'll probably have / a prototype sometime next year that / basically looks like this" at 2:07:48 to 2:07:56.
- date: ok. The release timestamp 1629417612 is 2021-08-19 23:40 UTC, 16:40 Pacific.
- role: problem. The notes name no role, though the method says each claim's notes name the role that applied. None of the 14 Musk claim files names one. Here the role would be Tesla's chief executive, with Tesla counting as a company building AI chips and models (the FSD computer, and the Dojo chip shown at this same event). That is a judgement and should be written down.
- admission: problem, borderline. The bar ("a physical Tesla humanoid robot prototype shown in public") holds no AI condition at all. It is a hardware prototype date, and the owner's rules put plain hardware dates out, with borderline cases staying out. As one of the original 30 claims, it counts as a hit. John should rule whether a humanoid robot prototype counts as "AI ships something". If it stays, the bar needs an AI element.
- due: ok (2022).
- verdict: if admitted, the evidence holds up. The Tesla AI Day 2022 captions (released 2022-09-30 Pacific) have "the first time we try this robot without any backup support. Cranes, mechanical mechanisms, no cables" at 17:03, and "humble beginnings" at 19:48. `evidence_by = maker` is honest.

### 2024-07-01-musk-grok-2-in-august  (oldhits)  — FAIL
- quote: ok. The mirror returns "Grok 2, which comes out in August, will be a giant improvement in this regard.", posted Mon Jul 01 04:47:22 +0000 2024, in reply to beffjezos.
- date: problem (minor; no count changes). The method keeps this ledger's dates "in the speaker's own time". 04:47 UTC is the evening of 2024-06-30 in both Texas and California, so `when` should be 2024-06-30. The `when_note` notices this but keeps 07-01. The file name cannot change; the `when` field can.
- role: problem. No role note. The role is founder and head of xAI (founded 2023), which qualifies; the notes should say so.
- admission: ok. It names a model's release date.
- due: ok (due_date 2024-08-31).
- verdict: ok. xAI's page reads "Aug 13, 2024 Grok-2 Beta Release ... We are excited to release an early preview of Grok-2". It also says "𝕏 Premium and Premium+ users will have access". That counts as a release. `evidence_by = maker` is honest.
- notes: The bar leaves out "a giant improvement" at purging AI-written text from training data. That was the point of the post, and the prediction keeps it. Leaving it out is defensible, since it has no measure, but the reason should stay written in the bar, as it is now.

### 2023-07-25-nadella-security-copilot-early-access-this-fall  (hits)  — FAIL
- quote: ok. The transcript reads "Finally, our Security Copilot – the first product to apply this next generation of AI to SecOps – will be available to customers via a paid early access program this fall." The ellipsis is described correctly.
- date: ok. The transcript header reads "Tuesday, July 25, 2023".
- role: ok. Chairman and chief executive, as named on the call.
- admission: ok. An AI product shipping on a stated date.
- due: ok as reasoned (autumn ends 2023-12-21). The method has no rule for seasons, so this is a judgement, but harmless here.
- verdict: the hit stands, but four fields must change.
  1. `verdict_source` should be Microsoft's own post, which is the record of the event: https://www.microsoft.com/en-us/security/blog/2023/10/19/microsoft-security-copilot-early-access-program-harnessing-generative-ai-to-empower-security-teams/ (published 2023-10-19), with "our Early Access Program is now open to qualified customers". BleepingComputer (published 2023-10-22) only relays that post.
  2. `verdict_on` should be 2023-10-19, the date of the announcement, not 2023-10-22, the date of the press report.
  3. `evidence_by` should be `maker`, not `outside`. The only evidence is Microsoft's own announcement. BleepingComputer measured nothing.
  4. The bar leaves out "paid", which is in his words. Neither Microsoft's post nor BleepingComputer says the program was paid. An outside analyst, Directions on Microsoft (in its 2024-03-13 piece on general availability, found by search and not opened), describes it as "paid, private testing via Microsoft's Early Access Program since October 2023". The bar should include "paid", with that record or a Microsoft one opened and cited.

## Summary

PASS 4, FAIL 6, COULD NOT VERIFY 0.

Every quote was found verbatim at its source. None of the FAILs comes from a misquote. They come from these:

- **Legg, proto-AGI within eight years** (`2011-12-31-legg-proto-agi-within-eight-years`): the reason given for "cannot be tested" twists his "might be impossible to falsify" (his reason was military secrecy), and the post defines proto-AGI in the same source, so under the bar rule it may need scoring, likely as a miss. John to rule.
- **Legg, AGI not in the next two years** (`2023-10-17-legg-agi-not-next-year-or-year-after`): a "not before" lower bound is counted as a hit. It is borderline under admission rule 2 (AI "will do" something), and it is already flagged for John, so it should not be published as a hit until he rules.
- **Mensch, not superhuman in every domain** (`2026-01-14-mensch-not-superhuman-in-every-domain-within-two-years`): a negative claim whose two-year span comes from the previous sentence. Borderline, so it should stay out or go to John.
- **Musk, Tesla Bot prototype next year** (`2021-08-19-musk-tesla-bot-prototype-next-year`): the bar is a plain hardware prototype date with no AI condition, so it is borderline under the hardware exclusion and needs John's ruling. There is also no role note.
- **Musk, Grok 2 in August** (`2024-07-01-musk-grok-2-in-august`): no role note, and `when` should be 2024-06-30 under the method's "speaker's own time" rule. The verdict itself is sound.
- **Nadella, Security Copilot early access this fall** (`2023-07-25-nadella-security-copilot-early-access-this-fall`): the verdict rests on a press relay. Use Microsoft's 2023-10-19 post, set `verdict_on` to 2023-10-19, change `evidence_by` from `outside` to `maker`, and add "paid" to the bar with a source for it.

A pattern across batches: none of the 14 Musk claim files names his qualifying role in `notes`, though the method requires it. The 2010–2011 Legg role question (DeepMind as a frontier company weeks after its founding) needs one ruling from John covering all four of those claims.

## Batch 6

# Batch 6 results: independent check of 10 claim files (Nadella 3, Pichai 7)

Checked 2026-10-19. Sources opened: YouTube captions through yt-dlp (three Google I/O keynotes); Microsoft and Alphabet transcript PDFs through curl, with the text pulled out by macOS PDFKit; web pages directly or through the r.jina.ai reader copy. Nothing in the repository was edited.

### 2023-10-nadella-m365-copilot-generally-available-this-year.toml  (hits)  — FAIL
- quote: ok. The words are verbatim in the Microsoft 365 paragraph of the 2023 shareholder letter (read through r.jina.ai).
- date: problem. The letter is signed "Satya Nadella, Chairman and Chief Executive Officer, October 16, 2023" at the foot of the letter. `when_note` says "the page gives no day", which is false. Fix: `when = "2023-10-16"`, and rewrite `when_note` to cite the signature date. The id keeps its "2023-10" form, which is allowed since a file is never renamed, but `when` should be the full date.
- role: ok. He was chief executive from 2014-02-04 and chair from 2021-06-16; the letter itself signs him as Chairman and CEO.
- admission: ok. The words look forward, carry a date ("later this year") and come from his own words. One note: he is restating a launch date Microsoft had already set at the 2023-09-21 event (1 November). Nobody checked whether Nadella himself said "November 1" at that event. If he did, the method's rule for an unchanged repeat would key the claim to 2023-09-21 with `due_date` 2023-11-01. The verdict would not change.
- due: ok (2023).
- verdict: ok. Microsoft's post (published 2023-11-15) says "On November 1, 2023, Copilot for Microsoft 365 became generally available for enterprises". `verdict_on` 2023-11-01 is right.
- notes: `evidence_by = maker` is honest.

### 2024-05-21-nadella-team-copilot-preview-later-this-year.toml  (hits)  — PASS
- quote: ok. Verbatim on page 14 of the official Build 2024 transcript, spoken by SATYA NADELLA.
- date: ok (2024-05-21).
- role: ok.
- admission: ok.
- due: ok (2024).
- verdict: ok. The Ignite 2024 Book of News (event of 2024-11-19) has "Facilitator agent: ... works within Teams meetings and chats ... This agent is in preview" and "Project Manager agent ... in Planner ... This agent is in preview."
- notes: He said "These capabilities will **all** come", and he named three: meeting facilitator, collaborator (in chats) and project manager. The `bar` names only two. The Facilitator's chat role ("In chats, the Facilitator shares a summary of important information") reasonably covers the collaborator, so the hit stands. Still, the bar or the `notes` should say that the collaborator role is taken to be covered by the Facilitator in chats. The Book of News says "in preview" without saying public or private; the bar's "available to customers in preview" allows either.

### 2025-05-19-nadella-sora-on-azure-next-week.toml  (hits)  — PASS
- quote: ok. Verbatim on page 9 of the Build 2025 transcript, spoken by SATYA NADELLA.
- date: ok (2025-05-19).
- role: ok.
- admission: ok, though it is close to the line: it is a launch date for another company's model on Microsoft's cloud. It is still "AI will ship", not a hardware date.
- due: ok (`due_date` 2025-06-01, the end of the following week).
- verdict: ok, but there is a better record. The "What's new" page gives only "May 2025: Sora video generation released (preview)". Microsoft's own Foundry developer blog post "Go from prompt to playback with Sora ... in the video playground" (https://devblogs.microsoft.com/foundry/sora-in-video-playground/) was published 2025-05-29 and introduces Sora in Foundry. Its screenshots are dated 2025-05-28. The Tech Community launch post (https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/unlock-new-dimensions-of-creativity-gpt-image-1-and-sora/4414972) is dated 2025-05-19 and says "Sora, now available in AI Foundry". It was written for the Build keynote day and updated 2025-05-30, so it does not fix the release day on its own.
- notes: Suggested change: `verdict_on = 2025-05-29`, with the devblogs post added as the dated record. Either date falls inside the window, so the verdict and counts are unchanged.

### 2022-05-11-pichai-youtube-auto-chapters-80-million-goal.toml  (sample)  — FAIL
- quote: problem. The quote drops words without marking the gap. The official captions (en-US track, Pichai's segment, 00:11:33 to 00:11:42) read: "With this, we now have a goal to 10x the number of videos with auto generated chapters from eight million today to 80 million over the next year." The file has "...the number of videos with from eight million...". "auto generated chapters" has been cut out, which turns the quote into garbled words put in his mouth. Fix: restore the words. The full run from "we now have" is 26 words, one over the 25-word limit, so start at "a goal": "a goal to 10x the number of videos with auto generated chapters from eight million today to 80 million over the next year" (23 words). Also extend `source_locator` to 00:11:42, since the sentence ends there and not at 00:11:37. The speaker is confirmed as Pichai: his labelled segment starts at caption line 127 and runs until "Thanks, Sundar" at line 1226.
- date: ok (2022-05-11; upload date 20220511).
- role: ok. He was chief executive of Google and Alphabet.
- admission: ok. It is a stated goal for an AI feature (DeepMind's multimodal model making chapters automatically), so `is_goal` is right.
- due: ok. "Over the next year" from 2022-05-11 ends in May 2023, judged at 2023-12-31 under the span rule.
- verdict: weak (flag for the lead). The `verdict_source` (DeepMind's post of 2023-06-16) says auto chapters have been applied to "tens of millions of videos (and counting)". That does not show a shortfall, because 80 million is itself "tens of millions". The miss rests entirely on not finding a record, and the bar was written as "a dated record of at least 80 million". `direction = "not_come"` claims more than the record shows: nothing shows the number was not reached. At minimum, `verdict_why` should say plainly that the June 2023 figure is consistent with either outcome. The lead should consider whether `direction` can honestly be set at all. The status `missed` follows the bar as written, so it is not itself a FAIL.
- notes: `evidence_by = maker` is honest.

### 2023-05-10-pichai-magic-editor-later-this-year.toml  (hits)  — PASS
- quote: ok. Verbatim in the captions at 00:09:19 to 00:09:24 (the file says 00:09:16 to 00:09:23; a small timestamp slip worth fixing). It is in Pichai's labelled segment (his segment starts at line 104 and runs until "SISSIE HSIAO: Thanks, Sundar" at line 1242).
- date: ok (upload 20230510).
- role: ok.
- admission: ok.
- due: ok (2023).
- verdict: ok, with one source fix. The `verdict_source` is Google's post of 2023-10-04, which is an advance announcement ("will all be available on Pixel 8 and Pixel 8 Pro"), not a record that the launch happened. The record is the 2024-04-10 post (https://blog.google/products-and-platforms/products/photos/google-photos-editing-features-availability/): "Last year, we launched Magic Editor on Pixel 8 and Pixel 8 Pro". I confirmed it on the page. `verdict_source` should point at that post, or at both. The verdict is unchanged.
- notes: The Pixel 8 launch date of 2023-10-12 comes from general knowledge; neither Google post gives the day of the launch.

### 2023-10-24-pichai-gemini-models-throughout-2024.toml  (hits)  — FAIL
- quote: ok. Verbatim on page 12 of Alphabet's Q3 2023 transcript, in his answer to Doug Anmuth. The fuller sentence is "we are just really laying the foundation of what I think of as the next-generation series of models we'll be launching all throughout 2024."
- date: ok (2023-10-24).
- role: ok.
- admission: ok.
- due: ok (2024).
- verdict: problem in the evidence, not the outcome. The bar needs "more than one new Gemini model released to the public across 2024", but the only `verdict_source` (2024-12-11) shows one model (Gemini 2.0 Flash, experimental, "available to all Gemini users"). The February 2024 models are asserted in `verdict_why` with no primary source opened. One of them is also misdescribed: Google's own post of 2024-02-15 (https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/) says 1.5 Pro came as "a limited preview ... to developers and enterprise customers", which is not "released to the public". Fix: cite a dated primary record for a second public 2024 release, either the 2024-02-08 Gemini Advanced / 1.0 Ultra post (linked from the 2024-02-15 post, which says "Last week, we rolled out ... Gemini 1.0 Ultra ... starting with Gemini Advanced") or the 1.5 Flash public preview of May 2024. Correct the 1.5 Pro wording. Once that is done, `verdict_on` should arguably be the date the bar was first met by two public releases, not 2024-12-11. The hit is very likely to survive the fix.
- notes: `evidence_by = maker` is honest.

### 2024-05-14-pichai-ai-overviews-us-this-week.toml  (hits)  — PASS
- quote: ok. Verbatim in the captions at 00:05:35 to 00:05:42. It is in Pichai's labelled segment (">>SUNDAR PICHAI: Hi, everyone" at line 83; no other speaker label before the quote).
- date: ok (upload 20240514).
- role: ok.
- admission: ok. It is an announced same-week launch, which is close to trivial, but admissible.
- due: ok (`due_date` 2024-05-19).
- verdict: ok. Liz Reid's post (published 2024-05-14) says "So today, AI Overviews will begin rolling out to everyone in the U.S." The line about "a billion people", said by Liz Reid and not Pichai, is rightly left out.
- notes: none.

### 2024-05-14-pichai-ask-photos-this-summer.toml  (hits)  — PASS
- quote: ok. Verbatim in the captions at 00:07:37 to 00:07:50, in Pichai's segment.
- date: ok.
- role: ok.
- admission: ok.
- due: ok. Ending summer at the September equinox (2024-09-22) is a reasonable reading; the method has no season rule, so the lead may want to write one down.
- verdict: ok. Google's post of 2024-09-05 says "Today, early access to Ask Photos is rolling out to select U.S. users as part of Google Labs". The judgement call (a rollout to some users counts) is stated openly.
- notes: none.

### 2025-02-04-pichai-mariner-astra-features-gemini-app.toml  (hits)  — PASS
- quote: ok. Verbatim on Google's posted Q4 2024 remarks (published 2025-02-04). "Both" refers to Project Mariner and Project Astra in the sentence before.
- date: ok.
- role: ok.
- admission: ok.
- due: ok (2025).
- verdict: ok. The Astra half: Pichai's I/O 2025 remarks (published 2025-05-20) say "Gemini Live now incorporates Project Astra's camera and screen-sharing capabilities ... already available to all Android users". The Mariner half: the Gemini 3 app post (2025-11-18) says Gemini Agent is "Built on insights from Project Mariner", "rolling out to Google AI Ultra members first". Both halves landed in 2025. The judgement that a feature built on Mariner counts as a Mariner feature is stated openly.
- notes: `verdict_source` names only the Mariner-half post. Add the I/O 2025 remarks (https://blog.google/innovation-and-ai/technology/ai/io-2025-keynote/) as a second source so that both conditions of the bar have a record in the file.

### 2025-02-04-pichai-waymo-austin-atlanta-2025.toml  (hits)  — PASS
- quote: ok. Verbatim on Google's posted Q4 2024 remarks.
- date: ok.
- role: ok.
- admission: ok. The method uses "a robotaxi service by Y" as its own example of a deployment claim. "Network and operations partnerships to open up new markets" reads partly as business expansion, but the claim is that a driverless (AI-driven) service opens in two cities.
- due: ok (2025).
- verdict: ok. His Q2 2025 remarks (published 2025-07-23) say "Last month, Waymo launched in Atlanta, more than doubled its Austin service territory". The Austin launch date (2025-03-04) rests on press reports, but his Q1 2025 remarks ("Through our partnership with Uber, we expanded in Austin") are his own record that the Austin service existed by then.
- notes, an open question for the lead: `repeated_on = [2025-04-24]` treats the 2025-04-24 words as an unchanged repeat. But that day he said "preparing for our public launch in Atlanta later this summer" (prepared remarks) and "first paid rides in Atlanta, via Uber, later this year" (his answer in the question session, page 19 of Alphabet's Q1 2025 transcript). "Later this summer" narrows the due point for Atlanta. The method's rule for a changed repeat ("new due year or changed condition") arguably makes it a separate record with `restates`; it would be a hit, since Atlanta opened 2025-06-24. That would add one hit to Pichai's count. The `notes` field already describes it as narrower, so the lead should rule on which reading applies.

## Cross-file notes
- Pichai's role note: several files say "Google since 2015-08-10". That is the day the change was announced; he took office as Google's chief executive when the Alphabet reorganisation took effect on 2015-10-02. It makes no difference to any claim in this batch (all from 2022 to 2025), but it should be corrected wherever the date appears.

## Summary
PASS 7 / FAIL 3 / COULD NOT VERIFY 0. No verdict changes.

- FAIL: the Microsoft 365 Copilot claim (`2023-10-nadella-m365-copilot-generally-available-this-year`). The letter is signed 2023-10-16, so `when` should be that full date, and `when_note` wrongly says the page gives no day.
- FAIL: the YouTube auto-chapters goal (`2022-05-11-pichai-youtube-auto-chapters-80-million-goal`). The quote silently drops "auto generated chapters" and so is not verbatim. Also, the verdict source's "tens of millions" does not show a shortfall, so `direction = not_come` claims more than the record shows.
- FAIL: the Gemini models through 2024 claim (`2023-10-24-pichai-gemini-models-throughout-2024`). The bar needs more than one public 2024 release, but the only source cited shows one, and `verdict_why` wrongly calls 1.5 Pro's February 2024 limited preview a release to the public. It needs a primary record for a second public release (the hit itself is very likely to stand).

## Batch 7

# Batch 7 results: checks of 10 claim files against their sources (2026-10-19)

Sources were opened on 2026-10-19: web pages with curl, YouTube captions with yt-dlp. For both Google I/O keynotes, the caption track that downloaded carries speaker labels ("SUNDAR PICHAI:"), so the speaker could be confirmed directly.

### 2025-05-20-pichai-gemini-25-to-search-this-week  (sample)  — FAIL
- quote: ok. The I/O 2025 keynote captions give "And starting this week, Gemini 2.5, our most intelligent model series, is coming to Search." The labelled caption track marks the speaker as SUNDAR PICHAI. The automatic captions place it at 00:47:38 to 00:47:47, which matches the locator.
- date: ok. The official Google upload is dated 2025-05-20.
- role: ok. He was chief executive of Google and Alphabet.
- admission: ok. It is a dated, forward-looking claim that an AI model will ship.
- due: ok. 2025-05-25 is the Sunday of the week it was said.
- verdict: problem. Two fields are wrong, and a third is weakly sourced.
  - **`direction = "not_come"` is contradicted by the record itself.** The file's own `verdict_why` and `verdict_source` (a Gigazine report of 2025-07-17) show Gemini 2.5 Pro running in AI Mode. Pichai's own Q2 2025 earnings remarks (https://blog.google/inside-google/message-ceo/alphabet-earnings-q2-2025/, 2025-07-23; I opened it) say "AI Overviews are now powered by Gemini 2.5". 9to5Google on 2025-06-18 (https://9to5google.com/?p=677145) reports Google saying Search runs custom versions of 2.5 Flash-Lite and Flash. Gemini 2.5 did reach Search, within about one to two months. If the verdict stays `missed`, `direction` must be `later`.
  - **`evidence_by = "outside"` is wrong.** Gigazine only passes on Google's own announcement, so the field should be `maker`. A Google primary record would be a better `verdict_source` than a trade report, for example the Q2 remarks above.
  - The Gigazine source covers Gemini 2.5 Pro for paying subscribers. That is not the "custom version of Gemini 2.5" for everyone in AI Mode and AI Overviews that Google announced on the day (Google's same-day post, https://blog.google/products/search/google-search-ai-mode-update/: "Starting this week, we're bringing a custom version of Gemini 2.5 ... into Search for both AI Mode and AI Overviews in the U.S."). `verdict_why` treats the two as the same thing.
  - The "missed" itself rests only on finding no record that it went live that week. That is allowed (a hit needs a dated record, and none was found), and the file's `verify` field says so honestly. It is still the weakest kind of miss.
- notes: Change before publishing: set `direction` to `later` and `evidence_by` to `maker`, and in `verdict_why` give the earliest dated Google record of Gemini 2.5 in Search. Optionally replace the Gigazine source with a Google record.

### 2025-05-20-pichai-meet-translation-enterprises-this-year  (sample)  — PASS
- quote: ok. The words are verbatim in the labelled captions: "and real-time translation will be coming to enterprises later this year." The automatic captions place them at about 00:10:22, which matches.
- date: ok (2025-05-20).
- role: ok.
- admission: ok. It is a dated ship date for an AI feature.
- due: ok (2025-12-31).
- verdict: ok as a judgement call. The Workspace Updates post dated 2026-02-04 says that as of 2026-01-27 the feature "is no longer restricted to businesses in a limited alpha program", and its rollout dates match. `evidence_by = maker` and `direction = later` are right.
- notes: The judgement call cuts closer than the file says. TechCrunch on 2025-05-20 (https://techcrunch.com/2025/05/20/google-meet-is-getting-real-time-speech-translation) reports Google saying "early testing coming to Workspace customers this year". If that was Google's own meaning of "coming to enterprises", the 2025 closed test would meet it and the claim is a hit. The file's notes should mention this. The start date of the closed test was not found.

### 2025-06-05-pichai-dramatic-progress-by-2030  (sample)  — PASS
- quote: ok. The words are verbatim on the transcript page between (00:39:54) and (00:40:31), in Pichai's own turn.
- date: ok. The transcript was posted on 2025-06-05; the recording date is unknown, as the file says.
- role: ok.
- admission: ok. It is forward-looking, dated "by 2030", and about AI progress.
- due: ok (2030).
- verdict: ok. Marking it "cannot be tested" (`unfalsifiable`) is right: "dramatic progress" and "in a big way" name no measure and no named comparison.
- notes: none.

### 2025-10-29-pichai-gemini-3-later-this-year  (hits)  — PASS
- quote: ok. "We're looking forward to the release of Gemini 3 later this year." is verbatim on Google's page of his remarks, which is dated Oct 29, 2025.
- date: ok.
- role: ok.
- admission: ok. It is a named AI model coming out by a date.
- due: ok (2025-12-31).
- verdict: ok. Google's post dated Nov 18, 2025 says "releasing Gemini 3 Pro in preview and making it available today across a suite of Google products". A public preview inside consumer products is a release. `evidence_by = maker` and `direction = on_time` are right.
- notes: The occasion says "remarks as posted by Google". This is Google's edited version of what he said, not a full call transcript. `source_kind = transcript` is acceptable, but "own_words" would describe it just as well.

### 2026-05-19-pichai-ask-youtube-broadly-us-this-summer  (hits)  — PASS
- quote: minor problem. The caption track I downloaded (with speaker labels, at 00:08:44) reads "it will roll out broadly in the US this summer". The file quotes "it'll". Without listening to the audio I cannot say which is right. The words are otherwise verbatim and inside Pichai's own segment.
- date: ok. The official upload is dated 2026-05-19.
- role: ok.
- admission: ok.
- due: ok. It ends at the September equinox, 2026-09-22, the same reading the other "this summer" claims use.
- verdict: ok. The Social Media Today report, published July 7, 2026, says Ask YouTube is "finally available for all signed-in users in the U.S. aged 13 and older" on desktop, quoting YouTube. That meets "most US users on at least one main platform". `evidence_by = maker` is right, since the report passes on YouTube's own announcement.
- notes: The same report says YouTube "added Ask YouTube to the CTV version of its app in February" 2026 (CTV means YouTube's app on smart TVs). That conflicts with the file's line "Mobile and TV followed on 2026-10-12". The line should be checked, or the TV part dropped. It does not change the verdict. Also, `checked_how` says "automatic captions", but the track that downloaded carries speaker labels, so it is probably a human-made track.

### 2026-05-19-pichai-docs-live-this-summer  (hits)  — PASS
- quote: ok. The words are verbatim at 00:11:03, in Pichai's segment. The caption continues "... Gmail and Google Keep then too", and the quote stops at 25 words.
- date: ok.
- role: ok.
- admission: ok.
- due: ok under the ledger's equinox reading (2026-09-22).
- verdict: ok. Google's post dated Sep 03, 2026 says the features "are rolling out this week", in Gmail and Keep for Google AI Plus, Pro and Ultra subscribers and in Docs for Pro and Ultra. That meets the bar.
- notes: **This hit depends on the equinox reading of "this summer".** If summer is read as ending on 31 August, as weather services count it, the rollout on 2026-09-03 is a miss. The method's due-year section has rules for months and quarters but none for seasons. Five "this summer" claims rely on the same choice, so the method should say how a season is read. As written, the choice is in the claim files but not in the method.

### 2023-07-14-suleyman-modern-turing-test-as-little-as-two-years  (sample)  — FAIL
- quote: ok. The words are verbatim on the MIT Technology Review page, dated July 14, 2023, in the paragraph straight after the test is described.
- date: ok.
- role: ok. He was co-founder and chief executive of Inflection AI.
- admission: problem. "Could be as little as two years away" gives the earliest the test might be passed, not a date by which AI will pass it. The admission rule needs words saying AI will do something by a date or within a length of time, and "borderline cases stay out".
- due: given only as the earliest date, which the file admits.
- verdict: problem. The status "cannot be tested" (`unfalsifiable`) is defined as a claim that "has a date but no bar an outsider could test". Here it is the reverse: the bar (his own, well-defined Modern Turing Test) can be tested, and the date is not a deadline. The method allows only two consistent treatments:
  - (a) leave it out as borderline (not dated as a deadline), and record the reason in the search log; or
  - (b) read "could" as a hedge, which the method says to score at face value, making the claim missed.
  - Calling it "cannot be tested" counts it under a status whose definition it does not fit.
- notes: Change before publishing: (a) is the reading the "borderline stays out" ruling points to. The file says the seed list of 2026-10-17 made the same call, so John may already have seen it. Also, the notes name the 2026-02-12 restatement but not the 2024-01-18 restatement, which names this claim in its `restates` field.

### 2023-08-18-suleyman-websites-and-apps-conversational-five-years  (sample)  — PASS
- quote: ok. The words are verbatim in the automatic captions at about 00:50:42. They are Suleyman's answer to Calacanis's question "what is Inflection AI", beginning "so we're developing a personal AI".
- date: ok. The This Week in Startups upload is dated 2023-08-18.
- role: ok. He was chief executive of Inflection AI.
- admission: ok.
- due: ok. Five years runs to 2028-08-18, judged at the end of 2028.
- verdict: ok. It is not yet due (`not_yet_due`).
- notes: none.

### 2024-01-18-suleyman-modern-turing-test-capabilities-cheap-before-2030  (sample)  — PASS
- quote: ok. The words are verbatim in the World Economic Forum upload's captions at about 00:44:48, within his description of the Modern Turing Test.
- date: ok. CNBC's upload (HPOxCHhCJFA) is dated 2024-01-18 and titled 1/18/2024; the Forum's own upload is dated 2024-02-12.
- role: ok. He was still at Inflection; he moved to Microsoft on 2024-03-19.
- admission: ok.
- due: follows the method's "later end where usage does not settle it" rule (2030, with 2029 as the earlier end). Note a mismatch with a sibling file: his own restatement of 2025-10-20 (2025-10-20-suleyman-ai-runs-a-business-before-2030) says "before 2030", and that file sets its due year to 2029. That is evidence that his own usage puts "the end of the decade" at the end of 2029. The method says the speaker's usage decides before the fallback, so `due` arguably should be 2029. No verdict changes, since the claim is not yet due either way.
- verdict: ok. It is not yet due (`not_yet_due`).
- notes: `statement_id` suleyman-2024-01 exists in the statements table, dated 2024-01, which matches.

### 2024-02-20-suleyman-hallucinations-largely-eliminated-next-year  (cov)  — FAIL
- quote: n/a (the file is marked press coverage only). `reported_as` matches the article. Communications Today, published 2024-02-21 01:55 UTC and crediting Moneycontrol, quotes him directly: "I'm very convinced that we're going to largely eliminate hallucinations over the next year. And they're going to be as accurate as any content that you can find on the web." The words are in the third paragraph, as the locator says.
- date: ok. The forum ran on 2024-02-20 and 2024-02-21 (from the nasscom event listing, seen in search results only), and the report went up at 07:25 India time on the second day, so 2024-02-20 is sound.
- role: ok. He was chief executive of Inflection.
- admission: ok.
- due: ok (2025).
- verdict: problem. This is exactly the case the 2026-10-19 ruling on named comparisons covers. "As accurate as any content that you can find on the web" names a comparison. Its plainest reading is "no less accurate than the most reliable content on the web", which an outsider could test. The file argues that web content has no single accuracy, but by the same argument "the smartest human" has no single intelligence, and that ruling keeps a bar for it. With that bar the claim would very likely be missed. The GPT-5 system card already used for the 2023 claim shows major factual errors in about 20% of answers from the models in use in mid-2025, well short of reliable reference sources.
- notes: Change before publishing: either write a plain-reading bar from the comparison and score the claim, or record John's ruling that this phrase is not a named comparison. The same question then applies to the restatement of 2024-09-18 (2024-09-18-suleyman-hallucinations-largely-eliminated-next-year). As far as I can see, its quoted words lack the web comparison, so it can stay "cannot be tested". Its due year (2025) is the same as the 2023 claim's, so it is a new record only because the wording of the test changed.

## Summary

PASS 7, FAIL 3, COULD NOT VERIFY 0.

- **2025-05-20-pichai-gemini-25-to-search-this-week:** `direction = not_come` is contradicted by the file's own evidence and by Pichai's 2025-07-23 remarks that AI Overviews ran on Gemini 2.5. It should be `later`. `evidence_by` should be `maker`, not `outside`.
- **2023-07-14-suleyman-modern-turing-test-as-little-as-two-years:** "could be as little as two years away" is an earliest date, not a deadline. "Cannot be tested" does not fit a claim whose bar can be tested; it should be left out as borderline, or else scored as a hedged claim.
- **2024-02-20-suleyman-hallucinations-largely-eliminated-next-year:** "as accurate as any content that you can find on the web" is a named comparison. Under the 2026-10-19 ruling it gives a plain-reading bar, and is likely missed rather than "cannot be tested".

Notes worth acting on, though they do not change any count:
- The "this summer" equinox reading decides the Docs Live hit and is not in the method.
- The Meet translation miss is closer than stated (TechCrunch reported Google saying "early testing" for business customers in 2025).
- The Ask YouTube file's line about TV arriving in October conflicts with its own source, which says TV came in February.
- The 2024-01-18 Modern Turing Test claim's due year is arguably 2029, from his own "before 2030".

## Batch 8

# Results, batch 8 (Mustafa Suleyman, ten claim files), checked 2026-10-19

Sources opened: captions of all five YouTube uploads (yt-dlp; upload dates read with yt-dlp), The Verge's printed Decoder transcript (curl; datePublished 2024-12-09T15:00 UTC), and every verdict source (OpenAI release notes through a reader copy, Altman's post through api.fxtwitter.com, the arXiv abstract, the archived Microsoft Copilot post of 2025-06-12, the archived OpenAI Voice mode FAQ of 2024-12-26, Windows Central's report of 2025-04-17). Also opened, to test the verdicts: Microsoft's Windows Experience Blog post of 2025-10-16 and Google's Gemini post of 2024-08-13.

Role, for all ten: Suleyman has been chief executive of Microsoft AI since 2024-03-19, and every claim here falls after that date. One point for the owner, which changes no row: Microsoft AI is a division of Microsoft, not a company of its own. The admission rule says "chief executive ... of a company". The owner's list of fourteen figureheads names him, so I treat the role as settled, but the page's wording should allow for a division head.

---

### 2024-04-suleyman-self-improving-ai-five-to-ten-years  (sample)  — FAIL
- quote: ok. TED's captions at 0:20:09 read "I think it's still a good five to 10 years / before we have to really confront that." Just before it (0:19:49 to 0:20:04) he describes an AI able to "independently self-improve, update its own code, explore an environment without oversight ... without a human in control".
- date: ok. The upload is dated 2024-04-22, and the talk was given at TED2024 that week, so recording only the month is right.
- role: ok.
- admission: problem. These words say the thing is *at least* five to ten years away ("still a good five to 10 years before"). They set a lower bound, not a "by" date. The plain reading is "not before about 2029", not "by 2034".
- due: the sum is right (2029 at the earlier end, 2034 at the later), but see below.
- verdict: not_yet_due, and the date is correctly ahead. The problem is the bar. It is written as a "by the end of 2034" test, and its first half (an AI that improves itself by changing its own code) arguably already exists in 2025 work like the Darwin Gödel Machine. That is the same paper this ledger uses to score his 2025 self-improvement claim as a hit. So in 2034 the ledger could score a "hit" for something arriving well *before* the window he said, which is the opposite of what he claimed.
- must change: either rewrite the bar, before publishing, to test the window he gave (the thing does not arrive before about 2029 and does by 2034, with "sooner" counted against him), or drop the claim as borderline under the admission rule. The restatement from 2025-12-12 that names this file in `restates` would need the same reading.

### 2024-06-25-suleyman-knowledge-at-zero-marginal-cost-15-to-20-years  (sample)  — PASS
- quote: ok. The automatic captions at 0:16:13 to 0:16:22 read "in 15 or 20 years time we will be producing new scientific cultural knowledge at almost zero marginal cost", word for word.
- date: ok. A blog post of 2024-06-26 (lifeboat.com, linking TechCrunch's piece of 2024-06-25) says the interview was "on Tuesday", which was 2024-06-25.
- role: ok.
- admission: ok.
- due: ok. 2039 and 2044.
- verdict: unfalsifiable is right. No one measures the cost of producing new knowledge.
- notes: the `when_note` gives the festival as 2024-06-20 to 2024-06-26. The Aspen Institute's own listing has the Ideas Festival as 2024-06-23 to 2024-06-29 (2024-06-20 to 2024-06-23 was the separate Aspen Ideas: Health). Fix the wording; the date itself stands.

### 2024-06-25-suleyman-real-time-interruptible-voice-by-end-of-year  (hits)  — FAIL (the verdict stands; the evidence must change)
- quote: ok. The captions at 0:44:36 to 0:44:45 read "literally by the end of this year we'll have realtime voice-based interfaces that allow full Dynamic interrupt and it feels like just talking", word for word.
- date: ok (see the claim above). The `when_note` has the same wrong festival dates.
- role: ok.
- admission: ok. "We" reads fairly as the field: he is talking to a teacher about using AI in general.
- due: ok (2024-12-31).
- verdict: problem. The cited `verdict_source` is OpenAI's Voice mode FAQ as captured on 2024-12-26. It does say "more natural, real-time conversations". But its only mention of interrupting is advice on "preventing interruptions" ("Occasionally, interruptions may happen ... use headphones ... Voice Isolation"). That is about noise cutting in by accident. It never says the user can interrupt the AI mid-answer, so the "interruptible" condition rests on an inference. The capture also does not show the `verdict_on` date of 2024-09-24.
- must change: cite a dated primary record that states the interrupt condition outright. Google's post of 2024-08-13 (https://blog.google/products/gemini/made-by-google-gemini-ai-updates/) says of Gemini Live: "You can even interrupt mid-response". It was released that day to paying Gemini Advanced users on Android. That is outside evidence, before the due date, and meets both conditions. Set `verdict_on` to 2024-08-13, or keep OpenAI as the source but cite a record that actually says the AI can be interrupted. The status stays hit, `evidence_by` stays outside, and `direction` stays on_time.

### 2024-09-18-suleyman-ai-memory-workable-in-18-months  (hits)  — PASS
- quote: ok. The captions at 0:25:11 to 0:25:15 read "I I think that we're 18 months away from really getting that to a workable level". "That" is the AI that "really does remember everything that You' said and it's able to retrieve from that history of your conversations accurately" (0:25:02 to 0:25:08).
- date: ok. At 0:36:09 to 0:36:13 Kara Swisher says Microsoft and BlackRock announced their fund "yesterday". The fund was announced 2024-09-17. The upload is dated 2024-10-23.
- role: ok.
- admission: ok. "We" here reads fairly as the field: it is a general question about the timeline.
- due: ok (2026-03-18).
- verdict: confirmed on the page. OpenAI's release notes carry a "January 15, 2026" entry: ChatGPT "can now more reliably find specific details from your past chats", and "Any past chat used to answer your question now appears as a source". Altman's post of 2025-04-10 17:13 UTC also confirmed: "it can now reference all your past conversations!".
- notes: "accurately enough for everyday use" rests entirely on OpenAI describing its own product; nobody measured it. `evidence_by = outside` meets the letter of the method (OpenAI is not his company), but the page will show this hit with no mark even though no one tested it. The `verdict_why` says so; consider saying so on the page too.

### 2024-10-suleyman-permanent-ai-memory-done-in-2025  (hits)  — FAIL (the hit probably stands; the bar's reading and `evidence_by` must change)
- quote: ok. The captions at 0:14:24 to 0:14:29 read "I'm I'm really confident 2025 memory is done permanent memory".
- date: ok. The upload description says "the October 2024 Masters of Scale Summit", so recording only the month is right.
- role: ok.
- admission: ok.
- due: ok (end of 2025). The `restates` link to the 18-month claim is right: same thing, earlier date.
- verdict: problem. In context, "we" is Microsoft, not the field. He says "we're going to nail memory ... we already have memory on the web ... co-pilot has really good citations ... so we're just kind of compressing that to do it for your personal Knowledge Graph" (0:14:22 to 0:14:49). The bar ("an AI assistant", any maker) and the evidence (Altman's ChatGPT post, marked `outside`) read it as a claim about the field. Unlike the other two "we" claims, this file's notes do not even argue the field reading.
- must change: rewrite the bar to Microsoft's Copilot. Score it on Microsoft's own record: Copilot Memory was announced 2025-04-04 (GeekWire, Redmond Magazine and The Register reports, 2025-04-04 to 2025-04-08) and widened in the Copilot Fall Release (2025-10-23); find Microsoft's own post for the source. Set `evidence_by = maker`. Check that Copilot's memory reached "permanent memory" across all conversations in 2025; if it did, the hit stands, now marked as the maker's word. The ChatGPT post can stay as context in the notes.

### 2024-10-suleyman-teams-experiment-with-self-improvement-in-2025  (hits)  — PASS
- quote: ok. The captions at 0:04:29 to 0:04:34 read "we can see that coming into view in 2025 / teams will start experimenting with that". "That" is "a closed loop of self-improvement that doesn't have a human and directly overseeing it" (0:04:22 to 0:04:29).
- date: ok (see the memory claim above).
- role: ok.
- admission: borderline but acceptable. It is about what research teams will do. The search-log row for the Aspen session (`suleyman-claims-028`) left out a claim for being "about people, not AI doing something". This one is about AI, because the experiment needs an AI that closes the loop.
- due: ok.
- verdict: confirmed. The arXiv paper 2505.22954, "Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents", was submitted 2025-05-29 by Jenny Zhang and four others. Its abstract: "a self-improving system that iteratively modifies its own code". Each change is made by a foundation model and tested against coding benchmarks. `evidence_by = outside` is right.
- notes: the abstract also says "All experiments were done with safety precautions (e.g., sandboxing, human oversight)". The bar's "no person directing each change" is still met, but the `verdict_why` should quote that sentence so a reader sees the tension with "doesn't have a human directly overseeing it". Similar experiments existed before he spoke (the Gödel Agent paper of October 2024, Self-Taught Optimizer of 2023), so the narrow bar is close to trivially met. The notes say it is read narrowly, which is honest.

### 2024-12-05-suleyman-copilot-vision-all-apps-always-on-2025  (sample)  — FAIL (the miss probably stands; `verdict_why` is wrong on the facts)
- quote: ok. The captions at 0:17:34 to 0:17:40 read "yeah I mean that is definitely coming uh you know next year", answering a question from the interviewer (Rowan Cheung). The question is quoted correctly in the notes.
- date: ok. The upload is dated 2024-12-05.
- role: ok.
- admission: ok, but the test comes entirely from the interviewer's wording ("that"). The bar uses the question's conditions and drops the interviewer's "possibly even infinite memory", which is right. He added "might be the back end of next year might be the summer".
- due: ok (end of 2025).
- verdict: problem. The `verdict_why` says that at the end of 2025 ordinary users could share "at most two chosen apps at a time ... in the United States", and that whole-desktop sharing "reached only Windows Insiders". That describes June to July 2025, not December. Microsoft's Windows Experience Blog of 2025-10-16 ("Making every Windows 11 PC an AI PC") says "Copilot Vision on Windows is now available worldwide", "in all markets where Copilot is offered", with "Full desktop and app sharing". It still runs only "with your permission", in sessions the user starts. So the always-on, 24/7 condition still failed and the miss very likely stands. But the stated reasons are wrong, and the `verdict_source` (a June post) is not the last record before the due date.
- must change: rewrite `verdict_why` to say that by 2025-10-16 desktop sharing reached ordinary users worldwide, and that what failed was always-on, 24/7 use. Add the 2025-10-16 post as the `verdict_source` (or alongside the June one). Reconsider `direction = not_come` against "partly came": that changes no count, but the wording should match.

### 2024-12-05-suleyman-copilot-vision-general-availability-early-2025  (hits)  — PASS (with a judgement call flagged)
- quote: ok. The captions at 0:17:00 to 0:17:07 read "sometime next year uh in the early part of next year it will go into GA and lots of people get access to it".
- date: ok.
- role: ok.
- admission: ok. A shipping claim about an AI product.
- due: a judgement call, disclosed in `due_basis`. The file reads "the early part of next year" as the first half (2025-06-30). If it meant the first quarter, the first wide release (free to all US users of Microsoft Edge, reported by Windows Central 2025-04-17) was late, and this would be a miss. The method has no rule for "early part". It is the generous reading, like the rule for ranges; the owner may want to rule on it.
- verdict: confirmed. The archived Microsoft post of 2025-06-12 says "Copilot Vision on Windows is available now in the US for Windows 10 and Windows 11", and also "part of Copilot Labs". Windows Central's report dated 2025-04-17 confirms the free Edge release. `evidence_by = maker` is right.
- notes: the product he was asked about was the Edge preview, so the April Edge release is the closer match, and `verdict_on` could be 2025-04-17. That date rests on press coverage, so if it is used, cite Microsoft's own April post. Two generous readings are stacked here: the first half of the year, and "GA" read as "the public got access" even though Microsoft kept the "Labs" label. The notes disclose the second; `verdict_why` should say both.

### 2024-12-09-suleyman-agi-plausible-five-to-seven-years  (sample)  — PASS
- quote: ok. The Verge transcript reads "I do think it is going to be plausible at some point in the next two to five generations.", word for word, followed by "but I think within the next five to seven years since each generation takes 18 to 24 months now. So, five generations could be up to 10 years away". His definition, "a general-purpose learning system that can perform well across all human-level training environments ... that includes physical labor", comes about 1,500 characters later, so the locator is fine.
- date: ok. datePublished is 2024-12-09T15:00 UTC, and the note on the earlier recording is right ("since I arrived eight or nine months ago now").
- role: ok.
- admission: acceptable, but weak. "Plausible" says it could happen, not that it will. The method keeps hedges and scores them at face value, and the bar keeps "plausible". Still, a miss in 2031 would hold him to a claim he hedged with "I don't want to say I think it's a high probability". Worth a line on the page.
- due: ok (2029 and 2031; "up to 10" correctly left unscored).
- verdict: not_yet_due, correct. Taking the bar from his own definition in the same source is right under the rule on named stages.
- notes: the `statement_id` (`suleyman-2024-02`, the coded statement from AOL's report) exists, with date 2024-12, which matches to the month.

### 2024-12-09-suleyman-generated-interfaces-default-three-or-five-years  (sample)  — PASS
- quote: ok. The transcript reads "The UI that you experience is going to be automagically produced by an LLM in three or five years, and that is going to be the default." The quote is a word-for-word run of it, and the "My bet is" sentence before it is quoted correctly in the notes.
- date: ok.
- role: ok.
- admission: ok. A dated forecast about AI products.
- due: ok (2027 and 2029).
- verdict: not_yet_due, correct.
- notes: none.

---

## Summary

PASS 6, FAIL 4, COULD NOT VERIFY 0. Every source opened and every quote was found word for word.

- **The self-improving AI claim, 5 to 10 years (TED, 2024-04):** his words set a lower bound ("still a good five to 10 years before"), but the bar is a "by 2034" test that work from 2025 may already meet. It could score a hit for something arriving before the window he gave. Rewrite the bar or drop the claim as borderline.
- **The interruptible voice claim, end of 2024 (Aspen, 2024-06-25):** the hit stands, but the cited OpenAI FAQ never says the user can interrupt the AI, and it does not show the 2024-09-24 date. Cite Google's Gemini Live post of 2024-08-13 ("You can even interrupt mid-response") or an OpenAI record that says it outright.
- **The permanent memory claim, 2025 (Masters of Scale, 2024-10):** in context "we" is Microsoft's Copilot, not the field. Rebase the bar on Copilot's 2025 memory release and set `evidence_by` to maker. The hit probably stands.
- **The always-on Copilot Vision claim, 2025 (Rundown, 2024-12-05):** `verdict_why` misstates the position at the end of 2025. Microsoft's post of 2025-10-16 shows Vision worldwide with full desktop sharing. Only always-on, 24/7 use failed. Fix the wording and the source; the miss probably stands.

Also to fix, no count changes: the Aspen `when_note` festival dates (the Ideas Festival ran 2024-06-23 to 2024-06-29), in both Aspen files.

Flagged for the owner, no change required:
- The Copilot Vision early-2025 hit rests on two generous readings ("early part" as the first half of the year, "GA" as public access despite the Labs label). Under a first-quarter reading it would be a miss.
- The 18-month memory hit rests on OpenAI's own description of accuracy, yet is unmarked (`outside`).
- The AGI claim's "plausible" makes it a weak forecast.

## Batch 9

# Batch 9 results: independent check of ten claim files (2026-10-19)

Sources were opened on 2026-10-19: YouTube captions downloaded with yt-dlp (upload dates read with `--print upload_date`), Meta's earnings-call transcripts (PDFs from s21.q4cdn.com, read as text), about.fb.com releases, the Lex Fridman and Dwarkesh transcript pages, and the Threads posts (post text read from the link-preview tags, post dates decoded from the post ids). Nothing in the repository was edited.

### 2025-11-12-suleyman-closed-loop-self-improvement-at-scale-few-years  (sample)  — PASS
- quote: ok. The captions at 0:18:44 to 0:18:53 read "so it doesn't seem very far-fetched to say that in a few years time at significant scale or that will get closed loop". The speaker is Suleyman, answering Kantrowitz's question at 0:17:05 about AI that improves itself. The caption word "or" is probably "all", which is a caption error and not a quote error.
- date: ok. Upload date 20251112 on Alex Kantrowitz's channel.
- role: ok. Chief executive of Microsoft AI (since March 2024).
- admission: doubtful, and the owner should decide. "It doesn't seem very far-fetched to say" calls the outcome plausible. It does not say it will happen. Under "borderline cases stay out" this could be left out. It is not a hypothetical, though, and the file keeps the hedge in `prediction`. In context he is talking about the pipeline that makes training data and judges it ("data the core commodity ... individual parts of that pipeline"), which the bar's "from start to finish" reading stretches a little.
- due: ok under this file's reading ("a few" as two to four years, 2027 to 2029). Across the ledger, though, "a few years" is read two ways. Suleyman's three files and one other use two to four years. `2025-04-30-zuckerberg-ai-business-agent-every-business`, `2026-08-10-zuckerberg-superintelligence-beyond-human-next-few-years` and `2025-05-28-amodei-axios-half-of-entry-level-white-collar-jobs` use two to five. Under two to five, this file's due year would be 2030. One reading should be ruled and applied everywhere. No count changes today.
- verdict: ok. Not yet due (2029).
- notes: none.

### 2025-11-25-sutskever-human-like-learner-5-to-20-years  (sample)  — PASS
- quote: ok. The printed transcript has "Ilya Sutskever 01:22:26 I think like 5 to 20." The host asks the question at 01:22:14, and Sutskever answers "Mhm" at 01:22:29 when asked "5 to 20 years?".
- date: ok. The page's post date is 2025-11-25T17:04 UTC.
- role: ok. Chief executive of Safe Superintelligence from July 2025. Whether Safe Superintelligence counts as "building frontier AI models" when it has released no model is a judgement the panel has already made, but worth knowing.
- admission: ok. The words carry a length of time and look forward. The thing being predicted is defined in the host's own question ("can learn as well as a human and subsequently ... become superhuman"), and the speaker's reply refers back to it.
- due: ok. 2030 to 2045, with the later end taken.
- verdict: ok. Not yet due. Treating "learn as well as a human" as a named comparison, which keeps a bar, fits the ruling.
- notes: none.

### 2023-02-01-zuckerberg-generative-ai-launches-this-year  (hits)  — PASS
- quote: ok. Verbatim in Meta's transcript of the fourth-quarter 2022 call (dated February 1st, 2023). It is Zuckerberg's first answer, to Brian Nowak's question on generative AI.
- date: ok.
- role: ok.
- admission: ok.
- due: ok (2023).
- verdict: ok. The release of 2023-09-27 (datePublished 2023-09-27) says AI stickers are "starting to roll out", Meta AI is introduced "in beta" and 28 AI characters are launching in beta in the US. That is three generative AI products in the year. Maker evidence, honestly marked.
- notes: a wording fix. `verdict_why` lists "image editing tools" among the things rolling out on 2023-09-27, but the release says restyle and backdrop are "coming soon to Instagram". Drop them or say "announced". The verdict does not change.

### 2023-09-27-zuckerberg-glasses-multimodal-ai-early-next-year  (hits)  — FAIL
- quote: ok. The Verge's interview captions at 0:45:54 to 0:46:01 read "sometime early next year we're also going to have this multimodality so you're going to be able to ask the AI". The upload date is 20230927. The channel is "Decoder with Nilay Patel", which is The Verge's.
- date: ok.
- role: ok.
- admission: ok.
- due: problem, and it changes the verdict. The file reads "early next year" as the first half of 2024 (due 2024-06-30). Other files read the same words as the first quarter:
  - `2023-12-06-hassabis-gemini-ultra-developers-enterprise-early-next-year` and `2023-12-06-hassabis-bard-advanced-early-next-year` ("the plainest reading of 'early'")
  - `2024-12-11-hassabis-gemini-2-more-google-products-early-next-year`
  - `2024-03-18-huang-self-driving-in-mercedes-end-2024-early-2025`, scored missed against a 2025-03-31 date with a verdict of 2025-06-04, which falls inside a first-half window.

  The release came on 2024-04-23. Under the first-quarter reading used for Hassabis and Huang this would be a miss. The first-half reading is used only where it produces a hit: here, the smaller Llama 4 claim and `2024-12-05-suleyman-copilot-vision-general-availability-early-2025`. That pattern looks like choosing the reading by outcome. One rule for "early" needs to be ruled and added to the method's due-year section, then applied to all seven files.
- verdict: depends on the due fix. The release of 2024-04-23 (datePublished 2024-04-23) does say multimodal Meta AI is rolling out "to all Ray-Ban Meta smart glasses in the US and Canada in beta", after a test begun in December. That is a hit under the first-half reading and a miss under the first-quarter one.
- notes: add "in beta" to `verdict_why`.

### 2023-09-28-zuckerberg-creator-ais-next-year  (hits)  — PASS
- quote: ok. Verbatim on the transcript page (published 2023-09-28T17:10 UTC), after the (00:42:59) marker, in Zuckerberg's turn.
- date: ok.
- role: ok.
- admission: ok.
- due: ok (2024).
- verdict: ok. The AI Studio release (datePublished 2024-07-29) says it is "starting to roll out AI Studio in the US" and that it "allows creators to build an AI as an extension of themselves to reach more fans". Instagram creators can set up such an AI, and named creators already had one. Maker evidence.
- notes: the page now carries an update of 2026-08-10 saying people can no longer create new AI characters in AI Studio. That has no bearing on the 2024 verdict, but anyone who opens the link will see it.

### 2024-07-23-zuckerberg-llama-most-advanced-next-year  (sample)  — PASS
- quote: ok. Verbatim in the essay (datePublished 2024-07-23).
- date: ok.
- role: ok.
- admission: ok.
- due: ok (2025).
- verdict: ok. The fourth-quarter 2025 call (January 28th, 2026) has "In '25 we rebuilt the foundations of our AI program. Over the coming months we're going to start shipping our new models", and the search log's row for the Access podcast (`zuckerberg-claims-073`) records his 2025-09-18 words on not being at the frontier. Missed, `not_come`, is right.
- notes: `evidence_by = "maker"` is honest. Outside leaderboards would also support the miss, if a stronger source is wanted.

### 2024-07-23-zuckerberg-meta-ai-most-used-by-end-of-year  (hits)  — FAIL
- quote: ok. Rowan Cheung's upload (20240723), captions at 0:27:35: "my goal was for it to be the most used AI assistant in the world by the end of the year".
- date: ok.
- role: ok.
- admission: ok (a goal, marked).
- due: ok (2024).
- verdict: problem. The bar has two parts, and only the first is shown:
  - Meta AI's own size. The third-quarter 2024 call has "over 500 million monthly actives", and the fourth-quarter 2024 call has "more than 700 million monthly actives". Both are Meta's own figures, which only Meta holds.
  - That it was used by more people than any other assistant. Nothing shows this except Meta's own claim on 2025-01-29 ("Meta AI is already used by more people than any other assistant") and the argument that no rival reported a bigger monthly figure. The method says a maker's own figure is evidence only "for a figure only the maker holds". Rivals' user counts are not Meta's figure, and an absence of rival reports is an argument, not a record. The file itself admits the comparison is "loose": rivals reported weekly users, Meta monthly.

  Either the owner rules that a maker's comparative statement about rivals is enough (and the page marks it), or this is not a hit. It cannot simply stay a hit on the current reasoning.
- notes: `verdict_on = 2024-12-31` is the due date, not the date of a record. The method asks for "the date of the demonstration, release or count", which here would be 2025-01-29 (the comparative claim) or 2024-10-30 (the count).

### 2024-07-23-zuckerberg-multimodal-llama-next-few-months  (hits)  — PASS
- quote: ok. Captions at 0:25:43 to 0:25:47: "launching them probably everywhere outside of the EU um uh hopefully over the next few months". The context is the multimodal models.
- date: ok.
- role: ok.
- admission: ok.
- due: ok. The month span runs into 2024 and is judged at year end.
- verdict: ok. The third-quarter 2024 call (October 30th, 2024) has "This quarter, we released Llama 3.2, including the leading small models that run on -device and open source multi-modal models." Maker evidence.
- notes: the release date of 2024-09-25 in `verdict_why` is not in the cited source. I could not open Meta's Llama 3.2 pages either: the ai.meta.com blog returned an error (400) and the newsroom address a not-found page (404). If that date can be confirmed, `verdict_on` should arguably be 2024-09-25 rather than the call date. The verdict does not change.

### 2024-10-30-zuckerberg-smaller-llama-4-early-next-year  (hits)  — FAIL
- quote: ok. Verbatim in the third-quarter 2024 transcript, in Zuckerberg's opening remarks.
- date: ok.
- role: ok.
- admission: ok. A named model release with a date.
- due: problem, the same one as the glasses claim. "Early next year" is read as the first half here, but as the first quarter in the Hassabis and Huang files. The release came on 2025-04-05, five days after a first-quarter due date of 2025-03-31, so under that reading this is a miss.
- verdict: depends on the due fix. The Threads post (text "New drop: llama.com/4"; post id dates it to 2025-04-05 18:58 UTC) is a dated maker record of the release. That Scout and Maverick are "the smaller Llama 4 models", compared with Behemoth, is a fair reading.
- notes: none.

### 2025-01-24-zuckerberg-meta-ai-leading-assistant-billion-people  (hits)  — FAIL
- quote: ok. The Threads link preview reads "In 2025, I expect Meta AI will be the leading assistant serving more than 1 billion people, ..."; the post id dates it to 2025-01-24 14:00 UTC.
- date: ok.
- role: ok.
- admission: ok. The changed-repeat link (`restates`) is right.
- due: ok (2025).
- verdict: problem.
  - The first condition, more than a billion people, is shown. The second-quarter 2025 call (July 30th, 2025) has "more than a billion monthly actives", Meta's own figure.
  - The second condition, leading (read as most used), is not shown by any record. The case rests on "no rival reported a larger monthly figure", which is an argument. In the same call Zuckerberg names "making Meta AI the leading personal AI" as a focus still to be reached. In 2025 OpenAI reported about 800 million weekly ChatGPT users (October 2025), which makes a lead on monthly users doubtful.
  - Neither the second-quarter nor the fourth-quarter 2025 transcript says Meta AI is the most used. The only 2025 record that does is the 2025-01-29 call ("already used by more people than any other assistant", at 700 million), which comes before the billion was reached and is again Meta's word about rivals.

  Under "every condition, shown by a dated primary record" this should be scored missed, with the "leading" condition named as not shown, unless the owner rules that Meta's comparative statement is enough.
- notes: none.

## Summary

PASS 6, FAIL 4, COULD NOT VERIFY 0. Every quote and date checked out.

FAIL reasons:
1. **`2023-09-27-zuckerberg-glasses-multimodal-ai-early-next-year`**: the verdict depends on how "early next year" is read. This file uses the first half of 2024; the Hassabis and Huang files use the first quarter. Under the first quarter, the release of 2024-04-23 is a miss. One rule is needed for all seven files.
2. **`2024-10-30-zuckerberg-smaller-llama-4-early-next-year`**: the same problem. Llama 4 came out on 2025-04-05, five days after a first-quarter due date.
3. **`2024-07-23-zuckerberg-meta-ai-most-used-by-end-of-year`**: "more people than any other assistant" rests only on Meta's own statement about rivals and on no rival reporting a bigger number. That is an argument, not a record. It needs an owner ruling, or a different status.
4. **`2025-01-24-zuckerberg-meta-ai-leading-assistant-billion-people`**: the "leading" condition is not shown by any 2025 record, Zuckerberg himself called "leading" a goal still to be reached, and ChatGPT's 800 million weekly users make the lead doubtful. It should be missed unless the owner rules otherwise.

Cross-file note (no count changes now): "a few years" is read as two to four years in Suleyman's files and as two to five in the two Zuckerberg files and the Amodei file named above. It needs one ruling.
