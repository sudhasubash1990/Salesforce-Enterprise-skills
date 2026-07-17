#!/usr/bin/env python3
"""Generate Sprint 5 — Enterprise Documentation & Deliverable Generator assets."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.7.0"
DATE = "2026-07-17"
SPRINT = "Sprint 5"

CROSS = [
    "[QE Brain (Sprint 1)](../brain/README.md)",
    "[Requirement Analysis (Sprint 2)](../knowledge/requirement-analysis.md)",
    "[Test Design Engine (Sprint 3)](../knowledge/test-design-engine.md)",
    "[Platform Foundation 4A](../knowledge/platform/README.md)",
    "[Enterprise Knowledge 4B](../knowledge/clouds/README.md)",
]


def titleize(slug: str) -> str:
    special = {
        "rtm": "Requirement Traceability Matrix (RTM)",
        "sit-checklist": "SIT Checklist",
        "uat-checklist": "UAT Checklist",
        "go-no-go-checklist": "Go / No-Go Checklist",
        "defect-rca-report": "Defect RCA Report",
        "executive-qa-dashboard": "Executive QA Dashboard",
        "ci-cd": "CI/CD",
    }
    return special.get(slug, slug.replace("-", " ").title())


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {i}" for i in items)


# Document intelligence metadata per template
# phase, owner, reviewers, approvers, inputs, outputs, links, when

INTEL = {}  # filled per template in catalog


def template_doc(slug: str, meta: dict) -> str:
    title = meta.get("title") or titleize(slug)
    purpose = meta["purpose"]
    phase = meta.get("phase", "Delivery")
    owner = meta.get("owner", "Test Lead / QE Lead")
    reviewers = meta.get("reviewers", ["BA", "SA (as applicable)", "Delivery Lead"])
    approvers = meta.get("approvers", ["Delivery Lead / Release Manager"])
    audience = meta.get("audience", ["QE team", "Delivery leadership", "BA", "Development"])
    inputs = meta.get("inputs", ["Approved scope / stories", "Risks", "Environment plan"])
    outputs = meta.get("outputs", [f"Completed {title}"])
    when = meta.get("when", f"Create during {phase} when stakeholders need a governed QA artifact.")
    sections = meta.get("sections", ["Purpose", "Scope", "Details", "Risks", "Approvals"])
    mandatory = meta.get("mandatory", ["Document ID", "Version", "Status", "Owner", "Date"])
    optional = meta.get("optional", ["Screenshots", "Appendix"])
    example = meta.get("example", f"_Illustrative skeleton — replace with project content._\n\n**{title}** — Project PRJ-XXX | Sprint/Release N | Status: Draft")
    related_tpl = meta.get("related_tpl", [])
    checklist_items = meta.get("review_checklist", [
        "Purpose and audience clear",
        "Inputs/outputs listed",
        "Traceability IDs present where required",
        "No client PII / credentials",
        "Aligned to engines (analysis → design → document)",
    ])

    sections_md = "\n".join(f"{i}. **{s}**" for i, s in enumerate(sections, 1))
    related = CROSS + [f"[{titleize(r)}]({r}.md)" for r in related_tpl] + [
        "[Document Intelligence](../guidelines/document-intelligence.md)",
        "[Deliverable Selection](../guidelines/deliverable-selection.md)",
        "[README.md](README.md)",
    ]

    return f"""---
title: {title}
module: Salesforce Quality Engineering
category: Template
document_type: Template
version: {VERSION}
review_status: Draft
owner: QE Practice Lead
created_date: {DATE}
last_updated: {DATE}
review_cycle: quarterly
keywords: [{slug}, template, documentation-generator]
tags: [template, sprint-5]
---

# {title}

**Template ID:** TPL-{slug.upper().replace('-', '_')[:40]}  
**Lifecycle phase:** {phase}  
**Methodology fit:** Agile / Scrum / SAFe / Waterfall (tailor sections)

---

## Purpose

{purpose}

## Business Context

{when}

Consulting-grade artifact for Salesforce Quality Engineering programs. Reuse across industries; tailor depth to project size and risk.

## Audience

{bullets(audience)}

## Owner

**Primary owner:** {owner}

## Document Intelligence

| Attribute | Guidance |
|-----------|----------|
| **When to create** | {when} |
| **Owner** | {owner} |
| **Reviewers** | {', '.join(reviewers)} |
| **Approvers** | {', '.join(approvers)} |
| **Project phase** | {phase} |

## Inputs

{bullets(inputs)}

## Outputs

{bullets(outputs)}

## Prerequisites

- Sprint 2 Requirement Analysis completed (or explicitly waived with documented assumptions)
- Sprint 3 Test Design completed when scenarios/cases/RTM are in scope
- Salesforce impact grounded in Sprint 4A/4B knowledge as applicable
- No unnecessary document — confirm selection via [Deliverable Selection](../guidelines/deliverable-selection.md)

## Instructions

1. Confirm this is the right artifact (lifecycle + governance need).
2. Gather inputs; reuse existing analysis/design outputs—do not re-invent.
3. Fill **Mandatory Fields**; mark N/A with rationale where not applicable.
4. Maintain requirement/scenario/case IDs for traceability.
5. Run **Review Checklist**; route per **Approval Flow**.
6. Store versioned Markdown; export to Excel/ADO/Jira as needed (Sprint 6 deepens ADO).
7. If publishing under `outputs/<project>/`, run the output-engine conversion per repo standards.

## Sections

{sections_md}

## Mandatory Fields

{bullets(mandatory)}

## Optional Fields

{bullets(optional)}

## Review Checklist

{bullets(checklist_items)}

## Approval Flow

1. Author ({owner}) → draft complete  
2. Reviewers ({', '.join(reviewers)}) → comments resolved  
3. Approvers ({', '.join(approvers)}) → approved  
4. Baseline version; link in RTM / release pack as applicable  

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.1.0 | YYYY-MM-DD | [Name] | Initial draft |
| 0.2.0 | YYYY-MM-DD | [Name] | Review updates |
| 1.0.0 | YYYY-MM-DD | [Name] | Approved baseline |

## Related Documents

{bullets(related)}

## Example Output

{example}

## Future Enhancements

