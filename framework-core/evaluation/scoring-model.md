---
title: Scoring Model
version: 0.1.0
tags: [framework-core]
status: draft
last_updated: 2026-07-18
---

# Scoring Model

## Purpose

Shared Pass / Partial / Fail model with optional weights.

## Scope

**In:** Cross-module SEACF contracts reusable by BA, QE, SA, Developer, DevOps, and Production Support packs.  
**Out:** Module-specific deep knowledge (lives in each module); inventing client metrics or certifications.

## Business Context

SEACF modules must share one orchestration, governance, and evaluation language so agents and humans do not re-implement routing, standards, or certification differently per skill.


## Scale

| Result | Value | Meaning |
|--------|-------|---------|
| Pass | 2 | Criteria met with evidence |
| Partial | 1 | Core present; gaps logged |
| Fail | 0 | Missing capability or hard-rule breach |

## Rules

1. **No invented percentages** without completing dimension rows.  
2. Hard-rule Fail (hallucinated SLA/cert/regulation) fails the area regardless of average.  
3. Modules declare weights in their scorecards (QE example: `validation/quality-scorecards/`).


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

- [certification-engine.md](certification-engine.md)
- [../governance/quality-standards.md](../governance/quality-standards.md)

## Future Enhancements

- Machine-readable route schemas
- Shared CI hooks for all modules
