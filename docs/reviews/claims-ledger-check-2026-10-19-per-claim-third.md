# Claims ledger check, third round, per-item results (2026-10-19)

The named fixes of the second pass, confirmed at the sources at commit 4bc00cc by two helpers of the checking session. Summary: claims-ledger-check-2026-10-19.md beside this file, section "Third round".

## Hassabis, Amodei and Suleyman items

# Third-round confirmation, helper a (five files)

Checked 2026-10-19. Nothing in the repository was edited. Downloads are in new folders under the scratchpad:
- `dl3-a-1`: the 2011 talk's captions, from yt-dlp. The only English tracks are automatic ones (`en-orig`, `en`); the uploader supplied no track.
- `dl3-a-2`: the arXiv pages, the version-1 PDFs and the ar5iv text of the two 2016 papers, plus the SCAN, Progressive Networks and CAD2RL abstract pages.
- `dl3-a-3`: two failed attempts to read the 2017 Neuron review. Cell's bot check blocked one; ScienceDirect returned 403 Forbidden to the other.
- `dl3-a-4`: Google's posts of December 2024, the Gemini API changelog, and the TestingCatalog report.
- `dl3-a-5`: LiveBench version 1, and the LMSYS post read through api.fxtwitter.com.
- `dl3-a-6`: the GPT-5 system card PDF, with its text pulled out through macOS PDFKit, and the BBC page.
- `dl3-a-7`: the Darwin Gödel Machine abstract page and the version-1 HTML.
- `dl3-a-8`: the Progressive Networks full text and the DeViSE abstract.

---

### 1. 2011-01-hassabis-transfer-learning-concepts-five-years — NOT CONFIRMED (the conceptual half fails his own definition; the transfer half is weak but defensible)

**(a) Does the test quote his definitions faithfully? Yes.** In the automatic captions:

- *Conceptual knowledge*, 22:32 to 24:29:
  - 23:57: "the next level above is what I'm calling conceptual so this is now when information has been slightly abstracted".
  - 24:05 to 24:15: "perceptual might be what a dog looks like ... physically ... conceptual information about a dog might be things like it it's a mammal makes a good companion".
  - The test's paraphrase ("abstracting information above the raw percepts, as 'it's a mammal' is above what a dog looks like") is faithful.
- *Transfer learning*, 35:10 to 35:42:
  - "in Psychology what's called transfer learning".
  - "we ex ract the the underlying rules behind why that worked and then ... apply it correctly in a completely new perceptual context one that looks completely different".
  - The test's paraphrase is faithful.
- The quote itself is verbatim at 39:10 to 39:18.
- The upload date is 20111212.

**Context the test leaves out**, which decides part (b). Just after the definition, at 24:39 to 26:10, he says perceptual-level hierarchical networks already exist and do well:
- He names "deep belief networks", "H Max" and "htn".
- What is missing is abstracting perceptual information "to something that isn't directly tied to the to the sensory inputs".
- "none of them so far have been able to generate abstract information ... abstracted away from the actual percepts themselves".
- He places this conceptual level in the brain in "the interaction between the hippocampus ... and higher level cortex" (26:41 to 26:51).

**(b) Conceptual half: Higgins et al., arXiv 1606.05579. Version 1 was submitted 2016-06-17 16:19 universal time, and all eight authors are Google DeepMind.** I judge that this does not meet his definition:
- The factors it discovers (position, scale, rotation, shape, "objectness") are properties of what an object looks like and where it is. That is his *perceptual* example ("what a dog looks like ... physically"), not his conceptual one ("it's a mammal, makes a good companion").
- The model is a variational autoencoder, which rebuilds the image from its learned factors. The factors are therefore, by construction, "directly tied to the sensory inputs". That is exactly what he said conceptual knowledge is not.
- The paper places its mechanism in "the ventral visual stream in the brain", a sensory pathway. He placed conceptual knowledge in the hippocampus and association and prefrontal cortex.
- DeepMind's own follow-up, SCAN (arXiv 1707.03389, 2017-07-11, also by Higgins), describes this kind of output as "disentangled visual primitives". It "learns concepts" by grounding them in those primitives. On the maker's own later framing, the 2016 work sits below concepts.
- The paper calls its factors "early visual concepts". The ledger's test is his definition, not the paper's word. "Some kind of" lowers the level he asked for, but not the kind of knowledge.

