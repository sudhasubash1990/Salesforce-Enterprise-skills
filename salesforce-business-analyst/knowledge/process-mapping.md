---
title: Process Mapping
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
related_interview_topics: [salesforce-business-analyst/interview-guide/current-state.md, salesforce-business-analyst/interview-guide/advanced/whiteboard-exercises.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/knowledge/README.md]
keywords: [process mapping]
tags: [process-mapping, as-is, to-be, sipoc]
review-cycle: quarterly
salesforce-cloud: Platform
---

# Process Mapping

## Overview

AS-IS and TO-BE process documentation—swimlanes, SIPOC, and value streams for Salesforce programs.

## Purpose

Make workflow explicit so requirements reflect real handoffs, exceptions, and system touchpoints.

## Why It Matters

Undocumented processes produce wrong automation, missed integrations, and adoption failure.

## Business Context

Process maps align stakeholders on current pain and future workflow before configuration.

## Salesforce Context

Maps show where Salesforce replaces, integrates with, or orchestrates across ERP, marketing, and portals.

## Core Concepts

| Technique | Use when |
|-----------|----------|
| Swimlanes | Role-based handoffs |
| SIPOC | Scoping supplier/input/output/customer |
| Value stream | End-to-end lead/case/order flow |
| AS-IS | Document today with pain annotations |
| TO-BE | Target workflow with automation notes |

## Key Terminology

See [../../shared/glossary.md](../../shared/glossary.md) — AS-IS, TO-BE, process owner.

## Frameworks and Models

- [../templates/process-map.md](../templates/process-map.md)
- Complex flows: [bpmn.md](bpmn.md)

## Enterprise Best Practices

- Map happy path and top exceptions
- Annotate systems on each step
- Timebox mapping workshops; defer edge cases to parking lot

## Common Mistakes

- Over-detail before prioritization
- Maps without validated pain points

## Anti-Patterns

- TO-BE map before AS-IS agreement
- Maps that nobody maintains post-go-live

## Decision Guidelines

Use SIPOC at kickoff; swimlanes for BRD; BPMN when gateways and events are complex.

## Real-World Examples

Lead-to-opportunity handoff swimlane: marketing → SDR → AE → ERP quote.

## Industry Considerations

Healthcare: clinical vs administrative swimlanes; compliance checkpoints as process steps.

## AI Guidance

Reference process-map template when user asks for AS-IS/TO-BE. Link steps to BR themes.

## Review Checklist

- [ ] Roles labeled in swimlanes
- [ ] Systems identified per step
- [ ] Pain points linked to steps

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
- [Whiteboard Exercises](../interview-guide/advanced/whiteboard-exercises.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Brain modules | **Downstream:** Templates, playbooks, deliverables | **Validation:** checklists.md

## Navigation

- **Previous:** [Prioritization Techniques](prioritization-techniques.md)
- **Next:** [Release Management](release-management.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
