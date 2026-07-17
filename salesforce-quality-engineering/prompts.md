---
title: Prompts
module: Salesforce Quality Engineering
category: Root
document_type: Guide
version: 0.14.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-18
review_cycle: quarterly
related_documents:
  - salesforce-quality-engineering/skill.md
  - salesforce-quality-engineering/validation/README.md
  - salesforce-quality-engineering/enterprise-orchestrator/README.md
  - salesforce-quality-engineering/enterprise-quality/README.md
  - salesforce-quality-engineering/production-support/README.md
  - salesforce-quality-engineering/production-support/operations-intelligence/README.md
  - salesforce-quality-engineering/automation-intelligence/README.md
  - salesforce-quality-engineering/quality-intelligence/README.md
  - salesforce-quality-engineering/ado/README.md
  - salesforce-quality-engineering/templates/README.md
  - salesforce-quality-engineering/brain/response-guidelines.md
keywords: [prompts]
tags: [prompts, sprint-10]
---

# Prompts

**Purpose:** Prompting standards through Sprint 11 Validation, Certification & Continuous Improvement.

**Scope:** Behaviour + Sprint 2–11 prompts. Never invent metrics, maturity scores, SLA/MTTR, ROI, flake %, coverage %, compliance certifications, or certification levels without evidence.

**Owner:** QE Practice Lead

**Version:** 0.14.0

**Status:** Draft (Sprint 11)

---

## How This AI Should Behave

Load [skill.md](skill.md), route via [enterprise-orchestrator/](enterprise-orchestrator/README.md), then Sprint 1–10 modules as applicable—including [enterprise-quality/](enterprise-quality/README.md) for CQO-level advisory.

- Synthesize prior engines; do not duplicate deep Sprint 7–9 content unnecessarily.
- Executive outputs: outcomes, residual risk, confidence, fewer high-impact actions.
- Compliance = overview/TBC unless Legal confirms.

## Expected Reasoning Flow

```
Classify request
  → … (Sprints 2–9 paths as applicable)
  → enterprise-quality/ advisory engine (if maturity/health/portfolio/exec/audit/roadmap)
  → Produce artifact
  → Completeness gate + response guidelines
```

## Expected Answer Structure

Use [brain/response-guidelines.md](brain/response-guidelines.md). For requirement inputs, Body = mandatory sections in [knowledge/requirement-analysis.md](knowledge/requirement-analysis.md).

---

## Standard Prompts (Sprint 2)

### Requirement Review

```
Act as a senior Salesforce QE consultant. Review the following requirement using the Requirement Analysis Engine.
Do NOT generate test cases or RTM.

Requirement:
[paste]

Produce all mandatory analysis sections (Executive Summary through Next Steps),
including Requirement Quality Assessment (1–5 dimensions), gaps, questions, risks, and scope.
```

### Story Analysis

```
Analyse this Salesforce user story for testability and completeness.
Identify missing AC, business rules, security, data, and integration details.
Score requirement quality. List Critical/High clarification questions.
Do not write test cases.

Story:
[paste]
```

### Epic Analysis

```
Perform QE requirement analysis on this epic. Decompose into implied features/stories only as gaps/recommendations (do not invent a full backlog).
Assess scope boundaries, risks, and Salesforce component impact themes.
No test cases.

Epic:
[paste]
```

### Feature Analysis

```
Analyse this Salesforce feature description. Cover As-Is/To-Be if inferable, functional/NFR gaps, component scan, and regression/automation intent.
No test cases or RTM.

Feature:
[paste]
```

### Acceptance Criteria Review

```
Review these acceptance criteria for observability, negative paths, and permission paths.
Flag untestable language and missing AC themes. Suggest improvements for the BA—do not silently rewrite unless asked.
No test cases.

AC:
[paste]
```

### Business Rule Extraction

```
Extract explicit and implied business rules from the requirement. Label implied rules as assumptions with impact.
Map each rule to likely Salesforce component types (VR, Flow, Apex, etc.) without designing implementation.
```

### Risk Identification

```
Identify business, functional, technical, testing, data, security, integration, deployment, and production risks for this requirement.
For each risk: Description, Impact, Probability, Mitigation, Owner, Priority.
```

### Gap Analysis

```
Produce a Requirement Gap Analysis against the validation catalog
(missing rules, AC, error handling, security, data, integration, notifications, reporting, NFR, audit, compliance, deployment).
```

### Clarification Questions

```
Generate clarification questions grouped by Business, Functional, Technical, Data, Security, Integration, Reporting, Automation, Testing, Deployment, Production Support.
Prioritize Critical / High / Medium / Low. Tie each to an analysis step.
```

### Scope Validation

```
Produce scope analysis: In Scope, Out of Scope, Dependencies, Assumptions, Constraints, Open Issues, Future Enhancements.
Flag silent out-of-scope and blocking dependencies.
```

---

## Standard Prompts (Sprint 3 — Test Design)

### Generate Test Scenarios

```
Using the Test Design Engine, generate enterprise test scenario OBJECTIVES for the following requirement.
Include Business, Functional, Negative, Exception, Validation, Permission, Integration, Data, and Regression scenario types as applicable.
Assign Business Critical / High / Medium / Low with rationale.
Do NOT write detailed test case steps.

Requirement / analysis context:
[paste]
```

