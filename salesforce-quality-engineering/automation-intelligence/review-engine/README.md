---
title: Automation Review Engine — README
module: Salesforce Quality Engineering
category: Automation Intelligence
document_type: Guide
version: 0.10.1
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-18
last_updated: 2026-07-18
tags: [automation-intelligence, sprint-8, review-engine]
---

# Automation Review Engine

## Purpose

Evaluate **existing** automation assets (Playwright, Selenium, Cypress, or hybrid) against enterprise Salesforce standards—and produce a maintainability score with prioritized improvements. Complements design/recommendation engines by assessing what teams already have.

## Scope

**In scope:** Architecture/modularity, POM/Screenplay quality, locator robustness, test data, CI/CD readiness, reporting/observability, flake/stability, governance, security/secrets, overall maintainability scoring, tool-specific review lenses, improvement prioritization.

**Out of scope:** Rewriting full test suites; inventing coverage/stability % without evidence; mandating Playwright migration without brownfield analysis.

## Inputs

- Repo outline / folder tree / sample page objects / configs (sanitized)
- CI pipeline description or YAML sketches
- Flake/failure metrics (or qualitative signals)
- Framework type (Playwright / Selenium / Cypress / other)
- Salesforce UI/API mix and persona model

## Outputs

- Dimension scores (1–5) with evidence
- Overall maintainability score
- Prioritized improvement backlog (P0–P3)
- Tool-specific findings
- Confidence and missing-evidence list

## Available Documents

| Document | Focus |
|----------|-------|
| [Automation Review Engine](automation-review-engine.md) | Orchestration and review process |
| [Review Scoring Model](review-scoring-model.md) | 1–5 scales and weighting |
| [Architecture and Modularity](architecture-and-modularity.md) | Layering and structure |
| [POM / Screenplay Quality](pom-screenplay-quality.md) | Abstraction quality |
| [Locator Robustness](locator-robustness.md) | Locator maintainability |
| [Test Data Management](test-data-management-review.md) | Data approach review |
| [CI/CD Readiness](cicd-readiness-review.md) | Pipeline integration |
| [Reporting and Observability](reporting-observability.md) | Reports, traces, logs |
| [Flaky and Stability](flaky-and-stability-review.md) | Flake indicators |
| [Governance Compliance](governance-compliance-review.md) | Standards, PR, ownership |
| [Security Practices](security-practices-review.md) | Secrets and credentials |
| [Maintainability Score](maintainability-score.md) | Roll-up score + narrative |
| [Improvement Prioritization](improvement-prioritization.md) | P0–P3 remediation order |
| [Review Report Template](review-report-template.md) | Standard review output |
| [Playwright Framework Review](playwright-framework-review.md) | Playwright lens |
| [Selenium Framework Review](selenium-framework-review.md) | Selenium lens |
| [Cypress Framework Review](cypress-framework-review.md) | Cypress lens |

## Navigation

- **Previous:** [../decision-engine/README.md](../decision-engine/README.md)
- **Next:** [automation-review-engine.md](automation-review-engine.md)
- **See Also:** [../automation-intelligence-engine.md](../automation-intelligence-engine.md)

## Related Documents

- [Automation Decision Engine](../automation-decision-engine.md)
- [Framework Design](../framework-design/README.md)
- [Automation Governance](../automation-governance/README.md)
- [Maintenance](../maintenance/README.md)
- [QI Automation Stability Rules](../../quality-intelligence/rules/automation-stability-rules.md)
- [Playwright Knowledge](../playwright/README.md)
