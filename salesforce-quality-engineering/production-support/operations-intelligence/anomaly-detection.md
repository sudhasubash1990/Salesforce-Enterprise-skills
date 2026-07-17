---
title: Operational Anomaly Detection
version: 0.11.1
tags: [production-support, sprint-9, operations-intelligence]
---

# Operational Anomaly Detection

## Purpose

Identify unusual production or support signals that deviate from expected baselines.

## Business Context

Early anomaly detection prevents silent degradation (e.g., rising Flow faults before customer Sev1).

## Lifecycle

Baseline → Observe → Flag anomaly → Classify (product/env/data/integration/noise) → Correlate → Act.

## Roles / Responsibilities

Monitoring owner maintains baselines; Support Lead triages anomalies; Platform validates technical causes.

## Inputs

Time-series: incidents, alert rates, job failures, API errors, login failures, page performance (as provided).

## Outputs

Anomaly list: signal, expected vs observed, severity of deviation, confidence, suggested next check.

## Activities

1. Confirm baseline window and definition.  
2. Flag spikes, drops, and new error signatures.  
3. Suppress known maintenance windows.  
4. Hand off to [incident-correlation.md](incident-correlation.md).  

## KPIs / SLAs

Track mean time to detect (MTTD) when data exists—do not invent.

## Risks

- Alert fatigue from low-value anomalies  
- Seasonal peaks misread as incidents  

## Best Practices

- Prefer relative change + absolute threshold.  
- Tag anomalies with Salesforce component (Flow, batch, API).  

## Examples

Platform Event lag 5× baseline for 45 minutes → anomaly High confidence → check subscribers + middleware.

## Interview Questions

- How do you separate anomalies from expected release spikes?  

## References

- [../monitoring/alert-management.md](../monitoring/alert-management.md)
- [../monitoring/threshold-management.md](../monitoring/threshold-management.md)

## Related Documents

- [Health Scoring](health-scoring.md)
- [Incident Correlation](incident-correlation.md)

## Navigation

- **Previous:** [health-scoring.md](health-scoring.md)
- **Next:** [incident-correlation.md](incident-correlation.md)

## Future Enhancements

- Seasonality models per industry cloud  
