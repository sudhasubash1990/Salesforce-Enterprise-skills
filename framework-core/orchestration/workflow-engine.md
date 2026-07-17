---
title: Workflow Engine
version: 0.1.0
tags: [framework-core]
status: draft
last_updated: 2026-07-18
---

# Workflow Engine

## Purpose

Compose multi-step consulting workflows across and within modules.

## Scope

**In:** Cross-module SEACF contracts reusable by BA, QE, SA, Developer, DevOps, and Production Support packs.  
**Out:** Module-specific deep knowledge (lives in each module); inventing client metrics or certifications.

## Business Context

SEACF modules must share one orchestration, governance, and evaluation language so agents and humans do not re-implement routing, standards, or certification differently per skill.


## Standard composition patterns

| Pattern | Order |
|---------|-------|
| Requirements → Stories | BA analysis → BA stories → (optional) QE testability review |
| Story → Test design | QE Sprint 2 → Sprint 3 → Sprint 5 docs |
| Defect → Prevention | QE Sprint 7 → 8/9 as needed → 10 if exec |
| Incident → Restore | PS/QE Sprint 9 first → RCA → advisory |
| Architecture decision | SA (or open question) → BA/QE impact |
| Framework certify | evaluation/ + module validation packs |

## Handoff contract

Every hop passes: IDs, assumptions, open questions, evidence refs, residual risk.


## Inputs

- User request / module intent
- Module `skill.md` and brain (when loaded)
- Optional evidence pack

## Outputs

- Route / context / workflow decisions
- References into module engines
- Governance-compliant artifacts

## Navigation

- **Up:** [README.md](../README.md) or parent folder README
- **Core root:** [../README.md](../README.md) 

## Related Documents

- [reasoning-pipeline.md](reasoning-pipeline.md)
- QE [composition-patterns.md](../../salesforce-quality-engineering/enterprise-orchestrator/composition-patterns.md)

## Future Enhancements

- Machine-readable route schemas
- Shared CI hooks for all modules
