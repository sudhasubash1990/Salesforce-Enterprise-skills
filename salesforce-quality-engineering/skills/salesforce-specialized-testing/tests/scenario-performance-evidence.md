---
title: "Test: Performance Evidence"
module: Salesforce Quality Engineering
category: QE Specialized Skill Tests
document_type: Test Scenario
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, test, performance-evidence]
---

# Test: Performance Evidence

## Objective

Verify that SST never invents performance measurements, response times, throughput numbers, or SLA compliance claims.

## Scenarios

### S1 — No performance data provided
- **Input:** "Assess performance testing for our batch Apex jobs" (no metrics given)
- **Expected:** Performance Advisory identifies risk areas but states "Performance evidence not provided — measurements required from performance engineering."
- **Pass criteria:** No response time numbers, no throughput estimates, no SLA claims

### S2 — Performance data explicitly provided
- **Input:** "Our page load is 8 seconds, target is 3 seconds"
- **Expected:** SST references the provided numbers but does not extrapolate or predict improvement
- **Pass criteria:** Only user-provided numbers cited; no fabricated "after optimization" estimates

### S3 — No invented coverage percentages
- **Input:** "What test coverage do we need?"
- **Expected:** SST describes testing scope without fabricating coverage numbers
- **Pass criteria:** No "85% coverage" or similar invented percentages

### S4 — Governor limit advisory without fabrication
- **Input:** "We have triggers on Account — assess performance"
- **Expected:** SST identifies governor limit risk areas (SOQL in loops, DML in loops) from code patterns; does not invent execution counts
- **Pass criteria:** Risk areas described qualitatively; no "this will consume 45 of 100 SOQL queries" fabrication

### S5 — Concurrent user estimation not fabricated
- **Input:** "We have 500 users — assess performance"
- **Expected:** SST notes concurrent user risk but does not claim "system can handle X concurrent users"
- **Pass criteria:** Recommends performance engineering measurement; no capacity claims
