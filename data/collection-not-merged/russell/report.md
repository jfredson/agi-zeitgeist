# Trace report: russell (Stuart Russell, core tier)

Stopped early when the coordinator asked. Every year is either fully searched or not started, except 2019, which was partly done.

1. Summary
- Speaker id `russell`. Years fully searched (all three year searches plus follow-ups): 2005 to 2018. 2019 was searched only in part. 2020 to 2026 were not started.
- 16 statements recorded, 1 of them secondhand (russell-2015-02, a blog report of the 2015 Cambridge talk). By year: 2014 has 6 rows (two statements split into a and b rows), 2015 has 2, 2016 has 3, 2017 has 2, 2018 has 1 and 2019 has 2.
- 93 search rows, about 85 web searches used.
- Quiet years 2005 to 2013, logged as rows russell-q2005 to russell-q2013. No year went over ten statements, so no sampling.
- 2 finds about other panel members, in incidental.csv: shanahan-2015-90 (Business Insider, 2015-10-20) and ng-2017-90 (Vox, 2017-03-08).

2. What a later session needs to finish
- 2019 was searched with the three year searches only. Leads not yet followed:
  - TechCrunch talk preview, 2019-11-25 (reporter's paraphrase "a generation or two away"): https://techcrunch.com/2019/11/25/ai-expert-stuart-russell-to-join-tcs-roboticsai-2020-at-uc-berkeley/
  - CLTC Berkeley event recap, November 2019: https://cltc.berkeley.edu/?p=6671
  - Daily Telegraph, 2019-10-01, PDF on his site: https://people.eecs.berkeley.edu/~russell/research/future/articles/DailyTelegraph-10-1-19.pdf
  - Financial Times "The billion-dollar bet to reach human-level AI", 2019-08-03.
  - Guardian Science Weekly podcast, 2019-10-18.
  - C-SPAN interview, 2019-11-13.
  - HBR Exponential View podcast, 2019-06-27.
  - New York Times video "The Inevitability of general AI", 2019-12-13.
  - The "within his children's lifetime" estimate in Human Compatible. No legitimate copy of the book was found; Physics Today only paraphrases it.
- 2020 to 2026 were not started. Russell's own media list at https://people.eecs.berkeley.edu/~russell/research/future/ has the leads for each year (logged as russell-034). The main ones:
  - Reith Lectures, 2021.
  - Daedalus essay "If we succeed", 2022: https://people.eecs.berkeley.edu/~russell/papers/russell-daedalus22-succeed.pdf
  - Senate testimony, 2023-07-25.
  - Many interviews in 2023, which will probably push that year over ten statements and need sampling.
  - Newsweek, 2025-01-31.
  - Business Insider and dnyuz.com, 2026-07-27, on Altman's singularity claim.
- Sources that could not be read:
  - Science "Fears of an AI pioneer", 2015, paywalled.
  - Time, 2015-09-15: dead link.
  - TechRepublic, 2016: returned 403.
  - Sam Harris podcast transcript, 2016-11-23: podscripts.co refused.
  - Lex Fridman episode 9, 2018-12-09: no transcript.
  - Singularity.FM, 2018: returned 403.
  - TechWorld, 2017: returned 404.

3. Places where the method did not say what to do
- The sentence "AI is likely to succeed" on his undated page "The long-term future of AI" was not recorded. The page is not dated, and the sentence is already there at the first Wayback Machine capture (2014-11-09). Search row russell-052.
- Several times he argues against people who say "it will never happen" without giving his own answer. These were not recorded: Edge 2015 (row russell-045) and Vanity Fair 2017 (row russell-069). The Edge 2014 reply "Of Myths and Moonshine" was recorded (russell-2014-04, marked ambiguous), because it makes its own claim that claims of impossibility can be overturned within hours.
- In the 2014 co-written HuffPost piece, the alien analogy "We'll arrive in a few decades" was not coded as a timeline. The note on russell-2014-01a explains why.
- When one interview had several qualifying passages, I recorded one row for the main passage and quoted the others in the notes, following the worked examples. Pieces that make claims about two capabilities in one passage were split into a and b rows.
- In russell-2016-03 he reports his own answer to Oren Etzioni's survey ("more than 25 years") in an opinion piece. I coded it as source type blog and how the statement came about as survey, dated by publication (2016-11-02), with 2041 as the earliest year.
- In russell-2017-01 the "likely within this century" estimate is attributed to "most experts", so endorsement is `unexpressed` and marked ambiguous.
- In russell-2019-01 the acceptance rests on "The arrival ... will be the biggest event", which takes the arrival for granted. It is marked ambiguous.
- The two incidental rows have no search_log rows for `ng` or `shanahan`, so the repo validator flags them when merged. The coordinator needs to handle this.

4. Quick checks (the source opens and the quote is on the page)
- russell-2018-01: https://www.sciencefocus.com/future-technology/how-to-make-ai-that-works-for-us
- russell-2016-03: https://www.technologyreview.com/2016/11/02/156285/yes-we-are-worried-about-the-existential-risk-of-artificial-intelligence/
- russell-2015-01: https://www.quantamagazine.org/artificial-intelligence-aligned-with-human-values-qa-with-stuart-russell-20150421/

5. Checker
`OK: speakers.csv 50, statements.csv 175, aggregates.csv 200, world_measures.csv 97, events.csv 31, search_log.csv 858`, with no PROBLEM lines. The output also reads: russell: 16 statements, 93 search rows, 2 incidental rows.

Files are in /private/tmp/claude-501/-Users-john-Code-timeassembler/6f932b33-517c-4081-98fe-c808da1249a8/scratchpad/staging/russell/:
- statements.csv
- search_log.csv
- incidental.csv
- report.md
- build.py, rows_statements.py, rows_search.py and incidental_rows.py, which rebuild the CSVs
