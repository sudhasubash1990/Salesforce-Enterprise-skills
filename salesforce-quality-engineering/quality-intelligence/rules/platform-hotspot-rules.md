---
title: Platform Hotspot Rules
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

# Platform Hotspot Rules

## Purpose

When Salesforce platform areas dominate defects, trigger targeted suites, automation, and knowledge loading—not generic “more testing.”

## Business Context

Salesforce failures cluster by metadata type (Flow, Apex, validation, Lightning, OmniStudio, etc.). Hotspot-aware recommendations improve ROI.

## Overview

“Dominate” = largest share of new defects in period, or clear cluster with Medium+ pattern confidence. Load matching 4A/4B knowledge when firing.

## Inputs

Defect tags by component type; counts; release context.

## Outputs

Fired `QI-R-PLT-*` actions.

## Process

---

### QI-R-PLT-001 — Flow-Related Defects Dominate

| Field | Content |
|-------|---------|
| **IF** | Flow-tagged defects are the plurality/majority **or** Flow share ≥ indicative share |
| **Indicative default** | ≥ 30% of new defects in period **or** top tag = Flow |
| **THEN** | 1) Build/expand **targeted Flow regression suites** (before/after save, entry criteria, fault paths) 2) Recommend **automation** for stable, high-value Flow paths 3) Review Flow versioning/activation/test coverage in sandbox 4) Load Flow platform knowledge (4A) |
| **Priority** | P1 |
| **Related** | [salesforce-quality-intelligence](../knowledge-base/salesforce-quality-intelligence.md), knowledge/automation (Flows) |

---

### QI-R-PLT-002 — Apex-Related Defects Dominate

| Field | Content |
|-------|---------|
| **IF** | Apex/trigger/class defects dominate |
| **Indicative default** | ≥ 30% or top tag = Apex |
| **THEN** | 1) Targeted Apex regression (bulk, governor, recursion, sharing) 2) Strengthen unit/integration test expectations with Dev 3) Add negative/permission paths where Apex enforces rules 4) Load Apex 4A knowledge |
| **Priority** | P1 |

---

### QI-R-PLT-003 — Validation Rule / Config Defects Dominate

| Field | Content |
|-------|---------|
| **IF** | Validation rules, required fields, record types, page layout defects dominate |
| **THEN** | 1) Config matrix regression (record type × profile × layout) 2) Pair with BA on rule clarity 3) Add data-negative scenarios |
| **Priority** | P1–P2 |

---

### QI-R-PLT-004 — Lightning Page / UI Defects Dominate

| Field | Content |
|-------|---------|
| **IF** | Lightning page / LWC UI defects dominate |
| **THEN** | 1) UI smoke + persona layout checks 2) Cross-browser only if in scope 3) Automation candidates for critical UI paths once stable |
| **Priority** | P2 |

---

### QI-R-PLT-005 — OmniStudio / Industry Cloud Defects Dominate

| Field | Content |
|-------|---------|
| **IF** | OmniStudio or Industry Cloud tagged defects dominate |
| **THEN** | 1) Journey-level regression for affected OmniScripts/FlexCards/IP 2) Data mapper / integration procedure negative paths 3) Load 4B cloud/OmniStudio articles |
| **Priority** | P1 |

---

### QI-R-PLT-006 — Batch / Platform Event Defects Dominate

| Field | Content |
|-------|---------|
| **IF** | Batch jobs or Platform Events dominate failures |
| **THEN** | 1) Volume/idempotency/retry scenarios 2) Monitoring and replay checks 3) Integration-aware regression |
| **Priority** | P1 |

## Examples

12 of 28 sprint defects tagged Flow → QI-R-PLT-001: Flow suite + automate Order Submit happy path + fault connector path.

## Best Practices

- Confirm tagging quality before declaring dominance.  
- Prefer suite expansion over “test everything.”

## Common Mistakes

- Automating unstable Flow paths immediately.  
- Ignoring activation/version mismatch as root of “Flow bugs.”

## Interview Questions

- What do you recommend when Flow defects dominate?  
- How do you define “dominate” without perfect taxonomy?

## Related Documents

- [Security Permission Rules](security-permission-rules.md)
- [Integration and Cloud Cluster Rules](integration-and-cloud-cluster-rules.md)

## Navigation

- **Previous:** [reopen-and-defect-quality-rules.md](reopen-and-defect-quality-rules.md)
- **Next:** [security-permission-rules.md](security-permission-rules.md)

## Future Enhancements

- Hotspot share calculator worksheet  