### Identify Test Design Techniques

```
Select appropriate test design techniques for this requirement and explain WHY each is chosen.
Reference positive/negative/BVA/EP/decision table/state transition/pairwise/exploratory/error guessing/risk-based as applicable.
```

### Analyse Coverage

```
Build a Quality Coverage Matrix (Requirement → Rule → Component → Scenario → Technique → Priority → Automation → Regression).
Assess coverage dimensions and list Covered / Partial / Missing gaps with recommendations.
Do not invent coverage percentages.
```

### Recommend Regression Scope

```
Recommend regression scope (In / Out / Conditional) based on Salesforce component impact and risk.
Explain neighbor features and pack intent. No detailed cases.
```

### Recommend Automation Candidates

```
Classify scenarios: Suitable for Automation / Manual Only / API / UI / Regression Automation / Smoke Automation.
Explain reasoning. Do NOT generate scripts or Playwright code.
```

### Perform Risk-Based Testing

```
Prioritize scenarios using Business Critical / High / Medium / Low.
Explain business/technical risk drivers for each priority band.
```

### Coverage Gap Analysis

```
Perform coverage gap analysis across functional, business rule, validation, integration, security, UI, data, automation, regression, UAT, and production-validation dimensions.
Recommend improvements only—no test case scripts.
```

---

## Standard Prompts (Sprint 4A — Platform Foundation)

### Explain Salesforce Component

```
Act as a senior Salesforce QE architect. Explain this Salesforce component using the Sprint 4A article structure
(Purpose, Business Context, Salesforce Overview, Architecture, Business Usage, Requirement Analysis Guidance,
Testing Considerations, Functional/Negative/Boundary Testing, Regression Testing, Automation Opportunities,
Security/Performance Considerations, Production Risks, Common Defects, Common Root Causes, Best Practices,
Interview Questions).
Load knowledge/platform|automation|security|data as applicable. No Admin setup steps or Apex code.
No detailed test cases.

Component:
[e.g., Master-Detail Relationship / Record-Triggered Flow / Custom Metadata Type]
```

### Explain Metadata

```
Explain this Salesforce metadata type or change from a QE lens.
Use knowledge/metadata/: impact analysis, dependencies, deployment considerations, testing strategy,
regression impact, and metadata risks. Scenario objectives only—no cases/scripts.

Metadata / change:
[paste]
```

### Explain Security Model

```
Explain the Salesforce security model elements implicated here (profiles, permission sets, FLS, OWD,
sharing, roles, restriction rules, MFA, etc.).
Use knowledge/security/. Cover permission testing, negative testing, regression risks, and common security defects.
Objectives only.

Access model / requirement:
[paste]
```

### Explain Automation

```
Explain this Salesforce automation (VR, Flow type, Apex async, approval, assignment/escalation, duplicate, CDC, etc.).
Use knowledge/automation/: purpose, business usage, execution order, testing strategy, negative/regression,
automation readiness, common failures, debugging considerations, best practices.
No scripts. No detailed test cases.

Automation:
[paste]
```

### Analyse Testing Impact

```
Analyse testing impact for this requirement/change using Sprint 4A Platform Foundation + Test Design Engine.
Identify components touched, what/why to test, techniques, scenario objective themes, and coverage gaps.
No detailed test case steps.

Requirement / change:
[paste]
```

### Identify Regression Scope

```
Identify regression scope (In / Out / Conditional) from this Salesforce change.
Use knowledge/metadata (impact + regression impact analysis) and knowledge/regression-planning.md.
List neighbor features and rationale. No detailed cases.

Change / metadata notes:
[paste]
```

### Analyse Metadata Risk

```
Analyse metadata risk for this change list or story.
Cover dependency breaks, deploy/validation risk, config vs customization depth, and production defect patterns.
Use knowledge/metadata/.

Metadata / change:
[paste]
```

### Analyse Security Risk

```
Analyse security risk for this requirement or access design.
Cover over-sharing, FLS leaks, View All/Modify All, guest/integration user risk, and persona negative paths.
Use knowledge/security/.

Requirement / access design:
[paste]
```

### Analyse Data Risk

```
Analyse data risk for this requirement, migration, or data change.
Cover integrity, duplicates, LDV, masking/PII, reconciliation, and migration validation themes.
Use knowledge/data/. Mark regulatory claims TBC with Legal/Compliance—do not invent GDPR/HIPAA rules.

Context:
[paste]
```

---

## Standard Prompts (Sprint 4B — Enterprise Business Knowledge)

### Cloud Analysis

```
Analyse this requirement for the stated Salesforce Cloud(s).
Use knowledge/clouds/<cloud>.md: business processes, common objects, typical users/integrations,
testing considerations, negative testing, regression scope, automation opportunities,
common defects, production issues, release considerations.
Confirm licensed products—do not invent features. Ground platform impact in Sprint 4A.
No detailed test cases / templates / ADO.

Cloud(s) + requirement:
[paste]
```

### Integration Review

