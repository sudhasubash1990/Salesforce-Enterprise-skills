---
title: Demo Script — 60–90 Second SEACF Walkthrough
module: Salesforce Enterprise Skills
category: Governance
document_type: Guide
version: 1.0.0
review_status: Draft
owner: SEACF Practice Lead
created_date: 2026-08-10
last_updated: 2026-08-10
review_cycle: quarterly
related_documents:
  - GETTING_STARTED.md
  - README.md
  - prompts/salesforce-ba-prompts.md
  - docs/workspace-integration.md
keywords: [demo, video, gif, onboarding, seacf]
tags: [demo-script, SEACF]
---

# Demo Script — Why Clone Salesforce Enterprise Skills

**Runtime target:** 75 seconds (range 60–90).  
**Purpose:** Show a first-time viewer the path from GitHub → Cursor → BA BRD → QE test strategy.  
**Honesty rules:** No fake screenshots. No claims of auto-UI overlays that Cursor does not provide. Show real repo pages, real terminal/retriever output, and real agent chat citing loaded files.

**Verified routing (do not improvise different paths on camera):**

| User ask | Retriever behaviour |
|----------|---------------------|
| BRD + Service Cloud complaint | Matches **brd** + Service Cloud → BA skill, `brd-template.md`, `service-cloud-patterns.md`, brain modules, Tier-0 |
| End-to-end Salesforce test strategy | **qe-redirect** → `salesforce-quality-engineering/skill.md` + Enterprise Orchestrator |

Optional pre-roll (not counted in 75s): open a terminal in the repo and keep this ready to paste if the agent’s file citations are too subtle on camera:

```powershell
python scripts/retrieve_context.py --query "Create a BRD for a Salesforce Service Cloud complaint management process."
```

---

## Shot list (10 scenes)

| # | Scene | Duration | Cumulative |
|---|-------|----------|------------|
| 1 | Repository | 6s | 0:06 |
| 2 | Clone | 6s | 0:12 |
| 3 | Cursor | 7s | 0:19 |
| 4 | Request (BA) | 8s | 0:27 |
| 5 | Routing | 8s | 0:35 |
| 6 | Knowledge | 8s | 0:43 |
| 7 | BRD output | 12s | 0:55 |
| 8 | QE request | 7s | 1:02 |
| 9 | Test strategy output | 10s | 1:12 |
| 10 | CTA | 3s | **1:15** |

Buffer: ±10s for voice pace. Cut Scene 6 narration short if over 85s.

---

### SCENE 1 — Repository

| Field | Content |
|-------|---------|
| **Screen** | Browser on the GitHub repo home: `https://github.com/sudhasubash1990/Salesforce-Enterprise-skills` |
| **Exact action** | Scroll once to show the README architecture diagram / repository structure table (BA + QE modules). |
| **Exact text (on screen)** | Repo title **Salesforce-Enterprise-skills**; README heading **Salesforce Enterprise Skills**. |
| **Duration** | 6 seconds |
| **Narration** | “Salesforce Enterprise Skills — a governed BA and Quality Engineering pack for Cursor.” |
| **Expected visual** | Real GitHub page: green **Code** button, README with SEACF architecture (framework-core → BA / QE). Do not overlay fake badges. |

---

### SCENE 2 — Clone

| Field | Content |
|-------|---------|
| **Screen** | Terminal (PowerShell or bash) *or* GitHub **Code** dropdown showing HTTPS URL, then cut to terminal. |
| **Exact action** | Paste and run the clone (or show the command already typed, then Enter). |
| **Exact text** | `git clone https://github.com/sudhasubash1990/Salesforce-Enterprise-skills.git` |
| **Duration** | 6 seconds |
| **Narration** | “Clone it locally — one command.” |
| **Expected visual** | Real `git clone` progress or a completed clone listing `README.md`, `.cursor/`, `salesforce-business-analyst/`, `salesforce-quality-engineering/`. |

