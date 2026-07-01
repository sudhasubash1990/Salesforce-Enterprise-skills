---
title: User Stories
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
related_interview_topics: [salesforce-business-analyst/interview-guide/user-stories.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/knowledge/README.md]
keywords: [user stories]
tags: [user-stories, agile, invest, backlog]
review-cycle: quarterly
salesforce-cloud: Sales Cloud, Service Cloud, Platform
---

# User Stories

## Overview

INVEST-compliant user stories for Salesforce agile delivery—structure, decomposition, refinement, and estimation inputs.

## Purpose

Canonical guidance for writing backlog items that are deliverable, testable, and traceable to business requirements.

## Why It Matters

Poor stories drive rework, untestable AC, and sprint spillover. Epics disguised as stories break forecasting.

## Business Context

Stories express incremental value for a persona. They negotiate scope within epics and releases.

## Salesforce Context

Stories must address permissions, record types, sharing, mobile, integration touchpoints, and bulk scenarios when applicable.

## Core Concepts

**Standard structure:** As a [role], I want [goal], so that [benefit].

**INVEST:**

| Principle | Salesforce check |
|-----------|------------------|
| Independent | Can deliver without unfinished dependency |
| Negotiable | Details in AC, not fixed UI mockup |
| Valuable | Links to BR outcome |
| Estimable | Team can size after refinement |
| Small | Completable in one sprint |
| Testable | 3+ Given/When/Then AC |

**Splitting techniques:** workflow steps, business rules, interface channels, CRUD variations, data variations.

## Key Terminology

| Term | Definition |
|------|------------|
| Epic | Large outcome spanning multiple stories |
| Feature | Group of related stories |
| Spike | Time-boxed research story |

## Frameworks and Models

Story mapping for release planning—see [epic-design.md](epic-design.md).

## Enterprise Best Practices

- `requirement_refs` to BR/FR on every story
- Include negative paths and permission scenarios
- Data setup notes for QA
- Refine in backlog grooming with admin/dev present

## Common Mistakes

- Epics labeled as user stories
- Missing benefit clause
- No link to parent requirement

## Anti-Patterns

- "As a user I want a new field on Account"
- Acceptance criteria that only say "verify page loads"

## Decision Guidelines

| Size | Action |
|------|--------|
| > 8 points repeatedly | Split |
| Cross-cloud dependency | Split or spike first |
| Unclear platform fit | Fit-gap before story finalization |

## Real-World Examples

See [../../examples/sample-user-story/dealer-portal-stories.md](../../examples/sample-user-story/dealer-portal-stories.md).

## Industry Considerations

Regulated data: stories must call out consent, retention, and field-level security in AC.

## AI Guidance

Always use [../templates/user-story-template.md](../templates/user-story-template.md). Validate with [../checklists.md](../checklists.md).

## Review Checklist

- [ ] INVEST pass
- [ ] 3+ testable AC
- [ ] requirement_refs present

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

- [User Stories](../interview-guide/user-stories.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Brain modules | **Downstream:** Templates, playbooks, deliverables | **Validation:** checklists.md

## Navigation

- **Previous:** [Stakeholder Analysis](stakeholder-analysis.md)
- **Next:** [Readme](README.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
