---
title: Salesforce QE Prompt Catalog
module: Salesforce Enterprise Skills
category: Root
document_type: Guide
version: 1.0.0
review_status: Draft
owner: SEACF Practice Lead
created_date: 2026-08-10
last_updated: 2026-08-10
review_cycle: quarterly
related_documents:
  - prompts/README.md
  - salesforce-quality-engineering/skill.md
  - salesforce-quality-engineering/prompts.md
keywords: [prompts, quality-engineering, salesforce, qa]
tags: [prompts, QE, SEACF]
---

# Salesforce QE Prompts

Route via [`salesforce-quality-engineering/skill.md`](../salesforce-quality-engineering/skill.md) and [`enterprise-orchestrator/enterprise-orchestrator.md`](../salesforce-quality-engineering/enterprise-orchestrator/enterprise-orchestrator.md). Load Tier-0 [`framework-core/`](../framework-core/README.md) first.

**Hard rule:** Do not invent coverage %, flake %, SLA/MTTR, ROI, maturity scores, or compliance certifications without evidence.

---

## Test strategy

### QE-01 — Service Cloud release test strategy

**Use when:** A release needs an entry/exit strategy before scenario writing.

**Prompt:**

```text
Act as a senior Salesforce Quality Engineer using Salesforce Enterprise Skills.

Load:
- framework-core/README.md (Tier-0)
- salesforce-quality-engineering/skill.md
- enterprise-orchestrator/enterprise-orchestrator.md
- enterprise-orchestrator/capability-routing-table.md

Draft a test strategy for:
Release: [name]
Clouds: Service Cloud [+ others]
Requirements / stories: [paste or summarize]

Cover:
- Scope / out of scope
- Test levels (unit config validation, SIT, UAT, regression, production smoke)
- Environments and data dependencies (mark TBC—no invented org names as fact)
- Entry/exit criteria
- Risk-based priorities
- Traceability approach to BR/FR/story IDs
- Automation intent (candidates only—no fake coverage %)
- Roles (QE, BA, Admin, Integration)

Save under outputs/[project]/05-quality/test-strategy.md
```

### QE-02 — Risk-based test strategy for multi-cloud release

**Use when:** Sales + Service + integration land in one train and risk focus is unclear.

**Prompt:**

```text
Using salesforce-quality-engineering/skill.md and
skills/risk-based-regression/README.md (plus enterprise-orchestrator routing),
produce a risk-based test strategy for:

Clouds: [Sales Cloud, Service Cloud, Experience Cloud—edit]
Key changes: [paste release notes / stories]
Integrations: [list]

Output:
1. Risk heatmap themes (functional, data, security, integration, UX)
2. What must be tested vs deferred with rationale
3. Regression slice recommendation (not a full inventory dump)
4. Evidence needed before go/no-go
5. Open questions—do not invent historical defect rates
```

---

## Test scenarios

### QE-03 — End-to-end scenarios from user stories

**Use when:** Stories are ready and QE must expand BA AC into E2E scenarios.

**Prompt:**

```text
Route via the QE Enterprise Orchestrator. From the Salesforce user stories below,
derive end-to-end test scenarios (not step-level cases yet).

Stories:
[paste]

For each scenario include:
- ID (TS-xxx), objective, personas, clouds/objects touched
- Preconditions / data setup needs
- Business path (happy + key alternate)
- Requirement / story refs
- Risk tag (Critical/High/Medium)
- Candidate automation suitability (Yes/No/Partial) with reason—no coverage %

Call out gaps where AC are untestable and return clarification questions to BA.
Save under outputs/[project]/05-quality/test-scenarios.md
```

### QE-04 — Omni-Channel routing scenario pack

**Use when:** Omni-Channel / queue changes need scenario coverage before config test.

**Prompt:**