- Sprint 6: deeper Azure DevOps field mapping
- Industry-specific examples under `scenarios/`
"""


def playbook_doc(slug: str, meta: dict) -> str:
    title = meta.get("title") or titleize(slug)
    related = CROSS + [
        "[Document Generation Rules](../guidelines/document-generation-rules.md)",
        "[README.md](README.md)",
    ]
    return f"""---
title: {title} Playbook
module: Salesforce Quality Engineering
category: Playbook
document_type: Playbook
version: {VERSION}
review_status: Draft
owner: QE Practice Lead
created_date: {DATE}
last_updated: {DATE}
review_cycle: quarterly
keywords: [{slug}, playbook]
tags: [playbook, sprint-5]
---

# {title} Playbook

## Purpose

{meta['purpose']}

## Participants

{bullets(meta.get('participants', ['QE Lead', 'BA', 'Delivery Lead']))}

## Inputs

{bullets(meta.get('inputs', ['Scope', 'Prior artifacts']))}

## Activities

{bullets(meta.get('activities', ['Prepare', 'Facilitate', 'Document outcomes', 'Confirm next steps']))}

## Outputs

{bullets(meta.get('outputs', ['Meeting outcomes', 'Updated artifacts']))}

## Success Criteria

{bullets(meta.get('success', ['Outcomes documented', 'Owners and dates assigned', 'Open risks logged']))}

## Escalation Points

{bullets(meta.get('escalation', ['Unresolved Critical gaps blocking design/execution', 'Missing approver / environment', 'Regulatory ambiguity — Legal/Compliance']))}

## Related Documents

{bullets(related + [f"[{titleize(t)}](../templates/{t}.md)" for t in meta.get('templates', [])])}

## Navigation

- **See Also:** [README.md](README.md) · [Deliverable Selection](../guidelines/deliverable-selection.md)
"""


# ---------------------------------------------------------------------------
# Template catalog
# ---------------------------------------------------------------------------

TEMPLATES = [
    ("test-strategy", {
        "purpose": "Define the overall quality approach for a Salesforce program or major release—what will be tested, how, where, by whom, and how risk is governed.",
        "phase": "Initiate / Plan",
        "owner": "Test Manager / QE Lead",
        "when": "Create at program or major release start—before detailed test planning—when strategy alignment is required.",
        "inputs": ["Business objectives", "Scope / clouds", "Constraints", "Risk appetite", "Environment landscape", "Automation intent"],
        "outputs": ["Approved Test Strategy", "Inputs to Test Plan and estimation"],
        "related_tpl": ["test-plan", "risk-assessment", "entry-criteria-checklist", "exit-criteria-checklist"],
        "sections": ["Document Control", "Scope & Objectives", "In/Out of Scope", "Testing Types & Levels", "Environment Strategy", "Resource Strategy", "Risk Strategy", "Automation Strategy", "Regression Strategy", "Defect Management", "Entry Criteria", "Exit Criteria", "Assumptions", "Dependencies", "Deliverables", "Communication Plan", "Metrics", "Governance", "Approvals"],
        "mandatory": ["Scope", "Objectives", "Testing types", "Environments", "Entry/Exit criteria", "Risk approach", "Owner", "Version"],
        "optional": ["Tooling details", "Training plan", "Vendor/ISV specifics"],
        "example": """### Excerpt — Objectives
1. Validate Service Cloud Case intake for CSR personas against AC.
2. Reduce production escape of permission defects via persona-based testing.
3. Establish risk-based regression for bi-weekly releases.""",
    }),
    ("test-plan", {
        "purpose": "Operationalize the Test Strategy for a sprint, release, or workstream with schedule, scope, data, resources, and execution plan.",
        "phase": "Plan / Sprint Planning",
        "owner": "Test Lead",
        "when": "Create per sprint or release after Test Strategy exists (or lightweight strategy for small changes).",
        "inputs": ["Test Strategy", "Backlog / stories", "Environment calendar", "Resource plan", "Risks"],
        "outputs": ["Approved Test Plan", "Execution schedule", "Reporting cadence"],
        "related_tpl": ["test-strategy", "test-scenario-document", "daily-status-report", "test-summary-report"],
        "sections": ["Document Control", "Scope & Objectives", "Features In Scope", "Features Out of Scope", "Schedule & Milestones", "Environment", "Resources", "Test Data", "Risks", "Dependencies", "Execution Plan", "Reporting", "Approvals"],
        "mandatory": ["In/Out scope", "Schedule", "Environments", "Resources", "Entry/exit references", "Risks"],
    }),
    ("requirement-review-report", {
        "purpose": "Document QE requirement review outcomes: quality score, gaps, questions, risks, and recommendations—without inventing scope.",
        "phase": "Discover / Refine",
        "owner": "QE Analyst / Test Lead",
        "when": "After Requirement Analysis Engine run on a story/epic/BRD excerpt.",
        "inputs": ["Requirement / story / AC", "Sprint 2 analysis outputs"],
        "outputs": ["Review report", "Clarification questions", "Quality score"],
        "related_tpl": ["requirement-gap-analysis", "requirement-quality-assessment", "risk-assessment"],
        "sections": ["Executive Summary", "Quality Score", "Gaps", "Questions", "Risks", "Salesforce Component Impact", "Recommendations", "Next Steps"],
    }),
    ("requirement-gap-analysis", {
        "purpose": "Catalog missing rules, AC themes, security, data, integration, and NFR gaps for stakeholder closure.",
        "phase": "Discover / Refine",
        "owner": "QE Analyst",
        "when": "When completeness gaps must be tracked to closure before design/build.",
        "related_tpl": ["requirement-review-report"],
        "sections": ["Gap ID", "Category", "Description", "Impact", "Owner", "Due Date", "Status"],
        "mandatory": ["Gap ID", "Category", "Impact", "Owner", "Status"],
    }),
    ("requirement-quality-assessment", {
        "purpose": "Score requirement quality across standard QE dimensions (1–5) with rationale.",
        "phase": "Discover / Refine",
        "owner": "QE Analyst",
        "when": "Alongside or within requirement review for governance dashboards.",
        "related_tpl": ["requirement-review-report"],
        "sections": ["Dimensions table", "Overall score", "Critical blockers", "Recommendations"],
    }),
    ("risk-assessment", {
        "purpose": "Capture quality risks (business, technical, data, security, integration, release) with mitigations and owners.",
        "phase": "Plan / Ongoing",
        "owner": "Test Lead / QE Lead",
        "when": "At planning and whenever material change increases residual risk.",
        "related_tpl": ["test-strategy", "release-readiness-checklist"],
        "sections": ["Risk register", "Probability/Impact", "Mitigation", "Contingency", "Owner", "Status"],
    }),
    ("rtm", {
        "purpose": "Maintain bidirectional traceability from requirements through scenarios, cases, automation, regression, and production validation.",
        "phase": "Design / Execute / Release",
        "owner": "Test Lead",
        "when": "When governance requires proof of coverage; support Business / Sprint / Release / UAT / Regression RTM views.",
        "inputs": ["BR/US/AC IDs", "Business rules", "Salesforce components", "Scenario/case IDs"],
        "outputs": ["RTM matrix (Markdown/Excel/ADO)", "Coverage gaps list"],
        "related_tpl": ["test-scenario-document", "test-case-document", "test-summary-report"],
        "sections": ["RTM type (Business/Sprint/Release/UAT/Regression)", "Traceability columns", "Coverage status", "Gaps", "Approvals"],
        "mandatory": ["Requirement ID", "Scenario ID", "Case ID (when cases exist)", "Status"],
        "example": """| BR | Story | AC | Rule | SF Component | Scenario | Case | Auto | Reg | Prod Val |
