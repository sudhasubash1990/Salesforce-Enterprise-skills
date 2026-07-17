#!/usr/bin/env python3
"""Sprint 11 — Enterprise Validation, Certification & Continuous Improvement pack."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VAL = ROOT / "salesforce-quality-engineering" / "validation"
VER = "0.14.0"

INDUSTRIES = [
    ("utilities", "Utilities", "Meter-to-cash, outage, field service"),
    ("retail", "Retail", "Omnichannel order, loyalty, returns"),
    ("banking", "Banking", "KYC onboarding, case servicing"),
    ("insurance", "Insurance", "FNOL, policy servicing"),
    ("healthcare", "Healthcare", "Patient/provider care coordination (overview)"),
    ("manufacturing", "Manufacturing", "Dealer, asset, warranty"),
    ("telecommunications", "Telecommunications", "Provisioning, activation, billing disputes"),
    ("public-sector", "Public Sector", "Constituent case / grants overview"),
    ("energy", "Energy", "Account/service, program enrollment overview"),
    ("consumer-goods", "Consumer Goods", "Trade promotion / retail execution overview"),
]

CAPABILITY_FOLDERS = [
    (
        "repository-validation",
        "Repository Validation",
        "Validate QE module structure, naming, markdown, links, duplicates, navigation, versioning.",
        [
            ("folder-structure.md", "Folder Structure", "Required L1/L2 folders present"),
            ("naming-standards.md", "Naming Standards", "lowercase-hyphen; CHANGELOG case"),
            ("markdown-standards.md", "Markdown Standards", "Frontmatter, Purpose/Scope sections"),
            ("cross-references.md", "Cross References", "Related Documents resolve"),
            ("broken-links.md", "Broken Links", "Relative links resolve"),
            ("duplicate-documents.md", "Duplicate Documents", "Multi-lens policy compliance"),
            ("navigation.md", "Navigation", "Previous/Next/Up consistency"),
            ("readme-quality.md", "README Quality", "Purpose, Scope, Inputs, Outputs"),
            ("file-consistency.md", "File Consistency", "Engine entry points exist"),
            ("versioning.md", "Versioning", "skill/README/CHANGELOG aligned"),
            ("completeness.md", "Completeness", "Sprints 1–10 packs present"),
            ("repository-scorecard.md", "Repository Scorecard", "Weighted repo dimension scores"),
        ],
    ),
    (
        "knowledge-validation",
        "Knowledge Validation",
        "Validate 4A/4B and domain knowledge expected outcomes.",
        [
            ("platform-knowledge.md", "Platform Knowledge", "Objects, relationships, record types"),
            ("metadata.md", "Metadata", "Deployable config testability"),
            ("automation.md", "Automation (platform)", "Flow/Apex/order of execution QE lens"),
            ("security.md", "Security", "CRUD/FLS/sharing scenarios"),
            ("integrations.md", "Integrations", "API/events/contracts"),
            ("clouds.md", "Clouds", "Sales/Service/Experience/… articles"),
            ("industry-knowledge.md", "Industry Knowledge", "Industry folders + BA scenario links"),
            ("performance.md", "Performance", "LDV/governor awareness"),
            ("release-management.md", "Release Management", "Release knowledge pack"),
            ("production-support-knowledge.md", "Production Support Knowledge", "PS knowledge cross-links"),
        ],
    ),
    (
        "requirement-validation",
        "Requirement Validation",
        "Validate Sprint 2 Requirement Analysis Engine behaviours.",
        [
            ("requirement-analysis.md", "Requirement Analysis", "10-step analysis enforced"),
            ("business-rules.md", "Business Rules", "Rules extracted/testable"),
            ("acceptance-criteria.md", "Acceptance Criteria", "GWT quality"),
            ("stakeholder-analysis.md", "Stakeholder Analysis", "Personas identified"),
            ("gap-analysis.md", "Gap Analysis", "Gaps flagged"),
            ("risk-analysis.md", "Risk Analysis", "Risks with mitigations intent"),
            ("requirement-quality.md", "Requirement Quality", "Completeness band"),
            ("clarification-questions.md", "Clarification Questions", "Blocking questions listed"),
            ("traceability.md", "Traceability", "ID chain intent"),
            ("coverage.md", "Coverage", "Component scan coverage"),
        ],
    ),
    (
        "test-design-validation",
        "Test Design Validation",
        "Validate Sprint 3 Test Design Engine outputs.",
        [
            ("functional-testing.md", "Functional Testing", "Happy-path objectives"),
            ("negative-testing.md", "Negative Testing", "Negative objectives"),
            ("boundary-testing.md", "Boundary Testing", "Boundary objectives"),
            ("regression-scope.md", "Regression Scope", "In/Out/Conditional"),
            ("automation-candidates.md", "Automation Candidates", "Candidates without scripts"),
            ("risk-coverage.md", "Risk Coverage", "Risk-based selection"),
            ("security-coverage.md", "Security Coverage", "Persona/permission paths"),
            ("integration-coverage.md", "Integration Coverage", "Interface scenarios"),
            ("data-validation.md", "Data Validation", "Data considerations"),
            ("performance-considerations.md", "Performance Considerations", "When in scope only"),
        ],
    ),
    (
        "documentation-validation",
        "Documentation Validation",
        "Validate Sprint 5 generated/template artifacts.",
        [
            ("test-strategies.md", "Test Strategies", "Strategy completeness"),
            ("test-plans.md", "Test Plans", "Plan completeness"),
            ("rtms.md", "RTMs", "Traceability matrix quality"),
            ("test-scenarios.md", "Test Scenarios", "Scenario packs"),
            ("test-cases.md", "Test Cases", "Only after design"),
            ("defect-reports.md", "Defect Reports", "Defect template quality"),
            ("qa-reports.md", "QA Reports", "Report consistency"),
            ("dashboards.md", "Dashboards", "Dashboard definitions"),
            ("playbooks.md", "Playbooks", "Ceremony guidance"),
            ("templates.md", "Templates", "Template library"),
            ("checklists.md", "Checklists", "Checklist library"),
        ],
    ),
    (
        "ado-validation",
        "Azure DevOps Validation",
        "Validate Sprint 6 ADO Delivery Intelligence guidance.",
        [
            ("epics.md", "Epics", "Epic guidance"),
            ("features.md", "Features", "Feature guidance"),
            ("user-stories.md", "User Stories", "Story ADO pack"),
            ("tasks.md", "Tasks", "Task guidance"),
            ("bugs.md", "Bugs", "Bug workflow"),
            ("test-plans.md", "Test Plans", "ADO Test Plans"),
            ("test-suites.md", "Test Suites", "Suite strategy"),
            ("test-cases.md", "Test Cases", "ADO cases"),
            ("dashboards.md", "Dashboards", "ADO dashboards"),
            ("queries.md", "Queries", "WIQL/query intel"),
            ("traceability.md", "Traceability", "E2E mapping"),
            ("work-item-relationships.md", "Work Item Relationships", "Hierarchy/links"),
        ],
    ),
    (
        "defect-validation",
        "Defect Intelligence Validation",
        "Validate Sprint 7 Defect Intelligence & Rules.",
        [
            ("defect-classification.md", "Defect Classification", "Taxonomy"),
            ("severity.md", "Severity", "Severity model"),
            ("priority.md", "Priority", "Priority model"),
            ("root-cause-analysis.md", "Root Cause Analysis", "RCA quality"),
            ("trend-analysis.md", "Trend Analysis", "Trends without invented %"),
            ("pattern-detection.md", "Pattern Detection", "Patterns/rules"),
            ("quality-metrics.md", "Quality Metrics", "Metric definitions"),
            ("preventive-actions.md", "Preventive Actions", "Prevention loop"),
            ("executive-reporting.md", "Executive Reporting", "QI exec reports"),
        ],
    ),
    (
        "automation-validation",
        "Automation Validation",
        "Validate Sprint 8 Automation Intelligence.",
        [
            ("automation-strategy.md", "Automation Strategy", "Strategy quality"),
            ("framework-selection.md", "Framework Selection", "Selection rationale"),
            ("playwright-guidance.md", "Playwright Guidance", "Playwright-first"),
            ("ci-cd.md", "CI/CD", "Pipeline test stages"),
            ("automation-roi.md", "Automation ROI", "ROI without invented numbers"),
            ("automation-governance.md", "Automation Governance", "Governance"),
            ("automation-metrics.md", "Automation Metrics", "Metric definitions"),
            ("framework-health.md", "Framework Health", "Review engine"),
        ],
    ),
    (
        "production-validation",
        "Production Support Validation",
        "Validate Sprint 9 Production Support & Ops Intelligence.",
        [
            ("incident-analysis.md", "Incident Analysis", "Incident triage"),
            ("problem-management.md", "Problem Management", "Problem/RCA"),
            ("release-readiness.md", "Release Readiness", "Release ops"),
            ("hypercare.md", "Hypercare", "Hypercare model"),
            ("monitoring.md", "Monitoring", "Monitoring intel"),
            ("runbooks.md", "Runbooks", "Runbook quality"),
            ("operational-metrics.md", "Operational Metrics", "No invented SLA"),
            ("service-management.md", "Service Management", "ITIL alignment"),
            ("production-stability.md", "Production Stability", "Stability signals"),
        ],
    ),
    (
        "enterprise-validation",
        "Enterprise Advisory Validation",
        "Validate Sprint 10 Enterprise Quality Advisory & Orchestrator.",
        [
            ("quality-maturity.md", "Quality Maturity", "Maturity assessment"),
            ("project-health.md", "Project Health", "Health RAG"),
            ("portfolio-health.md", "Portfolio Health", "Portfolio view"),
            ("architecture-assessment.md", "Architecture Assessment", "Architecture quality"),
            ("governance.md", "Governance", "Delivery governance"),
            ("compliance.md", "Compliance", "Overview/TBC only"),
            ("executive-recommendations.md", "Executive Recommendations", "Recommendation engine"),
            ("decision-engine.md", "Decision Engine", "Proceed/Hold/Escalate"),
            ("transformation-roadmaps.md", "Transformation Roadmaps", "Roadmap quality"),
        ],
    ),
]

GOLDEN = [
    ("requirement-analysis", "Requirement Analysis", "Incomplete + enriched stories"),
    ("test-design", "Test Design", "Scenario objective packs"),
    ("salesforce-metadata", "Salesforce Metadata", "Synthetic impact maps"),
    ("defects", "Defects", "Anonymized defect samples"),
    ("azure-devops", "Azure DevOps", "Work item hierarchy samples"),
    ("automation", "Automation", "Strategy/review inputs"),
    ("production-incidents", "Production Incidents", "Incident intake samples"),
    ("release-validation", "Release Validation", "Go/No-Go evidence packs"),
    ("executive-reporting", "Executive Reporting", "RAG signal packs"),
]

SCORECARDS = [
    ("repository", "Repository", 15),
    ("knowledge", "Knowledge", 10),
    ("requirement-analysis", "Requirement Analysis", 10),
    ("test-design", "Test Design", 10),
    ("documentation", "Documentation", 8),
    ("azure-devops", "Azure DevOps", 8),
    ("defect-intelligence", "Defect Intelligence", 8),
    ("automation", "Automation", 8),
    ("production-support", "Production Support", 8),
    ("enterprise-advisory", "Enterprise Advisory", 10),
    ("overall-framework", "Overall Framework", 5),
]


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def folder_readme(title: str, purpose: str, rel_docs: str, children: str = "") -> str:
    return f"""---