```text
Design Salesforce Omni-Channel test scenarios for:

Routing model notes:
[paste]

Using skill.md + knowledge relevant to Service Cloud routing (via orchestrator):
- Skills-based routing, overflow, after-hours, transfer, supervisor intervene
- Negative paths (no agents available, wrong skill, presence offline)
- Permission differences (agent vs supervisor)
- Integration with telephony/CTI if mentioned—mark vendor TBC

Do not invent SLA timers. List evidence to capture in sandbox (screenshots, queue metrics).
```

---

## Test cases

### QE-05 — Detailed test cases from scenarios

**Use when:** Scenarios are approved and execution scripts are needed.

**Prompt:**

```text
Expand these Salesforce test scenarios into detailed test cases suitable for ADO / Excel.

Scenarios:
[paste]

Each case:
- TC-xxx, linked TS-xxx / story IDs
- Steps with action + expected result (observable in Salesforce UI or API response)
- Test data requirements
- Persona / permission set assumption
- Negative and regression tags where relevant

Do not include Apex unit tests. Do not invent org URLs or credentials.
Save under outputs/[project]/05-quality/test-cases.md
```

### QE-06 — Permission-negative test case matrix

**Use when:** Sharing / permission sets are a release risk.

**Prompt:**

```text
Using salesforce-quality-engineering/skills/permission-testing-agent/README.md
and enterprise-orchestrator routing, build a permission-negative test matrix for:

Personas: [list]
Objects / actions: [Case create, Case edit closed, Knowledge publish, …]
Stories / FRs: [paste]

Produce:
| Persona | Action | Expected (Allow/Deny) | AC/Story ref | Test case ID | Notes |
Include FLS and sharing edge cases as questions if OWD unknown.
Never recommend Modify All / View All as a test workaround.
```

---

## Integration testing

### QE-07 — Salesforce integration test approach

**Use when:** Middleware syncs (billing, CIS, ERP) must be validated with Salesforce as system of engagement.

**Prompt:**

```text
Design an integration test approach for Salesforce ↔ [external system] using
salesforce-quality-engineering/skill.md and automation-intelligence / platform knowledge
via the Enterprise Orchestrator.

Interface summary:
[paste direction, objects, trigger events]

Produce:
1. In-scope interface scenarios (create/update/failure/retry/duplicate)
2. Source-of-truth checks per key field (business-level)
3. Environment prerequisites and stubs/mocks policy
4. Data setup / teardown rules
5. Evidence pack for SIT sign-off
6. Risks (governor limits, order of execution, partial failures)

No invented field maps or latency SLAs—mark TBC.
Save under outputs/[project]/05-quality/integration-test-approach.md
```

### QE-08 — Platform event / async integration scenarios

**Use when:** Async patterns (Platform Events, Change Data Capture, batch) are in scope.

**Prompt:**

```text
Create Salesforce async integration test scenarios for:

Pattern: [Platform Events | CDC | Batch / ETL | Outbound messages—edit]
Payload / objects: [describe]
Failure modes observed or feared: [paste]

Include ordering, duplicate delivery, replay, and monitoring/observable outcomes.
Separate what QE can prove in sandbox vs needs Integration engineer tooling.
Do not invent event schema—list required schema questions.
```

---

## Regression

### QE-09 — Risk-based regression pack for a sprint

**Use when:** Sprint changes touch shared objects and full regression won’t fit.

**Prompt:**

```text
Using skills/risk-based-regression/README.md and quality-intelligence guidance via orchestrator,
build a risk-based regression pack for sprint changes:

Changed metadata / stories:
[paste]
Known prior defects (if any): [paste or "none"]

Output:
1. Must-run regression scenarios (prioritized)
2. Explicit deferrals with risk acceptance questions for PO
3. Smoke vs deep regression split
4. Data refresh dependencies
5. Automation candidates vs manual-only

Do not claim historical failure rates without evidence. Save under
outputs/[project]/05-quality/regression-pack-sprint.md
```

### QE-10 — Metadata impact → regression scope

**Use when:** You have a `package.xml` or change list and need blast-radius testing.

**Prompt:**