```
Review this Salesforce integration from a QE lens.
Use knowledge/integration/: business usage, testing strategy, negative paths, error/retry/timeout,
regression, automation opportunities, production risks, common defects.
No scripts.

Integration description:
[paste]
```

### Managed Package Analysis

```
Analyse this managed/unlocked package change or upgrade for QE impact.
Use knowledge/managed-packages/: dependencies, namespaces, packaged metadata/Apex/Flows,
upgrade testing, regression strategy, vendor coordination, common issues.
No detailed cases.

Package / upgrade context:
[paste]
```

### Performance Risk Assessment

```
Assess performance risk for this Salesforce change or process.
Use knowledge/performance/: governors, SOQL/selectivity, Flow/batch, LDV, locking, concurrency,
report/dashboard/integration performance. Recommend testing focus and monitoring signals.
No load-test scripts unless asked at high level.

Context:
[paste]
```

### Release Readiness Assessment

```
Assess release readiness from a QE evidence perspective.
Use knowledge/release/: deployment/PPV, smoke/sanity, regression planning, Go/No-Go,
rollback, cutover, hypercare, production readiness (knowledge).
List evidence themes and residual risks—not a formal sign-off template.

Release / change context:
[paste]
```

### Industry-Based Testing Strategy

```
Propose an industry-aware testing strategy for this Salesforce program.
Use knowledge/industry/<industry>.md plus relevant clouds.
Cover typical processes, integrations, frequently tested scenarios, regression hotspots,
automation opportunities, and production risks. Mark regulatory items TBC with Compliance.

Industry + program context:
[paste]
```

### Regression Impact Assessment

```
Assess regression impact for this enterprise change.
Combine Sprint 4A metadata impact + Sprint 4B cloud/process/package/integration neighbors.
Produce In / Out / Conditional scope with rationale. Use knowledge/regression-planning.md.
No detailed test cases.

Change description:
[paste]
```

### Production Risk Review

```
Identify production risks for this Salesforce change or release.
Use knowledge/release/ and knowledge/performance/ (and clouds/industry as applicable).
Cover silent process failure, permission drift, integration backlog, volume/concurrency,
and hypercare signals. Recommend verification themes—not a playbook template.

Change / release context:
[paste]
```

---

## Standard Prompts (Sprint 5 — Documentation Generator)

### Generate Test Strategy

```
Generate an enterprise Salesforce Test Strategy using templates/test-strategy.md and
document-generation/test-strategy-generator.md.
Reuse any prior requirement analysis / risks provided. Include Scope, Objectives, Testing Types,
Environment/Resource/Risk/Automation/Regression strategies, Defect Management, Entry/Exit,
Assumptions, Dependencies, Deliverables, Communication, Metrics, Governance.
Mark assumptions. Do not invent coverage %.

Program / release context:
[paste]
```

### Generate Test Plan

```
Generate a Test Plan using templates/test-plan.md and document-generation/test-plan-generator.md.
Include In/Out scope, schedule, environment, resources, test data, risks, dependencies,
milestones, execution plan, reporting, approvals.
Reference the Test Strategy if provided.

Sprint / release context:
[paste]
```

### Generate RTM

```
Generate a Requirement Traceability Matrix using templates/rtm.md and document-generation/rtm-generator.md.
Map: BR → Story → AC → Business Rule → Salesforce Component → Scenario → Case → Automation → Regression → Prod Validation.
Specify RTM view: Business / Sprint / Release / UAT / Regression.
List coverage gaps—do not invent %.

Requirements / scenarios / cases (as available):
[paste]
```

### Generate Test Scenarios

```
Generate enterprise test SCENARIOS using templates/test-scenario-document.md and
document-generation/test-scenario-generator.md (and Test Design Engine).
Include Scenario ID, Objective, Process, Preconditions, Priority, Rules/AC, Risk,
Automation Candidate, Regression Required. Prefer objectives over step scripts unless cases requested.

Requirement / analysis:
[paste]
```

### Generate Test Cases

```
Generate enterprise test CASES using templates/test-case-document.md and
document-generation/test-case-generator.md.
Include Title, Objective, Preconditions, Test Data, Steps, Expected Results, Postconditions,
Priority, Requirement Mapping, Automation Candidate, Smoke/Regression/UAT tags.
Format for: [ADO | Excel | Xray | Zephyr | Manual].
Only after scenarios/AC are clear (or user provides ready inputs).

Scenarios / AC:
[paste]
```

### Generate Defect Report

```
Generate a defect report using templates/defect-report.md and document-generation/defect-generator.md.
Include Summary, Description, Steps, Expected, Actual, Environment, Evidence, Severity, Priority,
Business/Technical Impact, links, Retest notes, Regression impact.
No PII/credentials in evidence descriptions.

Failure details:
[paste]
```

### Generate Daily Status

```
Generate a Daily QA Status using templates/daily-status-report.md.
Include executed today, pass/fail, blockers, new defects, plan for tomorrow.

Execution snapshot:
[paste]
```

### Generate Weekly Report

```
Generate a Weekly QA Report using templates/weekly-status-report.md.
Include highlights, metrics (with sources), defect trends, risks, asks, next week plan.

Week data:
[paste]
```

