---
title: "Example: Salesforce Flow Failure Defect"
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, example, flow-failure]
---

# Example: Salesforce Flow Failure Defect

## Input (Tester Report)

> "When I create a new Case with Record Type = 'Complaint' and save, I get a Flow error. The case is saved but the auto-assignment to the Complaints Queue doesn't happen. This worked last sprint."

**Environment:** QA Sandbox (SFQA-02), Winter '26, Chrome 128, Sales Operations profile

## 1. Intent

Log a defect for a Record-Triggered Flow failure on Case creation.

## 2. Context

| Dimension | Value |
|-----------|-------|
| Project | Service Cloud Implementation |
| Sprint | Sprint 14 |
| Salesforce Cloud | Service Cloud |
| Component | Record-Triggered Flow: Case_Auto_Assignment |
| Environment | QA Sandbox SFQA-02 |
| Reporter | QA Tester |
| Date reported | 2026-08-19 |

## 3. Defect Analysis

| Dimension | Assessment |
|-----------|------------|
| Is this a defect? | Yes — deviation from previously working behavior |
| Title | [Flow] Case Auto-Assignment Flow fails for Complaint Record Type |
| Category | Automation / Flow |
| Severity | 2-High — Cases not routed to correct queue; manual workaround required |
| Priority | 2-High — Affects all Complaint Cases; workaround is manual reassignment |
| Reproducibility | Always (per tester report, confirmed in last sprint it worked) |
| Business impact | Complaint Cases not reaching Complaints Queue, SLA risk |
| Technical impact | Flow fault path triggered; Case saved but automation incomplete |

## 4. ADO Defect

### Title

`[Flow] Case Auto-Assignment Flow fails for Complaint Record Type`

### Severity: 2-High | Priority: 2

### Repro Steps

1. Log in to QA Sandbox SFQA-02 as Sales Operations profile user
2. Navigate to Cases tab → click "New Case"
3. Select Record Type = "Complaint"
4. Fill required fields: Contact = "Test Contact", Subject = "Test Complaint", Description = "Test"
5. Click "Save"
6. Observe the Flow error toast message on the Case record page
7. Check the Owner field — observe it shows the creating user, not "Complaints Queue"

### Expected Result

Case is saved and automatically assigned to the "Complaints Queue" via the Case_Auto_Assignment Flow.

### Actual Result

Case is saved but a Flow error appears. The Case Owner remains the creating user. Auto-assignment to Complaints Queue does not execute.

### Evidence

| Type | Reference |
|------|-----------|
| Error message | Flow fault: "An unhandled fault has occurred in flow Case_Auto_Assignment" |
| Environment | QA Sandbox SFQA-02, Winter '26 |
| Previous behavior | Working in Sprint 13 (confirmed by tester) |

## 5. Root Cause Hypothesis

- **Category:** Configuration / Metadata
- **Hypothesis:** A metadata change in Sprint 14 (possibly to the Complaint Record Type or the Flow entry criteria) caused the Flow to fault. The Flow may reference a field or value that was modified or removed.
- **Confidence:** Medium
- **Evidence needed:** Compare Flow version between Sprint 13 and Sprint 14; check if Record Type API name changed; review Flow fault detail in debug log

## 6. Regression Impact

- **Regression?** Yes — worked in Sprint 13
- **Previously working in:** Sprint 13 build
- **Release impact:** Workaround available (manual queue assignment) but blocks UAT sign-off for Complaint management

## 7. Quality Gates

| Gate | Status |
|------|--------|
| Repro steps numbered and reproducible | Pass |
| Expected vs actual clear | Pass |
| Severity and priority justified | Pass |
| No vague descriptions | Pass |
| Evidence provided | Pass |
| Root cause hypothesis present | Pass |

## 8. Dependencies

| Type | Description |
|------|-------------|
| Upstream requirement | US-045: Complaint Cases auto-assigned to Complaints Queue |
| Related test case | TC-112: Verify Case auto-assignment by Record Type |

## 9. Recommended Next Actions

1. Developer to review Flow `Case_Auto_Assignment` version history and debug log
2. Compare metadata between Sprint 13 and Sprint 14 deployments (use MIA)
3. After fix, run regression on all Record Type-specific Flows

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
