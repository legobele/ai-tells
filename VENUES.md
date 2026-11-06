# Venues — where humanizers and de-tell skills actually live

> **INTERNAL. Distribution notes, not doctrine.** This file exists so the operator knows where to publish and where the audience already is. It is not part of the method set, it is not referenced by `§3`, and it should be stripped before the skill is handed to anyone else.

Measured **2026-11-06**. Three axes per venue: **KYC** (what identity it costs you), **availability** (can you actually get in), **traffic** (how many people are actually there).

Traffic is **measured** wherever a public counter exists — GitHub stars, skills.sh installs, HuggingFace downloads, and 30-day Reddit post volume via the Arctic Shift archive API. Where no counter exists (Discord, Telegram, BlackHatWorld, FlowGPT), the row is marked **est.** and the number is an inference from platform structure, not a count. Do not treat estimated rows as data.

---

## The split that matters

Supply and demand are on different platforms, and confusing them wastes time.

| Layer | Where it lives | What you get there |
|---|---|---|
| **Supply** — the skills, prompts, tools, weights | GitHub → skills.sh → HuggingFace | The artifact itself, free, MIT-licensed, cloneable |
| **Demand** — people who just got flagged | Reddit | What is failing *this month*, in real time |
| **Gray market** — paid "guaranteed undetectable" services | Discord, Telegram, commercial SaaS | A subscription, a card charge, and your document in someone else's database |

If you want a working tool, the first row is the only row that matters. The second row is where you learn which detectors are currently firing. The third row is where people who skipped the first two rows go to lose money.

---

## The KYC ladder

Ranked by what each tier permanently costs you. This is the axis people underestimate: it is not "how annoying is signup," it is "what durable identifier now exists in a database next to the request."

| Tier | Cost | Reversible? |
|---|---|---|
| **0 — none** | Nothing. Read, clone, download. | n/a |
| **1 — email** | An address. Free, disposable, unlinked to legal identity. | Yes |
| **2 — email + risk scoring** | An address plus a platform that can demand a phone number *later*, at its discretion, based on VPN use, posting velocity, or a subreddit's rules. | Partly — the trigger is invisible until it fires |
| **3 — phone** | A number tied to a SIM and usually a carrier account. Effectively a legal identity in most jurisdictions. | No |
| **4 — payment instrument** | A card or bank account. Names, billing address, tax residency. | No |

A tier-2 venue is more dangerous than its signup page suggests, because the escalation is retroactive and unexplained. Reddit and Discord are both tier 2 for exactly this reason.

---

## Supply side — measured

These are the venues that actually hold the artifacts, ranked by measured traffic.

| Venue | KYC | Availability | Traffic (measured) | What's actually there |
|---|---|---|---|---|
| **GitHub** | 0 to read · 1 to participate | Open, global, no invite | `blader/humanizer` **65,520★** / 5,180 forks · `op7418/Humanizer-zh` **22,146★** · `AhmadHassan-BTed/Turnitout-Humanizer` **11,785★** · `epoko77-ai/im-not-ai` **6,428★** · four more above 3k★ | Full source, MIT-licensed, cloneable without an account. `blader/humanizer` has Discussions and a wiki enabled — the only real *community* surface in this list. |
| **skills.sh** | 0 | Open, no account | 12.1k skills indexed · `op7418/humanizer-zh` **56,933 installs** · `proseify.xyz/anti-prose-slop` **53,196** · `cursor/plugins/unslop` **32,721** · `petergyang/no-ai-slop` **29,872** · `hardikpandya/stop-slop` **19,096** · `blader/humanizer` **12,073** | The agent-skills directory. Public per-skill install counters — the closest thing this genre has to a leaderboard. |
| **HuggingFace** | 0 to download · 1 to publish | Open, no invite | `jialinyyzz/humanizer` **344,374 downloads** / 2,252 likes · its GGUF **30,986** · five more humanizer GGUFs above 3k · benchmark datasets at 300–760 downloads | Weights, GGUFs, and training corpora. The dataset shelf is where "humanized vs machine" benchmarks get published. |

**Read the three together and a shape appears.** GitHub measures *attention*, skills.sh measures *installation*, HF measures *downloads*. `blader/humanizer` has 65k stars but 12k installs — a 5.4:1 attention-to-adoption ratio, which is what a repo looks like when it is widely read about and less widely used. Its Chinese translation has 22k stars and 57k installs — a 0.4:1 ratio, which is what a repo looks like when it is *actually deployed*. The English-language repo is the famous one. The Chinese-language repo is the used one.