### Generate Test Summary

```
Generate a Test Summary Report using templates/test-summary-report.md.
Include scope, execution summary, coverage (no invented %), defects, residual risk, recommendations.

Cycle results:
[paste]
```

### Generate Executive Dashboard

```
Generate an Executive QA Dashboard using templates/executive-qa-dashboard.md.
Lead with outcomes, residual risk, and Go/No-Go posture; keep detail concise.

Release / steering inputs:
[paste]
```

---

## Standard Prompts (Sprint 6 — Azure DevOps Delivery Intelligence)

### Generate Epic

```
Generate an Azure DevOps Epic (ADO-ready title + description) using ado/epics/epic.md.
Include business outcome, success criteria, scope themes, risks, and child Feature recommendations.
Link to Salesforce clouds/components if known. No API calls.

Context:
[paste]
```

### Generate Feature

```
Generate an Azure DevOps Feature under the given Epic using ado/features/feature.md.
Include capability outcome, acceptance themes, dependencies, and suggested User Stories.

Epic + context:
[paste]
```

### Generate User Story

```
Generate an Azure DevOps User Story (INVEST) with nested Given/When/Then acceptance criteria.
Use ado/user-stories/user-story.md and align with BA story standards (do not invent BA scope).
Include Area/Iteration placeholders, tags, and testability notes. Leave Story Points empty unless asked.

Feature / requirement:
[paste]
```

### Generate Task

```
Generate Azure DevOps Tasks for the User Story (build vs test tasks as appropriate).
Use ado/tasks/task.md. Keep tasks small and sprint-completable.

User Story:
[paste]
```

### Generate Bug

```
Generate an enterprise Azure DevOps Bug using ado/bugs/bug.md and Sprint 5 defect standards.
Include Title, Summary, Environment, Area, Iteration, Build/Release, Steps, Expected, Actual,
Severity, Priority, Business Impact, Evidence, Regression Impact, Retest Guidance, links.

Failure details:
[paste]
```

### Generate Test Plan

```
Recommend/create an Azure DevOps Test Plan structure using ado/test-plans/ and ado/test-plans-organization.md.
Include naming, purpose, Area/Iteration, and suite strategy (smoke/regression/UAT/release).

Release / sprint context:
[paste]
```

### Generate Test Suite

```
Design Test Suites for a Test Plan: Static / Requirement-based / Query-based as appropriate.
Include Smoke, Regression, UAT, Release suite recommendations and organization rationale.
Use ado/test-suites/test-suite.md.

Plan purpose + scope:
[paste]
```

### Generate Test Case

```
Generate an Azure DevOps Test Case (ADO-ready) using ado/test-cases/test-case.md and Sprint 5 case template.
Include Title, Objective, Area, Iteration, Priority, Requirement Mapping, Preconditions, Test Data,
Steps, Expected, Postconditions, Automation Status, Smoke/Regression/UAT tags, Risk, Owner.

Story / scenario / AC:
[paste]
```

### Generate Dashboard Design

```
Design an Azure DevOps dashboard for audience: [QA Lead | Test Manager | PM | Release Manager | Delivery Manager | Executive].
Use ado/dashboards/. Include Purpose, KPIs, Charts, Filters, Metrics, Decision Support.
No widget JSON required unless asked.

Audience + program context:
[paste]
```

### Generate Traceability Matrix

```
Generate an ADO-oriented traceability view: Epic → Feature → Story → AC → Rule → Scenario → Case → Bug → Regression → Release → Prod Validation.
Use ado/traceability-intelligence.md and templates/rtm.md. List gaps—do not invent coverage %.

Backlog / test inputs:
[paste]
```

### Generate Release Readiness Assessment

```
Produce a release readiness assessment from an ADO evidence perspective.
Use ado/governance/release-readiness.md and Sprint 5 release-readiness / go-no-go checklists.
Recommend queries/dashboards to support the decision. Residual risk explicit.

Release context:
[paste]
```

---

## Standard Prompts (Sprint 7 — Defect Intelligence & Quality Analytics)

### Analyze Defect

```
Act as a Principal Salesforce Quality Engineering advisor. Analyse the following defect using quality-intelligence/defect-management and defect-intelligence-engine.md.
Classify type, severity, priority, lifecycle state, and Salesforce impact (4A/4B).
Recommend detection gaps and preventive actions. Do not invent metrics.
Reuse templates/defect-report.md structure where helpful.

Defect:
[paste]
```

### Perform RCA

```
Perform root cause analysis for the following defect/incident.
Select the most suitable RCA method (5 Whys, Fishbone, Pareto, FTA, or FMEA) and justify.
Separate symptom vs root cause; recommend corrective and preventive actions (CAPA).
Use quality-intelligence/root-cause-analysis/ and templates/defect-rca-report.md.
Mark assumptions and confidence explicitly.

Defect / incident:
[paste]
```

### Identify Defect Pattern

```
Identify defect patterns from the following defect set (recurring, duplicate, regression, hotspot, leakage, automation instability, etc.).
Apply pattern detection rules, assign confidence scores with rationale, and suggest preventive actions.
Use quality-intelligence/defect-patterns/. Do not invent counts—use only provided data.

Defect set / history:
[paste]
```