**(b) Transfer half: Rusu et al., arXiv 1610.04286. Version 1 was submitted 2016-10-13 22:42 universal time, and all six authors are Google DeepMind.** I judge this weak but defensible:
- The real robot's camera view looks different from the simulator's, and the task (reaching a target, rewarded) is carried across. That fits his "rewarding response ... in a completely new perceptual context" in spirit.
- But the policy is not applied "correctly" as it stands. A new network column is trained on the real robot for "approximately 60000 steps (about four hours)" and reaches 34 points.
- The transfer is a learning speed-up, which is transfer in the machine-learning sense, not his psychology sense of applying learned rules correctly in a new context.
- The quote "transfer learned policies from simulation to the real world" is verbatim in the abstract.

**Better records from 2011 to 2016, as he asked:**
- *Transfer*:
  - CAD2RL (Sadeghi and Levine, Berkeley, arXiv 1611.04201, 2016-11-13) trained a flying policy entirely on simulated images and flew a real quadrotor "without a single real training image". The trained skill is applied to a new-looking world with no retraining, which is a closer fit to his words. It is an outside record, so it would also change `evidence_by` to outside and `verdict_on` to 2016-11-13.
  - DeepMind's own Progressive Neural Networks (arXiv 1606.04671, 2016-06-15) includes "Pong Soup": the same Pong game with altered visuals (noise, black or white background, zoom, flipped). That is the same rules in a new-looking context, but again it uses new learning.
- *Conceptual knowledge*: I found no clearly better 2011 to 2016 record.
  - The nearest is DeViSE (Frome et al., Google, NeurIPS 2013). It links images to "semantic information gleaned from unannotated text" and labels classes it never saw. That attaches knowledge beyond appearance to percepts, but the knowledge comes from text rather than being abstracted from the percepts.
  - DeViSE was also Google Research's work, before Google bought DeepMind in January 2014, so it is outside evidence.
  - DeepMind's own explicit attempts at grounded concepts (SCAN, 2017-07-11; grounded language in a simulated 3D world, June 2017) come after the 2016-12-31 due date.
- I could not open Hassabis and colleagues' Neuron review of July 2017, "Neuroscience-Inspired Artificial Intelligence", after two attempts. It may say whether he thought these were still open in 2017, so it is worth reading before John rules.

**Dates and `evidence_by`:**
- `when` 2011-01, `due` 2016 and `verdict_on` 2016-10-13 (the later of the two papers) are all consistent.
- `evidence_by = maker` is right for the two papers cited, since both are DeepMind work.
- `verdict_source` names only the Rusu paper. The Higgins paper, which the conceptual half rests on, appears only in the reason and in the search-log row for this re-check (`hassabis-claims-061`).

**Verdict: the hit fails as filed.** The transfer half can stand, with CAD2RL the stronger record. The conceptual half is not met under his own definition, and a hit needs every condition. Under the test as now written, this is a "did not come true" (`missed`, judged 2016-12-31), unless John rules that "some kind of" admits the 2016 factor-learning work. This should go to John as a judgement, with the reason saying both readings. Whichever way he rules, two changes are needed:
- Name the Higgins paper as a source.
- Stop describing position, scale and rotation as "abstracted" above the percepts. On his definition, they are perceptual.

---

### 2. 2024-05-14-hassabis-astra-capabilities-gemini-app-later-this-year — CONFIRMED (one sourcing note)

- **The test text did not change.** `git show 4953661` changes only these fields: `status`, `verdict_on`, `verdict_why`, `verdict_source`, `direction`, `search_ids` and `notes`. The `quote`, `prediction`, `bar` and `due` lines are untouched.
- **The verdict source is right.** `blog.google/.../google-gemini-ai-update-december-2024/` is dated "Dec 11, 2024". It says: "we're also releasing a new Multimodal Live API that has real-time audio, video-streaming input". Google's developer post of the same day ("The next chapter of the Gemini era for developers", 2024-12-11) says: "Developers can now build real-time, multimodal applications with audio and video-streaming inputs from cameras or screens". The Gemini API changelog, dated December 11, 2024, lists "Bidirectional streaming with our Live API" in the public preview.
- **The AI Studio "Stream Real-Time" date.** It rests on press coverage. TestingCatalog (Alexey Shabanov, 11 Dec 2024) says: "Google AI Studio received a couple of significant updates today. One of them, called Stream Real-Time ... users can screen share or open their cameras". Google's own record of streaming inside AI Studio, in what I found, is the developer post of 2024-12-23: "Experiment with Multimodal Live Streaming directly in Google AI Studio", and the Live API "is available in Google AI Studio and Gemini API".
- **The hit stands either way.** Google's 2024-12-11 records show the publicly available live camera and screen streaming, in a public Google product, on that day. The 2024-12-23 post shows it inside AI Studio, still before 2024-12-31. `verdict_on` 2024-12-11 is supported.
- **Optional wording fix.** The reason could say that the AI Studio date of 2024-12-11 comes from a same-day press report, confirmed by Google on 2024-12-23. Today it reads as though Google's own post says so. All three pages are already in the search-log row for this re-check (`hassabis-claims-062`).