title: {title}
version: {VER}
tags: [validation, sprint-11]
---

# {title}

## Purpose

{purpose}

## Scope

**In:** Validation rules, expected outcomes, scorecards for this domain.  
**Out:** Live org execution; inventing certification levels for a checkout without evidence.

## Inputs

- Repository checkout / sample artifact / golden dataset
- [../enterprise-validation-engine.md](../enterprise-validation-engine.md)

## Outputs

- Pass / Partial / Fail with evidence paths
- Scorecard rows and improvement actions

## Navigation

- **Up:** [../README.md](../README.md)
- **Engine:** [../enterprise-validation-engine.md](../enterprise-validation-engine.md)

## Related Documents

{rel_docs}

{children}
"""


def validation_article(title: str, objective: str, folder: str, topic: str) -> str:
    return f"""---
title: {title}
version: {VER}
tags: [validation, sprint-11, {folder}]
---

# {title}

## Purpose

Validate **{topic}** within the Salesforce Quality Engineering framework.

## Validation Objective

{objective}

## Inputs

- Relevant module paths under `salesforce-quality-engineering/`
- Optional golden dataset from [../golden-datasets/](../golden-datasets/README.md)
- Prior sprint engine outputs when validating behaviour

## Expected Outputs

- Checklist results (Pass / Partial / Fail)
- Evidence paths (files, Route lines, sample artifacts)
- Gaps and remediation recommendations