|----|-------|----|------|--------------|----------|------|------|-----|----------|
| BR-01 | US-1024 | AC1 | BR1 | Case.Status | TS-01 | TC-01 | Y | Y | Y |""",
    }),
    ("test-scenario-document", {
        "purpose": "Capture enterprise test scenario objectives (what/why) before or alongside detailed cases.",
        "phase": "Design",
        "owner": "QE Analyst",
        "when": "After Test Design Engine; before or with case authoring.",
        "related_tpl": ["test-case-document", "rtm", "automation-candidate-matrix"],
        "sections": ["Scenario ID", "Title/Objective", "Business Process", "Preconditions", "Scope", "Priority", "Rules/AC Covered", "Risk", "Automation Candidate", "Regression Required", "Dependencies"],
        "mandatory": ["Scenario ID", "Objective", "Priority", "AC/Rule refs"],
    }),
    ("test-case-document", {
        "purpose": "Author executable test cases for ADO, Excel, Jira Xray, Zephyr, or manual packs.",
        "phase": "Design / Execute",
        "owner": "QE Analyst / Tester",
        "when": "When executable steps are required—after scenario objectives exist. Prefer nested Given/When/Then style where ADO-compatible.",
        "related_tpl": ["test-scenario-document", "rtm", "defect-report"],
        "sections": ["Case ID", "Title", "Objective", "Preconditions", "Test Data", "Steps", "Expected Results", "Postconditions", "Priority", "Requirement Mapping", "Automation Candidate", "Tags (Smoke/Regression/UAT)", "Tool format notes (ADO/Excel/Xray/Zephyr)"],
        "mandatory": ["Case ID", "Title", "Steps", "Expected Results", "Requirement/Scenario link", "Priority"],
        "example": """**TC-0142** — CSR updates preferred communication method  
