---
title: KPI Baseline Template
module: Salesforce Business Analyst
category: Template
document_type: Template
version: 1.0.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-03
last_updated: 2026-07-03
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/output-framework.md, salesforce-business-analyst/brain/validation-framework.md, salesforce-business-analyst/brain/anti-hallucination.md]
related_knowledge: [salesforce-business-analyst/knowledge/future-state-design.md, salesforce-business-analyst/knowledge/current-state-analysis.md, salesforce-business-analyst/knowledge/governance-framework.md]
related_templates: [salesforce-business-analyst/templates/business-case-template.md, salesforce-business-analyst/templates/future-state-template.md]
related_playbooks: [salesforce-business-analyst/playbooks/value-stream-mapping-playbook.md, salesforce-business-analyst/playbooks/digital-transformation-strategy-playbook.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/future-state.md]
related_examples: [examples/sample-brd/brd-excerpt.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/templates/README.md]
keywords: [kpi baseline template, kpi definition, target outcome, benefit realization, success metrics]
tags: [kpi-baseline-template, kpi, metrics, benefits]
---

# KPI Baseline Template

---
title: KPI Definition and Target Outcomes
type: kpi-baseline
version: 0.1.0
status: draft
last_updated: YYYY-MM-DD
project: PRJ-XXX-001
author:
tags: [salesforce, kpi, benefits, governance]
---

# KPI Definition and Target Outcomes

## Document Control

| Field | Value |
|-------|-------|
| Project | PRJ-XXX-001 |
| Version | 0.1.0 |
| Last updated | YYYY-MM-DD |
| Review frequency | Monthly / per governance cadence |
| Approved by | [Sponsor / COO] |

## Purpose

Establish the measurable baseline (current state) and target outcomes (future state) for the transformation, so benefits are traceable from business case through hypercare and benefit realization.

## KPI Register (Current vs. Target)

| KPI ID | Metric | Category | Current Baseline | Target | Measurement Method | Data Source | Frequency | Owner | Tracking Dashboard |
|--------|--------|----------|------------------|--------|--------------------|-------------|-----------|-------|--------------------|
| KPI-001 | System downtime | Operational resiliency | [e.g. X hrs/month] | [e.g. < Y hrs/month] | Monitoring tool uptime report | [APM / monitoring platform] | Weekly | [IT Ops Lead] | [Ops dashboard link/name] |
| KPI-002 | Data accuracy | Data quality | [e.g. X% match rate] | [e.g. ≥ 99.5%] | Data profiling / audit sample | [MDM / DQ tool] | Monthly | [Data Steward] | [DQ dashboard] |
| KPI-003 | Customer complaints | Customer experience | [e.g. X complaints/month] | [e.g. −40%] | Case volume by complaint record type | [Service Cloud reports] | Monthly | [Service Ops Lead] | [CX dashboard] |
| KPI-004 | Transaction processing time | Process efficiency | [e.g. X min/txn] | [e.g. ≤ Y min/txn] | End-to-end cycle time measurement | [Process mining / system logs] | Weekly | [Process Owner] | [Ops dashboard] |
| KPI-005 | Migration success rate | Migration | [n/a — pre-migration] | [e.g. ≥ 99.9% records loaded and validated] | Load reconciliation report per cutover wave | [ETL tool run logs] | Per wave | [Migration Lead] | [Migration dashboard] |
| KPI-006 | Reconciliation exceptions | Data / financial control | [e.g. X exceptions/day] | [e.g. ≤ Y/day, cleared within SLA] | Automated reconciliation job output | [Reconciliation engine] | Daily | [Finance Ops Lead] | [Reconciliation dashboard] |
| KPI-007 | Legacy run cost | Cost | [e.g. $X/year] | [e.g. −Z% after decommission] | Infrastructure + licence + support cost roll-up | [Finance / TBM tooling] | Quarterly | [Programme Sponsor] | [Executive dashboard] |
| KPI-008 | Release frequency / lead time | Delivery | [e.g. X releases/quarter] | [e.g. Y releases/quarter, lead time ≤ Z days] | Release calendar + pipeline metrics | [DevOps / release tooling] | Per release | [Release Manager] | [Delivery dashboard] |

Add or remove rows per engagement. Every KPI must have an owner and a named dashboard before baseline sign-off.

## KPI Definition Detail (one block per KPI)

### KPI-00X — [Metric name]

- **Definition:** [Precise, unambiguous definition of what is measured]
- **Formula:** [e.g. (successful records / total records) × 100]
- **Inclusions / exclusions:** [What counts, what does not]
- **Baseline collection window:** [Period used to establish current value]
- **Target rationale:** [Why this target — benchmark, business case commitment, regulatory SLA]
- **Tolerance / thresholds:** Green [x], Amber [y], Red [z]
- **Linked requirement(s):** BR-xxx / NFR-xxx

## Benefit Realization Mapping

| KPI ID | Business Case Benefit | Benefit Type | Realization Milestone | Accountable Executive |
|--------|----------------------|--------------|----------------------|----------------------|
| KPI-00X | [e.g. reduced cost to serve] | Cost / Revenue / Risk / CX | [e.g. 3 months post go-live] | [Role] |

## Measurement Governance

- Baseline values validated and signed off by [role] before design closure
- KPI dashboards reviewed at [weekly status call / steering committee]
- Deviations beyond Red threshold raised to CCB / steering with corrective action
- KPIs re-baselined only via change control, never silently

## Anti-Hallucination Guardrails

- Do not invent baseline numbers — mark as **TBC (to be confirmed with data owner)** until measured
- Cite the data source for every baseline and target
- Targets committed in the business case must not be altered without sponsor approval

## Review Checklist

- [ ] Every KPI has baseline, target, method, source, frequency, owner, dashboard
- [ ] Baselines measured (or explicitly TBC), never assumed
- [ ] Targets traceable to business case or regulatory obligation
- [ ] Thresholds defined for governance escalation
- [ ] No PII or client-specific identifiers

## Related Brain Modules

- [Output Framework](../brain/output-framework.md)
- [Validation Framework](../brain/validation-framework.md)
- [Anti-Hallucination](../brain/anti-hallucination.md)

## Related Knowledge

- [Future State Design](../knowledge/future-state-design.md)
- [Current State Analysis](../knowledge/current-state-analysis.md)
- [Governance Framework](../knowledge/governance-framework.md)

## Related Templates

- [Business Case Template](business-case-template.md)
- [Future State Template](future-state-template.md)

## Related Playbooks

- [Value Stream Mapping Playbook](../playbooks/value-stream-mapping-playbook.md)
- [Digital Transformation Strategy Playbook](../playbooks/digital-transformation-strategy-playbook.md)

## Related Industry Scenarios

- [Readme](../scenarios/README.md)

## Related Interview Topics

- [Future State](../interview-guide/future-state.md)

## Related Examples

- [Brd Excerpt](../../examples/sample-brd/brd-excerpt.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Business case, current-state analysis | **Downstream:** Governance dashboards, benefit realization review | **Validation:** validation-framework.md

## Navigation

- **Previous:** [Issue Log Template](issue-log-template.md)
- **Next:** [Lessons Learned Template](lessons-learned-template.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-03 | BA Practice Lead | Initial KPI baseline template (current vs. target register, benefit mapping, measurement governance) |
