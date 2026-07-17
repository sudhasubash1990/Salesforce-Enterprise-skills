---
title: Metric Threshold Rules
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

# Metric Threshold Rules

## Purpose

Map quality metric breaches to concrete QE actions.

## Business Context

Metrics alone do not improve quality; breached thresholds must drive scope, coverage, and process changes.

## Overview

Indicative defaults below are **not** universal SLAs. Prefer program thresholds. Formulas: [quality-metrics/](../quality-metrics/README.md).

## Inputs

Metric values, period, denominator definitions, program thresholds (optional).

## Outputs

Fired `QI-R-MET-*` rules + actions.

## Process

Evaluate each rule when evidence exists; mark TBC otherwise.

---

### QI-R-MET-001 — Elevated Defect Leakage

| Field | Content |
|-------|---------|
| **IF** | Defect Leakage > threshold |
| **Indicative default** | > 10% (or rising 2 consecutive releases) |
| **THEN** | 1) Expand regression scope for escaped modules/journeys 2) Review requirement & scenario coverage for escape cohort 3) Add escape defects to RCA backlog 4) Re-check entry/exit gates for test completeness |
| **Follow-on** | [production-leakage](../defect-patterns/production-leakage.md), requirement coverage metric |
| **Priority** | P1 (P0 if Sev1/Sev2 in production) |
| **Escalate when** | Leakage involves security/compliance or customer-impacting Sev1 |
| **Do not fire if** | Denominator unclear / leakage formula inconsistent—ask to clarify first |

---

### QI-R-MET-002 — Low Defect Removal Efficiency (DRE)

| Field | Content |
|-------|---------|
| **IF** | DRE < threshold |
| **Indicative default** | < 85% (program-set) |
| **THEN** | 1) Strengthen earlier test levels (shift-left static review + SIT depth) 2) Review escaped defect types for missed techniques 3) Increase risk-based exploratory on high-risk stories |
| **Priority** | P1 |
| **Related** | [defect-removal-efficiency](../quality-metrics/defect-removal-efficiency.md) |

---

### QI-R-MET-003 — High Fail Rate / Low Pass Rate

| Field | Content |
|-------|---------|
| **IF** | Fail Rate > threshold **or** Pass Rate < threshold (same suite/period) |
| **Indicative default** | Fail > 15% or Pass < 85% for planned execution (excluding blocked) |
| **THEN** | 1) Triage fails: product vs env vs data vs automation 2) Stabilize environment/data before expanding scope 3) Pause vanity “% complete” reporting until classification done |
| **Priority** | P1 |
| **Do not fire if** | Majority fails are blocked/env—route to environment rules instead |

---

### QI-R-MET-004 — High Defect Density (Hot Module)

| Field | Content |
|-------|---------|
| **IF** | Defect Density for a module/component > peer average or threshold |
| **Indicative default** | Top quartile vs release peers **or** > program density target |
| **THEN** | 1) Declare module hotspot 2) Targeted regression + design/config review 3) Consider additional peer review / unit test expectations with Dev |
| **Priority** | P1 |
| **Related** | [module-hotspots](../defect-patterns/module-hotspots.md) |

---

### QI-R-MET-005 — Rising Escaped Defects

| Field | Content |
|-------|---------|
| **IF** | Escaped defect count increases vs prior release/sprint |
| **Indicative default** | +1 Sev1/Sev2 **or** +20% escaped count |
| **THEN** | Same family as QI-R-MET-001; add release-readiness deep dive |
| **Priority** | P0–P1 |
| **Related** | [escaped-defects](../quality-metrics/escaped-defects.md) |

---

### QI-R-MET-006 — Weak Requirement Coverage Signal

| Field | Content |
|-------|---------|
| **IF** | Requirement Coverage < threshold **or** RTM gaps for in-scope stories |
| **Indicative default** | Coverage < 100% for Must/Should scope **or** open RTM gaps |
| **THEN** | 1) Close RTM gaps before execution claim 2) Block “done” for uncovered Must stories at gate 3) Pair with BA on AC clarity where gaps stem from ambiguity |
| **Priority** | P1 |
| **Related** | Sprint 2 Requirement Analysis, Sprint 5 RTM |

## Examples

Leakage 18%, threshold 10% → fire QI-R-MET-001; recommend expanded regression + coverage review for Account sync escape path.

## Best Practices

- Always state formula period and threshold source.  
- Pair metric rules with pattern/hotspot rules for sharper actions.

## Common Mistakes

- Using pass rate including blocked cases.  
- Comparing density across unequal module sizes without normalization note.

## Interview Questions

- What actions follow a leakage breach?  
- How do DRE and leakage relate in release decisions?

## Related Documents

- [Regression and Coverage Rules](regression-and-coverage-rules.md)
- [Release Gate Rules](release-gate-rules.md)

## Navigation

- **Previous:** [rule-evaluation-process.md](rule-evaluation-process.md)
- **Next:** [reopen-and-defect-quality-rules.md](reopen-and-defect-quality-rules.md)

## Future Enhancements

- Program threshold overlay examples  