## Pass Criteria

- Required files/engines exist and are loadable
- Hard rules visible (no invented metrics/SLA/scripts/maturity as applicable)
- Cross-links to prior sprints without duplicating full knowledge
- Sample exercise (if run) follows Orchestrator gates

## Fail Criteria

- Missing engine/README for the capability
- Agent jumps gates (e.g., cases before analysis) in sample run
- Invented KPI/SLA/maturity/compliance attestation in sample output
- Broken canonical links or orphaned duplicates violating multi-lens policy

## Validation Steps

1. Confirm folder/engine entry exists.  
2. Spot-check hard rules in `skill.md` / engine file.  
3. Run sample input from golden datasets or industry benchmark (optional).  
4. Compare to expected outcomes below.  
5. Record score on the matching quality scorecard.

## Sample Inputs

- See [../golden-datasets/](../golden-datasets/README.md) and [../benchmarking/](../benchmarking/README.md).

## Sample Outputs

- Route line: `Primary: Sprint N · Support: … · Advisory: Yes/No`
- Analysis/design/advisory sections with **Assumptions** labeled
- No fabricated percentages

## Scoring Rules

| Result | Meaning |
|--------|---------|
| Pass | All pass criteria met with evidence |
| Partial | Core present; gaps documented |
| Fail | Missing capability or hard-rule breach |

Do **not** invent a numeric certification score here—roll up via [../quality-scorecards/](../quality-scorecards/README.md) using declared weights.

## Common Failures

- Treating pointer files as full content depth
- Skipping Enterprise Orchestrator on multi-intent asks
- Using 40% automation / defect counts without denominators as “green”

## Recommendations

- Remediate gaps before claiming Enterprise Certified
- Add golden dataset coverage for recurring failures
- Log improvement items in [../continuous-improvement/](../continuous-improvement/README.md)

## Related Documents

- [README.md](README.md)
- [../enterprise-validation-engine.md](../enterprise-validation-engine.md)
- Sprint engines via [../../skill.md](../../skill.md)

## Navigation

- **Up:** [README.md](README.md)
- **See also:** [../regression-suite/](../regression-suite/README.md)

## Future Enhancements

- Automate structural checks in CI
- Machine-readable JSON validation reports
"""


def main() -> None:
    # Engine + root README
    write(
        VAL / "enterprise-validation-engine.md",
        f"""---
title: Enterprise Validation & Certification Engine
version: {VER}
tags: [validation, sprint-11, engine]
---

# Enterprise Validation & Certification Engine

## Purpose

Validate, benchmark, certify, and continuously improve the Salesforce Quality Engineering framework (Sprints 1–10 + Orchestrator).

## Process

```
Repository & knowledge structural validation
    ↓
Sprint capability validations (2→10)
    ↓
Industry benchmarks + golden datasets
    ↓
Skill regression suite (S1–S10)
    ↓
Quality scorecards (weighted)
    ↓
Certification level (Bronze→Enterprise Certified)
    ↓
Continuous improvement backlog + Salesforce release readiness
```

## Hard rules

1. **Evidence required** — Pass/Partial/Fail with paths; no invented scores.  
2. Certification levels are **methodology**; do not claim Platinum/Enterprise Certified without a completed scorecard session.  
3. Reuse Sprints 1–10; do not duplicate knowledge bodies.  
4. Align ISTQB, TMMi, ITIL 4, Well-Architected, TOGAF governance themes, SAFe/Agile quality, Responsible AI.  
5. Seasonal Salesforce release reviews are **compatibility assessments**, not product legal advice.

## Capability index

| Area | Path |
|------|------|
| Repository | [repository-validation/](repository-validation/README.md) |
| Knowledge | [knowledge-validation/](knowledge-validation/README.md) |
| Requirement | [requirement-validation/](requirement-validation/README.md) |
| Test Design | [test-design-validation/](test-design-validation/README.md) |
| Documentation | [documentation-validation/](documentation-validation/README.md) |
| ADO | [ado-validation/](ado-validation/README.md) |
| Defect | [defect-validation/](defect-validation/README.md) |
| Automation | [automation-validation/](automation-validation/README.md) |
| Production | [production-validation/](production-validation/README.md) |
| Enterprise | [enterprise-validation/](enterprise-validation/README.md) |
| Benchmarking | [benchmarking/](benchmarking/README.md) |
| Certification | [certification/](certification/README.md) |
| Regression | [regression-suite/](regression-suite/README.md) |
| Scorecards | [quality-scorecards/](quality-scorecards/README.md) |
| Golden data | [golden-datasets/](golden-datasets/README.md) |
| Test scenarios | [test-scenarios/](test-scenarios/README.md) |
| Continuous improvement | [continuous-improvement/](continuous-improvement/README.md) |
| SF release readiness | [continuous-improvement/salesforce-release-readiness.md](continuous-improvement/salesforce-release-readiness.md) |

