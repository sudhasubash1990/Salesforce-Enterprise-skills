---
title: Operational Decision Engine
version: 0.11.1
tags: [production-support, sprint-9, operations-intelligence]
---

# Operational Decision Engine

## Purpose

Apply reusable IF/THEN operational rules so recommendations are consistent, explainable, and prioritized.

## Business Context

Ops leaders make repeatable calls (declare MIM, defer release, surge staff). Encoding them reduces tribal knowledge risk.

## Lifecycle

Evaluate signals → Fire rules → Merge decisions → Sequence with recommendations engine.

## Roles / Responsibilities

Support Lead applies rules; Release Manager owns release decisions; Executives own waivers.

## Inputs

Health band, anomalies, correlations, release risk, SLA risk, capacity status, business impact.

## Outputs

Fired decision IDs + actions + urgency.

### Example decision rules

| ID | IF | THEN |
|----|----|------|
| OPS-D-001 | Health = Critical **or** open Sev1 | Declare/confirm major incident bridge; freeze non-critical changes |
| OPS-D-002 | Release risk = High/Critical **and** health ≤ Watch | Recommend defer or cut scope; require executive Go |
| OPS-D-003 | SLA breach Imminent on Sev1/Sev2 | Swarm + escalate + customer comms |
| OPS-D-004 | Capacity = Gap during hypercare/release | Add surge or delay release |
| OPS-D-005 | Correlated cluster ≥ N incidents on one dependency | Open problem; targeted monitoring; consider known error |
| OPS-D-006 | Security/permission anomaly with data exposure risk | Secure path first; engage Security; restrict change |

Prefer program thresholds for N; else state indicative default (e.g., N=5) as assumption.

## Activities

1. Score/predict modules first.  
2. Evaluate rules; cite IDs in output.  
3. Hand actions to [recommendations-engine.md](recommendations-engine.md).  

## KPIs / SLAs

Decision latency (time from signal to action)—qualitative if unmeasured.

## Risks

- Rule spam without merge  
- Ignoring human override with rationale  

## Best Practices

- Always allow documented override.  
- Align with Sprint 7 QI rules when defect/leakage signals dominate.  

## Examples

OPS-D-002 + OPS-D-004 fire → defer package upgrade 24h; surge integration on-call.

## Interview Questions

- Give an IF/THEN rule you use before Salesforce go-live.  

## References

- [../../quality-intelligence/rules/README.md](../../quality-intelligence/rules/README.md)
- [../support-playbooks/major-incident-playbook.md](../support-playbooks/major-incident-playbook.md)

## Related Documents

- [Recommendations Engine](recommendations-engine.md)
- [Health Scoring](health-scoring.md)

## Navigation

- **Previous:** [dependency-mapping.md](dependency-mapping.md)
- **Next:** [recommendations-engine.md](recommendations-engine.md)

## Future Enhancements

- Expand rule catalog with program overlays  