Preconditions: CSR persona; Account with Contact  
| Step | Action | Expected |
|------|--------|----------|
| 1 | Open Contact | Record loads |
| 2 | Set Preferred Method = Email | Value saves; no error |""",
    }),
    ("exploratory-testing-charter", {
        "purpose": "Time-boxed exploratory charter with mission, charter, and debrief notes.",
        "phase": "Execute",
        "owner": "QE Analyst",
        "when": "For risk-based discovery beyond scripted cases.",
        "sections": ["Mission", "Charter", "Time box", "Areas of focus", "Risks", "Debrief notes", "Bugs/questions found"],
    }),
    ("smoke-test-checklist", {
        "purpose": "Minimal critical-path checks after build/deploy.",
        "phase": "Deploy / Execute",
        "owner": "Test Lead",
        "when": "After every deploy to a test or production environment.",
        "related_tpl": ["deployment-validation-checklist", "sanity-test-checklist"],
        "sections": ["Build/Deploy ID", "Environment", "Checklist items", "Pass/Fail", "Blockers", "Sign-off"],
    }),
    ("sanity-test-checklist", {
        "purpose": "Narrow confirmation around a specific change set.",
        "phase": "Execute",
        "owner": "Tester",
        "when": "After targeted fixes or small changes when full regression is not justified.",
        "related_tpl": ["smoke-test-checklist", "regression-checklist"],
    }),
    ("regression-checklist", {
        "purpose": "Risk-based regression pack checklist for a release or sprint.",
        "phase": "Execute / Release",
        "owner": "Test Lead",
        "when": "Before release or after high-impact changes.",
        "related_tpl": ["rtm", "test-summary-report"],
        "sections": ["In scope packs", "Out of scope", "Conditional items", "Results", "Residual risk"],
    }),
    ("sit-checklist", {
        "purpose": "System Integration Testing readiness and execution checklist.",
        "phase": "Execute",
        "owner": "Test Lead / Integration Lead (QE)",
        "when": "Before and during SIT cycles.",
    }),
    ("uat-checklist", {
        "purpose": "UAT readiness and execution support checklist (partner with BA UAT process).",
        "phase": "UAT",
        "owner": "UAT Coordinator / Test Lead",
        "when": "Before UAT entry and during UAT execution.",
        "related_tpl": ["entry-criteria-checklist", "exit-criteria-checklist"],
    }),
    ("production-validation-checklist", {
        "purpose": "Post-go-live / production verification checklist.",
        "phase": "Hypercare / Production",
        "owner": "Test Lead / Release Manager (QE input)",
        "when": "Immediately after production deploy and during early hypercare.",
        "related_tpl": ["hypercare-validation-checklist", "go-no-go-checklist"],
    }),
    ("deployment-validation-checklist", {
        "purpose": "Pre/during/post deployment validation evidence checklist.",
        "phase": "Deploy",
        "owner": "Test Lead",
        "when": "Every controlled deployment to higher environments.",
        "related_tpl": ["smoke-test-checklist", "environment-readiness-checklist"],
    }),
    ("go-no-go-checklist", {
        "purpose": "Evidence-oriented Go/No-Go decision support checklist.",
        "phase": "Release",
        "owner": "Test Manager / QE Lead",
        "approvers": ["Release Manager", "Delivery Lead", "Business Owner (as required)"],
        "when": "At release decision meeting.",
        "related_tpl": ["release-readiness-checklist", "test-summary-report", "risk-assessment"],
        "sections": ["Entry evidence", "Open Critical/High defects", "Residual risk", "Rollback readiness", "Recommendation", "Decision", "Attendees"],
    }),
    ("release-readiness-checklist", {
        "purpose": "Consolidate readiness evidence before Go/No-Go.",
        "phase": "Release",
        "owner": "Test Lead",
        "when": "Prior to release decision; update as evidence lands.",
        "related_tpl": ["go-no-go-checklist", "exit-criteria-checklist"],
    }),
    ("defect-report", {
        "purpose": "Standard defect documentation for triage, fix, and retest.",
        "phase": "Execute",
        "owner": "Tester / QE Analyst",
        "when": "When a verified failure against expected behaviour is found.",
        "related_tpl": ["defect-rca-report", "test-case-document"],
        "sections": ["Summary", "Description", "Steps", "Expected", "Actual", "Environment", "Browser/Client", "Evidence", "Severity", "Priority", "Business Impact", "Technical Impact", "Requirement/Case link", "Retest notes", "Regression impact"],
        "mandatory": ["Summary", "Steps", "Expected", "Actual", "Environment", "Severity", "Priority"],
    }),
    ("defect-rca-report", {
        "purpose": "Root cause analysis for escaped or high-impact defects.",
        "phase": "Execute / Hypercare / Improve",
        "owner": "Test Lead + Dev Lead",
        "when": "For production escapes, Critical defects, or recurring failure patterns.",
        "related_tpl": ["defect-report", "lessons-learned"],
        "sections": ["Problem statement", "Timeline", "Root cause", "Contributing causes", "Corrective actions", "Preventive actions", "Process improvements"],
    }),
    ("test-summary-report", {
        "purpose": "Summarize execution outcomes, coverage, defects, and residual risk for a cycle.",
        "phase": "Execute / Release",
        "owner": "Test Lead",
        "when": "At end of sprint test cycle, SIT, UAT, or release test phase.",
        "related_tpl": ["rtm", "weekly-status-report", "go-no-go-checklist"],
        "sections": ["Scope", "Execution summary", "Coverage", "Defects", "Risks", "Recommendations", "Appendix metrics"],
    }),
    ("daily-status-report", {
        "purpose": "Daily QA pulse: planned vs actual, blockers, defects, risks.",
        "phase": "Execute",
        "owner": "Test Lead",
        "when": "During active execution (daily or per stand-up cadence).",
        "related_tpl": ["weekly-status-report"],
        "sections": ["Date", "Environment", "Executed today", "Pass/Fail", "Blockers", "New defects", "Plan tomorrow"],
    }),
    ("weekly-status-report", {
        "purpose": "Weekly QA trend report for delivery governance.",
        "phase": "Execute",
        "owner": "Test Lead / Test Manager",
        "when": "Weekly during delivery.",
        "related_tpl": ["daily-status-report", "executive-qa-dashboard"],
        "sections": ["Highlights", "Metrics", "Defect trends", "Risks", "Asks", "Next week plan"],
    }),
    ("executive-qa-dashboard", {
        "purpose": "One-page executive view of quality outcomes, risk, and Go/No-Go posture.",
        "phase": "Release / Governance",
        "owner": "Test Manager",
        "when": "Steering / release reviews.",
        "related_tpl": ["test-summary-report", "go-no-go-checklist"],
        "sections": ["Outcome KPIs", "Coverage", "Defect burn", "Top risks", "Recommendation", "Asks"],
    }),
    ("automation-assessment-report", {
        "purpose": "Assess automation feasibility, ROI themes, and readiness (no scripts required).",
        "phase": "Plan / Design",
        "owner": "Automation Lead / QE Lead",
        "when": "When deciding what to automate for a release or program.",
        "related_tpl": ["automation-candidate-matrix"],
    }),
    ("automation-candidate-matrix", {
        "purpose": "Classify scenarios/cases: Suitable / Manual only / API / UI / Smoke / Regression automation.",
        "phase": "Design",
        "owner": "QE Analyst / Automation Lead",
        "when": "After scenario design; before automation backlog commit.",
        "related_tpl": ["test-scenario-document", "automation-assessment-report"],
        "sections": ["ID", "Candidate class", "Rationale", "Priority", "Tooling intent", "Owner"],
    }),
    ("test-data-strategy", {
        "purpose": "Define test data approach: synthetic vs masked, personas, referential integrity, refresh.",
        "phase": "Plan",
        "owner": "Test Lead / Data Lead (QE)",
        "when": "Before major SIT/UAT; update when data model changes materially.",
        "related_tpl": ["test-data-request", "environment-readiness-checklist"],
    }),
    ("test-data-request", {
        "purpose": "Request specific test data sets with acceptance criteria for readiness.",
        "phase": "Plan / Execute",
        "owner": "Tester",
        "when": "When data provisioning is required from ops/integration teams.",
        "related_tpl": ["test-data-strategy"],
    }),
    ("environment-readiness-checklist", {
        "purpose": "Confirm environment configuration, access, integrations, and data readiness.",
        "phase": "Plan / Deploy",
        "owner": "Test Lead",
        "when": "Before test cycle entry and after refreshes.",
        "related_tpl": ["entry-criteria-checklist", "deployment-validation-checklist"],
    }),
    ("test-estimation-sheet", {
        "purpose": "Capture estimation inputs (T-shirt / relative sizing)—not false precision hours as story points.",
        "phase": "Plan",
        "owner": "Test Lead",
        "when": "During planning/refinement for test effort inputs.",
        "sections": ["Work item", "Complexity", "Uncertainty", "Dependencies", "T-shirt", "Notes", "Team confirmation"],
        "mandatory": ["Work item", "T-shirt or relative size", "Assumptions"],
    }),
    ("entry-criteria-checklist", {
        "purpose": "Gate checklist to enter a test phase (SIT/UAT/Regression/Prod Val).",
        "phase": "Plan / Execute",
        "owner": "Test Lead",
        "when": "Before starting a named test phase.",
        "related_tpl": ["exit-criteria-checklist", "environment-readiness-checklist"],
    }),
    ("exit-criteria-checklist", {
        "purpose": "Gate checklist to exit a test phase with residual risk stated.",
        "phase": "Execute / Release",
        "owner": "Test Lead",
        "when": "Before declaring a phase complete.",
        "related_tpl": ["entry-criteria-checklist", "test-summary-report", "go-no-go-checklist"],
    }),
    ("lessons-learned", {
        "purpose": "Capture what worked, what failed, and actions for the next release/program.",
        "phase": "Close / Improve",
        "owner": "Test Manager",
        "when": "After release or major incident RCA cycle.",
        "related_tpl": ["defect-rca-report", "knowledge-transfer-checklist"],
    }),
    ("hypercare-validation-checklist", {
        "purpose": "Structured hypercare validation and monitoring checks.",
        "phase": "Hypercare",
        "owner": "Test Lead / Production Support (QE)",
        "when": "During agreed hypercare window post go-live.",
        "related_tpl": ["production-validation-checklist"],
    }),
    ("knowledge-transfer-checklist", {
        "purpose": "KT checklist for handing quality knowledge to BAU/support teams.",
        "phase": "Close / Hypercare",
        "owner": "Test Lead",
        "when": "Before exit from project QE ownership.",
        "related_tpl": ["lessons-learned"],
    }),
    # Additional reporting / dashboard standards as templates
    ("sprint-qa-dashboard", {
        "purpose": "Sprint-level QA dashboard: burndown of cases, pass rate, blockers.",
        "phase": "Execute",
        "owner": "Test Lead",
        "when": "Sprint reviews / daily governance.",
    }),
    ("release-dashboard", {
        "purpose": "Release-level quality dashboard for readiness posture.",
        "phase": "Release",
        "owner": "Test Manager",
        "when": "Release trains / cutover weeks.",
    }),
    ("defect-dashboard", {
        "purpose": "Defect aging, severity mix, reopen rate dashboard standard.",
        "phase": "Execute",
        "owner": "Test Lead",
        "when": "Throughout execution and hypercare.",
    }),
    ("automation-dashboard", {
        "purpose": "Automation coverage, stability, and candidate backlog view.",
        "phase": "Execute / Improve",
        "owner": "Automation Lead",
        "when": "When automation program is active.",
    }),
    ("coverage-dashboard", {
        "purpose": "Requirement/scenario/case coverage dashboard aligned to RTM.",
        "phase": "Design / Execute",
        "owner": "Test Lead",
        "when": "When coverage governance is required.",
        "related_tpl": ["rtm"],
    }),
    ("quality-metrics-dashboard", {
        "purpose": "Quality metrics pack: escape rate, defect density themes, cycle time (define formulas per program).",
        "phase": "Governance",
        "owner": "Test Manager",
        "when": "Steering and continuous improvement reviews.",
    }),
]

PLAYBOOKS = [
    ("requirement-review", {
        "purpose": "Facilitate QE requirement review using the Requirement Analysis Engine.",
        "participants": ["QE Analyst", "BA", "SA (optional)", "PO/Business"],
        "inputs": ["Story/BRD/AC", "Prior RAID"],
        "activities": ["Load Sprint 2 engine", "Score quality", "Capture gaps/questions", "Agree owners/dates"],
        "outputs": ["Requirement Review Report", "Gap log", "Updated questions"],
        "templates": ["requirement-review-report", "requirement-gap-analysis", "requirement-quality-assessment"],
        "success": ["Critical questions assigned", "Quality score recorded", "No silent scope"],
    }),
    ("story-grooming", {
        "purpose": "QE participation in grooming to improve testability of stories and AC.",
        "participants": ["PO", "BA", "QE", "Dev"],
        "activities": ["Challenge AC observability", "Permission/negative paths", "Data/integration asks"],
        "outputs": ["Updated AC notes", "Risk flags", "Estimation inputs"],
        "templates": ["risk-assessment", "test-estimation-sheet"],
    }),
    ("test-planning", {
        "purpose": "Produce or refresh Test Plan from strategy and backlog.",
        "participants": ["Test Lead", "QE team", "Delivery Lead"],
        "templates": ["test-plan", "test-strategy", "environment-readiness-checklist"],
        "outputs": ["Test Plan", "Schedule", "Resource asks"],
    }),
    ("test-design-review", {
        "purpose": "Peer review of scenarios/cases/coverage before execution.",
        "participants": ["QE peers", "BA (optional)", "Automation Lead"],
        "activities": ["Check INVEST-like scenario quality", "Coverage gaps", "Automation candidates"],
        "templates": ["test-scenario-document", "test-case-document", "rtm"],
    }),
    ("regression-planning", {
        "purpose": "Select risk-based regression scope for a release.",
        "participants": ["Test Lead", "BA", "SA", "Release Manager"],
        "templates": ["regression-checklist", "rtm", "risk-assessment"],
        "outputs": ["In/Out/Conditional pack", "Owners"],
    }),
    ("defect-triage", {
        "purpose": "Triage defects for severity, priority, owner, and target fix.",
        "participants": ["Test Lead", "Dev Lead", "BA/PO", "SA (as needed)"],
        "templates": ["defect-report", "defect-dashboard"],
        "escalation": ["Priority disputes on business impact", "Environment unavailable for retest"],
    }),
    ("release-readiness", {
        "purpose": "Assemble readiness evidence and residual risk for Go/No-Go.",
        "participants": ["Test Manager", "Release Manager", "BA", "Dev Lead"],
        "templates": ["release-readiness-checklist", "go-no-go-checklist", "test-summary-report"],
    }),
    ("production-validation", {
        "purpose": "Execute production validation / early verification after deploy.",
        "participants": ["Test Lead", "Release Manager", "Support"],
        "templates": ["production-validation-checklist", "smoke-test-checklist"],
    }),
    ("hypercare", {
        "purpose": "Operate hypercare quality checks and feedback loop.",
        "participants": ["QE", "Support", "Dev", "BA"],
        "templates": ["hypercare-validation-checklist", "defect-report", "lessons-learned"],
    }),
    ("knowledge-transfer", {
        "purpose": "Transfer QA knowledge, packs, and monitoring cues to BAU.",
        "participants": ["Test Lead", "BAU Support", "Automation Lead"],
        "templates": ["knowledge-transfer-checklist", "lessons-learned"],
    }),
]


def write_guidelines() -> None:
    g = ROOT / "guidelines"
    g.mkdir(parents=True, exist_ok=True)

    (g / "README.md").write_text(f"""---
