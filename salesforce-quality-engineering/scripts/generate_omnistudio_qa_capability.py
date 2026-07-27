"""Generate Salesforce OmniStudio QA (OSQA) skill pack."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAP = ROOT / "skills" / "omnistudio-qa"
VERSION = "0.22.0"
DATE = "2026-07-27"

OUTPUT_SECTIONS = [
    "Executive Summary",
    "Business Scenario",
    "OmniStudio Components Reviewed",
    "Architecture Assessment",
    "Functional Validation",
    "Data Validation",
    "JSON Validation",
    "Integration Validation",
    "Security Assessment",
    "Performance Assessment",
    "Negative Test Scenarios",
    "Edge Case Testing",
    "Regression Scope",
    "Automation Opportunities",
    "Deployment Readiness",
    "Risks",
    "Recommendations",
]


def fm(title: str, category: str, doc_type: str, tags: list[str]) -> str:
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
tags: [{", ".join(tags)}]
---

"""


def write(rel: str, content: str) -> None:
    path = CAP / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  wrote {rel}")


def knowledge_article(title, slug, purpose, reasoning, cross_links, rules):
    links = "\n".join(f"- [{n}]({p})" for n, p in cross_links)
    return fm(title, "QE Specialized Skill Knowledge", "Knowledge Article", ["omnistudio-qa", "knowledge"]) + f"""# {title}

## Purpose

{purpose}

## Reasoning Model

{chr(10).join(f"{i}. {r}" for i, r in enumerate(reasoning, 1))}

## Decision Rules

{chr(10).join(f"- {r}" for r in rules)}

## Cross-Links (Canonical Depth)

{links}

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| {VERSION} | {DATE} | QE Practice Lead | Initial capability knowledge |
"""


def playbook(title, slug, objective, inputs, workflow, decisions, deliverables, expected, escalation, pointer=""):
    ptr = f"\n\n**Pointer:** {pointer}" if pointer else ""
    b = lambda xs: "\n".join(f"- {x}" for x in xs)
    return fm(title, "QE Specialized Skill Playbook", "Playbook", ["omnistudio-qa", "playbook"]) + f"""# {title}

## Objective

{objective}{ptr}

## Inputs

{b(inputs)}

## Validation Workflow

{b(workflow)}

## Decision Points

{b(decisions)}

## Deliverables

{b(deliverables)}

## Expected Results

{b(expected)}

## Escalation Rules

{b(escalation)}
"""


def template_doc(title, sections):
    body = "\n\n".join(f"## {s}\n\n_Complete during analysis._" for s in sections)
    return fm(title, "QE Specialized Skill Template", "Template", ["omnistudio-qa", "template"]) + f"""# {title}

{body}

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| {VERSION} | {DATE} | QE Practice Lead | Initial template |
"""


def prompt_doc(title, prompt, sections):
    return fm(title, "QE Specialized Skill Prompt", "Prompt", ["omnistudio-qa", "prompt"]) + f"""# {title}

## Prompt

```
{prompt}
```

## Required Output Sections

{chr(10).join(f"{i}. {s}" for i, s in enumerate(sections, 1))}

## Quality Gate

- Business Scenario + OmniStudio Components Reviewed BEFORE detailed test cases.
- Label assumptions; do not invent latency/throughput or SLA percentages.
- Chain MIA / SOVA / PTA / PWR / AFT / TDG when applicable.
"""


def example_doc(title, scenario, components, objectives, scenarios, backend, expected, negatives, qa):
    return fm(title, "QE Specialized Skill Example", "Example", ["omnistudio-qa", "example"]) + f"""# {title}

## Business Scenario

{scenario}

## OmniStudio Components

{components}

## Test Objectives

{objectives}

## Test Scenarios

{scenarios}

## Backend Validation

{backend}

## Expected Results

{expected}

## Negative Scenarios

{negatives}

## QA Recommendations

{qa}
"""


def test_doc(title, purpose, preconditions, steps, asserts, chains):
    return fm(title, "QE Specialized Skill Test", "Test Scenario", ["omnistudio-qa", "test"]) + f"""# {title}

## Purpose

{purpose}

## Preconditions

{chr(10).join(f"- {p}" for p in preconditions)}

## Steps

{chr(10).join(f"{i}. {s}" for i, s in enumerate(steps, 1))}

## Assertions

{chr(10).join(f"- {a}" for a in asserts)}

## Capability Chains

{chr(10).join(f"- {c}" for c in chains)}

## Notes

- Inventory Business Scenario and OmniStudio Components before expanding detailed cases.
- Do not invent latency, throughput, or SLA percentages.
"""


