---
title: Process Map
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
keywords: [process map]
tags: [process-map]
---

# Process Map Template

---
title: Process Map
type: process-map
version: 0.1.0
status: draft
last_updated: YYYY-MM-DD
project: PRJ-XXX-001
---

# Process: [Process Name]

## Overview

| Field | Value |
|-------|-------|
| Process owner | |
| Trigger | |
| Outcome | |
| Systems involved | Salesforce, [others] |

## AS-IS Process

```mermaid
flowchart TD
    A[Start: Trigger event] --> B[Step 1]
    B --> C{Decision?}
    C -->|Yes| D[Step 2a]
    C -->|No| E[Step 2b]
    D --> F[End]
    E --> F
```

### AS-IS Pain Points

| Step | Pain Point | Impact |
|------|------------|--------|
| | | |

## TO-BE Process

```mermaid
flowchart TD
    A[Start: Trigger event] --> B[Salesforce: Step 1]
    B --> C{Automation / Decision}
    C -->|Path A| D[Step 2a]
    C -->|Path B| E[Integration to ERP]
    D --> F[End]
    E --> F
```

### TO-BE Changes

| Step | Change | Requirement Ref |
|------|--------|-----------------|
| | | BR-xxx |

## Swimlane (Optional)

| Step | Sales Rep | System | Manager | Integration |
|------|-----------|--------|---------|-------------|
| 1 | | | | |
| 2 | | | | |

## Metrics

| Metric | AS-IS | TO-BE Target |
|--------|-------|--------------|
| Cycle time | | |
| Error rate | | |
| Manual touchpoints | | |

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

- **Previous:** [Process Flow Template](process-flow-template.md)
- **Next:** [Raci Template](raci-template.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
