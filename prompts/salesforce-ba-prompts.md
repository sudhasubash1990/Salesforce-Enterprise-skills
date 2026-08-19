---
title: Salesforce BA Prompt Catalog
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
  - salesforce-business-analyst/skill.md
  - salesforce-business-analyst/prompts.md
keywords: [prompts, business-analyst, salesforce]
tags: [prompts, BA, SEACF]
---

# Salesforce BA Prompts

Load Tier-0 [`framework-core/`](../framework-core/README.md) and [`salesforce-business-analyst/skill.md`](../salesforce-business-analyst/skill.md) before producing deliverables. Prefer platform-native Salesforce solutions. Never invent regulatory requirements.

---

## Requirement elicitation

### BA-01 — Discovery workshop pack (Service Cloud)

**Use when:** Kickoff discovery for a Service Cloud program and you need stakeholders, questions, agenda, and an initial RAID in one pass.

**Prompt:**

```text
Act as a senior Salesforce Business Analyst using Salesforce Enterprise Skills.

Load:
- framework-core/README.md (Tier-0)
- salesforce-business-analyst/skill.md
- salesforce-business-analyst/playbooks/discovery-workshop-playbook.md
- salesforce-business-analyst/templates/stakeholder-matrix-template.md
- salesforce-business-analyst/templates/raid-log-template.md

Context:
- Industry: [utilities | banking | insurance | healthcare | retail | telecom]
- Clouds: Service Cloud (+ list any others)
- Problem statement: [1–3 sentences]

Produce:
1. Stakeholder map with RACI (business + Salesforce delivery roles)
2. Top 12 discovery questions for executive + operations interviews
3. 4-hour TO-BE envisioning workshop agenda
4. Initial RAID log (at least 3 items each: Risk, Assumption, Issue, Dependency)
5. Open questions for Legal/Compliance (mark TBC—do not invent regulations)

Save under outputs/[project-code]/01-discovery/. Flag assumptions explicitly.
```

### BA-02 — Requirement elicitation interview script

**Use when:** You must interview ops users before writing BRs and need Salesforce-aware questions (Case, entitlements, channels, SLAs).

**Prompt:**

```text
Using salesforce-business-analyst/skill.md and knowledge/service-cloud-patterns.md
(load knowledge/salesforce-clouds-overview.md first), create a structured interview script
for eliciting requirements for:

Process: [e.g. complaint management / case escalation / billing enquiry]
Personas to interview: [list]
Channels: [phone, email, chat, Experience Cloud, field]

For each interview section provide:
- Question
- Why it matters on Salesforce (object/feature hint: Case, Entitlement, Omni-Channel, Knowledge, etc.)
- What evidence/artifact to capture
- Follow-up if the answer is vague

Do not draft the BRD yet. End with a gap list of topics still needed for BR IDs.
```

---

## BRD

### BA-03 — Service Cloud complaint management BRD

**Use when:** You need a baseline BRD with requirement IDs for a complaint / case process.

**Prompt:**

```text
Using salesforce-business-analyst/templates/brd-template.md and brain/output-framework.md,
draft a BRD for a Service Cloud complaint management process.

Project: [name]
Industry: [industry]
In scope: [channels, Case lifecycle, Knowledge, entitlements — edit]
Out of scope: [explicit list]

Requirements:
- Include AS-IS and TO-BE process summaries
- Write business requirements BR-001 onward (minimum 10), each with priority, success measure, owner role
- Add assumptions, constraints, dependencies, and out-of-scope
- Prefer standard Case / Entitlement / Omni-Channel / Knowledge before custom objects
- Never invent HIPAA/PCI/AML rules—mark Legal TBC where relevant

Run mental validation from brain/validation-framework.md and brain/anti-hallucination.md
before delivery. Save to outputs/[project]/03-requirements/brd.md
```

### BA-04 — BRD from workshop notes

**Use when:** You have messy workshop notes and need a structured BRD section set.

**Prompt:**

```text
Convert the workshop notes below into BRD sections using
salesforce-business-analyst/templates/brd-template.md.

Workshop notes:
[paste]

Rules:
- Extract only what is evidenced in the notes; list gaps as open questions
- Assign BR-xxx IDs to clear business needs
- Separate business requirements from solution design speculation
- Flag contradictions between stakeholders
- Map each BR to impacted Salesforce clouds/objects at a high level (no Apex)

Save draft under outputs/[project]/03-requirements/brd-from-workshop.md
```

---

## FRD

### BA-05 — FRD for Case lifecycle and entitlements

**Use when:** BRs are agreed and you need system behaviour for Case, milestones, and agent UX—still BA-level, not technical design.

