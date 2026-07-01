---
title: Review Process
module: Salesforce Business Analyst
category: Governance
document_type: Framework
version: 1.1.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/interview-index.md]
related_examples: [examples/sample-project/README.md]
related_documents: [docs/metadata-schema.md, docs/cross-linking-framework.md]
keywords: [review process]
tags: [review-process]
---

# Review Process

## Review Types

| Type | Trigger | Reviewers | SLA |
|------|---------|-----------|-----|
| **Content PR** | Any pull request | 1 peer + 1 maintainer | 2 business days |
| **Skill release** | MINOR/MAJOR skill version | BA practice lead | 5 business days |
| **Governance** | Changes to `docs/`, `.cursor/` | Repository maintainer | 3 business days |
| **Deliverable approval** | Client-facing BRD/story pack | Client PO + BA lead | Per project |

## PR Review Checklist

### Reviewer Responsibilities

- [ ] Purpose and scope of change are clear
- [ ] No regression in skill routing or broken links
- [ ] Examples are anonymized
- [ ] Terminology aligns with `shared/glossary.md`
- [ ] CHANGELOG updated appropriately
- [ ] Skill `description` follows third-person WHAT + WHEN pattern

### BA-Specific Review (Skill Changes)

- [ ] Playbook steps are actionable, not generic PM advice
- [ ] Templates produce testable outputs
- [ ] Salesforce platform guidance is current and conservative (prefer standard)
- [ ] Industry scenarios flag regulatory items as "confirm with client"

## Deliverable Review Workflow (Engagements)

```
Draft (author/agent)
    → Self-check (checklists.md)
    → Internal peer review
    → Solution Architect review (fit-gap, integration, data model)
    → Client workshop / sign-off
    → Approved (version 1.0.0)
```

## Feedback Severity

| Level | Action |
|-------|--------|
| **Blocker** | Must fix before merge/approval |
| **Major** | Fix before release; may merge with ticket |
| **Minor** | Fix or accept with documented rationale |
| **Suggestion** | Optional improvement |

## Escalation

Unresolved disputes on fit-gap classification or scope:

1. Document options with pros/cons
2. Escalate to program architect or steering committee
3. Record decision in decision log (ADR format recommended)

## Related Brain Modules

N/A — no direct relationships for this document type.

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

- [Metadata Schema](metadata-schema.md)
- [Cross Linking Framework](cross-linking-framework.md)

## Traceability

**Upstream:** — | **Downstream:** All repository documents | **Validation:** validate_metadata.py

## Navigation

- **Previous:** [Repository Guidelines](repository-guidelines.md)
- **Next:** [Security Guidelines](security-guidelines.md)
- **See Also:** [cross-linking-framework](cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
