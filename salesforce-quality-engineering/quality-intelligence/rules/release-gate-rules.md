---
title: Release Gate Rules
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

# Release Gate Rules

## Purpose

Translate quality-gate and readiness risks into go/no-go oriented recommendations.

## Business Context

Gates fail for reasons; rules should prescribe remediation paths, not only “fail the gate.”

## Overview

Works with [quality-gates/](../quality-gates/README.md) and Sprint 6 governance.

## Inputs

Gate checklist results, open Sev defects, leakage, coverage gaps, prod cluster signals.

## Outputs

Fired `QI-R-GAT-*` recommendations.

## Process

---

### QI-R-GAT-001 — Predicted or Actual Quality Gate Failure

| Field | Content |
|-------|---------|
| **IF** | Entry/Exit/Release gate criteria unmet **or** predictive gate-failure confidence High |
| **THEN** | 1) List failing criteria with evidence 2) Recommend remediation owners/dates 3) Option paths: fix-forward, scope cut, defer, or No-Go 4) Do not greenwash residual risk |
| **Priority** | P0 |
| **Related** | [quality-gate-failures](../predictive-quality/quality-gate-failures.md) |

---

### QI-R-GAT-002 — Open Sev1/Sev2 Without Waiver

| Field | Content |
|-------|---------|
| **IF** | Open Sev1/Sev2 in release scope without approved waiver |
| **THEN** | 1) Default recommend No-Go or conditional go with executive waiver 2) Require mitigation & monitoring plan |
| **Priority** | P0 |

---

### QI-R-GAT-003 — Cloud/Integration Cluster Before Release

| Field | Content |
|-------|---------|
| **IF** | QI-R-CLD-001 or QI-R-INT-001 fired in pre-prod/prod window before release |
| **THEN** | 1) Elevate targeted regression + readiness checks as **gate dependencies** 2) Add area-specific smoke to go-live plan |
| **Priority** | P0–P1 |
| **Pairs with** | integration-and-cloud-cluster-rules |

## Examples

Exit gate fails on RTM gaps + two Sev2 → QI-R-GAT-001/002: No-Go unless waiver; close RTM for Must stories; mitigation for Sev2.

## Best Practices

- Separate gate status from political pressure.  
- Always state residual risk if Conditional Go.

## Common Mistakes

- Passing gate on green automation while leakage rules fire.  
- Silent waivers without monitoring.

## Interview Questions

- How should fired QI rules influence go/no-go?  
- What is a conditional go?

## Related Documents

- [Recommendation Priority](recommendation-priority.md)
- [../quality-gates/README.md](../quality-gates/README.md)

## Navigation

- **Previous:** [regression-and-coverage-rules.md](regression-and-coverage-rules.md)
- **Next:** [recommendation-priority.md](recommendation-priority.md)

## Future Enhancements

- Gate decision tree visual  