---

### 3. 2024-amodei-new-model-most-intelligent-by-airing — CONFIRMED

- **LiveBench version 1:**
  - arXiv 2406.19314 version 1 was submitted "Thu, 27 Jun 2024 16:47:42 UTC".
  - Its text says: "claude-3-5-sonnet-20240620 performs the best across all six categories and performs the best overall, 6% better than all other models."
  - Its table gives Claude 3.5 Sonnet 61.2 overall, against 55.0 for gpt-4o-2024-05-13.
  - The authors are not Anthropic (Colin White and 14 others), so it is outside.
- **LMSYS post.** Posted Mon Jun 24 19:59:05 +0000 2024: "securing the #1 spot in Coding Arena, Hard Prompts Arena, and #2 in the Overall leaderboard". The post does not itself name GPT-4o as first. That rests on the VentureBeat lead in the ledger's search log (`amodei-claims-072`), which is acceptable.
- **The reason states both rankings correctly:** second overall on the Chatbot Arena, first in coding and hard questions; first overall on LiveBench, whose paper was posted 2024-06-27.
- **The search-log row exists.** `amodei-claims-084` is in `data/search_log.csv` (line 4908). It names arxiv.org/html/2406.19314v1, quotes the same sentence, and calls the outside record split.
- **Minor, no change needed.** The LiveBench paper post-dates `verdict_on` (2024-06-26) by a day. That is harmless, because the miss rests on the split, not on LiveBench's date.

---

### 4. 2024-02-20-suleyman-hallucinations-largely-eliminated-next-year — CONFIRMED

- **GPT-5 system card** (cdn.openai.com/gpt-5-system-card.pdf, dated "August 13, 2025"), section 3.7, Figure 1, "Factuality on ChatGPT Production Traffic (Browsing Enabled)". The "% responses with 1+ major incorrect claims" bars are 22.0%, 20.6%, 11.6% and 4.8%. The text pins down which bar is which model:
  - "gpt-5-thinking has 78% fewer than OpenAI o3": 22.0 × 0.22 ≈ 4.8.
  - "gpt-5-main has 44% fewer ... than GPT-4o": 20.6 × 0.56 ≈ 11.5, matching 11.6.
- The file's figures (4.8% gpt-5-thinking, 11.6% gpt-5-main, 20.6% GPT-4o, 22.0% o3) and the range "4.8% to 22%" are correct.
- **The miss still follows.** The BBC media centre page (published 22 October 2025) says:
  - "more than 3,000 responses from ChatGPT, Copilot, Gemini, and Perplexity";
  - "20% contained major accuracy issues, including hallucinated details and outdated information";
  - "22 public service media (PSM) organizations".
- Even the card's best figure is about one answer in twenty with a major error, so the "largely eliminated / as accurate as web content" test is not met.
- **Wording note, no status change.** "On the maker's own count" means OpenAI here. But in the ledger, "maker" means the speaker's company (Inflection or Microsoft), so "on OpenAI's own count" would avoid confusion.

---

### 5. 2024-10-suleyman-teams-experiment-with-self-improvement-in-2025 — NOT CONFIRMED (wording only; the hit can stand)

- **Date and authors:**
  - arXiv 2505.22954 version 1 was submitted "Thu, 29 May 2025 00:26:15 UTC", which matches `verdict_on` 2025-05-29.
  - Authors: Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, Jeff Clune ("Jenny Zhang and four others" is right).
  - Affiliations: University of British Columbia, Vector Institute and Sakana AI. The file leaves out the Vector Institute, which is minor.
  - The authors are outside Microsoft, so `evidence_by = outside` is right.
