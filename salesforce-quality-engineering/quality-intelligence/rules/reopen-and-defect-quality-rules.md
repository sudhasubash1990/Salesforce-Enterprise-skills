---
title: Reopen and Defect Quality Rules
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

# Reopen and Defect Quality Rules

## Purpose

Detect when rising reopens signal weak defect quality, weak fixes, or weak verification—and prescribe process corrections.

## Business Context

Reopens burn sprint capacity and hide systemic issues in triage, test data, environments, and fix verification.

## Overview

Focus on reopen rate, reopen trend, and defect description quality—not blame.

## Inputs

Reopen counts, reopen rate, sample reopened defects, verification evidence.

## Outputs

Fired `QI-R-REO-*` / `QI-R-DFQ-*` recommendations.

## Process

---

### QI-R-REO-001 — Reopened Defects Increasing

| Field | Content |
|-------|---------|
| **IF** | Reopened defect count or Reopen Rate increases vs prior period |
| **Indicative default** | Reopen Rate > 10% **or** rising 2 consecutive sprints |
| **THEN** | 1) Analyze **defect quality** (repro steps, expected vs actual, evidence) 2) Analyze **test data quality** used in fix verification 3) Review **fix verification practices** (who verifies, in which org, with which personas) 4) Sample reopens for RCA theme (incomplete fix vs wrong environment vs duplicate) |
| **Follow-on** | CAPA if systemic; coach triage checklist |
| **Priority** | P1 |
| **Escalate when** | Same Sev1 reopens twice or customer-facing production reopen |
| **Related** | [reopen-rate](../quality-metrics/reopen-rate.md), [ado/governance/bug-workflow](../../ado/governance/bug-workflow.md) |

---

### QI-R-DFQ-001 — Poor Defect Report Quality Pattern

| Field | Content |
|-------|---------|
| **IF** | Recurring defects lack steps, data, persona, or expected result (pattern confidence Medium+) |
| **THEN** | 1) Enforce defect template minimum fields 2) Reject/return incomplete bugs at triage 3) Short KT on defect writing for squad |
| **Priority** | P2 |
| **Related** | [templates/defect-report.md](../../templates/defect-report.md) |

---

### QI-R-REO-002 — Fix Verified Without Matching Persona/Data

| Field | Content |
|-------|---------|
| **IF** | Reopens show verification done with wrong profile, incomplete data, or wrong sandbox tier |
| **THEN** | 1) Mandate persona + data checklist on resolve 2) Align verification org with defect origin tier where possible 3) Add permission/data negative paths to verification |
| **Priority** | P1 |

## Examples

Reopen rate 16% (was 6%) → QI-R-REO-001: audit last 10 reopens for incomplete AC, wrong test user, and “fixed in wrong sandbox.”

## Best Practices

- Separate product reopen from environment-induced false fail.  
- Improve templates before adding more testers.

## Common Mistakes

- Closing defects on unit-test-only evidence for UI/persona bugs.  
- Treating every reopen as developer failure.

## Interview Questions

- What three areas do you inspect when reopens rise?  
- How does defect quality affect reopen rate?

## Related Documents

- [Metric Threshold Rules](metric-threshold-rules.md)
- [Continuous Improvement — CAPA](../continuous-improvement/capa.md)

## Navigation

- **Previous:** [metric-threshold-rules.md](metric-threshold-rules.md)
- **Next:** [platform-hotspot-rules.md](platform-hotspot-rules.md)

## Future Enhancements

- Reopen taxonomy codes for automation of themes  
