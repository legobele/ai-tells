---
id: scripted-input
name: Browser-automation input (Playwright / CDP)
class: countermeasure
status: emerging
fidelity: high
prevalence: rare
vector: none
surface: n/a - defeat mechanism
requires: a browser the target editor runs in
first-observed: 2026-11
last-verified: 2026-11-06
confidence: low
---

# Browser-automation input (Playwright / CDP)

## How it works
Playwright (or any CDP client) drives a real Chromium instance and dispatches `Input.dispatchKeyEvent` at the protocol layer. The browser generates genuine DOM key events with `isTrusted: true` — indistinguishable from a physical keyboard at the application level, because they *are* browser-generated events rather than synthetic `dispatchEvent` calls.

The application cannot tell. It is not being asked to.

## What it defeats
Everything an extension-based `typing-simulator.md` defeats, **plus the structural signatures** that file explicitly cannot fake:

| Signature | Extension simulators | Scripted input |
|---|---|---|
| Paste flag | defeated | defeated |
| Uniform typing speed | still visible | **defeated** — vary WPM per paragraph |
| One continuous session | still visible | **defeated** — schedule across real days |
| In-order construction | still visible | **defeated** — type ¶3, ¶4, ¶2, ¶1 |
| No idle gaps | still visible | **defeated** — sleep |
| No block deletions | still visible | **defeated** — delete and retype |

This is the important consequence: **`draftback.md` and `version-history.md` lose their primary discriminating signal against an adversary willing to script.** The control doesn't break; the signal stops being diagnostic.

## What it still does not defeat
Unchanged from `typing-simulator.md`:

- `voice-baseline.md` — the text is still not yours.
- `oral-defense.md` — you still can't explain it.
- `vocab-interrogation.md` — you still can't define the words.
- `hallucination-audit.md` — fake sources are still fake.
- `paper-in-class.md` — no browser involved.

## Why this is still a weak position
Three reasons, in order of strength.

**1. Cost inversion.** To defeat the structural signature you must script out-of-order construction, multi-day scheduling, variable pacing, and idle gaps. At that point you have spent more effort than writing the essay. Same conclusion reached independently in 2023 by a student on r/utdallas: *"it would most likely be harder than actually writing the paper."* This is a normal security outcome — defense in depth makes an attack uneconomical, not impossible. Irrational attacks are a legitimate defense.

**2. Interval statistics.** Human inter-keystroke intervals are **log-normal and heavy-tailed** — long hesitation spikes, bursts of fluency, autocorrelation between adjacent keys. Sampling a uniform distribution between 30-150ms produces a *smoother, thinner-tailed* distribution than any real typist. Any statistical analysis of the revision log can separate them once someone thinks to run it. This is the next honeypot→fingerprint cycle waiting to happen: see `trojan-horse.md` for the reference specimen.

**3. It leaves artifacts outside the document.** `navigator.webdriver`, CDP-detection timing probes, an unusual binary on a school-managed device, browser-extension or MDM inventory, network egress. None of this matters against an LMS that isn't checking — which is most of them — but it's a much larger forensic surface than typing into a text box.

## Fails when
- The submission venue isn't browser-based (printed, paper, verbal, locked-down lab image).
- The device is managed and monitored.
- Anyone correlates document history against network or endpoint telemetry.
- Nobody looks at all — in which case nothing was needed in the first place (§0).

## Notes
**Status is `emerging` and confidence is `low` on purpose: this entry is capability inference, not field observation.** No r/Teachers or r/Professors report of students using Playwright against a school LMS was found. The mechanism is verified — CDP trusted input is well-documented and Playwright ships it — but the *usage* is extrapolated.

Filed anyway because the capability changes the risk model for two existing entries, and the skill's rule is that `draftback.md` and `version-history.md` should carry a pointer rather than an unstated assumption. See the cross-references in both files.

Also worth logging honestly: **most LMSes don't block automation because they aren't attempting to.** Canvas, Blackboard, Schoology, Brightspace, and Moodle do not run bot detection on submission forms. That's not a vulnerability to be found — it's an absence of the threat model entirely.

**Language-class note:** §9 amplification still holds. A scripted submission in a Spanish class produces text whose vocabulary band and diacritics are still measurable against a semester of spoken output, and the oral component is native to the curriculum. The script defeats the transcript, not the conversation.

## Sources
- Playwright / Chrome DevTools Protocol documentation (trusted input semantics)
- r/utdallas 13bb0wr (cost-inversion argument, 2023)
- No field reports located. Confidence reflects that.
