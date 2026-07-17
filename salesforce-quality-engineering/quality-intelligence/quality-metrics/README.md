---
title: Quality Metrics — README
module: Salesforce Quality Engineering
category: Quality Intelligence
document_type: Guide
version: 0.9.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
tags: [quality-intelligence, sprint-7, quality-metrics]
---

# Quality Metrics

## Purpose

Definitions, formulas, interpretation, and actions for enterprise QA metrics.

## Scope

Density, leakage, DRE, coverage, execution, automation, reopen, MTTD/MTTR, indices. No invented values.

## Inputs

- Counts from ADO/test tools
- Period definition

## Outputs

- Metric interpretations
- Threshold proposals
- Actions

## Available Documents

| Document | Focus |
|----------|-------|
| [Defect Density](defect-density.md) | Defects per size unit |
| [Defect Leakage](defect-leakage.md) | Escapes to later phase |
| [Defect Removal Efficiency](defect-removal-efficiency.md) | DRE |
| [Requirement Coverage](requirement-coverage.md) | Req↔test mapping |
| [Test Coverage](test-coverage.md) | Designed coverage |
| [Execution Progress](execution-progress.md) | Run progress |
| [Pass Rate](pass-rate.md) | Pass ratio |
| [Fail Rate](fail-rate.md) | Fail ratio |
| [Automation Coverage](automation-coverage.md) | Automated share |
| [Automation Stability](automation-stability.md) | Flake rate inverse |
| [Escaped Defects](escaped-defects.md) | Prod/UAT escapes |
| [Reopen Rate](reopen-rate.md) | Reopened bugs |
| [MTTD](mttd.md) | Mean time to detect |
| [MTTR](mttr.md) | Mean time to resolve |
| [Regression Effectiveness](regression-effectiveness.md) | Reg pack value |
| [Requirement Volatility](requirement-volatility.md) | Churn |
| [Sprint Quality Index](sprint-quality-index.md) | Sprint composite |
| [Release Quality Index](release-quality-index.md) | Release composite |
| [Production Stability Index](production-stability-index.md) | Prod stability |

## Navigation

- **Previous:** [../defect-patterns/README.md](../defect-patterns/README.md)
- **Next:** [../risk-analysis/README.md](../risk-analysis/README.md)
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
