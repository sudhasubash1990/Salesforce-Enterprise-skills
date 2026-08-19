---
title: Test Case Report Template
module: Salesforce Quality Engineering
category: QE Specialized Skill Template
document_type: Template
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-test-case-designer, template, report]
---

# Test Case Report Template

10-section output template for ATCD deliverables.

---

## 1. Intent

**Request:** [Summarize what was requested]
**Test Design Goal:** [What the test cases aim to validate]

## 2. Context

| Dimension | Value |
|-----------|-------|
| Salesforce Cloud | [Sales / Service / Experience / etc.] |
| Objects in Scope | [List of objects] |
| Personas | [List of personas] |
| Environment | [SIT / UAT / Staging] |
| Sprint / Release | [Iteration] |

## 3. Assumptions

- `[ASSUMPTION]` [Assumption 1]
- `[ASSUMPTION]` [Assumption 2]

## 4. Requirement Analysis

| Requirement ID | Description | Testable Conditions | Business Rules |
|---------------|-------------|-------------------|----------------|
| [BR/FR-XXX] | [Summary] | [Conditions extracted] | [BRU-XXX] |

## 5. Test Design Approach

| Technique | Applied To | Rationale |
|-----------|-----------|-----------|
| [Technique] | [Feature/field] | [Why selected] |

## 6. Test Cases

_(Insert ADO test cases here using `ado-test-case-template.md` format or user-provided custom template)_

## 7. Traceability Matrix

| Requirement | Business Rule | AC | Test Scenario | Test Case | Coverage |
|-------------|--------------|-----|---------------|-----------|----------|
| [BR-XXX] | [BRU-XXX] | [AC-XXX] | [TS-XXX] | [TC-XXX] | Full / Partial / Gap |

## 8. Quality Gates

| Gate | Status |
|------|--------|
| Requirement understandable | Pass / Fail / Flag |
| AC available or assumed | Pass / Fail / Flag |
| Assumptions labeled | Pass / Fail / Flag |
| Test data identified | Pass / Fail / Flag |
| Persona identified | Pass / Fail / Flag |
| Expected results measurable | Pass / Fail / Flag |
| No vague expected results | Pass / Fail / Flag |

## 9. Dependencies

| Dependency | Type | Status |
|-----------|------|--------|
| [Dependency] | Upstream / Downstream / Data / Environment | [Status] |

## 10. Recommended Next Actions

- [ ] [Action 1]
- [ ] [Action 2]
- [ ] [Action 3]

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
