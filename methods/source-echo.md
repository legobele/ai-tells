---
id: source-echo
name: Source echo (searchable paraphrase)
class: anomaly
status: unverified
fidelity: medium
prevalence: low
vector: weak
surface: whether a distinctive phrase in the text is a near-verbatim trace of one retrievable document
requires: a search engine and thirty seconds
first-observed: 2025-01
last-verified: 2026-11-06
confidence: low
---

# Source echo

## How it works
Models are trained on documents. Ask one to explain a topic and the highest-probability continuation is frequently a close paraphrase of the specific document that dominated that region of the training distribution — a Wikipedia section, an encyclopedia entry, a study abstract, a textbook paragraph.

The paraphrase is faithful enough that a distinctive eight-to-twelve word run from it is still literally searchable. So the instructor takes a suspicious sentence, quotes it, searches, and lands on the source.

> "I can always tell AI wrote something because when I put portions of the text into Google, I find the reference documentation."
> — r/unb, instructor

## What it sees
- A quoted phrase returning an exact match in a reference work that is not cited anywhere in the essay.
- Sentence-level structure that tracks a single named source across a whole paragraph — same order, same examples, same framing.
- The specific flavor of closeness that isn't plagiarism (every word differs) and isn't independent composition (every idea is in the same sequence).
- Citation present but pointing somewhere else, or absent entirely while the prose maps cleanly onto a well-known source.

The signature is **structural fidelity with lexical distance**. Plagiarism detectors see neither, which is why this survives Turnitin's similarity check at 0%.

## Defeated by
- **Read the source and cite it.** The tell only exists because the derivation is unacknowledged. Attribute it and there's nothing left to notice.
- Write from your own understanding rather than letting a model rephrase a page. The moment you're reconstructing the argument rather than reproducing its sequence, the echo breaks.
- The cheap mechanical sanitizer: rewrite the paragraph's *order*, not its words. Reordering ideas destroys the searchable structure; synonym-swapping doesn't, which is why humanizers don't touch this.

## Fails when
- The subject is so well-trodden that any competent prose collides with the same source. Explaining photosynthesis or the causes of WWI will echo something no matter who writes it — the tell is near-useless on canonical topics.
- The matched phrase is generic ("the importance of early intervention"). Searchable ≠ distinctive.
- The source is itself derived from the same model output or from a content farm that copied it. The echo comes back and proves nothing. This is getting more common, not less.
- Nobody searches. Which is nearly everyone.

## Notes
Structurally the inverse of `hallucination-audit.md`: that one catches citations to things that don't exist, this catches prose derived from things that do, without saying so.

Both are *retrieval artifacts* — evidence of what the pipeline touched — rather than statistical estimates of authorship. That class of evidence is categorically stronger than anything a detector produces, because it is falsifiable by anyone with a browser.

`status: unverified` and `confidence: low` deliberately. The mechanism is sound and the report is credible, but I have one instructor's account and no prevalence data, and the false-positive surface (canonical topics, content farms) is large enough that it could easily be an artifact of a specific subject area rather than a general tell. Needs more field reports before it earns `live`.

## Sources
- r/unb 1hwshss
