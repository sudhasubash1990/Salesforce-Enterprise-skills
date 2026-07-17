---
title: Operational Dependency Mapping
version: 0.11.1
tags: [production-support, sprint-9, operations-intelligence]
---

# Operational Dependency Mapping

## Purpose

Map runtime dependencies that amplify Salesforce production blast radius (integrations, packages, jobs, clouds, identity).

## Business Context

Many “Salesforce” incidents are dependency failures; maps speed correlation and release-risk prediction.

## Lifecycle

Inventory critical paths → Map upstream/downstream → Tag criticality → Use in correlation/prediction → Keep current after releases.

## Roles / Responsibilities

Architect owns system map; Support Lead owns ops view; Integration owners maintain interface contracts.

## Inputs

Integration inventory, batch/event chains, managed packages, Experience/Agentforce/OmniStudio touchpoints, Named Credentials, middleware.

## Outputs

Dependency map (narrative or table), criticality (Tier 0–3), failure modes, monitoring coverage gaps.

## Activities

1. List Tier 0 journeys and their tech deps.  
2. Note sync vs async paths.  
3. Identify single points of failure.  
4. Link monitors and runbooks per edge.  

## KPIs / SLAs

% of Sev1 with mapped dependency (improvement metric when tracked).

## Risks

- Stale maps after package upgrades  
- Hidden point-to-point interfaces  

## Best Practices

- Prefer simple critical-path maps over encyclopedias.  
- Update map as part of release readiness.  

## Examples

Order Submit → Flow → Platform Event → Middleware → ERP; ERP timeout → Case backlog anomaly.

## Interview Questions

- How do dependency maps change major-incident bridges?  

## References

- [../../knowledge/integration/README.md](../../knowledge/integration/README.md)
- [../salesforce/integrations.md](../salesforce/integrations.md)

## Related Documents

- [Incident Correlation](incident-correlation.md)
- [Release Risk Prediction](release-risk-prediction.md)

## Navigation

- **Previous:** [business-impact-analysis.md](business-impact-analysis.md)
- **Next:** [operational-decision-engine.md](operational-decision-engine.md)

## Future Enhancements

- Mermaid template library for common SF patterns  
