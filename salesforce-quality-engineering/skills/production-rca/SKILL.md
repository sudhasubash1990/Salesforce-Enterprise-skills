---
name: production-rca
short_id: PRCA
description: >-
  Production defect and incident root-cause analysis for Salesforce programs. Scaffold skill — expand content in a later release.
version: 0.24.0
parent_module: salesforce-quality-engineering
status: scaffold
---

# Production RCA

**Status:** Scaffold (v0.24.0) — routable shell; full knowledge/playbook pack deferred.

## Purpose

Production defect and incident root-cause analysis for Salesforce programs

## Hard Rule

Capture incident context + timeline before RCA hypotheses.

## Loading Order

1. Tier-0 `framework-core/`
2. Parent [`../../SKILL.md`](../../SKILL.md) + Enterprise Orchestrator
3. This `SKILL.md` + [`skill-config.yaml`](skill-config.yaml)
4. Cross-linked Sprint engines (below) before inventing process

## Cross-Links (canonical content)

- [Sprint 7 Root Cause Analysis](../../quality-intelligence/root-cause-analysis/)
- [Sprint 9 Incident Management](../../production-support/incident-management/)
- [Defect RCA Report template](../../templates/defect-rca-report.md)

## Out of Scope

- Full domain encyclopedia (use Sprint engines linked above)
- Invented MTTR/SLA/% without evidence

## Related

- [README.md](README.md)
- [skills/README.md](../README.md)
