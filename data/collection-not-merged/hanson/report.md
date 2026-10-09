# Robin Hanson (speaker id hanson) trace: partial, stopped by the coordinator

1. Years 2005 to 2026. I recorded 10 statements, and 1 of them is secondhand (hanson-2016-01, Open Philanthropy's third-person notes of a conversation). The search log has 100 rows: 70 web searches (3 discovery searches, the 66 year-by-year searches, and 1 extra search for a podcast transcript), the follow-ups, the own-outlet rows, and 15 quiet-year rows. Statements by year: 2010 (1), 2016 (3), 2019 (1), 2021 (1), 2023 (1), 2024 (2), 2025 (1). The quiet years are 2005-2009, 2011-2015, 2017, 2018, 2020, 2022 and 2026. No year was busy enough to need sampling.

2. What is incomplete:
   - **The year-by-year web searches are done for every year.** All three queries were run and logged for each year from 2005 to 2026.
   - **No year is fully traced, because his main outlet was not read.** That outlet is the Overcoming Bias blog. I built a list of 762 likely posts from the blog's own search, saved in raw/cands.json. Not one of them was read or checked before the stop. The blog is where most of his statements will be, for example the 2008 debate with Yudkowsky about AI improving itself (the "foom" debate), "AI Progress Estimate" (2012-08-27), "I Still Don't Get Foom" (2014), "AGI Is Sacred" (2022-08-15) and "AI Is GPT, & GPTs Go Slow" (2025-04-15). Every quiet-year row says the blog was not checked, so all 22 years should be treated as partial.
   - Leads not finished:
     - The 2011-06-30 Jane Street debate transcript, in https://intelligence.org/files/AIFoomDebate.pdf (downloaded, not read; there was no PDF text tool).
     - The Cognitive Revolution episode "Is AGI Far?" (2024-02-27). I found no transcript. The episode notes list a chapter "Achieving full human level AI in the next 60-90 years".
     - The Closer to Truth interview from MindFest 2025: https://closertotruth.podbean.com/e/robin-hanson-on-the-age-of-ai-and-large-language-models
     - The GMU news item "Can we stop runaway AI?" (2023-06), which points to a New Yorker article. The reader copy came back empty.
     - The Plausible Futures interview: https://plausiblefutures.substack.com/p/interview-with-robin-hanson-on-emulated
     - The Singularity Weblog interview: https://www.singularityweblog.com/robin-hanson-on-singularity-1-on-1/
     - The Emerj podcast listing for September 2013.
     - The Quillette essays from 2023-04-14.
     - His other posts on X.

3. Places where the method was unclear, and what I did:
   - **"Very unlikely".** For a hard takeoff (hanson-2016-01), I coded this as `rejects` and marked it ambiguous. The codebook puts probabilities below 50% under `uncertain`.
   - **"Doesn't look terribly likely".** For foom (hanson-2024-01), I coded this as `uncertain`.
   - **Loose words for AI improving itself.** "Hard takeoff" and "foom", where the AI improves itself, I coded as `si_modify` and marked ambiguous.
   - **Expert round-up answers.** I coded the written answer to Return's question for 50% confidence (hanson-2023-01) as `survey` / `survey_response`, and put the year as `point_year` 2150.
   - **Routes to AGI.** The emulation-versus-AGI bet (hanson-2021-01) is a claim about which route comes first, so endorsement is `unexpressed`.
   - **One row per occasion.** Where one interview held several qualifying passages, I kept one row and put the others in the notes, as the trial did.
   - **Transcripts with unreliable speaker labels.** The Doom Debates quote comes from Substack's machine transcript, whose speaker labels are unreliable. I quoted only a passage that is clearly in Hanson's voice.

4. Three statements that are quick to check:
   - hanson-2024-02: post on X, https://x.com/robinhanson/status/1862901360389144861
   - hanson-2025-01: post on X, https://x.com/robinhanson/status/1983924759025848362
   - hanson-2010-01: NextBigFuture interview, https://www.nextbigfuture.com/2010/08/robin-hanson-interviewed-by-sander.html

5. Checker: `OK: speakers.csv 50, statements.csv 169, aggregates.csv 200, world_measures.csv 97, events.csv 31, search_log.csv 865`, and no PROBLEM lines.

Files are in staging/hanson/: statements.csv, search_log.csv, report.md, and the build scripts stmts.py and build.py. The raw/ folder holds the fetched pages, the blog index, and the 264 post texts that were downloaded but not read.