**The biggest sub-genre is not "humanizer."** Counting installs, the anti-slop family outsizes it: `anti-prose-slop` 53k, `unslop` 32k, `no-ai-slop` 30k, `stop-slop` 19k, `anti-slop` 15.6k across five variants. Those are developer-facing — changelogs, docs, marketing copy — and they exist because engineers got tired of reading their own model's output. Same technique, different evaluator. The genre's center of gravity is professional embarrassment, not academic accusation.

---

## Demand side — measured

30-day post counts from Arctic Shift, 2026-11-06. Lifetime figures are exact; the 30-day column is capped at the API's 100-per-request limit, so `100+` means "at least 100."

### The humanizer-specific subs (small, sincere, alive)

| Subreddit | Lifetime | Last 30d | Access | Character |
|---|---|---|---|---|
| `r/BypassAiDetect` | 1,071 posts / 5,308 comments | **95** | public | "Discuss the best ways to get away with the AI detection." The closest thing to a dedicated community. |
| `r/humanizeAIwriting` | 973 / 2,978 | **98** | public | Same population, more tool-recommendation threads. |
| `r/AIDetectionAcademia` | 430 / 3,271 | **78** | public | The academic-specific slice. Higher comment-to-post ratio — people argue here. |

### The Turnitin complaint cluster (the actual volume)

| Subreddit | Lifetime | Last 30d | Access |
|---|---|---|---|
| `r/CheckTurnitin` | 2,301 / 18,741 | **100+** | public |
| `r/CheckMyTurnitin_ai` | 1,078 / 13,390 | **100+** | public |
| `r/TurnitinScan` | 992 / 7,210 | **100+** | public |
| `r/AccusedOfUsingAI` | 493 / 6,887 | **100+** | public |
| `r/TurnitinAIResults` | 323 / 4,868 | **30** | public |
| `r/Turnitin` | 837 / 3,063 | **9** | public |
| `r/PassOrFlagged` | 193 / 873 | **2** | public |
| `r/DidntUseAI` | 27 / 75 | **0** | public |

### The adjacent massive subs (where the audience already is)

| Subreddit | Lifetime posts | Last 30d | Access |
|---|---|---|---|
| `r/ApplyingToCollege` | 977,930 | **100+** | public |
| `r/writing` | 586,023 | **100+** | public |
| `r/ChatGPT` | 550,222 | **100+** | public |
| `r/college` | 537,936 | **100+** | public |
| `r/Teachers` | 473,396 | **100+** | public |
| `r/HomeworkHelp` | 449,632 | **100+** | public |
| `r/6thForm` | 253,327 | **100+** | public |
| `r/IBO` | 230,346 | **100+** | public |
| `r/ArtificialInteligence` | 190,227 | **100+** | public |
| `r/GradSchool` | 177,249 | **100+** | public |
| `r/LocalLLaMA` | 130,286 | **100+** | public |
| `r/artificial` | 125,024 | **100+** | public |
| `r/AskAcademia` | 113,126 | **100+** | public |
| `r/ELATeachers` | 14,710 | **100+** | public |
| `r/antiai` | 72,252 | **100+** | **restricted** — approved submitters only |

**Four readings.**

**1. The dedicated humanizer subs are an order of magnitude smaller than the complaint subs.** ~270 posts a month across all three humanizer subs, against 2,301 lifetime in `r/CheckTurnitin` alone. People do not go looking for a humanizer until after they have been flagged. The market is post-hoc: it is a panic market, not a preparation market.

**2. Four brand-named subs are corpses.** `r/HumanizeAI` has 6 posts. Ever. `r/undetectableai` has 3. `r/AIDetector` has 2. `r/ChatGPTJailbreak` and `r/Professors` have zero posts in 30 days. A subreddit whose name matches a product is usually a squatter's shell, and the one that looks most official is often the least alive. Check lifetime post count before trusting any community recommendation that points at a brand name.

**3. `r/antiai` being `restricted` is the KYC lesson in miniature.** 72k posts of traffic, behind an approved-submitter gate. You can read it, you cannot speak in it, and the gate is invisible until you try. That is tier 2 in practice.

**4. The audience you would actually want to reach is in the mega-subs, not the niche ones.** `r/ApplyingToCollege` has 978k posts and 100+ a month. `r/Teachers` has 473k. Neither is about humanizers; both are full of the people the humanizers are for. Any distribution strategy that only touches the niche subs reaches a rounding error of the available audience.

---

## Gray market — estimated

No public counters here. Marked **est.**; treat the characterizations as structural, the numbers as absent.

