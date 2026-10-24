# "Black October": what was checked, and whether it belongs on the site

Written 2026-10-23. Status: **ruled by John on 2026-10-23** (see the last section). It answers his
request of 2026-10-23 ("Let's do a review of the current Black October cybersecurity situation
... I think it might be relevant to discuss as a news article on the AGI Zeitgeist site"). It
also checks a private brief he saved the same day, which is held in his own records and not
published here. The brief's facts were treated as leads, and each one was checked against a page
opened on 2026-10-23. Where a page could not be opened, this note says so.

**The recommendation: no news post on this site, for now.** The site's news rule allows a post
only when the site's own record changes (rule 4.11 of the family's tracker pattern;
`scripts/check_news.py` refuses a post that names no record). Black October changes no part of
the test, settles no claim and adds no panel statement. The two decisions the brief left for
John, and his rulings on them, are at the end.

## What "Black October" is

It is a nickname from social media, not an official name. It groups between 15 and 27 separate
security incidents that were disclosed between about October 14th and October 23rd, 2026. Many of
these attacks began weeks earlier, so the jump is mostly in disclosures, not in new attacks.

- **The name.** Business Today quotes an X post by the AISafetyMemes account on October 22nd,
  2026, which says "'Black October' they're calling it", so the name was already going round.
  Yahoo's newsroom searched X twice and could not find the post said to have started it. Nobody
  knows who coined it.
- **Who grouped the incidents together.** Two of the pages that list them are blogs by companies
  that sell security products (QNu Labs and SecuCenter). One of them states "Underneath all of it
  was AI", but its own list of incidents does not back that up. SecurityToday, a news site, writes
  that "the week's warnings do not attribute the surge itself to AI."

## What is confirmed, and by which page

