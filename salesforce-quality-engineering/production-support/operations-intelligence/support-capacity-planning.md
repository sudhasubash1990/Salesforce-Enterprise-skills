---
title: Support Capacity Planning
version: 0.11.1
tags: [production-support, sprint-9, operations-intelligence]
---

# Support Capacity Planning

## Purpose

Assess whether support capacity matches predicted load (releases, hypercare, seasonal peaks, incident surge).

## Business Context

Understaffed bridges extend MTTR and burn out on-call; overstaffing wastes cost—planning needs evidence.

## Lifecycle

Forecast demand → Compare roster/skills → Gap analysis → Surge/backfill plan → Exit criteria.

## Roles / Responsibilities

Service Delivery / Support Lead plans capacity; Release Manager signals release load; MIM plans Sev1 bridge coverage.

## Inputs

On-call roster, skill matrix (SF admin, integration, OmniStudio, etc.), release calendar, historical ticket volume (if provided), hypercare window.

## Outputs

Capacity status (Adequate / Tight / Gap), surge recommendations, skill risks, confidence.

## Activities

1. Estimate demand bands (steady / release / hypercare / major incident).  
2. Map skills to Salesforce hotspots.  
3. Identify single-points-of-failure.  
4. Recommend surge or scope deferral.  

## KPIs / SLAs

Coverage hours, backlog aging, after-hours load—from data only.

## Risks

- Assuming “same as last release” without change-scope check  
- Ignoring vendor/package support lead times  

## Best Practices

- Plan capacity before Go/No-Go, not after Sev1.  
- Pair junior+senior for complex integrations.  

## Examples

Utilities peak + managed package upgrade + 2 on-call → Gap; add integration specialist for 72h hypercare.

## Interview Questions

- How do you capacity-plan Salesforce hypercare?  

## References

- [../hypercare/hypercare-team.md](../hypercare/hypercare-team.md)
- [../support-playbooks/on-call-playbook.md](../support-playbooks/on-call-playbook.md)

## Related Documents

- [Release Risk Prediction](release-risk-prediction.md)
- [Recommendations Engine](recommendations-engine.md)

## Navigation

- **Previous:** [release-risk-prediction.md](release-risk-prediction.md)
- **Next:** [sla-breach-prediction.md](sla-breach-prediction.md)

## Future Enhancements

- Skill-heatmap worksheet  
