---
title: Dependency Management
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
keywords: [dependency management]
tags: [dependencies, raid, delivery]
review-cycle: quarterly
salesforce-cloud: Platform
---

# Dependency Management

## Overview

Internal, external, technical, and business dependencies—tracking and impact analysis.

## Purpose

Prevent sprint and release failures from untracked cross-team or system dependencies.

## Why It Matters

Salesforce programs depend on ERP, IAM, data, and vendor APIs—often the critical path.

## Business Context

Dependencies have providers, deliverables, needed-by dates, and impact if late.

## Salesforce Context

Examples: ERP Account API, SSO for Experience Cloud, marketing consent feed, sandbox refresh schedule.

## Core Concepts

| Type | Example |
|------|---------|
| Internal | Data model approval before stories |
| External | Vendor API certification |
| Technical | Middleware deployment before SIT |
| Business | Policy sign-off before portal launch |

**Record:** DEP-xxx, provider, deliverable, needed-by, impact if late, status

## Key Terminology

See [../templates/raid-log-template.md](../templates/raid-log-template.md).

## Frameworks and Models

- RAID dependencies section
- Prioritization: [prioritization-techniques.md](prioritization-techniques.md) dependency-first

## Enterprise Best Practices

- Track from discovery
- Review in weekly integration standup
- Link to release plan

## Common Mistakes

- Dependencies without dates
- Portal stories before SSO dependency met

## Anti-Patterns

- Assuming another team "will be ready"

## Decision Guidelines

Must stories blocked by open dependency → defer story or escalate dependency.

## Real-World Examples

DEP-001: IAM team delivers dealer SSO by week 8 for portal UAT.

## Industry Considerations

Multi-vendor SI programs: explicit dependency owners in RAID.

## AI Guidance

Flag dependencies when generating release plans and stories.

## Review Checklist

- [ ] Needed-by date on critical deps
- [ ] Provider named
- [ ] Impact if late documented

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

- **Previous:** [Data Migration](data-migration.md)
- **Next:** [Domains](domains.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
