---
title: Performance Test Assessment Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, performance-testing, playbook]
---

# Performance Test Assessment Playbook

## Purpose

Structured workflow for assessing performance testing needs. **Advisory only — never invent measurements.**

## Assessment Steps

### Step 1 — Identify Performance-Sensitive Areas
- Pages with many components or large related lists
- APIs handling high-volume or real-time traffic
- Batch processing on large datasets
- Flows with loops or complex logic

### Step 2 — Assess Governor Limit Proximity
- Review trigger bulkification patterns
- Identify SOQL in loops, DML in loops
- Assess CPU time risk for complex logic
- Review heap usage for large collections

### Step 3 — Assess Data Volume Impact
- Object record counts (current and projected)
- Query selectivity and custom indexes
- Archive and purge strategy
- Large data volume (LDV) patterns

### Step 4 — Assess Concurrency Risks
- Expected concurrent user count
- Record locking contention
- Sharing recalculation triggers
- Async job queue capacity

### Step 5 — Document Advisory
- Produce Performance Advisory section in SST report
- List risk areas without inventing numbers
- Recommend performance engineering engagement for measurement
- If no evidence available, state: *"Performance evidence not provided"*

## Hard Rules

- **Never** produce response time estimates
- **Never** claim SLA compliance without evidence
- **Never** fabricate throughput numbers
- **Always** recommend measurement by performance engineering when risk is identified

## Output

Performance Advisory section (section 10 of 18-section SST report).

## Related

- [Performance Testing Knowledge](../knowledge/performance-testing.md)
