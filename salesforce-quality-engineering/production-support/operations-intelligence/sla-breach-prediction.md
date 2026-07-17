---
title: SLA Breach Prediction
version: 0.11.1
tags: [production-support, sprint-9, operations-intelligence]
---

# SLA Breach Prediction

## Purpose

Predict likelihood that open or emerging incidents will breach response/resolution SLAs.

## Business Context

Proactive breach prediction enables reassignment, escalation, and customer communication before contractual failure.

## Lifecycle

Load open tickets + clocks → Compare to SLA targets → Score breach risk → Escalate / re-prioritize → Monitor.

## Roles / Responsibilities

Service Delivery owns SLA outlook; Incident owners execute; Support Lead escalates.

## Inputs

Open incidents with severity, timestamps, SLA targets (program-provided), queue depth, assignee load.

## Outputs

Per-ticket or cohort breach risk (Low/Medium/High/Imminent) + recommended action + confidence.

**Do not invent SLA targets or attainment %.**

## Activities

1. Confirm SLA definitions (response vs resolution).  
2. Flag tickets near clock with weak progress.  
3. Correlate with capacity gaps.  
4. Recommend escalate / swarm / workaround.  

## KPIs / SLAs

Breach prediction calibration vs actual breaches (later analysis).

## Risks

- Clock-watching without restoring service  
- Wrong timezone/business-hour calendars  

## Best Practices

- Separate contractual SLA from internal OLA.  
- Communicate early when Imminent.  

## Examples

Sev2 at 80% of resolution SLA with no update in 3h → Imminent; swarm + customer status.

## Interview Questions

- How do you predict SLA breach without a tool?  

## References

- [../incident-management/sla-management.md](../incident-management/sla-management.md)
- [../service-management/slas.md](../service-management/slas.md)

## Related Documents

- [Support Capacity Planning](support-capacity-planning.md)
- [Operational Decision Engine](operational-decision-engine.md)

## Navigation

- **Previous:** [support-capacity-planning.md](support-capacity-planning.md)
- **Next:** [business-impact-analysis.md](business-impact-analysis.md)

## Future Enhancements

- Business-hour calendar overlays  
