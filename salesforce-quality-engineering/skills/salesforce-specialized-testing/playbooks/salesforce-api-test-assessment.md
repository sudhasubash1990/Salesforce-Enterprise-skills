---
title: API Test Assessment Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, api-testing, playbook]
---

# API Test Assessment Playbook

## Purpose

Structured workflow for assessing API testing scope.

## Assessment Steps

### Step 1 — Inventory APIs
- Salesforce standard APIs in use (REST, SOAP, Bulk, Composite, Streaming, GraphQL)
- Custom REST/SOAP endpoints (Apex REST, Apex SOAP)
- API versions in use

### Step 2 — Assess Request/Response Contracts
- Expected request payloads and headers
- Expected response structure and status codes
- Error response format and codes

### Step 3 — Assess Authentication Requirements
- OAuth flow type per API consumer
- Token management and refresh
- Connected app scope validation

### Step 4 — Assess Negative and Boundary Scenarios
- Governor limit boundaries (SOQL, DML, CPU, heap)
- Max payload sizes, field length limits
- Invalid data types, missing required fields
- Rate limiting behavior

### Step 5 — Assess Contract Stability
- API version backward compatibility
- Breaking vs non-breaking changes
- Schema evolution strategy

### Step 6 — Document Assessment
- Produce API Assessment section in SST report
- Categorize API tests: functional, security, negative, boundary, contract

## Output

API Assessment section (section 9 of 18-section SST report).

## Related

- [API Testing Knowledge](../knowledge/api-testing.md)
- [Integration Test Assessment](salesforce-integration-test-assessment.md)
