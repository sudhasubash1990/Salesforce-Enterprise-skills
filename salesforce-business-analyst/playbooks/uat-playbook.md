---
title: Uat Playbook
module: Salesforce Business Analyst
category: Playbook
document_type: Consulting Methodology
version: 1.1.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/reasoning-framework.md, salesforce-business-analyst/brain/enterprise-behaviors.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/advanced/scenario-questions.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/playbooks/README.md]
keywords: [uat playbook]
tags: [uat-playbook]
---

# UAT Playbook

> **Sprint 4:** Planning methodology in [uat-planning-playbook.md](uat-planning-playbook.md) and go-live in [production-readiness-playbook.md](production-readiness-playbook.md).

User Acceptance Testing planning and execution for Salesforce releases.

## UAT Principles

- Test **business scenarios**, not clicks
- Trace every test to requirement and user story
- Use production-like data (masked)
- Business owns sign-off; QA facilitates

## Phase Timeline

| Phase | Activity |
|-------|----------|
| T-4 weeks | UAT scope from release backlog |
| T-3 weeks | Test scenarios drafted from AC |
| T-2 weeks | Data setup, user provisioning |
| T-1 week | UAT kickoff, dry run |
| T week | Execution, defect triage |
| T+1 week | Sign-off or conditional go-live |

## Test Scenario Format

```markdown
### TS-018: Dealer submits case via portal

**Refs:** US-015, BR-005
**Priority:** Must
**Tester role:** Dealer User (test account)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Log in to dealer portal | Dashboard loads |
| 2 | Navigate to New Case | Form displays required fields |
| 3 | Submit without Category | Validation error shown |
| 4 | Complete valid submission | Case created; email received |

**Pass / Fail:** ___
**Defect ID:** ___
**Notes:**
```

## Coverage Matrix

| US ID | AC Count | TS Count | Coverage % |
|-------|----------|----------|------------|
| US-015 | 4 | 2 | 100% |

Target: 100% Must stories covered; Should ≥ 80%.

## Defect Severity (Business View)

| Severity | Definition |
|----------|------------|
| S1 | Cannot complete core business scenario |
| S2 | Workaround exists; material impact |
| S3 | Cosmetic or low impact |
| S4 | Enhancement request |

## Sign-Off Criteria

- [ ] All Must test scenarios Pass
- [ ] No open S1 defects
- [ ] S2 defects with agreed waiver from sponsor
- [ ] Training completed for affected roles
- [ ] Release notes distributed

## Sign-Off Form

| Release | Version | Date |
|---------|---------|------|
| | | |

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Product Owner | | | |
| Business Sponsor | | | |

## Post-UAT

- Feed defects into backlog (fix vs defer)
- Update traceability matrix status
- Capture lessons learned for next release

## Related Brain Modules

- [Reasoning Framework](../brain/reasoning-framework.md)
- [Enterprise Behaviors](../brain/enterprise-behaviors.md)

## Related Knowledge

- [Readme](../knowledge/README.md)

## Related Templates

- [Readme](../templates/README.md)

## Related Playbooks

- [Readme](README.md)

## Related Industry Scenarios

- [Readme](../scenarios/README.md)

## Related Interview Topics

- [Scenario Questions](../interview-guide/advanced/scenario-questions.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Knowledge, templates | **Downstream:** Scenarios, workshop outputs | **Validation:** checklists.md

## Navigation

- **Previous:** [Uat Planning Playbook](uat-planning-playbook.md)
- **Next:** [Value Stream Mapping Playbook](value-stream-mapping-playbook.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
