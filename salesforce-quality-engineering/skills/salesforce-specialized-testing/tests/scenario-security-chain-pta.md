---
title: "Test: Security Chain PTA"
module: Salesforce Quality Engineering
category: QE Specialized Skill Tests
document_type: Test Scenario
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, test, security-chain-pta]
---

# Test: Security Chain PTA

## Objective

Verify that SST correctly assesses security scope and chains to PTA without producing detailed security test cases.

## Scenarios

### S1 — Experience Cloud with guest user
- **Input:** "We're launching an Experience Cloud portal with guest access"
- **Expected:** SST identifies Security as Required; assesses CRUD/FLS, sharing, guest user scope; chains to PTA
- **Pass criteria:** Security Assessment references guest user risks; "Chain to PTA" present; no Given/When/Then test scenarios in SST output

### S2 — Permission set changes
- **Input:** "We're adding new permission sets for the sales team"
- **Expected:** SST identifies Security as Required; assesses PS scope; chains to PTA
- **Pass criteria:** Security Assessment references least privilege review; PTA chain present

### S3 — API security with connected apps
- **Input:** "New connected app for external system integration"
- **Expected:** SST identifies Security as Required; assesses OAuth scope, connected app permissions; chains to PTA
- **Pass criteria:** API security scope documented; PTA chain present for detailed validation

### S4 — No security changes
- **Input:** "We're updating a Flow that doesn't change permissions"
- **Expected:** SST marks Security as Not Required with rationale
- **Pass criteria:** Security dimension "No" with explanation; no PTA chain; no security test content

### S5 — Sharing model restructure
- **Input:** "We're changing OWD from Public to Private for Cases and adding sharing rules"
- **Expected:** SST identifies Security as Required (Critical); assesses OWD, sharing rules, cascading impact; chains to PTA
- **Pass criteria:** Sharing model impact documented; PTA chain with High/Critical priority
