---
name: risk-based-regression
short_id: RBRR
description: >-
  Risk-prioritized regression scope for Salesforce releases. Scaffold skill — expand content in a later release.
version: 0.24.0
parent_module: salesforce-quality-engineering
status: scaffold
---

# Risk-Based Regression

**Status:** Scaffold (v0.24.0) — routable shell; full knowledge/playbook pack deferred.

## Purpose

Risk-prioritized regression scope for Salesforce releases

## Hard Rule

Complete risk/context assessment before finalizing regression scope.

## Loading Order

1. Tier-0 `framework-core/`
2. Parent [`../../SKILL.md`](../../SKILL.md) + Enterprise Orchestrator
3. This `SKILL.md` + [`skill-config.yaml`](skill-config.yaml)
4. Cross-linked Sprint engines (below) before inventing process

## Cross-Links (canonical content)

- [Regression Planning](../../knowledge/regression-planning.md)
- [Test Design Engine](../../knowledge/test-design-engine.md)
- [Metadata Impact Analyzer](../metadata-impact-analyzer/SKILL.md)
- [Regression Planning playbook](../../playbooks/regression-planning.md)

## Out of Scope

- Full domain encyclopedia (use Sprint engines linked above)
- Invented MTTR/SLA/% without evidence

## Related

- [README.md](README.md)
- [skills/README.md](../README.md)
