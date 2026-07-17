---
title: Quality Intelligence Rule Schema
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

# Quality Intelligence Rule Schema

## Purpose

Standard structure for every Quality Intelligence decision rule so the AI evaluates and explains them consistently.

## Business Context

Auditable quality advice requires transparent conditions, thresholds, and recommended actions—not opaque “AI judgment.”

## Overview

Every rule uses:

| Field | Description |
|-------|-------------|
| **Rule ID** | `QI-R-<DOMAIN>-NNN` (e.g., `QI-R-MET-001`) |
| **Name** | Short business name |
| **Signal type** | Metric · Pattern · Cluster · Trend · Gate |
| **IF (condition)** | Observable predicate |
| **Threshold** | Program value or *indicative default* |
| **Required evidence** | What must be present to fire |
| **THEN (actions)** | Ordered recommendations |
| **Follow-on** | RCA / reviews / suites to trigger |
| **Priority default** | P0–P3 |
| **Escalate when** | Conditions for leadership escalation |
| **Related** | Metrics, patterns, SF knowledge links |
| **Do not fire if** | Suppress conditions |

## Inputs

Rule authoring needs: signal definitions from [quality-metrics/](../quality-metrics/README.md) and [defect-patterns/](../defect-patterns/README.md).

## Outputs

Normalized rule cards consumable by [rules-engine.md](rules-engine.md).

## Process

When stating a rule in an answer:

```markdown
### QI-R-MET-001 — Elevated Defect Leakage
- **IF:** Defect Leakage > threshold (evidence: …)
- **THEN:**
  1. Expand regression scope for escaped modules
  2. Review requirement/scenario coverage for escape cohort
- **Priority:** P1
- **Confidence:** Medium (threshold indicative)
```

## Examples

See packs under this folder (`metric-threshold-rules.md`, etc.).

## Best Practices

- One primary signal per rule; secondary signals as modifiers.  
- Actions must be testable (“expand suite X”) not vague (“improve quality”).  
- Always allow override with rationale.

## Common Mistakes

- Rules that require unavailable data with no TBC path.  
- THEN clauses that prescribe Apex/LWC implementation detail.

## Interview Questions

- Why separate Rule ID from recommendation text?  
- How should program thresholds override defaults?

## Related Documents

- [Rules Engine](rules-engine.md)
- [Rule Evaluation Process](rule-evaluation-process.md)

## Navigation

- **Previous:** [rules-engine.md](rules-engine.md)
- **Next:** [rule-evaluation-process.md](rule-evaluation-process.md)

## Future Enhancements

- Severity weighting multipliers  
- Multi-condition AND/OR DSL  
