---
title: Readme
module: Salesforce Enterprise Skills
category: Root
document_type: Guide
version: 1.10.0
review_status: Approved
owner: SEACF Practice Lead
created_date: 2026-07-02
last_updated: 2026-08-04
review_cycle: quarterly
related_brain_modules:
  - salesforce-business-analyst/brain/README.md
  - salesforce-quality-engineering/brain/README.md
related_knowledge:
  - salesforce-business-analyst/knowledge/README.md
  - salesforce-quality-engineering/knowledge/README.md
  - framework-core/shared-knowledge/README.md
related_templates:
  - salesforce-business-analyst/templates/README.md
  - salesforce-quality-engineering/templates/README.md
related_playbooks:
  - salesforce-business-analyst/playbooks/README.md
  - salesforce-quality-engineering/playbooks/README.md
related_scenarios:
  - salesforce-business-analyst/scenarios/README.md
  - salesforce-quality-engineering/scenarios/README.md
related_interview_topics:
  - salesforce-business-analyst/interview-guide/interview-index.md
related_examples: [examples/sample-project/README.md]
related_documents:
  - docs/cross-linking-framework.md
  - docs/workspace-integration.md
  - ROADMAP.md
  - framework-core/README.md
  - CHANGELOG.md
  - salesforce-quality-engineering/skills/README.md
keywords: [README, SEACF]
tags: [README, SEACF]
---

# Salesforce Enterprise Skills

Enterprise-grade knowledge repository for Salesforce consulting disciplines—designed for **Cursor**, **Claude**, and human practitioners. Packages delivery experience into reusable skills, playbooks, templates, and governance artifacts under the **Salesforce Enterprise AI Consulting Framework (SEACF)**.

Cross-module contracts live in **[`framework-core/`](framework-core/README.md)** so Business Analyst, Quality Engineering, and future Architect / Developer / DevOps / Production Support packs share one orchestration, governance, and evaluation model.

## What's New (v1.10.0 — 2026-08-04)

Assessment-feedback hardening and workspace activation guidance:

- **[Workspace Integration Guide](docs/workspace-integration.md)** — how to activate SEACF skill routing when this repository is **not** your workspace root: open as own workspace, multi-root workspace (recommended), a copy-paste **bridge rule** for permanently nested clones, or user-level skill stubs. Includes an option comparison and a verification checklist.
- **BA retriever Windows fix** — `scripts/retrieve_context.py` no longer crashes on default Windows (cp1252) consoles when printing the QE redirect; output streams are forced to UTF-8.
- **Module-scoped validation schemas** — `scripts/validate_metadata.py` now applies the BA nine-section cross-linking contract only where it was authored (BA module, docs, shared, examples) and validates QE + `framework-core/` against their own lighter frontmatter contract; `archive/` and `.cursor/skills/` stubs are excluded. Validator findings dropped from ~20,000 false failures to a genuine, actionable backlog.
- **Output engine** — Word conversion now resolves relative image paths against the Markdown source directory, so embedded diagrams render in generated `.docx` files.

## Purpose

Salesforce programs fail more often from unclear requirements, weak quality gates, and misaligned solution decisions than from pure technical gaps. This repository encodes **how experienced practitioners think, document, and decide**—across Active modules today (BA + QE) with a shared Framework Core.

## Architecture (SEACF)

```
User Request
      │
      ▼
framework-core/          ← Tier-0 contracts (always load)
      │
      ├─► salesforce-business-analyst/     (Module 1 — Active)
      └─► salesforce-quality-engineering/  (Module 2 — Active)
              └─ enterprise-orchestrator/  (intra-QE routing)
```

| Layer | Path | Role |
|-------|------|------|
| Tier-0 | [`framework-core/`](framework-core/README.md) | Cross-module routing contracts, shared-knowledge indexes, governance, evaluation |
| BA Layer 2 | [`scripts/retrieve_context.py`](scripts/retrieve_context.py) + [`.cursor/rules/routing.mdc`](.cursor/rules/routing.mdc) | BA file-bundle retriever (QE keywords redirect to Module 2) |
| QE router | [`enterprise-orchestrator/`](salesforce-quality-engineering/enterprise-orchestrator/README.md) | Sprint capability routing inside Quality Engineering |

## Repository Structure

