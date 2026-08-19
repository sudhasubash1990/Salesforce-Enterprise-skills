---
title: Traceability Matrix Template
module: Salesforce Quality Engineering
category: QE Specialized Skill Template
document_type: Template
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-test-case-designer, template, traceability]
---

# Traceability Matrix Template

## Forward Traceability (Requirement → Test)

| Requirement ID | Requirement Title | Business Rules | Acceptance Criteria | Test Scenarios | Test Cases | Coverage Status |
|---------------|-------------------|----------------|--------------------:|----------------|------------|-----------------|
| BR-XXX | [Title] | BRU-XXX | AC-XXX | TS-XXX | TC-XXX | Full / Partial / Gap |

## Backward Traceability (Test → Requirement)

| Test Case ID | Test Case Title | Test Scenario | AC | Business Rule | Requirement | Link Status |
|-------------|-----------------|---------------|-----|---------------|-------------|-------------|
| TC-XXX | [Title] | TS-XXX | AC-XXX | BRU-XXX | BR-XXX | Linked / Orphan |

## Coverage Summary

| Metric | Count |
|--------|-------|
| Total requirements | |
| Fully covered | |
| Partially covered | |
| Not covered (gaps) | |
| Total test cases | |
| Linked test cases | |
| Orphan test cases | |

## Gap Analysis

| Requirement ID | Title | Gap Reason | Recommended Action |
|---------------|-------|-----------|-------------------|
| [BR-XXX] | [Title] | [Why not covered] | [Action needed] |

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