title: Guidelines — README
module: Salesforce Quality Engineering
category: Guide
document_type: Guide
version: {VERSION}
---

# Guidelines

## Purpose

Documentation intelligence and generation standards for Sprint 5.

## Scope

When/why/how to create artifacts; selection rules; generation rules; reporting & defect standards.

## Available Documents

| Document | Focus |
|----------|-------|
| [document-intelligence.md](document-intelligence.md) | When, who, inputs, outputs, phase, links |
| [deliverable-selection.md](deliverable-selection.md) | Which artifact when |
| [artifact-relationships.md](artifact-relationships.md) | How artifacts relate |
| [document-generation-rules.md](document-generation-rules.md) | Generation hard rules |
| [template-standards.md](template-standards.md) | Template structure standards |
| [reporting-standards.md](reporting-standards.md) | QA reporting / dashboards |
| [defect-documentation-standards.md](defect-documentation-standards.md) | Defect & RCA standards |

## Navigation

- **Previous:** [../templates/README.md](../templates/README.md)
- **Next:** [../document-generation/README.md](../document-generation/README.md)
- **See Also:** [../skill.md](../skill.md)
""", encoding="utf-8")

    (g / "document-intelligence.md").write_text(f"""---
title: Document Intelligence
version: {VERSION}
tags: [guidelines, sprint-5]
---

