# Public track review: Gemini 3.1 Pro

Received 2026-09-30 (Pacific). Prompt: `docs/reviews/public-track-review-prompt.md`. Reply saved verbatim below; John's and Claude's reconciliation goes in `docs/amendments.md`, not here.

---

Structural Vulnerabilities in the Proposed Method
Your method attempts to capture a moving target, but your instruments are calibrated for the wrong frequencies in several layers:

* Layer 1 (Attention): Google Ngrams tracks raw lexical volume independent of semantic context. Prior to 2015, "singularity" predominantly measures astrophysics and mathematics, not AI. This layer will return severe false positives for early AGI interest.

* Layer 2 (The Public Forum): r/singularity, Hacker News, and LessWrong represent an avant-garde, highly technical rationalist subculture. Using these as your proxy for "public opinion" is a fatal sampling error. You are measuring the enthusiast timeline, not the mainstream timeline.

* Layer 4 (The Mainstream Argument): A fixed sample of 15 op-eds per year is too sparse to yield quantitative significance and highly susceptible to the coder's selection rule. It functions as qualitative illustration, not a representative dataset.

* Sampling Bias (Frozen Vocabulary): Freezing your vocabulary to modern terms (AGI, p(doom), alignment) will retroactively erase pre-2015 discourse. Before 2015, the dominant terms were "Strong AI," "Human-Level Machine Intelligence (HLMI)," "Machine Consciousness," and "Expert Systems." A frozen list guarantees the illusion that nobody cared before 2015 simply because they used different words.

* Sampling Bias (Reddit Top Posts): Sampling the 20 "top-scoring" posts per quarter measures virality, not consensus. Reddit's algorithm heavily weights hype, outrage, and meme density, distorting the actual center of gravity in those communities.

Source Revisions and Pre-2015 Baselines
To capture the actual public and reach beyond young, technical, English-speaking men, adjust your intake:

* Drop: Google Ngrams and the 15 manual op-eds.

* Add (Pre-2015 Public Forum): Prior to 2010, the mainstream public did not debate AGI in op-eds; they debated it in movie theaters. Track Box Office Mojo or TV Tropes data for "Rogue AI," "Machine Uprising," and "Cybernetics" themes. Pop culture was the primary vehicle for pre-2015 public AGI discourse.

* Add (Global/Non-WEIRD Polling): Integrate the Lloyd's Register Foundation World Risk Poll (which tracks global AI/tech risk perception across 121 countries) and the Eurobarometer surveys on robotics and AI, which provide consistent baseline data going back to 2012.

* Add (Global Media): Replace the US-centric Media Cloud with Factiva or LexisNexis searches spanning non-US English, Spanish, and Mandarin news outlets, tracking regional translations of "human-level AI."

Realigning the Comparative Axis
Coding experts and the public with the exact same capability-focused scheme (e.g., "is the current system capable of self-improvement?") will yield a broken axis. The public lacks the technical taxonomy to parse recursive self-improvement; they parse impact.

Instead of a capability axis, map both cohorts on a Proximity and Disruption Matrix:

1. Proximity: Is AGI framed as a distant philosophical concept, a medium-term engineering hurdle, or an immediate societal reality?

2. Disruption Profile: Is the primary expectation existential (extinction/utopia), economic (automation/abundance), or social (misinformation/alienation)?

Experts and the public can both be cleanly coded on how close they believe the disruption is, and what shape that disruption will take, without requiring the public to articulate algorithmic capabilities.

The Strongest Skeptical Objection
The strongest objection a reader will raise against your headline claim is Insider Projection.

Your claim posits that by 2023, the central public question moved to "whether current systems are already capable of improving themselves." A skeptic will argue this is purely an insider Silicon Valley/LessWrong obsession. The actual mainstream public question from 2023 onward is "will this replace my job?" and "is this image real?"

To settle this, your data must explicitly cross-reference the volume of capability-focused terms ("self-improvement," "alignment," "AGI") against impact-focused terms ("AI jobs," "deepfake," "automation") within Layer 4 (Mainstream Media) and Layer 3 (Polling). If the impact terms eclipse the capability terms in the mainstream data, the headline claim is isolated to Layer 2 and invalid for the general public.

Foundational Datasets to Leverage
Do not rebuild expert timeline data from scratch. Build upon these established projects:

* The AI Impacts Surveys (Katja Grace et al.): The definitive expert baseline. Utilize their 2017 "When Will AI Exceed Human Performance?" and their 2024 "Thousands of AI Authors on the Future of AI" datasets, which directly measure expert timeline shifts, extinction probability estimates, and Full Automation of Labor (FAOL) projections.

* The Stanford AI Index: A yearly aggregate that already tracks global public opinion polls, legislative mentions, and media volume regarding AI.

* Global Catastrophic Risk Institute (GCRI): Seth Baum's historical databases of AGI projects and expert probability assessments provide excellent pre-2020 expert consensus mapping.
