---
title: POM / Screenplay Implementation Quality
version: 0.10.1
tags: [automation-intelligence, sprint-8, review-engine]
---

# POM / Screenplay Implementation Quality

## Purpose

Assess quality of Page Object Model, Component Object Model, or Screenplay abstractions.

## Business Context

Weak abstractions leak UI details into tests and multiply Salesforce Lightning churn cost.

## Architecture

POM/COM: pages/components expose intent methods; tests read like business steps. Screenplay: actors, tasks, questions, abilities separated.

## Decision Criteria

| Score | Signals |
|-------|---------|
| 5 | Intent methods; no raw locators in tests; components reused; assertions at right layer |
| 3 | POM exists but thin/anemic or fat (business + nav + assert mixed) |
| 1 | Locators and sleeps inline in every test |

## Best Practices

- Prefer business verbs (`submitCase`) over click chains in tests.  
- Keep assertions out of navigation-only methods unless Screenplay questions.  

## Salesforce Considerations

- Component objects for reusable Lightning widgets (related lists, modals).  

## Automation Considerations

- Do not require Screenplay if solid POM/COM meets needs—score design quality, not fashion.  

## Common Pitfalls

- “POM” that only stores selectors with no behavior.  
- Duplicated page classes per test file.  

## Examples

Tests call `casePage.createCase(data)` and API prep fixtures → score 4+.

## Interview Questions

- POM vs Screenplay—what do you review for quality?  

## Related Documents

- [../framework-design/page-object-model.md](../framework-design/page-object-model.md)
- [Locator Robustness](locator-robustness.md)

## Navigation

- **Previous:** [architecture-and-modularity.md](architecture-and-modularity.md)
- **Next:** [locator-robustness.md](locator-robustness.md)

## Future Enhancements

- Anti-pattern gallery  