## Related

- [QE Brain (Sprint 1)](../brain/README.md)
- [Requirement Analysis (Sprint 2)](../knowledge/requirement-analysis.md)
- [Test Design (Sprint 3)](../knowledge/test-design-engine.md)
- [Platform 4A](../knowledge/platform/README.md) · [Enterprise 4B](../knowledge/clouds/README.md)
- [Documentation (Sprint 5)](../templates/README.md)
- [ADO (Sprint 6)](../ado/README.md)
- [Defect (Sprint 7)](../quality-intelligence/README.md)
- [Automation (Sprint 8)](../automation-intelligence/README.md)
- [Production (Sprint 9)](../production-support/README.md)
- [Advisory (Sprint 10)](../enterprise-quality/README.md)
- [Enterprise Orchestrator](../enterprise-orchestrator/README.md)
""",
    )

    write(
        VAL / "README.md",
        f"""---
title: Validation — Enterprise Framework Validation & Certification
version: {VER}
tags: [validation, sprint-11]
---

# Sprint 11 — Enterprise Framework Validation, Certification & Continuous Improvement

## Purpose

Ensure the Salesforce Quality Engineering framework (Sprints 1–10) is complete, accurate, consistent, reusable, scalable, maintainable, enterprise-ready, AI-ready, and consulting-ready.

## Sprint 11 Overview

| Capability | Path |
|------------|------|
| **Enterprise Validation Engine** | [enterprise-validation-engine.md](enterprise-validation-engine.md) |
| Repository → Enterprise validations | domain folders below |
| Benchmark Suite | [benchmarking/](benchmarking/README.md) |
| Golden Datasets | [golden-datasets/](golden-datasets/README.md) |
| Regression Suite | [regression-suite/](regression-suite/README.md) |
| Certification | [certification/](certification/README.md) |
| Quality Scorecards | [quality-scorecards/](quality-scorecards/README.md) |
| Continuous Improvement | [continuous-improvement/](continuous-improvement/README.md) |
| Validation test scenarios | [test-scenarios/](test-scenarios/README.md) |

## Validation Framework

Structural + behavioural validation of every sprint engine, Orchestrator routing, and advisory sink—using Pass/Partial/Fail with evidence.

## Certification Process

1. Run repository + capability validations.  
2. Execute benchmarks + regression suite samples.  
3. Complete weighted [quality-scorecards/](quality-scorecards/README.md).  
4. Map to [certification/](certification/README.md) level (Bronze→Enterprise Certified).  
5. Publish report; open CI backlog items.

## Benchmark Suite

Ten industries under [benchmarking/](benchmarking/README.md) with expected analysis, risks, documents, recommendations, and evaluation criteria.

## Regression Suite

Per-sprint suites under [regression-suite/](regression-suite/README.md) so new knowledge does not break prior capabilities.

## Quality Scorecards

Weighted scorecards with pass/fail thresholds and improvement actions—**no invented scores without a scored session**.

## Continuous Improvement

Gap detection, duplicate/outdated content, Salesforce seasonal release impact, enhancement backlog.

## Framework Governance

Owned by QE Practice Lead / CQO posture; changes versioned in module CHANGELOG; multi-lens policy enforced.

## Scope

**In:** Framework validation & certification methodology.  
**Out:** Claiming a specific repo is “Platinum” without evidence; live customer org testing; inventing regulatory attestations.

## Inputs / Outputs

- **Inputs:** This checkout, golden datasets, optional `outputs/` samples  
- **Outputs:** Scorecards, certification report, improvement backlog

## Navigation

- **Up:** [../README.md](../README.md) · [../skill.md](../skill.md)
- **BA validation (sibling):** [../../salesforce-business-analyst/validation/README.md](../../salesforce-business-analyst/validation/README.md)

## Related Documents

- [enterprise-validation-engine.md](enterprise-validation-engine.md)
- [docs/multi-lens-policy.md](../../docs/multi-lens-policy.md)
- Legacy flat stubs (pointers): `*-validation.md` at this folder root redirect into subfolders

## Future Enhancements

- CI publishing of validation JSON
- Auto link-check gate in PR
""",
    )

    # Capability folders
    for folder, title, purpose, articles in CAPABILITY_FOLDERS:
        child_table = "| Document | Focus |\n|----------|-------|\n" + "\n".join(
            f"| [{fn}]({fn}) | {t} |" for fn, t, _ in articles
        )
        write(
            VAL / folder / "README.md",
            folder_readme(
                title,
                purpose,
                f"- [../enterprise-validation-engine.md](../enterprise-validation-engine.md)\n- Prior sprint packs via [../../skill.md](../../skill.md)",
                f"## Available Documents\n\n{child_table}",
            ),
        )
        for fn, atitle, objective in articles:
            write(
                VAL / folder / fn,
                validation_article(atitle, objective, folder, atitle.lower()),
            )
        # pointer from old flat file if name matches
        flat = VAL / f"{folder.replace('-validation', '')}-validation.md" if False else None

    # Pointers for old flat v0.13 filenames
    flat_map = {
        "repository-validation.md": "repository-validation/README.md",
        "knowledge-validation.md": "knowledge-validation/README.md",
        "requirement-validation.md": "requirement-validation/README.md",
        "test-design-validation.md": "test-design-validation/README.md",
        "documentation-validation.md": "documentation-validation/README.md",
        "ado-validation.md": "ado-validation/README.md",
        "defect-validation.md": "defect-validation/README.md",
        "automation-validation.md": "automation-validation/README.md",
        "production-validation.md": "production-validation/README.md",
        "advisory-validation.md": "enterprise-validation/README.md",
        "benchmark-scorecard.md": "quality-scorecards/overall-framework.md",
        "regression-suite.md": "regression-suite/README.md",
        "validation-checklist.md": "test-scenarios/master-validation-checklist.md",
    }
    for old, new in flat_map.items():
        write(
            VAL / old,
            f"""---
