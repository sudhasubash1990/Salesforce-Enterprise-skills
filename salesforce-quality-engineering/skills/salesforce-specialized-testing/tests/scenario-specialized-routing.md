---
title: "Test: Specialized Routing"
module: Salesforce Quality Engineering
category: QE Specialized Skill Tests
document_type: Test Scenario
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, test, routing]
---

# Test: Specialized Routing

## Objective

Verify that requests containing specialized testing keywords are routed to SST.

## Scenarios

### S1 — "What testing do we need for this release?"
- **Input:** General testing strategy question with Salesforce context
- **Expected:** Routes to SST, produces 10-dimension assessment
- **Pass criteria:** Testing Dimension Assessment table present with all 10 rows

### S2 — "Assess security testing for our Experience Cloud portal"
- **Input:** Security-specific testing request
- **Expected:** Routes to SST, Security dimension marked Required, chains to PTA
- **Pass criteria:** Security Assessment section present; PTA chain recommendation included

### S3 — "We need performance testing for our batch jobs"
- **Input:** Performance-specific testing request
- **Expected:** Routes to SST, Performance dimension marked Required
- **Pass criteria:** Performance Advisory section present; no invented metrics; states "evidence not provided" if no data given

### S4 — "Test our MuleSoft integration"
- **Input:** Integration testing request
- **Expected:** Routes to SST, Integration and API dimensions marked Required
- **Pass criteria:** Integration Assessment and API Assessment sections present

### S5 — "What browser testing do we need?"
- **Input:** Compatibility testing request
- **Expected:** Routes to SST, Compatibility dimension marked Required
- **Pass criteria:** Compatibility Assessment section present with browser matrix
