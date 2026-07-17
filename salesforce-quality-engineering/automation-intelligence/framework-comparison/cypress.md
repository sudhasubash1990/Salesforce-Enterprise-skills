---
title: Cypress
module: Salesforce Quality Engineering
category: Automation Intelligence
document_type: Knowledge Article
version: 0.10.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-18
last_updated: 2026-07-18
tags: [automation-intelligence, sprint-8, framework-comparison]
keywords: [cypress, automation-strategy, test-automation]
---

# Cypress

**Scope:** Sprint 8 Automation Intelligence — strategy and architecture advisory. **No full script generation.** Playwright-first, framework-agnostic. Reuse Sprint 3 automation candidates and Sprint 7 flaky-test rules.

**Version:** 0.10.0

---

## Purpose

Compare Cypress as an automation option for enterprise Salesforce programs.
## Business Context

- Automation exists to protect business outcomes and accelerate safe delivery—not to maximize script count.
- Enterprise Salesforce programs need maintainable, CI-ready automation with clear ownership.
## Architecture

- Cypress sits in the tool layer of the automation stack; selection depends on team skills, UI vs API mix, and CI constraints.
- Remain framework-agnostic at strategy level; Playwright-first is a default recommendation, not a mandate.
## Decision Criteria

- Salesforce UI suitability and locator resilience
- API testing support
- CI/CD and parallel execution maturity
- Learning curve and hiring market
- Maintenance model and community/vendor support
## Advantages

- Developer-friendly DX
- Time-travel debugging
- Strong for single-origin web apps
## Limitations

- Multi-tab/multi-origin and some enterprise patterns harder
- JavaScript-centric
## Best Practices

- Consider for specific web apps; not automatic default over Playwright for Salesforce
- Pilot on 1–2 critical journeys before estate-wide adoption
- Define POM/COM or Screenplay conventions before scale
## Salesforce Considerations

- Evaluate carefully for Salesforce Lightning complexity and multi-window flows.
- Validate against Lightning and Experience Cloud constraints before committing.
## Automation Considerations

- No full script generation in Sprint 8—produce design decisions, structure, and CI strategy
- Estimate effort/ROI with assumptions; delivery team confirms
- Cross-link Sprint 7 automation stability rules when flake signals appear
## Common Pitfalls

- Automating unstable UIs before API coverage
- Hard-coding secrets or org-specific IDs
- 100% UI coverage goals without pyramid discipline
- Skipping test data cleanup and environment isolation
## Examples

- Recommend Cypress when consider for specific web apps; not automatic default over playwright for salesforce
- Document migration risks if replacing an existing framework
## Interview Questions

- When would you apply Cypress on a Salesforce program?
- How do you balance Playwright-first guidance with an existing Selenium estate?
- What signals tell you automation is not yet appropriate?
## Related Documents

- [QE Brain (Sprint 1)](../../brain/README.md)
- [Requirement Analysis (Sprint 2)](../../knowledge/requirement-analysis.md)
- [Test Design Engine (Sprint 3)](../../knowledge/test-design-engine.md)
- [Platform Foundation 4A](../../knowledge/platform/README.md)
- [Enterprise Knowledge 4B](../../knowledge/clouds/README.md)
- [Documentation Generator (Sprint 5)](../../templates/README.md)
- [ADO Delivery Intelligence (Sprint 6)](../../ado/README.md)
- [Defect Intelligence (Sprint 7)](../../quality-intelligence/README.md)
- [QI Automation Stability Rules](../../quality-intelligence/rules/automation-stability-rules.md)
- [README.md](README.md)
- [../README.md](../README.md)
- [../automation-decision-engine.md](../automation-decision-engine.md)

## Navigation

- **Previous:** [Selenium](selenium.md)
- **Next:** [Robot Framework](robot-framework.md)
- **See Also:** [../README.md](../README.md)

## Future Enhancements

- Program-specific framework blueprints under outputs/<project>/
- Optional script templates in a later sprint if explicitly requested
