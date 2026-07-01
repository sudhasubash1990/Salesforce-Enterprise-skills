---
title: Prioritization Techniques
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
keywords: [prioritization techniques]
tags: [prioritization, wsjf, value, backlog]
review-cycle: quarterly
salesforce-cloud: Platform
---

# Prioritization Techniques

## Overview

Value-based, risk-based, and cost-of-delay methods for Salesforce backlog and release prioritization.

## Purpose

Provide repeatable techniques beyond subjective ordering.

## Why It Matters

Wrong priority wastes license and sprint capacity on low-value features.

## Business Context

Prioritization balances value, risk, dependency, and strategic alignment.

## Salesforce Context

Factor integration readiness, license availability, and admin capacity into sequencing.

## Core Concepts

| Technique | Application |
|-----------|-------------|
| MoSCoW | Release scope boundaries — [moscow-prioritization.md](moscow-prioritization.md) |
| WSJF | Weighted shortest job first in SAFe programs |
| Business value scoring | Objective × impact matrix |
| Risk-based | Must-haves with high delivery risk early |
| Cost of delay | Revenue or risk cost of waiting |
| Dependency-first | ERP API before portal case display |

**WSJF (summary):** (Business value + Time criticality + Risk reduction) / Job size

## Key Terminology

| Term | Definition |
|------|------------|
| Cost of delay | Economic impact of not delivering now |

## Frameworks and Models

Combine MoSCoW at release level with WSJF or team estimation within sprint.

## Enterprise Best Practices

- Facilitate prioritization with explicit criteria
- Revisit at phase gates
- Document why Won't items deferred

## Common Mistakes

- Priority by loudest stakeholder
- Ignoring dependencies

## Anti-Patterns

- Everything Must
- No recorded rationale for priority changes

## Decision Guidelines

Use Kano for enhancement roadmaps; MoSCoW for fixed-date releases.

## Real-World Examples

R1: ERP Account sync (dependency) before dealer portal (depends on Account 360).

## Industry Considerations

Public sector: legislative deadlines override WSJF.

## AI Guidance

When prioritizing, require criteria and document trade-offs per consulting principles.

## Review Checklist

- [ ] Criteria stated
- [ ] Dependencies considered
- [ ] Sponsor alignment for Must list

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

- **Previous:** [Moscow Prioritization](moscow-prioritization.md)
- **Next:** [Process Mapping](process-mapping.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
