---
title: Automation Review Engine
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

Assess existing Salesforce automation frameworks against enterprise standards and recommend prioritized improvements—so the AI can modernize brownfield estates, not only design greenfield ones.

## Business Context

Enterprise Salesforce programs often inherit Playwright, Selenium, or Cypress suites with high maintenance cost, flaky CI, and secrets risk. A structured review turns opinions into an auditable scorecard useful for QA Leads, Automation Architects, and Delivery Managers.

## Overview

```
Ingest evidence (structure, samples, CI, metrics)
    ↓
Identify stack (Playwright / Selenium / Cypress / hybrid)
    ↓
Score 9 dimensions (1–5) with evidence
    ↓
Compute maintainability score + confidence
    ↓
Prioritize improvements (P0–P3)
    ↓
Produce review report (template)
```

**Hard rules:** Do not invent stability/coverage %. Do not rewrite entire suites in the review—recommend changes. Do not mandate tool migration without cost/benefit.

## Inputs

| Input | Prefer |
|-------|--------|
| Folder tree / module map | Yes |
| Sample page/component objects (sanitized) | Yes |
| Locator strategy examples | Yes |
| Config / env / secrets approach | Yes |
| CI pipeline stages | Yes |
| Flake/pass metrics or qualitative flake notes | Yes |
| Ownership / PR / branching notes | Optional |

## Outputs

1. Dimension scorecard  
2. Overall maintainability score (see [maintainability-score.md](maintainability-score.md))  
3. Prioritized backlog  
4. Tool-specific findings  
5. Missing evidence / confidence  

## Process

1. Load [review-scoring-model.md](review-scoring-model.md).  
2. Score each dimension using its checklist article.  
3. Apply tool lens ([playwright](playwright-framework-review.md) / [selenium](selenium-framework-review.md) / [cypress](cypress-framework-review.md)).  
4. Cross-check Sprint 7 flake rules and Sprint 8 governance/design standards.  
5. Publish via [review-report-template.md](review-report-template.md).  

### Dimensions (mandatory)

| # | Dimension | Article |
|---|-----------|---------|
| 1 | Framework architecture and modularity | [architecture-and-modularity.md](architecture-and-modularity.md) |
| 2 | POM / Screenplay implementation quality | [pom-screenplay-quality.md](pom-screenplay-quality.md) |
| 3 | Locator robustness and maintainability | [locator-robustness.md](locator-robustness.md) |
| 4 | Test data management approach | [test-data-management-review.md](test-data-management-review.md) |
| 5 | CI/CD readiness and pipeline integration | [cicd-readiness-review.md](cicd-readiness-review.md) |
| 6 | Reporting and observability | [reporting-observability.md](reporting-observability.md) |
| 7 | Flaky test indicators and stability | [flaky-and-stability-review.md](flaky-and-stability-review.md) |
| 8 | Code review and governance compliance | [governance-compliance-review.md](governance-compliance-review.md) |
| 9 | Security practices (secrets management) | [security-practices-review.md](security-practices-review.md) |

## Examples

**Evidence:** Selenium suite with XPath-heavy pages, credentials in `config.json`, no parallel CI.  
**Outcome:** Locators 2/5, Security 1/5 (P0), CI/CD 2/5; Maintainability Low; top actions: remove secrets, introduce resilient locators, add smoke stage.

## Best Practices

- Cite file/path patterns as evidence (never paste secrets).  
- Separate **product flakes** from **automation debt**.  
- Recommend incremental modernization (stabilize → structure → accelerate).  

## Salesforce Considerations

- Lightning dynamic DOM raises the bar for locator and wait design.  
- Prefer API setup with thin UI asserts when reviewing inverted pyramids.  
- Persona/storage-state (or equivalent) should exist for multi-profile SF testing.  

## Automation Considerations

- Review is advisory; teams confirm remediation sequencing.  
- Full script rewrites are out of scope unless explicitly requested later.  

## Common Pitfalls

- Scoring without evidence (“looks fine”).  
- Forcing Playwright rewrite when governance/secrets are the real P0.  
- Ignoring positive API-layer assets in a UI-heavy critique.  

## Interview Questions

- How do you assess a brownfield Salesforce automation framework?  
- What is a P0 finding in an automation review?  
- How does maintainability scoring differ from coverage %?  

## Related Documents

- [Review Scoring Model](review-scoring-model.md)
- [Maintainability Score](maintainability-score.md)
- [../automation-intelligence-engine.md](../automation-intelligence-engine.md)
- [../../quality-intelligence/rules/automation-stability-rules.md](../../quality-intelligence/rules/automation-stability-rules.md)

## Navigation

- **Previous:** [README.md](README.md)
- **Next:** [review-scoring-model.md](review-scoring-model.md)
- **See Also:** [review-report-template.md](review-report-template.md)

## Future Enhancements

- Machine-readable scorecard JSON export  
- Optional repo scanner heuristics (path/pattern only)  
