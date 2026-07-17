---
title: Checklists
module: Salesforce Business Analyst
category: Root
document_type: Guide
version: 1.2.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/README.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/interview-index.md]
related_examples: [examples/sample-project/README.md]
related_documents: [docs/cross-linking-framework.md, ROADMAP.md]
keywords: [checklists]
tags: [checklists]
---

# BA Checklists

Quality gates for Salesforce Business Analyst deliverables.

## BRD Checklist

- [ ] Executive summary with measurable outcomes
- [ ] In scope and out of scope explicit
- [ ] Assumptions and constraints listed
- [ ] Each BR has unique ID, priority, source, owner
- [ ] Success measures on business requirements
- [ ] NFRs include security and performance where relevant
- [ ] Integration overview with direction and frequency
- [ ] Open questions have owners
- [ ] No client PII or confidential identifiers
- [ ] Terminology matches glossary

## User Story Checklist

- [ ] INVEST — story is splittable and valuable alone
- [ ] Role, goal, benefit present
- [ ] 3+ testable acceptance criteria (nested Given/When/Then bullets)
- [ ] Negative and permission scenarios included
- [ ] requirement_refs link to BR/FR
- [ ] Data and integration notes when applicable
- [ ] Not an epic (fits one sprint)
- [ ] Definition of Done stated
- [ ] T-shirt size and estimation inputs documented (story points deferred to team)
- [ ] Deliverables Expected (Implementation Team) section present
- [ ] BA deliverables distinguished from implementation build artifacts

## Azure DevOps Story Publish Checklist

- [ ] Work item type confirmed (User Story vs Task)
- [ ] Acceptance criteria visible in Description (required for Task type)
- [ ] Acceptance Criteria field populated when supported
- [ ] Story Points empty or marked indicative pending refinement
- [ ] Estimation section states points are not hours/days/months
- [ ] Real work item ID returned or actual API error reported

See [knowledge/ado-backlog-integration.md](knowledge/ado-backlog-integration.md).

## Fit-Gap Checklist

- [ ] Every Must/Should requirement classified
- [ ] Standard options explored before Extend/Gap
- [ ] Licensing flagged for Gap items
- [ ] Architect review for Extend/Gap
- [ ] Decisions recorded for pending items

## Workshop Checklist

- [ ] Objectives and agenda sent 48h ahead
- [ ] Right SMEs in room (not only managers)
- [ ] Notes distributed within 24h
- [ ] Requirements tagged with source
- [ ] Parking lot items tracked

## Discovery Exit Checklist

- [ ] Stakeholder RACI approved
- [ ] Top pain points validated by 2+ sources
- [ ] Systems inventory draft complete
- [ ] Scope hypothesis agreed with sponsor
- [ ] RAID log started

## UAT Readiness Checklist

- [ ] Test scenario per Must story
- [ ] Traceability matrix updated
- [ ] Test data and users provisioned
- [ ] Defect severity scale agreed
- [ ] Sign-off template prepared

## Brain-Loading Compliance Checklist (Sprint 10)

Run this BEFORE any other checklist. Failure here caused 4 rework cycles on Task-9.

- [ ] `identity.md` + `consulting-principles.md` loaded (any BA task)
- [ ] `reasoning-framework.md` loaded (any analysis)
- [ ] `decision-framework.md` loaded (if output contains fit-gap classification)
- [ ] `output-framework.md` + `communication-framework.md` loaded (if generating any deliverable)
- [ ] `validation-framework.md` + `anti-hallucination.md` loaded (before every response)
- [ ] `checklists.md` loaded (for artifact-specific gate — this file)
- [ ] Relevant Salesforce cloud knowledge loaded (e.g., `service-cloud-patterns.md` if Service Cloud mentioned)
- [ ] `salesforce-clouds-overview.md` loaded (if any specific cloud is referenced)
- [ ] `security-model.md` loaded (if permission/CRUD analysis is part of output)
- [ ] `shared/glossary.md` loaded (if terminology could be ambiguous)
- [ ] Relevant playbook loaded (e.g., `gap-analysis-playbook.md` if fit-gap produced)

## Agent Pre-Delivery Checklist

Run BEFORE first delivery — not after rework.

- [ ] Brain-Loading Compliance Checklist above is fully satisfied
- [ ] Loaded correct industry scenario (if applicable)
- [ ] Applied output standards
- [ ] Ran `validation-framework.md` quality gate
- [ ] Ran `anti-hallucination.md` claim check
- [ ] Assumptions section populated
- [ ] Open questions listed
- [ ] Suggested next steps included
- [ ] Local `.md` artifact saved under `outputs/<project>/` (if publishing externally)
- [ ] Output engine conversion run on local artifact

## Story Refinement (Grooming) Checklist

- [ ] Story understood by dev without BA present
- [ ] AC unambiguous to QA
- [ ] Dependencies identified
- [ ] Estimation complete or ready
- [ ] No open fit-gap for Must items

## Related Brain Modules

- [Readme](brain/README.md)

## Related Knowledge

- [Readme](knowledge/README.md)

## Related Templates

- [Readme](templates/README.md)

## Related Playbooks

- [Readme](playbooks/README.md)

## Related Industry Scenarios

- [Readme](scenarios/README.md)

## Related Interview Topics

- [Interview Index](interview-guide/interview-index.md)

## Related Examples

- [Readme](../examples/sample-project/README.md)

## Related Documents

- [Cross Linking Framework](../docs/cross-linking-framework.md)
- [Roadmap](../ROADMAP.md)

## Traceability

**Upstream:** — | **Downstream:** All skills | **Validation:** ROADMAP alignment

## Navigation

- **Previous:** [Changelog](CHANGELOG.md)
- **Next:** [Interview Guide](interview-guide.md)
- **See Also:** [skill.md](skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.2.0 | 2026-07-02 | BA Practice Lead | Estimation, deliverables, ADO publish checklist |
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
