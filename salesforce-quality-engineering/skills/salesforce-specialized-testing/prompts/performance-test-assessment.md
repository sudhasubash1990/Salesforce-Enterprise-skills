---
title: Performance Test Assessment Prompt
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompts
document_type: Prompt
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, performance-testing, prompt]
---

# Performance Test Assessment Prompt

## Usage

Use when performance risk assessment is needed. This is advisory only.

## Prompt

```
Assess performance testing needs for the following Salesforce implementation:

**Performance context:**
- Data volumes: [record counts, projected growth]
- Concurrent users: [expected user count]
- Batch processing: [batch jobs, scheduled Apex]
- Integrations: [callout-heavy flows, bulk API usage]
- UI complexity: [Lightning pages, component count]
- Governor limit concerns: [known SOQL/DML/CPU risks]

**Produce:**
1. Performance Advisory identifying risk areas
2. Governor limit proximity assessment (from code review, not execution)
3. Recommendations for performance engineering engagement

CRITICAL: Do NOT invent response times, throughput numbers, or SLA compliance claims.
If no performance evidence is provided, state: "Performance evidence not provided — measurements required from performance engineering."
```