| Venue | KYC | Availability | Traffic | Note |
|---|---|---|---|---|
| **Discord** | 1, escalating to **3** | Invite-gated; invites expire; servers die and take their history with them | **est. high** | Where paid "undetectable" services run support and resale. Server owners can demand a verified phone number at any time, retroactively, via verification level. Nothing is indexed; nothing is searchable; nothing survives the server. |
| **Telegram** | **3** — phone number, mandatory | Link-discoverable only; groups get nuked and reappear under new names | **est. high** | The hardest identity cost before payment. One account per number. Bots sell humanizer passes; the bot is the storefront and the operator is unidentifiable. |
| **BlackHatWorld** | 1 to read · **3** to sell | Open to read; marketplace selling requires a paid seller upgrade and review | **est. medium** | Contains AI-tool threads. Its actual value here is the review culture — sellers get vetted, which is also why the good ones cost money. |
| **FlowGPT** | 1–2 (Google or Discord login) | Bot-walled: Cloudflare returns **403** to non-browser clients | **est. medium** | Prompt marketplace; humanizer prompts circulate as shareable cards. Hard to audit programmatically, which is itself the finding. |
| **4chan** | **0** | Fully open, fully ephemeral | **est. high** | Zero identity cost and zero persistence. Threads 404 in days. Useful as a leading indicator of what tool names are circulating; useless as a reference. |
| **Commercial humanizer SaaS** | **4** — account + card | Open, paywalled, subscription-gated | **est. high** (affiliate-driven) | See hazard note below. |

### The commercial-SaaS hazard

Every one of these services works the same way: you paste the document into their box. That means a third party now holds **the text, your account, a timestamp, and a billing identity**, and the entire value proposition is that the document is sensitive. It is the only venue on this list where using it creates the exact artifact — a submission record — that the process-forensics layer looks for. A card charge plus a stored draft is a worse trail than a Google Doc.

This is not a KYC complaint. It is the same argument `methods/process-forensics.md` makes about version history, applied to a vendor you do not control.

---

## Ranked

Composite: identity cost (lower better), availability (higher better), measured traffic (higher better), artifact quality (higher better). Ranked for someone with no identity footprint who wants the actual technique.

| # | Venue | KYC | Why it lands here |
|---|---|---|---|
| **1** | **GitHub** | 0/1 | Zero cost to consume, everything is cloneable, the source is the artifact, and the biggest skill in the genre lives there with Discussions open. Nothing else is close. |
| **2** | **skills.sh** | 0 | Zero KYC, 12.1k indexed skills, public install counters. Not a community — a leaderboard. Use it to find what is actually being installed rather than what is being starred. |
| **3** | **HuggingFace** | 0/1 | Zero cost to download weights and datasets. The only venue on the list where the *training data* is public. |
| **4** | **Reddit** | 1–2 | Enormous measured demand and the only real-time signal on which detectors are firing. Punished for tier-2 escalation and for being a demand venue, not a supply one. |
| **5** | **4chan** | 0 | Zero KYC and real traffic, but ephemeral and unsearchable. Leading indicator only. |
| **6** | **Discord** | 1–3 | Where the paid market actually transacts, but invite-gated, phone-escalatable, and unindexed. No history survives. |
| **7** | **BlackHatWorld** | 1/3 | Readable, but the useful part — vetted sellers — is behind a paid tier. |
| **8** | **FlowGPT** | 1–2 | Real prompt marketplace, hard bot-wall, low auditability. |
| **9** | **Telegram** | 3 | Phone number. Nothing above tier 3 is worth it for a text technique you can get free on GitHub. |
| **10** | **Commercial SaaS** | 4 | Card, subscription, and your document retained. The worst identity-to-value ratio on the list. |

---

## Terminal hazards

Venues where no countermeasure exists, restated here because they keep appearing in forum threads as if they were solvable:

- **Paper, in class.** `methods/paper-in-class.md`. The only failure mode in the taxonomy where preparation is physical.
- **Oral defense.** `methods/oral-defense.md`. One question, no tooling, and the whole supply chain above becomes irrelevant.
- **Submitting to a detector-checking service.** Any site that offers to "scan" your draft is collecting the draft. That is a process-forensics event with a vendor's retention policy attached.

---

## Distribution play

The stack, in the order it matters. Each step is close to useless without the one before it.