| Item | What the opened page says | Page |
|---|---|---|
| PHP2Shell, two flaws in PHP, the programming language behind many websites | The flaws can let someone take over a web server without logging in. PHP released fixed versions 8.5.12, 8.4.27, 8.3.36 and 8.2.35 on October 21st, 2026. A further PHP notice on October 23rd, 2026 gives a setting change for a third, related flaw. | [php.net](https://www.php.net/) |
| Who found PHP2Shell | Calif says it found the first route in on August 1st, 2026 and reported it to PHP on August 11th. Ryan Austin wrote the report, and he worked with an AI assistant. Calif says "No special harness, or access to models that weren't generally available" was used. | [Calif's report](https://calif.io/php2shell) |
| | Wiz says it found the first flaw on August 19th, 2026, using frontier AI models and its own tool. It also says "a single researcher completed in a week" what used to take a team months. | [Wiz's report](https://www.wiz.io/blog/php2shell-php-rce) |
| The UK's warning | The UK's National Cyber Security Centre published an alert on October 21st, 2026. It says to update now, and to "consider taking the system offline" only if the stopgap fixes cannot be applied in time. | [NCSC alert](https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php) |
| Storm-0940 and ARTEX | On October 21st, 2026, Microsoft wrote that it "assesses that Storm-0940", a group it calls "China-state aligned", was behind the ConnectWise compromise. The group used ARTEX, "an open-source penetration testing framework" in which AI agents carry out the attack. Microsoft says ARTEX was used "to attempt to sign-in to more than 2,250 tenants", meaning organisations' Microsoft 365 accounts, and that some attacks reached administrator-level access in "less than 3 hours". | [Microsoft's report](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/) |
| | Wiz, on October 22nd, 2026, says its own observations "overlap with Microsoft's recent report". It also says the developer stopped publishing ARTEX's code on October 8th, 2026. | [Wiz's ARTEX report](https://www.wiz.io/blog/artex-in-the-wild-storm-0940-expands-targeting-of-it-and-software-vendors) |
| Monthly count of newly registered software flaws | For 2026: June 7,815; July 9,756; August 12,255; September 14,930; October 13,002 up to October 22nd. The page says three causes are mixed together in the rise: AI-assisted discovery, more organisations allowed to register flaws, and older records being filled in. It says "the published record cannot separate them." | [CRACI's trends page](https://craci.com/resources/CVE-publication-trends) |

## Figures going round that the sources do not support

- **Microsoft's monthly patch counts.** A chart going round gives rounder and different figures
  from those on Senserva's patch page, which counts 157 flaws fixed in October 2025, 537 in July
  2026, 1,169 in September 2026 and 1,771 in October 2026
  ([Senserva](https://senserva.com/patch-tuesday.html)). Computer Weekly's article on the same
  rise could not be opened.
- **"2,900 attempts per minute."** In Microsoft's text, 2,900 per minute is the failure rate in
  a separate password-guessing campaign that peaked on October 11th, 2026. Only a picture caption
  ties it to the 2,250 accounts.
- **"Bypassing multi-factor login."** Microsoft says the attackers got in "without requiring an
  interactive user sign-in". It does not use the words multi-factor.
- **Which AI models ARTEX ran on, and the files left on the attacker's server.** Neither
  Microsoft nor Wiz says either thing. Only AI Weekly does, and it cites The Hacker News
  ([AI Weekly](https://aiweekly.co/alerts/artex-developer-closes-ai-pentest-tool-after-korea-bank-hacks)).
  Under the site's rules these are second-hand.
- **"Only about 0.23% of 2026 flaws seen exploited."** This figure comes from a blog post that
  carries no date ([remio](https://www.remio.ai/post/mitre-cve-record-shows-ai-finding-security-flaws-faster-than-teams-can-triage-th)).
  The post places the figure next to a Google analysis but does not attribute it to Google.
- **"PHP runs roughly 70% of websites."** Wiz states this and cites no source for it.
- **Not opened:** Jason Clinton's posts, because X refused the fetch, so no link exists yet for
  "~18 months" or "vulnzero". Also not opened: Chris Krebs on CNBC, both CNBC articles, Axios,
  Forbes, Computer Weekly, and the statements from OpenAI and its president, Greg Brockman.
  Berkeley's page loaded with no figures on it.
- **Still disputed:** whether PHP2Shell is being exploited in the wild. One security firm says
  yes. The PHP, Dutch national cyber centre and UK pages that were opened confirm no case.

## The AI link

The link is real, and it is the clearest this record has seen. AI helped people find the PHP
flaws. In a separate case, attackers working for a state used an open-source AI agent system
against real organisations, and Microsoft says so in its own name. Most of the other incidents
in the bundle show no AI role.

## Against the site's own rules

- **The four parts of the test** are how fast AI's abilities are growing, what forecasters
  expect, whether AI is doing AI research, and whether the economy has changed gear. None of
  them moves. Finding bugs is not AI research, and nothing here is on the measure of how long a
  task AI can do.
- **The claims page.** Two of Dario Amodei's predictions are about AI hacking. Neither is
  settled. One needs a model that anyone can download and that hacks as well as Anthropic's
  Mythos Preview. ARTEX is open-source, but the models it ran on are not shown to be that good.
  The other needs AI agents able to take over "the entire internet" with a botnet.
- **The panel.** None of the 37 panel members, and none of the 15 company leaders the claims page
  follows, has spoken on it in the searches run today. Jason Clinton is Anthropic's head of
  security and is on neither list. Greg Brockman is not on the list of company leaders either.
- **The events list** takes open letters, government actions, reports, public statements and
  AI releases. Monday's weekly reading (October 26th, 2026) is the place to decide, under its
  own rules, whether Microsoft's report or the government advisories become a row. Even if one
  does, adding an event row is not one of the six things that earn a post.

## The two decisions, and John's rulings

**1. "Finalise the prominent-figure procedure so the Clinton statements can be logged under it."**
The procedure already exists and is already ruled: it is tip intake (`docs/tip-intake.md`,
amendment A29, widened by A32). It says plainly that people on no tier are not coded, and that
they are listed for the next review of the panel. So Clinton's words cannot go into the record
as statements unless the frozen panel changes. The panel was frozen on 2026-10-06 so that it
could not drift toward the story (A18). He also does not qualify for the claims page, because
that page covers the people who run the companies (A30).
**Ruled by John on 2026-10-23: "agreed".** Clinton is put forward for the next panel review
(`docs/panel-candidates.md`), and his statements are not coded. The recommendation he agreed
to was this: leave the procedure as it is. Put Clinton on the list for the next panel
review, and start the list file the procedure names (`docs/panel-candidates.md`, which does not
exist yet). Once his posts can be opened, his "~18 months" horizon can be kept there with its
link, so it is not lost. If John wants statements like his on the record, the honest route is
to rule that insiders who are not company leaders get their own list, the way A30 made one for
company heads. That would be a new amendment, and it would be his decision.

**2. "Post now while the term is live, or wait for the vanguard pilot to supply its own figure."**
**Ruled by John on 2026-10-23: no news post here; an essay on the Sentient Horizons blog
instead,** in its series of short pieces on the frontier. The recommendation was neither, as a
news post on this site. Posting now would break the news rule,
because nothing on the site has moved. Waiting for the vanguard pilot would not fix that either.
The vanguard is the site's sample of enthusiast forums (r/singularity so far). A before-and-after
around October 22nd would need a fresh pull of that forum and coding under the vanguard rules,
and would become a post only if it revised a figure the site shows. If John wants to write about
this week, two routes fit the rules:

- An essay on the Sentient Horizons blog. The brief itself named that site, and the angle it
  suggests fits an essay: AI risk moving from speculation to the work of patching and taking
  systems offline, told through counts anyone can pull again.
- A ruling that adds a seventh kind of post to this site: "widely reported, moved nothing". The
  family's held-steady idea (tracker pattern rule 4.3) is the precedent. A post of that kind
  would set out what was read against the test and why nothing moved, which the family's rules
  call the most credible thing a tracker can publish.
