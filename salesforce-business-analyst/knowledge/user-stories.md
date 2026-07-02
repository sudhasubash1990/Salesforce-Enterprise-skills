---
title: User Stories
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
related_knowledge: [salesforce-business-analyst/knowledge/README.md, salesforce-business-analyst/knowledge/ado-backlog-integration.md]
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

## Estimation (BA Role)

Story points are a **relative** size measure (complexity + effort + uncertainty)—**not** hours, days, or months. The delivery team assigns final story points at backlog refinement / planning poker.

| BA provides | BA does not provide |
|-------------|---------------------|
| T-shirt size (XS–XL) | Final story-point number (unless user explicitly requests indicative value) |
| Estimation-input table (approach, complexity, risk, dependencies) | Calendar duration or hour estimates |
| Splittability recommendation if story feels large | Velocity or sprint commitment |

**T-shirt guidance:**

| T-shirt | Typical signal |
|---------|----------------|
| S | Single object, few fields, no automation |
| M | One workflow + declarative automation + reporting (fits one sprint) |
| L | Multiple integrations, sharing complexity, or significant stakeholder iteration |
| XL | Split or spike first |

For ADO publishing rules, see [ado-backlog-integration.md](ado-backlog-integration.md).

## Deliverables Ownership

Distinguish **BA deliverables** (story, AC, business rules, estimation inputs) from **implementation team deliverables** (metadata, Flows, layouts, security, test evidence). Every story must include a **Deliverables Expected (Implementation Team)** section listing Salesforce build artifacts implied by the story. See [brain/identity.md](../brain/identity.md) scope table.

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
- Assigning exact story points without team refinement
- Omitting implementation deliverables (only listing BA artifacts)
- Acceptance criteria as unreadable paragraphs instead of nested bullets (especially in ADO)

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
- [ ] T-shirt size and estimation inputs documented
- [ ] Deliverables Expected (Implementation Team) listed
- [ ] Story points deferred to team unless explicitly requested as indicative

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
| 0.4.0 | 2026-07-02 | BA Practice Lead | Estimation discipline, deliverable ownership, ADO lessons |
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
