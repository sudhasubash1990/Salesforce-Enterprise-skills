---
title: Security Permission Rules
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

# Security Permission Rules

## Purpose

When permission-related defects recur, trigger a structured security review—not ad-hoc profile tweaks.

## Business Context

Access defects often escape functional happy-path testing. Recurrence indicates systemic gaps in profiles, permission sets, sharing, and FLS coverage.

## Overview

Applies to CRUD/FLS, sharing, permission sets, profiles, role hierarchy symptoms tagged security/permission.

## Inputs

Permission-tagged defects, personas affected, objects/fields involved.

## Outputs

Fired `QI-R-SEC-*` recommendations.

## Process

---

### QI-R-SEC-001 — Permission-Related Defects Recur

| Field | Content |
|-------|---------|
| **IF** | Permission/security defects recur across stories/sprints **or** pattern confidence Medium+ |
| **Indicative default** | ≥ 3 related defects in a release **or** ≥ 15% of defects tagged permission/security |
| **THEN** | 1) **Trigger security review** of profiles, permission sets, sharing rules, and field-level security for impacted objects 2) Build persona × object CRUD/FLS matrix tests 3) Add negative access scenarios to regression 4) Load [security-model](../../knowledge/security/README.md) / 4A security articles 5) Align with BA on persona definitions |
| **Priority** | P0–P1 (P0 if production data exposure risk) |
| **Escalate when** | Suspected over-access, data leakage, or compliance-impacting exposure—engage Security/Architecture |
| **Do not fire if** | Single one-off misconfiguration already fixed with verified CAPA—treat as closed unless recurrence |
| **Related** | [security-weaknesses](../defect-patterns/security-weaknesses.md) |

---

### QI-R-SEC-002 — Sharing Rule / Visibility Cluster

| Field | Content |
|-------|---------|
| **IF** | Defects cluster on “cannot see record” / “sees too much” |
| **THEN** | 1) Review OWD, sharing rules, manual shares, queues 2) Persona visibility scenarios in target sandbox 3) Document expected visibility rules with BA/Arch |
| **Priority** | P1 |

---

### QI-R-SEC-003 — Permission Set Drift After Deploy

| Field | Content |
|-------|---------|
| **IF** | Access defects appear immediately post-deploy / package upgrade |
| **THEN** | 1) Diff permission sets/profiles in release contents 2) Add permission deploy checklist to release readiness 3) Smoke critical personas post-deploy |
| **Priority** | P1 |
| **Related** | [release-gate-rules.md](release-gate-rules.md) |

## Examples

Four “Agent cannot edit Case.Status” defects across two sprints → QI-R-SEC-001: security review of Service Agent PS + FLS on Case + sharing for Case teams.

## Best Practices

- Test least-privilege and over-access, not only “can do happy path.”  
- Prefer permission sets over profile edits where program standard allows.

## Common Mistakes

- Fixing with “Modify All” to unblock testing.  
- Skipping persona matrix because “Admin works.”

## Interview Questions

- What review do you trigger when permission defects recur?  
- How do you test sharing without production data?

## Related Documents

- [Platform Hotspot Rules](platform-hotspot-rules.md)
- [../knowledge-base/salesforce-quality-intelligence.md](../knowledge-base/salesforce-quality-intelligence.md)

## Navigation

- **Previous:** [platform-hotspot-rules.md](platform-hotspot-rules.md)
- **Next:** [integration-and-cloud-cluster-rules.md](integration-and-cloud-cluster-rules.md)

## Future Enhancements

- Persona matrix template link pack  
