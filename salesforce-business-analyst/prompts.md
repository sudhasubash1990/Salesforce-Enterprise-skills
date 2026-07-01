---
title: Prompts
module: Salesforce Business Analyst
category: Root
document_type: Guide
version: 1.1.0
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
keywords: [prompts]
tags: [prompts]
---

# Prompts

Reusable prompts for human practitioners and AI agents.

## Discovery

```
Act as a senior Salesforce BA. I am starting discovery for a [industry] client implementing [clouds].

Context: [brief description]

Produce:
1. Stakeholder map with RACI
2. Top 10 discovery questions for executive interviews
3. 4-hour workshop agenda
4. Initial RAID log (5 items each category)

Flag assumptions. Do not invent regulatory requirements.
```

## BRD Section

```
Using the BRD template in salesforce-business-analyst/templates/brd-template.md,
draft sections 1-4 and business requirements BR-001 through BR-010 for:

Project: [name]
Industry: [industry]
Drivers: [list]
In scope: [list]
Out of scope: [list]

Each BR needs priority, success measure, and owner role.
```

## User Stories from BRD

```
Convert the following business requirements into epics and user stories with Given/When/Then acceptance criteria:

[paste BRs]

Rules: INVEST, 3+ AC per story, permission scenarios, requirement_refs, data notes.
Split epics larger than 8 stories.
```

## Fit-Gap

```
Perform fit-gap analysis for these requirements against Salesforce [clouds]:

[paste requirements]

Classify each as Standard/Config/Extend/Gap/Defer.
Reference standard features. Propose recommendation and effort (S/M/L).
Flag licensing implications.
```

## Process Map

```
Document AS-IS and TO-BE mermaid flowcharts for process: [name]

Systems: Salesforce [clouds], [integrations]
Include pain points table and requirement refs for TO-BE changes.
```

## UAT Scenarios

```
Create UAT test scenarios (TS-xxx) for these user stories:

[paste stories]

Format: steps, expected results, tester role, pass/fail.
Cover all acceptance criteria. 100% Must coverage.
```

## Backlog Refinement

```
Review these user stories for INVEST compliance and testable AC.
List failures and rewritten versions:

[paste stories]
```

## Scope Change Impact

```
A change request asks to: [description]

Assess impact on:
- BR/FR affected
- Stories to add/modify
- Integration and security
- Timeline risk

Recommend: accept, defer, or reject with rationale.
```

## Workshop Facilitation

```
I am facilitating a TO-BE envisioning workshop for [process] with [roles].

Provide:
- Facilitation script (opening, activities, closing)
- Dot-vote prioritization instructions
- Parking lot template
- Note-taking structure aligned to BRD
```

## Anti-Pattern Review

```
Review this requirement/story for BA anti-patterns (screen specs, non-testable AC, missing permissions, epic-as-story):

[paste content]

Provide corrected version.
```

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

- **Previous:** [Interview Guide](interview-guide.md)
- **Next:** [References](references.md)
- **See Also:** [skill.md](skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
