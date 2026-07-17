---
title: Incident Correlation
version: 0.11.1
tags: [production-support, sprint-9, operations-intelligence]
---

# Incident Correlation

## Purpose

Link related incidents, alerts, and changes into a single operational story (probable common cause or blast radius).

## Business Context

Uncorrelated tickets waste bridge time; correlation accelerates major-incident containment and problem creation.

## Lifecycle

Ingest tickets/alerts → Match keys (time, component, error signature, change window) → Cluster → Nominate parent incident/problem → Communicate.

## Roles / Responsibilities

MIM owns correlation during Sev1; Problem Manager owns lasting clusters.

## Inputs

Incident titles/symptoms, timestamps, affected objects/integrations, recent changes/releases, monitoring signatures.

## Outputs

Correlation clusters, confidence, suggested parent ticket, related changes, blast-radius note.

## Activities

1. Group by time proximity + same dependency ([dependency-mapping.md](dependency-mapping.md)).  
2. Check recent releases/changes.  
3. Merge duplicates; keep evidence links.  
4. Open/update problem if recurring.  

## KPIs / SLAs

Duplicate rate reduction; time-to-cluster (qualitative if no data).

## Risks

- Over-merging unrelated issues  
- Missing multi-cloud fan-out  

## Best Practices

- Prefer “probable correlation” language with confidence.  
- Never hide distinct Sev1 customer impacts inside one vague ticket.  

## Examples

12 “Case save failed” tickets within 20 minutes after Flow deploy → correlate to Flow version + shared validation rule.

## Interview Questions

- What keys do you use to correlate Salesforce incidents?  

## References

- [../incident-management/major-incidents.md](../incident-management/major-incidents.md)
- [../problem-management/problem-identification.md](../problem-management/problem-identification.md)

## Related Documents

- [Anomaly Detection](anomaly-detection.md)
- [Dependency Mapping](dependency-mapping.md)

## Navigation

- **Previous:** [anomaly-detection.md](anomaly-detection.md)
- **Next:** [release-risk-prediction.md](release-risk-prediction.md)

## Future Enhancements

- Auto-suggest parent/child ADO links  
