---
title: Defect Analysis Report Template
module: Salesforce Quality Engineering
category: QE Specialized Skill Template
document_type: Template
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, defect-analysis-report]
---

# Defect Analysis Report Template

9-section analysis report produced for every defect.

---

## 1. Intent

<!-- What is the user asking? Log defect / Analyze issue / Triage / Reproduce -->

## 2. Context

| Dimension | Value |
|-----------|-------|
| Project | |
| Sprint | |
| Salesforce Cloud | |
| Component | |
| Environment | |
| Reporter | |
| Date reported | |

## 3. Defect Analysis

| Dimension | Assessment |
|-----------|------------|
| Is this a defect? | Yes / No / Needs clarification |
| Title | |
| Category | |
| Severity | |
| Priority | |
| Reproducibility | |
| Business impact | |
| Technical impact | |

## 4. ADO Defect

<!-- Full structured defect per ado-defect-template.md -->

## 5. Root Cause Hypothesis

- **Category:**
- **Hypothesis:**
- **Confidence:**
- **Evidence supporting:**
- **Evidence needed:**

## 6. Regression Impact

- **Regression?** Yes / No / Unknown
- **Previously working in:**
- **Release impact:**

## 7. Quality Gates

| Gate | Status |
|------|--------|
| Repro steps numbered and reproducible | Pass / Fail |
| Expected vs actual clear | Pass / Fail |
| Severity and priority justified | Pass / Fail |
| No vague descriptions | Pass / Fail |
| Evidence provided | Pass / Fail |
| Root cause hypothesis present | Pass / Fail |

## 8. Dependencies

| Type | Description |
|------|-------------|
| Upstream requirement | |
| Related defect | |
| Related test case | |
| Blocked by | |

## 9. Recommended Next Actions

1. <!-- Action 1 -->
2. <!-- Action 2 -->
3. <!-- Action 3 -->

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
