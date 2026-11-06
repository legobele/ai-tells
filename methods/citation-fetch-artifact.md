---
id: citation-fetch-artifact
name: Citation fetch artifact ("Just a moment...")
class: content
status: emerging
fidelity: very-high
prevalence: rare
vector: live
surface: browser/bootstrap strings left in a bibliography because a fetch never reached the article
requires: the model used a fetch or search tool, and the target site challenges automated traffic
first-observed: 2026-10
last-verified: 2026-11-06
confidence: medium
---

# Citation fetch artifact

## How it works
A model with a browsing tool tries to verify or read a cited URL. Cloudflare — or any bot-management layer — intercepts and returns a challenge interstitial instead of the article. The interstitial has a `<title>`. The title is *"Just a moment..."*.

If the model extracts the page title to populate a reference field, the bibliography receives the challenge page's title in place of the article's.

> A reference formatted as `Author. Date. **Just a moment...** https://www.realurlthatworks.org`

The URL is real. That's what makes this interesting.

## What it sees
The literal strings the web puts in front of a blocked client:

- `Just a moment...` — Cloudflare managed challenge
- `Attention Required! | Cloudflare` — block page
- `Access denied` / `403 Forbidden`
- `Are you a robot?` / `Enable JavaScript and cookies to continue`
- `Before you continue` — consent interstitials
- `Page not found` on a URL the author insists they read

Any of these sitting where a title belongs is not a stylistic judgment. It's a machine-readable confession that a program tried to fetch a page, got stopped, and reported what it actually saw instead of what it was supposed to see.

## Why it's a different animal from a hallucination
`hallucination-audit.md` catches citations to things that **don't exist**. This catches citations to things that **do exist and were never read**.

Which inverts the usual check. "Does the URL resolve?" — yes, 200, but to a challenge page. "Is the journal real?" — yes. "Is the article title right?" — no, and the wrong answer is a load-balancer's HTML.

So this passes every shallow verification and fails the only one that matters. An instructor who clicks the link gets the article, sees the title doesn't match, and now has a question that has no innocent answer.

## Defeated by
Never let a title field be populated by anything but a title you read with your own eyes.

- Open the source yourself in a real browser. If it challenges you, it challenged the model too, and it can't be cited.
- If the title was machine-extracted, **read it before submitting.** `Just a moment...` survives because nobody reads their own bibliography — which is precisely what a citation exists to prove you did.
- Cite only what you can summarize from memory in a sentence. If you can't, you didn't read it, and no amount of formatting fixes that.

## Fails when
- The model had no fetch tool at all. Pure generation hallucinates a plausible title rather than echoing a challenge page — different tell, `hallucination-audit.md`.
- The topic's sources are open-access and unfettered. Nothing to challenge.
- The instructor doesn't open the bibliography. Common on low-stakes work.

## Notes
Structurally the same failure as citing a 404: the artifact of the retrieval attempt leaks into the artifact of the writing. Any pipeline that copies a field out of a fetched page inherits whatever the page actually was.

Worth generalizing while the instance is fresh: **whenever a tool result is pasted into a document without a human reading it, the tool's failure modes become your document's content.** This is the same class of error as a scraped table carrying a cookie banner into row one.

Status `emerging` — one well-documented field case, mechanism airtight, no prevalence data yet. If it starts appearing in instructor threads generally rather than as an oddity, promote to `live`.

## Sources
- r/Professors 1wxiju3 (2026-10)
