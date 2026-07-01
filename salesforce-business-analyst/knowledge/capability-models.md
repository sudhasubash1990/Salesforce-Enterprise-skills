---
title: Capability Models
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
keywords: [capability models]
tags: [capability, mapping, maturity, value]
review-cycle: quarterly
salesforce-cloud: Platform
---

# Capability Models

## Overview

Business capability mapping, maturity assessment, and Salesforce alignment for transformation programs.

## Purpose

Express what the organization does independent of systems—then map to Salesforce clouds and fit-gap decisions.

## Why It Matters

Capability thinking prevents org-chart-driven design and surfaces gaps before object modeling.

## Business Context

Capabilities are stable; systems and processes change. Heat maps guide investment.

## Salesforce Context

Map capabilities to [../../shared/salesforce-capability-map.md](../../shared/salesforce-capability-map.md)—flag licensing (CPQ, FSL, Data Cloud).

## Core Concepts

- **Business capability:** What the org does (e.g., "Manage dealer relationships")
- **Maturity:** Ad hoc → defined → managed → optimized
- **Value realization:** KPI movement tied to capability investment

```mermaid
flowchart LR
    CapMap[Business capabilities] --> Heat[Priority heat map]
    Heat --> SFMap[Salesforce cloud mapping]
    SFMap --> FitGap[Fit-gap analysis]
```

## Key Terminology

| Term | Definition |
|------|------------|
| Capability map | Structured view of business capabilities |
| TOM | Target operating model |

## Frameworks and Models

- Capability-based planning
- Link to [future-state-design.md](future-state-design.md) and [current-state-analysis.md](current-state-analysis.md)

## Enterprise Best Practices

- Workshop capability map with business, not IT-only
- Refresh at phase gates, not one-time
- Tie Must capabilities to release plan

## Common Mistakes

- Confusing departments with capabilities
- Capability map disconnected from backlog

## Anti-Patterns

- "Salesforce will fix our process" without capability gap analysis

## Decision Guidelines

High maturity gap + high value = prioritize in early release.

## Real-World Examples

"Unified customer view" capability → Account 360 on Sales + Service + ERP sync.

## Industry Considerations

Manufacturing: aftermarket service capabilities often undervalued in initial CRM scope.

## AI Guidance

Use capability language in discovery readouts before object names.

## Review Checklist

- [ ] Capabilities are verb-noun business language
- [ ] Salesforce mapping references capability map
- [ ] Maturity or priority indicated

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

- **Previous:** [Business Rules](business-rules.md)
- **Next:** [Constraints Management](constraints-management.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
