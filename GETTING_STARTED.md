---
title: Getting Started — 5 Minute Quick Start
module: Salesforce Enterprise Skills
category: Root
document_type: Guide
version: 1.0.0
review_status: Draft
owner: SEACF Practice Lead
created_date: 2026-08-10
last_updated: 2026-08-10
review_cycle: quarterly
related_documents:
  - README.md
  - docs/workspace-integration.md
  - framework-core/README.md
  - salesforce-business-analyst/skill.md
  - salesforce-quality-engineering/skill.md
keywords: [getting-started, quick-start, onboarding, cursor, seacf]
tags: [getting-started, SEACF]
---

# Salesforce Enterprise Skills — 5 Minute Quick Start

Use this guide to go from clone → first AI request in about five minutes. For full architecture and release notes, see [README.md](README.md).

## 1. What This Repository Does

**Salesforce Enterprise Skills** is a knowledge pack for Salesforce delivery work. It teaches AI tools (Cursor, Claude) and humans how experienced practitioners:

- Capture requirements (BRD, FRD, user stories)
- Decide Standard vs Config vs custom (fit-gap)
- Design and govern quality (test strategy, defects, automation)
- Support production incidents and go-live readiness

Everything sits under the **Salesforce Enterprise AI Consulting Framework (SEACF)**: shared Tier-0 contracts in [`framework-core/`](framework-core/README.md), then active modules for Business Analyst and Quality Engineering.

You ask in plain English. Routing loads the right skill, knowledge, templates, and playbooks—then you get structured, reviewable deliverables (usually under `outputs/`).

## 2. Who Should Use It

| Persona | Typical use |
|---------|-------------|
| Salesforce Business Analysts | Discovery, BRD/FRD, stories, workshops, RTM, RAID |
| Salesforce QA Engineers | Test strategy, scenario design, defect intelligence, automation review |
| Salesforce Consultants | Repeatable delivery artifacts across clients |
| Salesforce Architects | High-level fit-gap and capability alignment (BA/QE artifacts first) |
| Salesforce delivery teams | Shared language, templates, and quality gates |
| AI practitioners | Prompt patterns and governed agent workflows |
| Cursor users | Auto-loaded rules and skill stubs under [`.cursor/`](.cursor/README.md) |
| Claude users | Same Markdown skill packs—load Tier-0 then the module `skill.md` |

## 3. Clone the Repository

```bash
git clone https://github.com/sudhasubash1990/Salesforce-Enterprise-skills.git
cd Salesforce-Enterprise-skills
```

Or: GitHub **Code → Download ZIP**, then extract the folder.

## 4. Open in Cursor

1. Open Cursor.
2. **File → Open Folder**.
3. Select the `Salesforce-Enterprise-skills` folder (the repo root that contains `README.md` and `.cursor/`).

That folder **must** be a workspace root so [`.cursor/rules/`](.cursor/rules/) and [`.cursor/skills/`](.cursor/skills/salesforce-business-analyst/SKILL.md) auto-load.

If this repo is nested inside another project, do **not** stop here—use the [Workspace Integration Guide](docs/workspace-integration.md) (multi-root workspace or bridge rule).

**Claude / other AI tools:** Open the same folder as the project context. Start from [framework-core/README.md](framework-core/README.md), then [salesforce-business-analyst/skill.md](salesforce-business-analyst/skill.md) or [salesforce-quality-engineering/skill.md](salesforce-quality-engineering/skill.md).

## 5. Understand the Architecture

```
User Request
      │
      ▼
framework-core/                         ← Tier-0 (always load)
      │
      ├─► salesforce-business-analyst/  ← Module 1 (BA)
      └─► salesforce-quality-engineering/ ← Module 2 (QE)
              └─ enterprise-orchestrator/
```

