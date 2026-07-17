---
title: Automation Review Report Template
version: 0.10.1
tags: [automation-intelligence, sprint-8, review-engine]
---

# Automation Review Report Template

## Purpose

Standard output structure for Automation Review Engine assessments.

## Business Context

Consistent reports support modernization governance and vendor/partner handoffs.

## Template

```markdown
# Automation Framework Review Report

## Executive Summary
- Framework / stack:
- Maintainability score / band / status:
- Confidence:
- Top 3 actions:

## Scope and Evidence
- Repos / modules reviewed:
- Evidence provided:
- Missing evidence:

## Dimension Scorecard
| Dimension | Score (1–5) | Evidence | Priority gaps |
|-----------|-------------|----------|---------------|
| Architecture & modularity | | | |
| POM / Screenplay quality | | | |
| Locator robustness | | | |
| Test data management | | | |
| CI/CD readiness | | | |
| Reporting & observability | | | |
| Flaky / stability | | | |
| Governance compliance | | | |
| Security practices | | | |

## Maintainability Roll-up
- Weighted score:
- Overrides applied:
- Band / status:

## Tool-Specific Findings
(Playwright / Selenium / Cypress lens)

## Prioritized Improvements
| ID | Priority | Action | Owner cue | Success check |
|----|----------|--------|-----------|---------------|
| IMP-001 | P0 | | | |

## Salesforce Considerations
- Pyramid fit / Lightning risks / persona coverage:

## Assumptions and Out of Scope

## Next Review Date / Exit Criteria
```

## Best Practices

- Never paste secrets into the report.  
- Mark N/A dimensions explicitly.  

## Related Documents

- [Automation Review Engine](automation-review-engine.md)
- [Improvement Prioritization](improvement-prioritization.md)

## Navigation

- **Previous:** [improvement-prioritization.md](improvement-prioritization.md)
- **Next:** [playwright-framework-review.md](playwright-framework-review.md)

## Future Enhancements

- ADO work-item export mapping for IMP-*  
