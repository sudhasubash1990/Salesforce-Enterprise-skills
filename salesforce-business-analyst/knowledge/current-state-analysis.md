---
title: Current State Analysis
module: Salesforce Business Analyst
category: Knowledge
document_type: Knowledge Article
version: 0.3.0
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
related_interview_topics: [salesforce-business-analyst/interview-guide/current-state.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/knowledge/README.md]
keywords: [current state analysis]
tags: [current-state, as-is, discovery]
review-cycle: quarterly
salesforce-cloud: Platform
---

# Current State Analysis

## Overview

Methods for documenting AS-IS processes, systems landscape, pain points, and constraints.

## Purpose

Establish a validated baseline before TO-BE design and Salesforce fit-gap.

## Why It Matters

Future state built on assumed current state drives rework and integration surprises.

## Business Context

Current state captures how work actually happens—not only policy manuals.

## Salesforce Context

Inventory CRM, ERP, portals, spreadsheets, and integration points affecting Salesforce scope.

## Core Concepts

**Inputs:** interviews, observation, document analysis, system demos

**Outputs:**

- AS-IS process notes and maps
- Pain point list (ranked)
- Systems landscape diagram
- Data quality themes
- Constraint list

**Techniques:** shadow users, follow-a-record, artifact review

## Key Terminology

| Term | Definition |
|------|------------|
| Pain point | Friction reducing outcome |
| Workaround | Informal process compensating for system gap |

## Frameworks and Models

Discovery playbook timeline; SIPOC for scope—see [process-mapping.md](process-mapping.md).

## Enterprise Best Practices

- Triangulate: interview + observation + data
- Rank pains by frequency and impact
- Capture quotes as evidence (anonymized)

## Common Mistakes

- Single-stakeholder AS-IS
- Stated process ≠ observed process

## Anti-Patterns

- Skipping legacy integration discovery
- AS-IS documentation without pain linkage

## Decision Guidelines

Spend more discovery time on high-volume and regulated processes.

## Real-World Examples

Discovery workshop notes: top 5 pains, ERP as Account source of truth, dealer calls for status.

## Industry Considerations

Manufacturing: dealer channel often under-documented in HQ-centric AS-IS.

## AI Guidance

Reasoning Stage 6. Ask clarifying questions before inventing AS-IS detail.

## Review Checklist

- [ ] Pain points ranked
- [ ] Systems identified
- [ ] Sources cited (workshop, interview)

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

- [Current State](../interview-guide/current-state.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Brain modules | **Downstream:** Templates, playbooks, deliverables | **Validation:** checklists.md

## Navigation

- **Previous:** [Constraints Management](constraints-management.md)
- **Next:** [Data Migration](data-migration.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
