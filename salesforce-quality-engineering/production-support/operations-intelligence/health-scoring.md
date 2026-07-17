---
title: Production Health Scoring
version: 0.11.1
tags: [production-support, sprint-9, operations-intelligence]
---

# Production Health Scoring

## Purpose

Compute a transparent production health score from observable Salesforce ops signals.

## Business Context

Executives need a single health narrative; ops teams need drivers behind the score.

## Lifecycle

Collect period metrics → score dimensions → weight → band → publish drivers + actions.

## Roles / Responsibilities

Support Lead owns the score narrative; Platform/Integration own technical dimension evidence.

## Inputs

Incident volume/severity, reopen, MTTR (if provided), change failure, monitoring alerts, batch/Flow fail rates, SLA attainment (if provided).

## Outputs

| Band | Indicative weighted score |
|------|---------------------------|
| **Healthy** | 4.5–5.0 |
| **Stable** | 3.5–4.4 |
| **Watch** | 2.5–3.4 |
| **Degraded** | 1.5–2.4 |
| **Critical** | ≤ 1.4 |

**Override:** Open Sev1 or security exposure → Critical/Degraded regardless of average.

### Dimension cues (1–5)

Incident pressure · Change/release stability · Monitoring noise vs signal · Integration/async health · Support responsiveness (from provided data only).

## Activities

1. Score each dimension with evidence.  
2. Apply weights (program or equal default).  
3. Apply overrides.  
4. List top 3 negative drivers.  

## KPIs / SLAs

Health score is a composite—not a contractual SLA. Link to program SLAs separately.

## Risks

- Gaming the score by closing tickets prematurely  
- Missing dependency outages outside ticket volume  

## Best Practices

- Always show dimension table beside the band.  
- Compare period-over-period only with same definitions.  

## Examples

Sev2 surge on Order API + batch failures → Integration dimension 2 → overall Watch.

## Interview Questions

- What overrides should break a “green” health score?  

## References

- [../operational-excellence/production-stability.md](../operational-excellence/production-stability.md)
- [../monitoring/README.md](../monitoring/README.md)

## Related Documents

- [Anomaly Detection](anomaly-detection.md)
- [Recommendations Engine](recommendations-engine.md)

## Navigation

- **Previous:** [operations-intelligence-engine.md](operations-intelligence-engine.md)
- **Next:** [anomaly-detection.md](anomaly-detection.md)

## Future Enhancements

- Industry-specific weight packs  
