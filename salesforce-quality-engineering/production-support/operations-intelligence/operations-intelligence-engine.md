---
title: Operations Intelligence Engine
module: Salesforce Quality Engineering
category: Production Support
document_type: Guide
version: 0.11.1
tags: [production-support, sprint-9, operations-intelligence]
---

# Operations Intelligence Engine

## Purpose

Orchestrate health scoring → anomaly/correlation → prediction → capacity/impact → decisions → recommendations for Salesforce production operations.

## Business Context

Experienced ops leaders do not wait for Sev1 tickets alone—they read weak signals, correlate noise, and act before SLA and business impact worsen. This engine encodes that judgment transparently.

## Overview

```
Ingest ops signals (monitor + tickets + releases + capacity)
    ↓
Health scoring
    ↓
Anomaly detection + incident correlation
    ↓
Predict release risk & SLA breach (confidence stated)
    ↓
Business impact + dependency context
    ↓
Support capacity check
    ↓
Operational decision engine
    ↓
Recommendations engine (P0–P3)
```

## Lifecycle

Detect → Score → Correlate → Predict → Decide → Recommend → Feed PIR / problem / change.

## Roles / Responsibilities

| Role | Responsibility |
|------|----------------|
| Production Support Lead | Own health narrative and recommendations |
| Release Manager | Act on release-risk predictions |
| MIM / Incident Manager | Use correlation during bridges |
| Service Delivery | Capacity and SLA breach outlook |
| QE / Platform | Validate technical dependency risks |

## Inputs / Outputs

**Inputs:** monitoring, incidents, changes, releases, roster, dependencies, SLA targets.  
**Outputs:** scorecard, predictions with confidence, decision log, prioritized recommendations.

## Activities

1. Load [health-scoring.md](health-scoring.md) and score current period.  
2. Run [anomaly-detection.md](anomaly-detection.md) + [incident-correlation.md](incident-correlation.md).  
3. Predict via [release-risk-prediction.md](release-risk-prediction.md) and [sla-breach-prediction.md](sla-breach-prediction.md).  
4. Frame impact and deps; check capacity.  
5. Apply [operational-decision-engine.md](operational-decision-engine.md).  
6. Publish actions via [recommendations-engine.md](recommendations-engine.md).  

## KPIs / SLAs

Use program baselines only. Never invent health %, breach probability, or MTTR.

## Risks

- Alert fatigue from uncorrelated anomalies  
- False confidence from thin data  
- Recommendations without owners or success checks  

## Best Practices

- State confidence Low/Medium/High.  
- Prefer stabilize-now over deep analysis during Sev1.  
- Cross-link Sprint 7 predictive quality and QI rules when defect leakage signals appear.  

## Examples

Rising Flow failures + shared integration dependency + thin on-call → Health Fair, Release Risk High, recommend defer non-critical deploy + surge staffing.

## Interview Questions

- How does operations intelligence differ from raw monitoring?  
- When do you escalate a prediction vs wait for a ticket?  

## References

- ITIL 4 continual improvement / monitoring & event management themes  
- Salesforce Well-Architected (reliable)  
- Sprint 7 Defect Intelligence predictive patterns  

## Related Documents

- [README.md](README.md)
- [../production-support-engine.md](../production-support-engine.md)
- [../../quality-intelligence/predictive-quality/README.md](../../quality-intelligence/predictive-quality/README.md)

## Navigation

- **Previous:** [README.md](README.md)
- **Next:** [health-scoring.md](health-scoring.md)

## Future Enhancements

- Program threshold overlay JSON  
- Optional CMDB sync later  
