---
title: Healthcare Enrollment
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.22.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [omnistudio-qa, example]
---

# Healthcare Enrollment

## Business Scenario

Healthcare member enrollment Industries journey.

## OmniStudio Components

OmniScript EnrollMember; DR Load Member; Decision Table PlanEligibility; IP CreateCoverage; FlexCard Benefits.

## Test Objectives

Validate eligibility, member create, coverage create.

## Test Scenarios

Eligible enroll; ineligible; dependent add.

## Backend Validation

SOVA stubs for member/coverage objects (API TBC).

## Expected Results

Eligible path creates coverage; benefits card updates.

## Negative Scenarios

HIPAA-sensitive field exposure; IP failure; missing dependent data.

## QA Recommendations

Chain PTA for sensitive FLS; never invent PHI samples — use synthetic TDG.
