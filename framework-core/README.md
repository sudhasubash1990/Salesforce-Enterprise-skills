---
title: SEACF Framework Core
version: 0.3.0
tags: [framework-core, seacf]
status: draft
last_updated: 2026-10-09
---

# SEACF Framework Core

**Status:** v0.3.0 — Tier-0 contracts for routing, context lifecycle, execution state, grounding/claim validation, security, tool governance, Responsible AI, observability traces, and AI reliability evaluation. Additive P2 gap-closure (same version): BA→QE handoff, project memory, human-review metadata, context-engineering index, evaluation ba/qe/cross-module indexes. Canonical deep content stays in `shared/`, `docs/`, and Active module packs (BA, QE). Thin Core files are intentional contracts, not incomplete copies of module engines.

**Tier-0 manifest:** [tier-0-manifest.yaml](tier-0-manifest.yaml) (single source of truth for `always_load`).

## Purpose

Reusable **Framework Core** for the Salesforce Enterprise AI Consulting Framework (SEACF). Every present and future module—Business Analyst, Quality Engineering, Solution Architect, Developer, DevOps, Production Support—loads this core for orchestration, shared knowledge pointers, governance, and evaluation.

## Business Context

Without a core, each module invents its own router, glossary fork, and certification logic. Framework Core is the **single contract** for:

1. How requests are routed and reasoned  
2. Where shared Salesforce / industry / consulting knowledge lives  
3. How documentation and quality are governed  
4. How modules are benchmarked, scored, and certified  
5. How grounding, instruction precedence, untrusted content, tools, and Responsible AI apply cross-module  
6. How context lifecycle, execution state, claim validation, and audit traces apply cross-module  

## Scope

| In | Out |
|----|-----|
| Cross-module orchestration contracts | Full BA/QE/SA domain engines |
| Pointers + thin shared indexes | Duplicating `shared/` or module knowledge bodies |
| Governance, grounding, security, tools, RAI, observability | Awarding certification without evidence |
| Module integration map | Replacing module `skill.md` |

## Architecture

```
User Request
   |
   v
SECURITY + RESPONSIBLE AI + INSTRUCTION PRECEDENCE  [Tier-0]
   |
   v
CONTEXT ENGINE --> GROUNDING / SOURCE AUTHORITY --> REQUEST ROUTER
   |                                           |
   |                                           v
   |                                    BA / QE / Future Skill
   |                                           |
   |                                 Brain + Knowledge + Playbooks
   |                                           |
   +----------------------------------> Tool / Action Gateway
                                               |
                                               v
                                     Output + Claim Validation
                                               |
                                               v
                                      Evaluation + Audit Trace
```

## Folder map

| Path | Role |
|------|------|
| [orchestration/](orchestration/README.md) | Request routing, context policy, execution state, workflow, reasoning |
| [grounding/](grounding/README.md) | Evidence, claim validation, source authority, citations, conflicts |
| [security/](security/README.md) | Untrusted content, prompt-injection defence, secrets |
| [tools/](tools/README.md) | Tool governance, risk tiers, manifests, retry |
| [responsible-ai/](responsible-ai/README.md) | Cross-module RAI and data governance |
| [observability/](observability/README.md) | Decision/audit trace contract (no chain-of-thought) |
| [handoffs/](handoffs/README.md) | Cross-module BA→QE handoff contract + schema |
| [memory/](memory/README.md) | Structured project memory contract |
| [shared-knowledge/](shared-knowledge/README.md) | Cross-module Salesforce, industry, consulting, glossary |
| [governance/](governance/README.md) | Documentation, quality, precedence, skill/prompt contracts, human review, hardening program, versioning |
| [evaluation/](evaluation/README.md) | Benchmark, scoring, certification, AI reliability / red-team + ba/qe/cross-module indexes |
| [tier-0-manifest.yaml](tier-0-manifest.yaml) | Machine-readable always_load / on-demand lists |

## Module integration

| Module | Status | Skill entry | Uses core |
|--------|--------|-------------|-----------|
| Business Analyst | Active | `salesforce-business-analyst/skill.md` | Load Tier-0 manifest; BA router remains in `.cursor/rules` |
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
- [governance/instruction-precedence.md](governance/instruction-precedence.md)
- [governance/documentation-standards.md](governance/documentation-standards.md)
- [evaluation/certification-engine.md](evaluation/certification-engine.md)

## Future Enhancements

- LLM-executed adversarial / red-team runner; runtime trace collector; context token budgeting clocks
- SA/DEV/DO/PS module scaffolds that import this core on day one