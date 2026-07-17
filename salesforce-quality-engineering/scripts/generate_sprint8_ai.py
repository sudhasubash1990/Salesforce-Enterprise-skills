#!/usr/bin/env python3
"""Generate Sprint 8 — Automation Intelligence & Test Automation Architecture."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AI = ROOT / "automation-intelligence"
VERSION = "0.10.0"
DATE = "2026-07-18"
SPRINT = "Sprint 8"


def cross(prefix: str) -> list[str]:
    return [
        f"[QE Brain (Sprint 1)]({prefix}/brain/README.md)",
        f"[Requirement Analysis (Sprint 2)]({prefix}/knowledge/requirement-analysis.md)",
        f"[Test Design Engine (Sprint 3)]({prefix}/knowledge/test-design-engine.md)",
        f"[Platform Foundation 4A]({prefix}/knowledge/platform/README.md)",
        f"[Enterprise Knowledge 4B]({prefix}/knowledge/clouds/README.md)",
        f"[Documentation Generator (Sprint 5)]({prefix}/templates/README.md)",
        f"[ADO Delivery Intelligence (Sprint 6)]({prefix}/ado/README.md)",
        f"[Defect Intelligence (Sprint 7)]({prefix}/quality-intelligence/README.md)",
        f"[QI Automation Stability Rules]({prefix}/quality-intelligence/rules/automation-stability-rules.md)",
    ]


CROSS = cross("../..")
CROSS_ROOT = cross("..")


def titleize(slug: str) -> str:
    special = {
        "ci-cd": "CI/CD",
        "api-testing": "API Testing",
        "bdd-framework": "BDD Framework",
        "page-object-model": "Page Object Model",
        "screenplay-pattern": "Screenplay Pattern",
        "component-object-model": "Component Object Model",
        "rest-assured": "REST Assured",
        "webdriverio": "WebdriverIO",
        "oauth": "OAuth",
        "jwt": "JWT",
        "roi": "ROI",
        "pom": "Page Object Model",
        "github-actions": "GitHub Actions",
        "azure-devops-pipelines": "Azure DevOps Pipelines",
        "named-credentials": "Named Credentials",
        "shift-left-testing": "Shift Left Testing",
        "shift-right-testing": "Shift Right Testing",
        "agentforce": "Agentforce",
        "omnistudio": "OmniStudio",
        "experience-cloud": "Experience Cloud",
        "utilities-cloud": "Utilities Cloud",
    }
    return special.get(slug, slug.replace("-", " ").title())


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {i}" for i in items)


def folder_readme(
    folder: str,
    title: str,
    purpose: str,
    scope: str,
    articles: list[tuple[str, str]],
    prev: str,
    nxt: str,
) -> str:
    rows = "\n".join(f"| [{titleize(s)}]({s}.md) | {b} |" for s, b in articles)
    return f"""---
title: {title} — README
module: Salesforce Quality Engineering
category: Automation Intelligence
document_type: Guide
version: {VERSION}
review_status: Draft
owner: QE Practice Lead
created_date: {DATE}
last_updated: {DATE}
tags: [automation-intelligence, sprint-8, {folder}]
---

# {title}

## Purpose

{purpose}

## Scope

{scope}

**Hard rule:** Do **not** generate full automation scripts in this sprint—architecture, strategy, and decisions only.

## Available Documents

| Document | Focus |
|----------|-------|
{rows}

## Navigation

- **Previous:** [{prev}]({prev})
- **Next:** [{nxt}]({nxt})
- **See Also:** [../README.md](../README.md)

## Related Documents