- **The test matches the paper:**
  - Abstract: "a self-improving system that iteratively modifies its own code ... and empirically validates each change using coding benchmarks".
  - Text: "The DGM automatically improves itself from 20.0% to 50.0% on SWE-bench".
  - New versions are kept in an archive by their benchmark score. No person approves each change before it is kept.
- **The problem.** The reason quotes only the abstract's "(e.g., sandboxing, human oversight)" and calls it "oversight of the experiment as a whole". The paper's safety section is more specific, and the reason does not mention it: "we actively monitor agent performance and code changes, with the DGM archive providing a traceable lineage of modifications for review."
  - That is the sentence nearest to Suleyman's "a human directly overseeing it". It must be faced in the reason, as the second pass required for the left-out 4.8% figure in the Suleyman hallucination file (item 4).
  - My reading: monitoring and an archive kept "for review" are watching and after-the-fact review, not a person reviewing or approving each change before the loop goes on. So the test as written ("no person reviewing or approving each one") is still met, and the hit can stand.
- **What must change.** Quote that safety-section sentence in `verdict_why` and say why it is not approval of each change. Optionally, add the Vector Institute to the affiliations.

---

## Counts

CONFIRMED 3, NOT CONFIRMED 2, COULD NOT VERIFY 0.

- **The 2011 Hassabis transfer-learning and concepts claim:** the conceptual half is not met under his own definition. The 2016 factors (position, scale, rotation) are his "what it looks like" perceptual level, and DeepMind's own 2017 SCAN paper calls them "visual primitives". The hit fails as filed; it goes to John as a judgement, with "did not come true" the reading the test supports.
- **Suleyman's 2025 self-improvement experiment:** the reason leaves out the paper's "we actively monitor agent performance and code changes ... for review". The hit can stand, but that sentence must be quoted and answered.

## Kai-Fu Lee items

# Third-round check, helper b: Kai-Fu Lee's files (speaker id kaifulee)

Checked 2026-10-19 against commit 4bc00cc (the Lee fixes). Repository not edited. Downloads in
`dl3-b-1` to `dl3-b-7` under the scratchpad.

## 1. 2026-09-23-kaifulee-embodied-agi-five-to-ten-more-years.toml (is the embodied-AI line Lee's?) — CONFIRMED

- `yt-dlp --list-subs` on https://www.youtube.com/watch?v=c4w3njBhYVk lists an uploader track
  under "Available subtitles": `en` (English) and `id` (Indonesian). I downloaded `en` with
  `--write-subs` only (no automatic track): `dl3-b-1/c4w3njBhYVk.en.vtt`. Upload date 20260923.
- The uploader track marks a change of speaker with a leading dash. I counted 57 dashed cues,
  which matches the builder's count. There is no dash between 1:40:06 and 1:41:01. The run is all one turn:
  - 1:40:10 "is, for cognitive tasks, when AI can do 90% of the human tasks"
  - 1:40:34 "But answering questions and doing things are quite different."
  - 1:40:38 "I think we're probably still maybe two years away from that."
  - 1:40:43 "But we'll get low-hanging fruit pretty soon."
  - 1:40:48 "And then, of course, one could say AGI should also include"
  - 1:40:52 "physical robotics and embodied AI. So that adds another five to ten years,"
  - 1:40:56 "in my opinion."
  - 1:41:01 "- Last question." (the host, first dash after the answer)
  - 1:41:13 "- Yeah. So one of the things I talk about in my book AI Native," (Lee, next dash)
- The automatic track (`dl3-b-1a`) does put ">>" at 1:40:51 before "And then of course one could
  say AGI". The uploader track, made by the video makers, overrides it. The line is Lee's.
- Notes, not failures: (a) the quote is still the automatic-caption text ("uh", "5 to 10"). The
  uploader track gives cleaner words: "AGI should also include physical robotics and embodied AI.
  So that adds another five to ten years, in my opinion." `checked_how` could name that track.
  (b) The quote leaves out "And then, of course, one could say", the words that make the line
  conditional. `prediction` already says "If ...", so this is honest, but showing "one could say"
  in the quote would let readers see the framing for themselves.

## 2. 2026-02-04-kaifulee-ai-does-ninety-percent-of-tasks-in-two-to-three-years.toml (new 2026-02-04 claim), plus the restatement links and the search log — CONFIRMED