# Document Intelligence

Teach the AI **when** and **why** to create each QA document—not only the blank form.

## Core questions (every artifact)

| Question | Guidance |
|----------|----------|
| When? | Lifecycle phase + trigger event (see template Document Intelligence table) |
| Who owns? | Named role in template |
| Who reviews / approves? | Reviewers and approvers in template |
| Inputs? | Prefer reuse from Sprint 2/3 outputs and prior artifacts |
| Outputs? | Downstream consumers (RTM, summary, Go/No-Go) |
| Links? | See [artifact-relationships.md](artifact-relationships.md) |
| Phase? | Discover → Plan → Design → Execute → Release → Hypercare → Close |

## Lifecycle map (summary)

| Phase | Typical artifacts |
|-------|-------------------|
| Discover / Refine | Requirement Review, Gap Analysis, Quality Assessment, Risk |
| Plan | Test Strategy, Test Plan, Estimation, Data Strategy, Entry Criteria |
| Design | Scenarios, Cases, RTM, Automation Candidate Matrix, Design Review |
| Execute | Daily/Weekly status, Defects, Smoke/Sanity/Regression checklists, SIT/UAT |
| Release | Release Readiness, Go/No-Go, Test Summary, Dashboards |
| Hypercare / Close | Production Validation, Hypercare, Lessons Learned, KT |

## Rules

- Never create unnecessary documents ([document-generation-rules.md](document-generation-rules.md)).
- Small change → prefer checklist + sanity over full strategy rewrite.
- Always maintain traceability IDs.

## Related

{bullets(CROSS)}
""", encoding="utf-8")

    (g / "deliverable-selection.md").write_text(f"""---
title: Deliverable Selection Logic
version: {VERSION}
---

# Deliverable Selection Logic

| Situation | Prefer | Avoid |
|-----------|--------|-------|
| New program / major release | Test Strategy + Plan | Jumping to cases only |
| Single story clarification | Requirement Review Report | Full RTM rebuild |
| Need coverage proof | RTM (appropriate view) | Unlinked case dumps |
| Design complete, need execution | Scenario doc → Cases | Cases without objectives |
| Deploy tonight | Smoke + Deployment Validation | Full regression unless risk says so |
| Release decision | Readiness + Go/No-Go + Summary | Dashboard without evidence |
| Production escape | Defect + RCA | Closing without preventive actions |
| Automation ask | Candidate Matrix + Assessment | Scripts without candidates |
| UAT start | UAT + Entry Criteria | Starting without environment readiness |

## Project type tailoring

| Project type | Tailoring |
|--------------|-----------|
| Agile sprint | Lightweight plan; Sprint RTM; daily status |
| SAFe ART | Strategy per PI; Release RTM; dashboards |
| Waterfall / gated | Full strategy/plan; formal entry/exit; approvals |
| Package upgrade | Upgrade-focused regression + smoke; vendor notes |
| Integration-heavy | SIT checklist + integration defect fields |

## Related

- [document-intelligence.md](document-intelligence.md)
- [../templates/README.md](../templates/README.md)
""", encoding="utf-8")

    (g / "artifact-relationships.md").write_text(f"""---
title: Artifact Relationships
version: {VERSION}
---

# Artifact Relationships

```
Requirement Review / Gap / Quality Score
        ↓
   Risk Assessment
        ↓
 Test Strategy → Test Plan
        ↓
 Test Design (scenarios) → RTM
        ↓
 Test Cases ←→ Automation Candidate Matrix
        ↓
 Execution (Daily/Weekly) + Defects
        ↓
 Test Summary → Release Readiness → Go/No-Go
        ↓
 Production Validation → Hypercare → Lessons Learned / KT
```

## Traceability chain (RTM)

Business Requirement → User Story → AC → Business Rule → Salesforce Component → Scenario → Case → Automation → Regression → Production Validation

## Related

{bullets(CROSS)}
""", encoding="utf-8")

    (g / "document-generation-rules.md").write_text(f"""---
title: Document Generation Rules
version: {VERSION}
---

# Document Generation Rules

## Hard rules

1. **Never create unnecessary documents** — use [deliverable-selection.md](deliverable-selection.md).
2. **Lifecycle-based** — generate what the phase requires.
3. **Reuse** — pull from Requirement Analysis and Test Design outputs; do not rewrite from scratch.
4. **No duplicate content** — link related artifacts; summarize deltas only.
5. **Traceability** — preserve IDs across RTM, scenarios, cases, defects.
6. **Consistent formatting** — Markdown tables; consulting tone; no client PII/credentials.
7. **Enterprise governance** — include owner, version, status, approval where required.
8. **Analysis before heavy docs** — Strategy/Plan/RTM/Cases require Sprint 2 (± Sprint 3) unless user explicitly provides ready inputs.
9. **No silent invention** — mark assumptions; do not invent regulatory requirements.
10. **Export awareness** — structure for ADO / Jira / Excel; Sprint 6 deepens ADO publish.

## Tooling notes