**Prompt:**

```text
Using salesforce-business-analyst/templates/frd-template.md and skill.md Pre-Execution Gate,
produce an FRD for:

Capability: Case lifecycle + entitlement milestones for [process]
Source BRs: [list BR IDs or paste]

Include:
- Functional requirements FR-xxx with traceability to BR-xxx
- Business rules (BR1…)
- Personas and CRUD expectations (high level)
- Data considerations (standard vs candidate custom fields—flag TBC)
- Integration touchpoints as requirements (not middleware design)
- Negative / exception paths agents must handle
- Out of scope and open questions for Solution Architect

Do not prescribe Apex class names or LWC components unless the user already constrained them.
Save to outputs/[project]/03-requirements/frd.md
```

---

## User stories

### BA-06 — INVEST user stories from BRD

**Use when:** Turning approved BRs into a sprint-ready backlog slice.

**Prompt:**

```text
Convert the business requirements below into epics and INVEST user stories using
salesforce-business-analyst/templates/user-story-template.md and
knowledge/user-stories.md + knowledge/acceptance-criteria.md.

Business requirements:
[paste BR-xxx]

Rules:
- Title format: <Business Capability> - <Action>
- Nested Given/When/Then acceptance criteria (happy path, validation, permission)
- Business rules, field table if needed, object impact, security matrix
- Estimation: T-shirt size + estimation-input table only—do NOT assign final story points
- Deliverables Expected (Implementation Team) vs BA artifact distinction
- requirement_refs back to BR IDs
- Prefer Case / Contact / Account / Entitlement / Knowledge standard objects

Split anything that is an epic disguised as a story. Save under
outputs/[project]/03-requirements/user-stories/
```

### BA-07 — Sales Cloud onboarding story pack

**Use when:** You need a focused onboarding backlog for Sales Cloud (leads → accounts/contacts → opportunity).

**Prompt:**

```text
Generate a user story pack for customer onboarding on Sales Cloud for [industry].

Load salesforce-business-analyst/skill.md, knowledge/salesforce-clouds-overview.md,
and templates/user-story-template.md.

Cover at least:
1. Capture lead / inbound interest
2. Convert lead with duplicate checks
3. Enrich Account/Contact
4. Create Opportunity with stage entry criteria
5. Handoff notes to service (if Service Cloud in scope—else mark out of scope)

Each story: full 18-section pack per .cursor/rules/userstory-generation.mdc,
nested AC, permission scenarios, ASSUMPTIONS and OUT OF SCOPE.
Save under outputs/[project]/03-requirements/user-stories/
```

---

## Acceptance criteria

### BA-08 — Harden acceptance criteria for testability

**Use when:** Stories exist but AC are vague, UI-prescriptive, or missing negative/permission paths.

**Prompt:**

```text
Review and rewrite acceptance criteria for the Salesforce user stories below using
knowledge/acceptance-criteria.md and brain/anti-hallucination.md.

Stories:
[paste]

For each story:
1. Flag untestable language ("user-friendly", "fast", "as today")
2. Rewrite AC as nested bullets: Given / When / Then / And
3. Ensure happy path, validation/error, and permission scenarios
4. Remove Apex/LWC implementation prescription unless technically constrained
5. Note any missing data or integration AC as open questions for BA refinement

Return a before/after summary table plus the rewritten AC blocks ready for ADO.
```

---

## Fit-gap

### BA-09 — Fit-gap Standard / Config / Extend / Gap / Defer

**Use when:** Stakeholders ask "can Salesforce do this?" and you need a governed recommendation.

**Prompt:**

```text
Perform fit-gap analysis using salesforce-business-analyst/brain/decision-framework.md
and playbooks/fit-gap-analysis.md (governance: playbooks/gap-analysis-playbook.md).

Requirements:
[paste]

Target clouds: [Sales Cloud | Service Cloud | Experience Cloud | …]

For each requirement produce a table with:
| Req ID | Need | Classification (Standard/Config/Extend/Gap/Defer) | Salesforce capability | Recommendation | Effort (S/M/L) | Licensing / dependency notes | Open questions |

Rules:
- Prefer Standard then Config before Extend
- Do not invent AppExchange product claims—mark research TBC
- Flag Solution Architect decisions explicitly
- Summarize risks of custom build vs process change

Save to outputs/[project]/04-solution/fit-gap.md
```

### BA-10 — Fit-gap challenge session (custom-heavy design)

**Use when:** A proposed design is Apex/LWC-heavy and you need a platform-native challenge.

**Prompt:**