### Generate Fishbone Analysis

```
Generate a Fishbone (Ishikawa) analysis for the following quality problem.
Categories: People, Process, Platform/Config, Data, Environment, Tools/Automation, Requirements, External.
Use quality-intelligence/root-cause-analysis/fishbone-diagram.md.
List likely causes, evidence needed, and top preventive actions.

Problem statement:
[paste]
```

### Generate 5 Whys

```
Generate a structured 5 Whys analysis for the following defect or process failure.
Stop at a controllable root cause; avoid blaming individuals.
Provide Recommended Output: root cause statement, CAPA, and test/process improvements.
Use quality-intelligence/root-cause-analysis/5-whys.md.

Problem:
[paste]
```

### Predict Release Risk

```
Predict release readiness and quality risks from the following evidence.
Cover high-risk stories/components, likely regression areas, leakage risk, and quality-gate failure risk.
State confidence levels (Low/Medium/High) with rationale. Recommend mitigation plans.
Use quality-intelligence/predictive-quality/ and risk-analysis/. Do not invent KPI values.

Release / sprint evidence:
[paste]
```

### Analyze Quality Trends

```
Analyse quality trends from the following time-series or sprint/release data.
Cover defect, regression, automation, environment, and production signals as applicable.
Provide visualization ideas, interpretation, executive narrative, and improvement recommendations.
Use quality-intelligence/trend-analysis/. Do not invent data points.

Trend data:
[paste]
```

### Generate Executive Quality Report

```
Generate an executive quality report (choose: Quality Health / Sprint / Release / Production / Defect Trend / Risk / RCA / Improvement).
Follow quality-intelligence/knowledge-base report standards. Lead with outcomes and residual risk.
Include metrics only from provided data; mark gaps as TBC. Prevention-first recommendations.

Report type + evidence:
[paste]
```

### Recommend Preventive Actions

```
Based on the following defects, RCA, or patterns, recommend prioritized preventive actions
(requirement, design, config, test, automation, environment, governance).
Link each action to defect type / Salesforce hotspot where relevant.
Use quality-intelligence/continuous-improvement/preventive-actions.md and salesforce-quality-intelligence.md.

Inputs:
[paste]
```

### Generate Lessons Learned

```
Generate a lessons-learned pack from the following release/sprint/incident evidence.
Include what went well, what failed, root themes, CAPA, knowledge-sharing, and training recommendations.
Use quality-intelligence/continuous-improvement/lessons-learned.md and templates/lessons-learned.md.

Context:
[paste]
```

### Apply Quality Intelligence Rules

```
Act as an experienced Salesforce QE consultant. Evaluate the following quality signals using the Quality Intelligence Rules Engine (quality-intelligence/rules/).
For each fired rule: cite Rule ID, IF evidence, THEN actions, priority (P0–P3), suggested owner, and confidence.
Merge duplicate actions. Do not invent metrics or thresholds—use provided values or label indicative defaults.
Prefer actionable recommendations over metrics narrative alone.

Signals / metrics / defect set:
[paste]
Program thresholds (optional):
[paste]
```

### Recommend Actions from Metric Breach

```
Given the metric breach below, apply metric-threshold-rules.md and regression-and-coverage-rules.md.
If Defect Leakage > threshold, recommend expanding targeted regression and reviewing requirement coverage.
Cite Rule IDs (e.g., QI-R-MET-001, QI-R-REG-001). State residual risk.

Metric evidence:
[paste]
```

---

## Standard Prompts (Sprint 8 — Automation Intelligence)

### Recommend Automation Strategy

```
Act as a Principal Salesforce Test Automation Architect. Recommend an automation strategy for the program below.
Use automation-intelligence/automation-strategy/ and automation-intelligence-engine.md.
Cover pyramid, smoke/sanity/regression/API/UI mix, shift-left/right, maturity, and prioritization.
Do NOT generate full scripts. Playwright-first but framework-agnostic.

Program context:
[paste]
```

### Assess Automation Feasibility

```
Assess automation feasibility for the following requirement/scenario using the Automation Decision Engine.
Answer: Should this be automated? Why? Framework? Effort (T-shirt + assumptions)? ROI inputs? Risk? Maintenance? CI/CD readiness? Priority? Confidence.
Do not invent metrics. No full scripts.

Candidate:
[paste]
```

### Compare Automation Frameworks

```
Compare automation frameworks for the Salesforce context below (include Playwright, and others as relevant: Selenium, Cypress, Robot, WebdriverIO, API tools).
Use automation-intelligence/framework-comparison/. Cover strengths, weaknesses, SF suitability, learning curve, maintenance, CI/CD, recommended usage.
State a recommendation with rationale and migration risks if brownfield.

Context:
[paste]
```

### Design Playwright Framework

```
Design an enterprise Playwright framework architecture for Salesforce (layers, POM/COM, fixtures, auth/storage state, API+UI split, config/secrets, parallel, reporting, CI).
Use automation-intelligence/playwright/ and framework-design/. Provide folder structure and standards—NOT full test scripts.

Context:
[paste]
```

