---
title: Defect Pattern Recognition — README
module: Salesforce Quality Engineering
category: Quality Intelligence
document_type: Guide
version: 0.9.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
tags: [quality-intelligence, sprint-7, defect-patterns]
---

# Defect Pattern Recognition

## Purpose

Detect recurring patterns, hotspots, and leakage signals with confidence and prevention actions.

## Scope

Pattern types, detection rules, confidence scoring, preventive actions.

## Inputs

- Historical defects
- Component tags
- Release timeline

## Outputs

- Pattern list
- Confidence
- Preventive actions

## Available Documents

| Document | Focus |
|----------|-------|
| [Recurring Defects](recurring-defects.md) | Same failure repeats |
| [Duplicate Defects](duplicate-defects.md) | Same issue logged multiple times |
| [Regression Patterns](regression-patterns.md) | Change-induced repeats |
| [Module Hotspots](module-hotspots.md) | Hot component areas |
| [High Risk Components](high-risk-components.md) | Risk-ranked components |
| [Requirement Gaps](requirement-gaps.md) | Pattern of AC gaps |
| [Environment Failures](environment-failures.md) | Env failure clusters |
| [Integration Failures](integration-failures.md) | Interface failure clusters |
| [Security Weaknesses](security-weaknesses.md) | Access defect patterns |
| [Automation Instability](automation-instability.md) | Flaky automation patterns |
| [Production Leakage](production-leakage.md) | Escape patterns |
| [Business Rule Violations](business-rule-violations.md) | Rule breach patterns |
| [Pattern Detection Rules](pattern-detection-rules.md) | Detection rule catalog |
| [Confidence Score](confidence-score.md) | Pattern confidence |
| [Suggested Preventive Actions](suggested-preventive-actions.md) | Prevention catalog |

## Navigation

- **Previous:** [../root-cause-analysis/README.md](../root-cause-analysis/README.md)
- **Next:** [../quality-metrics/README.md](../quality-metrics/README.md)
- **See Also:** [../README.md](../README.md)

## Related Documents

- [QE Brain (Sprint 1)](../../brain/README.md)
- [Requirement Analysis (Sprint 2)](../../knowledge/requirement-analysis.md)
- [Test Design Engine (Sprint 3)](../../knowledge/test-design-engine.md)
- [Platform Foundation 4A](../../knowledge/platform/README.md)
- [Enterprise Knowledge 4B](../../knowledge/clouds/README.md)
- [Documentation Generator (Sprint 5)](../../templates/README.md)
- [ADO Delivery Intelligence (Sprint 6)](../../ado/README.md)
- [Defect Report Template](../../templates/defect-report.md)
- [Defect RCA Template](../../templates/defect-rca-report.md)
