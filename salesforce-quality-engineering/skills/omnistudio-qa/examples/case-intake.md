---
title: Case Intake
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

# Case Intake

## Business Scenario

Service case intake via OmniScript for contact centers.

## OmniStudio Components

OmniScript CaseIntake; DR Load Case; FlexCard CaseSummary; IP EnrichCustomer.

## Test Objectives

Validate case create, enrichment, and summary card.

## Test Scenarios

Billing inquiry; technical issue; escalate.

## Backend Validation

SOVA: Case fields and Account link.

## Expected Results

Case created with correct Type/Reason.

## Negative Scenarios

Missing contact; enrichment timeout; duplicate case.

## QA Recommendations

Chain AFT if Agentforce assists intake.
