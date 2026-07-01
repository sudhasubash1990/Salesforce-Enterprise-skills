---
title: Discovery Workshop Notes
module: Salesforce Business Analyst
category: Shared
document_type: Reference
version: 1.1.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/consulting-principles.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/interview-index.md]
related_examples: [examples/sample-project/README.md]
related_documents: [docs/metadata-schema.md, shared/traceability-model.md]
keywords: [discovery workshop notes]
tags: [discovery-workshop-notes]
---

# Discovery Workshop Notes — Apex Manufacturing

---
title: Discovery Workshop — Sales & Service Transformation
type: workshop-notes
version: 1.0.0
status: approved
last_updated: 2026-05-20
project: PRJ-APEX-MFG-001
---

## Session Details

| Field | Value |
|-------|-------|
| Date | 2026-05-18 |
| Duration | 4 hours |
| Facilitator | Senior BA |
| Attendees | VP Sales, Service Director, 4 sales reps, 3 service agents, IT lead |

## Objectives

1. Validate AS-IS sales and service processes
2. Identify top pain points and priorities
3. Capture initial requirement themes for BRD

## AS-IS Summary (Sales)

- Leads entered in spreadsheet, manually imported weekly
- Opportunities tracked in Salesforce but products quoted in ERP
- No visibility into dealer pipeline

**Pain points (ranked):**

1. Duplicate accounts (ERP vs CRM)
2. No mobile access for field reps
3. Forecast based on rep self-reporting only

## AS-IS Summary (Service)

- Cases in Salesforce; warranty claims in email
- Dealers call support line for order status
- Knowledge in SharePoint, not linked to Cases

## TO-BE Themes (Draft)

| Theme | Description | Priority |
|-------|-------------|----------|
| Single customer record | ERP is system of record for Account; CRM enriches | Must |
| Dealer self-service | Portal for cases and order lookup | Should |
| Unified quoting path | Evaluate CPQ vs ERP-led quoting | Must (decision needed) |

## Requirements Captured

| ID | Statement | Source |
|----|-----------|--------|
| BR-001 | Single Account view synced from ERP daily | Workshop |
| BR-002 | Field reps must log activities on mobile offline-capable | Interview |
| BR-005 | Dealers submit cases via portal with attachment support | Workshop |

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D-01 | ERP remains product master | IT constraint |
| D-02 | Phase CPQ evaluation to Release 2 | Timeline |

## Open Questions

1. Dealer portal: Experience Cloud vs existing DXP?
2. Offline mobile: Salesforce Mobile offline limits acceptable?
3. Data residency for dealer users in EU?

## Next Steps

- [ ] Process mapping session for case escalation (week of 5/25)
- [ ] ERP integration discovery with David Park
- [ ] Draft BRD sections 1–4

## Related Brain Modules

- [Consulting Principles](../../salesforce-business-analyst/brain/consulting-principles.md)

## Related Knowledge

- [Readme](../../salesforce-business-analyst/knowledge/README.md)

## Related Templates

- [Readme](../../salesforce-business-analyst/templates/README.md)

## Related Playbooks

- [Readme](../../salesforce-business-analyst/playbooks/README.md)

## Related Industry Scenarios

- [Readme](../../salesforce-business-analyst/scenarios/README.md)

## Related Interview Topics

- [Interview Index](../../salesforce-business-analyst/interview-guide/interview-index.md)

## Related Examples

- [Readme](../sample-project/README.md)

## Related Documents

- [Metadata Schema](../../docs/metadata-schema.md)
- [Traceability Model](../../shared/traceability-model.md)

## Traceability

**Upstream:** Governance | **Downstream:** All modules | **Validation:** glossary consistency

## Navigation

- **Previous:** —
- **Next:** —
- **See Also:** [cross-linking-framework](../../docs/cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
