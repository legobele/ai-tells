---
id: adversarial-stylometry
name: Adversarial stylometry loop (generator/discriminator)
class: countermeasure
status: emerging
fidelity: high
prevalence: rare
vector: none
requires: writing-samples, local-model, fine-tuning-access
first-observed: 2026-11-06
last-verified: 2026-11-06
confidence: low
---

# Adversarial stylometry loop

## How it works

Two models with opposed objectives, trained against each other.

**Discriminator `D`** — an authorship model. Input: a text. Training data: positive class = the operator's genuine writing samples; negative class = model-generated text. Output: a scalar "does this look like this specific person," plus ideally an interpretable delta report.

**Generator `G`** — the LLM producing the essay.

**The loop:**
1. `G` produces candidate text given prompt + current critique
2. `D` scores it against the operator's baseline
3. `D` emits a structured critique — not just a number
4. `G` regenerates with the critique in context
5. Repeat until `D`'s score plateaus
6. Collect the (critique, revised) pairs and **fine-tune `G`** on them

Step 6 is what makes it a training loop rather than a filter. Everything before step 6 is rejection sampling.

## Why this is a GAN

The structural identity is exact:

- Two networks, opposed objectives, trained jointly
- `D` learns the boundary between "real" (the person's samples) and "fake" (generated)
- `G` learns to cross that boundary
- In the limit `G`'s output distribution converges toward the real distribution
- Neither is useful alone; the value is entirely in the equilibrium

## Where it is not quite a GAN

Three deltas that change the implementation, and they're the interesting part.

**1. Frozen generator = rejection sampling, not a GAN.**
A vanilla GAN backpropagates `D`'s loss into `G`'s weights. If you're only prompting, there are no gradients — you're running best-of-N against a verifier. That's a well-studied and weaker regime: verifier-guided search. You only get a true adversary at step 6, when you have gradient access.

**2. Text is discrete.**
The original GAN's continuity assumption doesn't hold. Backprop through token sampling needs REINFORCE, Gumbel-softmax, or straight-through estimation — all of which are high-variance. Historically this is why text GANs underperformed, and why RLHF-style policy-gradient methods ate their lunch. Modern equivalent: treat `D` as a reward model and run DPO or PPO against it. **Which is exactly RLHF with a stylometric reward model instead of a preference model.**

**3. Tiny-data discriminator.**
GAN discriminators train on thousands of images. Here you might have twenty writing samples. A full classifier will overfit catastrophically. Realistic options:
- A stylometric **feature model** (sentence-length distribution, type-token ratio, function-word frequency, punctuation profile, lexical band) with a small classifier on top — interpretable, few-shot, doesn't need deep training.
- Or few-shot prompting a larger model to output the delta report, then treating that as `D`.

## The upgrade that makes it better than a GAN

A GAN discriminator returns a scalar. This one can return **"you used a tricolon in ¶3, your mean sentence length is 8% over baseline, and you've used 'leverage,' which appears nowhere in your twenty samples."**

That's not a score, it's a criticism. Which means `D` doubles as the reward signal *and* the revision instruction — so the loop converges far faster than blind adversarial search, because each step is informed rather than random.

**This is the actual architecture:** not GAN, but **a critic-guided self-improvement loop with a stylometric reward model.** The GAN intuition gets you the training structure; the interpretability is what makes it tractable on twenty samples.

## Failure mode: mode collapse into a parody of yourself

The dominant risk, and it's the classic GAN pathology with a nasty twist.

`D` trained on twenty samples learns the *surface statistics of those samples*. `G` learns to reproduce them exactly. Result: text that is stylometrically indistinguishable from the operator's writing — and therefore indistinguishable from their **weakest work**. Same sentence lengths, same vocabulary, same tics, same shallowness, no new content.

You converge on a forgery of your own floor, not your ceiling.

Guard against it:
- Hold out samples. `D` must not score text it trained on.
- Include *good* samples, not just typical ones, or the target is the median.
- Cap the loop. Past the plateau, more iterations degrade content for diminishing stylistic gain.
- Score content separately from style. A perfect style match on an empty essay is a failed generation.

## The surrogate-model problem

`D` is not the real evaluator. The real discriminator is a teacher holding an implicit model built from *different* data — in-class handwriting, spoken answers, quiz responses, semester-long impression — weighted differently and biased toward recency.

So this is not adversarial training against the true target. It's adversarial training against a **surrogate**, hoping the result transfers.

That's a well-known pattern from adversarial ML: when you can't query the target model, train a substitute and hope the perturbation transfers. Sometimes it does. Sometimes the surrogate and the target have learned different features and the attack fails completely.

Practical mitigation: build `D` from the samples closest to what the target actually sees. If teachers mostly know the operator from in-class writing, `D` should train on in-class writing — not on polished take-home work.

## Stack

Locally feasible on what's already installed: Qwen3.5-0.8B for `G`, Unsloth for step 6, llama.cpp or LM Studio for serving. A stylometric feature model for `D` is a few hundred lines of Python and runs on CPU.

Cost is dominated by the loop: 20-50 generations per draft. At 0.8B locally that's cheap; against a hosted frontier model it isn't.

## Notes
**`status: emerging`, `confidence: low`. This entry is architecture, not field observation.** No evidence anyone is running this against school evaluation. Filed because the operator derived it independently and the derivation is structurally sound.

Confidence is low for a *different* reason than originally written. It isn't low because the idea is unexamined — it's low because the idea is well-examined and the field's results are unflattering. See Prior art.

The interesting consequence: this isn't a detection method, it's a **generator-side defense** — it attacks §1.8 (`voice-baseline.md`) by matching the anomaly model rather than evading it. It's the only entry in this directory that addresses the one control classified as durable.

And it doesn't work against `oral-defense.md`, for the same reason nothing does.

## Prior art (checked 2026-11-06)

Not a novel architecture. Four literatures cover it, and one covers the whole thing.

**1. The name already exists.** Brennan, Afroz & Greenstadt, *Adversarial stylometry: circumventing authorship recognition to preserve privacy and anonymity*, ACM TISSEC 15(3), **2012**. Thirteen years before this file. They built authorship models and obfuscators that attack them, and named the field.

**2. The formal task exists, with a better objective function.** PAN author obfuscation, CLEF **2016-2018**. Task definition is this file's goal verbatim: *given a document and a set of documents from the same author, paraphrase the former so the author can't be identified.* Evaluation is three orthogonal axes, and this is the part worth stealing:

| Axis | Question |
|---|---|
| **Safety** | Does forensic analysis still reveal the author? |
| **Soundness** | Is the output still entailed by the original? |
| **Sensibleness** | Is the output inconspicuous? |

Sensibleness is the trap. Obfuscated text is often *unnatural* — and unnatural in 2026 reads as machine-written. The countermeasure reproduces the tell it was built to remove. PAN formalized that failure in 2016.

**3. The GAN structure, in LLMs, with theory.** SPIN — Chen, Deng, Yuan, Ji & Gu, *Self-Play Fine-Tuning*, **ICML 2024**. The model generates from its previous iteration, then learns to distinguish its own outputs from human-annotated data. The paper says the mechanism "resembles the idea of generative adversarial networks" and proves convergence under the same equilibrium condition: generator distribution must match the target at Nash. **This is the exact architecture in this file — with one substitution.** SPIN's positive class is *human data generally*; ours is *this one human's samples*. That substitution is the only novel piece here, and it's a data-selection change, not an architectural one. Related: DNO (Rosset et al. 2024), SPPO (Wu et al., ICLR 2025), Self-Rewarding LMs (Yuan et al. 2024).

**4. The personalization, shipped.** TinyStyler (Horvitz et al., EMNLP 2024 Findings) — **800M params**, conditions a small model on authorship embeddings (STYLE / LUAR) for few-shot style transfer toward a target author, and reports beating GPT-4 on authorship style transfer. MIT licensed, weights on HF. That's `D` and `G` at exactly the size class this file proposed, published, and better than the "prompt a big model" version. Also: StyleRemix (Fisher et al., EMNLP 2024) decomposes author style into named elements and steers with LoRA adapters — that's the critique format, implemented. And Bao & Carpuat, *Keep It Private* (2024), fine-tunes via RL on a reward balancing soundness / sense / privacy across 68k Reddit authors — that is "`D` as reward model, run DPO" already run.

**5. The direct test — and its answer.** Wang et al., *Catch Me If You Can? Not Yet: LLMs Still Struggle to Imitate the Implicit Writing Styles of Everyday Authors* (EMNLP 2025 Findings). 40,000+ generations, 400+ ordinary authors, few-shot, scored with an ensemble of authorship attribution + authorship verification + style matching + AI detection. That is this loop, evaluated at scale, on this population. The title is the result.

**6. The bad news, from a different field.** Caccia et al., *Language GANs Falling Short* (ICLR 2020): MLE beats text GANs across the entire quality-diversity space, and switching from likelihood to adversarial updates causes a measurable entropy collapse. The adversarial step, applied naively to discrete text, degrades the output. Mode collapse isn't the edge case; it's the default.

**7. The one result in this design's favour.** Grover — Zellers et al., NeurIPS 2019: a discriminator that has seen the generator's own outputs reaches **92%** where a generic discriminator reaches **73%**. "The best defense against Grover turns out to be Grover itself." Training `D` on `G`'s failures is measurably the strongest available discriminator. That's the argument for the closed loop over a static style guide.

### What's actually still open

Three things the literature does not cover, in descending value:

1. **The judge is a human with semester context, not a classifier.** Every paper above optimizes against automatic authorship verifiers. The teacher's model is built from in-class handwriting, spoken answers, quiz performance, and recency bias. Nothing in the corpus addresses that — which is exactly the surrogate gap, and it's the whole risk.
2. **Direction.** Almost all of this work moves text *away* from its author, toward generic. This moves *toward* a specific author. Genuinely rarer, but TinyStyler is most of the way there.
3. **The process dimension.** All of it is text-in, text-out. None of it models submission venue.

### Prior-art verdict

Worth building as a personal tool. Not worth believing it's novel against a human who has read a semester of your writing. The mechanism is 2012; the personalization is 2024; the efficacy against this specific adversary is untested by anyone.

## Sources
- Brennan, Afroz & Greenstadt, ACM TISSEC 15(3), 2012 — adversarial stylometry
- PAN/CLEF author obfuscation 2016-2018 — safety / soundness / sensibleness
- Chen et al., ICML 2024 — SPIN (self-play as GAN)
- Horvitz et al., EMNLP 2024 Findings — TinyStyler (800M, authorship embeddings)
- Fisher et al., EMNLP 2024 — StyleRemix (style-element decomposition, LoRA)
- Bao & Carpuat, 2024 — RL fine-tune on soundness/sense/privacy reward
- Wang et al., EMNLP 2025 Findings — "Not Yet" (40k generations, 400+ authors)
- Caccia et al., ICLR 2020 — Language GANs Falling Short
- Zellers et al., NeurIPS 2019 — Grover (92% vs 73%)
- Goodfellow et al. 2014; Papernot et al. 2016 — GANs; substitute models / transferability
