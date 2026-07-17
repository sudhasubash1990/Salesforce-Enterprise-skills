---
title: Selenium Framework Review Lens
version: 0.10.1
tags: [automation-intelligence, sprint-8, review-engine]
---

# Selenium Framework Review Lens

## Purpose

Apply Selenium-specific expectations for brownfield Salesforce automation reviews.

## Decision Criteria (additive checks)

| Area | Look for |
|------|----------|
| Waits | Explicit waits; almost no `Thread.sleep` |
| Driver lifecycle | Clean create/quit; Grid/remote config externalized |
| POM | Mature page factory or equivalent without locator leak |
| Parallel | Thread-safe drivers; no static WebDriver abuse |
| Grid | Healthy node strategy if scaled |
| Migration | Document cost/benefit before Playwright rewrite |

## Salesforce Considerations

- Lightning needs disciplined waits and robust locators—score harshly on sleeps.  

## Common Pitfalls

- Static driver singletons breaking parallel CI.  
- Recommending immediate full rewrite without P0 security/flake fixes.  

## Related Documents

- [../selenium/README.md](../selenium/README.md)
- [Improvement Prioritization](improvement-prioritization.md)

## Navigation

- **Previous:** [playwright-framework-review.md](playwright-framework-review.md)
- **Next:** [cypress-framework-review.md](cypress-framework-review.md)

## Future Enhancements

- Selenium→Playwright migration readiness checklist  
