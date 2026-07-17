---
title: Release Risk Prediction
version: 0.11.1
tags: [production-support, sprint-9, operations-intelligence]
---

# Release Risk Prediction

## Purpose

Predict operational risk of an upcoming Salesforce release using change scope, history, dependencies, and current health.

## Business Context

Release Managers need early Go/No-Go risk signals—not post-mortem only.

## Lifecycle

Ingest release scope → Score risk factors → Predict band + confidence → Recommend controls (surge, freeze, extra smoke).

## Roles / Responsibilities

Release Manager owns decision; Support Lead owns surge plan; QE owns validation depth advice.

## Inputs

Metadata/component change list, prior escape/incident history, open Sev defects, dependency criticality, hypercare window, current [health-scoring.md](health-scoring.md).

## Outputs

| Risk band | Meaning |
|-----------|---------|
| Low | Routine controls |
| Medium | Extra smoke + monitoring |
| High | Surge staff / scope cut / defer candidates |
| Critical | Recommend No-Go or executive waiver |

Always state **confidence** and missing evidence.

## Activities

1. Map changes to hotspots (Flow, Apex, sharing, integrations).  
2. Check current health + open Sev.  
3. Apply dependency blast radius.  
4. Output risk + mitigations via recommendations engine.  

## KPIs / SLAs

Track prediction-vs-outcome later (calibration)—do not invent accuracy %.

## Risks

- Over-predicting risk causing release paralysis  
- Under-predicting when history data is thin  

## Best Practices

- Cross-link Sprint 7 predictive quality and Sprint 8 CI readiness.  
- Prefer targeted regression over blanket freeze.  

## Examples

Permission-set + Experience Cloud sharing changes while health=Watch → High release risk; mandate persona smoke + sharing review.

## Interview Questions

- What signals raise Salesforce release risk most?  

## References

- [../release-operations/release-readiness.md](../release-operations/release-readiness.md)
- [../../quality-intelligence/predictive-quality/release-readiness-risks.md](../../quality-intelligence/predictive-quality/release-readiness-risks.md)

## Related Documents

- [SLA Breach Prediction](sla-breach-prediction.md)
- [Operational Decision Engine](operational-decision-engine.md)

## Navigation

- **Previous:** [incident-correlation.md](incident-correlation.md)
- **Next:** [support-capacity-planning.md](support-capacity-planning.md)

## Future Enhancements

- Release-risk scorecard template export  
