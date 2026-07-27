"""Generate Metadata Impact Analyzer specialized skill pack."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "metadata-impact-analyzer"
VERSION = "0.15.0"
DATE = "2026-07-27"


def fm(title: str, category: str, doc_type: str, tags: list[str], extra: str = "") -> str:
    tag_str = ", ".join(tags)
    return f"""---
title: {title}
module: Salesforce Quality Engineering
category: {category}
document_type: {doc_type}
version: {VERSION}
review_status: Draft
owner: QE Practice Lead
created_date: {DATE}
last_updated: {DATE}
review_cycle: quarterly
tags: [{tag_str}]
{extra}---

"""


def write(rel: str, content: str) -> None:
    path = SKILL / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  wrote {rel}")


def knowledge_article(
    title: str,
    slug: str,
    purpose: str,
    reasoning: list[str],
    cross_links: list[tuple[str, str]],
    decision_rules: list[str],
) -> str:
    links = "\n".join(f"- [{name}]({path})" for name, path in cross_links)
    rules = "\n".join(f"- {r}" for r in decision_rules)
    model = "\n".join(f"{i}. {r}" for i, r in enumerate(reasoning, 1))
    return fm(title, "Specialized Skill Knowledge", "Knowledge Article", ["metadata-impact-analyzer", "knowledge"]) + f"""# {title}

## Purpose

{purpose}

## Reasoning Model

{model}

## Decision Rules

{rules}

## Cross-Links (Canonical Depth)

