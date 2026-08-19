---
title: UAT Framework
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: knowledge
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, uat-framework]
---

# UAT Framework

## Purpose

Defines the end-to-end framework for planning, scoping, executing, and closing User Acceptance Testing on Salesforce implementations.

## UAT Phases

### Phase 1 — UAT Planning

1. **Identify business stakeholders** — who owns sign-off, who participates
2. **Define UAT scope** — which features, business processes, and personas
3. **Establish entry criteria** — what must be true before UAT begins
4. **Set exit criteria** — what constitutes UAT completion
5. **Allocate resources** — UAT testers, environments, data, timelines
6. **Create communication plan** — status cadence, escalation paths

### Phase 2 — Scope Definition

- Map user stories / requirements to UAT scenarios
- Identify in-scope vs. out-of-scope features
- Prioritize scenarios by business risk (High / Medium / Low)
- Confirm persona coverage — every impacted role has scenarios
- Document assumptions and constraints

### Phase 3 — Business Scenario Identification

- Derive scenarios from acceptance criteria, not from technical specs
- Include happy-path, exception, and edge-case business flows
- Validate scenarios with business owners before execution
- Ensure end-to-end journey coverage (not isolated feature tests)

### Phase 4 — UAT Execution

- Execute scenarios in a production-like environment
- Record evidence (screenshots, data confirmations)
- Log defects using business-impact classification
- Track progress against entry/exit criteria
- Conduct daily stand-ups with UAT participants

### Phase 5 — UAT Closure

- Compile UAT status report
- Validate all exit criteria are met
- Produce sign-off recommendation with evidence traceability
- Conduct Go/No-Go assessment
- Document deferred items and residual risks

## Entry Criteria

| Criteria | Description |
|----------|-------------|
| SIT complete | System Integration Testing passed with no critical open defects |
| Environment ready | UAT environment deployed, configured, and accessible |
| Test data available | Realistic business data loaded and verified |
| UAT testers trained | Business users briefed on process, tools, defect logging |
| Acceptance criteria defined | Every in-scope story has testable AC |
| UAT plan approved | UAT strategy and scope signed off by business owner |

## Exit Criteria

| Criteria | Description |
|----------|-------------|
| All critical scenarios executed | 100% of high-priority business scenarios run |
| No open critical/high defects | All Sev-1 and Sev-2 defects resolved or deferred with risk acceptance |
| AC validated | Every acceptance criterion has traced test evidence |
| Business owner sign-off | Formal sign-off from authorized business stakeholder |
| Residual risks documented | Deferred items and known issues logged with mitigation |

## Scope Definition Guidelines

### In-scope signals

- Features in the current release with user stories and AC
- Business processes changing as part of the release
- Personas impacted by the release
- Regulatory requirements tied to released features

### Out-of-scope signals

- Features not changing in this release (unless regression risk)
- Technical infrastructure changes without business-facing impact
- Performance / load testing (separate testing stream)

## Related

- [PO Testing Model](po-testing-model.md)
- [Business Acceptance](business-acceptance.md)
- [UAT Sign-off](uat-signoff.md)
