---
title: Locator Robustness and Maintainability
version: 0.10.1
tags: [automation-intelligence, sprint-8, review-engine]
---

# Locator Robustness and Maintainability

## Purpose

Evaluate locator strategy for resilience under Lightning DOM and metadata change.

## Business Context

Brittle locators are the top driver of Salesforce UI automation maintenance.

## Architecture

Centralized locator definitions; role/label/test-id preference; explicit wait strategy; no hard-coded dynamic SF IDs.

## Decision Criteria

| Score | Signals |
|-------|---------|
| 5 | Role/label/test-id first; stable custom attributes; shared locator maps; auto-wait used well |
| 3 | Mixed strategies; some XPath absolute; inconsistent waits |
| 1 | Absolute XPath / index / generated IDs dominant; fixed sleeps |

## Best Practices

- Prefer accessible names; collaborate on `data-testid` where controllable.  
- Quarantine known-unstable screens rather than “fixing” with sleeps.  

## Salesforce Considerations

- Shadow DOM / dynamic components need tool-appropriate piercing strategies.  
- Record type / app / console variations need parameterized locators.  

## Automation Considerations

- Cross-link [../automation-patterns/stable-locator-patterns.md](../automation-patterns/stable-locator-patterns.md).  

## Common Pitfalls

- Copying Salesforce-generated IDs from DevTools into suites.  

## Examples

`getByRole('button', { name: 'Save' })` patterns dominate → 4–5.  
`//div[3]/div[2]/button` common → 1–2.

## Interview Questions

- What locator anti-patterns fail first on Lightning upgrades?  

## Related Documents

- [../playwright/locators.md](../playwright/locators.md)
- [Flaky and Stability](flaky-and-stability-review.md)

## Navigation

- **Previous:** [pom-screenplay-quality.md](pom-screenplay-quality.md)
- **Next:** [test-data-management-review.md](test-data-management-review.md)

## Future Enhancements

- Locator debt heatmap heuristic  