```text
A solution design proposes significant custom Apex/LWC for the needs below.
Challenge it as a senior Salesforce BA using decision-framework.md,
shared/salesforce-capability-map.md, and knowledge/salesforce-clouds-overview.md.

Proposed design:
[paste]

Needs:
[paste]

Output:
1. Reclassification table (Standard/Config/Extend/Gap/Defer)
2. Which customs are justified vs premature
3. Recommended TO-BE using more configuration (Flows, validation rules, dynamic forms, Omni-Channel, etc.)
4. Residual gaps and integration needs
5. Questions for Architecture Review Board
```

---

## Process analysis

### BA-11 — AS-IS / TO-BE process map (Case handling)

**Use when:** You need process maps and pain points tied to future BRs.

**Prompt:**

```text
Document AS-IS and TO-BE for process: [name] using
salesforce-business-analyst/knowledge/process-mapping.md.

Systems today: [list]
Target: Salesforce [clouds] + [integrations]

Produce:
1. AS-IS narrative + mermaid flowchart
2. Pain points table (impact, frequency, evidence source)
3. TO-BE narrative + mermaid flowchart on Salesforce
4. Requirement refs (BR-xxx placeholders) for each TO-BE change
5. Handoffs, SLAs, and exception paths
6. Assumptions and out of scope

Do not invent SLAs—use placeholders or mark TBC. Save under
outputs/[project]/02-process/process-[name].md
```

### BA-12 — Omni-Channel / queue redesign analysis

**Use when:** Contact centre routing is broken and you need BA-level TO-BE before build.

**Prompt:**

```text
Analyse contact-centre routing for Service Cloud Omni-Channel.

Current state notes:
[paste]

Using knowledge/service-cloud-patterns.md and skill.md:
- Map AS-IS queues, skills, overflow, and after-hours handling
- Propose TO-BE routing principles (not exact org config XML)
- Define business rules for priority, presence, and transfer
- List FR candidates and data needed (skills taxonomy, business hours)
- Call out Experience Cloud / digital channel impacts if mentioned
- RAID entries for workforce and telephony dependencies

Flag items needing Workforce Engagement / CTI vendor confirmation as TBC.
```

---

## Stakeholder analysis

### BA-13 — Stakeholder matrix and RACI for Salesforce program

**Use when:** Program kickoff needs clarity on who decides vs who is consulted.

**Prompt:**

```text
Build a stakeholder analysis using
salesforce-business-analyst/templates/stakeholder-matrix-template.md and
knowledge/stakeholder-analysis.md.

Program: [name]
Clouds: [list]
Delivery model: [waterfall phases | agile sprints]

Produce:
1. Stakeholder matrix (role, interest, influence, engagement approach)
2. RACI for: discovery, BRD sign-off, fit-gap, backlog priority, UAT, go-live
3. Salesforce-specific roles (Product Owner, BA, SA, QE, Admin, Integration, Security, Change)
4. Risks from missing stakeholders (e.g. no Security for sharing model)
5. Recommended communication cadence

Save to outputs/[project]/01-discovery/stakeholder-matrix.md
```

---

## KPI

### BA-14 — KPI baseline for Service Cloud transformation

**Use when:** Executives ask for success metrics before build starts.

**Prompt:**

```text
Define KPI baselines using salesforce-business-analyst/templates/kpi-baseline-template.md.

Program outcomes desired:
[paste or list: e.g. reduce complaint handle time, improve FCR, cut reopen rate]

Rules:
- Separate leading vs lagging indicators
- For each KPI: definition, data source (Salesforce report/object or external), baseline (TBC if unknown), target, measurement cadence, owner
- Do NOT invent baseline numbers—use TBC and state what to measure in weeks 1–2 of discovery
- Tie KPIs to candidate BR/FR IDs
- Note Experience Cloud / telephony data dependencies

Save to outputs/[project]/08-executive/kpi-baseline.md
```

### BA-15 — Benefit realization check mid-program

**Use when:** Mid-release review against the original KPI baseline.

**Prompt:**

```text
Compare the KPI baseline below to current Salesforce reporting evidence.

KPI baseline:
[paste]

Available report/export notes:
[paste—or say "none yet"]

Using templates/kpi-baseline-template.md guidance:
- Assess which KPIs are measurable in Salesforce today vs still blocked
- Identify requirement or adoption gaps (not just "users need training")
- Recommend BA actions: story changes, reporting stories, OCM interventions
- Do not fabricate % improvements
```

---

## OCM

### BA-16 — OCM and upskilling plan for Salesforce go-live

**Use when:** Technical delivery is ahead of adoption planning.

**Prompt:**

