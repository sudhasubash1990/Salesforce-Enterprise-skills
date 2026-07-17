---
title: Operations Intelligence Engine — README
module: Salesforce Quality Engineering
category: Production Support
document_type: Guide
version: 0.11.1
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-18
last_updated: 2026-07-18
tags: [production-support, sprint-9, operations-intelligence]
---

# Operations Intelligence Engine

## Purpose

Turn production signals (incidents, monitoring, releases, capacity, SLAs) into **scored health, predicted risks, correlated insights, and actionable recommendations**—so the AI advises like an experienced Operations / Service Delivery Lead, not only a ticket logger.

## Scope

**In scope:** Health scoring, anomaly detection, incident correlation, release-risk prediction, support capacity planning, SLA-breach prediction, business-impact analysis, dependency mapping, operational decision engine, recommendations engine.

**Out of scope:** Inventing metric/SLA values; replacing monitoring tools; full Apex remediation.

## Inputs

- Incident/problem/change history (sanitized)
- Monitoring alerts and thresholds
- Release calendar and change risk notes
- Support roster / capacity signals
- Dependency maps (integrations, batches, clouds)
- Program SLA targets (or TBC)

## Outputs

- Health score + drivers
- Anomalies and correlations
- Predicted risks (release / SLA) with confidence
- Capacity and impact assessments
- Prioritized operational recommendations

## Available Documents

| Document | Focus |
|----------|-------|
| [Operations Intelligence Engine](operations-intelligence-engine.md) | Orchestration |
| [Health Scoring](health-scoring.md) | Production health score model |
| [Anomaly Detection](anomaly-detection.md) | Unusual ops signals |
| [Incident Correlation](incident-correlation.md) | Link related incidents |
| [Release Risk Prediction](release-risk-prediction.md) | Pre-release risk |
| [Support Capacity Planning](support-capacity-planning.md) | Capacity & surge planning |
| [SLA Breach Prediction](sla-breach-prediction.md) | Breach risk |
| [Business Impact Analysis](business-impact-analysis.md) | Impact framing |
| [Dependency Mapping](dependency-mapping.md) | Runtime dependencies |
| [Operational Decision Engine](operational-decision-engine.md) | Ops IF/THEN decisions |
| [Recommendations Engine](recommendations-engine.md) | Prioritized actions |

## Navigation

- **Previous:** [../operational-analytics/README.md](../operational-analytics/README.md)
- **Next:** [operations-intelligence-engine.md](operations-intelligence-engine.md)
- **See Also:** [../production-support-engine.md](../production-support-engine.md)

## Related Documents

- [Monitoring](../monitoring/README.md)
- [Operational Analytics](../operational-analytics/README.md)
- [Incident Management](../incident-management/README.md)
- [Sprint 7 QI Rules / Predictive](../../quality-intelligence/predictive-quality/README.md)
- [Sprint 7 Defect Intelligence](../../quality-intelligence/README.md)
