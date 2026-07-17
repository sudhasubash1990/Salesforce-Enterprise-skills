---
title: Regression and Coverage Rules
module: Salesforce Quality Engineering
category: Quality Intelligence
document_type: Reference
version: 0.9.1
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
tags: [quality-intelligence, sprint-7, rules-engine]
---

# Regression and Coverage Rules

## Purpose

Decide when to expand, focus, or challenge regression and requirement/test coverage based on quality signals.

## Business Context

Regression scope should follow risk and evidence—not habit or fear alone.

## Overview

Complements QI-R-MET-001 and hotspot rules with regression-specific actions.

## Inputs

Escape list, change impact, coverage metrics, prior regression effectiveness.

## Outputs

Fired `QI-R-REG-*` recommendations.

## Process

---

### QI-R-REG-001 — Expand Regression After Leakage / Escapes

| Field | Content |
|-------|---------|
| **IF** | Defect Leakage > threshold **or** escaped defects in module/journey |
| **THEN** | 1) Expand regression **for escaped areas** (not necessarily entire org) 2) Review requirement & scenario coverage for those areas 3) Update regression pack ownership and cadence 4) Re-run readiness against expanded pack |
| **Priority** | P1 |
| **Pairs with** | QI-R-MET-001, QI-R-MET-005 |
| **Note** | This is the canonical “leakage → expand regression + coverage review” rule family |

---

### QI-R-REG-002 — Regression Ineffective (Escapes Despite Execution)

| Field | Content |
|-------|---------|
| **IF** | Regression executed with high pass rate **but** escapes still occur in covered areas |
| **THEN** | 1) Challenge scenario quality (oracle, data, persona) 2) Add negative/permission/integration variants 3) Review whether “covered” was traceability fiction |
| **Priority** | P1 |
| **Related** | [regression-effectiveness](../quality-metrics/regression-effectiveness.md) |

---

### QI-R-REG-003 — Change Without Impact-Based Regression

| Field | Content |
|-------|---------|
| **IF** | High-impact metadata change (Flow/Apex/sharing/integration) with no mapped regression |
| **THEN** | 1) Block or condition gate until impact pack defined 2) Generate impact-based scenarios via Test Design Engine |
| **Priority** | P0–P1 |
| **Related** | Sprint 3 Test Design Engine |

## Examples

Two escapes in Billing Flow → QI-R-REG-001: add Billing Flow suite + AC coverage review for invoice adjustment stories; do not mandate full Sales Cloud regression.

## Best Practices

- Scope expansion is targeted first, broad second.  
- Always close the loop into RTM/scenario packs.

## Common Mistakes

- Doubling entire regression suite after one escape.  
- Expanding automation instead of fixing oracle/data.

## Interview Questions

- How do you expand regression intelligently after leakage?  
- When is regression “green” still a quality risk?

## Related Documents

- [Metric Threshold Rules](metric-threshold-rules.md)
- [Release Gate Rules](release-gate-rules.md)

## Navigation

- **Previous:** [automation-stability-rules.md](automation-stability-rules.md)
- **Next:** [release-gate-rules.md](release-gate-rules.md)

## Future Enhancements

- Impact-pack selection heuristics by metadata type  