**1. GitHub — the only venue that can host the artifact.**
Email-only KYC, no invite, no review, and MIT is the genre norm (`blader/humanizer`, `sepia`, `Humanizer-zh` are all MIT). A skill is a folder of markdown; a repo is the natural container and the only one that survives. Ceiling, measured: **65,520 stars** on `blader/humanizer` in under ten months. It is also the only venue on this list where the thing can be *cloned* rather than copied out of a screenshot.

**2. skills.sh — the install layer.**
It indexes GitHub repos and publishes per-skill install counts. 12.1k skills indexed. This is where "installs" actually happen for agent skills, and it is where the gap between attention and adoption becomes visible: `blader/humanizer` has 65,520 stars but **12,073 installs**, a 5.4:1 ratio. Its Chinese translation has 22,146 stars and **56,933 installs** — 0.4:1. Same technique, 4.7× the deployment. Publish here too, or the repo is a bookmark.

**3. HuggingFace — only if there are weights or datasets.**
Not a skill channel. 344,374 downloads on `jialinyyzz/humanizer` proves the appetite exists, but it is an appetite for a *model*, not for a prompt folder. Skip unless shipping a fine-tune or a corpus.

**4. Reddit — announcement, not hosting.**
The niche subs are smaller than they look: `r/BypassAiDetect` 95 posts/30d, `r/humanizeAIwriting` 98, `r/AIDetectionAcademia` 78. Combined, roughly 270 posts a month, in front of an audience that already knows what a humanizer is. The reach is in the mega-subs — `r/ApplyingToCollege` (977,930 lifetime posts), `r/college` (537,936), `r/Teachers` (473,396) — but those are where self-promotion rules bite and where the audience has not been flagged yet.

Post-flag, people search. Pre-flag, they don't. That is why the complaint subs (`r/CheckTurnitin` 2,301 posts, `r/CheckMyTurnitin_ai` 1,078) outdraw the humanizer subs 4:1 while being about the *problem* rather than the *solution*.

**5. Discord and Telegram — only if monetizing.**
Phone number or invite gate, no index, no history. The paid market transacts there and nowhere else, and the cost is a durable identity plus a platform that can vanish. Not a distribution channel for a free skill; a distribution channel for a product.

### What the numbers say to do

**Lead with the anti-slop framing, not the humanizer framing.** The anti-slop family outsizes the humanizer family on installs: `anti-prose-slop` 53,196 · `cursor/plugins/unslop` 32,721 · `no-ai-slop` 29,872 · `stop-slop` 19,096 · `anti-slop` 15,617. Those are developer-facing. The biggest measured audience in this space is engineers tired of their own model's prose, not students dodging Turnitin — and the technique underneath is identical. A hook aimed at the larger market costs nothing and reaches several times the installs.

**Translate.** `humanizer-zh` at 56,933 installs against the English original's 12,073 is the largest single effect in the dataset — 4.7×, from a translation. Korean (`nomadamas/k-skill/korean-humanizer`, 8,328) and Russian (`ilyautov/humanizer-ru`, 1,235) variants carry real install bases too. Highest-leverage move available, and it requires no new technique.

**Treat the star-to-install ratio as the scoreboard.** 5.4:1 is famous and unused. 0.4:1 is deployed. If the goal is distribution rather than applause, optimize the second number.

**Ignore the brand-name subreddits.** `r/HumanizeAI` has 6 posts. Ever. `r/undetectableai` has 3. `r/AIDetector` has 2. The subs that look like official product homes are squatted shells, and the one that looks most legitimate is usually the least alive.

---

## Re-measuring

Every number above is reproducible. The endpoints, in order of reliability:

```text
Reddit post volume   https://arctic-shift.photon-reddit.com/api/subreddits/search?subreddit=X
                     https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=X&after=<epoch>&limit=100&sort=desc
GitHub repos         https://api.github.com/search/repositories?q=humanize+ai&sort=stars&order=desc
skills.sh installs   https://skills.sh/api/search?q=humanizer
HF downloads         https://huggingface.co/api/models?search=humaniz&sort=downloads&direction=-1
```

What does **not** work, and should not be retried: `www.reddit.com/*.json` and `api.reddit.com` (403), `old.reddit.com` (HTML login wall), `redlib.*` mirrors (429/410), `safereddit.com` and `l.opnxng.com` (Anubis bot-wall), `pullpush.io` (526). The archive API is the only reliable path to Reddit volume right now.

Arctic Shift's `subscribers` field is a launch snapshot and is wrong by orders of magnitude — `r/BypassAiDetect` reports 25 subscribers against 1,071 posts. Use `_meta.num_posts` and 30-day volume. Anyone quoting subscriber counts for these subs is quoting a number that was stale before they read it.
