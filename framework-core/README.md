---
title: SEACF Framework Core
version: 0.1.0
tags: [framework-core, seacf]
status: draft
last_updated: 2026-07-18
---

# SEACF Framework Core

## Purpose

Reusable **Framework Core** for the Salesforce Enterprise AI Consulting Framework (SEACF). Every present and future module—Business Analyst, Quality Engineering, Solution Architect, Developer, DevOps, Production Support—loads this core for orchestration, shared knowledge pointers, governance, and evaluation.

## Business Context

Without a core, each module invents its own router, glossary fork, and certification logic. Framework Core is the **single contract** for:

1. How requests are routed and reasoned  
2. Where shared Salesforce / industry / consulting knowledge lives  
3. How documentation and quality are governed  
4. How modules are benchmarked, scored, and certified  

## Scope

| In | Out |
|----|-----|
| Cross-module orchestration contracts | Full BA/QE/SA domain engines |
| Pointers + thin shared indexes | Duplicating `shared/` or module knowledge bodies |
| Governance & evaluation methodology | Awarding certification without evidence |
| Module integration map | Replacing module `skill.md` |

## Architecture

```
User Request
      │
      ▼
framework-core/orchestration  (route · context · workflow · reasoning)
      │
      ▼
Module skill (BA | QE | SA | DEV | DO | PS)
      │
      ├── module brain + engines
      └── framework-core/shared-knowledge (pointers)
      │
      ▼
framework-core/governance  (standards · versioning · contribution)
      │
      ▼
framework-core/evaluation  (benchmark · score · certify · release readiness)
```

## Folder map

| Path | Role |
|------|------|
| [orchestration/](orchestration/README.md) | Request routing, context, workflow, reasoning pipeline |
| [shared-knowledge/](shared-knowledge/README.md) | Cross-module Salesforce, industry, consulting, glossary |
| [governance/](governance/README.md) | Documentation, quality, versioning, contribution |
| [evaluation/](evaluation/README.md) | Benchmark, scoring, certification, release readiness |

## Module integration

| Module | Status | Skill entry | Uses core |
|--------|--------|-------------|-----------|
| Business Analyst | Active | `salesforce-business-analyst/skill.md` | Load governance + shared-knowledge; BA router remains in `.cursor/rules` |
| Quality Engineering | Active | `salesforce-quality-engineering/skill.md` | Orchestrator aligns to core; validation aligns to evaluation/ |
| Solution Architect | Planned | — | Same contracts |
| Developer | Planned | — | Same contracts |
| DevOps | Planned | — | Same contracts |
| Production Support (standalone pack) | Planned | — | QE Sprint 9 remains until pack extracts |

**Rule:** Module engines own depth. Framework Core owns **contracts and shared indexes**. Prefer link over copy ([docs/multi-lens-policy.md](../docs/multi-lens-policy.md) themes apply cross-module).

## Relationship to existing repo roots

| Existing | Relationship |
|----------|----------------|
| [`shared/`](../shared/README.md) | Canonical enterprise files; `shared-knowledge/` indexes and extends |
| [`docs/`](../docs/README.md) | Repo governance; `governance/` summarizes + points here |
| QE `enterprise-orchestrator/` | Module-specific router; implements core orchestration contracts |
| QE `validation/` (Sprint 11) | Module evaluation pack; implements core evaluation contracts |
| BA `validation/` | BA certification; maps to core evaluation |

## Inputs / Outputs

- **Inputs:** Any SEACF user request  
- **Outputs:** Route plan, loaded module bundle, governed deliverable, optional evaluation

## Navigation

- **Repo root:** [../README.md](../README.md)
- **Roadmap:** [../ROADMAP.md](../ROADMAP.md)

## Related Documents

- [orchestration/request-router.md](orchestration/request-router.md)
- [governance/documentation-standards.md](governance/documentation-standards.md)
- [evaluation/certification-engine.md](evaluation/certification-engine.md)

## Future Enhancements

- `scripts/retrieve_context.py` routes that include framework-core by default
- SA/DEV/DO/PS module scaffolds that import this core on day one