---

### SCENE 3 — Cursor

| Field | Content |
|-------|---------|
| **Screen** | Cursor IDE |
| **Exact action** | **File → Open Folder** → select `Salesforce-Enterprise-skills` (repo root). Expand explorer to show `.cursor/`, `framework-core/`, `salesforce-business-analyst/`, `salesforce-quality-engineering/`. |
| **Exact text** | Folder name visible as workspace root; explorer roots as above. |
| **Duration** | 7 seconds |
| **Narration** | “Open the folder as the Cursor workspace root so routing rules load.” |
| **Expected visual** | Explorer with repo root — not a nested subfolder inside another project. (Nested setups need [workspace-integration.md](workspace-integration.md); do not demo that here.) |

---

### SCENE 4 — Request

| Field | Content |
|-------|---------|
| **Screen** | Cursor **Agent** chat (or Chat with Agent mode) |
| **Exact action** | Paste the prompt and send. |
| **Exact text** | `Create a BRD for a Salesforce Service Cloud complaint management process.` |
| **Duration** | 8 seconds |
| **Narration** | “Ask in plain English — Service Cloud complaint BRD.” |
| **Expected visual** | User message bubble with the exact sentence above. No staged “skill picker” UI unless your Cursor build truly shows skill stubs. |

---

### SCENE 5 — Routing

| Field | Content |
|-------|---------|
| **Screen** | Same Agent thread *or* split: terminal retriever output + Agent citing files |
| **Exact action** | Either (A) show agent text that references `salesforce-business-analyst/skill.md` / BRD route, or (B) cut to pre-run `retrieve_context.py` output highlighting `Matched tasks: brd` and `Matched clouds: Service Cloud`. |
| **Exact text (retriever highlight)** | `Matched tasks: brd` · `Matched clouds: Service Cloud` · `salesforce-business-analyst/skill.md` |
| **Duration** | 8 seconds |
| **Narration** | “Routing selects the Business Analyst skill — not a generic chat answer.” |
| **Expected visual** | Real retriever lines or agent citations. Do **not** fabricate a custom “Skill: BA” toast if Cursor does not show one. |

---

### SCENE 6 — Knowledge

| Field | Content |
|-------|---------|
| **Screen** | Retriever bundle list **or** Agent “reading” / citing files; optional quick peek in editor |
| **Exact action** | Scroll the context bundle (or agent file list) to highlight templates + Service Cloud knowledge. Optionally open `salesforce-business-analyst/templates/brd-template.md` in a tab for 2s. |
| **Exact text (call out)** | `salesforce-business-analyst/templates/brd-template.md` · `knowledge/service-cloud-patterns.md` · `knowledge/salesforce-clouds-overview.md` · Tier-0 `framework-core/` |
| **Duration** | 8 seconds |
| **Narration** | “It loads the BRD template and Service Cloud knowledge before writing.” |
| **Expected visual** | Real paths from the BA bundle (also typically includes brain modules, `checklists.md`, sample complaint story). No fake “100% context loaded” meter. |

---

### SCENE 7 — Output

| Field | Content |
|-------|---------|
| **Screen** | Generated Markdown in editor or chat — preferably saved under `outputs/` if the agent writes a file |
| **Exact action** | Scroll the outline: Executive Summary → Scope → AS-IS / TO-BE → Business Requirements `BR-001`… |
| **Exact text (structure to show)** | Headings aligned to [`brd-template.md`](../salesforce-business-analyst/templates/brd-template.md), e.g. **1. Executive Summary**, **3. Scope**, **7. AS-IS Summary**, **8. TO-BE Summary**, **9. Business Requirements** with `BR-00x`, plus **Assumptions** / **Open Questions**. |
| **Duration** | 12 seconds |
| **Narration** | “You get a structured BRD — IDs, scope, AS-IS and TO-BE — ready to review.” |
| **Expected visual** | Real generated draft. Prefer Case / complaint language. Do not claim “approved by client” or invent regulatory citations. If generation is slow, jump-cut to a **previously generated** local draft from a rehearsal (still real Markdown from this repo’s workflow — label on-screen “Rehearsal output” if not live). |

