---
id: number-gravitation
name: Number gravitation (7, 47, 347, 6:47)
class: signature
status: live
fidelity: high
prevalence: high
vector: weak
surface: the distribution of numerals in a text that is performing specificity
requires: counting, or a script
first-observed: 2023-01
last-verified: 2026-11-06
confidence: high
---

# Number gravitation

## How it works
There are **two number peaks**, they point in opposite directions, and they share one mechanism: the model reproduces the salience peak of whatever number-mode the prompt puts it in.

**Peak one — roundness.** When the task is *data generation* (estimates, synthetic datasets, percentages, prices), models cluster on round and even values: 25, 50, 70%, 100, powers of two. Documented, and it survives explicit instructions not to. The model is performing "a realistic number," and the most recognizable realistic number is a round one.

**Peak two — the 47 family.** When the task is *narrative specificity* (an anecdote, a timestamp, a measurement in a story, a detail meant to feel observed), models reach for numbers that read as *specific* rather than round. And the most recognizable specific number is **47** — with 7 as its parent and 347/847/1,470 as its children.

The mechanism for why 7 and not, say, 3:

- Humans already over-pick 7 when asked for a random digit — ~28%, roughly 3× uniform.
- Models amplify that to ~90%. Not a quirk of sampling: it's the model doing "what a random-looking number looks like," which is a cultural fact rather than a distribution, and the cultural fact is 7.
- 47 inherits the pull through three routes at once: it contains 7; `47%` is one of the most frequent numeric strings in web text; and `47` is a single high-probability token in most tokenizers, so it's *cheap*. A number the model can emit in one token and that carries 7's salience is doubly selected.
- `347` and `847` are the "organic measurement" costume: a 47 with a prefix digit attached so it reads as measured rather than chosen. The prefix is drawn from the same small alphabet — 2, 3, 4, 7, 8.
- `6:47` is the same thing at coarser granularity. The hour field draws from the genuinely common clock range; the minute field draws from the 47 prior. Result: `6:47`, `7:47`, `3:47`, `2:47`.

So the observation isn't a coincidence and it isn't a meme. It's the salience-amplification mechanism (`training-data-gravity.md`) with the specificity mode selected.

## What it sees
- **47**, and `47`-derived forms: 47%, 0.47, 4.7, 470, 1,470, 347, 547, 847.
- **7** standalone, and 7-containing specifics: 7 minutes, 17, 27, 70, 700.
- **Minutes ending in 47.** And, secondarily, `:00`, `:15`, `:30` when the whole set of times in a text is suspiciously tidy.
- **2, 3, 4, 8** as leading digits on invented quantities — the same low alphabet the 1–10,000 experiment surfaced (`7,200–7,500` cluster, digits `[7,2,4,8]`).
- **Roundness**, in the other mode: 20%, 75%, "about 3x", "roughly a decade", "dozens", "hundreds".
- **Repetition across a document.** The tell is strongest when 47 appears *twice* in unrelated places. Once is noise; twice is a prior.

The diagnostic isn't any single number. It's the **distribution against what the subject actually is.** A chemistry paper with 47 in it is unremarkable. A first-person anecdote where the drive took 47 minutes, there were 347 people, and it started at 6:47 is a glyph.

## Defeated by
- **Derive numbers from reality.** Measure it, count it, look it up. A number you actually obtained is immune to this entirely, and it also survives `hallucination-audit.md`, which is the higher-fidelity file.
- If a number is genuinely invented for a narrative: **use one that ends in 1, 3, or 9**, and vary the digit count. 313. 68. 9:41. Those sit where the model's prior is thin.
- **Prefer numbers that don't round-trip.** "Forty-one minutes" is better than "about forty minutes" and better than "47 minutes."
- **Cut the number.** Most invented specifics exist to create an impression of observation. Delete them and see if the sentence survives. If it does, the number was the tell.

## Fails when
- Short texts. One number is not a distribution.
- Genres where numbers are the content — lab reports, financial writing, sports. Every value is derived or given, and the tell has nowhere to live.
- The writer has real data, in which case the numbers are simply correct and there's nothing to see.
- The reader doesn't count. Universal. Nobody audits numerals unless they've been burned.

## Notes
`fidelity: high` on the *mechanism*, `vector: weak` in practice, because a teacher has to notice a digit preference and then be confident enough to say it out loud. In an accusation that's a weak card — "you used 47 twice" is not evidence of anything an honor board will accept.

But it's an **excellent fix**, because it's cheap, mechanical, and it removes a signal that costs nothing to remove. Same category as em-dash density: not a conviction, a hygiene item.

Worth naming because it's the tell people find most surprising: it feels random. It is the opposite of random. It's the most probable number in the language wearing a costume that says "I observed this."

`tools/gravity-check.py` histograms numerals and clock times and reports the 47-family share against a rough web-corpus baseline.

## Sources
- Leslie, 2025-10 — 28% human vs ~90% model on 7; salience amplification
- Coronado-Blázquez — digit clustering, temperature-invariant
- Hopkins & Renda, 2023 — systematic "favorite number" bias
- r/ChatGPT 1rz2ooh — 1–10,000 → 7,200–7,500; digit alphabet [7,2,4,8]
- r/ChatGPT 1sld76g — round/even clustering in synthetic data (peak one)
- Operator observation, 2026-11-06 — 7 / 47 / 347 / 847 / 6:47 in creative output