```text
Analyse metadata impact using
salesforce-quality-engineering/skills/metadata-impact-analyzer/README.md.

Input changes:
[paste package.xml, change set list, or story technical notes]

Produce:
- Impacted objects, automation, layouts, permissions themes
- Recommended regression scenarios tied to risk
- Go-live checklist items relevant to the blast radius
- Questions for Admin/Dev where impact is unclear

Do not invent org-specific automation names not present in the input.
```

---

## Data migration

### QE-11 — Data migration QA plan

**Use when:** Cutover includes historical Accounts/Contacts/Cases and QE owns validation.

**Prompt:**

```text
Using salesforce-quality-engineering/skills/data-migration-qa/README.md
(and playbooks under that skill as needed), create a data migration QA plan for:

Source: [system]
Targets: [Account, Contact, Case, …]
Cutover style: [big bang | phased]
Volumes: [TBC or provided—do not invent]

Include:
- Preload / mock load / dress rehearsal / production load validation stages
- Record count + business sample audit approach
- Owner mapping, record types, picklist value, date/timezone checks
- Attachment / content notes if in scope
- Rollback validation checkpoints
- Entry/exit for business sign-off

No fake reconciliation percentages. Save under
outputs/[project]/05-quality/data-migration-qa-plan.md
```

### QE-12 — Migration dress-rehearsal defect triage

**Use when:** Dress rehearsal produced mismatches and you need structured triage.

**Prompt:**

```text
Triage these Salesforce data migration dress-rehearsal findings using the
data-migration-qa skill and quality-intelligence defect practices.

Findings:
[paste counts, sample mismatches, error logs summary]

Classify each: data quality (source) vs mapping vs transform vs Salesforce validation
vs environment. Recommend containment for cutover weekend, evidence still needed,
and which defects block go-live vs can accept with workaround.
Do not invent root cause certainty—state confidence.
```

---

## API testing

### QE-13 — Salesforce API test scenarios (REST)

**Use when:** Integrations or Experience Cloud backends call Salesforce APIs.

**Prompt:**

```text
Design Salesforce API test scenarios (business-level) for:

APIs / resources: [Accounts, Cases, custom—edit]
Auth model: [Connected App / OAuth—TBC]
Consumers: [middleware, mobile, portal]

Using automation-intelligence/api-testing knowledge via orchestrator:
- CRUD happy paths tied to sharing/FLS expectations
- Negative: auth failure, validation rules, duplicate rules, governor-limit-aware bulk notes
- Idempotency and partial success for composites if relevant
- Traceability to FR/story IDs

Do not invent named credentials or endpoint URLs. Provide a data setup checklist.
Save under outputs/[project]/05-quality/api-test-scenarios.md
```

### QE-14 — API contract gaps for QE sign-off

**Use when:** Swagger/OpenAPI or mapping docs are incomplete before SIT.

**Prompt:**

```text
Review this Salesforce-related API contract / mapping for testability gaps.

Contract / mapping:
[paste]

List Critical/High questions blocking API test design. Identify missing error catalogs,
pagination, filtering, ownership fields, and Person Account / Record Type nuances.
Propose a minimal evidence set for SIT entry. Do not fabricate schema fields.
```

---

## Automation

### QE-15 — Automation candidate assessment (Salesforce UI)

**Use when:** Leadership asks “what should we automate?” for a Salesforce program.

**Prompt:**

```text
Using salesforce-quality-engineering/automation-intelligence/README.md and
enterprise-orchestrator routing, assess automation candidates for:

Scope stories/scenarios:
[paste]
Tooling preference: [Playwright | Selenium | none stated]

Produce:
| Scenario | Manual/Automate/Hybrid | Rationale | Stability risks (locators, dynamic UI, async) | Priority |
Call out Salesforce-specific risks (Lightning refreshes, flexible layouts, Omni-Channel).
Do not invent flake percentages or ROI. Recommend governance next steps only.
```

### QE-16 — Playwright locator / POM review for Salesforce

**Use when:** UI automation exists and needs a quality review before CI reliance.

