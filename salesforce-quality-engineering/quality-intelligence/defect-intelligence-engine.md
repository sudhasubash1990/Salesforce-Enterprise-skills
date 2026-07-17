---
title: Defect Intelligence Engine
version: 0.9.1
tags: [quality-intelligence, sprint-7]
---

# Defect Intelligence Engine

## Purpose

Orchestrate analysis → classification → RCA → patterns → metrics → **rules engine** → prediction → prevention for Salesforce QE.

## Process

```
Ingest defect / quality signals
    ↓
Classify (type, severity, priority)
    ↓
RCA (method selection)
    ↓
Pattern detection + confidence
    ↓
Metrics & trends (no invented %)
    ↓
Quality Intelligence Rules Engine   ← actionable IF/THEN recommendations
    ↓
Predictive risk (confidence stated)
    ↓
Preventive / corrective actions (CAPA)
    ↓
Executive reporting & continuous improvement
```

## Rules Engine

Load [rules/](rules/README.md) whenever metrics, patterns, hotspots, or gates imply a decision.

Examples:

| Signal | Rule family | Action direction |
|--------|-------------|------------------|
| Leakage > threshold | QI-R-MET-001 / QI-R-REG-001 | Expand targeted regression + requirement coverage review |
| Reopens rising | QI-R-REO-001 | Defect quality, test data, fix verification |
| Flow defects dominate | QI-R-PLT-001 | Flow regression suites + automation |
| Permission defects recur | QI-R-SEC-001 | Security review (profiles, PS, sharing, FLS) |
| Prod cluster in cloud/integration | QI-R-CLD-001 / QI-R-INT-001 | Targeted regression + release readiness |

## Hard Rules

1. Prevention over detection-only advice.  
2. Never invent metric values—ask for counts or mark TBC.  
3. Cite **Rule IDs** when recommending actions from the rules engine.  
4. Reuse Sprint 5 defect/RCA templates and Sprint 6 bug guidance.  
5. Tie Salesforce hotspots to 4A/4B knowledge.  

## Related

- [Rules Engine](rules/README.md)
- [QE Brain (Sprint 1)](../brain/README.md)
- [Requirement Analysis (Sprint 2)](../knowledge/requirement-analysis.md)
- [Test Design Engine (Sprint 3)](../knowledge/test-design-engine.md)
- [Platform Foundation 4A](../knowledge/platform/README.md)
- [Enterprise Knowledge 4B](../knowledge/clouds/README.md)
- [Documentation Generator (Sprint 5)](../templates/README.md)
- [ADO Delivery Intelligence (Sprint 6)](../ado/README.md)
- [Defect Report Template](../templates/defect-report.md)
- [Defect RCA Template](../templates/defect-rca-report.md)