{bullets(CROSS)}
"""


def article(folder: str, slug: str, meta: dict, nav: dict) -> str:
    title = meta.get("title") or titleize(slug)
    purpose = meta["purpose"]
    related = meta.get("related", []) + CROSS + [
        "[README.md](README.md)",
        "[../README.md](../README.md)",
        "[../automation-decision-engine.md](../automation-decision-engine.md)",
    ]

    def sec(key: str, heading: str, default: list[str] | str) -> str:
        val = meta.get(key, default)
        body = val if isinstance(val, str) else bullets(val)
        return f"## {heading}\n\n{body}\n"

    return (
        f"---\ntitle: {title}\nmodule: Salesforce Quality Engineering\n"
        f"category: Automation Intelligence\ndocument_type: Knowledge Article\n"
        f"version: {VERSION}\nreview_status: Draft\nowner: QE Practice Lead\n"
        f"created_date: {DATE}\nlast_updated: {DATE}\n"
        f"tags: [automation-intelligence, sprint-8, {folder}]\n"
        f"keywords: [{slug}, automation-strategy, test-automation]\n---\n\n"
        f"# {title}\n\n"
        f"**Scope:** {SPRINT} Automation Intelligence — strategy and architecture advisory. "
        f"**No full script generation.** Playwright-first, framework-agnostic. "
        f"Reuse Sprint 3 automation candidates and Sprint 7 flaky-test rules.\n\n"
        f"**Version:** {VERSION}\n\n---\n\n"
        + sec("purpose", "Purpose", purpose)
        + sec(
            "business_context",
            "Business Context",
            meta.get(
                "business_context",
                [
                    "Automation exists to protect business outcomes and accelerate safe delivery—not to maximize script count.",
                    "Enterprise Salesforce programs need maintainable, CI-ready automation with clear ownership.",
                ],
            ),
        )
        + sec(
            "architecture",
            "Architecture",
            meta.get(
                "architecture",
                [
                    f"{title} fits a layered automation architecture: tests → abstractions → drivers/clients → CI/CD → reporting.",
                    "Prefer stable APIs/service checks under a thin UI smoke layer (automation pyramid).",
                ],
            ),
        )
        + sec(
            "decision_criteria",
            "Decision Criteria",
            meta.get(
                "decision_criteria",
                [
                    "Business criticality and regression frequency",
                    "UI volatility vs API stability",
                    "Data/environment feasibility",
                    "Maintenance cost vs defect risk avoided",
                    "CI/CD execution time budget",
                ],
            ),
        )
        + sec(
            "advantages",
            "Advantages",
            meta.get(
                "advantages",
                [
                    "Improves repeatability and release confidence when applied to stable, high-value paths",
                    "Enables continuous testing feedback in pipelines",
                ],
            ),
        )
        + sec(
            "limitations",
            "Limitations",
            meta.get(
                "limitations",
                [
                    "Poor candidate selection creates flaky suites and false confidence",
                    "Does not replace exploratory, usability, or ambiguous-requirement testing",
                ],
            ),
        )
        + sec(
            "practices",
            "Best Practices",
            meta.get(
                "practices",
                [
                    "Automate after path stability and oracle clarity",
                    "Design for parallel, idempotent, environment-aware execution",
                    "Quarantine flaky tests; protect CI signal quality",
                    "Document ownership, naming, and review gates",
                ],
            ),
        )
        + sec(
            "salesforce",
            "Salesforce Considerations",
            meta.get(
                "salesforce",
                [
                    "Lightning DOM, dynamic IDs, and shadow boundaries increase UI brittleness—prefer roles/labels/test ids where controllable",
                    "Validate Flows, validation rules, sharing, and integrations with layered checks (API + targeted UI)",
                    "Respect governor limits, async (batch/platform events), and multi-persona security",
                ],
            ),
        )
        + sec(
            "automation_considerations",
            "Automation Considerations",
            meta.get(
                "automation_considerations",
                [
                    "No full script generation in Sprint 8—produce design decisions, structure, and CI strategy",
                    "Estimate effort/ROI with assumptions; delivery team confirms",
                    "Cross-link Sprint 7 automation stability rules when flake signals appear",
                ],
            ),
        )
        + sec(
            "pitfalls",
            "Common Pitfalls",
            meta.get(
                "pitfalls",
                [
                    "Automating unstable UIs before API coverage",
                    "Hard-coding secrets or org-specific IDs",
                    "100% UI coverage goals without pyramid discipline",
                    "Skipping test data cleanup and environment isolation",
                ],
            ),
        )
        + sec(
            "examples",
            "Examples",
            meta.get(
                "examples",
                [
                    "Illustrative: smoke login + create Case via API + UI assert status — not a full script dump",
                    "Decision example: high-churn Lightning page → keep manual exploratory; automate service assertions",
                ],
            ),
        )
        + sec(
            "interview",
            "Interview Questions",
            meta.get(
                "interview",
                [
                    f"When would you apply {title} on a Salesforce program?",
                    "How do you balance Playwright-first guidance with an existing Selenium estate?",
                    "What signals tell you automation is not yet appropriate?",
                ],
            ),
        )
        + "## Related Documents\n\n"
        + bullets(related)
        + "\n\n## Navigation\n\n"
        + f"- **Previous:** [{nav['prev_title']}]({nav['prev']})\n"
        + f"- **Next:** [{nav['next_title']}]({nav['next']})\n"
        + "- **See Also:** [../README.md](../README.md)\n\n"
        + "## Future Enhancements\n\n"
        + bullets(
            meta.get(
                "future",
                [
                    "Program-specific framework blueprints under outputs/<project>/",
                    "Optional script templates in a later sprint if explicitly requested",
                ],
            )
        )
        + "\n"
    )


def tool_meta(name: str, strengths: list[str], weaknesses: list[str], sf: str, usage: str) -> dict:
    return {
        "purpose": f"Compare {name} as an automation option for enterprise Salesforce programs.",
        "architecture": [
            f"{name} sits in the tool layer of the automation stack; selection depends on team skills, UI vs API mix, and CI constraints.",
            "Remain framework-agnostic at strategy level; Playwright-first is a default recommendation, not a mandate.",
        ],
        "decision_criteria": [
            "Salesforce UI suitability and locator resilience",
            "API testing support",
            "CI/CD and parallel execution maturity",
            "Learning curve and hiring market",
            "Maintenance model and community/vendor support",
        ],
        "advantages": strengths,
        "limitations": weaknesses,
        "salesforce": [sf, "Validate against Lightning and Experience Cloud constraints before committing."],
        "practices": [
            usage,
            "Pilot on 1–2 critical journeys before estate-wide adoption",
            "Define POM/COM or Screenplay conventions before scale",
        ],
        "examples": [
            f"Recommend {name} when {usage.lower()}",
            "Document migration risks if replacing an existing framework",
        ],
    }


FOLDERS: dict[str, dict] = {
    "automation-strategy": {
        "title": "Automation Strategy",
        "purpose": "Define when, what, and why to automate across Salesforce delivery.",
        "scope": "Pyramid, ROI, feasibility, prioritization, shift-left/right, continuous testing, maturity.",
        "docs": [
            ("automation-pyramid", "UI thin / API thick layering"),
            ("automation-testing-strategy", "Program automation strategy"),
            ("risk-based-automation", "Automate by risk"),
            ("regression-automation", "Regression pack automation"),
            ("smoke-automation", "Build/deploy smoke"),
            ("sanity-automation", "Focused sanity packs"),
            ("api-automation", "Service-layer automation strategy"),
            ("ui-automation", "UI automation strategy"),
            ("service-layer-testing", "Service/API middle layer"),
            ("automation-roi", "ROI model"),
            ("automation-feasibility", "Feasibility assessment"),
            ("automation-prioritization", "Backlog prioritization"),
            ("shift-left-testing", "Earlier quality feedback"),
            ("shift-right-testing", "Prod validation / monitoring loops"),
            ("continuous-testing", "Pipeline continuous testing"),
            ("automation-maturity-model", "Maturity stages"),
        ],
    },
    "framework-design": {
        "title": "Framework Design",
        "purpose": "Design maintainable, scalable enterprise automation frameworks.",
        "scope": "Architecture patterns, utilities, config, secrets, parallel/cross-browser—not script dumps.",
        "docs": [
            ("layered-architecture", "Layered test architecture"),
            ("page-object-model", "Page Object Model"),
            ("screenplay-pattern", "Screenplay pattern"),
            ("component-object-model", "Component Object Model"),
            ("data-driven-framework", "Data-driven design"),
            ("keyword-driven-framework", "Keyword-driven design"),
            ("hybrid-framework", "Hybrid frameworks"),
            ("bdd-framework", "BDD-oriented automation"),
            ("reusable-utilities", "Shared utilities"),
            ("logging", "Logging standards"),
            ("reporting", "Reporting design"),
            ("error-handling", "Error handling"),
            ("retry-logic", "Retry strategies"),
            ("parallel-execution", "Parallel design"),
            ("cross-browser-execution", "Cross-browser strategy"),
            ("configuration-management", "Config management"),
            ("environment-management", "Environment management"),
            ("secrets-management", "Secrets management"),
            ("versioning", "Framework versioning"),
            ("framework-scalability", "Scale patterns"),
        ],
    },
    "framework-comparison": {
        "title": "Framework Comparison",
        "purpose": "Select tools with transparent strengths, weaknesses, and Salesforce fit.",
        "scope": "Playwright, Selenium, Cypress, Robot, WebdriverIO, Appium, REST Assured, Postman, Karate.",
        "docs": [
            ("playwright", "Playwright comparison"),
            ("selenium", "Selenium comparison"),
            ("cypress", "Cypress comparison"),
            ("robot-framework", "Robot Framework comparison"),
            ("webdriverio", "WebdriverIO comparison"),
            ("appium", "Appium comparison"),
            ("rest-assured", "REST Assured comparison"),
            ("postman", "Postman comparison"),
            ("karate", "Karate comparison"),
        ],
    },
    "automation-patterns": {
        "title": "Automation Patterns",
        "purpose": "Reusable automation design patterns for Salesforce programs.",
        "scope": "Stability, isolation, oracle, wait, fixture, and anti-flake patterns.",
        "docs": [
            ("stable-locator-patterns", "Locator stability"),
            ("fixture-and-setup-patterns", "Fixtures and setup"),
            ("test-isolation-patterns", "Isolation and cleanup"),
            ("oracle-and-assertion-patterns", "Oracles and assertions"),
            ("wait-and-sync-patterns", "Waits and synchronization"),
            ("anti-flake-patterns", "Anti-flake patterns"),
            ("persona-security-patterns", "Persona/security automation"),
            ("async-event-patterns", "Batch/events patterns"),
        ],
    },
    "playwright": {
        "title": "Playwright Knowledge",
        "purpose": "Enterprise Playwright guidance for Salesforce (design-level, not full scripts).",
        "scope": "Architecture, locators, fixtures, POM, API, auth, visual, CI/CD, SF practices, failures.",
        "docs": [
            ("architecture", "Playwright architecture"),
            ("locators", "Locator strategy"),
            ("fixtures", "Fixtures"),
            ("page-objects", "Page objects with Playwright"),
            ("api-testing", "API testing in Playwright"),
            ("authentication", "Auth patterns"),
            ("storage-state", "Storage state"),
            ("visual-testing", "Visual testing"),
            ("tracing", "Tracing"),
            ("reporting", "Reporting"),
            ("retry-strategy", "Retry strategy"),
            ("parallel-execution", "Parallel execution"),
            ("mocking", "Mocking"),
            ("network-interception", "Network interception"),
            ("ci-cd-integration", "CI/CD integration"),
            ("salesforce-best-practices", "Salesforce best practices"),
            ("common-failures", "Common failures"),
        ],
    },
    "selenium": {
        "title": "Selenium Guidance",
        "purpose": "Enterprise Selenium considerations when Playwright is not adopted.",
        "scope": "Architecture fit, Grid, waits, SF UI risks, migration notes.",
        "docs": [
            ("selenium-architecture", "Selenium architecture"),
            ("webdriver-grid", "Grid / remote"),
            ("waits-and-stability", "Waits and stability"),
            ("salesforce-ui-risks", "SF UI risks"),
            ("migration-to-playwright", "Migration considerations"),
        ],
    },
    "cypress": {
        "title": "Cypress Guidance",
        "purpose": "When Cypress is appropriate vs Playwright for Salesforce.",
        "scope": "Architecture, limitations for multi-tab/multi-origin, CI fit.",
        "docs": [
            ("cypress-architecture", "Cypress architecture"),
            ("cypress-limitations", "Limitations"),
            ("salesforce-fit", "Salesforce fit assessment"),
            ("ci-cd-with-cypress", "CI/CD notes"),
        ],
    },
    "robot-framework": {
        "title": "Robot Framework Guidance",
        "purpose": "Keyword-driven automation with Robot Framework on Salesforce programs.",
        "scope": "Libraries, keywords, hybrid UI/API, governance.",
        "docs": [
            ("robot-architecture", "Robot architecture"),
            ("keyword-design", "Keyword design"),
            ("salesforce-libraries", "SF-oriented libraries"),
            ("governance-with-robot", "Governance"),
        ],
    },
    "api-testing": {
        "title": "API Testing",
        "purpose": "API automation strategy for Salesforce and integrations.",
        "scope": "REST/SOAP, OAuth/JWT, Named Credentials, contract, schema, negative, performance notes.",
        "docs": [
            ("rest", "REST API testing"),
            ("soap", "SOAP considerations"),
            ("oauth", "OAuth flows"),
            ("jwt", "JWT"),
            ("named-credentials", "Named Credentials"),
            ("api-mocking", "API mocking"),
            ("contract-testing", "Contract testing"),
            ("schema-validation", "Schema validation"),
            ("performance-considerations", "Performance considerations"),
            ("retry-logic", "API retry logic"),
            ("error-validation", "Error validation"),
            ("negative-testing", "Negative API testing"),
        ],
    },
    "mobile-testing": {
        "title": "Mobile Testing",
        "purpose": "Mobile automation advisory for Salesforce mobile / Field Service contexts.",
        "scope": "Appium strategy, device labs, when to keep manual—no full scripts.",
        "docs": [
            ("mobile-automation-strategy", "Mobile strategy"),
            ("appium-guidance", "Appium guidance"),
            ("device-cloud-labs", "Device clouds"),
            ("salesforce-mobile-considerations", "SF mobile considerations"),
        ],
    },
    "visual-testing": {
        "title": "Visual Testing",
        "purpose": "Visual regression advisory for Lightning/Experience UIs.",
        "scope": "Baselines, thresholds, when visual adds value vs noise.",
        "docs": [
            ("visual-regression-strategy", "Visual strategy"),
            ("baseline-management", "Baselines"),
            ("threshold-and-noise", "Thresholds and noise"),
            ("salesforce-ui-visual-risks", "SF visual risks"),
        ],
    },
    "performance-testing": {
        "title": "Performance Testing",
        "purpose": "Performance test strategy adjacent to functional automation.",
        "scope": "When to performance-test, governors, LDV, tooling intent—not load-script generation.",
        "docs": [
            ("performance-strategy", "Performance strategy"),
            ("salesforce-governor-awareness", "Governor awareness"),
            ("api-load-considerations", "API load considerations"),
            ("tooling-selection", "Tooling selection"),
        ],
    },
    "ci-cd": {
        "title": "CI/CD",
        "purpose": "Integrate automation into enterprise delivery pipelines.",
        "scope": "ADO, GitHub Actions, Jenkins, gates, promotion, publishing—design only.",
        "docs": [
            ("azure-devops-pipelines", "Azure DevOps Pipelines"),
            ("github-actions", "GitHub Actions"),
            ("jenkins", "Jenkins"),
            ("build-validation", "Build validation"),
            ("smoke-execution", "Smoke in CI"),
            ("regression-execution", "Regression in CI"),
            ("parallel-execution", "Parallel in CI"),
            ("environment-promotion", "Environment promotion"),
            ("approval-gates", "Approval gates"),
            ("quality-gates", "Quality gates"),
            ("rollback-strategy", "Rollback strategy"),
            ("deployment-validation", "Deployment validation"),
            ("test-result-publishing", "Result publishing"),
            ("notifications", "Notifications"),
            ("artifact-management", "Artifacts"),
        ],
    },
    "test-data": {
        "title": "Test Data Automation",
        "purpose": "Reliable, compliant test data for automation.",
        "scope": "Synthetic/masked/bulk/dynamic data, seeding, cleanup, isolation.",
        "docs": [
            ("synthetic-data", "Synthetic data"),
            ("masked-data", "Masked data"),
            ("salesforce-test-data", "Salesforce test data"),
            ("bulk-data", "Bulk data"),
            ("dynamic-data", "Dynamic data"),
            ("cleanup", "Cleanup"),
            ("refresh-strategy", "Refresh strategy"),
            ("data-seeding", "Data seeding"),
            ("api-data-creation", "API data creation"),
            ("data-dependencies", "Data dependencies"),
            ("environment-isolation", "Environment isolation"),
        ],
    },
    "automation-governance": {
        "title": "Automation Governance",
        "purpose": "Standards, ownership, and reviews for sustainable automation.",
        "scope": "Coding/naming, PRs, branching, ownership, readiness, KT.",
        "docs": [
            ("coding-standards", "Coding standards"),
            ("naming-standards", "Naming standards"),
            ("folder-structure", "Folder structure"),
            ("code-reviews", "Code reviews"),
            ("pull-requests", "Pull requests"),
            ("branch-strategy", "Branch strategy"),
            ("versioning", "Versioning"),
            ("framework-ownership", "Framework ownership"),
            ("automation-reviews", "Automation reviews"),
            ("release-readiness", "Release readiness"),
            ("documentation", "Documentation"),
            ("knowledge-transfer", "Knowledge transfer"),
        ],
    },
    "maintenance": {
        "title": "Automation Maintenance",
        "purpose": "Keep suites healthy and reduce maintenance drag.",
        "scope": "Flake triage, refactor triggers, quarantine, debt, ownership.",
        "docs": [
            ("maintenance-model", "Maintenance model"),
            ("flake-triage", "Flake triage"),
            ("refactor-triggers", "Refactor triggers"),
            ("quarantine-policy", "Quarantine policy"),
            ("technical-debt", "Automation technical debt"),
        ],
    },
    "metrics": {
        "title": "Automation Metrics",
        "purpose": "Measure automation value and health without inventing KPIs.",
        "scope": "Coverage, time, pass/fail, stability, ROI, cost, trends.",
        "docs": [
            ("automation-coverage", "Automation coverage"),
            ("execution-time", "Execution time"),
            ("pass-rate", "Pass rate"),
            ("failure-rate", "Failure rate"),
            ("script-stability", "Script stability"),
            ("flaky-tests", "Flaky tests"),
            ("maintenance-effort", "Maintenance effort"),
            ("roi", "ROI metrics"),
            ("defect-detection-rate", "Defect detection rate"),
            ("execution-cost", "Execution cost"),
            ("trend-analysis", "Trend analysis"),
        ],
    },
}

# Enrich comparison docs with tool-specific meta
TOOL_DETAILS = {
    "playwright": tool_meta(
        "Playwright",
        ["Strong auto-waits, tracing, API+UI in one toolchain", "Good parallel/CI support", "Storage state for auth reuse"],
        ["Team ramp if Selenium-only skills", "Visual/tooling ecosystem choices still needed"],
        "Generally strongest default for modern Lightning UI automation when locators are designed carefully.",
        "Default Playwright-first recommendation for greenfield Salesforce UI+API automation",
    ),
    "selenium": tool_meta(
        "Selenium",
        ["Mature ecosystem and hiring pool", "Language flexibility", "Grid for scale"],
        ["More boilerplate and wait discipline required", "Higher flake risk without strong design"],
        "Viable for brownfield estates; invest heavily in waits, POM, and Grid ops.",
        "Retain/optimize when migration cost exceeds benefit; plan gradual Playwright pilots",
    ),
    "cypress": tool_meta(
        "Cypress",
        ["Developer-friendly DX", "Time-travel debugging", "Strong for single-origin web apps"],
        ["Multi-tab/multi-origin and some enterprise patterns harder", "JavaScript-centric"],
        "Evaluate carefully for Salesforce Lightning complexity and multi-window flows.",
        "Consider for specific web apps; not automatic default over Playwright for Salesforce",
    ),
    "robot-framework": tool_meta(
        "Robot Framework",
        ["Keyword readability for mixed-skill teams", "Rich library ecosystem", "Good for hybrid keyword+Python"],
        ["Abstraction can hide poor design", "UI stability still depends on underlying driver"],
        "Useful when BA/QE collaboration on keywords is a program goal.",
        "Use for keyword-driven programs with clear library ownership",
    ),
    "webdriverio": tool_meta(
        "WebdriverIO",
        ["Modern JS ecosystem", "Flexible services", "Mobile via Appium integration paths"],
        ["Requires solid JS engineering discipline", "Salesforce UI challenges same as other WebDriver tools"],
        "Option for JS-centric teams already standardized on WDIO.",
        "Select when org standard is WebdriverIO and skills are deep",
    ),
    "appium": tool_meta(
        "Appium",
        ["Cross-platform mobile automation", "Integrates with device clouds"],
        ["Higher maintenance and device flakiness", "Slower feedback than API checks"],
        "Use for Salesforce mobile / Field Service mobile where business risk justifies cost.",
        "Automate critical mobile journeys only; keep most validation at API/service layer",
    ),
    "rest-assured": tool_meta(
        "REST Assured",
        ["Expressive Java API assertions", "Fits Java enterprise stacks"],
        ["Java-centric", "Not a UI solution"],
        "Strong for Salesforce REST integration testing in Java shops.",
        "Pair with UI tool (Playwright/Selenium) for full pyramid",
    ),
    "postman": tool_meta(
        "Postman",
        ["Fast exploratory and collection-based API checks", "Easy collaboration"],
        ["Large-scale code governance can be weaker than code-first frameworks", "CI patterns vary"],
        "Excellent for integration discovery and lightweight API suites; formalize for enterprise scale.",
        "Use for API exploration + gated collections; graduate critical suites to code-first when needed",
    ),
    "karate": tool_meta(
        "Karate",
        ["DSL for API (and some UI) with reports", "Good contract-style readability"],
        ["DSL lock-in considerations", "Team skill availability"],
        "Useful for API-centric Salesforce integration programs.",
        "Choose when API DSL productivity outweighs general-purpose language frameworks",
    ),
}


def enrich_meta(folder: str, slug: str) -> dict:
    if folder == "framework-comparison" and slug in TOOL_DETAILS:
        return TOOL_DETAILS[slug]
    purpose_map = {
        "automation-pyramid": "Explain and apply the test automation pyramid for Salesforce programs.",
        "automation-roi": "Estimate automation ROI with transparent assumptions—never invent financials.",
        "automation-feasibility": "Assess whether a scenario is ready and suitable to automate.",
        "automation-decision-engine": "Drive structured automate/manual/framework decisions.",
        "salesforce-best-practices": "Playwright practices tailored to Lightning and Salesforce testing constraints.",
        "common-failures": "Catalog common Playwright+Salesforce failure modes and prevention.",
        "named-credentials": "Test integrations that rely on Salesforce Named Credentials securely.",
        "flaky-tests": "Measure and act on flaky automation using Sprint 7 stability rules.",
        "azure-devops-pipelines": "Design Azure DevOps pipeline stages for Salesforce automation feedback.",
        "github-actions": "Design GitHub Actions workflows for automation execution and publishing.",
    }
    purpose = purpose_map.get(slug, f"Provide enterprise guidance on {titleize(slug)} for Salesforce automation intelligence.")
    meta: dict = {"purpose": purpose}
    if folder == "automation-strategy" and slug == "automation-pyramid":
        meta["architecture"] = [
            "Unit/component (where owned by Dev) → API/service → UI smoke/critical journeys.",
            "Salesforce: assert business rules via API/metadata checks; keep UI thin and persona-focused.",
        ]
        meta["decision_criteria"] = [
            "Prefer API when oracle is data/state",
            "UI only for true UI risk or E2E confidence",
            "Avoid inverting the pyramid for vanity UI coverage",
        ]
    if folder == "ci-cd":
        meta["salesforce"] = [
            "Align pipeline stages with sandbox promotion (dev → QA → UAT → pre-prod).",
            "Include post-deploy smoke and optional production validation hooks (shift-right).",
            "Publish results to ADO Test Plans / pipelines where the program uses Sprint 6 guidance.",
        ]
    if folder == "api-testing":
        meta["salesforce"] = [
            "Cover REST (and SOAP where legacy), bulk, and event-driven integrations.",
            "Test OAuth/JWT and Named Credential configurations without exposing secrets.",
            "Include negative auth, validation rule, and sharing-denied scenarios.",
        ]
    if folder == "playwright" and slug == "salesforce-best-practices":
        meta["practices"] = [
            "Use resilient locators (role/label/test id); avoid brittle dynamic Salesforce IDs",
            "Reuse storage state per persona; never commit secrets",
            "Prefer API setup/teardown; UI asserts outcomes",
            "Enable tracing on failure; quarantine flakes per governance",
            "Parallelize by file/project with isolated data",
        ]
    return meta


def root_readme() -> str:
    rows = "\n".join(
        f"| [{cfg['title']}]({folder}/README.md) | {cfg['purpose']} |"
        for folder, cfg in FOLDERS.items()
    )
    return f"""---
