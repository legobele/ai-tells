---
id: hallucination-audit
name: Hallucination audit / citation verification
class: content
status: live
fidelity: very-high
prevalence: high
vector: live
surface: whether the cited sources exist and say what's claimed
requires: instructor willingness to check
first-observed: 2023-01
last-verified: 2026-11-06
confidence: high
---

# Hallucination audit

## How it works
Check whether the sources exist. Check whether the numbers appear anywhere. Check whether the quotation is real.

This is not a probabilistic judgment — it's binary. The source either exists or it doesn't. Which makes it the highest-fidelity check available short of an oral defense, and the one most often named by teachers as their actual method.

> "I can catch a lot of AI through hallucination of evidence/quotations & entire sources."

## What it sees
- Fabricated sources with plausible names, plausible journals, plausible volume/issue numbers.
- Fabricated quotations attributed to real works.
- Real sources with fabricated specifics — right author, wrong claim.
- Numbers with no traceable origin.
- Statistically plausible but fictional studies.

## Defeated by
**Opening every source.** Not skimming — opening. If it's a journal article, find the DOI. If it's a book, find the page. If it's a statistic, find the original publication that produced it.

Cost: the single highest time-to-value ratio in the whole countermeasure stack, because it also makes the essay better.

## Fails when
- The instructor doesn't check. Common on low-stakes work.
- The work has no citations (creative writing, personal essays, narrative) — this control simply doesn't apply, which is exactly the gap the original r/Teachers poster described: *"for assignments that don't require it I'm kind of at a loss."*
- Paywalled sources are cited in a way that discourages verification.

## Notes
Rises to `very-high` fidelity because a fabricated citation has essentially zero false-positive rate. A human writing in good faith cites a source they read; the source therefore exists. A nonexistent source is proof of machine generation or deliberate fraud, and instructors rarely care which.

Also the most *legible* evidence for the instructor — unlike a detector score, "this journal does not exist" is something you can show a parent, an administrator, or an honor board.

Adjacent and underused: `paywalled-source` requirements. Assigning essays that draw on material behind a paywall mechanically defeats models that can't retrieve it. Logged here rather than as a separate method until enough evidence accumulates to warrant its own file.

## Sources
- r/Teachers 1ndpi9u
- r/Teachers 184344i (fabricated-quote variant)