| Target | Guidance |
|--------|----------|
| Markdown | Source of truth in repo / `outputs/<project>/` |
| Excel | Tables map 1:1 from template sections |
| Azure DevOps | Cases/defects as work items (Sprint 6) |
| Jira Xray / Zephyr | Preserve step/expected columns |

## Related

- [template-standards.md](template-standards.md)
""", encoding="utf-8")

    (g / "template-standards.md").write_text(f"""---
title: Template Standards
version: {VERSION}
---

# Template Standards

Every Sprint 5 template includes:

Purpose · Business Context · Audience · Owner · Inputs · Outputs · Prerequisites · Instructions · Sections · Mandatory Fields · Optional Fields · Review Checklist · Approval Flow · Version History · Related Documents · Example Output

Plus **Document Intelligence** (when / reviewers / approvers / phase).

## Quality bar

- Consulting-grade, reusable, modular
- Supports Agile, Scrum, SAFe, Waterfall
- Industry-agnostic with Salesforce hooks via 4A/4B links
- ISTQB-aligned terminology where applicable
""", encoding="utf-8")

    (g / "reporting-standards.md").write_text(f"""---
title: Reporting Standards
version: {VERSION}
---

# Reporting Standards

| Report / Dashboard | Cadence | Audience | Template |
|--------------------|---------|----------|----------|
| Daily QA Status | Daily | Delivery team | [daily-status-report](../templates/daily-status-report.md) |
| Weekly QA Report | Weekly | Delivery + PMO | [weekly-status-report](../templates/weekly-status-report.md) |
| Sprint QA Dashboard | Sprint | Scrum team | [sprint-qa-dashboard](../templates/sprint-qa-dashboard.md) |
| Release Dashboard | Release | Release mgmt | [release-dashboard](../templates/release-dashboard.md) |
| Executive QA Dashboard | Steering | Executives | [executive-qa-dashboard](../templates/executive-qa-dashboard.md) |
| Defect Dashboard | Ongoing | Triage forum | [defect-dashboard](../templates/defect-dashboard.md) |
| Automation Dashboard | Ongoing | Automation guild | [automation-dashboard](../templates/automation-dashboard.md) |
| Coverage Dashboard | Ongoing | QE + BA | [coverage-dashboard](../templates/coverage-dashboard.md) |
| Quality Metrics Dashboard | Monthly/PI | Leadership | [quality-metrics-dashboard](../templates/quality-metrics-dashboard.md) |
| Test Summary | Phase end | Approvers | [test-summary-report](../templates/test-summary-report.md) |

## Rules

- Metrics must define formula and data source; never invent coverage %.
- Executive views: outcomes and residual risk first; detail in appendix.
""", encoding="utf-8")

    (g / "defect-documentation-standards.md").write_text(f"""---
title: Defect Documentation Standards
version: {VERSION}
---

# Defect Documentation Standards

## Defect report must include

Summary · Description · Steps · Expected · Actual · Environment · Browser/Client · Evidence · Severity · Priority · Business Impact · Technical Impact · Requirement/Case link · Retest notes · Regression impact

Template: [defect-report](../templates/defect-report.md)

## RCA report must include

Problem · Timeline · Root cause · Contributing causes · Corrective · Preventive · Process improvements

Template: [defect-rca-report](../templates/defect-rca-report.md)

## Severity vs priority

- **Severity** = technical/business impact of the failure
- **Priority** = order of fix relative to release risk

Do not conflate the two.
""", encoding="utf-8")


def write_document_generation() -> None:
    d = ROOT / "document-generation"
    d.mkdir(parents=True, exist_ok=True)

    (d / "README.md").write_text(f"""---
title: Document Generation — README
version: {VERSION}
---

# Document Generation

## Purpose

Teach the AI **how to generate** consulting-grade QA artifacts using templates + engines (not blank forms alone).

## Scope

Generators for Strategy, Plan, RTM, Scenarios, Cases, Defects, and Reporting.

## Available Documents

| Generator | Focus |
|-----------|-------|
| [test-strategy-generator.md](test-strategy-generator.md) | Test Strategy |
| [test-plan-generator.md](test-plan-generator.md) | Test Plan |
| [rtm-generator.md](rtm-generator.md) | RTM views |
| [test-scenario-generator.md](test-scenario-generator.md) | Scenarios |
| [test-case-generator.md](test-case-generator.md) | Cases (ADO/Excel/Xray/Zephyr) |
| [defect-generator.md](defect-generator.md) | Defect + RCA |
| [reporting-generator.md](reporting-generator.md) | Status, summary, dashboards |

## Navigation

- **Previous:** [../guidelines/README.md](../guidelines/README.md)
- **Next:** [../playbooks/README.md](../playbooks/README.md)
- **See Also:** [../templates/README.md](../templates/README.md)
""", encoding="utf-8")

    gens = {
        "test-strategy-generator.md": """# Test Strategy Generator

## When to use

Program or major release start. Template: [test-strategy](../templates/test-strategy.md).

## Required inputs

Business objectives · Scope/clouds · Constraints · Risks · Environments · Automation intent · Org methodology (Agile/SAFe/Waterfall)

## Generation steps

1. Confirm Strategy is warranted (vs lightweight plan-only).
2. Run/reuse Requirement Analysis themes for scope risks.
3. Map testing types/levels to Salesforce components (4A/4B).
4. Fill all mandatory strategy sections:
   Scope · Objectives · Testing Types · Environment Strategy · Resource Strategy · Risk Strategy · Automation Strategy · Regression Strategy · Defect Management · Entry Criteria · Exit Criteria · Assumptions · Dependencies · Deliverables · Communication Plan · Metrics · Governance
5. Mark assumptions; list open questions.
6. Route for review/approval.

## Tailoring

| Size | Tailoring |
|------|-----------|
| Small change | 1–2 page strategy addendum |
| Enterprise program | Full strategy + governance |
""",
        "test-plan-generator.md": """# Test Plan Generator

## When to use

Per sprint/release after strategy exists. Template: [test-plan](../templates/test-plan.md).

## Sections to generate

Scope · Objectives · Features In/Out · Schedule · Environment · Resources · Test Data · Risks · Dependencies · Milestones · Execution Plan · Reporting · Approvals

## Steps

