# Review request: measuring how public opinion on AGI has moved, 2005 to 2026

I am building a public, citable dataset on how expert and public opinion about artificial general intelligence (AGI) has changed from 2005 to the present, plus an essay with charts built from it. The expert half is a fixed panel of named thinkers whose dated public statements are coded by which question they answer (is AGI possible, when will it arrive, is the current system already capable, can it improve itself), their timeline estimate, and their stance (dismissive through resigned), with a written sampling rule to prevent cherry-picking.

The public half is less settled, and I would like your critique and alternatives before I collect anything. The constraint is that every source must be publicly re-pullable by a reader; no personal recollection, no private data.

## The method as currently planned

Layer 1, attention: Wikipedia monthly page views for the AGI, Technological singularity and Superintelligence articles (2015 to present, older from raw dumps); Google Books Ngram yearly frequencies to 2022; GDELT news volume 2015 to present; Google Trends 2004 to present; New York Times article counts per year.

Layer 2, the public forum: the full r/singularity and r/artificial archives from 2008 (via Arctic Shift), Hacker News from 2007, LessWrong. Measures: posts per month, monthly share of comments using each term in a frozen vocabulary list (singularity, AGI, ASI, superintelligence, takeoff, recursive self-improvement, alignment, doom, p(doom), timelines, and slang like "feel the AGI"), and a coded sample of the 20 top-scoring r/singularity posts per quarter, coded with the same question and stance scheme as the experts.

Layer 3, default assumptions: polls with exact wording (Pew's concerned-versus-excited series 2021 onward, Monmouth 2015 versus 2023, YouGov items on AI surpassing humans, Ipsos global monitor, Gallup).

Layer 4, the mainstream argument: Media Cloud article counts across a fixed set of national outlets from about 2010, plus 15 opinion pieces per year chosen by a fixed rule and coded with the same scheme, to capture the move from "relax, it can't do that" to "what do we do now that it can".

Layer 5, vocabulary ledger: for each term, first appearance in books, first appearance in a national outlet, first month it passed 1% of r/singularity comments.

The headline claim being tested: the central public question moved from whether AGI is possible (roughly 2005 to 2015), to when it arrives (2016 to 2022), to whether current systems are already capable of improving themselves (2023 onward). The method is supposed to be able to show this claim is wrong.

## What I want from you

1. Where does this method fail to measure what it claims to measure? Be specific about which layer and why.
2. Which of these sources would you drop, and what would you add? I am especially interested in sources with coverage before 2015, when the public record is thinnest, and in sources that reach beyond young, technical, English-speaking men.
3. Is there a better way to put public and expert opinion on one comparable axis than coding both with the same question-and-stance scheme?
4. What is the strongest objection a skeptical reader would raise against the headline claim, and what evidence would settle it?
5. Are there existing datasets, papers or projects that already did part of this, which I should build on or cite rather than redo?
6. Anything about the sampling rules (20 top posts per quarter, 15 op-eds per year, frozen vocabulary list) that would let bias in?

Please be direct. I would rather hear that a layer is unsalvageable now than after it is collected.
