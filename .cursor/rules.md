---
title: Rules
module: Salesforce Business Analyst
category: Governance
document_type: Framework
version: 1.1.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/interview-index.md]
related_examples: [examples/sample-project/README.md]
related_documents: [docs/metadata-schema.md, docs/cross-linking-framework.md]
keywords: [rules]
tags: [rules]
---

# Cursor Rules

Persistent rules for agent behavior in Salesforce Enterprise Skills.

## Rule 1: Skill-First Execution

For Salesforce BA tasks, always load `salesforce-business-analyst/skill.md` before producing deliverables. Load `brain/reasoning-framework.md` when analyzing requirements; load `brain/validation-framework.md` and `brain/anti-hallucination.md` before delivering output. Do not improvise formats when a template exists.

## Rule 2: Traceability

Maintain requirement IDs across documents. If a user story is derived from BRD requirement `BR-012`, reference it in the story metadata.

## Rule 3: INVEST User Stories

User stories must be:

- **I**ndependent
- **N**egotiable
- **V**aluable
- **E**stimable
- **S**mall
- **T**estable

Reject or refactor stories that are epics disguised as stories.

## Rule 4: Acceptance Criteria Quality

Acceptance criteria must be:

- Observable and verifiable
- Written in Given/When/Then or bullet checklist form
- Free of implementation prescription unless technically constrained
- Include negative paths and permission scenarios where relevant

## Rule 5: Fit-Gap Discipline

When evaluating Salesforce fit:

| Classification | Definition |
|----------------|------------|
| **Standard** | Native feature meets need with configuration |
| **Config** | Declarative customization (flows, validation, layouts) |
| **Extend** | Low-code (Apex, LWC) with clear boundary |
| **Gap** | Not achievable without third-party, integration, or process change |
| **Defer** | Valid need, out of current release scope |

## Rule 6: Document Metadata

Generated documents must include YAML frontmatter:

```yaml
---
title: Document Title
type: brd | user-story | workshop-notes | fit-gap | test-scenario
version: 0.1.0
status: draft | review | approved
author: agent | <human>
last_updated: YYYY-MM-DD
project: <anonymized-project-code>
---
```

## Rule 7: Progressive Disclosure

Keep responses concise. Link to playbooks and knowledge files for depth rather than inlining entire frameworks.

## Rule 8: Quality Gate

Before finalizing any deliverable, run the mental checklist in `salesforce-business-analyst/checklists.md`.

## Related Brain Modules

N/A — no direct relationships for this document type.

## Related Knowledge

- [Readme](../salesforce-business-analyst/knowledge/README.md)

## Related Templates

- [Readme](../salesforce-business-analyst/templates/README.md)

## Related Playbooks

- [Readme](../salesforce-business-analyst/playbooks/README.md)

## Related Industry Scenarios

- [Readme](../salesforce-business-analyst/scenarios/README.md)

## Related Interview Topics

- [Interview Index](../salesforce-business-analyst/interview-guide/interview-index.md)

## Related Examples

- [Readme](../examples/sample-project/README.md)

## Related Documents

- [Metadata Schema](../docs/metadata-schema.md)
- [Cross Linking Framework](../docs/cross-linking-framework.md)

## Traceability

**Upstream:** — | **Downstream:** All repository documents | **Validation:** validate_metadata.py

## Navigation

- **Previous:** [Routing](routing.md)
- **Next:** —
- **See Also:** [cross-linking-framework](../docs/cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
