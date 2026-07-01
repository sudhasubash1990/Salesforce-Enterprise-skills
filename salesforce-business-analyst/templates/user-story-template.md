---
title: User Story Template
module: Salesforce Business Analyst
category: Template
document_type: Template
version: 1.1.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/output-framework.md, salesforce-business-analyst/brain/validation-framework.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/user-stories.md]
related_examples: [examples/sample-brd/brd-excerpt.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/templates/README.md]
keywords: [user story template]
tags: [user-story-template]
---

# User Story Template

---
title: User Story Pack
type: user-story
version: 0.1.0
status: draft
last_updated: YYYY-MM-DD
project: PRJ-XXX-001
epic: EP-XXX
---

# User Story: [EP-XXX Epic Title]

## Epic Statement

**Outcome:** [Measurable business outcome for this epic]

**Requirement refs:** BR-xxx, BR-yyy

---

### US-XXX: [Short descriptive title]

**As a** [persona / role],
**I want** [goal / capability],
**So that** [business benefit].

**Requirement refs:** BR-xxx, FR-xxx

**Priority:** Must / Should / Could

**Acceptance criteria:**

1. Given [context], when [action], then [observable result].
2. Given [negative context], when [action], then [expected handling].
3. Given [permission context], when [action], then [access result].

**Data considerations:** [Objects, fields, record types]

**Integration considerations:** [If applicable]

**Definition of Done:**

- [ ] Acceptance criteria met in target sandbox
- [ ] Security review for new fields/objects
- [ ] Test scenarios TS-xxx linked
- [ ] Release notes drafted

**Notes / Open items:**

---

[Repeat per story]

## Story Splitting Checklist

If story feels large, split by:

- [ ] Workflow path (happy vs exception)
- [ ] User role
- [ ] Data variation (record type)
- [ ] CRUD operation
- [ ] Interface (internal vs portal)

## Related Brain Modules

- [Output Framework](../brain/output-framework.md)
- [Validation Framework](../brain/validation-framework.md)

## Related Knowledge

- [Readme](../knowledge/README.md)

## Related Templates

- [Readme](README.md)

## Related Playbooks

- [Readme](../playbooks/README.md)

## Related Industry Scenarios

- [Readme](../scenarios/README.md)

## Related Interview Topics

- [User Stories](../interview-guide/user-stories.md)

## Related Examples

- [Brd Excerpt](../../examples/sample-brd/brd-excerpt.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Knowledge, BRD/FRD | **Downstream:** Playbooks, user stories, RTM | **Validation:** validation-framework.md

## Navigation

- **Previous:** [Traceability Matrix Template](traceability-matrix-template.md)
- **Next:** [Vision Document Template](vision-document-template.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
