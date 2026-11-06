---
id: typing-simulator
name: Typing simulators (Scrybe, Natural Typist, Human Auto Typer, TypeOS)
class: countermeasure
status: live
fidelity: medium
prevalence: medium
vector: none
surface: n/a - this is a defeat mechanism, not a detector
requires: chrome, google-docs
first-observed: 2023-12
last-verified: 2026-11-06
confidence: medium
---

# Typing simulators

## How it works
Chrome extensions that take pasted text and enter it into a Google Doc character by character with randomized inter-keystroke delay (commonly 30-150ms), occasional synthetic typos followed by backspace corrections, and configurable WPM.

Net effect: the Doc's revision log records thousands of discrete keystroke events instead of one paste event. `draftback.md` and `brisk-inspect-writing.md` see a typing session.

Representative products: **Scrybe**, **Natural Typist** (naturaltypist.com), **Human Auto Typer** (Undetectable.ai, ~$5/mo), **TypeOS**. Scrybe's store copy claims *"tested with 15+ history checkers and 100% passed as human typing"* — unverified vendor claim.

## What it defeats
Exactly one control: the paste flag. That's it.

## What it does not defeat
This list is the reason the file is filed as `countermeasure` with `vector: none` rather than as a real tool:

- **Voice baseline** (`voice-baseline.md`) — the text is still not yours in register or vocabulary band.
- **Oral defense** (`oral-defense.md`) — you still can't explain it.
- **Vocabulary interrogation** (`vocab-interrogation.md`) — you still can't define the words.
- **Hallucination audit** (`hallucination-audit.md`) — fake sources are still fake.
- **Paper-in-class** (`paper-in-class.md`) — doesn't apply at all.

## Fails when
**Structural signatures survive faster than keystroke signatures.** A simulated doc still shows:

- Uniform speed across the entire document — real writing has variable pace, bursts, and stalls.
- One continuous session — real writing happens across days.
- Strict in-order construction — real writing drafts out of order and returns.
- No long idle gaps — real writing has staring-at-the-wall time.
- No deletion of substantial blocks — real writing deletes whole paragraphs.

A teacher who watches a replay with intent can still read "typed straight through, once, in one sitting" as transcription rather than composition. The simulator solves the paste flag and nothing else.

## Notes
Filed here because it's the most-shopped-for thing in the category and the most oversold. Its existence matters less as a tool than as an *arms-race data point*: it's why the r/Teachers PSA thread concluded Draftback can't verify authorship, and why the teacher who wrote that PSA moved to paper.

Note the vendor framing on at least one of these: *"This tool is designed for legitimate use cases."* Appended to a product whose only use case is defeating revision-history verification.

## Sources
- chromewebstore.google.com — Scrybe listing
- naturaltypist.com
- k2radio 2023-12-13 (Human Auto Typer launch)
- r/Teachers 1hp8pru (PSA thread)