### Generate Automation Roadmap

```
Generate a phased automation roadmap (discover → pilot → scale → optimize) with candidates, framework choice, CI milestones, governance, and metrics.
Reuse Sprint 3 automation candidates if provided. No full scripts. Mark assumptions.

Inputs:
[paste]
```

### Identify Automation Candidates

```
From the following stories/scenarios, identify automation candidates vs remain-manual.
Prioritize by risk, frequency, stability, and oracle clarity. Prefer API over UI when appropriate.
Use decision-engine + automation-strategy. Confidence per candidate.

Backlog / scenarios:
[paste]
```

### Estimate Automation ROI

```
Estimate automation ROI for the scope below using metrics/roi.md and automation-strategy/automation-roi.md.
Show formula inputs needed; do not invent financials. Provide qualitative ROI + what data is required for a quantitative case.

Scope:
[paste]
```

### Review Automation Architecture

```
Review the following automation architecture/framework design against Sprint 8 standards (layered design, data, secrets, parallel, CI, governance, SF considerations).
List strengths, gaps, risks, and prioritized improvements. No script rewrites unless asked.

Architecture description / repo outline:
[paste]
```

### Review Existing Automation Framework

```
Act as a Principal Salesforce Test Automation Architect. Run the Automation Review Engine on the existing framework below.
Score all nine dimensions (1–5 or N/A): architecture/modularity, POM/Screenplay quality, locator robustness, test data, CI/CD readiness, reporting/observability, flake/stability, governance, security/secrets.
Compute maintainability score/band/status (Security ≤ 2 ⇒ At Risk). Apply Playwright/Selenium/Cypress lens as applicable.
Produce prioritized P0–P3 improvements (secure & stabilize before rewrite). Use review-report-template.md.
Do not invent flake/coverage %. Do not generate full scripts. Never echo secrets.

Framework evidence (structure, samples, CI, metrics — sanitized):
[paste]
```

### Score Automation Maintainability

```
Using automation-intelligence/review-engine/, produce a maintainability scorecard for the estate below.
Include weighted score, band, overrides, confidence, and top 5 remediation actions with owner cues.

Evidence:
[paste]
```

### Generate CI/CD Strategy

```
Design a CI/CD test automation strategy for Salesforce delivery (ADO Pipelines and/or GitHub Actions/Jenkins as applicable).
Cover build validation, smoke, regression, parallel, promotion, approval/quality gates, result publishing, artifacts, notifications, rollback/deploy validation.
Use automation-intelligence/ci-cd/. Design only—no pipeline YAML dumps unless requested as a sketch.

Context:
[paste]
```

### Analyze Flaky Tests

```
Analyze flaky automation signals below. Apply Sprint 7 QI automation-stability rules and Sprint 8 maintenance/metrics guidance.
Recommend quarantine, root themes (env/data/locator/timing/product), and stabilization backlog. No full script rewrites unless asked.

Flake evidence:
[paste]
```

---

## Standard Prompts (Sprint 9 — Production Support & Operational Excellence)

### Analyze Incident

```
Act as a Salesforce Production Support Lead. Analyse the incident below using production-support/incident-management/.
Classify severity/priority, business impact, likely Salesforce areas (4A/4B), immediate containment, and next steps.
Recommend runbook(s). Do not invent SLA clocks—use provided timestamps or mark TBC.

Incident:
[paste]
```

### Generate RCA

```
Perform operational root cause analysis for the production problem/incident below.
Reuse Sprint 7 QI RCA methods (5 Whys/Fishbone/etc.) via production-support/problem-management/root-cause-analysis.md.
Provide known error, corrective and preventive actions. Confidence explicit.

Evidence:
[paste]
```

### Prepare Go Live Checklist

```
Generate a go-live checklist (tech, data, business, support, rollback, communications, Go/No-Go).
Use production-support/go-live/ and Sprint 5 templates where relevant. Owners and evidence columns required.

Release context:
[paste]
```

### Assess Release Readiness

```
Assess Salesforce release readiness from an operations perspective.
Use production-support/release-operations/release-readiness.md plus go-live/monitoring gates.
List blockers, residual risk, and Go/No-Go recommendation. No invented metrics.

Evidence:
[paste]
```

### Generate Hypercare Plan

```
Create a hypercare plan: team/RACI, activities, monitoring, issue tracking, daily reporting, risks, exit criteria, KT.
Use production-support/hypercare/ and Sprint 5 hypercare templates.

Go-live context:
[paste]
```

### Prepare Major Incident Report

```
Produce a major incident report: timeline, impact, bridge roles, actions, workaround/resolution, communications, PIR actions.
Use incident-management/major-incidents.md and runbooks/major-incident.md.

Incident record:
[paste]
```

### Create Production Validation Checklist

```
Create a production validation checklist for post-deploy smoke/business/technical/data checks by persona.
Use go-live/ and release-operations/production-validation.md. Tie to critical journeys.

Release scope:
[paste]
```

### Generate Support Dashboard

```
Design an operational/executive support dashboard (widgets, KPIs, drill-downs, refresh cadence).
Use executive-reporting/ and operational-analytics/. Mark KPI formulas as needing program data—do not invent values.

Audience + context:
[paste]
```

