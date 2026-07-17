---
title: Operational Recommendations Engine
version: 0.11.1
tags: [production-support, sprint-9, operations-intelligence]
---

# Operational Recommendations Engine

## Purpose

Convert operations intelligence outputs into a prioritized, owner-ready action backlog.

## Business Context

Insights without actions do not restore service or improve stability. This engine packages the “so what.”

## Lifecycle

Collect fired decisions + predictions → Deduplicate → Prioritize P0–P3 → Assign owner cues → Define success checks → Track.

## Roles / Responsibilities

Support Lead publishes backlog; owners execute; Service Delivery tracks SLA-related actions.

## Inputs

Decision IDs, health drivers, predictions, BIA, capacity gaps, available runbooks.

## Outputs

| Priority | Use |
|----------|-----|
| **P0** | Now — Sev1, security, Imminent SLA, Critical health |
| **P1** | Same day / before release |
| **P2** | Near-term stability / problem CAPA |
| **P3** | Improvement / documentation |

Standard action card:

```markdown
- **Action:** …
- **Priority:** P0–P3
- **Why (signals / Decision IDs):** …
- **Owner cue:** …
- **Runbook:** …
- **Success check:** …
- **Confidence:** Low/Medium/High
```

## Activities

1. Merge duplicate recommendations.  
2. Cap executive view at top 5.  
3. Link runbooks from [../runbooks/](../runbooks/README.md).  
4. Feed PIR / problem / change as needed.  

## KPIs / SLAs

Action completion rate; residual risk after actions—when tracked.

## Risks

- Endless P0 lists  
- Actions without success checks  

## Best Practices

- Secure & restore before optimize.  
- Prefer reversible mitigations first.  

## Examples

P0: Open MIM bridge (OPS-D-001). P1: Defer Experience deploy (OPS-D-002). P2: Problem for Flow fault cluster. P3: Update dependency map.

## Interview Questions

- How do you prioritize ops recommendations under noise?  

## References

- [Operational Decision Engine](operational-decision-engine.md)
- [../executive-reporting/README.md](../executive-reporting/README.md)

## Related Documents

- [Operations Intelligence Engine](operations-intelligence-engine.md)
- [../runbooks/README.md](../runbooks/README.md)

## Navigation

- **Previous:** [operational-decision-engine.md](operational-decision-engine.md)
- **Next:** [README.md](README.md)

## Future Enhancements

- ADO work-item export mapping for OPS actions  