{links}

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)
- [../../knowledge/metadata/README.md](../../knowledge/metadata/README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| {VERSION} | {DATE} | QE Practice Lead | Initial specialized skill knowledge |
"""


def playbook(
    title: str,
    purpose: str,
    inputs: list[str],
    workflow: list[str],
    decisions: list[str],
    outputs: list[str],
    deliverables: list[str],
    escalation: list[str],
    pointer: str = "",
) -> str:
    def bullets(items: list[str]) -> str:
        return "\n".join(f"- {i}" for i in items)

    ptr = f"\n\n**Canonical ceremony pointer:** {pointer}" if pointer else ""
    return fm(title, "Specialized Skill Playbook", "Playbook", ["metadata-impact-analyzer", "playbook"]) + f"""# {title}

## Purpose

{purpose}{ptr}

## Inputs

{bullets(inputs)}

## Workflow

{bullets(workflow)}

## Decision Points

{bullets(decisions)}

## Outputs

{bullets(outputs)}

## Deliverables

{bullets(deliverables)}

## Escalation

{bullets(escalation)}

## Related Documents

- [SKILL.md](../SKILL.md)
- [playbooks/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| {VERSION} | {DATE} | QE Practice Lead | Initial playbook |
"""


def template_doc(title: str, sections: list[str]) -> str:
    body = "\n\n".join(f"## {s}\n\n_TBD — complete during analysis._" for s in sections)
    return fm(title, "Specialized Skill Template", "Template", ["metadata-impact-analyzer", "template"]) + f"""# {title}

**Purpose:** Reusable deliverable shell for Metadata Impact Analyzer outputs.

**Usage:** Copy into `outputs/<project>/` and complete all sections. Run `python output-engine/convert.py --file <path>` after authoring.

---

{body}

## Assumptions

- _List assumptions with IDs (A1, A2, …)._

## Open Questions

- _List unresolved items requiring architect or release manager confirmation._

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| {VERSION} | {DATE} | QE Practice Lead | Initial template |
"""


def prompt_doc(title: str, user_prompt: str, required_sections: list[str]) -> str:
    secs = "\n".join(f"{i}. {s}" for i, s in enumerate(required_sections, 1))
    return fm(title, "Specialized Skill Prompt", "Prompt", ["metadata-impact-analyzer", "prompt"]) + f"""# {title}

## Purpose

Reusable prompt for structured Metadata Impact Analyzer output.

## Prompt

```
{user_prompt}
```

## Required Output Sections

{secs}

## Quality Gate

- Dependency analysis MUST appear before test recommendations.
- All sections labeled; assumptions explicit.
- No invented coverage %, SLA, or certification levels.

## Related Documents

- [SKILL.md](../SKILL.md)
- [../templates/metadata-impact-report.md](../templates/metadata-impact-report.md)
"""


def example_doc(
    title: str,
    change: str,
    input_desc: str,
    analysis: list[str],
    regression: list[str],
    risk: str,
    soql: list[str],
) -> str:
    return fm(title, "Specialized Skill Example", "Example", ["metadata-impact-analyzer", "example"]) + f"""# {title}

## Input

**Change:** {change}

{input_desc}

## Expected Analysis (Dependency First)

{chr(10).join(f"- {a}" for a in analysis)}

## Expected Regression

| Scope | Rationale |
|-------|-----------|
{chr(10).join(f"| {r.split(' — ')[0] if ' — ' in r else r} | {r.split(' — ')[1] if ' — ' in r else 'See analysis'} |" for r in regression)}

## Expected Risk

**Rating:** {risk}

## Expected SOQL Validations

{chr(10).join(f"```sql{chr(10)}{q}{chr(10)}```" for q in soql)}

## Related Documents

- [SKILL.md](../SKILL.md)
- [examples/README.md](README.md)
"""


OUTPUT_SECTIONS = [
    "Executive Summary",
    "Metadata Changed",
    "Dependency Analysis",
    "Business Impact",
    "Technical Impact",
    "Security Impact",
    "Integration Impact",
    "Automation Impact",
    "Reporting Impact",
    "Regression Scope",
    "Deployment Risk",
    "Risk Rating",
    "Automation Candidates",
    "Recommended SOQL Validations",
    "Recommended Manual Tests",
    "Go / No-Go Recommendation",
]


def main() -> None:
    print("Generating Metadata Impact Analyzer skill pack...")
    SKILL.mkdir(parents=True, exist_ok=True)

    # skill-config.yaml
    write(
        "skill-config.yaml",
        f"""# Metadata Impact Analyzer — skill configuration
name: metadata-impact-analyzer
version: {VERSION}
parent_module: salesforce-quality-engineering
entry: SKILL.md

routing:
  keywords:
    - metadata
    - deployment
    - deploy
    - package.xml
    - change set
    - changeset
    - dependency
    - dependency analysis
    - impact analysis
    - metadata impact
    - regression impact
    - deployment review
    - field
    - object
    - flow
    - validation rule
    - page layout
    - record type
    - profile
    - permission set
    - permission set group
    - apex
    - trigger
    - lightning
    - lwc
    - aura
    - omnistudio
    - integration
    - named credential
    - connected app
    - platform event
    - change data capture
    - sharing rule
    - approval process
    - compact layout
    - flexipage
    - queue
    - custom metadata type
  primary_support:
    - knowledge/metadata/
    - knowledge/platform/
    - knowledge/automation/
    - knowledge/security/
    - knowledge/integration/
  downstream_after_analysis:
  - knowledge/test-design-engine.md
  - playbooks/regression-planning.md

output_schema:
  sections:
{chr(10).join(f"    - id: {s.lower().replace(' ', '_').replace('/', '_')}" + chr(10) + f"      title: \"{s}\"" for s in OUTPUT_SECTIONS)}

risk_rating:
  scale: [Low, Medium, High, Critical]
  rules:
    - Require evidence paths for every rating
    - Never invent numeric probability or coverage percentages
    - Escalate Critical to Release Manager and Solution Architect

quality_gates:
  - dependency_analysis_before_tests
  - all_sixteen_sections_present
  - assumptions_labeled
  - cross_links_to_sprint_4a_when_deep_dive_needed

escalation:
  - signal: security_model_change
    to: Security Architect
  - signal: integration_breaking_change
    to: Integration Architect
  - signal: production_deploy_high_risk
    to: Release Manager
  - signal: data_model_breaking_change
    to: Solution Architect
""",
    )

    # Knowledge articles
    knowledge_specs = [
        (
            "Salesforce Metadata Components",
            "salesforce-metadata-components.md",
            "Map changed metadata types to dependency surfaces and impact categories for QE analysis.",
            [
                "Identify metadata type from change manifest (package.xml, change set, or diff).",
                "Classify as data model, UI, automation, security, integration, or analytics.",
                "Load type-specific dependency rules from cross-linked Sprint 4A articles.",
                "Enumerate upstream producers and downstream consumers before impact statements.",
            ],
            [
                ("Metadata Types", "../../knowledge/metadata/metadata-types.md"),
                ("Metadata Overview", "../../knowledge/metadata/metadata-overview.md"),
                ("Metadata Dependencies", "../../knowledge/metadata/metadata-dependencies.md"),
            ],
            [
                "Never skip type classification — unknown type → mark Partial and request manifest detail.",
                "Treat packaged metadata separately from unpackaged (managed package constraints).",
                "Custom Metadata Types affect runtime config — trace Apex/LWC/Flow readers.",
            ],
        ),
        (
            "Object Relationships",
            "object-relationships.md",
            "Trace lookup, master-detail, junction, and polymorphic relationships affected by object/field changes.",
            [
                "List parent and child objects for each changed field or object.",
                "Identify roll-up summary fields, required lookups, and delete constraints.",
                "Check sharing inheritance on master-detail relationships.",
                "Map related list and report dependencies on relationship fields.",
            ],
            [
                ("Metadata Relationships", "../../knowledge/metadata/metadata-relationships.md"),
                ("Platform Knowledge", "../../knowledge/platform/README.md"),
                ("Record Types", "../../knowledge/platform/record-types.md"),
            ],
            [
                "Master-detail change → mandatory sharing and roll-up impact review.",
                "New required lookup → validate existing records and integration payloads.",
            ],
        ),
        (
            "Flow Dependencies",
            "flow-dependencies.md",
            "Analyze Record-Triggered, Scheduled, Screen, and Autolaunched Flow impacts and execution order.",
            [
                "Identify changed Flow elements: entry criteria, decisions, DML, subflows, Apex actions.",
                "Map referenced objects, fields, formulas, and invocable Apex.",
                "Check active vs inactive versions and deployment activation plan.",
                "Compare order of execution with triggers and validation rules on same object.",
            ],
            [
                ("Automation Knowledge", "../../knowledge/automation/README.md"),
                ("Metadata Dependencies", "../../knowledge/metadata/metadata-dependencies.md"),
            ],
            [
                "Record-triggered Flow on same object as trigger → flag order-of-execution risk.",
                "Subflow or invocable Apex change → trace all parent Flows.",
            ],
        ),
        (
            "Validation Rule Impact",
            "validation-rule-impact.md",
            "Assess validation rule changes on save paths, API integrations, and bulk operations.",
            [
                "Capture formula fields and error conditions referenced by the rule.",
                "Identify UI-only vs API save paths affected.",
                "Check bypass patterns (custom settings, hierarchy custom settings) if documented.",
                "Map integrations that create/update records subject to the rule.",
            ],
            [
                ("Validation Rule Testing", "../../knowledge/validation-rule-testing.md"),
                ("Metadata Impact Analysis", "../../knowledge/metadata/metadata-impact-analysis.md"),
            ],
            [
                "New blocking rule on integrated object → High integration risk until backfill validated.",
                "Rule formula referencing undeployed field → deployment ordering risk.",
            ],
        ),
        (
            "Apex Dependencies",
            "apex-dependencies.md",
            "Trace Apex class and trigger dependencies across automation, integrations, and tests.",
            [
                "List SOQL/DML targets and shared service classes.",
                "Identify trigger handler frameworks and recursion guards.",
                "Map @AuraEnabled, @InvocableMethod, REST, and Batch entry points.",
                "Check test class coverage dependencies (advisory — not coverage % invention).",
            ],
            [
                ("Platform Apex", "../../knowledge/platform/apex.md"),
                ("Automation Knowledge", "../../knowledge/automation/README.md"),
            ],
            [
                "Trigger logic change → regression on all bulk and single-record paths.",
                "Shared utility class change → enumerate all callers before scoping regression.",
            ],
        ),
        (
            "Permission Model",
            "permission-model.md",
            "Evaluate CRUD, FLS, and permission set assignments affected by metadata changes.",
            [
                "Map changed objects/fields/tabs/apps to permission requirements.",
                "Identify persona-specific access deltas.",
                "Check permission set group assignments and muting permission sets.",
                "Validate Experience Cloud and guest user profiles separately.",
            ],
            [
                ("Security Knowledge", "../../knowledge/security/README.md"),
                ("Permission Set Testing", "../../knowledge/permission-set-testing.md"),
                ("Sharing Security Testing", "../../knowledge/sharing-security-testing.md"),
            ],
            [
                "FLS change → mandatory negative test per affected persona.",
                "Profile change in production → treat as High security risk.",
            ],
        ),
        (
            "Profile vs Permission Set",
            "profile-vs-permission-set.md",
            "Apply least-privilege analysis when profiles or permission sets change.",
            [
                "Prefer permission set delta analysis over full profile rewrites.",
                "Document which permissions moved between profile and permission set.",
                "Identify users affected via PermissionSetAssignment queries.",
                "Flag View All / Modify All / Author Apex as exceptional permissions.",
            ],
            [
                ("Security Knowledge", "../../knowledge/security/README.md"),
                ("Permission Set Testing", "../../knowledge/permission-set-testing.md"),
            ],
            [
                "Profile narrowing → verify no business process breakage for standard users.",
                "Permission set expansion → security review required before deploy.",
            ],
        ),
        (
            "Sharing Model",
            "sharing-model.md",
            "Analyze sharing rules, OWD, role hierarchy, and manual sharing impacts.",
            [
                "Identify OWD and sharing rule changes on affected objects.",
                "Map role hierarchy and public group membership dependencies.",
                "Check Apex sharing (with sharing / without sharing) on changed classes.",
                "Validate report and dashboard visibility for restricted records.",
            ],
            [
                ("Sharing Security Testing", "../../knowledge/sharing-security-testing.md"),
                ("Security Knowledge", "../../knowledge/security/README.md"),
            ],
            [
                "OWD tightening → validate integration service account access.",
                "New sharing rule → regression on record visibility per persona.",
            ],
        ),
        (
            "Reporting Dependencies",
            "reporting-dependencies.md",
            "Identify reports, dashboards, and analytics dependencies on changed fields and objects.",
            [
                "Search report types, fields, filters, and bucket fields referencing changed metadata.",
                "Map dashboard components and dynamic dashboards.",
                "Check Einstein / CRM Analytics dependencies if in scope.",
                "Flag historical trending and snapshot fields.",
            ],
            [
                ("Reporting Knowledge", "../../knowledge/reporting/README.md"),
                ("Metadata Dependencies", "../../knowledge/metadata/metadata-dependencies.md"),
            ],
            [
                "Field type change → all dependent reports may break (High reporting risk).",
                "Deleted field → run report inventory before deploy.",
            ],
        ),
        (
            "Deployment Best Practices",
            "deployment-best-practices.md",
            "Apply QE deployment validation patterns before production promotion.",
            [
                "Validate deployment manifest completeness vs dependency graph.",
                "Confirm test execution evidence in target sandbox.",
                "Check deployment window, rollback plan, and post-deploy smoke scope.",
                "Align with release train and change advisory board requirements.",
            ],
            [
                ("Deployment Considerations", "../../knowledge/metadata/deployment-considerations.md"),
                ("Release Readiness", "../../knowledge/release/release-readiness.md"),
                ("Metadata Validation", "../../knowledge/metadata/metadata-validation.md"),
            ],
            [
                "Missing dependency in package → Fail deployment readiness.",
                "No rollback story for data model change → No-Go until documented.",
            ],
        ),
        (
            "Metadata API",
            "metadata-api.md",
            "Use Metadata API concepts to evidence dependency and deployment impact (QE lens — no live calls required).",
            [
                "Interpret package.xml members and destructive changes.",
                "Understand deploy/test/validate-only modes for readiness gates.",
                "Map component types to regression surfaces.",
            ],
            [
                ("Metadata Overview", "../../knowledge/metadata/metadata-overview.md"),
                ("Deployment Considerations", "../../knowledge/metadata/deployment-considerations.md"),
            ],
            [
                "DestructiveChanges.xml present → mandatory rollback and data backup review.",
            ],
        ),
        (
            "Tooling API",
            "tooling-api.md",
            "Use Tooling API concepts for dependency discovery evidence (QE advisory — no credentials in skill).",
            [
                "Reference Dependency API / MetadataComponentDependency patterns for impact evidence.",
                "Identify Flow, Apex, and ValidationRule dependency queries for SOQL validation section.",
                "Document when human architect must run live queries in org.",
            ],
            [
                ("Metadata Dependencies", "../../knowledge/metadata/metadata-dependencies.md"),
                ("Platform Knowledge", "../../knowledge/platform/README.md"),
            ],
            [
                "If dependency graph not supplied → state assumption and recommend Tooling query pack.",
            ],
        ),
        (
            "Release Management",
            "release-management.md",
            "Connect metadata impact analysis to release gates and Go/No-Go decisions.",
            [
                "Synthesize impact report into release readiness checklist.",
                "Align regression scope with release calendar and environment path.",
                "Escalate Critical risks to Release Manager with evidence pack.",
            ],
            [
                ("Release Knowledge", "../../knowledge/release/README.md"),
                ("Production Support Go-Live", "../../production-support/go-live/README.md"),
                ("Regression Impact Analysis", "../../knowledge/metadata/regression-impact-analysis.md"),
            ],
            [
                "Critical risk without mitigation → No-Go recommendation.",
                "Conditional Go only with documented residual risk acceptance.",
            ],
        ),
    ]

    for title, slug, purpose, reasoning, links, rules in knowledge_specs:
        write(f"knowledge/{slug}", knowledge_article(title, slug, purpose, reasoning, links, rules))

    write(
        "knowledge/README.md",
        fm("Metadata Impact Analyzer — Knowledge", "Specialized Skill Knowledge", "Guide", ["metadata-impact-analyzer", "knowledge-index"])
        + """# Metadata Impact Analyzer — Knowledge

## Purpose

Skill-specific reasoning articles for metadata dependency and deployment impact analysis.

## Canonical Depth

Full Sprint 4A encyclopedia remains in [`../../knowledge/metadata/`](../../knowledge/metadata/README.md). These articles provide **reasoning models and decision rules** — not duplicate reference content.

## Available Documents

| Document | Focus |
|----------|-------|
| [Salesforce Metadata Components](salesforce-metadata-components.md) | Type classification and impact surfaces |
| [Object Relationships](object-relationships.md) | Lookup, MD, junction impacts |
| [Flow Dependencies](flow-dependencies.md) | Flow version and execution order |
| [Validation Rule Impact](validation-rule-impact.md) | Save path and integration blocking |
| [Apex Dependencies](apex-dependencies.md) | Class, trigger, API entry points |
| [Permission Model](permission-model.md) | CRUD/FLS and persona deltas |
| [Profile vs Permission Set](profile-vs-permission-set.md) | Least-privilege change analysis |
| [Sharing Model](sharing-model.md) | OWD, rules, hierarchy |
| [Reporting Dependencies](reporting-dependencies.md) | Reports and dashboards |
| [Deployment Best Practices](deployment-best-practices.md) | QE deploy gates |
| [Metadata API](metadata-api.md) | Manifest and deploy modes |
| [Tooling API](tooling-api.md) | Dependency evidence patterns |
| [Release Management](release-management.md) | Go/No-Go alignment |

## Navigation

- **Up:** [../SKILL.md](../SKILL.md)
- **See Also:** [../../knowledge/metadata/README.md](../../knowledge/metadata/README.md)
""",
    )

    # Playbooks
    playbooks = [
        (
            "Metadata Impact Analysis",
            "metadata-impact-analysis.md",
            "Execute end-to-end metadata dependency and impact analysis before test design.",
            ["Change manifest or diff", "Target environment context", "Persona list", "Release window"],
            [
                "Load SKILL.md and classify metadata types.",
                "Build dependency graph (objects → fields → automation → security → integration → reporting).",
                "Produce 16-section impact report using template.",
                "Derive regression scope In/Out/Conditional.",
                "Issue Go/No-Go with evidence.",
            ],
            ["Is dependency graph complete?", "Any Critical security or integration risk?", "Destructive change present?"],
            ["Metadata Impact Report", "Risk rating", "SOQL validation pack"],
            ["metadata-impact-report.md", "regression-report.md"],
            ["Critical risk → Solution Architect", "Security model change → Security Architect"],
        ),
        (
            "Deployment Review",
            "deployment-review.md",
            "Review deployment package readiness from QE and release perspectives.",
            ["package.xml or change set list", "Prior sandbox test evidence", "Rollback plan"],
            [
                "Validate manifest vs dependency graph.",
                "Check deployment ordering (fields before VR, etc.).",
                "Confirm smoke and regression evidence.",
                "Produce Deployment Risk Report.",
            ],
            ["Missing dependencies?", "Destructive changes?", "Test evidence sufficient?"],
            ["Deployment Risk Report", "Residual risk list"],
            ["deployment-risk-report.md"],
            ["High deployment risk → Release Manager hold"],
        ),
        (
            "Regression Planning",
            "regression-planning.md",
            "Translate metadata impact into risk-based regression scope for the specialized skill context.",
            ["Completed Metadata Impact Report", "Release timeline", "Automation estate overview"],
            [
                "Extract impacted components from dependency analysis.",
                "Classify scenarios In / Out / Conditional.",
                "Prioritize by risk rating and business criticality.",
                "Identify automation candidates (design only).",
            ],
            ["Can any High area be Out of scope?", "Automation vs manual balance?"],
            ["Regression Report", "Automation candidate list"],
            ["regression-report.md"],
            ["Scope dispute → Test Lead + Release Manager"],
            "[../../playbooks/regression-planning.md](../../playbooks/regression-planning.md)",
        ),
        (
            "Risk Assessment",
            "risk-assessment.md",
            "Score and document deployment and regression risks with evidence.",
            ["Impact report", "Historical defect data (if available)", "Environment path"],
            [
                "Rate Business, Technical, Security, Integration, Automation, Reporting dimensions.",
                "Roll up to overall Risk Rating (Low/Medium/High/Critical).",
                "Document mitigations and residual risk.",
            ],
            ["Acceptable residual risk?", "Mitigation owner assigned?"],
            ["Risk matrix", "Escalation triggers"],
            ["deployment-risk-report.md"],
            ["Critical → steering / CAB escalation"],
        ),
        (
            "Release Readiness",
            "release-readiness.md",
            "Assemble metadata-impact evidence into release readiness and Go-Live gates.",
            ["Impact report", "Regression evidence", "Deployment risk report", "Open defects"],
            [
                "Complete Release Readiness Checklist.",
                "Confirm Go/No-Go recommendation alignment.",
                "Hand off to production validation playbook if Go.",
            ],
            ["All Critical risks mitigated?", "Rollback tested?"],
            ["Release Readiness Checklist", "Go/No-Go decision"],
            ["release-readiness-checklist.md", "go-live-checklist.md"],
            ["No-Go → Release Manager communicates hold"],
            "[../../knowledge/release/release-readiness.md](../../knowledge/release/release-readiness.md)",
        ),
    ]
    for title, slug, purpose, inputs, workflow, decisions, outputs, deliverables, escalation, *ptr in playbooks:
        pointer = ptr[0] if ptr else ""
        write(f"playbooks/{slug}", playbook(title, purpose, inputs, workflow, decisions, outputs, deliverables, escalation, pointer))

    write(
        "playbooks/README.md",
        fm("Metadata Impact Analyzer — Playbooks", "Specialized Skill Playbook", "Guide", ["metadata-impact-analyzer", "playbook-index"])
        + """# Metadata Impact Analyzer — Playbooks

| Playbook | Focus |
|----------|-------|
| [Metadata Impact Analysis](metadata-impact-analysis.md) | End-to-end impact workflow |
| [Deployment Review](deployment-review.md) | Package readiness |
| [Regression Planning](regression-planning.md) | In/Out/Conditional from impact |
| [Risk Assessment](risk-assessment.md) | Evidence-based risk rating |
| [Release Readiness](release-readiness.md) | Go/No-Go gates |
""",
    )

    # Templates
    templates = [
        ("Metadata Impact Report", "metadata-impact-report.md", OUTPUT_SECTIONS),
        (
            "Regression Report",
            "regression-report.md",
            ["Executive Summary", "Impact Summary", "In Scope", "Out of Scope", "Conditional", "Automation Candidates", "Owners", "Assumptions"],
        ),
        (
            "Deployment Risk Report",
            "deployment-risk-report.md",
            ["Executive Summary", "Deployment Package", "Dependency Gaps", "Ordering Risks", "Rollback Plan", "Risk Rating", "Mitigations", "Recommendation"],
        ),
        (
            "Release Readiness Checklist",
            "release-readiness-checklist.md",
            ["Metadata Evidence", "Regression Evidence", "Security Sign-off", "Integration Sign-off", "Open Defects", "Rollback Verified", "Go/No-Go"],
        ),
        (
            "Go-Live Checklist",
            "go-live-checklist.md",
            ["Pre-Deploy", "Deploy Window", "Post-Deploy Smoke", "Monitoring", "Hypercare Handoff", "Sign-off"],
        ),
        (
            "Architecture Review",
            "architecture-review.md",
            ["Change Summary", "Dependency Graph", "Design Concerns", "Security Review", "Integration Review", "Recommendations"],
        ),
        (
            "SOQL Validation Report",
            "soql-validation-report.md",
            ["Purpose", "Queries", "Expected Results", "Execution Notes", "Findings"],
        ),
    ]
    for title, slug, sections in templates:
        write(f"templates/{slug}", template_doc(title, sections))

    write(
        "templates/README.md",
        fm("Metadata Impact Analyzer — Templates", "Specialized Skill Template", "Guide", ["metadata-impact-analyzer", "template-index"])
        + """# Metadata Impact Analyzer — Templates

| Template | Use when |
|----------|----------|
| [Metadata Impact Report](metadata-impact-report.md) | Primary 16-section deliverable |
| [Regression Report](regression-report.md) | Regression scope from impact |
| [Deployment Risk Report](deployment-risk-report.md) | Deploy readiness review |
| [Release Readiness Checklist](release-readiness-checklist.md) | Release gate |
| [Go-Live Checklist](go-live-checklist.md) | Production cutover |
| [Architecture Review](architecture-review.md) | SA/TA review pack |
| [SOQL Validation Report](soql-validation-report.md) | Data and dependency queries |
""",
    )

    # Prompts
    base_prompt = (
        "Analyze the Salesforce metadata change below. Perform complete dependency analysis BEFORE any test recommendations. "
        "Produce all 16 sections: Executive Summary, Metadata Changed, Dependency Analysis, Business Impact, Technical Impact, "
        "Security Impact, Integration Impact, Automation Impact, Reporting Impact, Regression Scope, Deployment Risk, Risk Rating, "
        "Automation Candidates, Recommended SOQL Validations, Recommended Manual Tests, Go/No-Go Recommendation. "
        "Label assumptions. Do not invent coverage % or SLA values."
    )
    prompts = [
        ("Impact Analysis", "impact-analysis.md", base_prompt, OUTPUT_SECTIONS),
        (
            "Deployment Review",
            "deployment-review.md",
            base_prompt + " Focus on deployment package completeness, ordering, rollback, and deployment risk.",
            OUTPUT_SECTIONS,
        ),
        (
            "Regression Analysis",
            "regression-analysis.md",
            "Given the metadata impact analysis below, produce regression scope (In/Out/Conditional), automation candidates, and manual test priorities. Dependency analysis must be referenced.",
            ["Regression Scope", "Automation Candidates", "Recommended Manual Tests", "Assumptions"],
        ),
        (
            "Security Analysis",
            "security-analysis.md",
            "Analyze security impact of the metadata change: CRUD, FLS, sharing, profiles, permission sets, Experience Cloud. Produce Security Impact section plus SOQL validations for access.",
            ["Security Impact", "Recommended SOQL Validations", "Recommended Manual Tests", "Risk Rating"],
        ),
        (
            "Flow Review",
            "flow-review.md",
            "Review Flow metadata change: entry criteria, versions, subflows, Apex actions, order of execution. Dependency analysis first.",
            ["Dependency Analysis", "Automation Impact", "Regression Scope", "Risk Rating"],
        ),
        (
            "Validation Rule Review",
            "validation-rule-review.md",
            "Review Validation Rule change: formula dependencies, API save paths, bulk impact, integrations.",
            ["Dependency Analysis", "Technical Impact", "Integration Impact", "Recommended Manual Tests"],
        ),
        (
            "Object Review",
            "object-review.md",
            "Review object or field metadata change: relationships, layouts, record types, automation, reports.",
            ["Dependency Analysis", "Business Impact", "Reporting Impact", "Regression Scope"],
        ),
        (
            "Permission Review",
            "permission-review.md",
            "Review profile or permission set change: personas affected, least privilege, negative paths.",
            ["Security Impact", "Recommended SOQL Validations", "Recommended Manual Tests", "Go / No-Go Recommendation"],
        ),
    ]
    for title, slug, prompt, sections in prompts:
        write(f"prompts/{slug}", prompt_doc(title, prompt, sections))

    write(
        "prompts/README.md",
        fm("Metadata Impact Analyzer — Prompts", "Specialized Skill Prompt", "Guide", ["metadata-impact-analyzer", "prompt-index"])
        + """# Metadata Impact Analyzer — Prompts

Copy prompts into Cursor Agent mode with your change manifest attached.

| Prompt | Focus |
|--------|-------|
| [Impact Analysis](impact-analysis.md) | Full 16-section report |
| [Deployment Review](deployment-review.md) | Deploy readiness |
| [Regression Analysis](regression-analysis.md) | Scope from impact |
| [Security Analysis](security-analysis.md) | CRUD/FLS/sharing |
| [Flow Review](flow-review.md) | Flow dependencies |
| [Validation Rule Review](validation-rule-review.md) | VR and integrations |
| [Object Review](object-review.md) | Object/field changes |
| [Permission Review](permission-review.md) | Profile/perm set |
""",
    )

    # Examples
    examples = [
        (
            "Custom Field Added",
            "custom-field-added.md",
            "New custom picklist field `Account.Service_Tier__c` on Account; added to Account page layout and one Record-Triggered Flow entry criteria.",
            "Package adds `Account.Service_Tier__c` (Picklist). Layout: Account-Enterprise Layout. Flow: `Account_Tier_Routing` (Record-Triggered, Update).",
            [
                "Field referenced by Flow entry criteria — Flow must deploy after field.",
                "Layout section change affects Enterprise persona UI only if layout assignment unchanged.",
                "Reports using Account fields may need new column — scan report dependencies.",
            ],
            [
                "In — Account create/update with each picklist value",
                "In — Flow routing when Service_Tier changes",
                "Conditional — Report exports if finance reports use Account",
            ],
            "Medium",
            [
                "SELECT Id, Service_Tier__c FROM Account WHERE Service_Tier__c != null LIMIT 10",
                "SELECT Id, MasterLabel, Status FROM Flow WHERE Definition.DeveloperName = 'Account_Tier_Routing'",
            ],
        ),
        (
            "Validation Rule Changed",
            "validation-rule-changed.md",
            "Validation rule `Case_Closure_Check` on Case updated to require `Resolution_Code__c` when Status = Closed.",
            "VR formula now references `Resolution_Code__c`. Integration `CaseSync` updates Case status via REST.",
            [
                "VR blocks API close without Resolution_Code — integration payloads must include field.",
                "UI agents see new error on save — training impact.",
                "Order: field must exist before VR deploy.",
            ],
            [
                "In — UI close with/without Resolution_Code",
                "In — API CaseSync close payloads",
                "In — Bulk close data loader scenarios",
            ],
            "High",
            [
                "SELECT Id, Status, Resolution_Code__c FROM Case WHERE Status = 'Closed' AND Resolution_Code__c = null LIMIT 50",
            ],
        ),
        (
            "Flow Modified",
            "flow-modified.md",
            "Record-Triggered Flow `Opportunity_Auto_Approve` modified: new decision branch calls Apex `ApprovalService`.",
            "Flow version 3 adds Apex action. Class `ApprovalService` already in org. Subflow `Notify_Sales_Manager` referenced.",
            [
                "Apex action adds governor and exception surface.",
                "Subflow dependency — both must be active.",
                "Trigger on Opportunity may interact — check order of execution.",
            ],
            [
                "In — Opportunity amounts triggering each branch",
                "In — Apex fault path",
                "Conditional — Email alert recipients if subflow changes",
            ],
            "High",
            [
                "SELECT Id, VersionNumber, Status FROM Flow WHERE Definition.DeveloperName = 'Opportunity_Auto_Approve'",
            ],
        ),
        (
            "Permission Set Updated",
            "permission-set-updated.md",
            "Permission set `FSL_Dispatcher` granted Edit on `WorkOrder` and FLS Edit on `WorkOrder.Priority__c`.",
            "Permission set assigned to 120 users via Permission Set Group `Field_Service_Ops`.",
            [
                "FLS expansion — verify dispatcher personas only.",
                "WorkOrder sharing still applies — Edit CRUD does not bypass sharing.",
                "Mobile FSL app may cache permissions — retest mobile.",
            ],
            [
                "In — Dispatcher edit WorkOrder priority",
                "In — Technician without perm set cannot edit",
                "In — PSG assignment smoke for sample users",
            ],
            "Medium",
            [
                "SELECT AssigneeId, PermissionSet.Name FROM PermissionSetAssignment WHERE PermissionSet.Name = 'FSL_Dispatcher'",
            ],
        ),
        (
            "Profile Updated",
            "profile-updated.md",
            "Standard profile `Customer Community User` tab visibility changed; Object CRUD on `Case` reduced from Edit to Read.",
            "Experience Cloud site `Support Portal` uses this profile.",
            [
                "Community users lose Case edit — self-service flows may break.",
                "LWC components checking edit access need review.",
                "High visibility / reputational risk if portal breaks at deploy.",
            ],
            [
                "In — Portal user Case create/update paths",
                "In — Negative: edit denied with clear message",
                "Out — Internal agent Case edit (unaffected profile)",
            ],
            "Critical",
            [
                "SELECT Id, SobjectType, PermissionsEdit FROM ObjectPermissions WHERE Parent.Profile.Name = 'Customer Community User' AND SobjectType = 'Case'",
            ],
        ),
        (
            "Record Type Added",
            "record-type-added.md",
            "New Record Type `Enterprise_Account` on Account with dedicated page layout and picklist values.",
            "Assigned to Enterprise Sales profile. Existing automation keyed on RecordTypeId.",
            [
                "Picklist value sets may be record-type specific.",
                "Layouts and compact layouts per record type.",
                "Flows filtering RecordType developer name need regression.",
            ],
            [
                "In — Create Account with new record type",
                "In — Picklist values visible per record type",
                "Conditional — Automation branches on RecordType",
            ],
            "Medium",
            [
                "SELECT Id, DeveloperName, SobjectType FROM RecordType WHERE DeveloperName = 'Enterprise_Account'",
            ],
        ),
        (
            "Custom Object Added",
            "custom-object-added.md",
            "New custom object `Service_Contract__c` with master-detail to Account, two validation rules, and tab.",
            "Sharing controlled by parent Account. Integration will sync contracts nightly.",
            [
                "MD relationship drives sharing and delete behavior.",
                "New tab and app visibility via profiles/perm sets.",
                "Integration must respect VR and required fields.",
            ],
            [
                "In — CRUD and sharing via Account parent",
                "In — VR on create/update",
                "In — Integration upsert payload",
            ],
            "High",
            [
                "SELECT Id, Account__c FROM Service_Contract__c LIMIT 10",
            ],
        ),
        (
            "LWC Updated",
            "lwc-updated.md",
            "LWC `accountHealthScore` updated to call Apex `HealthScoreController` with new `@AuraEnabled` method.",
            "Component on Account Lightning record page. Guest users not in scope.",
            [
                "Apex API change — controller method signature.",
                "FLS enforced in Apex with sharing.",
                "Jest tests advisory; manual on record page required.",
            ],
            [
                "In — Component load and score display",
                "In — Error handling when Apex throws",
                "Conditional — Performance on list views if embedded elsewhere",
            ],
            "Medium",
            [
                "SELECT Id, Name FROM Account WHERE Id IN (SELECT ParentId FROM AccountContactRelation LIMIT 1)",
            ],
        ),
        (
            "Platform Event Added",
            "platform-event-added.md",
            "New Platform Event `Order_Shipped__e` published from Flow; external subscriber via Event Relay.",
            "Flow `Fulfillment_Complete` publishes event. MuleSoft subscriber in lower env only.",
            [
                "Publish/subscribe contract versioning.",
                "Event fields must match subscriber schema.",
                "High volume — governor and replay ID considerations.",
            ],
            [
                "In — Flow publishes event on fulfillment",
                "Conditional — Subscriber receipt in integrated env",
                "Out — Unrelated order flows",
            ],
            "High",
            [
                "SELECT Id, ReplayId, CreatedDate FROM Order_Shipped__e ORDER BY CreatedDate DESC LIMIT 5",
            ],
        ),
        (
            "Integration Modified",
            "integration-modified.md",
            "Named Credential `ERP_Sync` endpoint URL changed; Connected App callback updated for OAuth.",
            "Apex class `ErpSyncBatch` uses Named Credential. Experience Cloud login uses Connected App.",
            [
                "URL change affects all callouts using NC.",
                "OAuth callback mismatch breaks login.",
                "Certificate rotation may be required — confirm with integration team.",
            ],
            [
                "In — ErpSyncBatch successful callout",
                "In — OAuth login to Experience Cloud",
                "In — Negative: invalid credential handling",
            ],
            "Critical",
            [
                "SELECT Id, DeveloperName, Endpoint FROM NamedCredential WHERE DeveloperName = 'ERP_Sync'",
            ],
        ),
    ]
    for title, slug, change, input_desc, analysis, regression, risk, soql in examples:
        write(f"examples/{slug}", example_doc(title, change, input_desc, analysis, regression, risk, soql))

    write(
        "examples/README.md",
        fm("Metadata Impact Analyzer — Examples", "Specialized Skill Example", "Guide", ["metadata-impact-analyzer", "example-index"])
        + """# Metadata Impact Analyzer — Examples

| Example | Change type |
|---------|-------------|
| [Custom Field Added](custom-field-added.md) | Field + layout + Flow |
| [Validation Rule Changed](validation-rule-changed.md) | VR + integration |
| [Flow Modified](flow-modified.md) | Flow + Apex |
| [Permission Set Updated](permission-set-updated.md) | Perm set + FLS |
| [Profile Updated](profile-updated.md) | Community profile |
| [Record Type Added](record-type-added.md) | Record type + layout |
| [Custom Object Added](custom-object-added.md) | New object + MD |
| [LWC Updated](lwc-updated.md) | LWC + Apex |
| [Platform Event Added](platform-event-added.md) | Event + subscriber |
| [Integration Modified](integration-modified.md) | NC + Connected App |
""",
    )

    # Tests
    test_scenarios = [
        ("dependency-before-tests", "Output places Dependency Analysis before Recommended Manual Tests"),
        ("sixteen-sections", "All 16 output sections present and labeled"),
        ("risk-evidence", "Risk Rating includes evidence paths not invented percentages"),
        ("custom-field", "Custom field example traces Flow and layout dependencies"),
        ("security-profile", "Profile change flags Critical security and portal impact"),
        ("integration-vr", "Validation rule change flags API integration blocking"),
    ]
    for slug, desc in test_scenarios:
        write(
            f"tests/scenario-{slug}.md",
            fm(f"Test Scenario — {slug}", "Specialized Skill Test", "Test Scenario", ["metadata-impact-analyzer", "test"])
            + f"""# Test Scenario — {slug}

## Objective

{desc}

## Preconditions

- Metadata Impact Analyzer SKILL.md loaded
- Example or user-supplied change manifest available

## Steps

1. Run Impact Analysis prompt with fixture input.
2. Verify section order and content rules.
3. Record Pass / Partial / Fail with evidence.

## Pass Criteria

- Dependency analysis precedes test recommendations
- Assumptions explicitly labeled
- Risk rating justified

## Fail Criteria

- Test cases appear before dependency analysis
- Missing required sections
- Invented SLA or coverage %
""",
        )

    write(
        "tests/README.md",
        fm("Metadata Impact Analyzer — Tests", "Specialized Skill Test", "Guide", ["metadata-impact-analyzer", "test-index"])
        + """# Metadata Impact Analyzer — Validation Tests

## Purpose

Manual and agent regression scenarios verifying structured output and analysis discipline.

## How to Run

1. Load [../SKILL.md](../SKILL.md) and [../prompts/impact-analysis.md](../prompts/impact-analysis.md).
2. Execute each `scenario-*.md` with matching [../examples/](../examples/README.md) fixture.
3. Record Pass/Partial/Fail in a test log under `outputs/<project>/`.

## Scenarios

| Scenario | Focus |
|----------|-------|
| [dependency-before-tests](scenario-dependency-before-tests.md) | Section ordering |
| [sixteen-sections](scenario-sixteen-sections.md) | Completeness |
| [risk-evidence](scenario-risk-evidence.md) | Risk discipline |
| [custom-field](scenario-custom-field.md) | Field dependencies |
| [security-profile](scenario-security-profile.md) | Profile risk |
| [integration-vr](scenario-integration-vr.md) | VR + API |
""",
    )

    print("Done.")


if __name__ == "__main__":
    main()
