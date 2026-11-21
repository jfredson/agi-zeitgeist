# Proposed amendment A37: results made mainly by AI are listed beside the claims, not scored

**Status: approved by John on 2026-11-20 ("Approve as written") and entered in `docs/amendments.md` as A37 the same day. This file keeps the source notes for the first rows. Before approval it read: a proposal, written 2026-11-20 by the agent, at John's request of the same day. Nothing
here is entered. No table, page, validator check or news post changes until John rules. If he
says yes, the section below headed "A37" is copied into `docs/amendments.md` as it stands, under
a dated heading that records his words.**

How it came up. On 2026-11-20 Levent Alpöge, a mathematician who works at Anthropic, said he had
proved the Riemann Hypothesis working with Claude, and released the proof as code a computer can
check ([his note](https://alpo.ge/remark.pdf)). John asked whether the AGI Zeitgeist should cover
it. It moves none of the four parts of the singularity test, and the news-post rule (a post
explains a change to the record) left it nowhere to go. Of three options put to him (this table;
a note on one claim only; loosening the news-post rule), John chose this one, the agent's
recommendation.

John also asked, the same day, whether there is an argument for counting breakthroughs in the
sciences as progress towards AGI or superintelligence. The agent's answer, which shapes item 1
below, is in the section "Why shown and not scored".

---

### A37. Results in mathematics and science made mainly by AI are listed beside the claims, not scored

Applies to: a new table, `data/ai_results.csv`; the claims page (`/claims/`), which gains a
section that draws it; `scripts/validate.py`, which gains a check on it. The singularity test,
its frozen values (`docs/singularity-entry-thresholds.json`) and the claims ledger's rules are
untouched.

Was: a result made by an AI system appeared on the site only indirectly. It showed up inside the
note on a claim it bears on (OpenAI's disproof of an Erdős conjecture, in the note on Sam Altman's
prediction that 2026 would bring "systems that can figure out novel insights"), or in a statement
row when someone on the panel mentioned it (Altman, Kokotajlo and Floridi on OpenAI's
Navier–Stokes claim). There was no list of the results themselves, and no place to say whether
each one had been checked.

Now:

1. **The score does not change.** No row in the new table enters a gauge, the progress number or
   the headline. The table is context, on the same footing as the robots table beside part D (A33)
   and the company code figures beside part C.
2. **A table of results.** Each row is one result that its makers say was produced mainly by an
   AI system, on a problem that was named and open before the work began. It holds:
   - the date the result was announced, and where;
   - the problem, with a link, and how long it had stood open, from a source;
   - what was claimed, in one plain sentence, including whether it is the whole problem, a
     version of it, or a better bound on it;
   - who announced it, the AI system and its maker, and the people's part as they describe it;
   - how it can be checked: a proof a computer checks (such as Lean), a paper, code, or data;
   - **the check**, one of: `maker` (only the makers' word so far); `outside_partial` (people
     outside the maker have checked part of it, named in the row); `outside_confirmed` (people
     outside the maker, or a computer check of both the statement and the proof run by someone
     outside the maker, say it holds); `disputed`; `withdrawn`. The date of the check is given
     beside it, with its source.
3. **What is not a row:** benchmark and test scores; competition results on problems whose
   answers were already known; a result announced with nothing a reader can check (no paper,
   proof, code or data). When a figurehead on the ledger's list announces such a thing, it goes to
   the claims ledger under its own rules. Otherwise it is left out.
4. **Rows are kept.** A result found wrong stays in the table, marked `disputed` or `withdrawn`,
   with the date and the source. The check is updated as outside checks come in; each change is
   dated, and the weekly reading looks for them.
5. **All makers alike.** The table starts with every qualifying result the record already knows
   of from 2026, whoever made it. The first rows are, in date order:
   - OpenAI, 2026-05-20: a model disproved the planar unit distance conjecture (Erdős, 1946).
   - Alpöge and Furman, 2026-08: more than two thirds of the zeros of the Riemann zeta function
     are simple and on the critical line, checked in Lean (to be confirmed against the paper,
     including whether it is the result Anthropic described in August, before entry).
   - OpenAI, 2026-09: a claimed solution of a version of the Navier–Stokes problem.
   - Alpöge, Anthropic, 2026-11-20: a claimed proof of the Riemann Hypothesis and the Generalized
     Riemann Hypothesis, released as Lean code.
   Each row's facts are set down from sources opened when it is entered (see the source notes
   below), never from memory.
6. **Claims may point to rows.** A claim in the ledger whose test a result bears on may name the
   row in its note. The claim's verdict is still reached under the ledger's own rules, at its own
   date.

Why shown and not scored. Discovery is close to the heart of what the singularity idea is about:
Good's intelligence explosion and Vinge's event horizon are both about minds that outthink ours,
and the plainest sign of that from outside is a machine finding what the best people could not.
Open problems also carry a measure of difficulty nobody designed for the purpose (how long the
best people tried), which a lab cannot train for in advance. But each part of the test was chosen
because, used alone, it misleads, and a breakthrough used alone misleads too: a narrow system can
make a great discovery (computers helped prove the four-colour theorem in 1976), results come in
lumps rather than a series, makers choose what to try and announce only what works, and the
people's share is hard to separate from the machine's. Most of all, adding a scored measure on
the day a large result lands, when it would push the score up, is changing the rules after seeing
the outcome, which is what the frozen test exists to prevent. So the results are shown, dated and
checked, and the score is left alone.

What it costs: one small table, a section on the claims page, one validator check, and a look for
new rows and changed checks in the weekly reading. Most weeks will add nothing.

Not decided here, and left for John:
- whether the table should also be shown beside part A, which measures capability, as well as on
  the claims page;
- whether results in the natural sciences, which take years to confirm, follow the same rule as
  results in mathematics, which a computer can sometimes check in hours;
- whether a measure built on open problems, weighted by how long each stood open, should one day
  be studied as a candidate replacement for METR's series in part A (the open question A24). That
  would be an amendment of its own, defined in advance and run alongside the old measure before it
  counts, as the successor rule requires.

---

## Source notes for the first rows

Each source below was opened on 2026-11-20 by the agent or by a reading agent it sent, unless
marked. Nothing in a row is entered from memory. The check column is what the row would say if
entered today; it is read again on the day of entry.

**1. The unit distance conjecture (OpenAI, 2026-05-20). Check: `outside_confirmed`.**
- OpenAI, ["An OpenAI model has disproved a central conjecture in discrete geometry"](https://openai.com/index/model-disproves-discrete-geometry-conjecture/),
  dated May 20, 2026: an internal general-purpose reasoning model built point sets in the plane
  with more pairs one unit apart than Erdős's conjecture of 1946 allows. The proof is
  [a PDF on OpenAI's site](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-proof.pdf).
- The outside check: nine mathematicians (Alon, Bloom, Gowers, Litt, Sawin, Shankar, Tsimerman,
  Wang and Wood) posted ["Remarks on the disproof of the unit distance conjecture"](https://arxiv.org/abs/2605.20695)
  on 2026-05-20, a short write-up of the counterexample checked by people. The arXiv page does
  not say where the nine work; Scientific American says Litt is not involved with OpenAI. Before
  entry, confirm that the nine are outside OpenAI, which `outside_confirmed` needs.
- Scientific American, [2026-05-21](https://www.scientificamerican.com/article/ai-just-solved-an-80-year-old-erdos-problem-and-mathematicians-are-amazed):
  the outside experts saw an edited version of the model's reasoning, not its original output.
- Already in the record: the note on Altman's claim `2025-06-10-altman-2026-systems-novel-insights`
  cites the same page, read in Internet Archive copies on 2026-11-09.

**2. Two thirds of the zeta zeros (Alpöge and Furman, 2026-08-13). Check: `maker`, to be read again before entry.**
- [arXiv 2608.13637](https://arxiv.org/abs/2608.13637), version 1 of 2026-08-13, version 2 of
  2026-08-19, by Levent Alpöge and Ralph Furman: at least two thirds of the nontrivial zeros of
  the Riemann zeta function are simple and on the critical line (0.6725 with a known refinement),
  up from the previous record of 5/12. The main theorems are formalised in Lean 4.
- The arXiv comment says the proof was "discovered autonomously by Claude (Anthropic)" and checked
  and communicated by the listed authors.
- No outside check was looked for on 2026-11-20. Before entry, search for one; until one is found
  the check is `maker`, because the Lean work was done by the authors' side.

**3. Navier–Stokes, with an outside force (OpenAI, 2026-09-08). Check: `maker`, with a published objection to the Lean version.**
- OpenAI, ["On the Navier–Stokes Millennium Prize Problem"](https://openai.com/index/navier-stokes-solution/),
  dated September 8, 2026 and updated September 10: a fluid that starts smooth can break down in
  finite time while its energy stays finite, in the version of the problem with an outside force.
  About 10,000 agents ran for about 88 hours; the Lean version took a further 17 hours. OpenAI says
  it will not claim the prize.
- The Clay Mathematics Institute, [11 September 2026](https://www.claymath.org/news/navier-stokes-announcement):
  the problem "has apparently been settled", with its review "deliberately unhurried". It does not
  name OpenAI.
- Bastounis, Circelli and Hansen, [arXiv 2610.08144](https://arxiv.org/abs/2610.08144), and
  [King's College London's release of 2026-10-27](https://www.kcl.ac.uk/news/openais-navier-stokes-proof-called-into-question):
  the Lean version does not fully match the written proof; they have not shown the proof wrong. So
  the row is not `disputed` under item 2 (no one has said the result is false), but the row names
  the objection.
- A credit dispute: Tristan Buckmaster and Levent Alpöge posted related work on the Euler
  equations the night before; OpenAI's page credits them with that result. Worth noting in the row,
  because Alpöge is also the author of row 4.

**4. The Riemann Hypothesis and the Generalized Riemann Hypothesis (Alpöge, 2026-11-20). Check: `outside_partial`.**
- [Alpöge's note](https://alpo.ge/remark.pdf), created 2026-11-20 at 12:52 universal time: "I
  believe I have, working with Claude, discovered a proof of the Riemann Hypothesis", extending to
  the Generalized Riemann Hypothesis; the Lean code is in 14 archive parts on his site.
- Scientific American, [2026-11-20, Howlett](https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/)
  and [2026-11-20, Moskowitz](https://www.scientificamerican.com/article/the-ai-riemann-hypothesis-proof-is-almost-certainly-true-independent-mathematicians-attest/):
  Andrew Sutherland (MIT) compiled the code himself, rechecked by Lean's kernel with only the three
  standard axioms. Kevin Buzzard (Imperial College London): "We still await a successful comparator
  run", the check that the statement written in Lean is the real theorem.
- The mirror [n4rr4k/riemann-hypothesis](https://github.com/n4rr4k/riemann-hypothesis): comparator
  "not yet run" as of 2026-11-20; its README says the main theorem uses the standard library
  Mathlib's own definition of the Riemann Hypothesis, and that its "GRH" covers Dirichlet
  L-functions only. The row must say which generalised version is claimed.
- The mirror [Tomodovodoo/Riemann](https://github.com/Tomodovodoo/Riemann): 17,374,215 lines of Lean.
- Not confirmed and not to be used: Elliot Glazer's reported remark that the statement is GRH (only
  secondary sites quote it; the original post could not be opened), and Wikipedia's sentence that
  the proof "has been Lean-verified", whose sources could not be seen.
- When the comparator run is reported, the row moves to `outside_confirmed` if it passes, with the
  source and date.

## The checks owed before entry, done 2026-11-20 after approval

- **Row 1.** The write-up (https://arxiv.org/html/2605.20695) gives no affiliations, only email
  addresses; the nine are at Princeton, Manchester, Cambridge and the Collège de France, Toronto,
  Academia Sinica and Harvard, from their own or their universities' pages. None says they work for
  OpenAI, and the paper lists only academic and foundation funding. Daniel Litt writes that two
  people at OpenAI asked him to check it. The check stays `outside_confirmed`.
- **Row 2.** Anthropic's own page (https://www.anthropic.com/research/riemann-zeta, dated
  2026-08-10, updated 2026-08-13) announced the result first, so the row's date and announcement
  are Anthropic's. Its statement that two experts, Brian Conrey and Dan Goldston, read the paper is
  Anthropic's word. Youness Lamzouri (Université de Lorraine) reached the same bound by a different
  method (https://arxiv.org/abs/2609.02882, 2026-09-02, revised 2026-09-08) and notes two estimates
  the original neither states nor proves. No outsider re-ran the Lean proof and no journal has
  accepted it. The check is `outside_partial`, dated 2026-09-08.
- **Row 4.** The comparator run had still not been reported at 2026-11-20 20:43 universal time
  (the mirrors https://github.com/n4rr4k/riemann-hypothesis and
  https://github.com/Deicyde/riemann-hypothesis). The check stays `outside_partial`.
