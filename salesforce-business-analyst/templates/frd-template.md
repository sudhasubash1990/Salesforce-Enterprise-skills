---
title: Frd Template
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
keywords: [frd template]
tags: [frd-template]
---

# FRD Template

---
title: Functional Requirements Document
type: frs
version: 0.1.0
status: draft
last_updated: YYYY-MM-DD
project: PRJ-XXX-001
author:
tags: [salesforce, frd, functional-requirements]
clouds: [Sales Cloud, Service Cloud]
industry:
parent_id: BRD-version-ref
---

# Functional Requirements Document

## Document Control

| Field | Value |
|-------|-------|
| Version | 0.1.0 |
| Status | Draft |
| Parent BRD | [BRD title, version] |
| Prepared by | |
| Reviewed by | |

## 1. Purpose

[Link to business objectives from BRD; scope of this FRD]

## 2. Scope

### 2.1 In Scope

- [Functional areas covered]

### 2.2 Out of Scope

- [Explicit exclusions]

### 2.3 Assumptions

| ID | Assumption | Validate by | Owner |
|----|------------|-------------|-------|
| A-001 | | | |

## 3. Actors and Personas

| Persona | Salesforce profile / role | Description |
|---------|---------------------------|-------------|
| | | |

## 4. Functional Requirements

### 4.1 [Capability Area]

#### FR-001: [Short title]

| Attribute | Value |
|-----------|-------|
| ID | FR-001 |
| Parent BR | BR-xxx |
| Priority | Must / Should / Could / Won't |
| Category | Functional |
| Source | workshop / interview / assumption |

**Description:** [Testable system behaviour in business terms]

**Business rules:**

- When [condition], the system must [behaviour], except when [exception].

**Preconditions:** [State before trigger]

**Postconditions:** [State after successful completion]

**Salesforce context (high level):** [Object, feature area—e.g., Case, Flow, Experience Cloud]

**Acceptance criteria:**

1. Given [context], when [action], then [result].
2. Given [negative path], when [action], then [result].

**Data considerations:** [Fields, volumes, ownership]

**Security / permissions:** [Who can view/edit; sharing notes]

**Integration:** [Inbound/outbound events if applicable]

**Open questions:**

- [TBC items]

---

[Repeat FR-xxx blocks]

## 5. Non-Functional Requirements

| ID | Category | Requirement | Target | Source |
|----|----------|-------------|--------|--------|
| NFR-001 | Performance | | | |
| NFR-002 | Availability | | | |
| NFR-003 | Security | | | |
| NFR-004 | Usability | | | |
| NFR-005 | Data | | | |

## 6. Integration Requirements

| ID | Event / Entity | Source | Target | Direction | SLA / Volume |
|----|----------------|--------|--------|-----------|--------------|
| INT-001 | | | | | |

## 7. Reporting and Analytics

| Report / Dashboard | Audience | Key metrics | Source objects |
|------------------|----------|-------------|----------------|
| | | | |

## 8. Traceability

| FR ID | BR ID | User Story (planned) | Fit-Gap class |
|-------|-------|----------------------|---------------|
| FR-001 | BR-xxx | US-xxx | Standard / Config / Extend / Gap |

## 9. RAID Summary

| Type | ID | Description | Owner | Status |
|------|-----|-------------|-------|--------|
| Risk | R-001 | | | |
| Assumption | A-001 | | | |
| Issue | I-001 | | | |
| Dependency | DEP-001 | | | |

## 10. Approval

| Role | Name | Signature / Date |
|------|------|------------------|
| Business Owner | | |
| BA Lead | | |
| Solution Architect | | |

## Review Checklist

- [ ] Each FR is testable with actor, trigger, and outcome
- [ ] Linked to parent BR IDs
- [ ] Permissions and negative paths addressed
- [ ] No duplicate IDs
- [ ] Assumptions and TBC items documented
- [ ] Terminology matches [glossary](../../shared/glossary.md)

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

- **Previous:** [Feature Template](feature-template.md)
- **Next:** [Future State Template](future-state-template.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
