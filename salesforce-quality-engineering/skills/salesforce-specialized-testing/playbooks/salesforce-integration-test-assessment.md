---
title: Integration Test Assessment Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, integration-testing, playbook]
---

# Integration Test Assessment Playbook

## Purpose

Structured workflow for assessing integration testing scope.

## Assessment Steps

### Step 1 — Inventory Integrations
- List all external systems connected to Salesforce
- Identify integration pattern per system (REST, SOAP, event, middleware)
- Document data flow direction (inbound, outbound, bidirectional)

### Step 2 — Assess Authentication
- Named Credentials and OAuth flows
- Token lifecycle (acquisition, refresh, expiry)
- Certificate-based auth, API keys

### Step 3 — Assess Data Flow
- Field mapping between systems
- Data transformation rules
- Error handling and retry logic
- Idempotency and duplicate detection

### Step 4 — Assess Async Processing
- Platform Events and CDC subscriptions
- Batch Apex, Queueable, Future methods
- Retry behavior and dead letter handling

### Step 5 — Assess Error Scenarios
- External system unavailable
- Timeout handling
- Partial success in bulk operations
- Data validation failures across boundaries

### Step 6 — Document Assessment
- Produce Integration Assessment section in SST report
- List integration test scenarios at assessment level
- Identify environment dependencies (sandbox connectivity, mock services)

## Output

Integration Assessment section (section 7 of 18-section SST report).

## Related

- [Integration Testing Knowledge](../knowledge/integration-testing.md)
- [API Test Assessment](salesforce-api-test-assessment.md)
