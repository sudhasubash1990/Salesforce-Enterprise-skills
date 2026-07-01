---
title: Salesforce Security Model
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
related_interview_topics: [salesforce-business-analyst/interview-guide/delivery/architecture.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/knowledge/README.md]
keywords: [security model]
tags: [security, sharing, permissions, fls]
review-cycle: quarterly
salesforce-cloud: Platform
---

# Salesforce Security Model

## Overview

Authentication, authorization, sharing, and data protection concepts for BA requirements.

## Purpose

Ensure requirements address who can see and edit what—early and testably.

## Why It Matters

Sharing mistakes are expensive to fix post-go-live and cause compliance incidents.

## Business Context

Security requirements express business rules about data access and segregation.

## Salesforce Context

Layers: authentication (SSO, MFA) → authorization (profiles, permission sets) → sharing (OWD, roles, rules) → FLS.

## Core Concepts

| Layer | BA documents |
|-------|----------------|
| Authentication | SSO for portal, MFA policy |
| Profiles / permission sets | Persona capabilities |
| OWD | Default internal/external access |
| Role hierarchy | Management visibility |
| Sharing rules | Exception access |
| FLS | Field-level read/edit |
| Experience Cloud | External user licenses, sharing sets |

**Question:** Who can't see what? Include in stories as permission AC.

## Key Terminology

| Term | Definition |
|------|------------|
| OWD | Organization-wide defaults |
| FLS | Field-level security |

## Frameworks and Models

Security requirements in FRD §; never recommend bypassing controls.

## Enterprise Best Practices

- Security workshops with admin early
- Negative permission scenarios in AC
- External user model defined before portal stories

## Common Mistakes

- Security designed after UAT
- "Run as admin" workarounds in requirements

## Anti-Patterns

- Over-sharing "for simplicity"
- Portal exposing internal fields

## Decision Guidelines

Complex sharing → architect review; document as NFR and fit-gap Extend if needed.

## Real-World Examples

Dealer sees only own cases; internal rep sees territory accounts.

## Industry Considerations

Healthcare: minimum necessary access; audit on PHI fields.

## AI Guidance

Never recommend disabling sharing or MFA. See [../../docs/security-guidelines.md](../../docs/security-guidelines.md).

## Review Checklist

- [ ] Personas mapped to access model
- [ ] Permission AC on stories
- [ ] External user model documented

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

- [Architecture](../interview-guide/delivery/architecture.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Brain modules | **Downstream:** Templates, playbooks, deliverables | **Validation:** checklists.md

## Navigation

- **Previous:** [Salesforce Platform](salesforce-platform.md)
- **Next:** [Stakeholder Analysis](stakeholder-analysis.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
