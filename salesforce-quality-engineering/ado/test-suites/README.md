---
title: Test Suites — README
module: Salesforce Quality Engineering
category: ADO
document_type: Guide
version: 0.8.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
tags: [ado, sprint-6, test-suites]
---

# Test Suites

## Purpose

Organize cases inside plans: static, requirement-based, query-based, and purpose packs.

## When Used

When structuring execution for smoke, regression, UAT, release, or requirement coverage.

## Inputs

- Test Plan
- Requirements/stories
- Query criteria

## Outputs

- Suites with cases assigned

## Best Practices

- Prefer requirement-based for coverage
- Query-based for dynamic packs
- Static for curated smoke

## Available Documents

| Document | Focus |
|----------|-------|
| [Test Suite](test-suite.md) | Test Suite types and organization |

## Scope note

**Sprint 6 focuses on Delivery Intelligence** — work item quality, relationships, and ADO-ready artifact content.  
**Not in scope:** Azure DevOps REST API automation / auto-publish (optional later enhancement).

## Navigation

- **Previous:** [../test-plans/README.md](../test-plans/README.md)
- **Next:** [../test-cases/README.md](../test-cases/README.md)
- **See Also:** [../README.md](../README.md) · [../relationship-model.md](../relationship-model.md)

## Related Documents

- [QE Brain (Sprint 1)](../../brain/README.md)
- [Requirement Analysis (Sprint 2)](../../knowledge/requirement-analysis.md)
- [Test Design Engine (Sprint 3)](../../knowledge/test-design-engine.md)
- [Platform Foundation 4A](../../knowledge/platform/README.md)
- [Enterprise Knowledge 4B](../../knowledge/clouds/README.md)
- [Documentation Generator (Sprint 5)](../../templates/README.md)
- [BA ADO Backlog Integration](../../../salesforce-business-analyst/knowledge/ado-backlog-integration.md) (sibling—do not duplicate)
