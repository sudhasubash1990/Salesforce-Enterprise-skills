---
title: Salesforce Integration Testing
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, integration-testing]
---

# Salesforce Integration Testing

## Purpose

Reference for assessing Salesforce integration testing scope within SST.

## Integration Patterns

| Pattern | Protocol | Testing Focus |
|---------|----------|---------------|
| **REST API** | HTTP/JSON | Endpoints, payloads, status codes, auth headers |
| **SOAP API** | XML/WSDL | WSDL contract, envelope structure, fault handling |
| **Platform Events** | Pub/sub | Event publish, subscribe, replay ID, ordering, high-volume |
| **Change Data Capture** | Event-driven | Entity selection, gap detection, replay, event schema |
| **Named Credentials** | OAuth / basic | Token refresh, credential rotation, permission scope |
| **OAuth flows** | OAuth 2.0 | Authorization code, client credentials, JWT bearer |
| **Webhooks / Outbound Messaging** | HTTP POST | Delivery, retry, acknowledgment, ordering |
| **Middleware** | MuleSoft / Boomi / Informatica | Transformation, routing, error handling, monitoring |

## Key Test Areas

### Async Processing
- Queueable, Batch, Future — execution order, retry on failure, chaining limits
- Platform Event trigger — replay after failure, subscriber checkpoint

### Error Handling
- Timeout behavior (callout timeout vs Apex CPU limit)
- Retry logic — exponential backoff, max retries, dead letter
- Circuit breaker patterns — fallback behavior when external system unavailable

### Idempotency
- Duplicate message detection — external ID, unique constraints
- Replay safety — processing the same event twice produces same result
- Bulk deduplication — handling duplicates within a batch

### Data Mapping
- Field mapping accuracy between systems
- Data type conversions and format transformations
- Null/empty handling across system boundaries

## Related

- [../../../knowledge/](../../../knowledge/) — QE knowledge base
- [API Testing](api-testing.md) — API-specific testing details
- [Specialized Testing Model](specialized-testing-model.md)