| Path | Purpose |
|------|---------|
| [`framework-core/`](framework-core/README.md) | **SEACF Framework Core** (v0.1.0 scaffold) — orchestration, shared-knowledge indexes, governance, evaluation |
| [`.cursor/`](.cursor/README.md) | Agent rules + Cursor discovery stubs for BA and QE |
| [`docs/`](docs/README.md) | Repository governance, architecture, and quality standards |
| [`shared/`](shared/README.md) | Canonical cross-discipline glossary, taxonomy, consulting principles |
| [`examples/`](examples/README.md) | Reference artifacts (BRDs, user stories, workshops, projects) |
| [`salesforce-business-analyst/`](salesforce-business-analyst/README.md) | **Module 1** — BA skill, brain, knowledge, templates, playbooks, scenarios |
| [`salesforce-quality-engineering/`](salesforce-quality-engineering/README.md) | **Module 2** — QE skill through Sprint 11 + unified [`skills/`](salesforce-quality-engineering/skills/README.md) specialized packs |
| [`scripts/`](scripts/README.md) | Context retriever, metadata enrichment, repository validation |
| [`output-engine/`](output-engine/README.md) | Markdown → office format conversion |
| `archive/` | Legacy materials (not on the active skill path) |

## Current Skills

| Skill | Status | Description |
|-------|--------|-------------|
| SEACF Framework Core | Active (v0.1.0) | Tier-0 contracts: orchestration, shared-knowledge indexes, governance, evaluation ([`framework-core/`](framework-core/README.md)) |
| Salesforce Business Analyst | Active (v1.7.1) | Discovery → BRD/FRD/stories, fit-gap, OCM/digital transformation, interview guide, validation; Cursor stub [`.cursor/skills/salesforce-business-analyst/`](.cursor/skills/salesforce-business-analyst/SKILL.md) |
| Salesforce Quality Engineering | Active (v0.24.0) | Enterprise Orchestrator; Sprint 1–11 engines; unified [`skills/`](salesforce-quality-engineering/skills/README.md) specialized packs (MIA, SOVA, PTA, AFT, FSQA, TDG, PWR, OSQA, DMQA, PRCA, RBRR); Cursor stub [`.cursor/skills/salesforce-quality-engineering/`](.cursor/skills/salesforce-quality-engineering/SKILL.md) |

### Planned modules (not yet scaffolded)

Solution Architect · Developer · DevOps · standalone Production Support — see [ROADMAP.md](ROADMAP.md) and [framework-core/MODULE-INTEGRATION.md](framework-core/MODULE-INTEGRATION.md).

> **Note:** QE Sprint 9 `production-support/` is an **ops pack inside Module 2**, not the planned standalone Production Support module.

## Installation (Cursor)

Open this repository as a Cursor workspace — agent rules auto-load and route BA or QE requests to the correct skill.

### 1. Download the repository

```bash
git clone https://github.com/sudhasubash1990/Salesforce-Enterprise-skills.git
```

Or: GitHub **Code → Download ZIP** and extract.

### 2. Open the folder in Cursor

**File → Open Folder** → select the `Salesforce-Enterprise-skills` folder. Cursor picks up `.cursor/rules/` (routing, instructions, user-story generation, output generation) and discovery stubs under `.cursor/skills/`.

> **Using this repo inside another workspace?** Rules only auto-load when this folder is a workspace root. See the **[Workspace Integration Guide](docs/workspace-integration.md)** for activating skill routing from any workspace root — multi-root workspaces, the bridge rule for nested clones, and user-level skill stubs.

### 3. Start asking

**Business Analyst examples**

- *"Create a BRD for a Service Cloud complaint management process"*
- *"Generate user stories for customer onboarding"*
- *"Run a fit-gap analysis for these requirements"*
- *"Define KPI baselines and a change management strategy"*

**Quality Engineering examples**

- *"Draft a Salesforce test strategy from these requirements"*
- *"Triage a Sev1 production incident for meter readings"*
- *"Assess project quality health for the steering committee"*
- *"Run Sprint 11 validation against the QE framework"*
- *"Analyze metadata impact for this package.xml"*
- *"Validate OmniScript / DataRaptor journey for Move-In"*
- *"Review Playwright locators for Salesforce login POM"*

Routing loads the right Framework Core contracts, brain modules, knowledge, and templates automatically.

### 4. Optional — Azure DevOps publishing

Copy `.cursor/mcp.json.example` to `.cursor/mcp.json` and fill in organization, project, and PAT. Never commit `.cursor/mcp.json` — it is git-ignored.

### 5. Optional — Office file conversion

