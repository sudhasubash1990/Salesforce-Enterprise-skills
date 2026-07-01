---
title: Risk Management
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
related_interview_topics: [salesforce-business-analyst/interview-guide/delivery/risk-management.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/knowledge/README.md]
keywords: [risk management]
tags: [risk, raid, governance]
review-cycle: quarterly
salesforce-cloud: Platform
---

# Risk Management

## Overview

Risk identification, assessment, mitigation, and monitoring for Salesforce BA programs.

## Purpose

Canonical approach for risks in RAID and steering forums.

## Why It Matters

Unowned risks become issues at go-live.

## Business Context

Risks threaten outcomes, timeline, budget, and adoption—not only technical failure.

## Salesforce Context

Include governor limits, sharing model errors, integration failure, license gaps, and data migration quality.

## Core Concepts

**Categories:**

| Category | Examples |
|----------|----------|
| Business | Low adoption, ROI not met |
| Technical | Integration timeout, bulk failure |
| Data | Poor master data, migration mismatch |
| Security | External user exposure |
| Compliance | Unvalidated regulatory control |
| Adoption | Insufficient training |
| Delivery | Dependency slip, resource gap |
| Operational | No support model post-hypercare |

**Assessment:** Probability × Impact → priority

**Mitigation:** Action, owner, review date

## Key Terminology

See [../templates/raid-log-template.md](../templates/raid-log-template.md).

## Frameworks and Models

Reasoning Stage 11; steering review cadence weekly or bi-weekly.

## Enterprise Best Practices

- Start RAID in discovery
- Top 3 risks in every readout
- Link risks to requirements they affect

## Common Mistakes

- Risk register without owners
- Risks not revisited after scope change

## Anti-Patterns

- Identifying risks only at go-live

## Decision Guidelines

High impact + high probability → Must mitigation before build; escalate if unmitigated.

## Real-World Examples

R-001: ERP API delay blocks Account sync—mitigation: mock service for SIT.

## Industry Considerations

Financial services: conduct risk and data residency risks escalated early.

## AI Guidance

Document risks in RAID format. Never downplay compliance risks.

## Review Checklist

- [ ] Owner and mitigation on material risks
- [ ] Review date set
- [ ] Linked to scope/requirements

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

- [Risk Management](../interview-guide/delivery/risk-management.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Brain modules | **Downstream:** Templates, playbooks, deliverables | **Validation:** checklists.md

## Navigation

- **Previous:** [Requirements Engineering](requirements-engineering.md)
- **Next:** [Salesforce Clouds Overview](salesforce-clouds-overview.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
