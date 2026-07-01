---
title: Fit Gap Excerpt
module: Salesforce Business Analyst
category: Root
document_type: Guide
version: 1.1.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/README.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/interview-index.md]
related_examples: [examples/sample-project/README.md]
related_documents: [docs/cross-linking-framework.md, ROADMAP.md]
keywords: [fit gap excerpt]
tags: [fit-gap-excerpt]
---

# Worked Example: Fit-Gap Excerpt

Sample fit-gap rows for training and agent reference.

## Context

Apex Manufacturing — dealer portal release (fictional).

| Req ID | Need Summary | Standard Feature | Class | Recommendation | Effort | Risk |
|--------|--------------|------------------|-------|----------------|--------|------|
| BR-005 | Dealer case submission | Experience Cloud + Case | Config | Dealer record type, guest/auth portal, case web form | M | Low |
| BR-006 | Order status visibility | No native Order object | Extend | Custom Order__c + ERP nightly sync | M | Med |
| BR-007 | Knowledge for dealers | Knowledge + Data Categories | Standard | Publish articles with Dealer category | S | Low |
| BR-010 | Offline mobile quoting | Salesforce Mobile | Gap | Mobile offline limited; defer quoting to R2 or CPQ eval | L | High |

## Decision Log Reference

**D-02:** CPQ evaluation deferred to R2 — ERP quoting sufficient for R1 MVP.

## Lesson

BR-006 classified Extend (custom object) not Gap because pattern is well-established with ERP integration—Gap reserved for needs with no clear Salesforce pattern.

## Related Brain Modules

- [Readme](../brain/README.md)

## Related Knowledge

- [Readme](../knowledge/README.md)

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

- [Cross Linking Framework](../../docs/cross-linking-framework.md)
- [Roadmap](../../ROADMAP.md)

## Traceability

**Upstream:** — | **Downstream:** All skills | **Validation:** ROADMAP alignment

## Navigation

- **Previous:** [Discovery Readout Outline](discovery-readout-outline.md)
- **Next:** —
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
