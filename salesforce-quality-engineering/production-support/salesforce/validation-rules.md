---
title: Validation Rules
module: Salesforce Quality Engineering
category: Production Support
document_type: Knowledge Article
version: 0.11.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-18
last_updated: 2026-07-18
tags: [production-support, sprint-9, salesforce]
keywords: [validation-rules, production-support, operational-excellence]
---

# Validation Rules

**Scope:** Sprint 9 Production Support & Operational Excellence — Production Support Lead posture. ITIL 4-aligned; reuse Sprint 7 RCA/defect intelligence and Sprint 5 hypercare/prod-val templates. Do not invent SLA/MTTR values without data.

**Version:** 0.11.0

---

## Purpose

Guide production troubleshooting for Salesforce Validation Rules.
## Business Context

- Production stability protects revenue, trust, and regulatory posture on Salesforce programs.
- Operational excellence closes the loop from go-live through continuous service improvement.
## Lifecycle

- Detect / request → Classify → Respond → Resolve / fulfill → Validate → Close → Improve
- Map Validation Rules into the broader incident–problem–change–release value stream where relevant.
## Roles

- Production Support Lead / Service Delivery Lead
- Release Manager / Change Manager
- Incident / Major Incident Manager
- QE / Hypercare Lead
- Business Product Owner / Process Owner
- Platform / Integration / Security specialists
## Responsibilities

- Protect production; communicate clearly; restore service first when warranted
- Capture evidence for RCA and known errors; feed preventive actions
- Align with CAB/release governance and agreed SLAs/OLAs
## Inputs

- Incident/problem/change tickets
- Monitoring alerts and logs
- Release/deploy packages and runbooks
- Business impact statements
## Outputs

- Operational decisions, checklists, communications, and reports
- Known errors / knowledge articles / improvement actions
## Activities

- Confirm symptoms, persona, time window, and recent changes
- Check monitoring/logs; isolate config vs code vs data vs integration
- Apply workaround; open problem if recurring
- Update knowledge / runbook
## KPIs

- Define program KPIs with baselines—do not invent percentages
- Examples: MTTA, MTTR, SLA attainment, reopen rate, change success rate
## SLAs

- Use contracted or program SLAs/OLAs; mark TBC if not provided
- Separate response vs resolution targets by severity
## Risks

- Incomplete impact assessment or weak rollback readiness
- Communication gaps during major incidents
- Bypassing change control under pressure
## Best Practices

- Restore service first for Sev1; schedule deep RCA after stabilization
- Keep war-room / bridge discipline; single source of truth for status
- Link incidents → problems → known errors → changes
- Reuse runbooks; update after every major event
## Examples

- Illustrative: Sev1 integration outage → major incident bridge → workaround → PIR → problem record
- Replace with program ticket IDs and real timestamps when available
## Interview Questions

- How do you apply Validation Rules on an enterprise Salesforce program?
- How do ITIL practices interact with Agile/SAFe release trains?
- What evidence proves production is healthy after a release?
## References

- ITIL 4 service value system (practice alignment—not certification dump)
- ISTQB Advanced Test Management (release/ops quality interfaces)
- Salesforce Well-Architected (reliable, secure, performant)
- DevOps / continuous delivery operational feedback loops
## Related Documents

- [4A/4B knowledge](../../knowledge/README.md)
- [Sprint 7 Salesforce QI hotspots](../../quality-intelligence/knowledge-base/salesforce-quality-intelligence.md)
- [QE Brain (Sprint 1)](../../brain/README.md)
- [Requirement Analysis (Sprint 2)](../../knowledge/requirement-analysis.md)
- [Test Design Engine (Sprint 3)](../../knowledge/test-design-engine.md)
- [Platform Foundation 4A](../../knowledge/platform/README.md)
- [Enterprise Knowledge 4B](../../knowledge/clouds/README.md)
- [Documentation Generator (Sprint 5)](../../templates/README.md)
- [ADO Delivery Intelligence (Sprint 6)](../../ado/README.md)
- [Defect Intelligence (Sprint 7)](../../quality-intelligence/README.md)
- [Automation Intelligence (Sprint 8)](../../automation-intelligence/README.md)
- [README.md](README.md)
- [../README.md](../README.md)
- [../production-support-engine.md](../production-support-engine.md)

## Navigation

- **Previous:** [Flows](flows.md)
- **Next:** [Permission Sets](permission-sets.md)
- **See Also:** [../README.md](../README.md)

## Future Enhancements

- Program-specific SLA overlays under outputs/<project>/
- Deeper monitoring tool adapters (optional later)
