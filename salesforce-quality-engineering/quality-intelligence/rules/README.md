---
title: Quality Intelligence Rules Engine — README
module: Salesforce Quality Engineering
category: Quality Intelligence
document_type: Guide
version: 0.9.1
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
tags: [quality-intelligence, sprint-7, rules-engine]
---

# Quality Intelligence Rules Engine

## Purpose

Convert quality signals (metrics, patterns, Salesforce hotspots) into **actionable recommendations** using reusable IF/THEN decision rules—so the AI behaves as an experienced QE consultant, not only a metrics reporter.

## Scope

**In scope:** Rule schema, evaluation process, metric-threshold rules, reopen/defect-quality rules, platform hotspot rules (Flow, Apex, etc.), security/permission rules, integration/cloud cluster rules, automation/regression/release-gate rules, recommendation priority.

**Out of scope:** Inventing metric values; hard-coding program thresholds without program context; replacing RCA (rules *trigger* RCA and prevention, they do not replace root-cause method selection).

## Inputs

- Defect counts / classifications / component tags
- Metric values with period (or TBC)
- Pattern detection outputs ([defect-patterns/](../defect-patterns/README.md))
- Release / sprint / production context
- Program thresholds (or defaults marked as *indicative*)

## Outputs

- Fired rules (Rule IDs)
- Prioritized recommendations
- Suggested next analyses (RCA, coverage review, security review)
- Escalation signals
- Explicit assumptions and confidence

## Available Documents

| Document | Focus |
|----------|-------|
| [Rules Engine](rules-engine.md) | Orchestration and consulting behaviour |
| [Rule Schema](rule-schema.md) | Standard IF/THEN structure |
| [Rule Evaluation Process](rule-evaluation-process.md) | How to evaluate and prioritize |
| [Metric Threshold Rules](metric-threshold-rules.md) | Leakage, DRE, pass rate, etc. |
| [Reopen and Defect Quality Rules](reopen-and-defect-quality-rules.md) | Reopen rate / fix verification |
| [Platform Hotspot Rules](platform-hotspot-rules.md) | Flow, Apex, config, data, etc. |
| [Security Permission Rules](security-permission-rules.md) | Profiles, PS, sharing, FLS |
| [Integration and Cloud Cluster Rules](integration-and-cloud-cluster-rules.md) | Cloud/integration production clusters |
| [Automation Stability Rules](automation-stability-rules.md) | Flaky automation / instability |
| [Regression and Coverage Rules](regression-and-coverage-rules.md) | Regression expansion / RTM gaps |
| [Release Gate Rules](release-gate-rules.md) | Gate fail / readiness recommendations |
| [Recommendation Priority](recommendation-priority.md) | Urgency and sequencing |

## Navigation

- **Previous:** [../quality-gates/README.md](../quality-gates/README.md)
- **Next:** [rules-engine.md](rules-engine.md)
- **See Also:** [../defect-intelligence-engine.md](../defect-intelligence-engine.md)

## Related Documents

- [Defect Intelligence Engine](../defect-intelligence-engine.md)
- [Quality Metrics](../quality-metrics/README.md)
- [Defect Patterns](../defect-patterns/README.md)
- [Predictive Quality](../predictive-quality/README.md)
- [Continuous Improvement](../continuous-improvement/README.md)
- [Salesforce Quality Intelligence](../knowledge-base/salesforce-quality-intelligence.md)
- [ADO Bug Workflow](../../ado/governance/bug-workflow.md)
