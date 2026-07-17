---
title: Sharing Rules
module: Salesforce Quality Engineering
category: Automation Intelligence
document_type: Knowledge Article
version: 0.10.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-18
last_updated: 2026-07-18
tags: [automation-intelligence, sprint-8, salesforce]
keywords: [sharing-rules, automation-strategy, test-automation]
---

# Sharing Rules

**Scope:** Sprint 8 Automation Intelligence — strategy and architecture advisory. **No full script generation.** Playwright-first, framework-agnostic. Reuse Sprint 3 automation candidates and Sprint 7 flaky-test rules.

**Version:** 0.10.0

---

## Purpose

Advise how to automate or validate Sharing Rules on Salesforce programs.
## Business Context

- Automation exists to protect business outcomes and accelerate safe delivery—not to maximize script count.
- Enterprise Salesforce programs need maintainable, CI-ready automation with clear ownership.
## Architecture

- Prefer API/metadata/service assertions for Sharing Rules where UI is not the risk.
- Add targeted UI only for persona-visible outcomes.
## Decision Criteria

- Is the behavior better asserted via API, UI, or both?
- How volatile is the UI/metadata surface?
- What persona/security paths are mandatory?
## Advantages

- Improves repeatability and release confidence when applied to stable, high-value paths
- Enables continuous testing feedback in pipelines
## Limitations

- Poor candidate selection creates flaky suites and false confidence
- Does not replace exploratory, usability, or ambiguous-requirement testing
## Best Practices

- Automate after path stability and oracle clarity
- Design for parallel, idempotent, environment-aware execution
- Quarantine flaky tests; protect CI signal quality
- Document ownership, naming, and review gates
## Salesforce Considerations

- Load matching 4A/4B knowledge for Sharing Rules before recommending design.
- Respect packaging, governor, and sharing constraints.
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

- Illustrative: smoke login + create Case via API + UI assert status — not a full script dump
- Decision example: high-churn Lightning page → keep manual exploratory; automate service assertions
## Interview Questions

- When would you apply Sharing Rules on a Salesforce program?
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

- **Previous:** [Permission Sets](permission-sets.md)
- **Next:** [Experience Cloud](experience-cloud.md)
- **See Also:** [../README.md](../README.md)

## Future Enhancements

- Program-specific framework blueprints under outputs/<project>/
- Optional script templates in a later sprint if explicitly requested
