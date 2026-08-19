---
title: Cloud Testing Model
module: Salesforce Quality Engineering
category: QE Specialized Skill Guide
document_type: Guide
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing, cloud-testing-model]
---

# Cloud Testing Model

## Purpose

Define the multi-cloud functional testing framework that governs how Service Cloud, Sales Cloud, and Experience Cloud scenarios are structured, leveled, and covered.

## Business Context

Salesforce implementations rarely involve a single cloud. Functional testing must account for object interactions across clouds, shared data models, and persona overlap. A structured testing model prevents gaps at cloud boundaries.

## Assessment Criteria

- Each cloud's core objects and features are enumerated before scenario design
- Testing levels (unit, functional, integration, E2E) are mapped to cloud scope
- Coverage strategy addresses intra-cloud and cross-cloud paths

## Key Areas

### Testing Levels

| Level | Scope | Example |
|-------|-------|---------|
| Functional | Single object / feature within one cloud | Case creation with assignment rule |
| System | Multiple objects within one cloud | Lead conversion creating Account + Contact + Opportunity |
| Integration | Data flow between clouds or external systems | Experience Cloud case → Service Cloud routing |
| E2E | Full business journey across clouds | Lead capture → Conversion → Opportunity → Approval → Close |

### Coverage Strategy

- **Intra-cloud:** Every standard object's CRUD operations, automation triggers, and validation rules
- **Cross-cloud:** Journey-level scenarios with handoff verification at cloud boundaries
- **Persona overlay:** Each journey tested per relevant persona / profile combination

## Decision Framework

| Signal | Decision |
|--------|----------|
| Single cloud, single object | Functional-level scenarios sufficient |
| Multiple objects, one cloud | Add system-level scenarios |
| Two or more clouds involved | Mandatory E2E journey scenarios |
| External system integration | Add integration-level with mock/stub strategy |

## Best Practices

- Map cloud boundaries explicitly before scenario design
- Identify shared objects (Account, Contact) as integration seams
- Define persona matrix before expanding scenarios
- Cross-link to [cloud knowledge](../../../knowledge/clouds/) — do not duplicate

## Anti-Patterns

- Testing clouds in isolation when business process spans multiple clouds
- Assuming shared objects behave identically across cloud contexts
- Skipping persona variation at cloud boundaries

## Related Documents

- [SKILL.md](../SKILL.md)
- [Service Cloud Knowledge](../../../knowledge/clouds/service-cloud.md)
- [Sales Cloud Knowledge](../../../knowledge/clouds/sales-cloud.md)
- [Experience Cloud Knowledge](../../../knowledge/clouds/experience-cloud.md)