---

### SCENE 8 — QE

| Field | Content |
|-------|---------|
| **Screen** | Same Agent chat, new message |
| **Exact action** | Paste and send the QE ask (same thread so “this solution” has BRD context). |
| **Exact text** | `Create an end-to-end Salesforce test strategy for this solution.` |
| **Duration** | 7 seconds |
| **Narration** | “Same workspace — now ask Quality Engineering.” |
| **Expected visual** | Second user message with the exact sentence. |

---

### SCENE 9 — Output

| Field | Content |
|-------|---------|
| **Screen** | Agent response and/or `retrieve_context.py` showing **qe-redirect** |
| **Exact action** | Flash retriever: `REDIRECT -> salesforce-quality-engineering` and `enterprise-orchestrator/`. Then scroll the test strategy outline. |
| **Exact text (routing)** | `REDIRECT -> salesforce-quality-engineering` · `enterprise-orchestrator/enterprise-orchestrator.md` |
| **Exact text (strategy outline to show)** | Sections such as scope / out of scope, test levels, environments, entry/exit criteria, risks, traceability to requirements — consistent with QE skill guidance. |
| **Duration** | 10 seconds |
| **Narration** | “QE routing kicks in — test strategy with entry criteria and risks, not invented coverage numbers.” |
| **Expected visual** | Real QE-oriented draft. Do **not** show fabricated “Coverage 92%” or fake maturity scores (forbidden by QE prompts). |

---

### SCENE 10 — CTA

| Field | Content |
|-------|---------|
| **Screen** | End card: solid brand-safe background + repo URL (text only) or return to GitHub **Code** button |
| **Exact action** | Hold end card; no new UI demos. |
| **Exact text** | `Clone Salesforce Enterprise Skills and start building.` |
| **Duration** | 3 seconds |
| **Narration** | “Clone Salesforce Enterprise Skills and start building.” |
| **Expected visual** | Text + URL `https://github.com/sudhasubash1990/Salesforce-Enterprise-skills` (and optional pointer to [GETTING_STARTED.md](../GETTING_STARTED.md)). No stock footage of applause. |

---

## Full narration (single take)

> Salesforce Enterprise Skills — a governed BA and Quality Engineering pack for Cursor.  
> Clone it locally — one command.  
> Open the folder as the Cursor workspace root so routing rules load.  
> Ask in plain English — Service Cloud complaint BRD.  
> Routing selects the Business Analyst skill — not a generic chat answer.  
> It loads the BRD template and Service Cloud knowledge before writing.  
> You get a structured BRD — IDs, scope, AS-IS and TO-BE — ready to review.  
> Same workspace — now ask Quality Engineering.  
> QE routing kicks in — test strategy with entry criteria and risks, not invented coverage numbers.  
> Clone Salesforce Enterprise Skills and start building.

**Word count:** ~95 words → ~70–80s at a clear demo pace.

---

## 1. GIF version (loop-friendly)

**Target length:** 12–15 seconds, silent, looping.  
**Goal:** LinkedIn/docs embed teaser — not the full story.

| Beat | Time | Visual | On-screen caption (burned in) |
|------|------|--------|-------------------------------|
| A | 0–3s | GitHub README architecture | `Salesforce Enterprise Skills` |
| B | 3–6s | Cursor Agent: BA prompt (Scene 4 text) | `BA → BRD` |
| C | 6–9s | Scroll BRD headings + `BR-001` | `Structured BRD` |
| D | 9–12s | Agent QE prompt + `qe-redirect` / strategy H2s | `QE → Test strategy` |
| E | 12–15s | CTA card | `Clone & start building` |

**Production notes**

