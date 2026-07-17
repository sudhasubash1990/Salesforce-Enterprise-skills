---
title: Reporting and Observability Review
version: 0.10.1
tags: [automation-intelligence, sprint-8, review-engine]
---

# Reporting and Observability Review

## Purpose

Assess whether failures are diagnosable quickly via reports, logs, traces, and artifacts.

## Business Context

Slow triage destroys automation ROI even when coverage looks high.

## Architecture

Structured reports (JUnit/HTML), per-test logs, failure traces/screenshots/video (as applicable), correlation IDs, environment metadata in results.

## Decision Criteria

| Score | Signals |
|-------|---------|
| 5 | Rich failure artifacts; searchable reports; env/build metadata; dashboards |
| 3 | Basic pass/fail HTML; limited traces |
| 1 | Console-only; no artifacts; undiagnosable CI fails |

## Best Practices

- Capture artifacts **on failure** to control cost.  
- Include org/sandbox, browser, persona in report context.  

## Salesforce Considerations

- Record URL / Salesforce ID in logs when safe (non-prod).  

## Automation Considerations

- Playwright: tracing; Selenium: screenshots + logs; Cypress: screenshots/video.  

## Common Pitfalls

- Always-on video for every test in large suites.  

## Examples

Trace attached on fail + JUnit publish to ADO → 4–5.

## Interview Questions

- What observability proves a Salesforce UI failure is product vs automation?  

## Related Documents

- [../playwright/tracing.md](../playwright/tracing.md)
- [../framework-design/reporting.md](../framework-design/reporting.md)

## Navigation

- **Previous:** [cicd-readiness-review.md](cicd-readiness-review.md)
- **Next:** [flaky-and-stability-review.md](flaky-and-stability-review.md)

## Future Enhancements

- Observability checklist for executives  
