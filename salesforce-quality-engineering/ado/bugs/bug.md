---
title: Bug
module: Salesforce Quality Engineering
category: ADO
document_type: Knowledge Article
version: 0.8.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
tags: [ado, sprint-6, bugs]
keywords: [bug, azure-devops, quality-engineering]
---

# Bug

**Scope:** Sprint 6 Azure DevOps Delivery Intelligence — QE lens. Artifact content quality, not ADO admin or API automation.

**Version:** 0.8.0

---

## Purpose

Create enterprise-quality bug reports suitable for triage and release decisions.
## Business Context

- Supports enterprise Salesforce delivery governance and traceability.
- Aligns BA backlog language with QE evidence.
## Lifecycle

- Created → Active → Resolved/Closed (or Done) per process template
- Link upward to parent and downward to children/tests/bugs
## Inputs

- Scope / requirements
- Prior analysis or design artifacts
- Area Path / Iteration context
## Outputs

- Well-formed Bug ready to paste into Azure DevOps
- Links for traceability
## Relationships

- See [Relationship Model](../relationship-model.md)
## Examples

- Title pattern: `<Capability> - <Outcome>`
- Keep descriptions scannable with headings and bullets
## Testing Considerations

- Every User Story should drive scenarios/cases
- Bugs must link to failing case/story when known
- Test Plans organize evidence for release gates
## Governance

- Respect DoR/DoD
- Area Path and Iteration required for reporting
- No client PII/credentials in work item fields
## Best Practices

- Title: concise failure statement
- Fields: Environment, Area, Iteration, Build/Release, Steps, Expected, Actual, Severity, Priority, Business Impact, Evidence, Regression Impact, Retest Guidance
- Link to Test Case and User Story when known
## Common Mistakes

- Orphan work items with no parent/links
- Tasks that are epics in disguise
- Bugs without repro steps or environment
- Test cases without requirement mapping
## Quality Engineering Perspective

- Work items are the backbone of evidence—not just task tracking.
- QE ensures testability, traceability, and release readiness signals in ADO.
## Interview Questions

- How does this work item type support end-to-end traceability?
- What fields are mandatory for QE reporting?
- How do you avoid duplicate BA vs QE content?
## Related Documents

- [../../templates/defect-report.md](../../templates/defect-report.md)
- [../../guidelines/defect-documentation-standards.md](../../guidelines/defect-documentation-standards.md)
- [QE Brain (Sprint 1)](../../brain/README.md)
- [Requirement Analysis (Sprint 2)](../../knowledge/requirement-analysis.md)
- [Test Design Engine (Sprint 3)](../../knowledge/test-design-engine.md)
- [Platform Foundation 4A](../../knowledge/platform/README.md)
- [Enterprise Knowledge 4B](../../knowledge/clouds/README.md)
- [Documentation Generator (Sprint 5)](../../templates/README.md)
- [BA ADO Backlog Integration](../../../salesforce-business-analyst/knowledge/ado-backlog-integration.md) (sibling—do not duplicate)
- [README.md](README.md)
- [../README.md](../README.md)
- [../relationship-model.md](../relationship-model.md)

## Navigation

- **Previous:** [README](README.md)
- **Next:** [README](README.md)
- **See Also:** [README.md](README.md)

## Future Enhancements

- Optional API publish helpers (post–Delivery Intelligence)
- Project-specific process template mapping examples
