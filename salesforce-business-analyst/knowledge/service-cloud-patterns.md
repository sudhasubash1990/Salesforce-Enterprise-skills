---
title: Service Cloud Patterns
module: Salesforce Business Analyst
category: Knowledge
document_type: Knowledge Article
version: 1.0.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
difficulty: intermediate
industry: all
related_brain_modules: [salesforce-business-analyst/brain/reasoning-framework.md, salesforce-business-analyst/brain/decision-framework.md]
related_knowledge: [salesforce-business-analyst/knowledge/salesforce-clouds-overview.md, salesforce-business-analyst/knowledge/security-model.md, salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/user-story-template.md]
related_playbooks: [salesforce-business-analyst/playbooks/gap-analysis-playbook.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/salesforce/service-cloud.md]
related_examples: [examples/sample-user-story/dealer-portal-stories.md, examples/sample-user-story/service-cloud-complaint-story.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/knowledge/README.md]
keywords: [service cloud, case, entitlement, knowledge, omni-channel, complaint, service agent]
tags: [service-cloud, case-management, entitlements, knowledge-base, omni-channel, customer-service]
salesforce-cloud: Service Cloud
---

# Service Cloud Patterns

## Overview

BA patterns for Salesforce Service Cloud — the platform's customer service backbone. Load this article whenever requirements mention complaints, cases, customer service agents, call centers, entitlements, knowledge articles, or Omni-Channel routing.

## Purpose

Provide domain-specific BA knowledge so the agent does not rely on general LLM knowledge when recommending Service Cloud solutions.

## When to Load

Load this article when any of these signals appear in the requirement:

- Customer service, support agent, call center, complaint, case
- Entitlement, SLA, milestones, service contract
- Knowledge base, knowledge article, self-service
- Omni-Channel, routing, queue, skill-based routing
- Service Console, service dashboard, CSAT
- Email-to-Case, Web-to-Case, Chat

## Core Objects and Features

### Case Object (Standard)

The Case object is the primary record for tracking customer issues in Service Cloud.

| Aspect | BA Guidance |
|--------|-------------|
| **When to use** | Any customer complaint, inquiry, issue, or request tracking |
| **Prefer over custom object** | Always use Case before creating a custom Complaint__c or Issue__c object |
| **Record types** | Use record types to distinguish complaint vs inquiry vs request (avoid separate custom objects) |
| **Case origin** | Standard picklist: Phone, Email, Web, Chat — extend with custom values only if needed |
| **Case type** | Standard picklist: Problem, Feature Request, Question — extend or replace per business taxonomy |
| **Status lifecycle** | Typical: New → Working → Escalated → Closed. Customize per process; avoid >8 statuses |
| **Priority** | Standard picklist: High, Medium, Low, Critical. Default via automation, not manual entry |
| **Auto-number** | Case Number is auto-generated (do not create a custom number field) |

### Key Standard Fields on Case

| Field | Type | BA Notes |
|-------|------|----------|
| Contact | Lookup | Links case to the customer. Consider Contact auto-creation from Email-to-Case |
| Account | Lookup | Auto-populates from Contact.Account. Useful for reporting by company |
| Subject | Text(255) | Short summary. Required by default |
| Description | Long Text | Full details. Consider minimum length validation |
| Status | Picklist | Lifecycle tracking. Default: New |
| Priority | Picklist | Business criticality. Default: Medium or per business rule |
| Origin | Picklist | Channel (Phone, Email, Web). Important for channel analytics |
| Type | Picklist | Categorization. Map to business taxonomy |
| Reason | Picklist | Root cause (post-resolution) |
| Escalated | Checkbox | Set by escalation rules or manually |
| Closed Date | DateTime | Auto-set when Status = Closed |

### Entitlements and Milestones

| Feature | BA Guidance |
|---------|-------------|
| **Entitlements** | Define support levels per account/contact/asset (e.g., Gold = 4hr response, Silver = 8hr) |
| **Milestones** | Time-based SLA checkpoints (First Response, Resolution). Trigger escalation if breached |
| **Entitlement Process** | Sequence of milestones applied to cases matching entitlement criteria |
| **Fit-gap** | Standard feature — classify as **Standard** in fit-gap when SLA tracking is required |

### Knowledge (Salesforce Knowledge)

| Feature | BA Guidance |
|---------|-------------|
| **Knowledge articles** | Agent-facing and customer-facing content for case deflection |
| **Article types** | FAQ, How-To, Troubleshooting — use data categories for taxonomy |
| **Case attachment** | Agents can attach relevant articles to cases |
| **Self-service** | Expose via Experience Cloud for customer self-resolution |
| **Fit-gap** | Standard when deflection or knowledge reuse is required |

### Omni-Channel

