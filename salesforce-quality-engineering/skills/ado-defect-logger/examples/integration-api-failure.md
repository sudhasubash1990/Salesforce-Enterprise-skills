---
title: "Example: Integration API Failure Defect"
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, example, integration-api]
---

# Example: Integration API Failure Defect

## Input (Tester Report)

> "The nightly Account sync from ERP to Salesforce failed. 847 out of 2,300 Account records were not created. The integration log shows HTTP 400 errors with 'REQUIRED_FIELD_MISSING: Required fields are missing: [Industry]' for the failed records."

**Environment:** Integration Sandbox (SFINT-03), Middleware: MuleSoft, ERP: SAP S/4HANA

## 1. Intent

Log a defect for a bulk integration failure caused by missing required field mapping.

## 2. Context

| Dimension | Value |
|-----------|-------|
| Project | ERP-Salesforce Integration |
| Sprint | Sprint 8 |
| Salesforce Cloud | Sales Cloud |
| Component | Account sync integration (MuleSoft → Salesforce REST API) |
| Environment | Integration Sandbox SFINT-03 |
| Reporter | Integration Tester |
| Date reported | 2026-08-19 |

## 3. Defect Analysis

| Dimension | Assessment |
|-----------|------------|
| Is this a defect? | Yes — 37% record failure rate in integration sync |
| Title | [Integration] Account sync fails for 847 records — REQUIRED_FIELD_MISSING: Industry |
| Category | Integration / Data |
| Severity | 2-High — Significant data sync failure, partial load |
| Priority | 2-High — Blocks integration testing; data completeness at risk |
| Reproducibility | Always (same records fail on re-run) |
| Business impact | 37% of Accounts not synced; downstream processes (Opportunity, Contact) affected |
| Technical impact | Salesforce validation rule requires Industry; ERP records lack mapped value |

## 4. ADO Defect

### Title

`[Integration] Account sync fails for 847/2300 records — REQUIRED_FIELD_MISSING: Industry`

### Severity: 2-High | Priority: 2

### Repro Steps

1. Trigger the nightly Account sync job in MuleSoft (SFINT-03 environment)
2. Wait for job completion (approximately 15 minutes for 2,300 records)
3. Check MuleSoft integration log for the sync run
4. Observe 847 records with HTTP 400 status
5. Open error detail for any failed record — observe error: `REQUIRED_FIELD_MISSING: Required fields are missing: [Industry]`
6. Query Salesforce: `SELECT COUNT() FROM Account WHERE CreatedDate = TODAY` — observe only 1,453 records created

### Expected Result

All 2,300 Account records from ERP are successfully created in Salesforce.

### Actual Result

Only 1,453 of 2,300 records created. 847 records fail with `REQUIRED_FIELD_MISSING: Required fields are missing: [Industry]`. The failed ERP records have null or unmapped values in the Industry-equivalent field.

### Evidence

| Type | Reference |
|------|-----------|
| Error message | `REQUIRED_FIELD_MISSING: Required fields are missing: [Industry]` |
| Integration log | MuleSoft job log, run ID: JOB-20260819-001 |
| SOQL validation | `SELECT COUNT() FROM Account WHERE CreatedDate = TODAY` → 1,453 |
| ERP data sample | 847 SAP records have null `BRANCHE` (Industry) field |

## 5. Root Cause Hypothesis

- **Category:** Integration / Data
- **Hypothesis:** The field mapping between SAP `BRANCHE` and Salesforce `Industry` does not handle null values. The Salesforce validation rule or field requirement makes Industry mandatory, but 847 ERP source records have no value. The mapping needs a default value or the validation rule needs review.
- **Confidence:** High
- **Evidence needed:** Confirm if Industry is required via validation rule or field property; review MuleSoft mapping for null handling; confirm with business if a default Industry value is acceptable

## 6. Regression Impact

- **Regression?** No — first integration test cycle with full data volume
- **Release impact:** Blocks integration testing completion

## 7. Quality Gates

All gates pass.

## 8. Dependencies

| Type | Description |
|------|-------------|
| Upstream requirement | INT-012: Nightly Account sync from SAP to Salesforce |
| Related | Data mapping specification v2.1 |
| Blocked by | Decision on default Industry value for unmapped ERP records |

## 9. Recommended Next Actions

1. Integration team to add null-handling for Industry field in MuleSoft mapping
2. Business to decide: default Industry value or allow null (requires validation rule change)
3. After fix, re-run sync with same 2,300 records and verify 100% success
4. Add data quality check to integration monitoring dashboard

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
