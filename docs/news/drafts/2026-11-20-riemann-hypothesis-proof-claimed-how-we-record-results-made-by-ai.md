---
title: A proof of the Riemann Hypothesis made with AI has been claimed. Here is how we will record results like it
date: 2026-11-20
status: draft
kind: method-changed
summary: A mathematician at Anthropic says he and its AI, Claude, have proved the Riemann Hypothesis, the most famous unsolved problem in mathematics, and has released the proof as code a computer can check. It is the latest of several results in mathematics made mainly by AI this year. They do not move the singularity test, but from now on they are listed on the claims page with how far each has been checked.
records: [A37]
before: "Results made by AI mentioned only in notes on the claims they bear on"
after: "a table of results in mathematics and science made mainly by AI, each with its check, shown on the claims page and never scored"
sources:
  - label: Levent Alpöge, "Remark", November 20th, 2026
    url: https://alpo.ge/remark.pdf
  - label: Scientific American, "Anthropic mathematician claims to prove Riemann hypothesis", November 20th, 2026
    url: https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/
  - label: Scientific American, "The AI Riemann hypothesis proof is almost certainly true, independent mathematicians attest", November 20th, 2026
    url: https://www.scientificamerican.com/article/the-ai-riemann-hypothesis-proof-is-almost-certainly-true-independent-mathematicians-attest/
  - label: OpenAI, "An OpenAI model has disproved a central conjecture in discrete geometry", May 20th, 2026
    url: https://openai.com/index/model-disproves-discrete-geometry-conjecture/
  - label: Alon and others, "Remarks on the disproof of the unit distance conjecture", May 20th, 2026
    url: https://arxiv.org/abs/2605.20695
  - label: Alpöge and Furman, "More than two thirds of the zeta zeros are simple and on the critical line", August 2026
    url: https://arxiv.org/abs/2608.13637
  - label: OpenAI, "On the Navier–Stokes Millennium Prize Problem", September 8th, 2026
    url: https://openai.com/index/navier-stokes-solution/
  - label: King's College London, "OpenAI's Navier-Stokes proof called into question", October 27th, 2026
    url: https://www.kcl.ac.uk/news/openais-navier-stokes-proof-called-into-question
  - label: The claims page
    url: https://agizeitgeist.com/claims/
---

<!-- DRAFT. Not for publishing until John rules on the proposed method change and it is
entered in the amendments file, and until the comparator run on the Riemann proof is reported.
The two paragraphs marked UPDATE are rewritten then, from the source that reports it. -->