| Folder | What it is |
|--------|------------|
| [`framework-core/`](framework-core/README.md) | Shared SEACF contracts: routing, context loading, governance, evaluation. Load before BA or QE deep work. |
| [`salesforce-business-analyst/`](salesforce-business-analyst/README.md) | BA skill: brain, knowledge, templates, playbooks, scenarios, interview guide. Entry: [`skill.md`](salesforce-business-analyst/skill.md). |
| [`salesforce-quality-engineering/`](salesforce-quality-engineering/README.md) | QE skill + Enterprise Orchestrator and specialized packs. Entry: [`skill.md`](salesforce-quality-engineering/skill.md). |
| [`.cursor/`](.cursor/README.md) | Cursor rules (`instructions`, `routing`, output/user-story rules) and skill discovery stubs. |
| [`examples/`](examples/README.md) | Sample BRD, user story, workshop, and project artifacts to learn the expected shape. |
| [`scripts/`](scripts/README.md) | Utilities—especially [`retrieve_context.py`](scripts/retrieve_context.py) for BA context bundles, plus validators. |
| [`output-engine/`](output-engine/README.md) | Optional Markdown → Word/Excel/PowerPoint/PDF conversion after you write to `outputs/`. |

Supporting folders you will meet next: [`docs/`](docs/README.md) (governance), [`shared/`](shared/README.md) (glossary and standards), `outputs/` (your generated work).

## 6. Your First AI Request

Paste any of these into Cursor Agent (or Claude with this repo in context):

**1 — BRD generation**

```text
Create a BRD for a Service Cloud complaint management process for a utilities
retailer. Include AS-IS / TO-BE, business requirements with IDs (BR-xxx),
assumptions, and out of scope. Save under outputs/demo-complaint/03-requirements/.
```

**2 — Fit-gap analysis**

```text
Run a fit-gap analysis for these requirements against Salesforce Service Cloud.
Classify each as Standard / Config / Extend / Gap / Defer and recommend the
platform-native option first. Flag open questions for the Solution Architect.
```

**3 — User story generation**

```text
Generate INVEST user stories for customer onboarding in Sales Cloud.
Use Given/When/Then acceptance criteria (nested bullets), business rules,
object impact, security matrix, and BA estimation inputs (T-shirt size only—
no final story points). Save under outputs/demo-onboarding/03-requirements/user-stories/.
```

**4 — Salesforce test strategy**

```text
Draft a Salesforce test strategy from these requirements for a Service Cloud
case management release. Cover scope, test levels, environments, entry/exit
criteria, risks, and traceability to requirements. Route via the QE Enterprise Orchestrator.
```

**5 — Production incident analysis**

```text
Triage a Sev1 production incident: meter readings failed to sync to Salesforce
for the last 2 hours. Provide impact assessment, likely failure domains,
immediate containment steps, evidence to collect, and a hypercare checklist.
Use QE production-support guidance—do not invent org-specific credentials or URLs.
```

**Optional check (BA path):** before a large BA ask, run:

```powershell
python scripts/retrieve_context.py --query "Create a BRD for Service Cloud complaints"
```

If the result is **qe-redirect**, switch to the QE skill—do not stay on the BA path.

## 7. Example Workflow

```
User request
    "Generate user stories for complaint logging in Service Cloud"
        │
        ▼
Routing
    .cursor/rules/routing.mdc
    + scripts/retrieve_context.py (BA)  OR  enterprise-orchestrator (QE)
        │
        ▼
Relevant skill
    salesforce-business-analyst/skill.md
    (+ Tier-0 framework-core contracts)
        │
        ▼
Knowledge
    e.g. knowledge/service-cloud-patterns.md,
         knowledge/user-stories.md
        │
        ▼
Templates / playbooks
    templates/user-story-template.md
    (+ brain/output-framework.md, validation modules)
        │
        ▼
Generated output
    outputs/<project>/03-requirements/user-stories/*.md
    optional: python output-engine/convert.py --file <path>
        │
        ▼
Validation
    brain/validation-framework.md + anti-hallucination
    + checklists.md before you treat the draft as ready
```

