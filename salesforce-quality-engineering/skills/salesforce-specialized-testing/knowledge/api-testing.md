---
title: Salesforce API Testing
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, api-testing]
---

# Salesforce API Testing

## Purpose

Reference for assessing Salesforce API testing scope within SST.

## API Categories

| API | Use Case | Key Test Focus |
|-----|----------|----------------|
| **REST API** | CRUD, queries, composite | Payload, status codes, error format |
| **SOAP API** | Enterprise/partner integration | WSDL compliance, session management |
| **Bulk API 2.0** | High-volume data operations | Job lifecycle, batching, error records |
| **Streaming API** | Real-time notifications | PushTopic, Generic, CDC subscription |
| **Metadata API** | Deployment and configuration | Component retrieval, deploy status |
| **Tooling API** | Developer operations | Query, CRUD on metadata |
| **Composite API** | Multi-operation requests | Subrequest ordering, all-or-none, reference IDs |
| **GraphQL API** | Flexible queries | Schema introspection, query depth, errors |

## Test Categories

### Request/Response Validation
- Correct HTTP method, headers, content-type
- Response body structure matches expected schema
- Pagination (nextRecordsUrl) handling

### Status Code Validation
- 200/201 success paths
- 400 bad request — malformed payload, missing required fields
- 401 unauthorized — expired token, invalid credentials
- 403 forbidden — insufficient permissions
- 404 not found — invalid record ID, deleted record
- 500 server error — unhandled Apex exception

### Authentication
- OAuth token acquisition and refresh
- Session ID management and expiration
- Connected app scope enforcement

### Schema and Contract Testing
- JSON schema validation for custom APIs
- API version backward compatibility
- Field additions are non-breaking; removals are breaking

### Negative and Boundary Testing
- Governor limit boundaries (100 SOQL, 150 DML, 200 records composite)
- Max field length payloads
- Special characters, unicode, null values
- Concurrent API calls and rate limiting

## Related

- [Integration Testing](integration-testing.md)
- [Specialized Testing Model](specialized-testing-model.md)