title: Pointer — {old}
type: pointer
version: {VER}
---

# Moved (Sprint 11)

**Canonical:** [{new}]({new})
""",
        )

    # Benchmarking
    write(
        VAL / "benchmarking" / "README.md",
        folder_readme(
            "Benchmark Suite",
            "Industry benchmark scenarios for framework behavioural validation.",
            "- [../golden-datasets/](../golden-datasets/README.md)\n- [../../scenarios/README.md](../../scenarios/README.md)",
            "## Industries\n\n"
            + "\n".join(f"- [{label}]({key}/README.md)" for key, label, _ in INDUSTRIES),
        ),
    )
    for key, label, ctx in INDUSTRIES:
        write(
            VAL / "benchmarking" / key / "README.md",
            f"""---
title: Benchmark — {label}
version: {VER}
tags: [benchmark, sprint-11, {key}]
---

# Benchmark — {label}

## Purpose

Benchmark QE framework behaviour on a synthetic **{label}** program.

## Business Context

{ctx}. Anonymized; no client PII. Align BA scenarios when present under `salesforce-business-analyst/scenarios/`.

## Requirements (seed)

Provide an incomplete story such as: "User must complete a critical {label.lower()} process in Salesforce."

## Expected Analysis

- Sprint 2 gaps, personas, Salesforce component scan, risks, clarification questions
- No detailed test cases at analysis-only stage

## Expected Risks

- Permission/FLS, integration handoffs, data integrity, release/UAT timing (as applicable)

## Expected Documents

- Optional Test Strategy (assumptions labeled) after analysis
- Scenario objectives (Sprint 3) when requested
- Not: invented BRD regulatory sections

## Expected Recommendations

- Orchestrator Route line; Hold/Escalate if production symptoms introduced

## Expected Deliverables

- Analysis memo · optional strategy · scenario matrix · (if asked) health RAG from synthetic metrics

## Evaluation Criteria

| Criterion | Pass |
|-----------|------|
| Gate order | Analysis before cases |
| Anti-hallucination | No invented SLA/maturity/% |
| Industry reuse | Links BA/QE industry knowledge; no duplication |
| Advisory | Sprint 10 only when exec/health asked |

## Related Documents

- [../README.md](../README.md)
- [../../enterprise-orchestrator/](../../../enterprise-orchestrator/README.md)

## Navigation

- **Up:** [../README.md](../README.md)
""",
        )

    # Move/repurpose end-to-end-scenarios → pointer to benchmarking + test-scenarios
    write(
        VAL / "end-to-end-scenarios" / "README.md",
        f"""---
title: E2E Scenarios (Legacy Path)
type: pointer
version: {VER}
---

# End-to-End Scenarios (Legacy Path)

**Canonical benchmarks:** [../benchmarking/](../benchmarking/README.md)  
**Validation scripts:** [../test-scenarios/](../test-scenarios/README.md)

Industry folders under this path remain as thin redirects where present.
""",
    )

    # Golden datasets
    write(
        VAL / "golden-datasets" / "README.md",
        folder_readme(
            "Golden Datasets",
            "Reusable synthetic datasets that anchor skill regression and benchmarks.",
            "- [../regression-suite/](../regression-suite/README.md)\n- [../benchmarking/](../benchmarking/README.md)",
            "## Datasets\n\n"
            + "\n".join(f"- [{t}]({k}/README.md)" for k, t, _ in GOLDEN),
        ),
    )
    for key, title, desc in GOLDEN:
        write(
            VAL / "golden-datasets" / key / "README.md",
            f"""---
title: Golden Dataset — {title}
version: {VER}
tags: [golden-dataset, sprint-11]
---

# Golden Dataset — {title}

## Purpose

{desc} for repeatable validation (synthetic only).

## Scope

**In:** Anonymized examples and expected behavioural outcomes.  
**Out:** Real customer data; production credentials.

## Sample dataset

| ID | Input summary | Expected behaviour |
|----|---------------|--------------------|
| GD-{key[:3].upper()}-01 | Minimal / incomplete input | Clarifying questions; assumptions labeled |
| GD-{key[:3].upper()}-02 | Complete enough input | Full capability output without invented metrics |
| GD-{key[:3].upper()}-03 | Hostile / gate-skip ask | Gate enforced or explicit waiver |

## Usage

1. Load matching sprint engine.  
2. Paste sample.  
3. Compare to expected behaviour.  
4. Log on regression suite / scorecard.

## Related Documents

- [../README.md](../README.md)
- [../../regression-suite/](../../regression-suite/README.md)

## Navigation

- **Up:** [../README.md](../README.md)
""",
        )
        write(
            VAL / "golden-datasets" / key / "samples.md",
            f"""---
title: Samples — {title}
version: {VER}
---

# Samples — {title}

## GD sample A (incomplete)

```
[Incomplete {title} request — details TBD]
```

**Expect:** Questions, assumptions, no silent invention.

## GD sample B (structured)

```
Context: Synthetic enterprise Salesforce program
Ask: Exercise {title} capability with explicit assumptions listed by the agent
Constraints: Do not invent KPI %, SLA, or compliance certifications
```

