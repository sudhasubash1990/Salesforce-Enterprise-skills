---
title: Constraints Management
module: Salesforce Business Analyst
category: Knowledge
document_type: Knowledge Article
version: 0.3.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
difficulty: intermediate
industry: all
related_brain_modules: [salesforce-business-analyst/brain/reasoning-framework.md, salesforce-business-analyst/brain/output-framework.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/interview-index.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/knowledge/README.md]
keywords: [constraints management]
tags: [constraints, scope, governance]
review-cycle: quarterly
salesforce-cloud: Platform
---

# Constraints Management

## Overview

Budget, timeline, resource, technology, compliance, and organizational constraints on Salesforce programs.

## Purpose

Document fixed limits that shape fit-gap and release planning.

## Why It Matters

Ignoring constraints produces unachievable requirements and failed go-lives.

## Business Context

Constraints are non-negotiable boundaries unless sponsor approves change.

## Salesforce Context

Examples: org edition, license count, integration window, governor limits, data residency, mobile offline limits.

## Core Concepts

| Constraint type | BA action |
|-----------------|-----------|
| Budget | Scope to MoSCoW; flag licensing cost |
| Timeline | Thin-slice releases |
| Resources | Defer Could; flag skill gaps |
| Technology | Document in FRD NFRs; architect validation |
| Compliance | TBC Legal; never self-certify |
| Organizational | Change management requirements |

## Key Terminology

| Term | Definition |
|------|------------|
| Fixed constraint | Cannot change without sponsor approval |

## Frameworks and Models

BRD constraints section; escalate when Must outcomes conflict with constraints.

## Enterprise Best Practices

- Distinguish constraint vs assumption
- Revalidate constraints at phase gates
- Link constraints to fit-gap deferrals

## Common Mistakes

- Hidden license limits
- Ignoring batch window for integration

## Anti-Patterns

- Promising Must scope despite known timeline constraint

## Decision Guidelines

Must + constraint conflict → escalate with options: scope, time, or investment.

## Real-World Examples

Fixed go-live date R1 with ERP freeze window—integration must be batch-only.

## Industry Considerations

Data residency constraints affect cloud region and integration architecture.

## AI Guidance

Document constraints explicitly. Do not invent relaxed constraints.

## Review Checklist

- [ ] Constraints section in BRD
- [ ] Conflicts with Must items escalated

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

- [Interview Index](../interview-guide/interview-index.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Brain modules | **Downstream:** Templates, playbooks, deliverables | **Validation:** checklists.md

## Navigation

- **Previous:** [Capability Models](capability-models.md)
- **Next:** [Current State Analysis](current-state-analysis.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