title: Automation Intelligence — README
module: Salesforce Quality Engineering
version: {VERSION}
tags: [automation-intelligence, sprint-8]
---

# Automation Intelligence & Test Automation Architecture

## Purpose

Enable the AI to act as a **Test Automation Architect**: recommend whether to automate, select frameworks, design architecture, plan CI/CD, estimate ROI, and govern maintainable Salesforce automation—**without generating full scripts**.

## Scope (Sprint 8)

**In scope:** Strategy, framework design/comparison, Playwright enterprise guidance, API/mobile/visual/performance advisory, CI/CD, test data, governance, maintenance, metrics, Salesforce automation intelligence, decision engine.

**Out of scope:** Full Playwright/Selenium/Cypress script generation; inventing coverage % or ROI numbers without inputs.

## Engine entry

- [automation-intelligence-engine.md](automation-intelligence-engine.md)
- [automation-decision-engine.md](automation-decision-engine.md)

## Folders

| Folder | Focus |
|--------|-------|
{rows}
| [salesforce/](salesforce/README.md) | Salesforce-specific automation intelligence |
| [decision-engine/](decision-engine/README.md) | Automate? Framework? ROI? Priority? |

## Supported frameworks (advisory)

Playwright (**default first**), Selenium, Cypress, Robot Framework, WebdriverIO, Appium, REST Assured, Postman, Karate.