### Analyze SLA Performance

```
Analyse SLA performance from the data below (response/resolution by severity).
Highlight breaches, trends, and improvement actions. Do not invent attainment %.

SLA data:
[paste]
```

### Generate Operational Health Report

```
Generate a production/operational health report (incidents, changes, releases, monitoring, risks, recommendations).
Use executive-reporting/production-health-report.md and operational-excellence/.

Period + evidence:
[paste]
```

### Create Runbook

```
Create a reusable production runbook with: Purpose, Trigger, Prerequisites, Steps, Validation, Rollback, Communication, Escalation, Success Criteria, Lessons Learned.
Use production-support/runbooks/ structure. Salesforce-specific where applicable.

Scenario:
[paste]
```

### Run Operations Intelligence

```
Act as a Salesforce Operations / Service Delivery Lead. Run the Operations Intelligence Engine on the signals below.
Produce: health score/band + drivers; anomalies; incident correlations; release risk and/or SLA breach risk with confidence; capacity notes; relevant OPS-D-* decisions; prioritized P0–P3 recommendations with owner cues and runbook links.
Do not invent SLA/MTTR/KPI values. Use production-support/operations-intelligence/.

Signals / evidence:
[paste]
```

### Score Production Health

```
Score production health using operations-intelligence/health-scoring.md.
Show dimension scores, weighted band, overrides (Sev1/security), top drivers, and confidence.

Period evidence:
[paste]
```

### Predict Release / SLA Risk

```
Predict release risk and/or SLA breach risk from the evidence below.
Use release-risk-prediction.md and sla-breach-prediction.md. State confidence and mitigations. Cite OPS-D decisions if they fire.

Evidence:
[paste]
```

---

## Standard Prompts (Sprint 11 — Validation & Certification)

### Validate Repository

```
Run repository-validation/ against salesforce-quality-engineering/.
Cover structure, naming, markdown, cross-refs, broken links, duplicates, navigation, README quality, versioning, completeness.
Produce repository scorecard rows with Pass/Partial/Fail and evidence paths. No invented %.

Focus (optional):
[paste]
```

### Validate Requirement Analysis

```
Validate Sprint 2 Requirement Analysis using validation/requirement-validation/ and golden-datasets/requirement-analysis/.
Confirm analysis-before-cases, gaps, risks, questions, component scan. Record Pass/Partial/Fail.
```

### Validate Test Design

```
Validate Sprint 3 Test Design using validation/test-design-validation/ and golden-datasets/test-design/.
Confirm scenarios/coverage/regression/automation candidates before detailed cases.
```

### Validate Documentation

```
Validate Sprint 5 documentation pack using validation/documentation-validation/.
Check strategy/plan/RTM/scenario/case/defect/report/template/playbook/checklist completeness rules.
```

### Validate Azure DevOps Artifacts

```
Validate Sprint 6 ADO guidance using validation/ado-validation/.
Cover hierarchy, Test Plans/Suites/Cases, bugs, queries, dashboards, traceability, relationships.
Do not invent API publish behaviour.
```

### Validate Automation Strategy

```
Validate Sprint 8 using validation/automation-validation/.
Strategy, framework selection, Playwright-first, CI/CD, ROI (no invented numbers), governance, review-engine health.
No full script generation.
```

### Validate Production Readiness

```
Validate Sprint 9 using validation/production-validation/.
Incident/problem, release readiness, hypercare, monitoring, runbooks, ops metrics (no invented SLA), stability.
```

### Benchmark Framework

```
Run an industry benchmark from validation/benchmarking/<industry>/.
Provide Business Context through Evaluation Criteria results.
Industries: utilities|retail|banking|insurance|healthcare|manufacturing|telecommunications|public-sector|energy|consumer-goods
Do not invent regulatory requirements.

Industry:
[name]
```

### Generate Certification Report

```
Using validation/certification/ and completed quality-scorecards/, draft a Certification Report.
Recommend Bronze/Silver/Gold/Platinum/Enterprise Certified/Not ready ONLY from scored evidence.
Never invent an overall percentage or level without scorecard inputs.

Scorecard session notes:
[paste]
```

### Assess Enterprise Readiness

```
Assess enterprise readiness of the QE framework via validation/quality-scorecards/ and enterprise-validation/.
Summarize RAG per area, residual gaps, and whether Proceed to adoption demos is warranted.
```

### Generate Improvement Backlog

```
From validation findings, update/propose items for validation/continuous-improvement/improvement-backlog.md.
Include gaps, duplicates, outdated candidates, and Salesforce release impacts if provided.
Priority High/Medium/Low; no invented velocity metrics.
```

---

## Standard Prompts (Enterprise Orchestrator)

### Orchestrate QE Request

```
Act as the Enterprise Orchestrator for Salesforce Quality Engineering.
1) Classify intent using enterprise-orchestrator/capability-routing-table.md
2) State a one-line Route: Primary sprint · Support · Advisory Yes/No · Pattern ID if multi-hop
3) Load only the selected engine(s); do not duplicate knowledge across sprints
4) If executive / portfolio / maturity / Proceed-Hold decision → sink into Sprint 10 advisory after operational evidence
5) Never invent metrics, maturity scores, SLA/MTTR, or compliance attestations

User request:
[paste]
```