**Prompt:**

```text
Review the Playwright page objects / locators below using
salesforce-quality-engineering/skills/playwright-review/README.md.

Code / locators:
[paste]

Assess resilience for Lightning Experience, recommend locator strategy improvements,
and list flaky patterns. Do not rewrite an entire framework unless asked.
No invented CI pass-rate metrics.
```

### QE-17 — Test data strategy for automated Salesforce suites

**Use when:** Automation is blocked by brittle or shared sandbox data.

**Prompt:**

```text
Using skills/test-data-generator/README.md and automation-intelligence guidance,
design a test data strategy for Salesforce automation covering:

Objects: [list]
Personas: [list]
Constraints: [scratch org | partial sandbox | full—edit]

Include create/cleanup patterns, uniqueness rules, Reference data vs transactional data,
and PII handling (no real customer data). Mark volume targets TBC unless provided.
```

---

## Defect triage

### QE-18 — Salesforce defect triage board

**Use when:** Daily triage needs severity, component, and next owner clarity.

**Prompt:**

```text
Triage the Salesforce defects below using quality-intelligence defect practices
via the Enterprise Orchestrator.

Defects:
[paste]

For each: severity suggestion, likely layer (config, automation/order of execution,
integration, data, permission, environment), reproduce notes gaps, and owner squad
(BA vs Admin vs Dev vs Integration vs Env). Identify duplicates/clusters.
Do not invent production incident chronologies.
```

### QE-19 — Flaky vs product defect decision

**Use when:** A failing automated test may be product or harness.

**Prompt:**

```text
Decide whether this failure is a Salesforce product defect, test harness issue,
or environment issue.

Evidence:
[paste logs, screenshots description, steps, recent metadata deploys]

Using automation-intelligence review thinking:
- Decision + confidence
- Additional evidence to collect
- Short-term quarantine recommendation (yes/no) without inventing flake %
- If product defect: suggested bug title + acceptance repro for Dev
```

---

## Production quality assessment

### QE-20 — Pre-go-live quality / release readiness assessment

**Use when:** Steering committee needs a go/no-go quality view.

**Prompt:**

```text
Perform a production readiness / quality assessment using
salesforce-quality-engineering/templates/release-readiness-checklist.md,
enterprise-quality advisory patterns via orchestrator, and skill.md.

Inputs:
Test execution summary: [paste]
Open defects: [paste]
Migration status: [paste]
Unresolved risks: [paste]

Output:
- Readiness stance (Proceed / Proceed with conditions / No-go) with rationale
- Residual risks and required conditions
- Evidence gaps (do not invent coverage or MTTR)
- Hypercare focus areas for first 72 hours
- Executive summary (short)

Save under outputs/[project]/08-executive/release-readiness.md
```

### QE-21 — Sev1 production incident triage (Salesforce)

**Use when:** Production is impaired and QE/ops need structured containment guidance.

**Prompt:**

```text
Triage a Sev1 Salesforce production incident using
salesforce-quality-engineering/production-support/README.md and
skills/production-rca/README.md via Enterprise Orchestrator.

Incident:
[symptoms, start time, impacted process, clouds—paste]
What we know / don’t know:
[paste]

Provide:
1. Impact assessment (users, processes, data integrity)—no fake user counts
2. Likely failure domains (config deploy, integration, data, auth, platform event)
3. Immediate containment steps (safe—no “disable sharing” / security bypass)
4. Evidence to collect (debug logs themes, deployment history, middleware, jobs)
5. Communication bullets for incident commander
6. Hypercare checklist after mitigation

Do not invent org URLs, credentials, or confirmed root cause.
```

### QE-22 — Hypercare quality pulse (week 1)

**Use when:** Post-go-live daily quality reporting is needed.

**Prompt:**

```text
Create a Day-N hypercare quality pulse template filled with the evidence below.

Evidence:
[paste tickets, defects, monitoring notes]

Using production-support guidance:
- Themes, Sev distribution (only if provided), reopen risks
- Salesforce components implicated
- Actions for BA (requirement miss) vs Dev/Admin vs Integration
- Exit criteria questions for ending hypercare
Do not invent SLA compliance %.
```

