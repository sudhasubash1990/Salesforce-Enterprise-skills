---
title: Module Integration Map
version: 0.1.0
---

# Module Integration Map

| Folder | Discipline | Status | Core load order |
|--------|------------|--------|-----------------|
| salesforce-business-analyst | BA | Active | framework-core → skill.md → brain → knowledge/templates |
| salesforce-quality-engineering | QE | Active | framework-core → skill.md → enterprise-orchestrator → engines |
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

Core v0.1.0 is a **contract scaffold**: loading tiers, router contracts, and pointers are enforced; deep engines remain in Active modules (`shared/`, BA, QE). Deepen Core documents as SA/DEV/DO/PS adopt them — do not treat thin Core files as full replacements for module engines.

See [governance/contribution-guide.md](governance/contribution-guide.md) to register a new module.
