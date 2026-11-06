---
id: training-data-gravity
name: Training-data gravity (salience amplification)
class: signature
status: live
fidelity: high
prevalence: very-high
vector: weak
surface: which register the text is in, and how hard it leans on that register's most recognizable markers
requires: a reader who can name registers
first-observed: 2023-01
last-verified: 2026-11-06
confidence: high
---

# Training-data gravity

This is the parent file. Every other signature tell in `methods/` is a special case of it.

## How it works

The model does not sample the training distribution. It reproduces the distribution's **salience peaks** and then amplifies them.

The evidence is unusually clean because number generation makes it measurable. Asked to pick a number between 0 and 9, humans pick 7 about 28% of the time — a well-documented quirk, roughly three times uniform. Asked the same, language models pick 7 **about 90% of the time** (Leslie, 2025, summarizing Coronado-Blázquez). The model learned the quirk and turned the volume to eleven. Temperature adjustments don't fix it.

The generalization is stated better than I could:

> "Just as humans are not picking a random number, but *performing* 'picking a random number', the LLM is not generating a random number but imitating what humans say one looks like. It's a simulation of a simulation, which drives it towards a single, dominant answer.
>
> LLMs often exaggerate patterns that are common, salient, or meme-like, flattening diversity and negating subtlety. Ask it to write verse in the style of Shakespeare and it will ladle on the 'thous' and 'thees' because those are the salient markers of 'Shakespeare' in the data. **LLMs are drawn to the most salient cultural markers, losing the spread of real human behaviour.**"
> — Ian Leslie, 2025-10

So the tell is not "this text came from the internet." It is **"this text is the most recognizable possible version of whichever register it is in, with every marker turned up."**

## The consequence: there is no single AI tell

There are per-register signature clusters. A banned-phrase list fails because it's an inventory of one register's markers; change the prompt and the markers change.

| Register | Corpus source | Salient markers it amplifies | Where it leaks |
|---|---|---|---|
| **Rationalist / LessWrong** | Overcoming Bias → LessWrong → ACX | "epistemic status", "steelman", "I notice I'm confused", numbered theses, bolded claim sentences, hedged-then-asserted, the "actually, the real question is" pivot | any essay that wants to seem *insightful*. Argument, analysis, opinion. |
| **Tech blog / HN** | engineering blogs, launch posts | "here's the thing", "let me be clear", "the honest version", confident comparatives, the concession-then-pivot | explanatory prose, technical writing |
| **LinkedIn** | career content | "humbled", "grateful", "lessons learned", "agree?", humblebrag-then-lesson structure | short reflections, personal statements |
| **Academic abstract** | papers | nominalization, "This paper argues", "in this context", "significant implications", passive framing | research-flavored essays |
| **Wikipedia** | encyclopedia | neutral summary voice, "notably", "has been described as", "is considered" | any informative paragraph |
| **Forum / Reddit** | comments | lowercase openers, "honestly", "ngl", em-dash asides, the self-interrupt | discussion posts, casual assignments |
| **Workshop fiction** | MFA-adjacent prose | sensory opening, present tense, weather, second person, a small object doing emotional work | any creative piece |
| ****Assistant (RLHF)** | preference data | "It's worth noting", "That said", the balanced close, the offer to continue, "ultimately" | **everything**, as a residual that survives register switches |

That last row is the important one. The assistant register is the *substrate* — it's what the model is actually tuned to be. Prompt it into rationalist voice and the seams still show: the summarizing close, the symmetrical both-sides, the paragraph that resolves.

**Testable claim:** if you cannot name which register you are writing in, you are in the default register, and the default register is the assistant register.

## Why "write like a human" fails

"Human" is not a direction. The model's internal model of human writing is *itself a salience peak* — the most recognizable markers of human writing: contractions, fragments, typos, "honestly", an em-dash aside, a lowercase opener.

So adding those markers is not moving away from a peak. It is **moving from one peak to a more recognizable one.** This is precisely why AI-humanizer output reads as a distinct, worse dialect: you have swapped the assistant peak for a peak that is *deliberately performed*, and deliberate performance of informality is more legible than informality.

The failure mode has a name in the field, and the name is not flattering:

> "a lot of puffy and vague language. Not only did those lines sound like AI, they weakened the writing."
> — r/ELATeachers, on grading it as a writing problem instead of an AI problem

### The field agrees, and it's measured

The largest humanizer skill in existence is `blader/humanizer` — **65,520 stars, 5,180 forks, MIT-licensed**, and its own README says the quiet part outright:

> Humanizer edits for human readers. Getting past AI detectors is not a goal, and detectors still flag most of its output.

Its Chinese translation (`op7418/Humanizer-zh`) is the most-installed variant at **56,933 installs** against the original's 12,073. So the genre's flagship artifact — built by someone with every incentive to claim otherwise — describes itself as a *readability* intervention rather than an evasion one. That is this file's conclusion arriving from the opposite direction: humanizer prose is a salience peak, and swapping peaks does not move you off the map.

