---
title: UAT Sign-off Model
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: knowledge
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, uat-signoff]
---

# UAT Sign-off Model

## Purpose

Defines the governance model for UAT sign-off, Go/No-Go decisions, and production readiness assessment from a business perspective.

## Sign-off Authority

| Role | Authority |
|------|-----------|
| **Business Owner / Sponsor** | Final Go/No-Go decision |
| **Product Owner** | Validates acceptance criteria met; recommends sign-off |
| **UAT Lead** | Confirms execution completeness; presents evidence |
| **Release Manager** | Validates deployment readiness (technical side) |
| **Compliance / Legal** | Signs off on regulatory scenarios (when applicable) |

## Go/No-Go Criteria

### Go — proceed to production

| Criterion | Evidence Required |
|-----------|-------------------|
| All critical business scenarios passed | Scenario execution log with evidence |
| All acceptance criteria validated | AC traceability matrix — all green |
| No open Sev-1 or Sev-2 defects | Defect log filtered by severity |
| Business owner confirms readiness | Signed sign-off document |
| Rollback plan documented | Rollback procedure reviewed by Release Manager |
| Training / communications complete | Training completion records |

### No-Go — defer to next release

| Trigger | Action |
|---------|--------|
| Open Sev-1 defect with no workaround | Fix and re-test; defer release |
| Critical business process blocked | Escalate to business owner for risk decision |
| Insufficient scenario coverage | Extend UAT window or reduce scope |
| Data quality issues block validation | Resolve data issues; re-execute affected scenarios |
| Regulatory scenario failed | Mandatory fix before go-live |

### Conditional Go — proceed with known risks

| Condition | Requirement |
|-----------|-------------|
| Open Sev-2 defects with workarounds | Business owner accepts risk in writing |
| Partial persona coverage | Deferred personas documented with planned follow-up |
| Non-critical scenario gaps | Post-go-live validation plan agreed |

## Risk-Based Sign-off

Classify outstanding items by business risk:

| Risk Level | Definition | Sign-off Impact |
|------------|------------|-----------------|
| **Critical** | Business cannot operate; regulatory breach | Blocks Go |
| **High** | Significant business process disruption | Blocks Go unless mitigated |
| **Medium** | Workaround available; limited impact | Conditional Go with documented risk |
| **Low** | Cosmetic or minor inconvenience | Go with post-go-live fix plan |

## Production Readiness Checklist (Business Perspective)

- [ ] All business-critical processes validated end-to-end
- [ ] All personas tested with representative scenarios
- [ ] Acceptance criteria fully traced to evidence
- [ ] Business owner briefed on residual risks
- [ ] Rollback / contingency plan communicated
- [ ] Help desk / support team briefed on changes
- [ ] End-user training completed
- [ ] Go-live communications sent
- [ ] Post-go-live validation plan in place

## Sign-off Document Structure

1. **UAT Summary** — scope, duration, participants
2. **Execution Summary** — scenarios executed, passed, failed, blocked
3. **Defect Summary** — open defects by severity with business impact
4. **AC Traceability** — acceptance criteria → scenario → evidence
5. **Residual Risks** — outstanding items with mitigation / acceptance
6. **Recommendation** — Go / No-Go / Conditional Go with rationale
7. **Sign-off Block** — name, role, date, signature

## Related

- [UAT Framework](uat-framework.md)
- [Business Acceptance](business-acceptance.md)