1. Import strategy decisions (do not contradict without change control).
2. Bind to backlog IDs and environment calendar.
3. Define entry/exit references.
4. Publish reporting cadence (daily/weekly).
""",
        "rtm-generator.md": """# RTM Generator

## Traceability chain

Business Requirement → User Story → Acceptance Criteria → Business Rule → Salesforce Component → Test Scenario → Test Case → Automation → Regression → Production Validation

## Supported views

| RTM type | Use |
|----------|-----|
| Business RTM | Program/BR coverage |
| Sprint RTM | Sprint backlog coverage |
| Release RTM | Release train evidence |
| UAT RTM | Business validation mapping |
| Regression RTM | Pack ↔ prior requirements |

## Rules

- Never invent coverage %.
- Gap rows must list remediation owner.
- Template: [rtm](../templates/rtm.md)
""",
        "test-scenario-generator.md": """# Test Scenario Generator

## Fields

Scenario ID · Objective · Business Process · Preconditions · Scope · Priority · Business Rules Covered · AC Covered · Risk Level · Automation Candidate · Regression Required · Dependencies

## Rules

- Objectives first (Sprint 3); steps belong in cases.
- Priority: Business Critical / High / Medium / Low with rationale.
- Template: [test-scenario-document](../templates/test-scenario-document.md)
""",
        "test-case-generator.md": """# Test Case Generator

## Formats

| Format | Notes |
|--------|-------|
| Azure DevOps | Title, steps HTML, AC link, tags |
| Excel | Columns for Step / Action / Expected |
| Jira Xray / Zephyr | Preserve step entities |
| Manual | Nested Given/When/Then acceptable |

## Fields

Title · Objective · Preconditions · Test Data · Steps · Expected Results · Postconditions · Automation Candidate · Priority · Requirement Mapping · Regression/Smoke/UAT tags

## Rules

- Generate only after scenario objectives (or explicit user request with ready AC).
- Include negative and permission paths when security is in scope.
- Template: [test-case-document](../templates/test-case-document.md)
""",
        "defect-generator.md": """# Defect Generator

## Defect

Generate all fields in [defect-documentation-standards](../guidelines/defect-documentation-standards.md) and [defect-report](../templates/defect-report.md).

## RCA

Use [defect-rca-report](../templates/defect-rca-report.md) for escapes and Critical defects.

## Rules

- Separate Severity vs Priority.
- Link to Case/Requirement IDs.
- Evidence without PII/credentials.
""",
        "reporting-generator.md": """# Reporting Generator

## Generate on request

- Daily Status → [daily-status-report](../templates/daily-status-report.md)
- Weekly Report → [weekly-status-report](../templates/weekly-status-report.md)
- Test Summary → [test-summary-report](../templates/test-summary-report.md)
- Executive Dashboard → [executive-qa-dashboard](../templates/executive-qa-dashboard.md)
- Other dashboards → see [reporting-standards](../guidelines/reporting-standards.md)

## Rules

- Cite data sources; no invented metrics.
- Executive view: recommendation + residual risk first.
""",
    }
    for name, body in gens.items():
        (d / name).write_text(f"---\ntitle: {name.replace('.md','').replace('-',' ').title()}\nversion: {VERSION}\ntags: [document-generation, sprint-5]\n---\n\n{body}\n\n## Related\n\n{bullets(CROSS)}\n", encoding="utf-8")


def main() -> None:
    # Templates
    tdir = ROOT / "templates"
    tdir.mkdir(parents=True, exist_ok=True)
    # remove old placeholder-only if regenerating all
    keep = {s + ".md" for s, _ in TEMPLATES} | {"README.md"}
    for p in tdir.glob("*.md"):
        if p.name not in keep:
            p.unlink()

    rows = []
    for slug, meta in TEMPLATES:
        (tdir / f"{slug}.md").write_text(template_doc(slug, meta), encoding="utf-8")
        rows.append(f"| [{meta.get('title') or titleize(slug)}]({slug}.md) | {meta['phase']} | {meta.get('owner', 'Test Lead')} |")

    (tdir / "README.md").write_text(f"""---
title: Templates — README
module: Salesforce Quality Engineering
version: {VERSION}
tags: [templates, sprint-5]
---

# Templates

## Purpose

Enterprise, consulting-grade QA templates for Salesforce Quality Engineering.

## Scope

{SPRINT} Documentation Generator — templates only (generation logic in `document-generation/` and `guidelines/`).

## Available Documents

| Template | Phase | Owner |
|----------|-------|-------|
{chr(10).join(rows)}

## Navigation

- **Previous:** [../knowledge/README.md](../knowledge/README.md)
- **Next:** [../guidelines/README.md](../guidelines/README.md)
- **See Also:** [../document-generation/README.md](../document-generation/README.md) · [../playbooks/README.md](../playbooks/README.md)

## Related Documents

{bullets(CROSS)}
""", encoding="utf-8")

    # Playbooks
    pdir = ROOT / "playbooks"
    pdir.mkdir(parents=True, exist_ok=True)
    keep_p = {s + ".md" for s, _ in PLAYBOOKS} | {"README.md"}
    for p in pdir.glob("*.md"):
        if p.name not in keep_p:
            p.unlink()
    prows = []
    for slug, meta in PLAYBOOKS:
        (pdir / f"{slug}.md").write_text(playbook_doc(slug, meta), encoding="utf-8")
        prows.append(f"| [{titleize(slug)}]({slug}.md) | {meta['purpose'][:80]} |")

    (pdir / "README.md").write_text(f"""---
title: Playbooks — README
version: {VERSION}
tags: [playbooks, sprint-5]
---

# Playbooks

## Purpose

Reusable facilitation playbooks for core QE ceremonies and gates.

## Scope

{SPRINT} — process playbooks (not BA OCM playbooks; cross-link BA where needed).

## Available Documents

| Playbook | Focus |
|----------|-------|
{chr(10).join(prows)}

## Navigation

- **Previous:** [../document-generation/README.md](../document-generation/README.md)
- **Next:** [../ado/README.md](../ado/README.md)
- **See Also:** [../templates/README.md](../templates/README.md)

## Related Documents

{bullets(CROSS)}
""", encoding="utf-8")

    write_guidelines()
    write_document_generation()
    print(f"Sprint 5 assets written under {ROOT} (templates={len(TEMPLATES)}, playbooks={len(PLAYBOOKS)})")


if __name__ == "__main__":
    main()
