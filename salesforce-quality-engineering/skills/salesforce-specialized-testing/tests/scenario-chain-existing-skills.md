---
title: "Test: Chain Existing Skills"
module: Salesforce Quality Engineering
category: QE Specialized Skill Tests
document_type: Test Scenario
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, test, chain-skills]
---

# Test: Chain Existing Skills

## Objective

Verify that SST chains to PTA, DMQA, MIA, and RBRR instead of duplicating their capabilities.

## Scenarios

### S1 — Security dimension chains to PTA
- **Input:** Request involving permission or sharing changes
- **Expected:** SST produces Security Assessment section with scope; explicitly chains to PTA for detailed test scenarios
- **Pass criteria:** "Chain to PTA" appears; no detailed CRUD/FLS test cases produced by SST

### S2 — Data dimension chains to DMQA
- **Input:** Request involving data migration
- **Expected:** SST produces Data Assessment section with scope; chains to DMQA for migration validation
- **Pass criteria:** "Chain to DMQA" appears; no detailed migration reconciliation steps produced by SST

### S3 — Release dimension chains to MIA
- **Input:** Request involving deployment to production
- **Expected:** SST produces Release Assessment section; chains to MIA for metadata impact
- **Pass criteria:** "Chain to MIA" appears; no detailed metadata dependency analysis produced by SST

### S4 — Regression dimension chains to RBRR
- **Input:** Request with changes affecting existing functionality
- **Expected:** SST produces Regression Assessment section; chains to RBRR for prioritization
- **Pass criteria:** "Chain to RBRR" appears; no detailed regression test case list produced by SST

### S5 — Multiple chains in single assessment
- **Input:** Complex release with security + data + deployment + regression impact
- **Expected:** All four chains appear in Recommended Next Actions
- **Pass criteria:** PTA, DMQA, MIA, RBRR all listed with priority in section 18