What its empirical claim actually measures is worth naming, too. In a blind test, judges preferred its rewrite over the original AI text **16 times out of 16** ([#229](https://github.com/blader/humanizer/issues/229)). That is a *human-preference* result. It establishes that the output reads better. It establishes nothing about whether a detector moves, and the author says as much.

## The correct move: orthogonal, not opposite

Opposite of the model's register is `§8`'s de-tell mode, and under a synthetic baseline it's a liability (`synthetic-baseline.md`). Also it just produces humanizer prose.

The move is **orthogonal** — pick a direction the corpus has low density in. Not "less AI," but "more of something the model has almost none of":

| Axis | Model's gravity | Orthogonal move |
|---|---|---|
| **Specificity** | invented plausible detail, 47-ish | detail only you could have — the number of seats, the actual name, the thing that happened |
| **Position** | balanced, both-sides, ultimately-resolves | take a side the model wouldn't; leave an objection standing |
| **Structure** | intro → three → conclusion, each resolving | end mid-thought; let a section be shorter than its point demands |
| **Length** | the length the prompt implies | much shorter, or longer than the point requires |
| **Emotion** | named ("I was frustrated") | enacted (the sentence gets shorter) |
| **Failure** | nothing in the text fails | include a thing that doesn't work and say so |
| **Conclusion** | verdict | open question you genuinely don't answer |

Every one of those is unfakeable in the direction that matters, because the model cannot supply *your* particulars and RLHF actively suppresses unresolved endings.

## The LessWrong loop, which is funny and also the point

The rationalist register is heavily overrepresented in pretraining relative to its real-world frequency: web-native, long-form, heavily interlinked, unusually high quality-per-token. It is therefore one of the strongest gravity wells for any prompt containing "insight," "argument," or "essay."

Which means the models now write in it well enough that **the forum that invented it has banned the style.**

LessWrong's own policy post prohibits "the stereotypical writing style of an AI assistant" and rejects posts that "will almost certainly fail this criteria (since they will by default be written with the typical LLM 'style')." In the comments, a moderator is confident the style is detectable; another notes that appending "and don't write it in standard LLM style" is not enough.

The register's originators are policing their own dialect because a model learned it harder than they meant it. That is the tower-of-babel loop in one artifact: the corpus teaches the model, the model amplifies the corpus, the corpus disowns the amplification.

Also worth having on record, from the same essay that documents rationalist writing ("Rat Traps", Asterisk): the tell has already decayed into self-parody inside its own community — *"Use it once, it's a technique; twice, a pattern; thrice, a gimmick; and henceforth, a cliche."* The markers listed above are now *also* how a human performs rationalism badly. Which means the LessWrong register is a **low-fidelity** tell on its own and only informative in combination.

## The kill list

Concrete markers, each with the mechanism and the counter. This list is a cache, not doctrine — extend it in the register-specific files.

**Paragraph and sentence architecture**
- **Mic-drop cadence** — every paragraph ends on a punchline. Model: RLHF rewards closure per unit. Counter: in `mic-drop-cadence.md`.
- **Bolded claim sentences** — the "skim me" formatting of blog prose. Counter: bold nothing, or bold once.
- **Fractal resolution** — sentence resolves, paragraph resolves, section resolves, essay resolves. Counter: only the essay resolves.
- **The concession-pivot** — "X is true. But Y." in every section. Counter: once.
- **Numbered thesis** — "Three things follow." Counter: prose, or an actual list of two.

**Lexicon**
- "delve", "tapestry", "testament", "landscape", "realm", "navigate", "underscore", "pivotal", "robust", "leverage", "seamless", "nuanced", "multifaceted" — counter: delete the sentence, it wasn't carrying anything.
- "It's worth noting", "That said", "Ultimately", "In essence", "At its core" — counter: the sentence works without the frame.
- "not X, but Y" — the single most overused construction in the rationalist gravity well. Counter: allow it once. Then assert Y.
- "here's the thing", "let me be clear", "the real question is" — counter: say the thing.

**Numbers and time**
- 7, 47, 347, 847, 6:47. Two peaks, one mechanism. See `number-gravitation.md`.
- Round numbers where specificity is being performed: 20%, 75%, 3x, "a decade".
- "dozens", "hundreds", "scores" — abstraction dressed as magnitude.

**Punctuation**
- Em-dash density. Counter: ≤1 per 200 words. **And note the inversion:** students are now *avoiding* em-dashes and colons because they've been told these are tells (`synthetic-baseline.md`). A text with zero em-dashes and conspicuous semicolon avoidance is running a detector-awareness signature. Neither direction is safe; the safe thing is a plausible personal rate, held steady.
- Tricolon addiction. Counter: one per 500 words, and lopsided.
- The em-dash reveal — "and that's — well, that's the problem."

**Register hygiene**
- Any sentence that could be a pull-quote. There should be at most one.
- Any paragraph whose last line is a standalone declarative. Should be <20% of paragraphs.
- Any claim that no one could disagree with. See `reviewer-stance.md`.

## What this changes about everything else

`§8`'s de-tell mode was a list of things to add — variance, fragments, register breaks. That was written against a signature detector and it is the wrong instrument against a salience model. The model already knows all of those tricks; they're in the humanizer corpus and they've been averaged.

What the model *cannot* do is be in a register it has little of, at a length it doesn't default to, taking a position its preference tuning punishes, about particulars it has never seen.

That is the whole play. Everything else is punctuation.

## Sources
- Leslie, "Why Are LLMs Fixated On the Number 7?", 2025-10 — 28% human vs ~90% model, salience amplification, Shakespeare/thou
- Coronado-Blázquez, "LLMs and the number 7" — digit clustering, temperature-invariant
- Hopkins & Renda, 2023 — "favorite number" bias in LLM integer generation
- r/ChatGPT 1rz2ooh — 7,200–7,500 cluster when asked for 1–10,000; digit alphabet [7,2,4,8]
- LessWrong, "Policy for LLM Writing on LessWrong" — bans "the stereotypical writing style of an AI assistant"
- "Rat Traps", Asterisk #08, 2024-11 — rationalist register, marker decay ("technique → pattern → gimmick → cliche")
- r/ELATeachers 1rmeg3y — "puffy and vague language" as the field term
- r/ChatGPT 1sld76g — round/even clustering in *data generation* (opposite peak; see `number-gravitation.md`)
