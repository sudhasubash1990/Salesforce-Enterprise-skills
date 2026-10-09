---
title: Module Integration Map
version: 0.3.0
---

# Module Integration Map

| Folder | Discipline | Status | Core load order |
|--------|------------|--------|-----------------|
| salesforce-business-analyst | BA | Active | Tier-0 manifest → context-policy → skill.md → brain → knowledge/templates (execution-state-model gates delivery) |
| salesforce-quality-engineering | QE | Active | Tier-0 manifest → context-policy → skill.md → enterprise-orchestrator → engines |
| salesforce-solution-architect | SA | Planned (folder not created) | framework-core → skill.md → architecture brain |
| salesforce-developer | DEV | Planned (folder not created) | framework-core → skill.md → build standards |
| salesforce-devops | DO | Planned (folder not created) | framework-core → skill.md → pipeline intelligence |
| salesforce-production-support | PS (standalone) | Planned (folder not created) | framework-core → skill.md → ITIL/ops engines |

## Production Support — dual narrative (do not conflate)

| Path | What it is |
|------|------------|
| `salesforce-quality-engineering/production-support/` | **QE Sprint 9** ops pack (go-live, hypercare, incident/problem/change, ops intelligence) inside Module 2 |
| `salesforce-production-support/` (planned) | Future **standalone SEACF module** for dedicated Production Support practice — not yet scaffolded |

Until the standalone PS module exists, production-support requests route through QE Sprint 9 via the Enterprise Orchestrator.

## Framework Core maturity

Core **v0.3.0** includes P0 (grounding, instruction precedence, security, tools, Responsible AI), P1 (context lifecycle A–H, claim validation, execution state, observability traces, AI reliability/red-team), and **additive P2 gap-closure** (context-engineering index, BA→QE handoff, project memory, human-review policy, evaluation ba/qe/cross-module indexes) without a version bump. Loading tiers, router contracts, and pointers are enforced; deep engines remain in Active modules (`shared/`, BA, QE). Deepen Core documents as SA/DEV/DO/PS adopt them — do not treat thin Core files as full replacements for module engines.

Cross-module handoff: [handoffs/ba-qe-handoff.md](handoffs/ba-qe-handoff.md). Structured memory: [memory/project-memory-contract.md](memory/project-memory-contract.md).

New modules **MUST** publish a [governance/skill-contract.md](governance/skill-contract.md)-conformant `skill-contract.yaml`. Active BA/QE thin contracts: [`../salesforce-business-analyst/skill-contract.yaml`](../salesforce-business-analyst/skill-contract.yaml), [`../salesforce-quality-engineering/skill-contract.yaml`](../salesforce-quality-engineering/skill-contract.yaml).

Program controls (change plan, DoD, checklist): [governance/hardening-program.md](governance/hardening-program.md).

See [governance/contribution-guide.md](governance/contribution-guide.md) to register a new module.
