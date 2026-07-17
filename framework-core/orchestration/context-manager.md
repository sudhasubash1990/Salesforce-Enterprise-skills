---
title: Context Manager
version: 0.1.0
tags: [framework-core]
status: draft
last_updated: 2026-07-18
---

# Context Manager

## Purpose

Define progressive disclosure: load the minimum file bundle for a request.

## Scope

**In:** Cross-module SEACF contracts reusable by BA, QE, SA, Developer, DevOps, and Production Support packs.  
**Out:** Module-specific deep knowledge (lives in each module); inventing client metrics or certifications.

## Business Context

SEACF modules must share one orchestration, governance, and evaluation language so agents and humans do not re-implement routing, standards, or certification differently per skill.


## Loading tiers

| Tier | Load | When |
|------|------|------|
| 0 | `framework-core/` contracts (this pack) | Any SEACF task |
| 1 | Module `skill.md` + identity/brain entry | Any module task |
| 2 | Task engines (analysis, design, templates) | Per intent |
| 3 | Deep knowledge articles | Only when component/cloud implicated |
| 4 | Evaluation / certification | When validating the framework or module |

## Rules

1. **Do not** preload all modules.  
2. Prefer README → engine → article.  
3. Shared knowledge via [../shared-knowledge/](../shared-knowledge/README.md) before copying into a module.  
4. Mark assumptions when context is missing.


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

- [request-router.md](request-router.md)
- [../../shared/README.md](../../shared/README.md)

## Future Enhancements

- Machine-readable route schemas
- Shared CI hooks for all modules
