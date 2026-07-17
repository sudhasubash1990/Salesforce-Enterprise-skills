---
title: Enterprise Quality Advisory Engine
version: 0.12.1
tags: [enterprise-quality, sprint-10]
---

# Enterprise Quality Advisory Engine

## Purpose

Synthesize Sprints 1–9 into executive-grade assessments and decisions for Salesforce programs and portfolios. Invoked by the **[Enterprise Orchestrator](../enterprise-orchestrator/enterprise-orchestrator.md)** when advisory / portfolio / maturity / release-decision intent is classified—not as a replacement for deep operational engines.

## Process

```
(Upstream) Enterprise Orchestrator routes request + gathers Sprint 2–9 evidence
    ↓
Ingest evidence (project / portfolio / architecture / ops / AI / compliance)
    ↓
Assess maturity + project/portfolio health
    ↓
Architecture / AI / compliance / audit lenses
    ↓
Capability model + benchmarks (generic)
    ↓
Decision engine (Proceed/Hold/Escalate/…)
    ↓
Recommendation engine (prioritized)
    ↓
Executive dashboards / roadmaps / Executive Recommendations
```

## Hard rules

1. **Never invent** maturity scores, KPI %, DORA numbers, or compliance attestations.  
2. Regulations = overview / TBC with Legal-Compliance unless cited.  
3. Reuse Sprint 7 QI, Sprint 8 automation review, Sprint 9 ops intelligence—do not duplicate.  
4. Always state confidence and residual risk.  
5. Align with ISTQB ATM, TMMi, Well-Architected, ITIL 4, DORA concepts, TOGAF governance themes, Responsible AI.  
6. On Sev1 / active outage, Orchestrator must complete Sprint 9 triage before this engine.  

## Capabilities

| Capability | Path |
|------------|------|
| Enterprise Advisory | [README.md](README.md) |
| Executive Decision Support | [decision-engine/](decision-engine/README.md) |
| Quality Maturity Assessment | [quality-maturity/](quality-maturity/README.md) |
| Portfolio Intelligence | [portfolio-management/](portfolio-management/README.md) |
| Architecture Quality Assessment | [architecture-quality/](architecture-quality/README.md) |
| AI Governance | [ai-governance/](ai-governance/README.md) |
| Compliance Awareness | [compliance/](compliance/README.md) |
| Capability Assessment | [capability-model/](capability-model/README.md) |
| Strategic Recommendation Engine | [recommendation-engine/](recommendation-engine/README.md) |

## Related

- [Enterprise Orchestrator](../enterprise-orchestrator/README.md)
- [QE Brain (Sprint 1)](../brain/README.md)
- [Requirement Analysis (Sprint 2)](../knowledge/requirement-analysis.md)
- [Test Design Engine (Sprint 3)](../knowledge/test-design-engine.md)
- [Platform Foundation 4A](../knowledge/platform/README.md)
- [Enterprise Knowledge 4B](../knowledge/clouds/README.md)
- [Documentation Generator (Sprint 5)](../templates/README.md)
- [ADO Delivery Intelligence (Sprint 6)](../ado/README.md)
- [Defect Intelligence (Sprint 7)](../quality-intelligence/README.md)
- [Automation Intelligence (Sprint 8)](../automation-intelligence/README.md)
- [Production Support (Sprint 9)](../production-support/README.md)