**Expect:** Structured output per engine; facts vs assumptions separated.
""",
        )

    # Regression suite per sprint
    write(
        VAL / "regression-suite" / "README.md",
        folder_readme(
            "Framework Regression Suite",
            "Ensure prior sprint capabilities still work after framework changes.",
            "- [../golden-datasets/](../golden-datasets/README.md)\n- [../enterprise-validation-engine.md](../enterprise-validation-engine.md)",
            "## Suites\n\n"
            + "\n".join(
                f"- [Sprint {s}](sprint-{s}/README.md)"
                for s in ["1", "2", "3", "4a", "4b", "5", "6", "7", "8", "9", "10"]
            ),
        ),
    )
    sprint_meta = [
        ("1", "QE Brain", "Load brain modules; consulting posture"),
        ("2", "Requirement Analysis", "Incomplete story → analysis only"),
        ("3", "Test Design", "Scenarios/coverage before cases"),
        ("4a", "Platform Foundation", "Record Types / security impact language"),
        ("4b", "Enterprise Knowledge", "Cloud/integration awareness"),
        ("5", "Documentation", "Test Strategy template sections"),
        ("6", "ADO", "Hierarchy guidance; no invented API publish"),
        ("7", "Defect Intelligence", "No invented leakage %; Rule IDs when applicable"),
        ("8", "Automation Intelligence", "No full scripts; Playwright-first"),
        ("9", "Production Support", "Sev1 first; no invented SLA"),
        ("10", "Enterprise Advisory", "RAG health; Hold/Escalate; no fake maturity"),
    ]
    for sid, name, expect in sprint_meta:
        write(
            VAL / "regression-suite" / f"sprint-{sid}" / "README.md",
            f"""---
title: Regression Suite — Sprint {sid.upper()} ({name})
version: {VER}
tags: [regression, sprint-11]
---

# Regression Suite — Sprint {sid.upper()} — {name}

## Purpose

Prove Sprint {sid.upper()} capability still behaves after framework updates.

## Scope

Behavioural checks for **{name}**.

## Inputs

- Golden datasets · prompts in [cases.md](cases.md)

## Outputs

- Pass/Partial/Fail log

## Cases

See [cases.md](cases.md).

## Pass / Fail

| Pass | Fail |
|------|------|
| {expect} | Gate skipped or metrics invented |

## Navigation

- **Up:** [../README.md](../README.md)
""",
        )
        write(
            VAL / "regression-suite" / f"sprint-{sid}" / "cases.md",
            f"""---
title: Cases — Sprint {sid}
version: {VER}
---

# Cases — Sprint {sid.upper()}

| ID | Prompt intent | Expect |
|----|---------------|--------|
| S{sid.upper()}-R01 | Smoke ask for {name} | {expect} |
| S{sid.upper()}-R02 | Gate-pressure ask | Hard rule held |
| S{sid.upper()}-R03 | Cross-link check | Prior sprint reused, not duplicated |

## Execution log

| ID | Version | Result | Notes |
|----|---------|--------|-------|
| S{sid.upper()}-R01 | | | |
| S{sid.upper()}-R02 | | | |
| S{sid.upper()}-R03 | | | |
""",
        )

    # Certification
    write(
        VAL / "certification" / "README.md",
        folder_readme(
            "Certification Framework",
            "Define Bronze→Enterprise Certified criteria and report generation.",
            "- [../quality-scorecards/](../quality-scorecards/README.md)\n- [levels.md](levels.md)\n- [certification-report-template.md](certification-report-template.md)",
            "## Documents\n\n- [levels.md](levels.md)\n- [criteria.md](criteria.md)\n- [certification-report-template.md](certification-report-template.md)",
        ),
    )
    write(
        VAL / "certification" / "levels.md",
        f"""---
title: Certification Levels
version: {VER}
---

# Certification Levels

| Level | Intent | Indicative bar (methodology) |
|-------|--------|------------------------------|
| **Bronze** | Core structure present | Repository + Brain + S2/S3 engines Pass |
| **Silver** | Delivery docs + ADO | Bronze + S5/S6 Pass or Partial with plan |
| **Gold** | Intelligence layer | Silver + S7/S8 Pass |
| **Platinum** | Ops + Advisory | Gold + S9/S10 + Orchestrator Pass |
| **Enterprise Certified** | Full governance | Platinum + benchmarks (≥3 industries) + regression sample + CI backlog process |

**Rule:** Levels are awarded only after a scored [quality-scorecards/](../quality-scorecards/README.md) session with evidence. Never self-attest without the report.
""",
    )
    write(
        VAL / "certification" / "criteria.md",
        f"""---
title: Certification Evaluation Criteria
version: {VER}
---

# Certification Evaluation Criteria

| Dimension | What is evaluated |
|-----------|-------------------|
| Knowledge | 4A/4B completeness, multi-lens policy |
| Reasoning | Orchestrator gates, analysis-before-cases |
| Consistency | Naming, versioning, pointers |
| Documentation | Templates/generators usable |
| Traceability | IDs / Related links |
| Automation | Strategy/review without script dumps |
| Production Readiness | Sev1-first, no invented SLA |
| Governance | Advisory decisions + CI backlog |
| Quality | Scorecard discipline |
| Overall Score | Weighted rollup from scorecards |

Weights live in [../quality-scorecards/overall-framework.md](../quality-scorecards/overall-framework.md).
""",
    )
    write(
        VAL / "certification" / "certification-report-template.md",
        f"""---
title: Certification Report Template
version: {VER}
type: template
---

# QE Framework Certification Report

| Field | Value |
|-------|--------|
| Date | |
| Assessor | |
| Repo version / commit | |
| Module version | |
| Recommended level | Bronze / Silver / Gold / Platinum / Enterprise Certified / Not ready |

## Executive summary

[Evidence-based narrative — no invented scores]

## Scorecard rollup

| Area | Weight | Result | Notes |
|------|--------|--------|-------|
| Repository | | | |
| … | | | |
| Overall | 100% | | |

## Benchmarks executed

| Industry | Result |
|----------|--------|
| | |

