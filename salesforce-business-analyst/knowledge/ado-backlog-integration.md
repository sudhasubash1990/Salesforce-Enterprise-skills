---
title: Azure DevOps Backlog Integration
module: Salesforce Business Analyst
category: Knowledge
document_type: Knowledge Article
version: 1.0.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
difficulty: intermediate
industry: all
related_brain_modules: [salesforce-business-analyst/brain/output-framework.md, salesforce-business-analyst/brain/anti-hallucination.md, salesforce-business-analyst/brain/identity.md]
related_knowledge: [salesforce-business-analyst/knowledge/user-stories.md, salesforce-business-analyst/knowledge/acceptance-criteria.md]
related_templates: [salesforce-business-analyst/templates/user-story-template.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/user-stories.md]
related_examples: [examples/sample-user-story/dealer-portal-stories.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/knowledge/README.md]
keywords: [azure devops, ado, backlog, work items, story points, estimation]
tags: [azure-devops, ado, backlog, user-stories, estimation]
review-cycle: quarterly
salesforce-cloud: Platform
---

# Azure DevOps Backlog Integration

## Overview

Guidance for publishing Salesforce BA user stories to Azure DevOps (ADO) work items—field mapping, estimation discipline, deliverable ownership, and acceptance criteria formatting for stakeholder readability.

## Purpose

Prevent common ADO publishing mistakes: invisible acceptance criteria, premature story-point assignment, and unclear implementation deliverables.

## Work Item Type Selection

| Work item type | When to use | Acceptance Criteria visibility |
|----------------|-------------|--------------------------------|
| **User Story** | Agile process; AC field renders on form | Native `Acceptance Criteria` field visible |
| **Task** | Basic process or team convention uses Task for stories | `Acceptance Criteria` field may **not render** on the Task form—even when populated |

**Rule:** When creating a **Task** that carries user-story content, **always embed Acceptance Criteria in `System.Description`** (in addition to populating `Microsoft.VSTS.Common.AcceptanceCriteria` when the field exists). Stakeholders review the Description tab; hidden fields cause false "missing AC" feedback.

## ADO Field Mapping (Typical)

| BA content | ADO field | Format |
|------------|-----------|--------|
| Title | `System.Title` | `<Capability> - <Action>` |
| User story + business context + rules + estimation + deliverables | `System.Description` | HTML (`<h2>`, `<ul>`, `<table>`) |
| Acceptance criteria (Gherkin) | `Microsoft.VSTS.Common.AcceptanceCriteria` | HTML nested bullets; **also** duplicate in Description for Task type |
| Business priority | `Microsoft.VSTS.Common.Priority` | 1–4 (org-specific scale) |
| Story points | `Microsoft.VSTS.Scheduling.StoryPoints` | **Defer to team** — see Estimation section |
| Tags | `System.Tags` | Semicolon-separated (e.g., `ServiceCloud; Case`) |

Multi-line fields must use valid HTML. Avoid CDATA. Test with a minimal patch if large HTML payloads fail validation.

## Estimation Discipline (BA vs Team)

Story points measure **relative size** (complexity + effort + uncertainty)—**not** hours, days, or months. Calendar duration is derived from team **velocity** after refinement.

| Role | Owns | Does not own |
|------|------|--------------|
| **BA** | T-shirt size (XS/S/M/L/XL); estimation-input table; splittability note; risks/dependencies | Final story-point number |
| **Delivery team** | Story points at backlog refinement / planning poker | BA artifact authorship |

### BA estimation section (required in Description)

Include this block in every ADO user story or story-task:

```markdown
## Estimation (BA Input — Team to Confirm at Refinement)

**T-shirt size:** M (Medium)

**Story points:** Not finalized — delivery team to assign during backlog refinement / planning poker.

**Note:** Story points are a relative measure of complexity, effort, and uncertainty — not hours, days, or months.

| Estimation input | Assessment |
|------------------|------------|
| Solution approach | Standard/Config/Extend (from fit-gap) |
| Complexity | Low / Medium / High |
| Uncertainty / risk | List TBC items |
| Dependencies | Upstream/downstream |
| Splittability | Can split by workflow, role, or interface if oversized |
```

**Do not** populate `Microsoft.VSTS.Scheduling.StoryPoints` unless the user explicitly requests a provisional value—and label it *indicative, pending planning poker* in Description. Prefer leaving Story Points empty until refinement.

See [anti-hallucination.md](../brain/anti-hallucination.md) — assigning exact story points without team input is a red flag.

## Deliverables: BA vs Implementation Team

