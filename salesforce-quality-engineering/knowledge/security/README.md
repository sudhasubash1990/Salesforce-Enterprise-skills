---
title: Security Knowledge — README
module: Salesforce Quality Engineering
category: Knowledge
document_type: Guide
version: 0.5.1
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
review_cycle: quarterly
related_documents:
  - salesforce-quality-engineering/knowledge/README.md
keywords: [security, knowledge-index, sprint-4a]
tags: [knowledge, sprint-4a, security]
---

# Security Knowledge

## Purpose

Access control, sharing, identity, and audit surfaces for persona-based quality risk.

## Scope

Profiles through MFA, sharing model, territory overview, audit/login/field history—from a testing lens.

**In scope (Sprint 4A):** This folder.  
**Out of scope (Sprint 4A):** Clouds, industries, CPQ, Agentforce, OmniStudio, managed packages, production-support deep dives → **Sprint 4B**.

## Available Documents

| Document | Focus |
|----------|-------|
| [Profiles](profiles.md) | Baseline persona access |
| [Permission Sets](permission-sets.md) | Additive access |
| [Permission Set Groups](permission-set-groups.md) | Bundled permission sets |
| [Field Level Security](field-level-security.md) | Field visibility/editability |
| [Object Level Security](object-level-security.md) | Object CRUD and View All/Modify All |
| [Role Hierarchy](role-hierarchy.md) | Role-based visibility |
| [Sharing Rules](sharing-rules.md) | Criteria/owner sharing |
| [Manual Sharing](manual-sharing.md) | Ad-hoc shares |
| [Public Groups](public-groups.md) | Group membership |
| [Queues](queues.md) | Queue ownership |
| [Organization-Wide Defaults](organization-wide-defaults.md) | OWD baseline |
| [Restriction Rules](restriction-rules.md) | Negative access filters |
| [Territory Management](territory-management.md) | Territory management overview |
| [Login Policies](login-policies.md) | Login IP/hours controls |
| [Session Policies](session-policies.md) | Session security settings |
| [MFA](mfa.md) | Multi-factor authentication |
| [Audit Trail](audit-trail.md) | Setup Audit Trail |
| [Login History](login-history.md) | Login History monitoring |
| [Field History Tracking](field-history-tracking.md) | Field history for security/audit |

## Navigation

- **Previous:** [automation/](../automation/README.md)
- **Next:** [data/](../data/README.md)
- **See Also:** [../../skill.md](../../skill.md) · [../README.md](../README.md)

## Related Knowledge

- [Requirement Analysis](../requirement-analysis.md)
- [Test Design Engine](../test-design-engine.md)
- [QE Brain](../../brain/README.md)
- [Risk-Based Testing](../risk-based-testing.md)
- [Regression Planning](../regression-planning.md)
- Sibling foundation folders: [platform](../platform/README.md) · [metadata](../metadata/README.md) · [automation](../automation/README.md) · [security](../security/README.md) · [data](../data/README.md)