On November 20th, 2026, [Levent Alpöge](https://alpo.ge/), a mathematician who works at [Anthropic](https://www.anthropic.com/), posted a four-page note saying that he believes he has, "working with Claude", proved the [Riemann Hypothesis](https://en.wikipedia.org/wiki/Riemann_hypothesis) ([Alpöge's note](https://alpo.ge/remark.pdf)). Claude is Anthropic's AI. The Riemann Hypothesis is the most famous unsolved problem in mathematics. It was put forward by [Bernhard Riemann](https://en.wikipedia.org/wiki/Bernhard_Riemann) in 1859, and it says, in effect, that the count of prime numbers stays as close as it possibly can to the average pattern the primes follow. He says the same method also proves a wider version, the [Generalized Riemann Hypothesis](https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis).

He did not post a paper. He posted the proof as code written in [Lean](https://lean-lang.org/), a programming language for mathematics in which a computer checks every step. It is very long: one public copy counts more than 17 million lines ([a mirror of the code on GitHub](https://github.com/Tomodovodoo/Riemann)). In the note he says he steered the work towards the right setting, that Claude then "far outpaced" him, and that he does not yet understand parts of the argument himself.

## What has been checked so far

<!-- UPDATE when the comparator run is reported. -->
A computer check can only show that the code proves what the code says. So two questions matter. The first is whether the proof runs without gaps, and here [Andrew Sutherland](https://math.mit.edu/~drew/), a mathematician at MIT, compiled the code himself and found that Lean's checker accepted it, using only the standard starting assumptions every Lean proof is allowed ([Scientific American](https://www.scientificamerican.com/article/the-ai-riemann-hypothesis-proof-is-almost-certainly-true-independent-mathematicians-attest/)). The second is whether the statement at the end of those 17 million lines really is the Riemann Hypothesis, and not something easier that looks like it. [Kevin Buzzard](https://profiles.imperial.ac.uk/k.buzzard), a mathematician at Imperial College London, said on the day that this check had not yet been run ([Scientific American](https://www.scientificamerican.com/article/the-ai-riemann-hypothesis-proof-is-almost-certainly-true-independent-mathematicians-attest/)).

## It is not the first

This year has brought several results in mathematics made mainly by AI, from more than one company.

On May 20th, 2026, [OpenAI](https://openai.com/) said one of its models had disproved a conjecture [Paul Erdős](https://en.wikipedia.org/wiki/Paul_Erd%C5%91s) made in 1946 about [how many pairs of points can be exactly one unit apart](https://en.wikipedia.org/wiki/Unit_distance_graph) ([OpenAI's announcement](https://openai.com/index/model-disproves-discrete-geometry-conjecture/)). The same day, nine mathematicians, among them Timothy Gowers and Daniel Litt, posted a short write-up of the counterexample that people had checked ([their write-up](https://arxiv.org/abs/2605.20695)).

In August 2026, Alpöge and Ralph Furman posted a paper showing that more than two thirds of the zeros that the Riemann Hypothesis is about lie where it says they should, up from a previous record of five twelfths. The paper says Claude found the proof and the two authors checked it, and its main results are also written in Lean ([their paper](https://arxiv.org/abs/2608.13637)). A mathematician outside Anthropic, Youness Lamzouri, has since reached the same result by a different route ([his paper](https://arxiv.org/abs/2609.02882)).

On September 8th, 2026, OpenAI said that about 10,000 copies of an unreleased model, working together for about 88 hours, had settled one form of the [Navier–Stokes problem](https://www.claymath.org/millennium/navier-stokes-equation/), another of the seven [Millennium Prize Problems](https://www.claymath.org/millennium-problems/) ([OpenAI's announcement](https://openai.com/index/navier-stokes-solution/)). It showed that a moving fluid can break down in a finite time in the version of the problem where an outside force is applied. No outside mathematician has yet confirmed it. Researchers at King's College London have argued that OpenAI's Lean version does not fully match its written proof, while saying they have not shown the proof wrong ([King's College London](https://www.kcl.ac.uk/news/openais-navier-stokes-proof-called-into-question)).

## What it changes here

The singularity test does not move. It measures four things: how fast AI's ability to do long tasks is growing, whether forecasts of AI still work, how much of the work of improving AI is done by AI, and how fast the world economy grows. A proof in mathematics is none of those.

There is a real argument that results like these should count for more. The idea of a singularity is about machines that outthink us, and the clearest sign of that is a machine finding what the best people could not. But each part of the test was chosen because, used on its own, it can mislead, and so can a single breakthrough. A system that is good at one thing can make a great discovery. Results come in lumps, not as a steady series. Companies choose what to try and announce only what works. And it is hard to separate the people's share from the machine's. Most of all, adding a new scored measure on the day a large result lands, when that result would push the score up, would be changing the rules after seeing the outcome, which is what fixing the test in advance is meant to prevent.

So from now on these results are listed in a table on [the claims page](https://agizeitgeist.com/claims/), and none of them is scored. Each row says what was claimed, who made it, how it can be checked, and how far it has been checked by people outside the company that made it: only the maker's word, partly checked, confirmed, disputed or withdrawn. A result found to be wrong stays in the table with that mark. The first four rows are the four results above. The claims page is where industry leaders' predictions are kept, and some of those predictions are about exactly this, such as [Sam Altman](https://en.wikipedia.org/wiki/Sam_Altman)'s of June 2025 that 2026 would bring "systems that can figure out novel insights". Those predictions are judged at their own dates, under their own rules, and the table gives the evidence a place to sit until then.

## What to watch

<!-- UPDATE when the comparator run is reported. -->
The next step on the Riemann proof is the check that its final statement says what the Riemann Hypothesis says. After that comes the slower work of people understanding it, which Alpöge says he means to do and expects to bring much shorter proofs. The table will change as each of these checks is reported.
