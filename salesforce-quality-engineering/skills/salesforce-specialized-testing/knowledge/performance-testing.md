---
title: Salesforce Performance Testing
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, performance-testing]
---

# Salesforce Performance Testing

## Purpose

Advisory reference for assessing performance testing needs within SST. **SST never invents performance measurements.** If no evidence is available, state: *"Performance evidence not provided — measurements required from performance engineering."*

## Performance Risk Areas

| Area | Risk Indicators | What to Assess |
|------|----------------|----------------|
| **Page load** | Complex Lightning pages, many components, large related lists | Component count, flexipage complexity |
| **API response** | High-volume API calls, complex queries, large payloads | Query selectivity, payload size, callout chains |
| **Bulk operations** | Data loader, Bulk API, mass updates | Record volume, trigger complexity, batch size |
| **Large datasets** | Tables > 1M records, complex relationships | Query plans, selective indexes, archive strategy |
| **Concurrent users** | High user count, shared record contention | Locking, sharing recalculation, async capacity |
| **Flow performance** | Complex screen flows, loops, subflows | Loop iterations, DML in loops, interview limits |
| **Integration latency** | External callouts, middleware hops | Callout timeout settings, retry overhead |
| **Governor limits** | SOQL queries, DML operations, CPU time, heap | Trigger bulkification, query optimization |
| **Batch processing** | Scheduled jobs, batch Apex, queueable chains | Batch size, execution time, scheduling conflicts |

## Assessment Approach

1. **Identify risk areas** from implementation context
2. **Flag areas requiring measurement** — do not estimate values
3. **Recommend performance engineering engagement** for measurement
4. **Document known governor limit proximity** based on code review (not execution)

## What SST Does NOT Do

- Produce response time estimates
- Claim SLA compliance without evidence
- Fabricate throughput numbers
- Predict concurrent user capacity
- Generate load test scripts (recommend tooling only)

## Related

- [Specialized Testing Model](specialized-testing-model.md)
- [../../../knowledge/](../../../knowledge/) — QE knowledge base
