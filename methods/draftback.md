---
id: draftback
name: Draftback
class: process-forensics
status: live
fidelity: medium
prevalence: medium
vector: live
surface: every keystroke in a Google Doc's revision log
requires: google-docs, chrome, edit-rights, teacher-awareness
first-observed: 2022-02
last-verified: 2026-11-06
confidence: high
---

# Draftback

## How it works
Chrome extension by James Somers. Parses the Google Doc's internal revision log (the chunked-snapshot protobuf data the Doc already stores) and replays it as a video, keystroke by keystroke. Also emits typing-speed statistics, session timing, and a heatmap of where edits clustered.

Requires three things simultaneously: the document lives in Google Docs, the viewer uses Chrome, and the viewer has edit rights on the document.

## What it sees
- **Paste events** — a block of text appearing with no keystrokes behind it. Highest-signal output.
- **Session structure** — how many sittings, when, for how long.
- **Typing speed distribution** — flat speed across a long span is transcription, not composition.
- **Order of construction** — strict top-to-bottom with no returns looks like dictation.
- **Total wall clock** vs. plausible writing time.

## Defeated by
- **Typing simulator extensions** (Scrybe, Natural Typist, Human Auto Typer, TypeOS) — replay text with randomized 30-150ms delays and synthetic typos.
- **Actually typing it**, which is also the only method that produces the structural signatures.
- Manual retyping with edits on the way through.

## Fails when
- No Chrome, no Docs, no edit rights.
- Nobody watches the replay. This is the common case — see SKILL.md §2.7.
- The replay is watched but the teacher doesn't know what composition looks like.

## Notes
A 73-point r/Teachers PSA thread exists specifically titled *"Revision History / Draftback is Not a Way to Verify No AI was used"* — the author discovered typing simulators and left the profession over it.

**Critical limitation for the adversary too:** simulators solve the paste flag and nothing else. A simulated doc still shows uniform speed, one continuous session, and in-order construction. A teacher watching with intent can still read "typed straight through once" as transcription.

## Notes (cont.)
**Fidelity caveat, 2026-11:** `scripted-input.md` closes the structural gap that extensions leave open — out-of-order construction, variable pacing, idle gaps, and block deletions are all forgeable via CDP trusted input. Against an adversary who scripts, the structural signature stops being diagnostic and this control degrades toward the paste flag alone.

That entry is `confidence: low` (capability inference, no field reports). But the assumption is worth carrying openly rather than burying: **this control's strength is contingent on the adversary not scripting.** If scripting becomes normal, re-rate to `fidelity: low`.

## Sources
- r/Teachers 1i0g6dq, 1gy2z8m, 1hp8pru
- draftback.com