## Supported CI/CD platforms

Azure DevOps Pipelines · GitHub Actions · Jenkins

## Navigation

- **Previous:** [../quality-intelligence/README.md](../quality-intelligence/README.md)
- **Next:** [automation-intelligence-engine.md](automation-intelligence-engine.md)
- **See Also:** [../skill.md](../skill.md)

## Related Documents

{bullets(CROSS_ROOT)}
"""


def engine_md() -> str:
    return f"""---
title: Automation Intelligence Engine
version: {VERSION}
tags: [automation-intelligence, sprint-8]
---

# Automation Intelligence Engine

## Purpose

Orchestrate automation strategy → feasibility → framework selection → architecture → CI/CD → governance → metrics for Salesforce QE.

## Process

```
Requirement / scenario / candidate input
    ↓
Feasibility & prioritization (strategy)
    ↓
Automate vs manual decision (decision engine)
    ↓
Framework selection (comparison + Playwright-first default)
    ↓
Architecture & patterns (framework-design)
    ↓
Test data + CI/CD design
    ↓
Governance & maintenance model
    ↓
Metrics & health (no invented %)
```

## Hard rules

1. **No full script generation** in Sprint 8—design and decisions only.  
2. Playwright-first, framework-agnostic (respect brownfield estates).  
3. Never invent ROI, coverage %, or execution times without data/assumptions.  
4. Reuse Sprint 3 automation candidates; Sprint 7 flake/stability rules; Sprint 6 ADO CI concepts.  
5. Prefer API/service automation under thin UI smoke (pyramid).  

