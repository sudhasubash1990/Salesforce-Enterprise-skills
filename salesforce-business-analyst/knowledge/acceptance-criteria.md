---
title: Acceptance Criteria
module: Salesforce Business Analyst
category: Knowledge
document_type: Knowledge Article
version: 0.4.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
difficulty: foundational
industry: all
related_brain_modules: [salesforce-business-analyst/brain/reasoning-framework.md, salesforce-business-analyst/brain/output-framework.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/acceptance-criteria.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/knowledge/README.md]
keywords: [acceptance criteria]
tags: [acceptance-criteria, bdd, testing, invest]
review-cycle: quarterly
salesforce-cloud: Platform
---

# Acceptance Criteria

## Overview

Testable acceptance criteria using Given/When/Then—positive, negative, permission, and validation scenarios.

## Purpose

Define "done" for user stories and functional requirements in a way QA and business can execute.

## Why It Matters

Untestable AC is the primary cause of UAT failure and production defect leakage on Salesforce programs.

## Business Context

AC translate requirements into verifiable conditions agreed by PO and delivery team.

## Salesforce Context

Include profile/permission set, record type, sharing, validation rules, Flow triggers, and integration mocks where relevant.

## Core Concepts

**Given/When/Then format:**

```
Given [precondition and data state]
When [action by actor]
Then [observable outcome]
```

**Readable format (preferred for ADO and stakeholder review):** use nested bullets per scenario—not dense paragraphs.

```markdown
- **AC1 — Happy path:**
  - **Given** [context]
  - **When** [action]
  - **Then** [outcome]
  - **And** [additional outcome]
```

For Azure DevOps HTML, use nested `<ul>` / `<li>` with **Given**, **When**, **Then**, **And** labels. See [ado-backlog-integration.md](ado-backlog-integration.md).

### ADO HTML Rendering Example

When publishing AC to ADO `System.Description` or `Microsoft.VSTS.Common.AcceptanceCriteria`, use this nested list structure:

```html
<h2>Acceptance Criteria</h2>
<ul>
  <li><b>AC1 — Happy path: create complaint</b>
    <ul>
      <li><b>Given</b> a Customer Service Agent is logged into Service Cloud</li>
      <li><b>And</b> the agent has permission to create Cases</li>
      <li><b>When</b> the agent creates a complaint with all required fields</li>
      <li><b>Then</b> a Case record is saved successfully</li>
      <li><b>And</b> Status defaults to "New"</li>
    </ul>
  </li>
  <li><b>AC2 — Validation: missing required field</b>
    <ul>
      <li><b>Given</b> a Customer Service Agent is creating a complaint</li>
      <li><b>When</b> any required field is missing</li>
      <li><b>Then</b> the complaint cannot be saved</li>
      <li><b>And</b> a clear validation message identifies the missing field(s)</li>
    </ul>
  </li>
  <li><b>AC3 — Permission: agent cannot delete</b>
    <ul>
      <li><b>Given</b> a Customer Service Agent views an existing complaint</li>
      <li><b>When</b> the agent attempts to delete the complaint</li>
      <li><b>Then</b> the action is denied or unavailable</li>
    </ul>
  </li>
</ul>
```

**Do NOT** use `<p>` with `<br/>` for Given/When/Then lines — this renders as dense paragraphs in ADO and is hard to scan. Always use nested `<ul><li>`.

**Scenario types:**

| Type | Example |
|------|---------|
| Positive | Happy path case creation |
| Negative | Missing required field blocked |
| Permission | User without edit cannot change Status |
| Boundary | Attachment at max size rejected |
| Integration | ERP sync updates Account within SLA |

**Definition of Done:** Sprint DoD (code, tests, review) vs story AC (functional behaviour).

## Key Terminology

| Term | Definition |
|------|------------|
| AC | Acceptance criteria |
| DoD | Definition of Done (team agreement) |
| Test scenario | UAT execution script (TS-xxx) |

## Frameworks and Models

Map AC to UAT scenarios via [../templates/traceability-matrix-template.md](../templates/traceability-matrix-template.md).

## Enterprise Best Practices

- Minimum 3 AC per story
- Test data states documented
- Error messages specified where UX matters
- Link AC to TS IDs for Must-have stories

## Common Mistakes

- "Verify page loads" as sole AC
- AC that describe implementation (Apex class names)
- No negative path
- Single-paragraph AC blocks that are hard to scan in ADO or backlog tools

## Anti-Patterns

- Subjective AC ("user-friendly", "fast")
- AC untraceable to requirement ID

## Decision Guidelines

Complex rules: separate AC per rule variation. Bulk behaviour: dedicated AC with volume note.

## Real-World Examples

Dealer portal story: submit case with attachment; missing required fields; unauthorized profile denied.

## Industry Considerations

Audit trail requirements: AC for field history and who changed regulated fields.

## AI Guidance

Generate AC before closing story. Run [../brain/validation-framework.md](../brain/validation-framework.md) testability check.

## Review Checklist

- [ ] Given/When/Then structure
- [ ] Positive and negative covered
- [ ] Permissions addressed if applicable

## Related Brain Modules

- [Reasoning Framework](../brain/reasoning-framework.md)
- [Output Framework](../brain/output-framework.md)

## Related Knowledge

- [Readme](README.md)

## Related Templates

- [Readme](../templates/README.md)

## Related Playbooks

- [Readme](../playbooks/README.md)

## Related Industry Scenarios

- [Readme](../scenarios/README.md)

## Related Interview Topics

- [Acceptance Criteria](../interview-guide/acceptance-criteria.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Brain modules | **Downstream:** Templates, playbooks, deliverables | **Validation:** checklists.md

## Navigation

- **Previous:** [Readme](README.md)
- **Next:** [Ai In Business Analysis](ai-in-business-analysis.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.4.0 | 2026-07-02 | BA Practice Lead | Nested bullet AC format; ADO readability guidance |
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
