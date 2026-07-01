---
title: Data Migration
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
keywords: [data migration]
tags: [data-migration, cutover, data-quality]
review-cycle: quarterly
salesforce-cloud: Platform
---

# Data Migration

## Overview

Data migration strategy, mapping, cleansing, validation, reconciliation, and cutover for Salesforce programs.

## Purpose

Define BA-owned migration requirements—not ETL implementation.

## Why It Matters

Failed migration is a top cause of CRM go-live rollback.

## Business Context

Migration delivers the right data, quality, and relationships at cutover—not all historical data.

## Salesforce Context

Objects, external IDs, duplicate rules, ownership, record types, and post-migration integration sync.

## Core Concepts

| Phase | BA deliverables |
|-------|-----------------|
| Strategy | Migrate vs archive vs integrate; waves |
| Mapping | Source → Salesforce field mapping document |
| Cleansing | Quality rules, ownership, dedupe criteria |
| Validation | Record counts, sample reconciliation, sign-off criteria |
| Reconciliation | Exception handling process |
| Rollback | Criteria to abort cutover |
| Cutover | Freeze window, hypercare data support |

**Transition requirements:** TR-xxx in [requirement-types.md](requirement-types.md).

## Key Terminology

| Term | Definition |
|------|------------|
| External ID | Upsert key for integration/migration |
| Wave | Phased migration tranche |

## Frameworks and Models

Distinguish migration (one-time load) from ongoing integration—[integration-patterns.md](integration-patterns.md).

## Enterprise Best Practices

- Scope data explicitly in BRD
- Business sign-off on mapping and sample loads
- Migration UAT scenarios with production-like volume sample

## Common Mistakes

- Big-bang without reconciliation
- Missing inactive user ownership strategy

## Anti-Patterns

- "Migrate everything" without business value filter

## Decision Guidelines

Historical data beyond retention policy → archive, not migrate.

## Real-World Examples

Wave 1: active Accounts and Contacts; Wave 2: 24 months Cases; legacy leads archived.

## Industry Considerations

Healthcare: PHI minimization in migration scope.

## AI Guidance

Document acceptance criteria for migration validation. Flag data ownership assumptions.

## Review Checklist

- [ ] Scope and waves defined
- [ ] Sign-off criteria for reconciliation
- [ ] Rollback criteria documented

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

- **Previous:** [Current State Analysis](current-state-analysis.md)
- **Next:** [Dependency Management](dependency-management.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