Install [Pandoc](https://pandoc.org/installing.html), then:

```bash
pip install -r output-engine/requirements.txt
```

Deliverables still work as Markdown if you skip this.

## Getting Started

### For Human Practitioners

1. Read [docs/vision.md](docs/vision.md) for strategic intent.
2. Skim [framework-core/README.md](framework-core/README.md) for Tier-0 contracts.
3. **BA:** [skill-guide.md](salesforce-business-analyst/skill-guide.md) → [skill.md](salesforce-business-analyst/skill.md).
4. **QE:** [salesforce-quality-engineering/README.md](salesforce-quality-engineering/README.md) → [skill.md](salesforce-quality-engineering/skill.md) → [enterprise-orchestrator/](salesforce-quality-engineering/enterprise-orchestrator/README.md) → [skills/](salesforce-quality-engineering/skills/README.md) for specialized packs.
5. Check [ROADMAP.md](ROADMAP.md) and [CHANGELOG.md](CHANGELOG.md) for current scope.

### For AI Agents (Cursor)

1. Load Tier-0: `framework-core/README.md`, `orchestration/request-router.md`, `orchestration/context-manager.md`, `governance/quality-standards.md`.
2. Load [`.cursor/rules/instructions.mdc`](.cursor/rules/instructions.mdc) and [`.cursor/rules/routing.mdc`](.cursor/rules/routing.mdc).
3. For BA requests, run:

```powershell
python scripts/retrieve_context.py --query "<request>"
```

Load the returned bundle. If the result is **qe-redirect**, switch to `salesforce-quality-engineering/skill.md` and the Enterprise Orchestrator — do not continue on the BA path.

4. Complete the module Pre-Execution Gate before any deliverable.
5. Follow [shared/output-standards.md](shared/output-standards.md) for generated artifacts. Save under `outputs/<project>/` and run `python output-engine/convert.py --file <path>` when publishing office formats.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Contributions must follow [docs/markdown-standards.md](docs/markdown-standards.md) and pass `python scripts/validate_repository.py`. New modules register via [framework-core/governance/contribution-guide.md](framework-core/governance/contribution-guide.md).

## License

MIT — see [LICENSE](LICENSE).

## Related Brain Modules

- [BA Brain](salesforce-business-analyst/brain/README.md)
- [QE Brain](salesforce-quality-engineering/brain/README.md)

## Related Knowledge

- [BA Knowledge](salesforce-business-analyst/knowledge/README.md)
- [QE Knowledge](salesforce-quality-engineering/knowledge/README.md)
- [Framework Core shared-knowledge](framework-core/shared-knowledge/README.md)

## Related Templates

- [BA Templates](salesforce-business-analyst/templates/README.md)
- [QE Templates](salesforce-quality-engineering/templates/README.md)

## Related Playbooks

- [BA Playbooks](salesforce-business-analyst/playbooks/README.md)
- [QE Playbooks](salesforce-quality-engineering/playbooks/README.md)

## Related Industry Scenarios

- [BA Scenarios](salesforce-business-analyst/scenarios/README.md)
- [QE Scenarios](salesforce-quality-engineering/scenarios/README.md)

## Related Interview Topics

- [BA Interview Index](salesforce-business-analyst/interview-guide/interview-index.md)

## Related Examples

- [Sample project](examples/sample-project/README.md)

## Related Documents

- [Framework Core](framework-core/README.md)
- [Module Integration](framework-core/MODULE-INTEGRATION.md)
- [Cross Linking Framework](docs/cross-linking-framework.md)
- [Workspace Integration Guide](docs/workspace-integration.md) — activate skill routing from any workspace root
- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)

## Traceability

**Upstream:** — | **Downstream:** All skills | **Validation:** ROADMAP + CHANGELOG alignment

## Navigation

- **Previous:** —
- **Next:** [Framework Core](framework-core/README.md) · [BA Readme](salesforce-business-analyst/README.md) · [QE Readme](salesforce-quality-engineering/README.md)
- **See Also:** [cross-linking-framework](docs/cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.10.0 | 2026-08-04 | SEACF Practice Lead | Workspace integration guide (skill routing from any workspace root), retriever Windows console fix, module-scoped validator schemas, Word image-path resolution |
| 1.9.0 | 2026-07-28 | SEACF Practice Lead | QE unified skills/ (v0.24.0), registry, specialized-pack examples, CONTRIBUTING/ROADMAP/.gitignore alignment |
| 1.8.0 | 2026-07-18 | SEACF Practice Lead | Multi-module SEACF README: Framework Core + BA + QE, Tier-0 routing, planned modules, agent getting-started |
| 1.7.0 | 2026-07-03 | BA Practice Lead | Transformation coverage: KPI/OCM/digital transformation; retriever and routing support |
| 1.6.0 | 2026-07-02 | BA Practice Lead | Layer 2 deterministic context retriever |
| 1.5.0 | 2026-07-02 | BA Practice Lead | Sprint 10 pre-execution gate and related BA hardening |
| 1.4.0 | 2026-07-02 | BA Practice Lead | ADO backlog integration, estimation discipline |
| 1.3.0 | 2026-07-02 | BA Practice Lead | Sprints 8–9 validation and continuous KM |
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
