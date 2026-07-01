---
title: Business Rules
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
keywords: [business rules]
tags: [business-rules, validation, compliance]
review-cycle: quarterly
salesforce-cloud: Platform
---

# Business Rules

## Overview

Capturing, classifying, and tracing business rules on Salesforce programs.

## Purpose

Single approach for decision rules, validation rules, and compliance rules in requirements.

## Why It Matters

Undocumented rules live only in developers' heads and break at scale or org changes.

## Business Context

Rules express policies and constraints that systems must enforce consistently.

## Salesforce Context

Prefer validation rules, duplicate rules, Flow decisions, and entitlement logic before Apex. Document rule implementation layer in fit-gap.

## Core Concepts

**Rule pattern:** When [condition], the system must [behaviour], except when [exception].

| Category | Example |
|----------|---------|
| Validation | Case cannot close without resolution code |
| Decision | Discount > 20% requires manager approval |
| Compliance | PII field not visible to external profile |
| Derivation | Opportunity amount rolls up from line items |

**Traceability:** Rule ID → BR/FR → story AC → test scenario

## Key Terminology

See [../../shared/reusable-components.md](../../shared/reusable-components.md#business-rule-pattern).

## Frameworks and Models

Rules catalog in FRD or appendix; link to [requirement-types.md](requirement-types.md).

## Enterprise Best Practices

- Centralize rules list; avoid scattering in UI specs
- Flag conflicting rules from different workshops
- Version rules with BRD/FRD

## Common Mistakes

- Rules only in dev notes
- Exceptions not documented

## Anti-Patterns

- Hard-coded thresholds without business owner
- Duplicate rules in validation rule and Flow

## Decision Guidelines

| Complexity | Approach |
|------------|----------|
| Field-level | Validation rule |
| Multi-object | Flow |
| High volume / complex | Apex (architect decision) |

## Real-World Examples

Dealer tier determines case priority—decision rule with exception for safety recalls.

## Industry Considerations

Financial services: AML hold rules require audit trail in AC.

## AI Guidance

Extract rules as testable FR or AC. Never invent regulatory rules.

## Review Checklist

- [ ] Condition and exception clear
- [ ] Traceable to BR/FR
- [ ] Testable AC or TS

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

- **Previous:** [Business Analysis Fundamentals](business-analysis-fundamentals.md)
- **Next:** [Capability Models](capability-models.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