- Source access: https://fddi.fudan.edu.cn/be/56/c18965a769622/page.htm did not answer from here.
  I made two curl attempts (40 s and 60 s timeouts), one over http and one outside the sandbox,
  and WebFetch failed too. Archive.org has no copy. Instead I read the copy that the second-pass helper saved
  earlier today (`dl2-5-fudan/page.htm`, 19:23), copied into `dl3-b-2/`. The check below therefore rests
  on that saved file, not on a live fetch of my own.
- Page facts: the title is "蒋昌建对话李开复：站在2026'多智能体上岗元年'……", with "作者：李开复 发布时间：2026-02-19"
  and "来源：李开复". The introduction says the dialogue was on 2026年2月4日, on CCTV's 《中关村对话·AI 迎春夜》, and that the text is
  "李开复博士公众号复现对谈内容，经授权转载" (his public account's reproduction, reposted with permission).
- Section "04 AGI之争", his answer to the host's LeCun-versus-Hassabis question, reads: "但我可以很确定地预测，在未来两到三年内，将出现一个'令人惊艳的AI'，它能够完成人类90%的任务，并且比90%的人类做得更好。我认为这一定会发生。"
  The file's quote matches word for word, starting at 在未来. "可以很确定地预测" is quoted correctly in the notes.
- Date: `when` = 2026-02-04 is the day of the dialogue. Correct.
- Test: "do 90% of human tasks better than 90% of people" is his own named comparison. Correct.
- Due year: 2026-02-04 plus two to three years gives 2028 to 2029. The file has due 2029 and early end 2028. Correct.
- `restates` points to 2025-10-02-kaifulee-ai-better-than-ninety-percent-in-five-years (about five years, the same test). Correct.
- 2026-09-23-kaifulee-agi-about-two-years.toml now has `restates` pointing to the new 2026-02-04 file. Correct.
- Search log: row kaifulee-claims-060 (the first Fudan read) was **not edited** and still does not list
  this claim. The record is a new row, kaifulee-claims-084 (the re-read of section 04). It quotes the
  claim and says where it is recorded. It also logs as left out "如果我们能基于AI，在5年内将人类能创造的价值放大100倍"
  (a conditional, 'if') and the hardware line "我预计未来数年必将迎来高潮" (undated, and about hardware). Both lines are in the
  source as quoted (hardware line in section 02; hundredfold in section 04). The claim file's `search_ids`
  list both 060 and 084. Adding a re-read row instead of rewriting an old row fits a search log, so I
  count this as done. If the owner wants row 060 itself complete, one sentence pointing to row 084 would do it.
- Notes, not failures: (a) `source_kind = "transcript"`. The text is a printed reproduction of the dialogue,
  not a recording anyone checked, so `printed_qa` would describe it better. This changes no count.
  (b) The older file 2025-10-02-kaifulee-ai-better-than-ninety-percent-in-five-years.toml still says only
  "Restated on 2026-09-23". It could also name the 2026-02-04 restatement.

## 3. 2024-11-10-kaifulee-gpt5-not-within-six-months.toml and 2024-11-10-kaifulee-consumer-ai-apps-explode-first-half-2025.toml (Qianwang interview upgrade) — CONFIRMED

- Fetched https://news.qq.com/rain/a/20241105A04EME00 (curl, `dl3-b-3/qq.htm`). Its metadata reads `"media":"腾讯新闻潜望"` and
  `"pubtime":"2024-11-05 13:21:22"`. The page reads "2024-11-05 13:21发布于北京腾讯新闻《潜望》官方账号", "主笔作者 | 张小珺", and
  "以下是对话全文。（为方便阅读，作者做了一些文本优化）". It is a printed question-and-answer text, so `source_kind = "printed_qa"` is right.
- Which source: the brief calls it "Tencent Tech's WeChat post, linked from Recode China AI". The files
  actually cite the Tencent News page of the same Qianwang account, not the WeChat post. `checked_how` says
  so, and also says the WeChat page showed only a verification page. Both are the Qianwang account's printing,
  dated 2024-11-05. The second pass gave the WeChat timestamp as 13:51 Beijing time; the Tencent News page says
  13:21. The date is the same either way.
- GPT-5 file: under the heading "OpenAI还藏了很多牌", Lee says "本来GPT-5应该现在已经出来。现在看，即便出来，最快也是半年后了。" This matches the quote word for word.
  The English rendering is faithful. "Because its training had not gone smoothly" is from the line just before
  ("它GPT-5训练得不是很顺利"). The due date 2025-05-31 follows the month rule.
  The verdict holds: OpenAI's "Introducing GPT-5" page has the published time "Thu, 07 Aug 2025 14:48:06 GMT",
  which is after 2025-05-31. The status `hit` stands.
- Consumer-apps file: under the heading "AI应用会在明年上半年爆发", the host asks "全球来看应用会什么时候大爆发？" and Lee
  answers "2C应用应该就是明年前半年。" This matches the quote. The reason in `prediction` (inference costs low
  enough) is from his next answer, "从推理成本可以算出来". Faithful.
- `when_note` on both files explains that the words were printed on 2024-11-05, that the audio podcast came on
  2024-11-10, and that the record keeps 2024-11-10 because its id is fixed. Clear and correct.
- The seven-year AGI line is printed as "如果说AGI必然发生，我们假设它是7年以后发生". That is a supposition, and search row
  kaifulee-claims-087 rightly leaves it out.

## 4. 2024-11-26-kaifulee-ai-apps-proliferate-within-two-years.toml and 2024-11-26-kaifulee-flood-of-ai-apps-in-2025.toml (WIRED byline) — NOT CONFIRMED

- The byline is now stated correctly. The WIRED page (curl, `dl3-b-4/wired.htm`; `datePublished` 2024-11-26T06:35-05:00)
  has the author note "Kai-Fu Lee is the CEO of Sinovation Ventures and author of AI Superpowers." "01.AI" appears
  nowhere on the page, and the column says "I'm backing a team". Both files' `occasion` and `notes` now say this correctly.
- **New error, in both files.** The notes say "01.AI's own repost on news.qq.com, 2024-12-17". `checked_how` says
  "01.AI's account reposted it". I opened https://news.qq.com/rain/a/20241217A04FX900: its metadata reads `"media":"李开复"`, so it is
  **Lee's own Tencent News account**, not 01.AI's. The repost does sign the column "CEO of 01.AI and Chairman of Sinovation Ventures"
  (in Chinese, "零一万物 CEO、创新工场董事长"), so the role point stands. Fix: say "his own account's repost".
- **Named fix not made, in the flood file.** 2024-11-26-kaifulee-flood-of-ai-apps-in-2025.toml still says "Restates the
  Qianwang forecast of 2024-11-10". The second pass asked for 2024-11-05, the date the words were printed, which item 3 now uses.
- The verdicts and counts do not change.

## 5. 2024-03-kaifulee-hallucination-solved-in-eighteen-months.toml (OpenAI citation and Vectara figures) — NOT CONFIRMED

- The OpenAI citation is correct. The page https://openai.com/index/why-language-models-hallucinate/ (via r.jina.ai) is titled
  "Why language models hallucinate". It reads "GPT‑5 has significantly fewer hallucinations ... but they still occur. Hallucinations remain a
  fundamental challenge for all large language models". A web search gives its date as 2025-09-05, with the paper
  (arXiv 2509.04664) dated 2025-09-04. `verdict_source` now points to this post. The status `missed` and its date stand.
- Vectara's figures are only partly right. Source: the README at https://raw.githubusercontent.com/vectara/hallucination-leaderboard/main/README.md,
  "Last updated on October 16, 2026".
  - These parts are right: "about 6.5% to 14%" for current frontier models (gpt-6-sol 6.5%, gpt-5.4 7.0%, Claude Opus 4.7 12.0%,
    Gemini 3 Pro 13.6%, Kimi K2.5 14.2%), and Gemini 3 Pro at 13.6%.
  - **Wrong:** "only some small models score below 6%". Several large models from earlier generations also score below 6%: Llama 3.3 70B 4.1%,
    Mistral Large 2411 4.5%, DeepSeek-V3.2-Exp 5.3%, DeepSeek-V3.1 5.5%, GPT-4.1 5.6%, Grok 3 5.8%, and Amazon Nova Pro 5.1%.
  - **Selective:** "OpenAI's newest about 6.5 to 7%". OpenAI's newest rows are gpt-6-sol 6.5%, gpt-6-astra 8.7%,
    gpt-5.5 9.3% and gpt-5.4 7.0%, so about 6.5 to 9.3%. "Anthropic's Claude Opus models about 12%": the range is 10.9%
    (Opus 4.5) to 12.2% (Opus 4.6), so about 11 to 12%.
  - Suggested wording: "current frontier models ... in about 6.5% to 14% (OpenAI's newest about 6.5 to 9%, Anthropic's Claude Opus
    models about 11 to 12%, Google's Gemini 3 Pro 13.6%); the rows below 6% are mostly small or older models."
- The verdict and counts do not change. Only the reason text needs correcting.

## 6. 2024-10-kaifulee-agi-better-at-almost-everything-five-to-ten-years.toml, 2024-10-kaifulee-robot-cannot-clean-a-room-within-three-years.toml, 2025-10-30-kaifulee-company-run-by-ai-agents-five-to-ten-years.toml — CONFIRMED

Captions were re-read with yt-dlp. Neither video has an uploader track, so I used the automatic `en-orig` track. Moonshots
(https://www.youtube.com/watch?v=n1BVlDPercI) was uploaded 20241205; Astana Hub (https://www.youtube.com/watch?v=nNtan_n1BD0) was uploaded 20251030.

- **Better at almost everything (2024-10).** 56:40 to 56:55: "AGI just means something overwhelms us that does almost everything we do so much better even the
  most challenging intellectual tasks like uh inventing a new um theorem or something in physics or chemistry". At 57:04
  to 57:09: "I think it's highly likely that it will arrive in the next 5 to 10 years". The test now keeps "almost everything
  people do much better than people, including the most challenging intellectual tasks". That is his test. The locator (56:17 to 57:09) is correct, and so are the due year 2034 and early end 2029.
  The only gloss is "making a new finding" for his "something", which is harmless.
- **Robot cannot clean a room (2024-10).** At 1:00:58 Lee speaks of "these robots um that Elon Musk has shown". At 1:01:24 to 1:01:29 the host says "I'm an
  investor in figure AI" and that "figure yeah and Tesla both are projecting around a $30,000 price tag". At 1:01:55 to 1:02:05 Lee says "especially used around the home ...
  the just clean my room is one thing that I would predict in three years this robot cannot even begin to do because every
  room is different". The test now uses his words ("this robot" is the Tesla or Figure home humanoid; "cannot even begin to"), and it is scored as a
  forecast that something will not happen. That is reading 2, as ruled by John. The due date 2027-10-31 is three years from about 2024-10-19, and the month sets
  the day, as in the GPT-5 file. That is sensible. Note: the notes already say the claim "will be scored as not come true at 2027-10-31", based on Figure's
  own demonstration of 2026-03-09. His reason was "every room is different", and that demonstration does not show an ordinary home the robot had not been trained in.
  The method enters verdicts only when the date passes, so this sentence could be softened to "this may decide it; to be judged at 2027-10-31".
- **Company run by AI agents (2025-10-30).** 6:45 to 7:01: "So now you've automated the whole company which is accountable to the CEO who basically tells the agent what to do.
  In reality we won't get there for another perhaps 5 or 10 years but we'll get there step by step." The test uses his words and is scored as a
  forecast that something will not happen. It is judged at the earlier end, 2030-10-31: "won't ... for another perhaps 5 or 10 years" rules out at least five
  years, so that is the date his words commit to. The due date is sensible and matches the GPT-5 file's "at the earliest" handling.
  Small point: `source_locator` ends at 6:55, but the quoted sentence runs to about 7:01.

## Counts

CONFIRMED 4 (items 1, 2, 3, 6); NOT CONFIRMED 2 (items 4, 5); COULD NOT VERIFY 0. Item 2 was checked
against the second-pass helper's saved copy of the Fudan page, because the site did not answer from here.

- Item 4: the byline is right, but both files call the 2024-12-17 news.qq.com repost 01.AI's, when it is on Lee's own account
  (`"media":"李开复"`); and the flood file still says "Qianwang forecast of 2024-11-10" instead of 2024-11-05.
- Item 5: the OpenAI citation is right, but "only some small models score below 6%" is false (GPT-4.1, Grok 3, DeepSeek-V3.1,
  Mistral Large and Llama 3.3 70B are all below 6%), and "OpenAI's newest about 6.5 to 7%" leaves out gpt-6-astra at 8.7% and gpt-5.5 at 9.3%.