## Regression suite sample

| Sprint | Result |
|--------|--------|
| | |

## Gaps & improvement backlog

| ID | Gap | Priority | Owner |
|----|-----|----------|-------|
| | | | |

## Sign-off

| Role | Name | Date |
|------|------|------|
| CQO / QE Practice Lead | | |
| Assessor | | |
""",
    )

    # Quality scorecards
    write(
        VAL / "quality-scorecards" / "README.md",
        folder_readme(
            "Quality Scorecards",
            "Weighted scorecards with pass/fail thresholds and improvement actions.",
            "- [../certification/](../certification/README.md)\n- [overall-framework.md](overall-framework.md)",
            "## Scorecards\n\n"
            + "\n".join(f"- [{t}]({k}.md) (weight {w}%)" for k, t, w in SCORECARDS),
        ),
    )
    for key, title, weight in SCORECARDS:
        write(
            VAL / "quality-scorecards" / f"{key}.md",
            f"""---
title: Scorecard — {title}
version: {VER}
tags: [scorecard, sprint-11]
---

# Scorecard — {title}

## Purpose

Score **{title}** readiness for framework certification.

## Weight in overall framework

**{weight}%** (see [overall-framework.md](overall-framework.md) for rollup).

## Dimensions (score 0–2 each: Fail=0, Partial=1, Pass=2)

| Dimension | 0 | 1 | 2 | Score | Evidence |
|-----------|---|---|---|-------|----------|
| Completeness | Missing | Partial | Complete | | |
| Accuracy / hard rules | Breach | Minor gaps | Clean | | |
| Consistency | Broken links/dupes | Some drift | Consistent | | |
| Usability for consulting | Unusable | Usable with gaps | Demo-ready | | |

## Thresholds

| Band | Rule |
|------|------|
| Pass | Average ≥ 1.5 and no Fail on hard rules |
| Partial | Average ≥ 1.0 |
| Fail | Average < 1.0 or hard-rule Fail |

## Improvement actions

| Gap | Action | Owner | Target |
|-----|--------|-------|--------|
| | | | |

## Related

- [README.md](README.md)
- Matching validation folder under `../`
""",
        )

    write(
        VAL / "quality-scorecards" / "overall-framework.md",
        f"""---
title: Overall Framework Scorecard
version: {VER}
---

# Overall Framework Scorecard

## Purpose

Roll up weighted area scorecards into a certification recommendation.

## Weights

| Area | Weight % |
|------|----------|
"""
        + "\n".join(f"| {t} | {w} |" for _, t, w in SCORECARDS)
        + f"""

**Total:** 100%

## Rollup method

1. Complete each area scorecard (Pass/Partial/Fail).  
2. Map Pass=2, Partial=1, Fail=0; compute weighted average.  
3. Map to certification level per [../certification/levels.md](../certification/levels.md).  
4. **Do not** invent a percentage without completing step 1–2.

## Session log

| Date | Weighted result | Level | Assessor |
|------|-----------------|-------|----------|
| | | | |
""",
    )

    # Test scenarios for validation
    write(
        VAL / "test-scenarios" / "README.md",
        folder_readme(
            "Validation Test Scenarios",
            "Executable validation scenarios and master checklist for Sprint 11.",
            "- [master-validation-checklist.md](master-validation-checklist.md)\n- [../benchmarking/](../benchmarking/README.md)",
            "## Documents\n\n- [master-validation-checklist.md](master-validation-checklist.md)\n- [orchestrator-routing-scenarios.md](orchestrator-routing-scenarios.md)",
        ),
    )
    write(
        VAL / "test-scenarios" / "master-validation-checklist.md",
        f"""---
title: Master Validation Checklist
version: {VER}
---

# Master Validation Checklist

- [ ] Repository validation suite
- [ ] Knowledge validation suite
- [ ] Requirement → Enterprise capability validations
- [ ] ≥1 industry benchmark
- [ ] Golden dataset smoke (3 samples)
- [ ] Regression suites sampled (S2, S8, S9, S10 minimum)
- [ ] Quality scorecards completed
- [ ] Certification report drafted (level TBD until scored)
- [ ] Continuous improvement backlog updated
""",
    )
    write(
        VAL / "test-scenarios" / "orchestrator-routing-scenarios.md",
        f"""---
title: Orchestrator Routing Scenarios
version: {VER}
---

# Orchestrator Routing Scenarios

| ID | Ask | Expect primary |
|----|-----|----------------|
| ORCH-01 | Incomplete story | Sprint 2 |
| ORCH-02 | Generate scenarios | Sprint 3 (+2 if needed) |
| ORCH-03 | Full Playwright script | Sprint 8 design only |
| ORCH-04 | Production users cannot… | Sprint 9 |
| ORCH-05 | Assess project health | Sprint 10 |
| ORCH-06 | Validate the QE module | validation/ Sprint 11 |
""",
    )

    # Continuous improvement + SF release readiness
    write(
        VAL / "continuous-improvement" / "README.md",
        folder_readme(
            "Continuous Improvement",
            "Detect gaps, duplicates, outdated content; track Salesforce release impacts; maintain improvement backlog.",
            "- [improvement-backlog.md](improvement-backlog.md)\n- [salesforce-release-readiness.md](salesforce-release-readiness.md)\n- [knowledge-lifecycle.md](knowledge-lifecycle.md)",
            "## Documents\n\n- [gap-detection.md](gap-detection.md)\n- [duplicate-detection.md](duplicate-detection.md)\n- [knowledge-lifecycle.md](knowledge-lifecycle.md)\n- [salesforce-release-readiness.md](salesforce-release-readiness.md)\n- [improvement-backlog.md](improvement-backlog.md)\n- [version-history-practice.md](version-history-practice.md)",
        ),
    )
    for fn, title, purpose in [
        ("gap-detection.md", "Identify Knowledge Gaps", "Find missing engines, READMEs, industries, or gates."),
        ("duplicate-detection.md", "Detect Duplicate Content", "Enforce multi-lens pointers vs full copies."),
        ("knowledge-lifecycle.md", "Knowledge Lifecycle Management", "Review cycle, owners, deprecate/archive rules."),
        ("improvement-backlog.md", "Improvement Backlog", "Prioritized framework enhancements."),
        ("version-history-practice.md", "Version History Practice", "CHANGELOG/skill version discipline."),
    ]:
        write(
            VAL / "continuous-improvement" / fn,
            f"""---