---

## Additional high-value QE prompts

### QE-23 — Requirement testability review (no test cases yet)

**Use when:** Shift-left—QE reviews BR/story quality before design freeze.

**Prompt:**

```text
Act as senior Salesforce QE. Review the requirement/story using the Requirement Analysis
guidance in salesforce-quality-engineering (prompts.md Sprint 2 behaviour).
Do NOT generate test cases or RTM yet.

Requirement / story:
[paste]

Produce mandatory analysis: quality assessment dimensions, gaps, Critical/High questions,
Salesforce component impact themes, risks, scope boundary notes, next steps.
```

### QE-24 — OmniStudio / FlexCard journey validation plan

**Use when:** Industry cloud / OmniStudio journeys (e.g. Move-In) are in the release.

**Prompt:**

```text
Using salesforce-quality-engineering/skills/omnistudio-qa/README.md, create a validation
plan for OmniScript / DataRaptor / Integration Procedure journey:

Journey: [name]
Notes: [paste]

Cover UI path, data transform correctness, failure handling, and regression on related
standard objects. List environment prerequisites and TBC items. No invented industry
regulatory rules.
```

### QE-25 — Agentforce / AI agent testing prompts pack

**Use when:** Agentforce actions or guardrails need a test approach.

**Prompt:**

```text
Using salesforce-quality-engineering/skills/agentforce-testing/README.md,
draft a test approach for Agentforce configuration:

Agent purpose: [describe]
Tools/actions: [list]
Guardrails notes: [paste]

Include functional dialogues, refusal/guardrail cases, grounding/data access risks,
and human handoff. Do not invent model benchmark scores. Flag Legal/Compliance TBC
for AI disclosure.
```

### QE-26 — Field Service scheduling quality scenarios

**Use when:** FSL scheduling / work orders are in scope.

**Prompt:**

```text
Using skills/field-service-testing/README.md, design quality scenarios for Field Service:

Scope: [work orders, service appointments, optimization—edit]
Constraints: [skills, territories, SLAs—mark TBC]

Include emergency vs planned, dispatcher vs mobile worker, and optimization edge cases.
No invented travel-time accuracy metrics.
```

### QE-27 — SOQL / report validation for UAT evidence

**Use when:** UAT evidence depends on reports or queries being trustworthy.

**Prompt:**

```text
Using skills/soql-validation-assistant/README.md, review these SOQL/report definitions
for correctness and UAT evidence fitness:

[paste SOQL or report description]

Flag sharing, selective filters, row limits, and date-literal pitfalls.
Suggest safer validation queries. Do not run against production or ask for credentials.
```

### QE-28 — End-to-end QE slice (strategy → scenarios → readiness)

**Use when:** Demo why cloning SEACF QE matters—one governed path.

**Prompt:**

```text
Run a full Salesforce QE slice for a Service Cloud case-management release
using Salesforce Enterprise Skills.

Steps:
1. Load Tier-0 framework-core + salesforce-quality-engineering/skill.md
2. Route via enterprise-orchestrator/enterprise-orchestrator.md
3. Produce a concise test strategy (entry/exit, risks, environments)
4. Derive 8 end-to-end scenarios from the stories below
5. Propose a risk-based regression slice
6. Draft release-readiness conditions (no invented coverage %)
7. Save under outputs/demo-case-qe/ and state any output-engine convert command

Stories / requirements:
[paste]

Never invent SLA/MTTR/coverage metrics. Prefer questions over fabricated facts.
```

---

## Related documents

- [Prompt library index](README.md)
- [QE skill](../salesforce-quality-engineering/skill.md)
- [QE module prompts](../salesforce-quality-engineering/prompts.md)
- [QE prompts index](../salesforce-quality-engineering/prompts/README.md)
- [Getting started](../GETTING_STARTED.md)