- Export 1080×1080 or 1200×628; 8–12 fps is enough for UI.
- No voiceover; captions only.
- Loop by ending on the CTA matching Scene 1 energy (repo → CTA).
- Prefer screen recording + captions; **do not** use AI-generated fake IDE frames.
- Host exported GIF/video outside this repository (release asset or CDN) — do not commit binaries here.

---

## 2. YouTube / LinkedIn video version

**Target length:** 75–90 seconds.  
**Aspect:** 16:9 YouTube; crop/safe 1:1 or 4:5 for LinkedIn native.

### Title / description (copy)

**Title:** Clone Salesforce Enterprise Skills — BA BRD to QE Test Strategy in Under 90 Seconds  

**Description:**

```text
See how Salesforce Enterprise Skills routes a Service Cloud complaint BRD
through the Business Analyst skill, then hands a test-strategy ask to
Quality Engineering — in the same Cursor workspace.

Repo: https://github.com/sudhasubash1990/Salesforce-Enterprise-skills
Quick start: GETTING_STARTED.md

Chapters:
0:00 Repo
0:06 Clone
0:12 Open in Cursor
0:19 BA request
0:27 Routing + knowledge
0:43 BRD output
0:55 QE request
1:02 Test strategy
1:12 CTA
```

**LinkedIn post body (optional):**

```text
Most AI demos invent a BRD.
This one loads a real Salesforce BA skill pack, Service Cloud knowledge,
and a BRD template — then routes the next ask to Quality Engineering.

Clone: https://github.com/sudhasubash1990/Salesforce-Enterprise-skills
Start: GETTING_STARTED.md
```

### Recording checklist

1. Workspace root = repo root (rules load).
2. Rehearse once so BRD + strategy exist; use live generation if machines are fast, else labeled rehearsal files under `outputs/`.
3. Font zoom 110–125% in Cursor for readability.
4. Hide MCP secrets / `.cursor/mcp.json` / PAT fields.
5. Captions: burn-in or YouTube auto-captions reviewed against the narration script above.

---

## 3. README embed recommendation

Add a short **Demo** block near the top of [README.md](../README.md) (after Purpose or Installation). Prefer a text link to this script; if you host a GIF/video, keep binaries **out of git** (GitHub release asset or external URL).

**Recommended Markdown (text-only):**

```markdown
## Demo (90 seconds)

Walkthrough script: [docs/demo-script.md](docs/demo-script.md) — GitHub → clone → Cursor → Service Cloud BRD → QE test strategy.

Quick start: [GETTING_STARTED.md](GETTING_STARTED.md)
```

**Embed rules**

| Do | Don’t |
|----|--------|
| Link the script and GETTING_STARTED | Claim a YouTube URL that is not published |
| Host GIF/video as a release asset or external URL | Commit large GIF/MP4 binaries into this repository |
| Keep alt text accurate | Fake “Live in Cursor” thumbnails that are not screen recordings |

---

## Pre-demo setup (presenter)

1. Clone fresh or clean `outputs/demo-complaint/` from a prior rehearsal.
2. Confirm: `python scripts/retrieve_context.py --query "Create a BRD for a Salesforce Service Cloud complaint management process."` shows `Matched tasks: brd`.
3. Confirm QE query shows `REDIRECT -> salesforce-quality-engineering`.
4. Cursor: Agent mode; model of your choice — do not claim a specific model is required.
5. Optional: have [prompts/salesforce-ba-prompts.md](../prompts/salesforce-ba-prompts.md) BA-03 open off-camera for a longer live talk-track after the 90s cut.

---

## Related documents

- [GETTING_STARTED.md](../GETTING_STARTED.md)
- [README.md](../README.md)
- [Workspace integration](workspace-integration.md)
- [BA BRD template](../salesforce-business-analyst/templates/brd-template.md)
- [QE skill](../salesforce-quality-engineering/skill.md)
- [BA prompts catalog](../prompts/salesforce-ba-prompts.md)
