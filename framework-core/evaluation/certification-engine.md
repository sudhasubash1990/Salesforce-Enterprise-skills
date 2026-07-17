---
title: Certification Engine
version: 0.1.0
tags: [framework-core]
status: draft
last_updated: 2026-07-18
---

# Certification Engine

## Purpose

Cross-module certification level methodology.

## Scope

**In:** Cross-module SEACF contracts reusable by BA, QE, SA, Developer, DevOps, and Production Support packs.  
**Out:** Module-specific deep knowledge (lives in each module); inventing client metrics or certifications.

## Business Context

SEACF modules must share one orchestration, governance, and evaluation language so agents and humans do not re-implement routing, standards, or certification differently per skill.


## Levels (methodology)

| Level | Intent |
|-------|--------|
| Bronze | Core structure + primary engines |
| Silver | Delivery artifacts / integration with backlog tools |
| Gold | Intelligence / analytics layer |
| Platinum | Ops + advisory / architecture governance |
| Enterprise Certified | Platinum + multi-industry benchmarks + regression sample + improvement process |

## Rule

Levels are **not** awarded without a scored session and signed report. Framework Core defines the ladder; modules supply evidence packs.

## Implementations

- QE: `validation/certification/`  
- BA: `validation/certification-report-template.md`  


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

- [scoring-model.md](scoring-model.md)
- [release-readiness.md](release-readiness.md)

## Future Enhancements

- Machine-readable route schemas
- Shared CI hooks for all modules
