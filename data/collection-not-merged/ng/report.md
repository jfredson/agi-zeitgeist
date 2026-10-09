# Trace report: ng (Andrew Ng, core tier)

The coordinator told me to stop, so I stopped early. Every row below comes from a search I actually ran or a page I actually read.

1. **Summary.** Years covered: 2005 to 2026. I ran all three fixed year searches (Y1 to Y3) for every one of those years, plus the three discovery searches (D1 to D3).
   - **Statements:** 14 recorded, 2 of them secondhand (ng-2015-01 from The Register and ng-2016-01 from Fortune).
   - **Search log:** 104 rows, about 70 of them web searches.
   - **Quiet years:** 2005 to 2014, 2017, 2018, 2019 and 2021.
   - **Sampling:** no busy years, so none was needed.
   - **Own outlet:** I read every letter in The Batch, his weekly newsletter. That covers issues 1 to 374 (2019 to 2026-10-09), except issues 119 and 124, which returned a server error.

2. **Partial work and unread leads.** The year searches are complete. The follow-ups for 2023 to 2026 are not: those years may hold more statements outside The Batch.
   - **Leads found but not followed up:**
     - NBC News 2025 interview at the AI Developers Conference ("no way this is going to take us all the way to AGI just by itself"): https://www.nbcnews.com/tech/innovation/andrew-ng-says-ai-limited-wont-replace-humans-anytime-soon-rcna246074
     - Business Insider on his Y Combinator talk ("AGI has been overhyped"): https://www.businessinsider.nl/google-brain-founder-andrew-ng-says-agi-is-overhyped/
     - MIT Sloan Middle East: https://www.mitsloanme.com/?p=13628
     - TED talk transcript: https://www.ted.com/talks/andrew_ng_ai_isn_t_the_problem_it_s_the_solution/transcript
     - His written statement to the 2023 US Senate AI Insight Forum (cited on LessWrong as giving 1% in 100 years).
     - EqualAI podcast: https://equalai.transistor.fm/episodes/andrew-ng-should-we-fear-an-ai-driven-existential-crisis
     - February 2026 Fast Company interview ("many decades away", known only through https://awesomeagents.ai/news/andrew-ng-agi-training-bubble-fact-check/)
     - vneconomy.vn report of 2026-08-05
     - OODA Loop brief of a Financial Times interview
     - Information Age on his tweet about extinction risk
     - Lex Fridman podcast #73 (2020)
     - O'Reilly podcast, 2024-05
   - **Leads I tried but could not read:**
     - TIME / ACM reprint 212068 (403 error and a verification wall).
     - Hedge Fund Alpha, 2015-09-23 (login wall).
     - The Megyn Kelly Show ep. 151 transcript on podscripts.co (connection refused).
     - insideHPC, Intel AI DevCon 2018 (no response).
     - Martin Ford's 2018 book "Architects of Intelligence" (no legitimate readable copy).
     - His "evil superintelligence ... Mars" tweet (I could not find the tweet id or date).
   - **Outlets not checked:** his X and LinkedIn accounts, and podcasts in general.

3. **Judgment calls where the method was silent.**
   - **What "killer robots" means.** For the "evil AI" and "killer robots" remarks (ng-2015-01, ng-2015-02, ng-2016-01) I coded the target as superintelligence, because he was answering fears of super-intelligent AI. I marked them ambiguous, since the words themselves name no capability.
   - **A borderline row.** ng-2016-01 (a Fortune report of the Mars remark) only just qualifies. I kept it rather than drop it.
   - **"Remains far away".** In ng-2022-02 this phrase gives no unit of time, unlike "decades away". I coded it like the Altman row altman-2015-03 ("a long, long way"): the capability is disputed now and the endorsement is left unexpressed.
   - **"At least decades away".** In ng-2024-01 no number of decades is given. I coded it as accepts with a qualitative timeline and no lower_bound tag, because that tag needs a year.
   - **Route plus a near date.** ng-2025-03 ("hype that LLMs are a path to AGI in just a few years") rejects both a route and a near date. I coded it as rejects for that horizon and marked it ambiguous. There is no not_by year, because "a few years" is not a number.
   - **Fields taken from outside the stored quote.** ng-2022-01 takes its affect, consequence and agency codes from elsewhere in the same letter, and the notes say so.
   - **Letters not recorded.** The Batch letters about extinction risk alone were treated as consequences only, so not qualifying.
   - **Notes text to correct.** The notes for ng-2022-01 should say medium for coding_confidence, but the field itself is set to high. The coordinator may want to set the field to medium.

4. **Quick checks** (each source opens and the quote is on the page):
   - ng-2024-01: https://www.deeplearning.ai/the-batch/issue-232/
   - ng-2025-02: https://www.deeplearning.ai/the-batch/issue-327/
   - ng-2015-01: https://www.theregister.com/2015/03/19/andrew_ng_baidu_ai/

5. **Checker:** `OK: speakers.csv 50, statements.csv 173, aggregates.csv 200, world_measures.csv 97, events.csv 31, search_log.csv 869` (no PROBLEM lines). The rows are the 14 statements and 104 search-log rows above, with no incidental rows.
