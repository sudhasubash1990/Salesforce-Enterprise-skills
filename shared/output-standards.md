---
title: Output Standards
module: Salesforce Business Analyst
category: Shared
document_type: Reference
version: 1.1.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/consulting-principles.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/interview-index.md]
related_examples: [examples/sample-project/README.md]
related_documents: [docs/metadata-schema.md, shared/traceability-model.md]
keywords: [output standards]
tags: [output-standards]
---

# Output Standards

Formatting and quality standards for all agent- and human-generated deliverables.

## Universal Sections

Every formal deliverable includes:

1. **Document control** (title, version, status, date, authors)
2. **Purpose**
3. **Scope** (in / out)
4. **Assumptions**
5. **Body** (type-specific)
6. **Open questions**
7. **Approval** (when status = approved)

## Writing Quality

| Do | Don't |
|----|-------|
| "Case must auto-route to Tier 2 when Priority = Critical" | "Make the case page better" |
| "Within 3 seconds for 95th percentile" | "Fast loading" |
| "Sales Manager role can reassign" | "Admins can do everything" |

## User Story Format

```markdown
### US-042: [Short title]

**As a** Service Agent,
**I want** to see related Cases on the Account timeline,
**So that** I can understand customer history without opening multiple tabs.

**Requirement refs:** BR-012, FR-008

**Acceptance criteria:**
1. Given an Account with 3+ related Cases, when the Agent views the Account record, then the Activity timeline shows Case subjects chronologically.
2. Given the Agent lacks Case read permission, when viewing the Account, then Cases are not visible.
3. Given a Case marked Internal Only, when a standard Agent views the Account, then that Case is excluded.

**Data considerations:** Case.AccountId, Case.IsVisibleInSelfService
**Notes:** Confirm sharing model for partner users (Open Question #4)
```

## BRD Requirement Format

```markdown
#### BR-012: Unified customer view for service agents

| Attribute | Value |
|-----------|-------|
| Priority | Must |
| Source | Discovery workshop 2026-06-15 |
| Owner | Service Operations |

**Statement:** Service agents must access consolidated customer interaction history (Cases, Orders, Contracts) from a single Account view during live customer contact.

**Success measure:** Average handle time reduced by 15% within 90 days of go-live.

**Dependencies:** Order and Contract data available in Salesforce or via integration.
```

## Tables and IDs

- All requirements numbered sequentially
- No duplicate IDs within a project namespace
- Cross-reference using ID links in markdown

## Agent Completion Statement

When finishing a deliverable, agents should end with:

```
**Assumptions made:** [list or "none"]
**Open questions:** [list or "none"]
**Suggested next steps:** [e.g., architect review, workshop validation]
```

## Related Brain Modules

- [Consulting Principles](../salesforce-business-analyst/brain/consulting-principles.md)

## Related Knowledge

- [Readme](../salesforce-business-analyst/knowledge/README.md)

## Related Templates

- [Readme](../salesforce-business-analyst/templates/README.md)

## Related Playbooks

- [Readme](../salesforce-business-analyst/playbooks/README.md)

## Related Industry Scenarios

- [Readme](../salesforce-business-analyst/scenarios/README.md)

## Related Interview Topics

- [Interview Index](../salesforce-business-analyst/interview-guide/interview-index.md)

## Related Examples

- [Readme](../examples/sample-project/README.md)

## Related Documents

- [Metadata Schema](../docs/metadata-schema.md)
- [Traceability Model](traceability-model.md)

## Traceability

**Upstream:** Governance | **Downstream:** All modules | **Validation:** glossary consistency

## Navigation

- **Previous:** [Glossary](glossary.md)
- **Next:** [Relationship Matrix](relationship-matrix.md)
- **See Also:** [cross-linking-framework](../docs/cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
