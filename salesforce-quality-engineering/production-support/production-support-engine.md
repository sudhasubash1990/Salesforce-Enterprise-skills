---
title: Production Support Engine
version: 0.11.1
tags: [production-support, sprint-9]
---

# Production Support & Operational Excellence Engine

## Purpose

Orchestrate go-live → hypercare → incident/problem/change → release ops → monitoring → **operations intelligence** → service improvement for Salesforce production.

## Process

```
Go-Live readiness & Go/No-Go
    ↓
Deploy + production validation
    ↓
Hypercare (stabilize)
    ↓
Steady-state: Incident / Request / Change / Release
    ↓
Problem management + known errors
    ↓
Monitoring & operational analytics
    ↓
Operations Intelligence (health, anomalies, predictions, decisions, recommendations)
    ↓
Executive reporting + continual improvement
```

## Hard rules

1. Restore service first for Sev1; deep RCA after stabilization (reuse Sprint 7 methods).  
2. Never invent SLA, MTTR, MTBF, or KPI values—ask or mark TBC.  
3. Prefer runbooks; update them after major events.  
4. Emergency change ≠ no documentation.  
5. Cross-link 4A/4B for Salesforce component troubleshooting.  
6. Operations Intelligence predictions must state confidence; Security/Sev1 overrides health greens.  

## Capabilities

| Capability | Path |
|------------|------|
| Production Intelligence | [salesforce/](salesforce/README.md) |
| Incident Intelligence | [incident-management/](incident-management/README.md) |
| Operational Excellence | [operational-excellence/](operational-excellence/README.md) |
| ITIL Awareness | [service-management/](service-management/README.md) |
| Release Operations | [release-operations/](release-operations/README.md) |
| Support Analytics | [operational-analytics/](operational-analytics/README.md) |
| Monitoring Intelligence | [monitoring/](monitoring/README.md) |
| Runbook Intelligence | [runbooks/](runbooks/README.md) |
| **Operations Intelligence** | [operations-intelligence/](operations-intelligence/README.md) |

## Related

- [QE Brain (Sprint 1)](../brain/README.md)
- [Requirement Analysis (Sprint 2)](../knowledge/requirement-analysis.md)
- [Test Design Engine (Sprint 3)](../knowledge/test-design-engine.md)
- [Platform Foundation 4A](../knowledge/platform/README.md)
- [Enterprise Knowledge 4B](../knowledge/clouds/README.md)
- [Documentation Generator (Sprint 5)](../templates/README.md)
- [ADO Delivery Intelligence (Sprint 6)](../ado/README.md)
- [Defect Intelligence (Sprint 7)](../quality-intelligence/README.md)
- [Automation Intelligence (Sprint 8)](../automation-intelligence/README.md)
- [Operations Intelligence Engine](operations-intelligence/operations-intelligence-engine.md)