## Related

{bullets(CROSS_ROOT)}
- [automation-decision-engine.md](automation-decision-engine.md)
- [rules/](../quality-intelligence/rules/automation-stability-rules.md)
"""


def decision_engine_md() -> str:
    return f"""---
title: Automation Decision Engine
version: {VERSION}
tags: [automation-intelligence, sprint-8]
---

# Automation Decision Engine

## Purpose

Answer structured automation questions with reasoning and confidence scores.

## Questions the AI must answer

| Question | Output |
|----------|--------|
| Should this be automated? | Yes / No / Later + why |
| Why? | Business + technical rationale |
| Which framework? | Tool + alternatives |
| Estimated effort? | T-shirt / range + assumptions (not fake hours certainty) |
| Expected ROI? | Qualitative + formula inputs needed |
| Risk level? | Low/Medium/High |
| Maintenance complexity? | Low/Medium/High |
| CI/CD readiness? | Ready / Gaps |
| Regression impact? | Pack impact statement |
| Automation priority? | P0–P3 |

## Decision flow

```
Is the path stable and oracle clear?
  No → Manual / Later + stabilize first
  Yes ↓
Is frequency/risk high enough?
  No → Manual exploratory / checklist
  Yes ↓
Prefer API/service over UI when possible
  ↓
Select framework (Playwright-first unless constraints)
  ↓
Score effort, maintenance, CI readiness, ROI inputs
  ↓
Priority + roadmap placement
```

