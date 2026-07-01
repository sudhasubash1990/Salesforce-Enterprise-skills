---
title: Requirement Types
module: Salesforce Business Analyst
category: Knowledge
document_type: Knowledge Article
version: 0.3.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
difficulty: foundational
industry: all
related_brain_modules: [salesforce-business-analyst/brain/reasoning-framework.md, salesforce-business-analyst/brain/output-framework.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/requirement-gathering.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/knowledge/README.md]
keywords: [requirement types]
tags: [requirements, brd, frd, nfr]
review-cycle: quarterly
salesforce-cloud: Platform
---

# Requirement Types

## Overview

Taxonomy of requirement types on Salesforce programs—when to use each and how they trace across deliverables.

## Purpose

Single source of truth for classifying requirements. Prevents mixed types in one document and broken traceability.

## Why It Matters

Stakeholders express needs at different levels. Misclassification causes UAT failures and scope disputes.

## Business Context

Requirements span outcomes (business), behaviour (functional), quality (non-functional), and transition (cutover/training).

## Salesforce Context

Map types to BRD, FRD, user stories, and NFR sections. Reference Salesforce objects conceptually—not as screen specs in BRs.

## Core Concepts

| Type | Focus | ID pattern | Primary document |
|------|-------|------------|------------------|
| Business | Outcome, why | BR-xxx | BRD |
| Stakeholder | Stakeholder need | SH-xxx | BRD / workshop notes |
| Functional | System behaviour | FR-xxx | FRD |
| Non-functional | Quality attribute | NFR-xxx | FRD |
| Transition | Cutover, training, migration | TR-xxx | BRD / release plan |
| Regulatory | Control, compliance | REG-xxx | BRD (TBC Legal) |
| Technical | Build constraint | TECH-xxx | FRD / architect |

**Traceability chain:** BR → FR → US → AC → TS

## Key Terminology

See L0–L5 hierarchy in [../../shared/taxonomy.md](../../shared/taxonomy.md).

## Frameworks and Models

- MoSCoW priority on business and functional items
- Fit-gap classification on functional needs: [../playbooks/fit-gap-analysis.md](../playbooks/fit-gap-analysis.md)

## Enterprise Best Practices

- One type per requirement block
- Business requirements stay technology-agnostic
- NFRs must be measurable (latency, availability, volume)
- Regulatory items never self-certified by BA

## Common Mistakes

- Screen layouts labeled as business requirements
- Functional detail in BRD that belongs in FRD
- Missing transition requirements for data migration

## Anti-Patterns

- "The system shall" in BR without actor
- Duplicate IDs across documents

## Decision Guidelines

| Need | Document |
|------|----------|
| Why and outcome | BRD (BR) |
| Detailed behaviour | FRD (FR) |
| Sprint deliverable | User story (US) |
| Quality / scale | FRD (NFR) |

## Real-World Examples

- BR-012: Reduce dealer inbound calls by 25%
- FR-014: Dealer submits Service case via portal with attachment under 5 MB
- NFR-003: Portal case submission responds within 3 seconds at P95

## Industry Considerations

Healthcare: REG items with Legal owner; HIPAA controls documented, not claimed as met.

## AI Guidance

Classify each requirement when generating BRD/FRD. Enforce `requirement_refs` on stories.

## Review Checklist

- [ ] Each requirement has type, ID, priority, source
- [ ] BRs are outcome-oriented
- [ ] FRs are testable

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

- [Requirement Gathering](../interview-guide/requirement-gathering.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Brain modules | **Downstream:** Templates, playbooks, deliverables | **Validation:** checklists.md

## Navigation

- **Previous:** [Release Management](release-management.md)
- **Next:** [Requirements Engineering](requirements-engineering.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
