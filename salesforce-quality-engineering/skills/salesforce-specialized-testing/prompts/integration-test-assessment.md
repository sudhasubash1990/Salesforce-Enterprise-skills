---
title: Integration Test Assessment Prompt
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompts
document_type: Prompt
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, integration-testing, prompt]
---

# Integration Test Assessment Prompt

## Usage

Use when the primary concern is integration and API testing scope.

## Prompt

```
Assess the integration and API testing scope for the following Salesforce implementation:

**Integration context:**
- External systems: [list systems and integration patterns]
- APIs: [REST, SOAP, Bulk, Platform Events, CDC]
- Middleware: [MuleSoft, Boomi, Informatica, custom]
- Authentication: [Named Credentials, OAuth, certificates]
- Data flow: [inbound, outbound, bidirectional]
- Async processing: [Batch, Queueable, Future, Platform Events]

**Produce:**
1. Integration Assessment with pattern analysis, auth, data flow, async, error handling, idempotency
2. API Assessment with request/response, status codes, negative, boundary, contract testing scope
3. Environment dependencies and mock service needs

Label all assumptions. Do not invent performance metrics for integration latency.
```
