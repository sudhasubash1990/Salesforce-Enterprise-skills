---
title: Playwright Framework Review Lens
version: 0.10.1
tags: [automation-intelligence, sprint-8, review-engine]
---

# Playwright Framework Review Lens

## Purpose

Apply Playwright-specific expectations when reviewing existing Playwright estates for Salesforce.

## Decision Criteria (additive checks)

| Area | Look for |
|------|----------|
| Fixtures | Typed fixtures; worker isolation; no shared mutable page |
| Locators | `getByRole` / label / test id over CSS/XPath soup |
| Auth | `storageState` per persona; secrets not in project |
| API | `request` context for setup/teardown |
| Resilience | Auto-wait used; traces on fail; smart retries |
| Parallel | Fully parallel with isolated data |
| Config | Projects per browser/env; no hardcoded org URLs in tests |

## Salesforce Considerations

- Console/Lightning navigation helpers centralized.  
- Network interception used carefully (prefer real SF API for setup).  

## Common Pitfalls

- Disabling isolation to “make tests pass”.  
- Committing `storageState` with session cookies to git.  

## Related Documents

- [../playwright/README.md](../playwright/README.md)
- [Automation Review Engine](automation-review-engine.md)

## Navigation

- **Previous:** [review-report-template.md](review-report-template.md)
- **Next:** [selenium-framework-review.md](selenium-framework-review.md)

## Future Enhancements

- Playwright config smell list  
