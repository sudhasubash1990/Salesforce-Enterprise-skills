---
title: Release Management
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
keywords: [release management]
tags: [release, deployment, hypercare, uat]
review-cycle: quarterly
salesforce-cloud: Platform
---

# Release Management

## Overview

Release planning, deployment coordination, testing gates, hypercare, and lessons learned.

## Purpose

Align BA deliverables to release trains and go-live criteria.

## Why It Matters

Requirements without release context cause big-bang risk and unclear UAT scope.

## Business Context

Releases deliver thin slices of TO-BE capabilities with measurable outcomes.

## Salesforce Context

Sandbox promotion path, UAT sign-off, production deployment window, post-go-live hypercare.

## Core Concepts

| Phase | BA role |
|-------|---------|
| Planning | Map BR/themes to R1/R2/R3; MoSCoW per release |
| Testing | UAT scenarios per release; RTM coverage |
| Deployment | Change log, release notes content |
| Hypercare | Priority defect triage support; FAQ updates |
| Rollback | Business criteria to revert (with PM/architect) |
| Lessons learned | Requirement quality feedback |

## Key Terminology

| Term | Definition |
|------|------------|
| Hypercare | Intensive support period post-go-live |
| Release train | Cadence of deployments |

## Frameworks and Models

[../playbooks/uat-playbook.md](../playbooks/uat-playbook.md); sample project three-release plan.

## Enterprise Best Practices

- UAT sign-off per release, not only final
- Release notes trace to BR/US
- Hypercare scope and duration agreed pre-go-live

## Common Mistakes

- UAT only on final combined release
- No hypercare BA support plan

## Anti-Patterns

- Go-live without rollback decision criteria

## Decision Guidelines

Must scope slip → re-MoSCoW or move date—document in RAID.

## Real-World Examples

Apex Manufacturing: 9 months, 3 releases—portal in R3 after ERP sync R1.

## Industry Considerations

Retail peak seasons: blackout deployment windows as constraints.

## AI Guidance

Tag requirements with release hints. Generate UAT per release scope.

## Review Checklist

- [ ] Release column in RTM
- [ ] UAT scope matches release
- [ ] Hypercare mentioned in BRD

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

- **Previous:** [Process Mapping](process-mapping.md)
- **Next:** [Requirement Types](requirement-types.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