### Route Multi-Capability Request

```
Using enterprise-orchestrator/composition-patterns.md, select the best COMP-* pattern
(or compose a custom ordered hop list). Execute in order, pass IDs/evidence forward,
and produce a unified response with facts vs assumptions.

Request:
[paste]
```

---

## Standard Prompts (Sprint 10 — Enterprise Quality Advisory)

### Assess Project Health

```
Act as an Enterprise Quality Advisor. Assess project health using enterprise-quality/project-health/.
Cover requirements, coverage, automation, defects, release/regression/environment/delivery health, stakeholder engagement, risk exposure.
Produce overall score/RAG, executive summary, recommendations, confidence. Do not invent metrics.

Evidence pack:
[paste]
```

### Assess Quality Maturity

```
Assess quality maturity (TMMi/ISTQB/CQE themes as applicable) using enterprise-quality/quality-maturity/.
Provide current vs target, gaps, improvement plan. Evidence-based levels only—no invented indices.

Context:
[paste]
```

### Assess Automation Maturity

```
Assess automation maturity using quality-maturity/automation-maturity.md and Sprint 8 automation-intelligence (review engine if brownfield evidence provided).
Current/target, gaps, roadmap actions. No invented coverage %.

Evidence:
[paste]
```

### Assess Release Readiness

```
Assess release readiness from an enterprise advisory view (project health + Sprint 9 release ops + decision engine).
Recommend Proceed / Hold / Escalate / Delay / Reduce Scope with confidence and residual risk.

Evidence:
[paste]
```

### Perform Quality Audit

```
Perform a quality audit (choose type or multi-area) using enterprise-quality/quality-audits/.
Produce scorecard, findings, severity, remediation. Reuse Sprint 8 automation review for automation audits.

Scope + evidence:
[paste]
```

### Generate Executive Dashboard

```
Design an executive quality dashboard for the audience below (CIO/CTO/CQO/Program/Delivery/Release/QA/CoE/ARB/Steering).
Include Audience, KPIs (definitions), visualizations, thresholds (program-set), actions, escalation criteria.
Use enterprise-quality/executive-reporting/. Do not invent KPI values.

Audience + context:
[paste]
```

### Generate Portfolio Health Report

```
Generate a portfolio quality health report using enterprise-quality/portfolio-management/.
Heat map narrative, cross-project risks, strategic recommendations. No invented comparative scores.

Portfolio evidence:
[paste]
```

### Assess Architecture Quality

```
Assess Salesforce architecture quality (platform, integration, security, automation, data, debt, risks).
Use enterprise-quality/architecture-quality/ and 4A/4B knowledge. Recommendations with confidence.

Architecture context:
[paste]
```

### Generate Transformation Roadmap

```
Generate a quality transformation roadmap (90-day / 6-month / 12-month automation / CoE / AI / ops excellence / testing strategy as requested).
Use enterprise-quality/roadmaps/. Phases, milestones, success measures, assumptions.

Current state + goals:
[paste]
```

### Recommend Executive Actions

```
Using enterprise-quality decision-engine and recommendation-engine, recommend executive actions
(Proceed/Hold/Escalate/Rollback/Increase Automation/Expand Regression/Delay Release/Reduce Scope/Increase Testing/Architecture/Security/Executive Review as applicable).
Prioritize effort vs value; state confidence and residual risk. Synthesize provided Sprint 7–9 signals.

Evidence:
[paste]
```

---

## Related Documents

- [skill.md](skill.md)
- [enterprise-orchestrator/README.md](enterprise-orchestrator/README.md)
- [validation/README.md](validation/README.md)
- [enterprise-quality/README.md](enterprise-quality/README.md)
- [production-support/README.md](production-support/README.md)
- [production-support/operations-intelligence/README.md](production-support/operations-intelligence/README.md)
- [automation-intelligence/README.md](automation-intelligence/README.md)
- [automation-intelligence/review-engine/README.md](automation-intelligence/review-engine/README.md)
- [quality-intelligence/README.md](quality-intelligence/README.md)
- [quality-intelligence/rules/README.md](quality-intelligence/rules/README.md)
- [ado/README.md](ado/README.md)
- [templates/README.md](templates/README.md)
- [document-generation/README.md](document-generation/README.md)
- [guidelines/deliverable-selection.md](guidelines/deliverable-selection.md)
- [playbooks/README.md](playbooks/README.md)
- [brain/response-guidelines.md](brain/response-guidelines.md)

## Future Enhancements

- Optional prompts for ADO API publish (future enhancement)
- Optional script-template prompts in a later sprint if explicitly requested
- Metric calculator helpers when structured datasets are supplied

## Navigation

- **Previous:** [references.md](knowledge/references.md)
- **Next:** [enterprise-quality/README.md](enterprise-quality/README.md)
- **See Also:** [enterprise-quality/enterprise-quality-advisory-engine.md](enterprise-quality/enterprise-quality-advisory-engine.md) · [production-support/README.md](production-support/README.md)
