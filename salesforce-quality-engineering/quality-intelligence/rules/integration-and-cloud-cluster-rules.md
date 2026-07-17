---
title: Integration and Cloud Cluster Rules
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

# Integration and Cloud Cluster Rules

## Purpose

When production (or late-stage) defects cluster in a Salesforce cloud or integration, prioritize **targeted regression** and **release readiness** for that area.

## Business Context

Enterprise Salesforce value often fails at boundaries—Service Cloud + middleware, Experience Cloud identity, Utilities integrations. Cluster response must be focused and gate-aware.

## Overview

Clustering = same cloud, package, API, or event family appearing repeatedly in production or UAT/SIT escapes.

## Inputs

Production/UAT defect tags (cloud, integration name), severity, volume, release map.

## Outputs

Fired `QI-R-INT-*` / `QI-R-CLD-*` recommendations.

## Process

---

### QI-R-CLD-001 — Production Defects Cluster in a Salesforce Cloud

| Field | Content |
|-------|---------|
| **IF** | Production defects cluster in one Salesforce Cloud (e.g., Service, Sales, Experience, Utilities) |
| **Indicative default** | ≥ 3 prod defects in same cloud in window **or** majority of Sev1/Sev2 in one cloud |
| **THEN** | 1) Prioritize **targeted regression** for that cloud’s critical journeys 2) Elevate **release readiness checks** for that cloud (config, permissions, integrations, data) 3) Load matching 4B cloud article 4) Add cloud-specific smoke to production validation 5) Consider temporary feature freeze on high-risk changes in that cloud |
| **Priority** | P0–P1 |
| **Escalate when** | Sev1 ongoing or regulatory impact |
| **Related** | [knowledge/clouds/](../../knowledge/clouds/README.md), predictive release readiness |

---

### QI-R-INT-001 — Production Defects Cluster in an Integration

| Field | Content |
|-------|---------|
| **IF** | Production defects cluster on an integration (API, event, middleware, MuleSoft, etc.) |
| **Indicative default** | ≥ 3 related integration defects **or** repeated timeout/mapping/auth failures |
| **THEN** | 1) Targeted integration regression (auth, mapping, retry, idempotency, failure handling) 2) Release readiness: contract version, named credentials, connected apps, monitoring alerts 3) Coordinate with Integration/Architecture owners 4) Load 4B integration knowledge 5) Add post-deploy integration smoke |
| **Priority** | P0–P1 |
| **Related** | [integration-failures](../defect-patterns/integration-failures.md) |

---

### QI-R-INT-002 — Sync / Dual-Write Inconsistency Cluster

| Field | Content |
|-------|---------|
| **IF** | Defects show Salesforce vs external system data mismatch cluster |
| **THEN** | 1) Reconciliation test pack 2) Ordering/race scenarios 3) Monitoring & replay validation in readiness |
| **Priority** | P1 |

---

### QI-R-CLD-002 — Experience Cloud Access Cluster

| Field | Content |
|-------|---------|
| **IF** | Experience Cloud login/visibility/sharing defects cluster |
| **THEN** | 1) Guest vs authenticated persona matrix 2) Sharing sets / network access review 3) Targeted Experience regression + readiness |
| **Priority** | P1 |

## Examples

Five production incidents on Order API timeout/mapping → QI-R-INT-001: expand Order API regression, verify named credential rotation in readiness, add synthetic probe post-deploy.

## Best Practices

- Name the integration/cloud explicitly in recommendations.  
- Pair with leakage rules when escapes originate from that area.

## Common Mistakes

- Broad “full regression” when a contract/auth fix is the real need.  
- Skipping monitoring/readiness for “functional-only” retests.

## Interview Questions

- What do you prioritize when prod defects cluster in one cloud?  
- How do integration clusters change release readiness?

## Related Documents

- [Release Gate Rules](release-gate-rules.md)
- [Security Permission Rules](security-permission-rules.md)

## Navigation

- **Previous:** [security-permission-rules.md](security-permission-rules.md)
- **Next:** [automation-stability-rules.md](automation-stability-rules.md)

## Future Enhancements

- Cloud×integration risk heat-map template  
