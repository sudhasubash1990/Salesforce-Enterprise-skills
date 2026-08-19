---
title: Defect Quality Standards
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, defect-quality]
---

# Defect Quality Standards

What makes a good defect report, and when to reject a vague one.

## Characteristics of a Good Defect

1. **Reproducible** — Another tester can follow the steps and see the same result
2. **Specific** — Identifies the exact component, page, field, or action
3. **Evidence-based** — Includes screenshots, logs, error messages, or data
4. **Isolated** — Describes one defect, not a bundle of issues
5. **Contextualized** — States environment, user profile, data conditions
6. **Traceable** — Links to requirement, test case, or user story
7. **Impact-stated** — Describes business and technical impact

## Repro Step Quality Checklist

- [ ] Steps are numbered sequentially
- [ ] Each step is a single atomic action
- [ ] Login credentials / profile / persona specified
- [ ] Navigation path is explicit (not "go to the record")
- [ ] Test data values included where relevant
- [ ] Observation point is clear ("observe that..." or "notice that...")
- [ ] Expected result stated
- [ ] Actual result stated with evidence

## Evidence Requirements by Defect Type

| Defect Type | Minimum Evidence |
|-------------|-----------------|
| UI | Screenshot + browser + screen resolution |
| Functional | Input data + expected vs actual + requirement reference |
| Integration | API request/response + status code + timestamps |
| Data | Record ID + field values (expected vs actual) + SOQL |
| Security | User profile + action attempted + error message |
| Performance | Operation + response time + acceptable threshold |
| Flow | Flow name + version + input variables + fault message |
| Apex | Class/method + exception + stack trace |

## Rejection Criteria

Reject and request clarification when:

| Condition | Action |
|-----------|--------|
| No repro steps | Ask for numbered steps |
| No expected vs actual | Ask what should happen vs what happens |
| No environment specified | Ask which org/sandbox/browser |
| Vague description only | Ask specific clarifying questions |
| Multiple issues in one defect | Ask to split into separate defects |
| Enhancement disguised as defect | Redirect to user story process |
| Cannot determine affected component | Ask for page/object/Flow name |

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
