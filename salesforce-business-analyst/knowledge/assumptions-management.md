---
title: Assumptions Management
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
related_interview_topics: [salesforce-business-analyst/interview-guide/interview-index.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/knowledge/README.md]
keywords: [assumptions management]
tags: [assumptions, raid, governance]
review-cycle: quarterly
salesforce-cloud: Platform
---

# Assumptions Management

## Overview

Logging, validation, ownership, and closure of assumptions on Salesforce programs.

## Purpose

Prevent undocumented assumptions from becoming production defects.

## Why It Matters

Undocumented assumptions are the leading source of late rework on enterprise CRM programs.

## Business Context

Assumptions fill gaps until validated by stakeholder or technical discovery.

## Salesforce Context

Common assumptions: org edition features, integration availability, data quality, license counts, SSO approach.

## Core Concepts

**Assumption record:** ID, statement, validate-by date, owner, status (Open / Validated / Invalidated), linked requirements.

**Lifecycle:**

```
Log → Review in steering → Validate or invalidate → Update requirements
```

**Pattern:** We assume [statement]. Validate by [date/milestone].

## Key Terminology

See [../../shared/consulting-principles.md](../../shared/consulting-principles.md) — Explicit Assumptions.

## Frameworks and Models

- RAID log assumptions section
- Every deliverable ends with Assumptions per [../../shared/output-standards.md](../../shared/output-standards.md)

## Enterprise Best Practices

- Label inferred AI context as assumptions
- Invalidate assumptions trigger change impact
- No silent defaults in requirements

## Common Mistakes

- Assumptions buried in prose
- Never closing validated assumptions

## Anti-Patterns

- Treating assumptions as facts in Must requirements

## Decision Guidelines

Invalidated assumption affecting Must scope → change request or re-MoSCoW.

## Real-World Examples

A-002: Assume ERP provides real-time Account updates—validate by integration workshop week 4.

## Industry Considerations

Regulatory assumptions always owned by Legal/Compliance validation.

## AI Guidance

Mandatory per [../brain/anti-hallucination.md](../brain/anti-hallucination.md). Ask before assuming.

## Review Checklist

- [ ] Assumptions section present
- [ ] Validate-by and owner on material items

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

- **Previous:** [Ai In Business Analysis](ai-in-business-analysis.md)
- **Next:** [Babok Guide](babok-guide.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
