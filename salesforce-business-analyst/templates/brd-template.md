---
title: Business Requirements Document
module: Salesforce Business Analyst
category: Template
document_type: Business Requirements Document
version: 0.4.0
review_status: Draft
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: YYYY-MM-DD
review_cycle: quarterly
industry: 
related_brain_modules: [salesforce-business-analyst/brain/output-framework.md, salesforce-business-analyst/brain/validation-framework.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/user-stories.md]
related_examples: [examples/sample-brd/brd-excerpt.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/templates/README.md]
keywords: [brd template]
tags: [salesforce, brd]
template-id: brd
last-reviewed: 2026-07-02
review-cycle: quarterly
salesforce-cloud: Sales Cloud, Service Cloud
project: PRJ-XXX-001
author: 
---

# Business Requirements Document

## Purpose

Authoritative business needs, scope, and success criteria for Salesforce programs.

## When to Use

After discovery workshops; before detailed FRD and agile backlog decomposition.

## Intended Audience

Sponsor, business owners, BA, architect, PM.

## Prerequisites

Discovery summary, stakeholder map, initial RAID.

## Inputs

Workshop notes, AS-IS/TO-BE themes, capability map.

## Completion Instructions

1. Complete document control and metadata.
2. Assign BR-xxx IDs; apply MoSCoW.
3. Document assumptions, constraints, dependencies, out-of-scope.
4. Run [../checklists.md](../checklists.md) BRD gate.

---

## Document Control

| Field | Value |
|-------|-------|
| Version | 0.1.0 |
| Status | Draft |
| Prepared by | |
| Approved by | |

## 1. Executive Summary

[2–3 paragraphs: problem, proposed solution, expected outcomes]

## 2. Business Objectives

| ID | Objective | Success Metric | Target |
|----|-----------|----------------|--------|
| OBJ-001 | | | |

## 3. Scope

### 3.1 In Scope

-

### 3.2 Out of Scope

-

### 3.3 Dependencies

-

## 4. Stakeholders

| Role | Name | Responsibility |
|------|------|----------------|
| Executive Sponsor | | |
| Product Owner | | |

## 5. Assumptions

| ID | Assumption | Validate By |
|----|------------|-------------|
| A-001 | | |

## 6. Constraints

-

## 7. AS-IS Summary

[Current state processes and systems]

## 8. TO-BE Summary

[Future state capabilities]

## 9. Business Requirements

#### BR-001: [Title]

| Attribute | Value |
|-----------|-------|
| Priority | Must / Should / Could / Won't |
| Source | |
| Owner | |

**Statement:**

**Success measure:**

**Dependencies:**

---

[Repeat for each requirement]

## 10. Functional Requirements

#### FR-001: [Title]

| Attribute | Value |
|-----------|-------|
| Parent | BR-xxx |
| Priority | |

**Statement:** When [trigger], the system shall [behavior].

**Business rules:**

**Exceptions:**

## 11. Non-Functional Requirements

#### NFR-001: [Category — Performance / Security / etc.]

**Statement:**

**Measure:**

## 12. Integration Overview

| System | Direction | Entities | Frequency |
|--------|-----------|----------|-----------|
| | | | |

## 13. Reporting & Analytics

| Report / KPI | Audience | Source |
|--------------|----------|--------|
| | | |

## 14. Open Questions

| # | Question | Owner | Due |
|---|----------|-------|-----|
| 1 | | | |

## 15. Glossary

| Term | Definition |
|------|------------|
| | |

## 16. Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| | | | |

## Appendix A: Traceability Matrix (Initial)

| BR ID | FR ID | Epic | Notes |
|-------|-------|------|-------|
| | | | |

## Review Checklist

- [ ] Outcomes stated per BR; unique IDs; MoSCoW applied
- [ ] Out-of-scope section complete
- [ ] Assumptions and RAID linked

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

- **Previous:** [Assumption Log Template](assumption-log-template.md)
- **Next:** [Business Case Template](business-case-template.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
