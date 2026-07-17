---
title: Common Risks
module: Salesforce Quality Engineering
category: Knowledge
document_type: Knowledge Article
version: 0.5.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
review_cycle: quarterly
related_documents:
  - salesforce-quality-engineering/knowledge/reporting/common-risks.md
  - salesforce-quality-engineering/knowledge/requirement-analysis.md
  - salesforce-quality-engineering/knowledge/test-design-engine.md
keywords: [common-risks, salesforce, quality-engineering]
tags: [knowledge, sprint-4, reporting]
---

# Common Risks

**Purpose:** Catalog filter mistakes, running-user issues, and folder sharing leaks.

**Scope:** Salesforce QE knowledge — requirement analysis, testing strategy, regression, UAT, automation readiness, and production validation. Not an Admin or Developer how-to.

**Owner:** QE Practice Lead

**Version:** 0.5.0

**Status:** Draft (Sprint 4)

---

## Purpose

Catalog filter mistakes, running-user issues, and folder sharing leaks.

## Business Context

- Common Risks affects how business users complete journeys and how defects surface in production.
- QE must connect business outcomes to Salesforce configuration and automation behaviour.

## Salesforce Overview

- Salesforce provides Common Risks as a platform capability used across clouds and industries.
- Treat product details as org-confirmed; do not invent edition-specific features.

## Key Features

- Configurable behaviour driven by metadata and permissions
- Impacts create/read/update/delete journeys and reporting visibility
- Interacts with automation, security, and integrations

## Where Used

- Enterprise Salesforce programs during discovery, build, UAT, and hypercare
- Impact analysis when stories change related metadata

## Business Examples

- Retail: CSR updates customer preference and downstream Case routing changes
- Utilities: field update drives work-order eligibility or billing hold
- Banking: permission or validation change blocks a regulated update path

## Testing Considerations

- Confirm requirement intent maps to this component before designing scenarios
- Cover happy path, negative path, persona/permission path, and data boundary path
- Validate order-of-execution interactions with related automation
- Use [../test-design-engine.md](../test-design-engine.md) for scenario objectives and coverage matrix

## Functional Test Focus

- Observable outcome matches acceptance criteria for in-scope personas
- Field/object state after save matches business rules
- UI/API pathways produce equivalent business results where both are in scope

## Negative Test Focus

- Invalid input / missing required data blocked with clear message
- Unauthorized persona cannot complete restricted action
- Partial failure does not leave inconsistent record state (or is documented)

## Regression Considerations

- Neighbor objects, layouts, automation, and reports that consume the same fields
- Sharing/visibility side effects after metadata deploy
- Apply [../regression-planning.md](../regression-planning.md) for In / Out / Conditional scope

## Automation Opportunities

- API-level checks for deterministic rules (preferred over brittle UI)
- Smoke pack candidates for high-frequency create/update paths
- Do not automate unstable exploratory or one-off migration validation

## Production Risks

- Silent behaviour change after deploy (no error, wrong outcome)
- Permission drift between sandboxes and production
- Volume/concurrency differences vs test data

## Common Defects

- Requirement assumed standard behaviour that is actually custom
- Missing persona coverage (works for admin, fails for end user)
- Automation order-of-execution conflict
- Report/dashboard filters not updated with field changes

## Best Practices

- Analyse requirements and Salesforce impact before writing detailed cases
- Prefer platform-native configuration over custom when fit is confirmed
- Keep evidence: persona, data, environment, expected vs actual
- Cross-link BA artifacts; do not rewrite BA requirements as QE truth

## Interview Tips

- Explain how you would test Common Risks without jumping to click-paths first
- Describe risks, regression neighbors, and automation candidates with rationale

## Related Documents

- [Requirement Analysis](../requirement-analysis.md)
- [Test Design Engine](../test-design-engine.md)
- [Test Coverage Model](../test-coverage-model.md)
- [Risk-Based Testing](../risk-based-testing.md)
- [../README.md](../README.md)
- [README.md](README.md)

## Future Enhancements

- Deepen org-edition notes and industry examples in later sprints
- Link detailed case templates when Sprint 5 lands

## Navigation

- **Previous:** [Validation Strategy](validation-strategy.md)
- **Next:** [README](README.md)
- **See Also:** [README.md](README.md) · [Test Design Engine](../test-design-engine.md)
