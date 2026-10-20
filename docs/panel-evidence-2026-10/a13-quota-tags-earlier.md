# A13 quota tags, group f

Checked 2026-09-30 by claude-agent. Only the quota tags are done here. The earliest-statement, latest-statement and prominence checks (C1, C2, C3) are in `docs/panel-verification-2026-10.md`.

How to read this:
- Skeptic dates come from the panel-verification table, from `data/statements.csv` for the five seed speakers, or from pages fetched in this session.
- Affiliations come from Wikipedia pages fetched in this session, read through a summarising tool. Check the wording against the live page before any of it goes into `speakers.csv`.
- I applied "pre-2017" literally, so statements made in 2017 do not count toward `skeptic`. Where that rule decides the result, the entry says so.
- `non_us_uk` and `skeptic` depend on what someone said before 2017. They can't apply to people in the 2020s cohort, who by definition said nothing then.

Web searches used: 3 of 25.

### Ray Kurzweil
Tier checked: core (seed)
C1/C2/C3: see panel-verification
Quota tags: skeptic: no. His prediction before 2017 is human-level AI by 2029 and the Singularity by 2045 (2005, https://singularity.com/qanda.html) | non_us_uk: no (US) | philosopher: no | frontier_lab: arguable. He has been Director of Engineering at Google since December 2012, hired to "bring natural language understanding to Google" (fetched 2026-09-30, https://en.wikipedia.org/wiki/Ray_Kurzweil). Google was building frontier models over that time, but this is an engineering-director job, not leadership of a lab. Flag for me.

### Nick Bostrom
Tier checked: core
C1/C2/C3: see panel-verification
Quota tags: skeptic: no. In 1997 he put human-level hardware "in the first quarter of the next century", and in 2008 gave under 50% odds of superintelligence by 2033 (https://nickbostrom.com/superintelligence). | non_us_uk: no, a near miss. He is Swedish but was in the UK for all his statements before 2017: the London School of Economics (PhD 2000), then Oxford, where he ran the Future of Humanity Institute 2005–2024 (https://en.wikipedia.org/wiki/Nick_Bostrom). | philosopher: YES. PhD in philosophy, London School of Economics, 2000; Wikipedia calls him "a philosopher known for his work on existential risk" (fetched 2026-09-30, https://en.wikipedia.org/wiki/Nick_Bostrom) | frontier_lab: no

### Eliezer Yudkowsky
Tier checked: core
C1/C2/C3: see panel-verification
Quota tags: skeptic: no. In 2008 he expected "a fast, local increase in capability" (https://www.lesswrong.com/posts/JBadX7rwdcRFzGuju/recursive-self-improvement) | non_us_uk: no (Machine Intelligence Research Institute, Berkeley, US) | philosopher: no. He is self-taught with no formal degree; Wikipedia calls him an "artificial intelligence researcher" and "writer on decision theory and ethics" (https://en.wikipedia.org/wiki/Eliezer_Yudkowsky) | frontier_lab: no

### Robin Hanson
Tier checked: core
C1/C2/C3: see panel-verification
Quota tags: skeptic: YES. On 2012-08-27 he wrote "we probably have at least a century to go" for human-level AI (https://www.overcomingbias.com/p/ai-progress-estimatehtml) | non_us_uk: no (George Mason University, US) | philosopher: no, a near miss. He has an MA in Conceptual Foundations of Science from the University of Chicago, but his PhD is in social science (Caltech) and he holds an economics appointment (https://en.wikipedia.org/wiki/Robin_Hanson). | frontier_lab: no

### Geoffrey Hinton
Tier checked: core (seed)
C1/C2/C3: see panel-verification
Quota tags: skeptic: YES. In May 2015 he said "No sooner than 2070" (published 2015-11-23, https://www.newyorker.com/magazine/2015/11/23/doomsday-invention-artificial-intelligence-nick-bostrom; statement `hinton-2015-01` in `data/statements.csv`). Note that in 2016 he refused to predict "beyond five years" (`hinton-2016-01`), which is a different position. | non_us_uk: YES. He has been at the University of Toronto, Canada, since 1987 (except for University College London 1998–2001), so he was in Canada for the 2015 statement (https://en.wikipedia.org/wiki/Geoffrey_Hinton). | philosopher: arguable. Wikipedia calls him a "cognitive scientist", and he has a BA in experimental psychology (Cambridge, 1970), but his PhD is in artificial intelligence (Edinburgh, 1978). Flag for me; don't count him toward the minimum of two without a ruling. | frontier_lab: YES. Google Brain, 2013–2023, alongside his Toronto post (https://en.wikipedia.org/wiki/Geoffrey_Hinton)

### Yann LeCun
Tier checked: core (seed)
C1/C2/C3: see panel-verification
Quota tags: skeptic: YES (medium confidence). On 2015-02-18 he was asked whether the Singularity-style uploading of minds would come within 30 years. He answered "not anytime soon" and said progress "is very likely to hit some limit... and then saturate" (https://spectrum.ieee.org/facebook-ai-director-yann-lecun-on-deep-learning; `lecun-2015-01`). There is also a 2005 slide: "still quite far from rat level intelligence" (https://cs.stanford.edu/groups/nips05-AI-Workshop/LeCun-AI.pdf). His clearest statement, "still quite far from building artificial general intelligence" (`lecun-2017-01`), is from 2017, so it doesn't count under the pre-2017 rule. | non_us_uk: no, a near miss. He is French but was at NYU and Facebook in the US for all of 2005–2017 (https://en.wikipedia.org/wiki/Yann_LeCun). | philosopher: no | frontier_lab: YES. He joined Facebook AI Research in 2013 and was Meta's chief AI scientist until he left in November 2025 (https://en.wikipedia.org/wiki/Yann_LeCun).

### Yoshua Bengio
Tier checked: core (unclear in panel check)
C1/C2/C3: see panel-verification
Quota tags: skeptic: near miss, unresolved. His only interview before 2017 (MIT Technology Review, 2016-01-30, seen through a LessWrong excerpt at https://www.lesswrong.com/posts/4qPy8jwRxLg9qWLiG/yoshua-bengio-on-ai-progress-hype-and-risks) stresses how much science remains, but gives no timescale. His 2019 line "It could be ten years, it could be 100 years" is too late (https://archive.blogs.harvard.edu/toshietakahashi/?p=1291). His 2023 recollection of "decades or even centuries away" is hindsight. Don't tag him without the original 2016 interview. | non_us_uk: YES. Université de Montréal (faculty since 1993) and Mila, Canada (https://en.wikipedia.org/wiki/Yoshua_Bengio) | philosopher: no | frontier_lab: no, a near miss. He co-founded Element AI (Montreal, 2016), which never built frontier models, and later advised ServiceNow. Wikipedia lists no role at Google, OpenAI, DeepMind, Anthropic or Microsoft.

### Demis Hassabis
Tier checked: core
C1/C2/C3: see panel-verification
Quota tags: skeptic: no. His 2010 talk was titled "A systems neuroscience approach to building AGI" | non_us_uk: no (London) | philosopher: arguable. PhD in cognitive neuroscience, UCL Institute of Neurology, 2009 (https://en.wikipedia.org/wiki/Demis_Hassabis). That is neuroscience rather than cognitive science in the strict sense. Flag for me. | frontier_lab: YES. DeepMind co-founder (2010) and CEO; Wikipedia says he moved to chief scientist in 2026 (https://en.wikipedia.org/wiki/Demis_Hassabis)

### Shane Legg
Tier checked: core
C1/C2/C3: see panel-verification
Quota tags: skeptic: no. In 2009 he predicted "roughly human level AGI in the year 2025" (https://www.vetta.org/2009/12/tick-tock-tick-tock-bing/) | non_us_uk: possible, unresolved. He is a New Zealander, did his PhD at IDSIA in Switzerland (2008, thesis "Machine Super Intelligence") and a postdoc at the University of Lugano, Switzerland. He then moved to UCL's Gatsby Unit in London, and DeepMind (2010 on) is in London (https://en.wikipedia.org/wiki/Shane_Legg). Whether his December 2009 blog forecast was written in Lugano or London isn't established, and his PhD thesis or earlier blog posts from Switzerland might qualify. Needs a check. | philosopher: no | frontier_lab: YES. DeepMind co-founder (2010), now Chief AGI Scientist at Google DeepMind (https://en.wikipedia.org/wiki/Shane_Legg)

### Sam Altman
Tier checked: core (seed)
C1/C2/C3: see panel-verification
Quota tags: skeptic: no. In his 2014 blog post, AGI "might work, and if it does, it will be the biggest development in technology ever" (https://blog.samaltman.com/ai) | non_us_uk: no | philosopher: no | frontier_lab: YES. OpenAI co-founder (2015), CEO 2019 to now (https://en.wikipedia.org/wiki/Sam_Altman)

### Gary Marcus
Tier checked: core (seed)
C1/C2/C3: see panel-verification
Quota tags: skeptic: YES. On 2016-05-04 he said robots "aren't going to be [as clever as HAL] for at least thirty or fifty years" (https://www.edge.org/conversation/gary_marcus-is-big-data-taking-us-closer-to-the-deeper-questions-in-artificial; `marcus-2016-01`). There is also a December 2014 paraphrase saying the threat is "still many decades off" (`marcus-2014-01`). | non_us_uk: no (NYU, US) | philosopher: YES. Cognitive scientist by training (PhD in cognitive science, MIT, 1993) and by appointment (psychology and neural science professor at NYU) (https://en.wikipedia.org/wiki/Gary_Marcus) | frontier_lab: no, a near miss. He directed Uber AI Labs 2016–2017 after Uber bought his start-up Geometric Intelligence, but Uber was not building frontier models.

### Andrew Ng
Tier checked: core
C1/C2/C3: see panel-verification
Quota tags: skeptic: YES (medium confidence). On 2015-03-19 he said: "There could be a race of killer robots in the far future, but I don't work on not turning AI evil today for the same reason I don't worry about the problem of overpopulation on the planet Mars" (https://www.theregister.com/2015/03/19/andrew_ng_baidu_ai/). He gives no number of years; "far future" is the only timescale. | non_us_uk: no, a near miss. He was chief scientist of Baidu, a Chinese company, from 2014 to 2017, but the 2015 talk was in San Jose, California, and Wikipedia doesn't say he was based in China (https://en.wikipedia.org/wiki/Andrew_Ng). | philosopher: no | frontier_lab: YES. Founded and directed the Google Brain deep learning project 2011–2012; Baidu chief scientist 2014–2017 (https://en.wikipedia.org/wiki/Andrew_Ng)

### Stuart Russell
Tier checked: core
C1/C2/C3: see panel-verification
Quota tags: skeptic: no. His 2014 co-written piece treats superhuman AI as physically possible and a serious risk (https://www.huffpost.com/entry/artificial-intelligence_b_5174265) | non_us_uk: no. He is British but based at UC Berkeley in the US (https://en.wikipedia.org/wiki/Stuart_J._Russell) | philosopher: no. Physics BA, computer science PhD | frontier_lab: no. All his roles are academic.

### Rodney Brooks
Tier checked: core
C1/C2/C3: see panel-verification
Quota tags: skeptic: YES. On 2014-11-11 he wrote "it is a mistake to be worrying about us developing malevolent AI anytime in the next few hundred years", and that volitional AI will take "most likely, centuries" ("Artificial intelligence is a tool, not a threat", fetched 2026-09-30, https://robohub.org/artificial-intelligence-is-a-tool-not-a-threat/). There is also 2008-06-01: "I strongly suspect it won't happen before 2030" (https://spectrum.ieee.org/i-rodney-brooks-am-a-robot). | non_us_uk: no. He is Australian but was at MIT in the US from 1984 (https://en.wikipedia.org/wiki/Rodney_Brooks) | philosopher: no | frontier_lab: no. His companies (iRobot, Rethink Robotics, Robust.AI) build robots, not frontier AI models.

### Elon Musk
Tier checked: core
C1/C2/C3: see panel-verification
Quota tags: skeptic: no. In 2014 he called AI the largest existential threat, and in 2017 wrote that the singularity "is coming soon" | non_us_uk: no (US) | philosopher: no | frontier_lab: YES. Co-founded OpenAI in December 2015 and left its board in 2018; launched xAI in July 2023 (https://en.wikipedia.org/wiki/Elon_Musk)

### Ilya Sutskever
Tier checked: core (with caveat)
C1/C2/C3: see panel-verification
Quota tags: skeptic: no. The 2015 OpenAI launch post he co-signed says only that "it's hard to predict when human-level AI might come within reach" | non_us_uk: no, a near miss. He was in Toronto for his PhD (finished around 2013), but his only statement before 2017 is from OpenAI in the US, after Google Brain in the Bay Area 2013–2015 (https://en.wikipedia.org/wiki/Ilya_Sutskever) | philosopher: no | frontier_lab: YES. Google Brain research scientist 2013–2015; OpenAI co-founder and chief scientist 2015–2024; co-founded Safe Superintelligence in 2024 and became its CEO in 2025 (https://en.wikipedia.org/wiki/Ilya_Sutskever)

### François Chollet
Tier checked: core (with caveat)
C1/C2/C3: see panel-verification
Quota tags: skeptic: near miss. On 2017-07-18 he called a "singularitarian robot apocalypse" "pure fantasy" (https://blog.keras.io/the-future-of-deep-learning.html). That is from 2017, not before it, and it is about a robot apocalypse rather than when AGI arrives. In the same post he allows that a learning system "could be interpreted as an AGI". | non_us_uk: no, a near miss. He is French but was at Google in the US from 2015 (https://en.wikipedia.org/wiki/François_Chollet) | philosopher: no | frontier_lab: arguable. Senior Staff Engineer at Google 2015–2024, where he created Keras (https://en.wikipedia.org/wiki/François_Chollet). That is a senior technical role at a frontier company, but not a research-leadership role on its frontier models. Flag for me.

### Luciano Floridi
Tier checked: core (proposed skeptic)
C1/C2/C3: see panel-verification
Quota tags: skeptic: YES. On 2016-05-09 he wrote "True AI is not logically impossible, but it is utterly implausible" (https://aeon.co/essays/true-ai-is-both-logically-possible-and-utterly-implausible) | non_us_uk: no, a near miss. He is Italian, but in 2016 his main post was at the University of Oxford, UK; his Bologna chair is current, and he has been at Yale since 2023 (https://en.wikipedia.org/wiki/Luciano_Floridi) | philosopher: YES. Wikipedia calls him "an Italian and British philosopher" of information. Yale has appointed him Professor in the Practice of Cognitive Science since 2023 (fetched 2026-09-30, https://en.wikipedia.org/wiki/Luciano_Floridi) | frontier_lab: no

### Dario Amodei
Tier checked: cohort_2020s (clears the core bar per panel-verification)
C1/C2/C3: see panel-verification
Quota tags: skeptic: no. In 2017 he said AGI "definitely will eventually happen" (https://80000hours.org/podcast/episodes/the-world-needs-ai-researchers-heres-how-to-become-one/) | non_us_uk: no (US) | philosopher: no. Physics and biophysics degrees | frontier_lab: YES. Baidu November 2014 to October 2015, then Google; OpenAI Vice President of Research 2016–2021; Anthropic co-founder and CEO since 2021 (https://en.wikipedia.org/wiki/Dario_Amodei)

### Leopold Aschenbrenner
Tier checked: cohort_2020s
C1/C2/C3: see panel-verification
Quota tags: skeptic and non_us_uk: don't apply, since he has no statements before 2017. He is German, but based in the US. | philosopher: no. BA in economics and mathematics-statistics, Columbia, 2021 | frontier_lab: near miss. He was a researcher on OpenAI's Superalignment team 2023–2024 (fired April 2024), which is a research role but not a senior one (https://en.wikipedia.org/wiki/Leopold_Aschenbrenner). Tag him only if any research role at a frontier lab counts.

### Daniel Kokotajlo
Tier checked: cohort_2020s
C1/C2/C3: see panel-verification
Quota tags: skeptic and non_us_uk: don't apply, since he has no statements before 2017 | philosopher: YES. BA in philosophy (Notre Dame, 2014) and MA in philosophy (UNC Chapel Hill, 2017), then doctoral study in philosophy at UNC; Wikipedia doesn't say whether he finished the PhD (fetched 2026-09-30, https://en.wikipedia.org/wiki/Daniel_Kokotajlo_(researcher)) | frontier_lab: near miss. He was a researcher in OpenAI's governance division 2022–2024, which is not a senior research role on the models (same page).

### Ajeya Cotra
Tier checked: cohort_2020s
C1/C2/C3: see panel-verification
Quota tags: skeptic and non_us_uk: don't apply | philosopher: no. No Wikipedia page exists (404); her background is in computer science, which I didn't confirm on a fetched page. | frontier_lab: no. She spent about nine years at Open Philanthropy (now Coefficient Giving) and is now on the technical staff at METR, an organisation that evaluates AI models rather than building them (seen in a search result, https://www.longtermwiki.com/wiki/ajeya-cotra).

### Jensen Huang
Tier checked: cohort_2020s
C1/C2/C3: see panel-verification
Quota tags: skeptic and non_us_uk: don't apply | philosopher: no | frontier_lab: near miss. Nvidia, which he co-founded and runs, makes the chips frontier labs use, not the frontier models themselves. Tag him only if supplying the hardware counts. (No page was fetched for this; it is a general fact, so cite a source before relying on it.)

### Mustafa Suleyman
Tier checked: cohort_2020s (clears the core bar per panel-verification)
C1/C2/C3: see panel-verification
Quota tags: skeptic: near miss, borderline. On 2016-12-05 in London he said: "when we say it's 20 years out or decades way, we say that it so far out, we can't really measure it" (fetched 2026-09-30, https://techcrunch.com/2016/12/05/deepmind-ceo-mustafa-suleyman-says-general-ai-is-still-a-long-way-off). He places general AI decades off and "so far out" it can't be measured, which arguably doubts it within decades. But "20 years out" falls inside the window, unlike Hinton's 2070. I to rule. | non_us_uk: no (London, DeepMind) | philosopher: no, a near miss. He studied philosophy and theology at Mansfield College, Oxford, but dropped out at 19 (https://en.wikipedia.org/wiki/Mustafa_Suleyman) | frontier_lab: YES. DeepMind co-founder (2010) and chief product officer, then head of applied AI after Google bought it, to 2019; co-founded Inflection AI in 2022; CEO of Microsoft AI since March 2024 (https://en.wikipedia.org/wiki/Mustafa_Suleyman)

## Group f tallies against the A13 minimums

- **skeptic** (minimum 6): 7 clear: Hanson, Hinton, LeCun (medium confidence), Marcus, Ng (medium confidence), Brooks, Floridi. Near misses: Bengio (no timescale before 2017), Chollet (statement is from 2017 and not about timing), Suleyman (borderline). LeCun and Ng rest on looser wording; if both fall, the count is 5.
- **non_us_uk** (minimum 3): 2 clear: Hinton (Toronto, Canada) and Bengio (Montréal, Canada). Possible third: Legg (Switzerland until about 2009), not yet checked. Other near misses were all US- or UK-based at the time: Bostrom, LeCun, Ng, Sutskever, Chollet, Floridi.
- **philosopher** (minimum 2): 4 clear: Bostrom, Marcus, Floridi, Kokotajlo (who is in the cohort, not the core). Arguable: Hinton, Hassabis. Within the core alone, 3 clear (Bostrom, Marcus, Floridi).
- **frontier_lab** (minimum 3): 10 clear: Hinton, LeCun, Hassabis, Legg, Altman, Ng, Musk, Sutskever, Amodei, Suleyman. 2 arguable: Kurzweil and Chollet. Near misses: Aschenbrenner, Kokotajlo, Marcus, Bengio, Huang.

Queries (WebSearch, 3):
1. `Rodney Brooks 2014 "artificial intelligence is a tool, not a threat" "next few hundred years"`
2. `Ajeya Cotra joins 2025 new role after Open Philanthropy`
3. `Yoshua Bengio 2015 OR 2016 interview human-level AI "decades" away superintelligence not worried`

Pages fetched: Wikipedia pages for Hinton, Bengio, LeCun, Hassabis, Legg, Ng, Kurzweil, Bostrom, Hanson, Marcus, Floridi, Chollet, Kokotajlo, Aschenbrenner, Suleyman, Sutskever, Amodei, Brooks, Musk, Russell, Yudkowsky, Altman, and Cotra (404). Also The Register (Ng, 2015), Robohub (Brooks, 2014), LessWrong (Bengio, 2016), the Harvard blog (Bengio, 2019) and TechCrunch (Suleyman, 2016). The ACM interview page with Brooks returned 403.