def main() -> None:
    print("Generating OmniStudio QA skill pack...")
    CAP.mkdir(parents=True, exist_ok=True)

    cloud = "../../knowledge/clouds/omnistudio.md"
    mia = "../../skills/metadata-impact-analyzer/SKILL.md"
    sova = "../soql-validation-assistant/SKILL.md"
    pta = "../permission-testing-agent/SKILL.md"
    pwr = "../playwright-review/SKILL.md"
    aft = "../agentforce-testing/SKILL.md"
    tdg = "../test-data-generator/SKILL.md"
    auto = "../../automation-intelligence/salesforce/omnistudio.md"
    eq = "../../enterprise-quality/salesforce/omnistudio.md"

    knowledge_specs = [
        (
            "OmniStudio Architecture",
            "omnistudio-architecture.md",
            "Assess Industries journey architecture before component-level cases.",
            [
                "Map channel (LEX / Experience / Community) and journey purpose.",
                "Inventory OmniScript, FlexCard, DR, IP, and decision/calc dependencies.",
                "Identify shared reusable OmniScripts and versioning risks.",
                "Cross-link cloud encyclopedia — do not duplicate product overview.",
            ],
            [("OmniStudio Cloud Knowledge", cloud), ("Automation Advisory", auto), ("Enterprise Quality Advisory", eq)],
            ["No component inventory → incomplete Architecture Assessment.", "Reusable OS change without consumer map → High regression risk."],
        ),
        (
            "OmniScript Design",
            "omniscript-design.md",
            "Validate OmniScript navigation, conditionals, Data JSON, and submit paths.",
            [
                "Walk steps, conditional views, and required fields.",
                "Validate Save for Later / resume and error messaging.",
                "Inspect Data JSON shape at key transitions.",
                "Confirm submit/IP handoff and user feedback.",
            ],
            [("OmniStudio Cloud Knowledge", cloud), ("JSON Structure", "json-structure.md"), ("Playwright Review", pwr)],
            ["Step-click only without JSON/submit → Fail Functional Validation.", "Missing Save for Later when required → Edge gap."],
        ),
        (
            "FlexCard Architecture",
            "flexcard-architecture.md",
            "Assess FlexCard rendering, actions, binding, and child-card patterns.",
            [
                "Verify data source and refresh strategy.",
                "Validate action targets (OS, IP, navigation).",
                "Check conditional visibility and pagination.",
                "Flag heavy nested cards for performance risk (label assumptions).",
            ],
            [("OmniStudio Cloud Knowledge", cloud), ("Performance Best Practices", "performance-best-practices.md")],
            ["Action opens wrong OS version → Critical functional defect.", "PII on card without FLS check → Chain PTA."],
        ),
        (
            "DataRaptor Types",
            "dataraptor-types.md",
            "Validate Extract, Load, Transform, and Turbo Extract mapping accuracy.",
            [
                "Classify DR type and input/output contracts.",
                "Trace field mappings, formulas, and null handling.",
                "Pair Load paths with SOVA stubs for CRM proof.",
                "Note bulk/Turbo constraints and error paths.",
            ],
            [("OmniStudio Cloud Knowledge", cloud), ("SOQL Validation Assistant", sova), ("Test Data Generator", tdg)],
            ["Load without SOQL proof for critical CRM writes → Incomplete Data Validation.", "Silent null overwrite → High data risk."],
        ),
        (
            "Integration Procedures",
            "integration-procedures.md",
            "Validate IP orchestration: branches, cache, retry, remotes, SF operations.",
            [
                "Map step sequence and conditional branches.",
                "Validate response mapping into Data JSON / OS.",
                "Review cache keys and retry policy (document; do not invent SLAs).",
                "Confirm error handling and rollback expectations.",
            ],
            [("OmniStudio Cloud Knowledge", cloud), ("Remote Actions", "remote-actions.md"), ("Error Handling", "error-handling.md")],
            ["Happy-path-only IP tests → Fail Integration Validation.", "External HTTP without contract stub → Label TBC."],
        ),
        (
            "Decision Matrix",
            "decision-matrix.md",
            "Validate Decision Matrix inputs, outputs, and priority/default behavior.",
            [
                "Enumerate input dimensions and expected outputs.",
                "Cover priority conflicts and default rows.",
                "Test boundary values and missing inputs.",
                "Trace matrix usage from OS/IP callers.",
            ],
            [("Decision Tables", "decision-tables.md"), ("OmniStudio Cloud Knowledge", cloud)],
            ["No default/edge coverage → Incomplete Decision Logic.", "Matrix change without caller regression → High risk."],
        ),
        (
            "Decision Tables",
            "decision-tables.md",
            "Validate Decision Table rulesets used in Industries journeys.",
            [
                "Inventory rules and evaluation order.",
                "Test true/false and multi-match behavior.",
                "Confirm OS/IP consumption of results.",
                "Label org-specific rule names as TBC when unknown.",
            ],
            [("Decision Matrix", "decision-matrix.md")],
            ["Ambiguous multi-match without documented policy → Escalate BA/Architect."],
        ),
        (
            "Calculation Procedures",
            "calculation-procedures.md",
            "Validate Calculation Procedures/Matrices for pricing and scoring journeys.",
            [
                "Map inputs, steps, and output fields.",
                "Verify calculation accuracy with known fixtures (TDG).",
                "Cover zero/null/overflow edges.",
                "Do not invent formula results — use provided expected values.",
            ],
            [("Expression Sets", "expression-sets.md"), ("Test Data Generator", tdg)],
            ["No expected calc fixtures → Block accuracy claims.", "CPQ/EPC calc change → Expand Regression Scope."],
        ),
        (
            "Expression Sets",
            "expression-sets.md",
            "Validate Expression Set evaluation in Industries decisioning.",
            [
                "Inventory expressions and variable context.",
                "Test true/false and nested expressions.",
                "Confirm binding into OS/IP/decision paths.",
                "Flag hard-coded literals that should be configuration.",
            ],
            [("Calculation Procedures", "calculation-procedures.md")],
            ["Expression change without regression pack → High risk."],
        ),
        (
            "JSON Structure",
            "json-structure.md",
            "Validate OmniScript Data JSON and IP response JSON contracts.",
            [
                "Define expected keys at step boundaries.",
                "Validate types, arrays, and nested nodes.",
                "Detect orphan keys and overwrite collisions.",
                "Recommend TDG seed JSON for repeatable tests.",
            ],
            [("OmniScript Design", "omniscript-design.md"), ("Test Data Generator", tdg)],
            ["Missing JSON Validation section when OS in scope → Fail quality gate."],
        ),
        (
            "Remote Actions",
            "remote-actions.md",
            "Validate Remote/HTTP/Apex remotes and Salesforce Object actions.",
            [
                "Classify action type and auth/contract expectations.",
                "Stub request/response samples (sanitized).",
                "Validate error mapping back to OS messaging.",
                "Chain SOVA when SF object writes occur.",
            ],
            [("Integration Procedures", "integration-procedures.md"), ("SOQL Validation Assistant", sova)],
            ["Live credentials in artifacts → Critical Security escalate.", "No error-path remote tests → Incomplete Integration."],
        ),
        (
            "Performance Best Practices",
            "performance-best-practices.md",
            "Assess OmniStudio performance risks without inventing timings.",
            [
                "Flag chatty DR/IP patterns and oversized JSON.",
                "Note FlexCard nesting and refresh frequency risks.",
                "Require measured evidence or labeled assumptions for latency claims.",
                "Recommend sampling strategy — not invented SLA %.",
            ],
            [("OmniStudio Cloud Knowledge", cloud), ("Enterprise Quality Advisory", eq)],
            ["Invented p95/p99 numbers → Anti-pattern.", "No Performance Assessment when remotes in scope → Incomplete."],
        ),
        (
            "Error Handling",
            "error-handling.md",
            "Validate user-visible and orchestration error paths.",
            [
                "Map validation, remote, and system errors to UX messages.",
                "Confirm IP failure branches and OS catch paths.",
                "Ensure no silent data loss on partial failure.",
                "Document retry vs fail-fast policy.",
            ],
            [("Integration Procedures", "integration-procedures.md"), ("OmniScript Design", "omniscript-design.md")],
            ["Happy path only → Fail Negative Test Scenarios gate."],
        ),
        (
            "Salesforce Industries Deployment",
            "salesforce-industries-deployment.md",
            "Assess packaging, activation, and environment promotion for OmniStudio.",
            [
                "Inventory deployables (OS/FC/DR/IP/decision versions).",
                "Chain MIA for metadata impact and dependency order.",
                "Confirm activation/publish steps and Experience exposure.",
                "Document rollback and residual risk.",
            ],
            [("Metadata Impact Analyzer", mia), ("OmniStudio Cloud Knowledge", cloud)],
            ["Deploy without component inventory → No-Go Deployment Readiness."],
        ),
        (
            "OmniStudio Testing Best Practices",
            "omnistudio-testing-best-practices.md",
            "Synthesize enterprise OSQA discipline for Industries QA.",
            [
                "Business scenario + components before cases.",
                "Always cover functional, data/JSON, integration when in scope.",
                "Chain MIA/SOVA/PTA/PWR/AFT/TDG.",
                "Use 17-section report; label assumptions.",
            ],
            [("SKILL.md", "../SKILL.md"), ("OmniStudio Cloud Knowledge", cloud)],
            ["Every deliverable uses 17-section schema when journey QA is in scope."],
        ),
        (
            "Vlocity Industries Context",
            "vlocity-industries-context.md",
            "Advisory on Vlocity/Industries naming, licensing, and legacy packaging — not a license opinion.",
            [
                "Acknowledge Vlocity vs OmniStudio naming in brownfield orgs.",
                "Do not invent licensing entitlements — confirm with Architect.",
                "Map legacy package names to current OmniStudio components.",
                "Prefer current OmniStudio terminology in new artifacts.",
            ],
            [("OmniStudio Cloud Knowledge", cloud)],
            ["License claims without confirmation → Label TBC / escalate Architect."],
        ),
    ]
    for spec in knowledge_specs:
        write(f"knowledge/{spec[1]}", knowledge_article(*spec))

    write(
        "knowledge/README.md",
        fm("OmniStudio QA — Knowledge", "QE Specialized Skill Knowledge", "Guide", ["omnistudio-qa"])
        + """# OmniStudio QA — Knowledge

Canonical product encyclopedia: [`../../knowledge/clouds/omnistudio.md`](../../knowledge/clouds/omnistudio.md). These articles provide **OSQA reasoning models** only — do not duplicate encyclopedia bodies.

| Document | Focus |
|----------|-------|
| [OmniStudio Architecture](omnistudio-architecture.md) | Journey architecture |
| [OmniScript Design](omniscript-design.md) | Steps, JSON, submit |
| [FlexCard Architecture](flexcard-architecture.md) | Cards and actions |
| [DataRaptor Types](dataraptor-types.md) | Extract/Load/Transform/Turbo |
| [Integration Procedures](integration-procedures.md) | Orchestration |
| [Decision Matrix](decision-matrix.md) | Matrix rules |
| [Decision Tables](decision-tables.md) | Table rules |
| [Calculation Procedures](calculation-procedures.md) | Calc accuracy |
| [Expression Sets](expression-sets.md) | Expressions |
| [JSON Structure](json-structure.md) | Data JSON contracts |
| [Remote Actions](remote-actions.md) | Remotes / HTTP / Apex |
| [Performance Best Practices](performance-best-practices.md) | Perf risks (no invented %) |
| [Error Handling](error-handling.md) | Failure paths |
| [Salesforce Industries Deployment](salesforce-industries-deployment.md) | Deploy / activate |
| [OmniStudio Testing Best Practices](omnistudio-testing-best-practices.md) | OSQA discipline |
| [Vlocity Industries Context](vlocity-industries-context.md) | Naming / licensing advisory |

## Related Documents

- [SKILL.md](../SKILL.md)
""",
    )

    playbook_specs = [
        (
            "OmniScript Testing",
            "omniscript-testing.md",
            "Validate OmniScript journeys end-to-end including Data JSON and submit.",
            ["Business scenario", "OmniScript name/version", "Expected Data JSON samples", "Personas"],
            [
                "Confirm Business Scenario and component inventory.",
                "Walk steps, conditionals, required fields.",
                "Validate Save for Later / resume if in scope.",
                "Capture Data JSON at key steps; validate submit/IP handoff.",
                "Document negatives and edge cases.",
            ],
            ["Missing JSON samples → request TDG seed or label TBC.", "UI automation needed → chain PWR."],
            ["17-section report sections 1–7, 11–12 populated", "SOVA stubs for CRM outcomes"],
            ["Happy path + negatives documented", "No invented latency claims"],
            ["Broken submit / data corruption → Critical escalate"],
            "knowledge/omniscript-design.md",
        ),
        (
            "FlexCard Testing",
            "flexcard-testing.md",
            "Validate FlexCard render, actions, binding, and child cards.",
            ["Card inventory", "Data sources", "Action targets", "Personas"],
            [
                "Inventory cards and data sources.",
                "Validate render and conditional visibility.",
                "Exercise actions (OS/IP/nav).",
                "Check refresh/pagination; note perf risks.",
                "Chain PTA if restricted fields visible.",
            ],
            ["Wrong action target → Fail Functional Validation.", "PII exposure → escalate PTA/Security."],
            ["FlexCard findings in Architecture/Functional/Security sections"],
            ["Actions resolve to correct OS/IP versions"],
            ["Experience PII leak → Security Architect"],
            "knowledge/flexcard-architecture.md",
        ),
        (
            "DataRaptor Testing",
            "dataraptor-testing.md",
            "Validate DataRaptor mapping, formulas, null handling, and CRM accuracy.",
            ["DR type and name", "Input/output samples", "CRM expected outcomes"],
            [
                "Classify Extract/Load/Transform/Turbo.",
                "Trace mappings and formulas.",
                "Test null/missing input paths.",
                "Produce SOVA stubs for Load/CRM writes.",
                "Note performance risks without inventing timings.",
            ],
            ["Critical Load without SOVA → incomplete Data Validation."],
            ["Data + JSON Validation sections", "SOVA query stubs"],
            ["Mapping accuracy verified against fixtures"],
            ["Silent overwrite of critical fields → Critical"],
            "knowledge/dataraptor-types.md",
        ),
        (
            "Integration Procedure Testing",
            "integration-procedure-testing.md",
            "Validate IP flow, branches, cache, retry, remotes, and SF operations.",
            ["IP name/version", "Branch matrix", "Remote contracts (sanitized)", "Error expectations"],
            [
                "Map step sequence and branches.",
                "Execute happy and failure paths (advisory).",
                "Validate response mapping into OS/JSON.",
                "Document cache/retry policy; label assumptions.",
                "Chain SOVA for SF object actions.",
            ],
            ["No failure branch coverage → Fail Integration Validation."],
            ["Integration Validation + Negatives populated"],
            ["Branch matrix covered or residual risk listed"],
            ["Systemic remote failure → Release Manager + Omni Architect"],
            "knowledge/integration-procedures.md",
        ),
        (
            "Decision Matrix Testing",
            "decision-matrix-testing.md",
            "Validate Decision Matrix/Table and calculation/expression outcomes.",
            ["Matrix/table inventory", "Input fixtures", "Expected outputs"],
            [
                "Enumerate rules and priorities.",
                "Test defaults, boundaries, missing inputs.",
                "Trace caller OS/IP consumption.",
                "Use TDG fixtures for calc accuracy.",
            ],
            ["No expected fixtures → block accuracy claims."],
            ["Functional + Edge sections for decision logic"],
            ["Priority/default behavior documented"],
            ["Ambiguous multi-match → BA/Architect"],
            "knowledge/decision-matrix.md",
        ),
        (
            "Performance Testing",
            "performance-testing.md",
            "Assess OmniStudio performance risks with evidence or labeled assumptions.",
            ["Component inventory", "Known bottlenecks", "Any measured timings (optional)"],
            [
                "Identify chatty DR/IP and oversized JSON.",
                "Note FlexCard nesting/refresh risks.",
                "Recommend measurement approach.",
                "Populate Performance Assessment without inventing %.",
            ],
            ["Any numeric SLA without evidence → remove or label assumption."],
            ["Performance Assessment section", "Risks for known bottlenecks"],
            ["Assumptions labeled; no invented SLA %"],
            ["Prod latency Sev1 → Production support / Omni Architect"],
            "knowledge/performance-best-practices.md",
        ),
        (
            "Regression Testing",
            "regression-testing.md",
            "Define OmniStudio regression scope after component or metadata change.",
            ["MIA impact (if any)", "Changed components", "Dependent journeys"],
            [
                "Start from MIA/component delta.",
                "Map consumers (reusable OS, shared DR/IP).",
                "Prioritize critical journeys.",
                "Link TDG seed packs and automation opportunities.",
            ],
            ["Reusable OS changed → expand consumer regression."],
            ["Regression Scope section", "Automation Opportunities"],
            ["Critical journeys listed with residual risk"],
            ["Unscoped high-risk shared IP → No-Go until owned"],
            "knowledge/omnistudio-testing-best-practices.md",
        ),
        (
            "Release Readiness",
            "release-readiness.md",
            "Assess deployment readiness for OmniStudio / Industries release.",
            ["Component versions", "Activation checklist", "Security/Experience sign-off", "Defect residual risk"],
            [
                "Confirm Business Scenario and Components Reviewed present.",
                "Verify functional/data/JSON/integration coverage.",
                "Chain PTA for Experience; MIA for deploy order.",
                "Document Go / Conditional Go / No-Go with risks.",
            ],
            ["Critical open defects → No-Go.", "Missing security for Experience → Conditional Go at best."],
            ["Deployment Readiness + Risks + Recommendations"],
            ["Decision recorded with evidence links"],
            ["PII / data corruption open → Security + Release Manager"],
            "knowledge/salesforce-industries-deployment.md",
        ),
    ]
    for spec in playbook_specs:
        write(f"playbooks/{spec[1]}", playbook(*spec))

    write(
        "playbooks/README.md",
        fm("OmniStudio QA — Playbooks", "QE Specialized Skill Playbook", "Guide", ["omnistudio-qa"])
        + """# OmniStudio QA — Playbooks

| Playbook | Focus |
|----------|-------|
| [OmniScript Testing](omniscript-testing.md) | Journey / JSON / submit |
| [FlexCard Testing](flexcard-testing.md) | Cards / actions |
| [DataRaptor Testing](dataraptor-testing.md) | Mapping / CRM proof |
| [Integration Procedure Testing](integration-procedure-testing.md) | Orchestration |
| [Decision Matrix Testing](decision-matrix-testing.md) | Decision / calc |
| [Performance Testing](performance-testing.md) | Perf risks |
| [Regression Testing](regression-testing.md) | Change impact |
| [Release Readiness](release-readiness.md) | Go / No-Go |

## Related Documents

- [SKILL.md](../SKILL.md)
""",
    )

    # Templates
    write("templates/omnistudio-test-strategy.md", template_doc(
        "OmniStudio Test Strategy",
        [
            "Program Context",
            "In-Scope Journeys",
            "Component Inventory Approach",
            "Test Levels (Unit / Integration / E2E / UAT)",
            "Data / JSON Strategy",
            "Security / Experience Strategy",
            "Performance Strategy",
            "Automation Strategy (PWR / API)",
            "Regression Strategy",
            "Environments and Entry/Exit Criteria",
            "Risks and Assumptions",
            "Traceability",
        ],
    ))
    write("templates/omniscript-test-report.md", template_doc(
        "OmniScript / OmniStudio Test Report",
        OUTPUT_SECTIONS,
    ))
    write("templates/dataraptor-validation-report.md", template_doc(
        "DataRaptor Validation Report",
        [
            "Executive Summary",
            "DataRaptor Inventory",
            "Type and Contract Assessment",
            "Mapping Validation",
            "Formula and Null Handling",
            "CRM Outcome / SOVA Stubs",
            "Negative and Edge Cases",
            "Performance Notes",
            "Risks",
            "Recommendations",
        ],
    ))
    write("templates/integration-procedure-test-report.md", template_doc(
        "Integration Procedure Test Report",
        [
            "Executive Summary",
            "IP Inventory",
            "Flow and Branch Matrix",
            "Response Mapping",
            "Cache and Retry Policy",
            "Remote / HTTP / Apex Actions",
            "Salesforce Object Operations",
            "Error Handling",
            "SOVA Stubs",
            "Risks",
            "Recommendations",
        ],
    ))
    write("templates/performance-assessment-report.md", template_doc(
        "OmniStudio Performance Assessment Report",
        [
            "Executive Summary",
            "Components and Risk Drivers",
            "JSON Size / Chatty Call Patterns",
            "FlexCard Nesting / Refresh",
            "Measurement Plan",
            "Evidence or Assumptions",
            "Risks",
            "Recommendations",
        ],
    ))
    write("templates/regression-checklist.md", template_doc(
        "OmniStudio Regression Checklist",
        [
            "Change Summary",
            "MIA / Metadata Impact",
            "Affected Journeys",
            "Shared / Reusable Component Consumers",
            "Must-Run Scenarios",
            "Optional / Deferred Scenarios",
            "Automation Coverage Gaps",
            "Sign-Off",
        ],
    ))
    write("templates/deployment-readiness-checklist.md", template_doc(
        "OmniStudio Deployment Readiness Checklist",
        [
            "Business Scenario Confirmed",
            "Components Reviewed Confirmed",
            "Functional / Data / JSON / Integration Gates",
            "Security / Experience Gates",
            "Performance Residual Risk",
            "Defect Residual Risk",
            "Activation / Publish Steps",
            "Rollback Plan",
            "Go / Conditional Go / No-Go Decision",
        ],
    ))
    write("templates/defect-root-cause-template.md", template_doc(
        "OmniStudio Defect Root Cause Template",
        [
            "Defect Summary",
            "Business Scenario Impact",
            "Component(s) Involved",
            "Observed vs Expected",
            "Root Cause Hypothesis",
            "JSON / Mapping / Integration Evidence",
            "Security / Data Impact",
            "Fix Verification Plan",
            "Regression Additions",
            "Lessons Learned",
        ],
    ))
    write(
        "templates/README.md",
        fm("OmniStudio QA — Templates", "QE Specialized Skill Template", "Guide", ["omnistudio-qa"])
        + """# OmniStudio QA — Templates

| Template | Use |
|----------|-----|
| [OmniStudio Test Strategy](omnistudio-test-strategy.md) | Program-level strategy |
| [OmniScript Test Report](omniscript-test-report.md) | **Primary 17-section QA report** |
| [DataRaptor Validation Report](dataraptor-validation-report.md) | DR-focused |
| [Integration Procedure Test Report](integration-procedure-test-report.md) | IP-focused |
| [Performance Assessment Report](performance-assessment-report.md) | Perf (no invented %) |
| [Regression Checklist](regression-checklist.md) | Change regression |
| [Deployment Readiness Checklist](deployment-readiness-checklist.md) | Go / No-Go |
| [Defect Root Cause Template](defect-root-cause-template.md) | Defect analysis |

## Related Documents

- [SKILL.md](../SKILL.md)
""",
    )

    prompts = [
        (
            "Review OmniScript",
            "review-omniscript.md",
            "Load skills/omnistudio-qa/SKILL.md.\nReview OmniScript: {{OmniScriptName}} for business scenario: {{Scenario}}.\nInventory related DR/IP/FlexCards. Produce all 17 output sections.\nLabel assumptions; do not invent latency %.",
        ),
        (
            "Validate FlexCard",
            "validate-flexcard.md",
            "Load skills/omnistudio-qa/SKILL.md.\nValidate FlexCard: {{FlexCardName}} — render, actions, binding, child cards.\nInclude Security Assessment if Experience-exposed. Chain PTA when FLS risk.",
        ),
        (
            "Review Integration Procedure",
            "review-integration-procedure.md",
            "Load skills/omnistudio-qa/SKILL.md.\nReview Integration Procedure: {{IPName}} — branches, cache, retry, remotes, SF ops.\nPopulate Integration Validation, Negatives, and SOVA stubs.",
        ),
        (
            "Validate DataRaptor",
            "validate-dataraptor.md",
            "Load skills/omnistudio-qa/SKILL.md.\nValidate DataRaptor: {{DRName}} (type: {{Type}}).\nTrace mappings, null handling, and CRM outcomes. Chain SOVA for Load paths.",
        ),
        (
            "Review Decision Matrix",
            "review-decision-matrix.md",
            "Load skills/omnistudio-qa/SKILL.md.\nReview Decision Matrix/Table: {{MatrixName}} with input fixtures {{Fixtures}}.\nCover priorities, defaults, and edges. Do not invent expected calc results.",
        ),
        (
            "Validate JSON",
            "validate-json.md",
            "Load skills/omnistudio-qa/SKILL.md.\nValidate OmniScript Data JSON / IP response JSON for {{Journey}}.\nDocument key contracts, types, and overwrite risks. Recommend TDG seed packs.",
        ),
        (
            "Generate OmniStudio Test Cases",
            "generate-omnistudio-test-cases.md",
            "Load skills/omnistudio-qa/SKILL.md.\nBusiness Scenario: {{Scenario}}.\nComponents: {{ComponentList}}.\nGenerate test cases ONLY after Business Scenario + Components Reviewed.\nInclude functional, data/JSON, integration, negatives, edges.",
        ),
        (
            "Review Performance",
            "review-performance.md",
            "Load skills/omnistudio-qa/SKILL.md.\nAssess performance risks for {{Journey}} components {{ComponentList}}.\nUse evidence or labeled assumptions — never invent latency/throughput %.",
        ),
        (
            "Assess Deployment Readiness",
            "assess-deployment-readiness.md",
            "Load skills/omnistudio-qa/SKILL.md.\nAssess Deployment Readiness for OmniStudio release {{ReleaseId}}.\nConfirm gates, residual risk, and Go / Conditional Go / No-Go. Chain MIA/PTA as needed.",
        ),
        (
            "Analyze OmniStudio Defects",
            "analyze-omnistudio-defects.md",
            "Load skills/omnistudio-qa/SKILL.md.\nAnalyze defect {{DefectId}} for journey {{Scenario}}.\nUse defect root-cause template themes: component, JSON/mapping/integration evidence, fix verification, regression additions.",
        ),
    ]
    for title, slug, prompt in prompts:
        write(f"prompts/{slug}", prompt_doc(title, prompt, OUTPUT_SECTIONS))

    write(
        "prompts/README.md",
        fm("OmniStudio QA — Prompts", "QE Specialized Skill Prompt", "Guide", ["omnistudio-qa"])
        + """# OmniStudio QA — Prompts

| Prompt | File |
|--------|------|
| Review OmniScript | [review-omniscript.md](review-omniscript.md) |
| Validate FlexCard | [validate-flexcard.md](validate-flexcard.md) |
| Review Integration Procedure | [review-integration-procedure.md](review-integration-procedure.md) |
| Validate DataRaptor | [validate-dataraptor.md](validate-dataraptor.md) |
| Review Decision Matrix | [review-decision-matrix.md](review-decision-matrix.md) |
| Validate JSON | [validate-json.md](validate-json.md) |
| Generate OmniStudio Test Cases | [generate-omnistudio-test-cases.md](generate-omnistudio-test-cases.md) |
| Review Performance | [review-performance.md](review-performance.md) |
| Assess Deployment Readiness | [assess-deployment-readiness.md](assess-deployment-readiness.md) |
| Analyze OmniStudio Defects | [analyze-omnistudio-defects.md](analyze-omnistudio-defects.md) |

## Related Documents

- [SKILL.md](../SKILL.md)
""",
    )

    examples = [
        (
            "Customer Onboarding",
            "customer-onboarding.md",
            "New customer completes Industries onboarding guided flow across Account/Contact creation.",
            "OmniScript Onboarding; DR Extract Account; DR Load Contact; IP CreateCustomer; FlexCard Status.",
            "Validate end-to-end onboarding, Data JSON, CRM creates, and Experience access.",
            "Happy path steps; conditional KYC branch; Save for Later; submit success.",
            "SOVA stubs: Account/Contact created with expected fields; IP response codes.",
            "Customer record created; OS completes; FlexCard shows Active.",
            "Duplicate email; missing required; remote timeout; unauthorized Experience user.",
            "Chain PTA for Experience; TDG for seed; PWR for UI automation.",
        ),
        (
            "Utility Service Connection",
            "utility-service-connection.md",
            "Utility customer requests new service connection at premises.",
            "OmniScript ServiceConnect; DR Extract Premises; IP CreateServicePoint; Decision Matrix Eligibility.",
            "Validate eligibility decision, premises data, and service point create.",
            "Eligible premises; ineligible premises; multi-service select.",
            "SOVA: ServicePoint / related utility objects as configured.",
            "Eligible path creates service point; ineligible shows message.",
            "Invalid premise ID; IP branch failure; FLS on premise fields.",
            "Chain SOVA + PTA; label utility object API names TBC if unknown.",
        ),
        (
            "Meter Installation",
            "meter-installation.md",
            "Field-aligned Industries journey for meter install scheduling handoff.",
            "OmniScript MeterInstall; FlexCard AppointmentSummary; DR Load Asset; IP NotifyFSL.",
            "Validate asset create/update and handoff messaging (not full FSL QA).",
            "Install complete; cancel; reschedule note.",
            "SOVA: Asset fields; optional FSQA cross-link for scheduling depth.",
            "Asset updated; FlexCard reflects status.",
            "Missing meter serial; IP notify failure.",
            "Cross-link FSQA for deep Field Service; keep OSQA on Omni path.",
        ),
        (
            "Move In Move Out",
            "move-in-move-out.md",
            "Utility Move In / Move Out guided journey.",
            "OmniScript MoveInOut; DR Extract AccountService; IP TransferService; FlexCard Timeline.",
            "Validate transfer logic, JSON, and CRM updates.",
            "Move In; Move Out; same-day both; Save for Later.",
            "SOVA stubs for service dates and account linkage.",
            "Correct service dates; timeline card updates.",
            "Overlapping dates; unauthorized user; remote fail.",
            "Primary reference journey for OSQA smoke demos.",
        ),
        (
            "Product Configuration",
            "product-configuration.md",
            "CPQ/EPC-style product configuration via OmniStudio.",
            "OmniScript ProductConfig; Decision Matrix Options; Calculation Procedure Price; FlexCard Cart.",
            "Validate option rules and calculation accuracy with fixtures.",
            "Base + add-on; incompatible options; quantity edges.",
            "Expected calc fixtures from TDG; no invented prices.",
            "Cart totals match fixtures; incompatible blocked.",
            "Zero quantity; missing price book; expression error.",
            "Do not invent EPC catalog — label TBC.",
        ),
        (
            "Quote Generation",
            "quote-generation.md",
            "Sales quote generation through Industries guided flow.",
            "OmniScript QuoteGen; DR Load QuoteLine; IP SubmitQuote; Decision Table Discounts.",
            "Validate quote lines, discounts, and submit.",
            "Standard quote; discount path; multi-product.",
            "SOVA: Quote / QuoteLineItem fields.",
            "Quote submitted; lines match JSON.",
            "Discount over limit; submit failure; FLS on amount.",
            "Chain PTA for amount fields; SOVA for CRM proof.",
        ),
        (
            "Case Intake",
            "case-intake.md",
            "Service case intake via OmniScript for contact centers.",
            "OmniScript CaseIntake; DR Load Case; FlexCard CaseSummary; IP EnrichCustomer.",
            "Validate case create, enrichment, and summary card.",
            "Billing inquiry; technical issue; escalate.",
            "SOVA: Case fields and Account link.",
            "Case created with correct Type/Reason.",
            "Missing contact; enrichment timeout; duplicate case.",
            "Chain AFT if Agentforce assists intake.",
        ),
        (
            "Complaint Registration",
            "complaint-registration.md",
            "Regulated complaint registration journey.",
            "OmniScript ComplaintReg; DR Load Complaint; Decision Matrix Severity; IP NotifyCompliance.",
            "Validate severity classification and compliance notify.",
            "Standard complaint; high severity; anonymous.",
            "SOVA stubs for complaint custom object (label API TBC).",
            "Severity set; notify invoked for high.",
            "PII in free text; notify failure; unauthorized portal user.",
            "Escalate Security for PII; PTA for portal.",
        ),
        (
            "Insurance Claim Submission",
            "insurance-claim-submission.md",
            "Insurance FNOL / claim submission guided journey.",
            "OmniScript ClaimSubmit; DR Extract Policy; DR Load Claim; IP ValidateCoverage; FlexCard ClaimStatus.",
            "Validate policy lookup, claim create, coverage validation.",
            "In-coverage claim; out-of-coverage; multi-claimant.",
            "SOVA: Claim / Policy related objects (API TBC).",
            "In-coverage creates claim; out-of-coverage message.",
            "Expired policy; remote coverage timeout; FLS on claim amount.",
            "Label insurance object model TBC; chain PTA/SOVA.",
        ),
        (
            "Healthcare Enrollment",
            "healthcare-enrollment.md",
            "Healthcare member enrollment Industries journey.",
            "OmniScript EnrollMember; DR Load Member; Decision Table PlanEligibility; IP CreateCoverage; FlexCard Benefits.",
            "Validate eligibility, member create, coverage create.",
            "Eligible enroll; ineligible; dependent add.",
            "SOVA stubs for member/coverage objects (API TBC).",
            "Eligible path creates coverage; benefits card updates.",
            "HIPAA-sensitive field exposure; IP failure; missing dependent data.",
            "Chain PTA for sensitive FLS; never invent PHI samples — use synthetic TDG.",
        ),
    ]
    for title, slug, scenario, components, objectives, scenarios, backend, expected, negatives, qa in examples:
        write(
            f"examples/{slug}",
            example_doc(title, scenario, components, objectives, scenarios, backend, expected, negatives, qa),
        )

    write(
        "examples/README.md",
        fm("OmniStudio QA — Examples", "QE Specialized Skill Example", "Guide", ["omnistudio-qa"])
        + """# OmniStudio QA — Examples

| Example | Domain |
|---------|--------|
| [Customer Onboarding](customer-onboarding.md) | Onboarding |
| [Utility Service Connection](utility-service-connection.md) | Utilities |
| [Meter Installation](meter-installation.md) | Utilities / FSL handoff |
| [Move In Move Out](move-in-move-out.md) | Utilities |
| [Product Configuration](product-configuration.md) | CPQ / EPC |
| [Quote Generation](quote-generation.md) | Sales / CPQ |
| [Case Intake](case-intake.md) | Service |
| [Complaint Registration](complaint-registration.md) | Service / Compliance |
| [Insurance Claim Submission](insurance-claim-submission.md) | Insurance |
| [Healthcare Enrollment](healthcare-enrollment.md) | Healthcare |

## Related Documents

- [SKILL.md](../SKILL.md)
- [TDG OmniStudio Journey Data](../test-data-generator/examples/omnistudio-journey-data.md)
""",
    )

    tests = [
        (
            "OmniScript Navigation",
            "scenario-omniscript-navigation.md",
            "Validate step navigation, conditionals, and required fields.",
            ["Business scenario documented", "OmniScript inventory listed"],
            ["Open OS", "Navigate steps including conditional branch", "Attempt skip required", "Complete happy path"],
            ["Conditional path reachable", "Required enforcement observed", "Inventory preceded detailed cases"],
            ["PWR for UI automation design", "TDG for step fixtures"],
        ),
        (
            "FlexCard Rendering",
            "scenario-flexcard-rendering.md",
            "Validate FlexCard render, visibility, and actions.",
            ["FlexCard inventory", "Data source available (stub OK)"],
            ["Render card", "Toggle conditional visibility", "Invoke primary action"],
            ["Correct data binding", "Action target correct OS/IP"],
            ["PTA if restricted fields", "PWR for UI assert patterns"],
        ),
        (
            "DataRaptor Mapping",
            "scenario-dataraptor-mapping.md",
            "Validate DR field mapping and null handling.",
            ["DR type known", "Input/output fixtures"],
            ["Run Extract/Transform with fixtures", "Exercise null inputs", "Trace Load mappings"],
            ["Mappings match expected", "Null behavior documented"],
            ["SOVA stubs for Load CRM proof", "TDG for fixtures"],
        ),
        (
            "Integration Procedure Execution",
            "scenario-integration-procedure-execution.md",
            "Validate IP happy and branch/failure paths.",
            ["IP inventory", "Branch matrix"],
            ["Execute happy path", "Force failure branch", "Validate response mapping"],
            ["Branches covered or residual risk listed", "Errors mapped to OS"],
            ["SOVA for SF ops", "Remote contract stubs"],
        ),
        (
            "Decision Logic",
            "scenario-decision-logic.md",
            "Validate Decision Matrix/Table priorities and defaults.",
            ["Matrix/table inventory", "Input fixtures"],
            ["Apply priority rows", "Apply default", "Missing input"],
            ["Outputs match fixtures", "Caller OS/IP consumes result"],
            ["TDG fixtures", "No invented outputs"],
        ),
        (
            "Calculation Accuracy",
            "scenario-calculation-accuracy.md",
            "Validate Calculation Procedure / Expression Set with known fixtures.",
            ["Calc/expression inventory", "Expected result fixtures"],
            ["Run base calc", "Edge zero/null", "Overflow or max if defined"],
            ["Results match fixtures only", "Edges documented"],
            ["TDG for calc packs", "Do not invent prices"],
        ),
        (
            "Error Handling",
            "scenario-error-handling.md",
            "Validate validation, remote, and system error UX/orchestration.",
            ["Error catalog", "OS/IP catch paths known"],
            ["Trigger field validation", "Simulate remote timeout", "Simulate IP failure"],
            ["User message clear", "No silent data loss"],
            ["Negatives section required"],
        ),
        (
            "Performance",
            "scenario-performance.md",
            "Document performance risk assessment without inventing timings.",
            ["Component inventory", "Optional measured evidence"],
            ["Identify chatty patterns", "Note JSON size risks", "Recommend measurement"],
            ["Assumptions labeled", "No invented latency %"],
            ["Performance Assessment section"],
        ),
        (
            "Security",
            "scenario-security.md",
            "Validate CRUD/FLS/Experience exposure themes for Omni journeys.",
            ["Personas", "Restricted fields list"],
            ["Run as authorized persona", "Run as unauthorized", "Check Experience exposure"],
            ["Unauthorized blocked", "FLS respected"],
            ["Chain PTA", "Escalate PII issues"],
        ),
        (
            "Regression",
            "scenario-regression.md",
            "Validate regression pack after OmniStudio component change.",
            ["Change list / MIA report", "Dependent journeys"],
            ["Map consumers", "Execute must-run journeys", "Record residual risk"],
            ["Critical journeys covered", "Shared IP/OS consumers listed"],
            ["MIA upstream", "Automation Opportunities"],
        ),
        (
            "Production Readiness",
            "scenario-production-readiness.md",
            "Validate Deployment Readiness gates for release.",
            ["17-section report draft", "Defect list", "Activation plan"],
            ["Confirm Business Scenario + Components Reviewed", "Check functional/data/JSON/integration", "Record Go decision"],
            ["Gates evidenced", "No-Go if critical open"],
            ["MIA + PTA + Release Manager"],
        ),
    ]
    for title, slug, purpose, preconditions, steps, asserts, chains in tests:
        write(f"tests/{slug}", test_doc(title, purpose, preconditions, steps, asserts, chains))

    write(
        "tests/README.md",
        fm("OmniStudio QA — Tests", "QE Specialized Skill Test", "Guide", ["omnistudio-qa"])
        + """# OmniStudio QA — Tests

| Scenario | File |
|----------|------|
| OmniScript Navigation | [scenario-omniscript-navigation.md](scenario-omniscript-navigation.md) |
| FlexCard Rendering | [scenario-flexcard-rendering.md](scenario-flexcard-rendering.md) |
| DataRaptor Mapping | [scenario-dataraptor-mapping.md](scenario-dataraptor-mapping.md) |
| Integration Procedure Execution | [scenario-integration-procedure-execution.md](scenario-integration-procedure-execution.md) |
| Decision Logic | [scenario-decision-logic.md](scenario-decision-logic.md) |
| Calculation Accuracy | [scenario-calculation-accuracy.md](scenario-calculation-accuracy.md) |
| Error Handling | [scenario-error-handling.md](scenario-error-handling.md) |
| Performance | [scenario-performance.md](scenario-performance.md) |
| Security | [scenario-security.md](scenario-security.md) |
| Regression | [scenario-regression.md](scenario-regression.md) |
| Production Readiness | [scenario-production-readiness.md](scenario-production-readiness.md) |

## Related Documents

- [SKILL.md](../SKILL.md)
""",
    )

    print("Done.")


if __name__ == "__main__":
    main()
