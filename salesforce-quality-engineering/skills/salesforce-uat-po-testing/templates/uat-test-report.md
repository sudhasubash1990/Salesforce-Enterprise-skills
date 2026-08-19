---
title: UAT Test Report Template
module: Salesforce Quality Engineering
category: QE Specialized Skill Template
document_type: template
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, uat-test-report]
---

# UAT Test Report

> Replace placeholders in `[brackets]` with project-specific content.

---

## 1. Intent

**What business validation is being performed:**
[Describe the business validation purpose — e.g., "Validate the new opportunity approval process meets sales team requirements for Q3 release."]

---

## 2. Context

| Attribute | Value |
|-----------|-------|
| Project | [Project name] |
| Release | [Release name / version] |
| Salesforce Cloud(s) | [Sales Cloud, Service Cloud, Experience Cloud, etc.] |
| Business Domain | [Sales, Service, Operations, etc.] |
| UAT Phase | [Planning / Execution / Closure] |
| Date Range | [Start date] — [End date] |

---

## 3. Assumptions

| ID | Assumption | Status |
|----|------------|--------|
| A1 | [Assumption text] | Open / Confirmed / Invalidated |
| A2 | [Assumption text] | Open / Confirmed / Invalidated |

---

## 4. UAT Scope

### In scope

- [Feature / business process 1]
- [Feature / business process 2]

### Out of scope

- [Feature / business process excluded with rationale]

---

## 5. Business Risk Assessment

| Feature / Process | Business Risk | Impact if Failed | Priority |
|-------------------|---------------|------------------|----------|
| [Feature 1] | [Critical / High / Medium / Low] | [Business impact description] | [Must test / Should test] |

---

## 6. Reasoning

[Explain why these scenarios were selected and how they were prioritized — connect to business risk, persona coverage, and AC traceability.]

---

## 7. Business Scenarios

Use the PO-friendly format for each scenario:

### Scenario S-001: [Business Scenario Name]

| Field | Value |
|-------|-------|
| **Business Scenario** | [Plain-language description] |
| **Business Objective** | [Why this matters] |
| **Preconditions** | [What must be true before starting] |
| **Business Steps** | 1. [Step in user's language] |
| **Expected Business Outcome** | [What the user expects to see] |
| **Acceptance Criteria** | [AC ID(s) validated] |
| **Business Risk** | [What goes wrong if this fails] |
| **Evidence Required** | [Screenshots, data confirmation, etc.] |
| **Business Owner** | [Name / role] |
| **UAT Status** | Not Started / In Progress / Passed / Failed / Blocked |

---

## 8. Acceptance Criteria Validation

| AC ID | Acceptance Criterion | Scenario(s) | Evidence | Status |
|-------|----------------------|-------------|----------|--------|
| AC-001 | [AC text] | S-001 | [Evidence ref] | Passed / Failed / Not Tested |

---

## 9. Persona Coverage

| Persona | Scenarios | Coverage Status |
|---------|-----------|-----------------|
| [Persona 1] | S-001, S-003 | Covered |
| [Persona 2] | S-002 | Covered |
| [Persona 3] | — | Gap — scenarios needed |

---

## 10. UAT Test Cases

[List individual test cases derived from business scenarios, using business language.]

| TC ID | Business Scenario | Test Description | Expected Outcome | Status |
|-------|-------------------|------------------|-------------------|--------|
| TC-001 | S-001 | [Business-language test] | [Expected result] | Passed / Failed |

---

## 11. Entry / Exit Criteria

### Entry Criteria

| Criterion | Met? |
|-----------|------|
| [Entry criterion] | Yes / No |

### Exit Criteria

| Criterion | Met? |
|-----------|------|
| [Exit criterion] | Yes / No |

---

## 12. Sign-off Recommendation

**Recommendation:** [Go / Conditional Go / No-Go]

**Rationale:** [Evidence-based reasoning for the recommendation]

**Residual Risks:**
- [Risk 1 — mitigation / acceptance]

---

## 13. Dependencies

| Dependency | Type | Status |
|------------|------|--------|
| [Dependency] | Upstream / Downstream / Data / Environment | Resolved / Open |

---

## 14. Recommended Next Actions

| # | Action | Owner | Target Date |
|---|--------|-------|-------------|
| 1 | [Action item] | [Owner] | [Date] |
