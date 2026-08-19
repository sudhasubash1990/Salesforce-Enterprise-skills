---
title: Root Cause Analysis Framework
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, root-cause-analysis]
---

# Root Cause Hypothesis Framework

Structured approach to hypothesizing root causes for Salesforce defects at logging time. For deep RCA lifecycle, see [quality-intelligence/root-cause-analysis/](../../../quality-intelligence/root-cause-analysis/).

## Root Cause Categories

| Category | Description | Common Signals |
|----------|-------------|----------------|
| **Configuration** | Incorrect declarative setup | Wrong picklist values, page layout issues, record type mapping, assignment rules |
| **Metadata** | Metadata dependency or deployment issue | Missing field, broken formula reference, incomplete change set |
| **Code** | Apex, LWC, or trigger defect | Unhandled exception, null pointer, governor limit, incorrect logic |
| **Integration** | API, middleware, or callout failure | HTTP errors, timeout, payload mismatch, auth failure, missing mapping |
| **Data** | Data quality or migration issue | Missing records, incorrect field values, duplicate data, orphan records |
| **Permission** | Security model misconfiguration | CRUD violation, FLS restriction, sharing rule gap, profile/perm set issue |

## Hypothesis Template

For each defect, provide:

```
Root Cause Hypothesis:
- Category: [Configuration | Metadata | Code | Integration | Data | Permission]
- Hypothesis: [Specific statement of what went wrong]
- Confidence: [High | Medium | Low]
- Evidence supporting: [What evidence points to this cause]
- Evidence needed: [What additional investigation would confirm/refute]
- Suggested investigator: [Role best positioned to confirm]
```

## Hypothesis Confidence Levels

| Level | Criteria |
|-------|----------|
| **High** | Error message or log directly points to cause; similar pattern seen before |
| **Medium** | Symptoms are consistent with the hypothesis but multiple causes possible |
| **Low** | Educated guess based on component type; limited evidence available |

## Salesforce-Specific RCA Patterns

| Pattern | Likely Root Cause | Investigation |
|---------|-------------------|---------------|
| `FIELD_CUSTOM_VALIDATION_EXCEPTION` | Validation rule conflict | Check validation rules on object |
| `INSUFFICIENT_ACCESS_OR_READONLY` | Permission gap | Check profile, permission set, OWD, sharing rules |
| `System.LimitException` | Governor limit | Review SOQL queries, DML operations, CPU time |
| Flow fault with `$Flow.FaultMessage` | Flow logic error | Check Flow version, decision elements, fault paths |
| `System.NullPointerException` | Missing null check in Apex | Review Apex class/trigger at stack trace line |
| HTTP 401/403 from integration | Auth/permission issue | Check Named Credential, Connected App, remote system |
| HTTP 500 from integration | Remote system error | Check remote system logs, payload format |
| Records not appearing | Sharing model | Check OWD, sharing rules, role hierarchy |

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
