---
title: Validation Rules
module: Salesforce Quality Engineering
category: Knowledge
document_type: Knowledge Article
version: 0.5.1
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
review_cycle: quarterly
related_documents:
  - salesforce-quality-engineering/knowledge/automation/validation-rules.md
  - salesforce-quality-engineering/knowledge/requirement-analysis.md
  - salesforce-quality-engineering/knowledge/test-design-engine.md
  - salesforce-quality-engineering/brain/README.md
keywords: [validation-rules, salesforce, quality-engineering, platform-foundation]
tags: [knowledge, sprint-4a, automation]
---

# Validation Rules

**Purpose:** QE guidance for VR formulas, bypass patterns, and message testability.

**Scope:** Sprint 4A Platform Foundation — QE lens (analysis, test design, regression, automation readiness, production validation). Not Admin/Developer how-to.

**Owner:** QE Practice Lead

**Version:** 0.5.1

**Status:** Draft (Sprint 4A)

---

## Purpose

QE guidance for VR formulas, bypass patterns, and message testability.

## Business Context

- Business outcomes depend on correct platform behaviour for the right personas and data.
- Defects often appear as wrong visibility, silent automation side effects, or data integrity breaks—not only UI errors.

## Salesforce Overview

- Salesforce exposes this capability as configurable metadata (and sometimes data) on a multi-tenant platform.
- Confirm edition, licenses, and org-specific configuration before asserting behaviour.

## Architecture

- Fires on save before many after-save automations—understand order of execution
- May be bypassed by specific integration designs—confirm explicitly

## Business Usage

- Supports enterprise CRM / service / industry processes on Salesforce.
- Used by named personas with least-privilege access expectations.

## Requirement Analysis Guidance

- Map story AC to this component using [../requirement-analysis.md](../requirement-analysis.md)
- Ask: which objects/fields/personas/channels (UI vs API) are in scope?
- Flag untestable language and missing negative/permission paths.

## Testing Considerations

- Design scenario objectives via [../test-design-engine.md](../test-design-engine.md) before detailed cases
- Cover happy path, negative, boundary, and persona/permission paths
- Evidence: persona, data, environment, expected vs actual

## Functional Testing

- Observable outcomes match acceptance criteria for in-scope personas
- State after save/action matches business rules

## Negative Testing

- Unauthorized persona cannot complete restricted action
- Invalid/missing data is blocked with a clear, testable message

## Boundary Testing

- Field length, numeric edges, date edges, picklist subsets, null/blank
- Volume edges where platform limits may surface (document assumptions)

## Regression Testing

- Apply [../regression-planning.md](../regression-planning.md) — In / Out / Conditional scope
- Neighbor automation, layouts, reports, and integrations that consume the same fields

## Automation Opportunities

- API-level checks for deterministic rules (preferred over brittle UI)
- Smoke candidates for high-frequency create/update paths
- Do not automate unstable exploratory or one-off migration validation

## Security Considerations

- Validate CRUD/FLS/sharing for every persona named in the requirement
- Treat View All / Modify All / guest access as high-risk exceptions

## Performance Considerations

- Consider bulk behaviour and governor-limit failure modes when volume is in scope
- LDV and selective queries matter for list views, roll-ups, sharing, and batches

## Production Risks

- Silent behaviour change after deploy (no error, wrong outcome)
- Permission or data drift between sandboxes and production

## Common Defects

- Works for System Admin; fails for end-user persona
- Order-of-execution conflict between automation components
- Missing regression on neighbor reports/integrations

## Common Root Causes

- Incomplete requirement analysis (missing persona, data, or exception path)
- Environment config drift (FLS, assignment, CMDT, custom settings)
- Assumed standard behaviour that was customized

## Best Practices

- Analyse requirements and Salesforce impact before writing detailed cases
- Prefer platform-native fit when confirmed; document gaps explicitly
- Keep evidence packs suitable for Go/No-Go and audit
- Reason with [../../brain/README.md](../../brain/README.md) and [../../skill.md](../../skill.md)

## Interview Questions

- How would you decide regression scope when this component changes?
- What negative and permission scenarios are mandatory?
- Which failures are common in production and how do you detect them?

## References

- Salesforce Help / Release Notes (org-confirmed edition)
- ISTQB: risk-based testing, equivalence partitioning, boundary value analysis
- [Requirement Analysis](../requirement-analysis.md) · [Test Design Engine](../test-design-engine.md)


## Related Documents

- [../validation-rule-testing.md](../validation-rule-testing.md)
- [Requirement Analysis](../requirement-analysis.md)
- [Test Design Engine](../test-design-engine.md)
- [QE Brain](../../brain/README.md)
- [Risk-Based Testing](../risk-based-testing.md)
- [README.md](README.md)
- [../README.md](../README.md)

## Navigation

- **Previous:** [README](README.md)
- **Next:** [Record-Triggered Flows](record-triggered-flows.md)
- **See Also:** [README.md](README.md) · [Test Design Engine](../test-design-engine.md)

## Future Enhancements

- Deepen industry examples in Sprint 4B where cloud-specific
- Link Sprint 5 case templates to scenario objectives herein