| Feature | BA Guidance |
|---------|-------------|
| **Routing** | Assigns work (cases, chats, leads) to agents based on availability and skill |
| **Routing types** | Queue-based (simple) vs Skill-based (complex). Choose based on team structure |
| **Capacity model** | Tab-based or Status-based. Affects agent workload calculation |
| **Supervisor view** | Real-time monitoring of queue depths and agent status |
| **Fit-gap** | Standard for multi-channel routing; Config for skill-based rules |

### Email-to-Case and Web-to-Case

| Channel | BA Guidance |
|---------|-------------|
| **Email-to-Case** | Auto-creates cases from emails to a support address. On-Demand preferred over client-based |
| **Web-to-Case** | HTML form or Experience Cloud page creates cases. Limited to 5,000/day |
| **Chat / Messaging** | Embedded Service for real-time support. Creates cases with transcript |

## Common BA Patterns

### Pattern: Complaint Management

- Use **Case** with a Complaint record type (or Case Type = Complaint)
- Required fields: Contact lookup, Complaint Category (picklist), Description, Priority, Status
- Defaults via Record-Triggered Flow: Status = New, Priority = Medium
- Confirmation email via Email Alert + Email Template triggered by Flow
- Manager dashboard with standard Reports + Dashboard

### Pattern: Multi-Tier Support

- Entitlements define SLA per tier (Platinum, Gold, Silver)
- Milestones track First Response and Resolution Time
- Escalation rules auto-escalate on milestone breach
- Assignment rules route to appropriate queue by tier

### Pattern: Knowledge-Enabled Service

- Agents search Knowledge during case handling
- Suggested articles appear based on case subject/description
- Article feedback loop: agents flag gaps, knowledge team fills them
- Self-service portal exposes published articles via Experience Cloud

## Fit-Gap Classification for Service Cloud

| Capability | Typical Classification | Notes |
|------------|----------------------|-------|
| Case creation and tracking | Standard | Native Case object |
| Required field validation | Config | Validation rules, required fields on layout |
| Status/Priority defaults | Config | Record-Triggered Flow or default values |
| Confirmation email on case creation | Config | Flow + Email Alert + Email Template |
| Manager dashboard | Standard | Reports + Dashboard |
| SLA tracking with milestones | Standard | Entitlements (may need license check) |
| Omni-Channel routing | Standard/Config | Queue-based is standard; skill-based is config |
| Customer self-service portal | Config | Experience Cloud with Knowledge |
| Integration with external ticketing system | Extend/Gap | API or middleware required |
| AI-powered case classification | Extend | Einstein Classification or custom ML |

## Security Patterns

| Persona | Typical Access |
|---------|---------------|
| Service Agent | Create, Read Own/Team, Update Own/Team, No Delete |
| Service Manager | Read All (or hierarchy-based), Update, Run Reports |
| System Admin | Full CRUD |
| Customer (Portal) | Create, Read Own, Update Own (limited fields) |

OWD for Case: typically **Private** or **Controlled by Parent** (Account). Sharing rules for cross-team visibility.

## Common Mistakes

| Mistake | Correction |
|---------|------------|
| Custom Complaint__c object instead of Case | Use Case with record type or picklist categorization |
| Custom auto-number field for case reference | Case Number is standard and auto-generated |
| No record type — all cases look the same | Add record types for distinct processes (Complaint, Inquiry, Request) |
| SLA tracked in custom fields | Use Entitlements and Milestones (standard feature) |
| Email sent via Apex instead of declarative | Use Flow + Email Alert unless complex conditional logic is needed |
| Delete permission given to agents | Agents should not delete cases; use sharing/permissions to restrict |

## Related Brain Modules

- [Reasoning Framework](../brain/reasoning-framework.md)
- [Decision Framework](../brain/decision-framework.md)

## Related Knowledge

- [Salesforce Clouds Overview](salesforce-clouds-overview.md)
- [Security Model](security-model.md)

## Related Templates

- [User Story Template](../templates/user-story-template.md)

## Related Playbooks

- [Gap Analysis Playbook](../playbooks/gap-analysis-playbook.md)

## Related Industry Scenarios

- [Readme](../scenarios/README.md)

## Related Interview Topics

- [Service Cloud](../interview-guide/salesforce/service-cloud.md)

## Related Examples

- [Dealer Portal Stories](../../examples/sample-user-story/dealer-portal-stories.md)
- [Service Cloud Complaint Story](../../examples/sample-user-story/service-cloud-complaint-story.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Brain modules, salesforce-clouds-overview | **Downstream:** User stories, fit-gap, templates | **Validation:** checklists.md

## Navigation

- **Previous:** [Security Model](security-model.md)
- **Next:** [Salesforce Clouds Overview](salesforce-clouds-overview.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | BA Practice Lead | Initial Service Cloud patterns article (from Task-9 gap analysis) |
