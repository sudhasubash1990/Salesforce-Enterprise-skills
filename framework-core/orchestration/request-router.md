---
title: Request Router
version: 0.1.0
tags: [framework-core]
status: draft
last_updated: 2026-07-18
---

# Request Router

## Purpose

Classify intent and route to the correct SEACF module and capability engine.

## Scope

**In:** Cross-module SEACF contracts reusable by BA, QE, SA, Developer, DevOps, and Production Support packs.  
**Out:** Module-specific deep knowledge (lives in each module); inventing client metrics or certifications.

## Business Context

SEACF modules must share one orchestration, governance, and evaluation language so agents and humans do not re-implement routing, standards, or certification differently per skill.


## Evaluation Method

1. Detect **discipline** (BA / QE / SA / DEV / DO / PS).  
2. Detect **capability** within module (e.g. BRD vs user story; requirement analysis vs advisory).  
3. Emit Route line: `Module · Primary capability · Support · Advisory/Validation`.  
4. Hand off to module skill Pre-Execution Gate.

## Decision Framework

| Signal | Module |
|--------|--------|
| BRD, FRD, user story, fit-gap, workshop, KPI, OCM | Business Analyst |
| Test strategy, defects, automation, UAT quality, prod incident QE lens, project health | Quality Engineering |
| Target architecture, integration design, Well-Architected | Solution Architect (when pack exists) |
| Apex/LWC implementation, package, metadata deploy code | Developer (when pack exists) |
| Pipeline, CI/CD, environments, DevOps Center | DevOps (when pack exists) |
| Incident/problem/change ops (standalone pack) | Production Support pack — until then QE Sprint 9 |

## Ambiguity

If discipline unclear → ask **one** clarifying question. Prefer BA for requirements authorship; QE for testability/quality; SA for architecture decisions.

## Module implementations

- QE: [salesforce-quality-engineering/enterprise-orchestrator/](../../salesforce-quality-engineering/enterprise-orchestrator/README.md)
- BA: [.cursor/rules/routing.mdc](../../.cursor/rules/routing.mdc) + `scripts/retrieve_context.py`


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

- [context-manager.md](context-manager.md)
- [workflow-engine.md](workflow-engine.md)
- [../README.md](../README.md)

## Future Enhancements

- Machine-readable route schemas
- Shared CI hooks for all modules