```text
Create a change management / upskilling plan using
salesforce-business-analyst/playbooks/change-management-playbook.md and
templates/comms-upskilling-plan-template.md.

Release: [name]
Personas impacted: [agents, supervisors, back-office, partners]
Clouds: [list]
Go-live window: [date or TBC]

Produce:
1. Change impact by persona (process, system, skill)
2. Resistance risks and mitigations
3. Comms plan (audience, message, channel, timing)
4. Role-based upskilling curriculum (Salesforce navigation vs process training)
5. Hypercare support model (BA/QE/ops)—no invented SLAs
6. Success measures linked to KPI baseline if provided

Save to outputs/[project]/08-executive/comms-upskilling-plan.md
```

---

## Additional high-value BA prompts

### BA-17 — RAID log refresh before steering committee

**Use when:** Preparing a steering pack and RAID is stale.

**Prompt:**

```text
Refresh the RAID log using salesforce-business-analyst/templates/raid-log-template.md
and knowledge/risk-management.md.

Current RAID:
[paste]

Recent changes:
[paste: scope, integration delays, UAT feedback]

Update statuses, add missing Salesforce-specific risks (sharing model, governor limits,
data migration, sandbox refresh, AppExchange license), and produce a steering-committee
summary of top 5 risks with owners and next actions. No fabricated dates.
```

### BA-18 — Requirements traceability matrix (RTM)

**Use when:** QE or audit asks for BR → FR → story → test coverage mapping.

**Prompt:**

```text
Build an RTM using salesforce-business-analyst/templates/traceability-matrix-template.md.

Inputs:
Business requirements: [paste or path]
Functional requirements: [paste or path]
User stories: [paste or path]
Test scenarios (if any): [paste or "none"]

Produce a matrix with IDs, coverage status (Covered / Partial / Gap), and gaps to close
before UAT. Highlight orphan stories and untested Must BRs. Save under
outputs/[project]/03-requirements/rtm.md
```

### BA-19 — UAT scenario pack from stories

**Use when:** UAT planning needs BA-owned scenarios before QE expands test cases.

**Prompt:**

```text
Create UAT scenarios using salesforce-business-analyst/playbooks/uat-playbook.md
and playbooks/uat-planning-playbook.md from these user stories:

[paste]

For each story produce TS-xxx scenarios covering all AC, including permission-denied paths.
Format: preconditions, steps, expected results, tester role, pass/fail, requirement_refs.
Prioritize Must-scope. Note sandbox data dependencies. Do not invent production data volumes.
Save under outputs/[project]/05-uat/uat-scenarios.md
```

### BA-20 — ADO-ready story publish pack

**Use when:** Stories are approved locally and you need ADO field-ready content.

**Prompt:**

```text
Prepare these user stories for Azure DevOps using
salesforce-business-analyst/knowledge/ado-backlog-integration.md and the ADO Publish Checklist
in salesforce-business-analyst/checklists.md.

Stories:
[paste markdown]

For each story output:
1. System.Title
2. HTML-ready System.Description (full pack)
3. Nested HTML Acceptance Criteria
4. Suggested Tags (semicolon-separated)
5. Priority suggestion
6. Story Points: leave empty unless I explicitly ask for indicative

Remind: save local .md under outputs/ before any ADO API publish.
Do not fabricate work item IDs.
```

### BA-21 — Experience Cloud partner portal requirements

**Use when:** External users need Case or order visibility via Experience Cloud.

**Prompt:**

```text
Elicit and structure BA requirements for an Experience Cloud partner portal that allows
partners to [create/view Cases | view orders | update assets—edit].

Load knowledge/salesforce-clouds-overview.md and skill.md.
Cover sharing/security questions for BA (without recommending "view all"),
branding vs process scope, authentication assumptions (TBC with IAM),
and FR/BR candidates. Produce open questions for Security and Architecture.
Prefer standard Experience Cloud + sharing sets / portal users patterns in recommendations.
Save draft BR list under outputs/[project]/03-requirements/experience-cloud-brs.md
```

### BA-22 — Data migration BA requirements (cutover)

**Use when:** Migration is in scope and BA must define what "done" means—not ETL code.

**Prompt:**

```text
Define business requirements for data migration into Salesforce for [objects].

Source systems: [list]
Cutover window: [TBC or describe]
Objects: [Account, Contact, Case, …]

Using knowledge/data-migration.md and skill.md:
- BR/FR for historical data, open Cases, attachments, owner mapping, and reconciliation
- Acceptance criteria for business sign-off (record counts, sample audits)—no invented volumes
- In-scope vs archive-only vs out-of-scope
- Dependencies on Security (PII), QE data migration pack, and integration freeze
- RAID entries

Hand off technical mapping as open questions for Data Architect. Save under
outputs/[project]/03-requirements/data-migration-requirements.md
```