## Confidence

Always state **Low / Medium / High** confidence with missing-data notes.

## Related

- [automation-intelligence-engine.md](automation-intelligence-engine.md)
- [automation-strategy/automation-feasibility.md](automation-strategy/automation-feasibility.md)
- [framework-comparison/README.md](framework-comparison/README.md)
- [metrics/roi.md](metrics/roi.md)
"""


SF_DOCS = [
    ("lightning-pages", "Lightning Pages automation approach"),
    ("flows", "Flow automation approach"),
    ("validation-rules", "Validation rule checks"),
    ("reports", "Reports automation advisory"),
    ("dashboards", "Dashboard checks"),
    ("record-types", "Record type coverage"),
    ("profiles", "Profile-related checks"),
    ("permission-sets", "Permission set automation"),
    ("sharing-rules", "Sharing rule scenarios"),
    ("experience-cloud", "Experience Cloud automation"),
    ("utilities-cloud", "Utilities Cloud automation"),
    ("agentforce", "Agentforce automation advisory"),
    ("omnistudio", "OmniStudio automation"),
    ("managed-packages", "Managed package automation"),
    ("integrations", "Integration automation"),
    ("batch-jobs", "Batch job automation"),
    ("platform-events", "Platform Events automation"),
]

DECISION_DOCS = [
    ("should-automate", "Should this be automated?"),
    ("framework-selection", "Which framework?"),
    ("effort-and-roi", "Effort and ROI"),
    ("risk-and-maintenance", "Risk and maintenance"),
    ("ci-cd-readiness", "CI/CD readiness"),
    ("priority-scoring", "Automation priority"),
    ("confidence-scoring", "Confidence scores"),
]


def main() -> None:
    AI.mkdir(parents=True, exist_ok=True)
    (AI / "README.md").write_text(root_readme(), encoding="utf-8")
    (AI / "automation-intelligence-engine.md").write_text(engine_md(), encoding="utf-8")
    (AI / "automation-decision-engine.md").write_text(decision_engine_md(), encoding="utf-8")

    folder_order = list(FOLDERS.keys())
    for i, folder in enumerate(folder_order):
        cfg = FOLDERS[folder]
        path = AI / folder
        path.mkdir(parents=True, exist_ok=True)
        docs = [(d[0], d[1]) for d in cfg["docs"]]
        prev = f"../{folder_order[i-1]}/README.md" if i > 0 else "../README.md"
        nxt = f"../{folder_order[i+1]}/README.md" if i < len(folder_order) - 1 else "../salesforce/README.md"
        (path / "README.md").write_text(
            folder_readme(folder, cfg["title"], cfg["purpose"], cfg["scope"], docs, prev, nxt),
            encoding="utf-8",
        )
        for j, (slug, _blurb) in enumerate(docs):
            meta = enrich_meta(folder, slug)
            prev_s = docs[j - 1][0] + ".md" if j > 0 else "README.md"
            next_s = docs[j + 1][0] + ".md" if j < len(docs) - 1 else "README.md"
            prev_t = titleize(docs[j - 1][0]) if j > 0 else "README"
            next_t = titleize(docs[j + 1][0]) if j < len(docs) - 1 else "README"
            (path / f"{slug}.md").write_text(
                article(
                    folder,
                    slug,
                    meta,
                    {
                        "prev": prev_s,
                        "next": next_s,
                        "prev_title": prev_t,
                        "next_title": next_t,
                    },
                ),
                encoding="utf-8",
            )

    # Salesforce automation intelligence
    sf = AI / "salesforce"
    sf.mkdir(parents=True, exist_ok=True)
    (sf / "README.md").write_text(
        folder_readme(
            "salesforce",
            "Salesforce Automation Intelligence",
            "Teach how to approach automation for Salesforce platform and cloud capabilities.",
            "Lightning, Flow, security metadata, clouds, OmniStudio, Agentforce, integrations, async—decision and design level only.",
            SF_DOCS,
            "../metrics/README.md",
            "../decision-engine/README.md",
        ),
        encoding="utf-8",
    )
    for j, (slug, _b) in enumerate(SF_DOCS):
        meta = {
            "purpose": f"Advise how to automate or validate {titleize(slug)} on Salesforce programs.",
            "architecture": [
                f"Prefer API/metadata/service assertions for {titleize(slug)} where UI is not the risk.",
                "Add targeted UI only for persona-visible outcomes.",
            ],
            "decision_criteria": [
                "Is the behavior better asserted via API, UI, or both?",
                "How volatile is the UI/metadata surface?",
                "What persona/security paths are mandatory?",
            ],
            "salesforce": [
                f"Load matching 4A/4B knowledge for {titleize(slug)} before recommending design.",
                "Respect packaging, governor, and sharing constraints.",
            ],
        }
        prev_s = SF_DOCS[j - 1][0] + ".md" if j > 0 else "README.md"
        next_s = SF_DOCS[j + 1][0] + ".md" if j < len(SF_DOCS) - 1 else "README.md"
        (sf / f"{slug}.md").write_text(
            article(
                "salesforce",
                slug,
                meta,
                {
                    "prev": prev_s,
                    "next": next_s,
                    "prev_title": titleize(SF_DOCS[j - 1][0]) if j > 0 else "README",
                    "next_title": titleize(SF_DOCS[j + 1][0]) if j < len(SF_DOCS) - 1 else "README",
                },
            ),
            encoding="utf-8",
        )

    # Decision engine folder (deep dive articles)
    de = AI / "decision-engine"
    de.mkdir(parents=True, exist_ok=True)
    (de / "README.md").write_text(
        folder_readme(
            "decision-engine",
            "AI Decision Engine",
            "Structured automate/manual/framework/ROI/priority decisions with confidence.",
            "Decision questions, scoring, and recommendation format—not script generation.",
            DECISION_DOCS,
            "../salesforce/README.md",
            "../README.md",
        ),
        encoding="utf-8",
    )
    for j, (slug, _b) in enumerate(DECISION_DOCS):
        meta = {
            "purpose": f"Guide the AI on {titleize(slug)} within the Automation Decision Engine.",
            "decision_criteria": [
                "Evidence completeness",
                "Business risk and frequency",
                "Technical stability and data readiness",
                "Team skills and CI/CD constraints",
            ],
            "outputs": [
                "Decision + reasoning",
                "Confidence Low/Medium/High",
                "Next actions / open questions",
            ],
        }
        # fix - article doesn't use outputs key specially - add via process
        meta["architecture"] = [
            "See ../automation-decision-engine.md for the master question set.",
            "Cite framework-comparison and strategy articles when recommending tools.",
        ]
        prev_s = DECISION_DOCS[j - 1][0] + ".md" if j > 0 else "README.md"
        next_s = DECISION_DOCS[j + 1][0] + ".md" if j < len(DECISION_DOCS) - 1 else "README.md"
        (de / f"{slug}.md").write_text(
            article(
                "decision-engine",
                slug,
                meta,
                {
                    "prev": prev_s,
                    "next": next_s,
                    "prev_title": titleize(DECISION_DOCS[j - 1][0]) if j > 0 else "README",
                    "next_title": titleize(DECISION_DOCS[j + 1][0]) if j < len(DECISION_DOCS) - 1 else "README",
                },
            ),
            encoding="utf-8",
        )

    count = sum(1 for _ in AI.rglob("*.md"))
    print(f"Wrote ~{count} files under {AI}")


if __name__ == "__main__":
    main()
