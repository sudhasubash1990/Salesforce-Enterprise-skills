---
title: Salesforce Regression Planning
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing, regression-planning]
---

# Salesforce Regression Planning

## Objective

Plan regression, smoke, and sanity test suites for Salesforce releases — identifying which functional scenarios must be re-executed based on change impact.

## Inputs

- Release scope (new features, configuration changes, metadata changes)
- MIA impact report — chain [MIA](../../metadata-impact-analyzer/SKILL.md)
- Existing functional test inventory
- Production defect history (areas with higher defect density)
- Deployment timeline and testing window

## Validation Workflow

1. Obtain MIA impact report for the release
2. Map impacted objects/features to existing functional test scenarios
3. Classify scenarios: smoke (critical path), sanity (feature-specific), full regression
4. Prioritize by risk: high-defect areas and cross-cloud journeys first
5. Define smoke suite (executed immediately post-deployment)
6. Define sanity suite (feature-specific validation post-deployment)
7. Define full regression scope (scheduled within testing window)

## Decision Points

| Decision | Criteria |
|----------|----------|
| Smoke only | Hotfix with isolated change, low risk |
| Smoke + sanity | Standard release with feature changes |
| Full regression | Major release, cross-cloud impact, or schema change |
| Regression scope reduction | Testing window constrained — prioritize by risk |

## Expected Results

- Smoke suite covers critical business paths and completes within defined window
- Sanity suite validates changed features without false positives from unrelated areas
- Full regression suite covers all impacted functional scenarios per MIA report
- Regression scope is traceable to change impact — not arbitrary

## Anti-Patterns

- Running full regression for every release regardless of change scope
- Defining regression scope without MIA impact analysis
- Skipping smoke test after deployment — going straight to feature testing

## Related Documents

- [Metadata Impact Analyzer](../../metadata-impact-analyzer/SKILL.md)
- [SKILL.md](../SKILL.md)