### BA-23 — Security & sharing requirements workshop prep

**Use when:** Before profiles/permission sets are designed, BA must capture who can see what.

**Prompt:**

```text
Prepare a security requirements pack for Salesforce using knowledge/security-model.md
and skill.md.

Personas: [list]
Sensitive data: [PII / financial / health—mark TBC with Legal]
Objects: [list]

Produce:
1. Workshop agenda focused on OWD, role hierarchy needs, sharing exceptions
2. Persona × object CRUD matrix (business intent)
3. Questions that prevent "give everyone Modify All"
4. Candidate BRs/FRs for field-level security and Experience Cloud visibility
5. Items that must escalate to Security Architect

Do not recommend bypassing sharing. Save under
outputs/[project]/01-discovery/security-requirements-prep.md
```

### BA-24 — Integration requirements (BA view)

**Use when:** Middleware exists and BA must specify business contracts, not APIs.

**Prompt:**

```text
Document integration requirements from a BA perspective using
knowledge/integration-patterns.md and skill.md.

Interfaces:
[paste: system A ↔ Salesforce, trigger events, direction]

For each interface specify:
- Business trigger and frequency (real-time / near-real-time / batch)—mark TBC if unknown
- Source of truth per data element
- Failure / retry business expectations (not MuleSoft flows)
- Idempotency / duplicate business rules
- Monitoring / ops ownership questions
- FR IDs and dependencies

No invented API field maps. Flag SA/Integration engineer follow-ups.
```

### BA-25 — Scope change impact assessment

**Use when:** A late CR threatens the release train.

**Prompt:**

```text
Assess this Salesforce scope change as a senior BA.

Change request:
[paste]

Baseline: [link or paste BR/story list]

Assess impact on:
- BR/FR/stories to add/modify/defer
- Fit-gap classification changes
- Integration, security, data migration, reporting
- UAT and OCM
- RAID updates

Recommend accept / defer / reject with rationale and MoSCoW suggestion.
Do not invent timeline dates—state dependency assumptions instead.
```

### BA-26 — Digital transformation / process standardization framing

**Use when:** Leadership wants "Salesforce transformation" without clear process standardization.

**Prompt:**

```text
Using salesforce-business-analyst/playbooks/digital-transformation-strategy-playbook.md
and templates/kpi-baseline-template.md, frame a Salesforce digital reinvention slice for:

Domain: [service operations | sales | field | …]
Industry: [industry]

Produce:
1. AS-IS fragmentation themes (systems + process variants)
2. TO-BE standardization principles on Salesforce
3. Candidate capability roadmap (now / next / later)—no fake dates
4. KPI baseline skeleton
5. OCM implications
6. What must stay local vs enterprise-standard

Flag Architecture and licensing decisions as open questions.
```

### BA-27 — Anti-pattern review of a BA draft

**Use when:** You want a quality gate before stakeholder send-out.

**Prompt:**

```text
Review this BA draft against salesforce-business-analyst/brain/validation-framework.md,
brain/anti-hallucination.md, and checklists.md.

Draft:
[paste BRD, FRD, or stories]

Report:
1. Failures (missing IDs, untestable AC, epic-as-story, invented regulations, exact story points, security bypasses)
2. Severity
3. Corrected excerpts
4. Brain-loading / Pre-Execution Gate gaps if evident

Do not inflate quality scores. Be specific and actionable.
```

### BA-28 — End-to-end BA slice (complaint → stories → fit-gap)

**Use when:** Demo why SEACF matters—one request through the full BA path.

**Prompt:**

```text
Run a full Salesforce BA slice for utilities complaint management on Service Cloud
using Salesforce Enterprise Skills end-to-end.

Steps (do not skip):
1. python scripts/retrieve_context.py --query "Service Cloud complaint BRD and user stories"
   (or simulate the bundle) and load returned files + Tier-0
2. Draft BRD section summary (BR-001–BR-008) via templates/brd-template.md
3. Produce 5 INVEST stories via templates/user-story-template.md with nested AC
4. Fit-gap table via decision-framework.md + playbooks/fit-gap-analysis.md
5. Pre-delivery validation via validation-framework.md + anti-hallucination.md
6. Save artifacts under outputs/demo-complaint/ and list convert.py command for office output

Prefer Case standard model. No invented regulatory rules. No final story points.
```

---

## Related documents

- [Prompt library index](README.md)
- [BA skill](../salesforce-business-analyst/skill.md)
- [BA module prompts](../salesforce-business-analyst/prompts.md)
- [Getting started](../GETTING_STARTED.md)
