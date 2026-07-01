---
title: Raid Log Template
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
keywords: [raid log template]
tags: [raid-log-template]
---

# RAID Log Template

---
title: RAID Log
type: raid
version: 0.1.0
status: draft
last_updated: YYYY-MM-DD
project: PRJ-XXX-001
author:
tags: [salesforce, raid, governance]
---

# RAID Log

## Document Control

| Field | Value |
|-------|-------|
| Project | PRJ-XXX-001 |
| Version | 0.1.0 |
| Last updated | YYYY-MM-DD |
| Review frequency | Weekly / Bi-weekly steering |

## Risks

| ID | Description | Impact | Likelihood | Mitigation | Owner | Status | Review date |
|----|-------------|--------|------------|------------|-------|--------|-------------|
| R-001 | If [event], then [impact on outcome/timeline] | High/Med/Low | High/Med/Low | [Action] | [Role] | Open / Mitigated / Closed | |

**Entry pattern:** If [event], then [impact]. Mitigation: [action]. Owner: [role].

## Assumptions

| ID | Assumption | Validate by | Owner | Status | Linked req |
|----|------------|-------------|-------|--------|------------|
| A-001 | We assume [statement] | [date/milestone] | [role] | Open / Validated / Invalidated | BR-xxx |

**Entry pattern:** We assume [statement]. Validate by [date/milestone].

## Issues

| ID | Description | Impact | Resolution | Owner | Target date | Status |
|----|-------------|--------|------------|-------|-------------|--------|
| I-001 | [Problem] | | [Action] | [role] | | Open / Resolved |

## Dependencies

| ID | Dependency | Provider | Deliverable needed | Needed by | Impact if late | Status |
|----|------------|----------|-------------------|-----------|----------------|--------|
| DEP-001 | [Team/system] must deliver [artifact] | [Team] | [Artifact] | [date] | [impact] | Open / Met |

## Escalation Log

| Date | Item ID | Escalated to | Outcome |
|------|---------|--------------|---------|
| | | | |

## Review Checklist

- [ ] Material risks have mitigation and owner
- [ ] Assumptions have validation date and owner
- [ ] Dependencies have needed-by date
- [ ] Linked to requirements where applicable
- [ ] No PII or client-specific identifiers

Pattern reference: [reusable-components.md](../../shared/reusable-components.md#raid-entry-templates)

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

- **Previous:** [Raci Template](raci-template.md)
- **Next:** [Risk Register Template](risk-register-template.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
