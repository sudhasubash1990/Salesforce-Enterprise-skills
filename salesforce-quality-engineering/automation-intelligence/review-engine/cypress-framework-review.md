---
title: Cypress Framework Review Lens
version: 0.10.1
tags: [automation-intelligence, sprint-8, review-engine]
---

# Cypress Framework Review Lens

## Purpose

Apply Cypress-specific expectations and Salesforce fit checks during reviews.

## Decision Criteria (additive checks)

| Area | Look for |
|------|----------|
| Architecture | Support file / custom commands used judiciously (not god-commands) |
| Isolation | Tests clean; no improper state leakage |
| Auth | Secure session handling; no committed sessions |
| API | `cy.request` for setup where appropriate |
| Limitations | Multi-tab / multi-origin SF flows acknowledged |
| CI | Dashboard/recording policy clear; secrets safe |

## Salesforce Considerations

- Flag Cypress when Lightning multi-window/console patterns dominate—may be wrong tool, not just bad tests.  
- Do not auto-fail review solely for not being Playwright; score fitness and quality.  

## Common Pitfalls

- Overusing `cy.wait(fixedMs)`.  
- Ignoring origin constraints until late in the program.  

## Related Documents

- [../cypress/README.md](../cypress/README.md)
- [../framework-comparison/cypress.md](../framework-comparison/cypress.md)

## Navigation

- **Previous:** [selenium-framework-review.md](selenium-framework-review.md)
- **Next:** [README.md](README.md)

## Future Enhancements

- Cypress vs Playwright decision addendum for reviews  
