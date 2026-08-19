---
title: "Example: Integration Testing Assessment"
module: Salesforce Quality Engineering
category: QE Specialized Skill Examples
document_type: Example
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, integration-testing, example]
---

# Example: Integration Testing Assessment

> Integration and API testing assessment for a MuleSoft middleware + REST API implementation connecting Salesforce to an external billing system.

## 1. Intent

Assess integration and API testing scope for a new billing integration: Salesforce → MuleSoft → External Billing System (REST API), with Platform Events for async notifications.

## 2. Context

| Attribute | Value |
|-----------|-------|
| Salesforce Clouds | Sales Cloud |
| Key Features | Opportunity-to-Invoice, Platform Events |
| Integrations | MuleSoft → Billing System (REST), Platform Events |
| Environment | Developer sandbox |

## 3. Assumptions

| ID | Assumption | Status |
|----|-----------|--------|
| A1 | Billing system test environment available | Assumed |
| A2 | OAuth client credentials flow via Named Credential | Assumed |
| A3 | Platform Events used for invoice status updates | Assumed |

## 4. Implementation Analysis

When an Opportunity is Closed Won, a Flow triggers a Platform Event. MuleSoft subscribes, calls the billing system REST API to create an invoice, and publishes an Invoice_Status__e Platform Event back to Salesforce to update the Opportunity.

## 5. Testing Dimension Assessment

| Dimension | Required | Rationale | Chain Skill |
|-----------|----------|-----------|-------------|
| Security | No | No security model changes | — |
| Integration | Yes | MuleSoft + Platform Events + billing API | — |
| Data | No | No data migration | — |
| API | Yes | REST API contract validation | — |
| Performance | Yes | High-volume opportunity closures | Advisory |
| Accessibility | No | No UI changes | — |
| Mobile | No | No mobile requirements | — |
| Compatibility | No | No UI changes | — |
| Regression | Yes | Opportunity process changes | RBRR |
| Release/Deployment | Yes | New Flow, Platform Event, Named Credential | MIA |

## 7. Integration Assessment

### Outbound: Salesforce → MuleSoft → Billing
- Flow triggers Platform Event on Opportunity Closed Won
- MuleSoft subscribes to Platform Event, transforms payload, calls billing REST API
- **Test:** Event published with correct payload fields
- **Test:** MuleSoft transformation accuracy (Opportunity fields → Invoice fields)
- **Test:** Billing API called with correct auth and payload

### Inbound: Billing → MuleSoft → Salesforce
- Billing system sends invoice status webhook to MuleSoft
- MuleSoft publishes Invoice_Status__e Platform Event
- Salesforce trigger updates Opportunity
- **Test:** Invoice status correctly mapped to Opportunity field
- **Test:** Replay ID handling for missed events

### Error Handling
- **Test:** Billing system unavailable — MuleSoft retry behavior (3 retries, exponential backoff)
- **Test:** Malformed response from billing — error logged, no Salesforce update
- **Test:** Platform Event publish failure — error handling in Flow
- **Test:** Duplicate event processing — idempotency via external ID

### Async Processing
- **Test:** Platform Event delivery order under bulk Opportunity closures
- **Test:** Subscriber checkpoint recovery after failure
- **Test:** High-volume Platform Event limits (max events/hour)

## 9. API Assessment

### Billing System REST API
- `POST /invoices` — Create invoice from Opportunity data
- `GET /invoices/{id}` — Retrieve invoice status
- **Status codes:** 201 (created), 400 (validation error), 401 (auth failure), 409 (duplicate), 503 (unavailable)
- **Contract:** JSON schema for invoice request/response validated against API spec
- **Negative:** Missing required fields, invalid currency, negative amounts
- **Boundary:** Maximum line items per invoice, field length limits

## 10. Performance Advisory

**Risk areas identified:**
- Bulk Opportunity closure (e.g., quarter-end) generating many simultaneous Platform Events
- MuleSoft callout chain latency (Salesforce → MuleSoft → Billing → MuleSoft → Salesforce)
- Platform Event daily limit consumption

*Performance evidence not provided — measurements required from performance engineering.*

## 16. Quality Gates

| Gate | Status | Evidence |
|------|--------|----------|
| Dimension assessment complete | Pass | 10 dimensions assessed |
| Chain skills identified | Pass | RBRR, MIA |
| No invented metrics | Pass | Performance stated as "evidence not provided" |
| Assumptions labeled | Pass | A1–A3 documented |

## 18. Recommended Next Actions

| # | Action | Skill | Priority |
|---|--------|-------|----------|
| 1 | Integration test execution with billing sandbox | Manual | High |
| 2 | API contract validation (schema tests) | Manual | High |
| 3 | Regression scope for Opportunity process | RBRR | Medium |
| 4 | Metadata impact analysis for deployment | MIA | Medium |
| 5 | Performance engineering for bulk event testing | External | Medium |