Clarify **who produces what**. A story point or t-shirt size does **not** list deliverables by itself—the story body must.

### BA deliverables (in scope for the BA / this work item)

- User story statement (As a / I want / So that)
- Acceptance criteria (testable, Given/When/Then)
- Business rules, assumptions, out-of-scope
- Field requirements and objects impacted
- Security/permission matrix (persona level)
- Estimation inputs (t-shirt + rationale)
- **Deliverables expected** section for the implementation team

### Implementation team deliverables (document in story, built by dev/admin)

| Category | Examples (Salesforce) |
|----------|----------------------|
| Data model | Record types, custom fields, picklists |
| UX | Page layouts, Lightning pages, validation rules |
| Automation | Flows, email templates, assignment rules |
| Reporting | Reports, dashboards |
| Security | Profiles, permission sets, sharing updates |
| Evidence | Sandbox test results against AC, release notes |

**Template phrase:** *"Deliverables Expected (Implementation Team)"* — bullet list of configuration/build artifacts the story implies. Do not conflate with BA document deliverables.

## Acceptance Criteria Format for ADO

Use **nested bullet lists** in HTML for readability (not single paragraphs):

```html
<h2>Acceptance Criteria</h2>
<ul>
  <li><b>AC1 — Happy path:</b>
    <ul>
      <li><b>Given</b> …</li>
      <li><b>When</b> …</li>
      <li><b>Then</b> …</li>
      <li><b>And</b> …</li>
    </ul>
  </li>
</ul>
```

Minimum: 3 AC covering happy path, validation/error, and permission (when applicable). See [acceptance-criteria.md](acceptance-criteria.md).

## Definition of Done

Story-level DoD includes:

- All AC validated in target sandbox
- Implementation deliverables deployed and tested
- Security review for new fields/objects/permissions
- **Story points assigned by delivery team at refinement** (if not done earlier)

## Common Mistakes

| Mistake | Correction |
|---------|------------|
| AC only in hidden field on Task | Duplicate AC in Description |
| "Story Points: 5" with no team sizing | T-shirt + estimation inputs; defer points |
| Story points interpreted as hours | Add explicit note in Estimation section |
| No implementation deliverables listed | Add "Deliverables Expected (Implementation Team)" |
| AC as dense paragraphs | Use nested Given/When/Then bullets |

## Local Artifact Save (Mandatory Before API Call)

Before calling the ADO API to create or update a work item:

1. Save the complete story pack as a `.md` file under `outputs/<project-folder>/03-requirements/user-stories/`
2. Run `python output-engine/convert.py --file <path-to.md>` to generate the office format
3. Only then proceed with the ADO API call
4. After successful creation, update the local `.md` with the ADO work item ID

This ensures a recoverable local copy exists if the API fails and maintains the output pipeline per `output-generation.mdc`.

## AI Agent Checklist (ADO Publish)

- [ ] Brain-Loading Compliance Checklist satisfied (see `checklists.md`)
- [ ] Pre-delivery validation run (validation-framework + anti-hallucination + checklists)
- [ ] Local `.md` artifact saved and output engine conversion run
- [ ] Work item type confirmed (User Story vs Task)
- [ ] Description includes full story pack + Estimation + Deliverables Expected
- [ ] AC in nested bullet HTML in Description (required for Task)
- [ ] AC field populated when supported
- [ ] Story Points empty or marked indicative only
- [ ] Tags and Priority set per business criticality
- [ ] Return real work item ID or actual API error (never fabricate IDs)

## Related Brain Modules

- [Identity](../brain/identity.md) — BA vs implementation scope
- [Anti-Hallucination](../brain/anti-hallucination.md) — estimation red flags
- [Output Framework](../brain/output-framework.md)

## Related Knowledge

- [User Stories](user-stories.md)
- [Acceptance Criteria](acceptance-criteria.md)

## Related Templates

- [User Story Template](../templates/user-story-template.md)

## Related Playbooks

- [Story Refinement Playbook](../playbooks/story-refinement-playbook.md)
- [Backlog Grooming Playbook](../playbooks/backlog-grooming-playbook.md)

## Related Industry Scenarios

- [Readme](../scenarios/README.md)

## Related Interview Topics

- [User Stories](../interview-guide/user-stories.md)

## Related Examples

- [Service Cloud Complaint Story](../../examples/sample-user-story/service-cloud-complaint-story.md)
- [Dealer Portal Stories](../../examples/sample-user-story/dealer-portal-stories.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | BA Practice Lead | ADO field mapping, estimation discipline, deliverable ownership, AC formatting (from Task 9 lessons) |
