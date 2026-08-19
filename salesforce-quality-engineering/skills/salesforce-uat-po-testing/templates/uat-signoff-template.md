---
title: UAT Sign-off Template
module: Salesforce Quality Engineering
category: QE Specialized Skill Template
document_type: template
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, uat-signoff]
---

# UAT Sign-off Document

---

## 1. UAT Summary

| Attribute | Value |
|-----------|-------|
| Project | [Project name] |
| Release | [Release name / version] |
| UAT Duration | [Start date] — [End date] |
| UAT Lead | [Name] |
| Business Owner | [Name] |
| Participants | [List of UAT participants by role] |

---

## 2. Execution Summary

| Metric | Count |
|--------|-------|
| Total scenarios planned | [N] |
| Scenarios executed | [N] |
| Passed | [N] |
| Failed | [N] |
| Blocked | [N] |
| Not executed | [N] |

---

## 3. Defect Summary

| Severity | Open | Resolved | Deferred | Total |
|----------|------|----------|----------|-------|
| Sev-1 Critical | [N] | [N] | [N] | [N] |
| Sev-2 High | [N] | [N] | [N] | [N] |
| Sev-3 Medium | [N] | [N] | [N] | [N] |
| Sev-4 Low | [N] | [N] | [N] | [N] |

---

## 4. Acceptance Criteria Traceability

| AC ID | Criterion | Scenario | Evidence | Status |
|-------|-----------|----------|----------|--------|
| AC-001 | [AC text] | S-001 | [Evidence ref] | Passed / Failed |

---

## 5. Persona Coverage

| Persona | Tested? | Notes |
|---------|---------|-------|
| [Persona 1] | Yes / No | [Coverage notes] |

---

## 6. Exit Criteria Assessment

| Exit Criterion | Met? | Notes |
|----------------|------|-------|
| All critical scenarios executed | Yes / No | [Details] |
| No open Sev-1 / Sev-2 defects | Yes / No | [Details] |
| AC fully traced | Yes / No | [Details] |
| Business owner sign-off obtained | Yes / No | [Details] |

---

## 7. Residual Risks

| Risk | Business Impact | Mitigation | Accepted By |
|------|----------------|------------|-------------|
| [Risk description] | [Impact] | [Mitigation plan] | [Name / role] |

---

## 8. Recommendation

**Recommendation:** [Go / Conditional Go / No-Go]

**Rationale:**
[Evidence-based reasoning for the recommendation. Reference execution summary, defect status, AC traceability, and residual risks.]

---

## 9. Post-Go-Live Validation Plan

*(Complete if Conditional Go)*

| Item | Validation | Owner | Target Date |
|------|-----------|-------|-------------|
| [Deferred item] | [How it will be validated post-go-live] | [Owner] | [Date] |

---

## 10. Sign-off

| Name | Role | Decision | Date | Signature |
|------|------|----------|------|-----------|
| [Name] | Business Owner | Go / No-Go | [Date] | _________ |
| [Name] | Product Owner | Go / No-Go | [Date] | _________ |
| [Name] | UAT Lead | Go / No-Go | [Date] | _________ |
| [Name] | Release Manager | Go / No-Go | [Date] | _________ |