title: {title}
version: {VER}
tags: [continuous-improvement, sprint-11]
---

# {title}

## Purpose

{purpose}

## Validation Objective

Ensure the framework improves continuously without silent drift.

## Inputs

- Validation/scorecard results · link scans · Salesforce release notes (org-confirmed)

## Expected Outputs

- Backlog items with priority and owner
- Restructure / docs / deprecation recommendations

## Pass Criteria

- Gaps logged with evidence
- No silent duplicate proliferation
- Version history updated on material change

## Fail Criteria

- Known gaps ignored across two validation cycles
- Full-content duplicates reintroduced against multi-lens policy

## Validation Steps

1. Review latest scorecards and link scan.  
2. List gaps/duplicates/outdated candidates.  
3. File backlog items.  
4. Track to closure in CHANGELOG.

## Sample Inputs / Outputs

- Input: “97 duplicate basenames” audit → Output: pointer migration backlog  
- Input: Winter release note on Agentforce → Output: release readiness assessment entry

## Scoring Rules

Track backlog burn-down qualitatively; do not invent velocity metrics.

## Common Failures

- Editing knowledge without version bump
- Archiving without pointer for old links

## Recommendations

- Run CI after each sprint pack change
- Tie SF seasonal reviews to [salesforce-release-readiness.md](salesforce-release-readiness.md)

## Related Documents

- [README.md](README.md)
- [../../CHANGELOG.md](../../CHANGELOG.md)

## Navigation

- **Up:** [README.md](README.md)

## Future Enhancements

- Automated stale-file detector by `last_updated`
""",
        )

    write(
        VAL / "continuous-improvement" / "salesforce-release-readiness.md",
        f"""---
title: Salesforce Release Readiness (Framework Compatibility)
version: {VER}
tags: [continuous-improvement, sprint-11, salesforce-release]
---

# Salesforce Release Readiness — Framework Compatibility

## Purpose

Repeatable process to assess QE framework compatibility with Salesforce seasonal releases and product changes.

## Validation Objective

Ensure knowledge, scenarios, and advisory guidance stay aligned with Spring / Summer / Winter releases, new clouds, Agentforce, OmniStudio, Data Cloud, and platform deprecations—**without inventing product behaviour**.

## Inputs

- Salesforce Release Notes (edition-confirmed)
- Current `knowledge/clouds/`, Agentforce/OmniStudio/Data Cloud articles
- Validation scorecards

## Expected Outputs

- Compatibility assessment (Impacts / No impact / TBC)
- Update backlog for affected articles
- Temporary “verify in org” flags where behaviour is edition-specific

## Pass Criteria

- Assessment recorded for the release cycle
- Impacted articles listed with owners
- No unverified feature claims added to knowledge

## Fail Criteria

- Framework claims new product features without citation
- Deprecations ignored after two cycles

## Validation Steps (repeatable)

1. **Identify cycle** — Spring / Summer / Winter (year).  
2. **Scan notes** for Agentforce, OmniStudio, Data Cloud, platform deprecations, new clouds.  
3. **Map to framework paths** — clouds/, automation-intelligence/, enterprise-quality/salesforce/, production-support/.  
4. **Classify** — Impact / Watch / N/A.  
5. **Backlog** updates; bump versions on changed articles.  
6. **Regression** — run S4B + S8 + S10 sample cases.  
7. **Record** in session table below.

## Sample Inputs

- “Winter ’XX — Agentforce topic X changed” (cite note URL/title in real assessments)

## Sample Outputs

| Area | Impact | Action |
|------|--------|--------|
| Agentforce knowledge | Watch | Re-verify prompts; mark TBC until org-confirmed |
| Deprecated API used in examples | Impact | Update example; add deprecation note |

## Scoring Rules

Compatibility assessment is Pass if cycle reviewed and backlog filed—not if “100% compatible” is claimed without evidence.

## Common Failures

- Copying marketing claims into knowledge as facts
- Skipping Experience/Industry cloud impacts

## Recommendations

- Schedule assessment each seasonal release
- Prefer “overview / verify in target org” language for new features

## Related Documents

- [README.md](README.md)
- [../../knowledge/clouds/](../../knowledge/clouds/README.md)
- [improvement-backlog.md](improvement-backlog.md)

## Navigation

- **Up:** [README.md](README.md)

## Future Enhancements

- Checklist template per cloud product line
""",
    )

    # improvement backlog starter
    write(
        VAL / "continuous-improvement" / "improvement-backlog.md",
        f"""---
title: Framework Improvement Backlog
version: {VER}
---

# Framework Improvement Backlog

| ID | Item | Source | Priority | Status |
|----|------|--------|----------|--------|
| CI-001 | CI link-check on PR | Sprint 11 | High | Proposed |
| CI-002 | JSON export for scorecards | Sprint 11 | Medium | Proposed |
| CI-003 | Expand golden datasets with fixtures | Sprint 11 | Medium | Proposed |
| CI-004 | Seasonal SF release assessment calendar | Sprint 11 | High | Proposed |
| CI-005 | Optional Regression Intelligence deep-pack | Roadmap | Low | Proposed |
""",
    )

    print(f"DONE Sprint 11 validation pack at {VAL} version {VER}")


if __name__ == "__main__":
    main()
