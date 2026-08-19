---
title: Scenario — Sign-off Readiness
module: Salesforce Quality Engineering
category: QE Specialized Skill Test
document_type: test-scenario
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, test, signoff-readiness]
---

# Test Scenario — Sign-off Readiness Validation

## Objective

Verify that Go/No-Go recommendations are evidence-based, use the correct template, and do not fabricate metrics.

## Test Cases

### TC-1: Go recommendation with evidence

**Input:** "All 15 scenarios passed, no open defects, all AC traced. Recommend sign-off."
**Expected:** Go recommendation citing the evidence provided
**Pass criteria:**
- Recommendation is "Go"
- References: 15/15 scenarios passed, 0 open defects, AC traceability complete
- No invented additional metrics

### TC-2: No-Go recommendation

**Input:** "3 Sev-1 defects open, 5 of 12 scenarios not executed, 2 AC have no test evidence"
**Expected:** No-Go recommendation with clear rationale
**Pass criteria:**
- Recommendation is "No-Go"
- Lists each blocking factor with business impact
- Does not soften the recommendation with invented workarounds

### TC-3: Conditional Go with risk acceptance

**Input:** "All critical scenarios passed, 2 Sev-3 defects open, 1 persona not fully tested due to unavailability"
**Expected:** Conditional Go with documented risks
**Pass criteria:**
- Recommendation is "Conditional Go"
- Lists residual risks: open Sev-3 defects, persona coverage gap
- Requires risk acceptance from business owner
- Includes post-go-live validation plan

### TC-4: No fabricated percentages

**Input:** "Give me a UAT completion summary"
**Expected:** Summary uses actual counts and evidence
**Pass criteria:** No statements like "87% pass rate" or "estimated 95% coverage" unless those numbers are derived from provided data
