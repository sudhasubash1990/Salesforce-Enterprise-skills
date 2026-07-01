---
title: Traceability Matrix Template
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
keywords: [traceability matrix template]
tags: [traceability-matrix-template]
---

# Traceability Matrix Template

---
title: Requirements Traceability Matrix
type: traceability
version: 0.1.0
status: draft
last_updated: YYYY-MM-DD
project: PRJ-XXX-001
author:
tags: [salesforce, traceability, rtm]
---

# Requirements Traceability Matrix (RTM)

## Document Control

| Field | Value |
|-------|-------|
| Project | PRJ-XXX-001 |
| Version | 0.1.0 |
| BRD reference | [version] |
| Last updated | YYYY-MM-DD |

## Traceability Matrix

| BR ID | FR ID | Epic | US ID | TS ID | Priority | Fit-Gap | Release | Status | Notes |
|-------|-------|------|-------|-------|----------|---------|---------|--------|-------|
| BR-001 | FR-001 | EP-001 | US-001 | TS-001 | Must | Standard | R1 | Proposed | |
| BR-001 | FR-002 | EP-001 | US-002 | TS-002 | Must | Config | R1 | Approved | |
| BR-002 | | EP-002 | US-010 | | Should | Extend | R2 | Deferred | Architect review |

## Status Values

| Status | Meaning |
|--------|---------|
| Proposed | Drafted, not yet approved |
| Approved | Accepted by business owner |
| In build | Development in progress |
| In test | QA / UAT in progress |
| Done | Released and accepted |
| Deferred | Out of current release |
| Rejected | Not proceeding |

## Coverage Summary

| Metric | Count |
|--------|-------|
| Total BR (Must) | |
| BR with ≥1 user story | |
| User stories with ≥1 test scenario | |
| Orphan user stories (no BR ref) | |
| Orphan test scenarios (no US ref) | |

**Target:** 100% Must BRs traced to stories; 100% Must stories traced to test scenarios before UAT.

## Change Log

| Date | Row(s) | Change | Author |
|------|--------|--------|--------|
| | | | |

## Review Checklist

- [ ] No duplicate IDs
- [ ] Every US has requirement_refs to BR or FR
- [ ] Must-priority items have test scenario or UAT plan
- [ ] Deferred items documented with rationale
- [ ] Updated after backlog or scope changes

Pattern reference: [reusable-components.md](../../shared/reusable-components.md#traceability-row)

UAT linkage: [uat-playbook.md](../playbooks/uat-playbook.md)

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

- **Previous:** [Stakeholder Matrix Template](stakeholder-matrix-template.md)
- **Next:** [User Story Template](user-story-template.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