## 8. Common Use Cases

| Use case | Ask for… | Starts in |
|----------|----------|-----------|
| Business requirements baseline | BRD / FRD | [BA skill](salesforce-business-analyst/skill.md) + [BRD template](salesforce-business-analyst/templates/brd-template.md) |
| Backlog for a sprint | User stories + AC | [BA skill](salesforce-business-analyst/skill.md) + [user story template](salesforce-business-analyst/templates/user-story-template.md) |
| Build vs configure | Fit-gap table | [Fit-gap playbook](salesforce-business-analyst/playbooks/fit-gap-analysis.md) |
| Discovery workshop | Agenda + notes | [BA playbooks](salesforce-business-analyst/playbooks/README.md) |
| Release test approach | Test strategy | [QE skill](salesforce-quality-engineering/skill.md) + [Enterprise Orchestrator](salesforce-quality-engineering/enterprise-orchestrator/README.md) |
| Sev1 / hypercare | Incident triage | [QE production-support](salesforce-quality-engineering/production-support/README.md) |
| Learn by example | Sample artifacts | [examples/](examples/README.md) |
| Publish to Azure DevOps | Stories / work items | Configure [`.cursor/mcp.json.example`](.cursor/mcp.json.example) → `mcp.json` (never commit secrets) |

## 9. Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Skills / routing not loading | Repo not the workspace root | **File → Open Folder** on the clone root. Confirm `.cursor/rules/` is at the workspace root. |
| Rules ignored in a monorepo | Nested clone | Add this repo as a second root, or install a bridge rule—see [docs/workspace-integration.md](docs/workspace-integration.md). |
| Agent invents process / skips templates | Instructions not applied | Re-open the correct folder; ask the agent to follow [`.cursor/rules/instructions.mdc`](.cursor/rules/instructions.mdc) and [routing.mdc](.cursor/rules/routing.mdc). |
| `retrieve_context.py` fails | Python missing or wrong directory | From repo root: `python scripts/retrieve_context.py --query "your ask"`. Use Python 3. Use `--list-tasks` to see routes. |
| QE ask got BA templates | Wrong route | Rephrase with QE keywords (test strategy, defect, Sev1, hypercare) or open [salesforce-quality-engineering/skill.md](salesforce-quality-engineering/skill.md) explicitly. |
| No `.docx` / `.xlsx` beside Markdown | Output engine optional / not installed | Markdown alone is valid. To convert: install [Pandoc](https://pandoc.org/installing.html), `pip install -r output-engine/requirements.txt`, then `python output-engine/convert.py --file <path-to.md>`. Details: [output-engine/README.md](output-engine/README.md). |

## 10. Next Steps

| Goal | Go here |
|------|---------|
| Full repo overview | [README.md](README.md) |
| Why SEACF exists | [docs/vision.md](docs/vision.md) |
| Nested / multi-root Cursor setup | [docs/workspace-integration.md](docs/workspace-integration.md) |
| Tier-0 contracts | [framework-core/README.md](framework-core/README.md) |
| BA deep dive | [skill-guide.md](salesforce-business-analyst/skill-guide.md) → [skill.md](salesforce-business-analyst/skill.md) |
| QE deep dive | [QE README](salesforce-quality-engineering/README.md) → [skill.md](salesforce-quality-engineering/skill.md) → [Enterprise Orchestrator](salesforce-quality-engineering/enterprise-orchestrator/README.md) |
| Output quality bar | [shared/output-standards.md](shared/output-standards.md) |
| Contribute | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Scope & history | [ROADMAP.md](ROADMAP.md) · [CHANGELOG.md](CHANGELOG.md) |

**Suggested 15-minute practice:** open [examples/sample-project/README.md](examples/sample-project/README.md), then run one BA prompt and one QE prompt from [section 6](#6-your-first-ai-request).
