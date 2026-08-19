---
title: Test Design Techniques
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-test-case-designer, test-design-techniques]
---

# Test Design Techniques

Test design technique reference for ADO Test Case Designer. For the comprehensive test design engine, see [`../../../knowledge/test-design-engine.md`](../../../knowledge/test-design-engine.md) — this file provides ATCD-specific application guidance, not a duplicate.

## Technique Selection Matrix

| Technique | Best For | Salesforce Example |
|-----------|----------|-------------------|
| **Equivalence Partitioning** | Reducing test cases for large input domains | Picklist values, record type assignments |
| **Boundary Value Analysis** | Numeric/date/text field limits | Field character limits (255), currency precision, date ranges |
| **Decision Table** | Complex business rules with multiple conditions | Approval process criteria, assignment rules, escalation rules |
| **State Transition** | Lifecycle/stage-based objects | Opportunity stages, Case status, Lead conversion |
| **Use Case Testing** | E2E business process flows | Quote-to-Cash, Lead-to-Opportunity, Case resolution |
| **Pairwise / Combinatorial** | Multiple independent parameters | Record type + profile + page layout combinations |
| **Risk-Based** | Prioritizing test effort by risk | Governor limit scenarios, integration failure paths |
| **Error Guessing** | Platform-specific failure modes | Bulk DML limits, SOQL 101, mixed DML, sharing violations |

## Applying Techniques to Salesforce

### Equivalence Partitioning

Partition input space into classes that should behave identically:

- **Valid classes:** Required field with valid value, optional field empty, picklist valid selection
- **Invalid classes:** Required field blank, text exceeding max length, invalid picklist value via API

### Boundary Value Analysis

Test at edges of valid ranges:

| Boundary | Min | Max | Examples |
|----------|-----|-----|----------|
| Text field | 0 chars | Max length | Name field: 0, 1, 79, 80 chars |
| Number field | Min value | Max value | Amount: 0, 0.01, 999999999.99 |
| Date field | Earliest valid | Latest valid | Close Date: today, past date, far future |
| Collection | 0 items | Governor limit | Related list: 0, 1, max child records |

### Decision Table

Map conditions to expected actions:

| Condition 1 | Condition 2 | Condition 3 | Expected Action |
|-------------|-------------|-------------|-----------------|
| Amount > 100K | Stage = Proposal | Discount > 10% | Route to VP approval |
| Amount ≤ 100K | Any stage | Discount ≤ 10% | Auto-approve |

### State Transition

Model valid and invalid state changes:

```
Lead: Open → Working → Contacted → Qualified → Converted
                                              → Unqualified (terminal)
Invalid: Converted → Open (should be blocked)
```

## Technique-to-ADO Mapping

Each technique produces specific ADO test case patterns:

| Technique | ADO Test Case Pattern |
|-----------|----------------------|
| Equivalence Partitioning | One TC per equivalence class, parameterized |
| Boundary Value | TC at each boundary (min, min+1, max-1, max, beyond) |
| Decision Table | One TC per rule/row in decision table |
| State Transition | One TC per valid transition + invalid transition attempts |
| Use Case | One TC per main flow + alternate/exception flows |
| Pairwise | Parameterized TC with pairwise-generated data rows |

## Cross-Reference

For full technique definitions, algorithms, and selection flowcharts, load [`../../../knowledge/test-design-engine.md`](../../../knowledge/test-design-engine.md).

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
