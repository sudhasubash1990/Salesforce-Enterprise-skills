"""Generate Salesforce Playwright Review (PWR) skill pack."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAP = ROOT / "skills" / "playwright-review"
VERSION = "0.21.0"
DATE = "2026-07-27"

OUTPUT_SECTIONS = [
    "Executive Summary",
    "Framework Assessment",
    "Architecture Review",
    "Code Quality Review",
    "Locator Review",
    "Assertion Review",
    "Synchronization Review",
    "Salesforce Compatibility Review",
    "Maintainability Assessment",
    "Performance Analysis",
    "CI/CD Readiness",
    "Security Considerations",
    "Flaky Test Analysis",
    "Risks",
    "Recommendations",
    "Refactoring Suggestions",
    "Best Practices",
    "Overall Quality Score",
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
    return fm(title, "QE Specialized Skill Knowledge", "Knowledge Article", ["playwright-review", "knowledge"]) + f"""# {title}

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
    return fm(title, "QE Specialized Skill Playbook", "Playbook", ["playwright-review", "playbook"]) + f"""# {title}

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
    return fm(title, "QE Specialized Skill Template", "Template", ["playwright-review", "template"]) + f"""# {title}

{body}

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| {VERSION} | {DATE} | QE Practice Lead | Initial template |
"""


def prompt_doc(title, prompt, sections):
    return fm(title, "QE Specialized Skill Prompt", "Prompt", ["playwright-review", "prompt"]) + f"""# {title}

## Prompt

```
{prompt}
```

## Required Output Sections

{chr(10).join(f"{i}. {s}" for i, s in enumerate(sections, 1))}

## Quality Gate

- Framework context and review scope BEFORE line-by-line critique.
- 1–5 scores with evidence or N/A; no invented coverage/flake %.
- Refactoring suggestions as snippets only unless full rewrite requested.
"""


def example_doc(title, original, issues, improvements, refactored, practices, qa):
    return fm(title, "QE Specialized Skill Example", "Example", ["playwright-review", "example"]) + f"""# {title}

## Original Implementation

{original}

## Identified Issues

{issues}

## Recommended Improvements

{improvements}

## Refactored Example

{refactored}

## Best Practices

{practices}

## QA Recommendations

{qa}
"""


def main() -> None:
    print("Generating Playwright Review skill pack...")
    CAP.mkdir(parents=True, exist_ok=True)

    write(
        "skill-config.yaml",
        f"""name: playwright-review
short_id: PWR
version: {VERSION}
parent_module: salesforce-quality-engineering
entry: SKILL.md

routing:
  keywords:
    - Playwright
    - Playwright Test
    - Automation Review
    - Test Script
    - Test Framework
    - Locator
    - Selector
    - POM
    - Page Object
    - Fixtures
    - Assertions
    - Retry
    - Timeout
    - Parallel Execution
    - CI/CD
    - Azure DevOps
    - GitHub Actions
    - Code Review
    - Test Stability
    - Flaky Tests
    - Flake
    - Reporting
    - Trace Viewer
    - storageState
    - playwright.config
    - getByRole
    - Auto Waiting
  primary_support:
    - automation-intelligence/review-engine/
    - automation-intelligence/playwright/
  upstream_skills:
    - skills/metadata-impact-analyzer
  downstream_capabilities:
    - skills/soql-validation-assistant
    - skills/permission-testing-agent
    - skills/agentforce-testing
    - skills/test-data-generator
  downstream_after_analysis:
    - knowledge/test-design-engine.md

output_schema:
  sections:
{chr(10).join(f'    - id: {s.lower().replace(" ", "_").replace("/", "_")}' + chr(10) + f'      title: "{s}"' for s in OUTPUT_SECTIONS)}

quality_gates:
  - framework_context_before_script_critique
  - eighteen_sections_labeled
  - scores_1_to_5_with_evidence_or_na
  - no_invented_coverage_or_flake_percent
  - salesforce_sync_when_ui_in_scope
  - secrets_and_flake_before_cosmetic
  - refactor_snippets_not_full_suite_unless_requested

escalation:
  - signal: secrets_or_storage_state_in_git
    to: Security Architect
  - signal: systemic_flake_blocking_release
    to: Automation Lead + Release Manager
  - signal: no_ci_for_critical_smoke
    to: DevOps / Release Manager
""",
    )

    pw = "../../automation-intelligence/playwright"
    re = "../../automation-intelligence/review-engine"
    mia = "../../skills/metadata-impact-analyzer/SKILL.md"
    sova = "../soql-validation-assistant/SKILL.md"
    pta = "../permission-testing-agent/SKILL.md"
    aft = "../agentforce-testing/SKILL.md"
    tdg = "../test-data-generator/SKILL.md"

    knowledge_specs = [
        ("Playwright Architecture for Review", "playwright-architecture.md",
         "Assess layering before criticizing individual tests.",
         ["Map projects, workers, fixtures, and page layers.", "Identify shared mutable state risks.", "Separate UI vs API concerns.", "Cross-link Sprint 8 architecture — do not duplicate."],
         [("Architecture", f"{pw}/architecture.md"), ("Architecture and Modularity", f"{re}/architecture-and-modularity.md")],
         ["No framework map → incomplete Architecture Review.", "Shared page across workers → High maintainability risk."]),
        ("Playwright Configuration", "playwright-configuration.md",
         "Review playwright.config for env, projects, retries, reporters.",
         ["Inventory projects (browsers/envs).", "Check retries, timeout, workers.", "Flag hardcoded org URLs in config.", "Ensure reporters/traces on failure."],
         [("CI/CD Integration", f"{pw}/ci-cd-integration.md")],
         ["Hardcoded secrets in config → Critical security."]),
        ("Page Object Model", "page-object-model.md",
         "Evaluate POM/Screenplay abstractions for Salesforce flows.",
         ["Pages own locators/actions; tests own assertions/flow.", "Avoid dumping business logic only in tests.", "Score against Sprint 8 POM lens.", "Prefer small cohesive pages over god objects."],
         [("Page Objects", f"{pw}/page-objects.md"), ("POM / Screenplay Quality", f"{re}/pom-screenplay-quality.md")],
         ["God page objects → Fail maintainability gate."]),
        ("Fixtures", "fixtures.md",
         "Review fixture design for personas, auth, and isolation.",
         ["Typed fixtures preferred.", "Worker isolation; no shared mutable page.", "Persona fixtures map to PTA themes.", "Setup via API where possible."],
         [("Fixtures", f"{pw}/fixtures.md"), ("Test Data Generator", tdg)],
         ["Shared mutable fixture state → Flake risk."]),
        ("Hooks", "hooks.md",
         "Assess before/after hooks for cleanup and side effects.",
         ["Prefer fixtures over global hooks where possible.", "Ensure cleanup does not hide failures.", "Avoid heavy UI login in every beforeEach when storageState exists."],
         [("Fixtures", "fixtures.md")],
         ["Login UI in every test without storageState → Performance smell."]),
        ("Locator Strategies", "locator-strategies.md",
         "Score locator robustness for Lightning and Experience UI.",
         ["Prefer getByRole / label / test-id.", "Flag absolute XPath and brittle CSS.", "Centralize SF-specific locators.", "Chain MIA when FlexiPage/LWC changes."],
         [("Locators", f"{pw}/locators.md"), ("Locator Robustness", f"{re}/locator-robustness.md"), ("Metadata Impact Analyzer", mia)],
         ["XPath soup for Lightning → Fail Locator Review."]),
        ("Assertions", "assertions.md",
         "Review assertion clarity and failure diagnostics.",
         ["Assert business outcomes, not only element presence.", "Use web-first assertions with auto-wait.", "Avoid soft-assert spam that hides defects.", "Pair UI assert with SOVA when data state matters."],
         [("SOQL Validation Assistant", sova)],
         ["Presence-only asserts for critical CRM writes → Weak."]),
        ("Auto Waiting", "auto-waiting.md",
         "Prefer Playwright auto-wait over hard sleeps for Salesforce UI.",
         ["Identify sleep()/waitForTimeout abuse.", "Use expect(...).toBeVisible and locator actions.", "Document intentional network waits.", "SF Lightning may need targeted ready helpers — not blanket sleeps."],
         [("Common Failures", f"{pw}/common-failures.md")],
         ["Hard sleep as primary sync → Fail Synchronization Review."]),
        ("Network Mocking", "network-mocking.md",
         "Review route mocking vs real Salesforce API usage.",
         ["Prefer real SF API for setup/teardown when validating CRM.", "Mock only unstable third parties with justification.", "Document mock contracts.", "Avoid masking SF defects with over-mocking."],
         [("Mocking", f"{pw}/mocking.md"), ("Network Interception", f"{pw}/network-interception.md")],
         ["Mocking core CRM write path for UI 'pass' → High risk."]),
        ("API Testing", "api-testing.md",
         "Assess Playwright request context for setup and API coverage.",
         ["Use request fixture for seed/cleanup.", "Keep API tests independent of UI flakes.", "Recommend SOVA for post-condition queries.", "Auth for API must not leak secrets."],
         [("API Testing", f"{pw}/api-testing.md"), ("SOQL Validation Assistant", sova)],
         ["UI-only setup for bulk data → recommend TDG/API."]),
        ("Authentication", "authentication.md",
         "Review Salesforce login, MFA-aware patterns, and storageState.",
         ["storageState per persona.", "Never commit session cookies.", "MFA: document program approach (TOTP vault, sandbox waiver) — do not invent.", "Chain PTA for persona coverage."],
         [("Authentication", f"{pw}/authentication.md"), ("Storage State", f"{pw}/storage-state.md"), ("Permission Testing Agent", pta)],
         ["storageState in git → Critical escalate Security."]),
        ("Parallel Execution", "parallel-execution.md",
         "Evaluate fullyParallel, workers, and data isolation.",
         ["Confirm isolated test data per worker.", "Flag shared Pricebook/Account collisions.", "Recommend External ID prefixes (TDG).", "Measure only with evidence — no invented speedups."],
         [("Parallel Execution", f"{pw}/parallel-execution.md"), ("Test Data Generator", tdg)],
         ["Parallel without data isolation → Flake Critical."]),
        ("Retry Strategy", "retry-strategy.md",
         "Review retries as resilience vs masking defects.",
         ["Config retries for infra flake only.", "Investigate root cause before raising retries.", "Trace on first retry preferred.", "Do not use retries to hide bad locators."],
         [("Retry Strategy", f"{pw}/retry-strategy.md"), ("Flaky and Stability", f"{re}/flaky-and-stability-review.md")],
         ["High retries without flake analysis → Fail Flaky Analysis."]),
        ("Trace Viewer", "trace-viewer.md",
         "Ensure traces/screenshots/video support triage.",
         ["Traces on failure in CI.", "Retention policy documented.", "PII in traces — scrub or restrict access.", "Link reporting observability."],
         [("Tracing", f"{pw}/tracing.md"), ("Reporting and Observability", f"{re}/reporting-observability.md")],
         ["No artifacts on CI fail → CI/CD gap."]),
        ("Reporting", "reporting.md",
         "Assess HTML/JUnit/custom reporters for release evidence.",
         ["Map reporters to ADO/GH requirements.", "Include flake taxonomy if available.", "Do not invent pass rates.", "Executive summary should cite artifact locations."],
         [("Reporting", f"{pw}/reporting.md")],
         ["No publish step in CI → CI/CD Readiness weak."]),
        ("Accessibility Testing", "accessibility-testing.md",
         "Review a11y checks as advisory coverage for Experience/Lightning.",
         ["Note axe/playwright-a11y usage if present.", "Do not invent WCAG certification.", "Prioritize Experience Cloud public pages.", "Pair with UX defects, not only automation."],
         [("Visual Testing", f"{pw}/visual-testing.md")],
         ["Claiming WCAG pass without scan evidence → anti-pattern."]),
        ("Salesforce UI Automation Best Practices", "salesforce-ui-automation-best-practices.md",
         "Salesforce-specific UI automation review lens.",
         ["Centralize Lightning navigation helpers.", "Handle related lists, console tabs, utility bar.", "Experience vs LEX differences.", "Agentforce UI → chain AFT for AI quality beyond clicks."],
         [("Salesforce Best Practices", f"{pw}/salesforce-best-practices.md"), ("Agentforce Testing", aft)],
         ["UI-only Agentforce tests without AFT → Incomplete."]),
        ("Salesforce Synchronization Techniques", "salesforce-synchronization-techniques.md",
         "Sync patterns for Lightning rendering and async saves.",
         ["Prefer auto-wait + network idle sparingly.", "Ready helpers for spinner/toast.", "Avoid fixed sleeps.", "Validate save via UI toast + optional SOVA."],
         [("Common Failures", f"{pw}/common-failures.md"), ("SOQL Validation Assistant", sova)],
         ["Sleep-only sync → Fail Synchronization Review."]),
        ("CI/CD Integration", "cicd-integration.md",
         "Generic CI readiness for Playwright Salesforce suites.",
         ["Sharding, browsers, artifacts, secrets injection.", "Smoke vs full suite gates.", "Fail-fast vs complete report tradeoffs.", "Cross-link ADO/GH specifics."],
         [("CI/CD Integration", f"{pw}/ci-cd-integration.md"), ("CI/CD Readiness", f"{re}/cicd-readiness-review.md")],
         ["Secrets in pipeline logs → Critical."]),
        ("Azure DevOps Pipelines", "azure-devops.md",
         "Review ADO YAML for Playwright jobs and Test Plans linkage.",
         ["Check pool, Node version, cache.", "Publish HTML/JUnit.", "Variable groups for secrets.", "Do not invent ADO publish API unless requested."],
         [("CI/CD Integration", "cicd-integration.md")],
         ["Hardcoded PAT in YAML → Critical Security."]),
        ("GitHub Actions", "github-actions.md",
         "Review GH Actions workflows for Playwright.",
         ["actions/setup-node, cache, matrix browsers.", "Artifacts upload on failure.", "OIDC/secrets — never echo.", "PR vs main branch gates."],
         [("CI/CD Integration", "cicd-integration.md")],
         ["Unpinned actions at latest without rationale → Governance note."]),
        ("Playwright Review Best Practices", "playwright-review-best-practices.md",
         "Synthesize enterprise PWR discipline.",
         ["Context before critique.", "Score with Sprint 8 model.", "Prioritize secrets and flake.", "Snippet refactors; chain MIA/SOVA/PTA/AFT/TDG.", "Label assumptions."],
         [("Automation Review Engine", f"{re}/automation-review-engine.md"), ("Review Scoring Model", f"{re}/review-scoring-model.md")],
         ["Every deliverable uses 18-section schema."]),
    ]
    for spec in knowledge_specs:
        write(f"knowledge/{spec[1]}", knowledge_article(*spec))

    write(
        "knowledge/README.md",
        fm("Playwright Review — Knowledge", "QE Specialized Skill Knowledge", "Guide", ["playwright-review"])
        + """# Playwright Review — Knowledge

Canonical encyclopedia: [`../../automation-intelligence/playwright/`](../../automation-intelligence/playwright/README.md) and [`../../automation-intelligence/review-engine/`](../../automation-intelligence/review-engine/README.md). These articles provide **PWR reasoning models**.

| Document | Focus |
|----------|-------|
| [Playwright Architecture](playwright-architecture.md) | Layering |
| [Playwright Configuration](playwright-configuration.md) | Config |
| [Page Object Model](page-object-model.md) | POM |
| [Fixtures](fixtures.md) | Fixtures |
| [Hooks](hooks.md) | Hooks |
| [Locator Strategies](locator-strategies.md) | Locators |
| [Assertions](assertions.md) | Assertions |
| [Auto Waiting](auto-waiting.md) | Auto-wait |
| [Network Mocking](network-mocking.md) | Mocking |
| [API Testing](api-testing.md) | API |
| [Authentication](authentication.md) | Auth |
| [Parallel Execution](parallel-execution.md) | Parallel |
| [Retry Strategy](retry-strategy.md) | Retries |
| [Trace Viewer](trace-viewer.md) | Traces |
| [Reporting](reporting.md) | Reports |
| [Accessibility Testing](accessibility-testing.md) | A11y |
| [Salesforce UI Automation Best Practices](salesforce-ui-automation-best-practices.md) | SF UI |
| [Salesforce Synchronization Techniques](salesforce-synchronization-techniques.md) | Sync |
| [CI/CD Integration](cicd-integration.md) | CI generic |
| [Azure DevOps](azure-devops.md) | ADO |
| [GitHub Actions](github-actions.md) | GHA |
| [Playwright Review Best Practices](playwright-review-best-practices.md) | Synthesis |
""",
    )

    playbooks = [
        ("Framework Review Playbook", "framework-review.md",
         "Assess Playwright framework structure and config.",
         ["Repo tree", "playwright.config", "Fixture/POM layout"],
         ["Map architecture layers.", "Score Sprint 8 dimensions.", "Document Framework Assessment.", "List P0–P3 gaps."],
         ["JS vs TS? Brownfield constraints?"],
         ["Framework Assessment Report", "18-section report"],
         ["Architecture scored with evidence", "No invented metrics"],
         ["Critical secrets → Security"],
         f"[{re}/automation-review-engine.md]"),
        ("Script Review Playbook", "script-review.md",
         "Review individual Playwright tests and page objects.",
         ["Sample specs", "Page objects", "Assertions"],
         ["Review locators/assertions/sync.", "Produce snippet refactors.", "Update Code Quality and Locator sections."],
         ["Full rewrite requested?"],
         ["Automation Code Review Report sections 4–7"],
         ["Actionable refactors", "Snippets only unless rewrite asked"],
         ["Systemic anti-pattern → Automation Lead"],
         ""),
        ("Locator Optimization Playbook", "locator-optimization.md",
         "Harden locators for Lightning and Experience UI.",
         ["Failing locators", "UI samples", "MIA UI deltas"],
         ["Classify brittle selectors.", "Recommend role/label/test-id.", "Chain MIA if layout changed.", "Update Locator Review."],
         ["Can product add data-testid?"],
         ["Locator Review Checklist"],
         ["Brittleness reduced or accepted residual risk"],
         ["Layout churn → MIA + Product"],
         f"[{mia}]({mia})"),
        ("Flaky Test Investigation Playbook", "flaky-test-investigation.md",
         "Investigate flake root causes before raising retries.",
         ["Failure history", "Traces", "Parallel settings"],
         ["Cluster flake themes (sync, data, env).", "Reproduce with trace.", "Fix root cause; limit retries.", "Document Flaky Test Analysis."],
         ["Infra vs app flake?"],
         ["Flaky Test Investigation Report"],
         ["Root cause hypothesized with evidence", "No invented flake %"],
         ["Release-blocking flake → Release Manager"],
         f"[{re}/flaky-and-stability-review.md]"),
        ("Salesforce UI Automation Playbook", "salesforce-ui-automation.md",
         "Review Salesforce-specific UI automation patterns.",
         ["LEX/Experience/Console scope", "Auth approach", "Sample flows"],
         ["Assess sync helpers.", "Check console/related list handling.", "Chain AFT for Agentforce UI.", "Chain PTA for persona UI."],
         ["Agentforce in scope?"],
         ["Salesforce Compatibility Review section"],
         ["SF sync strategy present", "Persona coverage noted"],
         ["No sync strategy → SF Automation Architect"],
         f"[{pw}/salesforce-best-practices.md]"),
        ("CI/CD Review Playbook", "cicd-review.md",
         "Review pipeline readiness for Playwright suites.",
         ["YAML/pipeline", "Secrets approach", "Artifact publish"],
         ["Check install/cache/browsers.", "Artifacts on fail.", "Smoke gate vs full suite.", "Score CI/CD Readiness."],
         ["ADO or GitHub Actions?"],
         ["CI/CD Readiness Report"],
         ["Secrets not in logs", "Artifacts available"],
         ["No CI for critical smoke → DevOps"],
         ""),
        ("Performance Optimization Playbook", "performance-optimization.md",
         "Reduce slow Playwright Salesforce suites without inventing timings.",
         ["Suite duration signals", "Login pattern", "Parallel config"],
         ["Find sleep and serial bottlenecks.", "Recommend storageState and API setup.", "Label duration assumptions.", "Update Performance Analysis."],
         ["Measured timings available?"],
         ["Performance Review Report"],
         ["Bottlenecks listed", "No invented SLAs"],
         ["LDV UI suite without isolation → Performance note"],
         ""),
        ("Release Automation Readiness Playbook", "release-automation-readiness.md",
         "Assemble Go/No-Go evidence for automation reliance at release.",
         ["18-section report", "Critical defects", "CI smoke results"],
         ["Confirm Critical flake/secrets closed.", "Smoke suite green in CI.", "Document residual risk.", "Issue recommendation."],
         ["Residual risk accepted by RM?"],
         ["Overall Quality Score + Recommendations"],
         ["Critical=0 or accepted", "Evidence cited"],
         ["Critical open → No-Go"],
         "../../knowledge/release/release-readiness.md"),
    ]
    for title, slug, *rest in playbooks:
        write(f"playbooks/{slug}", playbook(title, slug, *rest))

    write(
        "playbooks/README.md",
        fm("Playwright Review — Playbooks", "QE Specialized Skill Playbook", "Guide", ["playwright-review"])
        + """# Playwright Review — Playbooks

| Playbook | Focus |
|----------|-------|
| [Framework Review](framework-review.md) | Framework |
| [Script Review](script-review.md) | Scripts/POM |
| [Locator Optimization](locator-optimization.md) | Locators |
| [Flaky Test Investigation](flaky-test-investigation.md) | Flake |
| [Salesforce UI Automation](salesforce-ui-automation.md) | SF UI |
| [CI/CD Review](cicd-review.md) | CI/CD |
| [Performance Optimization](performance-optimization.md) | Performance |
| [Release Automation Readiness](release-automation-readiness.md) | Release |
""",
    )

    templates = [
        ("Automation Code Review Report", OUTPUT_SECTIONS),
        ("Framework Assessment Report", ["Purpose", "Structure", "Config", "Fixtures", "Abstraction", "Gaps", "Scores", "Recommendations"]),
        ("Locator Review Checklist", ["Role/Label/TestId", "XPath/CSS Brittleness", "SF Dynamic Components", "Iframes", "Related Lists", "Centralization", "Status"]),
        ("Performance Review Report", ["Slow Tests", "Waits", "Parallel Efficiency", "Auth/Login Cost", "Assumptions", "Recommendations"]),
        ("CI/CD Readiness Report", ["Pipeline", "Secrets", "Browsers", "Artifacts", "Gates", "Gaps", "Score"]),
        ("Flaky Test Investigation Report", ["Symptom", "Evidence", "Root Cause Hypothesis", "Fix", "Retry Policy", "Residual Risk"]),
        ("Automation Health Scorecard", ["Architecture", "POM", "Locators", "Data", "CI/CD", "Reporting", "Flake", "Security", "Overall 1-5", "Evidence Notes"]),
        ("Playwright Best Practices Checklist", ["Config", "Fixtures", "Locators", "Assertions", "Auth", "Parallel", "Traces", "CI", "SF Sync", "Secrets"]),
    ]
    for title, sections in templates:
        slug = title.lower().replace(" ", "-").replace("/", "-") + ".md"
        write(f"templates/{slug}", template_doc(title, sections))

    write(
        "templates/README.md",
        fm("Playwright Review — Templates", "QE Specialized Skill Template", "Guide", ["playwright-review"])
        + """# Playwright Review — Templates

| Template | Use |
|----------|-----|
| [Automation Code Review Report](automation-code-review-report.md) | Primary 18-section deliverable |
| [Framework Assessment Report](framework-assessment-report.md) | Framework |
| [Locator Review Checklist](locator-review-checklist.md) | Locators |
| [Performance Review Report](performance-review-report.md) | Performance |
| [CI/CD Readiness Report](ci-cd-readiness-report.md) | CI/CD |
| [Flaky Test Investigation Report](flaky-test-investigation-report.md) | Flake |
| [Automation Health Scorecard](automation-health-scorecard.md) | Scorecard |
| [Playwright Best Practices Checklist](playwright-best-practices-checklist.md) | Checklist |
""",
    )

    base = (
        "Act as Salesforce Playwright Review (PWR). Provide Framework Assessment context "
        "BEFORE line-by-line script critique. Produce all 18 sections per SKILL.md. "
        "Score 1–5 with evidence or N/A; do not invent coverage or flake %. "
        "Refactoring suggestions as snippets only unless full rewrite requested. Context:\n[paste]"
    )
    prompts = [
        ("Review Playwright Framework", "review-playwright-framework.md", base + "\nFocus: Framework Assessment and Architecture.", OUTPUT_SECTIONS),
        ("Review Test Script", "review-test-script.md", base + "\nFocus: Code Quality, Locators, Assertions, Sync.", OUTPUT_SECTIONS),
        ("Optimize Locators", "optimize-locators.md", base + "\nFocus: Locator Review and Salesforce Compatibility.", OUTPUT_SECTIONS),
        ("Improve Assertions", "improve-assertions.md", base + "\nFocus: Assertion Review; recommend SOVA when data state matters.", OUTPUT_SECTIONS),
        ("Analyze Flaky Tests", "analyze-flaky-tests.md", base + "\nFocus: Flaky Test Analysis and Retry Strategy.", OUTPUT_SECTIONS),
        ("Review Parallel Execution", "review-parallel-execution.md", base + "\nFocus: Parallel isolation and Performance Analysis.", OUTPUT_SECTIONS),
        ("Review Configuration", "review-configuration.md", base + "\nFocus: Framework Assessment and config smells.", OUTPUT_SECTIONS),
        ("Review Authentication Strategy", "review-authentication-strategy.md", base + "\nFocus: Auth/storageState and Security Considerations.", OUTPUT_SECTIONS),
        ("Review CI/CD Pipeline", "review-cicd-pipeline.md", base + "\nFocus: CI/CD Readiness (ADO or GitHub Actions).", OUTPUT_SECTIONS),
        ("Improve Test Maintainability", "improve-test-maintainability.md", base + "\nFocus: Maintainability, Refactoring Suggestions, Overall Quality Score.", OUTPUT_SECTIONS),
    ]
    for title, slug, prompt, sections in prompts:
        write(f"prompts/{slug}", prompt_doc(title, prompt, sections))

    write(
        "prompts/README.md",
        fm("Playwright Review — Prompts", "QE Specialized Skill Prompt", "Guide", ["playwright-review"])
        + """# Playwright Review — Prompts

| Prompt | File |
|--------|------|
| Review Playwright Framework | [review-playwright-framework.md](review-playwright-framework.md) |
| Review Test Script | [review-test-script.md](review-test-script.md) |
| Optimize Locators | [optimize-locators.md](optimize-locators.md) |
| Improve Assertions | [improve-assertions.md](improve-assertions.md) |
| Analyze Flaky Tests | [analyze-flaky-tests.md](analyze-flaky-tests.md) |
| Review Parallel Execution | [review-parallel-execution.md](review-parallel-execution.md) |
| Review Configuration | [review-configuration.md](review-configuration.md) |
| Review Authentication Strategy | [review-authentication-strategy.md](review-authentication-strategy.md) |
| Review CI/CD Pipeline | [review-cicd-pipeline.md](review-cicd-pipeline.md) |
| Improve Test Maintainability | [improve-test-maintainability.md](improve-test-maintainability.md) |
""",
    )

    examples = [
        ("Login Test Review", "login-test-review.md",
         "```ts\ntest('login', async ({ page }) => {\n  await page.goto(process.env.SF_URL!);\n  await page.fill('#username', process.env.SF_USER!);\n  await page.fill('#password', process.env.SF_PASS!);\n  await page.click('#Login');\n  await page.waitForTimeout(10000);\n});\n```",
         "- Hard sleep after login\n- Credentials from env OK but no storageState reuse\n- No assertion of landing page",
         "- Use storageState fixture per persona\n- Replace sleep with expect(home locator)\n- Keep secrets in CI secret store",
         "```ts\ntest.use({ storageState: 'auth/sales.json' });\ntest('home loads', async ({ page }) => {\n  await page.goto('/lightning/page/home');\n  await expect(page.getByRole('heading', { name: /Home/i })).toBeVisible();\n});\n```",
         "Never commit storageState with live cookies.",
         "Chain PTA for persona matrix; score Security and Sync."),
        ("Salesforce Record Creation Test", "salesforce-record-creation-test.md",
         "UI-only Account create with CSS selectors and no data cleanup.",
         "- Brittle CSS\n- No API setup/cleanup\n- Asserts only toast text",
         "- getByLabel for fields\n- API create optional; External ID cleanup\n- Assert record via UI + SOVA stub",
         "```ts\nawait page.getByLabel('Account Name').fill('TDG Acme Test');\nawait page.getByRole('button', { name: 'Save' }).click();\nawait expect(page.getByText('was saved')).toBeVisible();\n```",
         "Prefer TDG External IDs for cleanup.",
         "Recommend SOVA count query; TDG for seed."),
        ("Dynamic Locator Review", "dynamic-locator-review.md",
         "`page.locator('div.slds-truncate:nth-child(3)')` for related list.",
         "- Position-based CSS\n- Breaks on column reorder",
         "- Role/name within related list\n- data-testid if product allows\n- Chain MIA on FlexiPage change",
         "```ts\npage.getByRole('link', { name: 'Case 00001234' })\n```",
         "Avoid nth-child for Lightning.",
         "Locator Review Fail until hardened."),
        ("Page Object Review", "page-object-review.md",
         "God AccountPage with 40 methods and embedded waits.",
         "- Low cohesion\n- Duplicated waits\n- Business assertions inside page",
         "- Split list/detail/edit pages\n- Moves assertions to tests\n- Shared wait helpers",
         "```ts\nexport class AccountEditPage {\n  constructor(private page: Page) {}\n  name = this.page.getByLabel('Account Name');\n  async save() { await this.page.getByRole('button', { name: 'Save' }).click(); }\n}\n```",
         "Pages = actions/locators; tests = outcomes.",
         "Score POM dimension 2–3 until split."),
        ("Fixture Review", "fixture-review.md",
         "Global `page` mutated across parallel workers.",
         "- Shared mutable state\n- Race conditions",
         "- Per-test fixtures\n- Worker-scoped auth only via storageState files",
         "```ts\nexport const test = base.extend({\n  salesPage: async ({ browser }, use) => {\n    const context = await browser.newContext({ storageState: 'auth/sales.json' });\n    const page = await context.newPage();\n    await use(page);\n    await context.close();\n  },\n});\n```",
         "Isolate contexts per test.",
         "Parallel Execution + Flake sections."),
        ("API Test Review", "api-test-review.md",
         "UI login used to seed 50 Accounts before API assert.",
         "- Slow\n- UI flake coupled to API check",
         "- request.newContext with OAuth/session\n- TDG payloads\n- SOVA for verification",
         "```ts\nconst api = await request.newContext({ baseURL, extraHTTPHeaders: { Authorization: `Bearer ${token}` } });\nawait api.post('/services/data/v59.0/sobjects/Account', { data: { Name: 'TDG API Acc' } });\n```",
         "Keep secrets out of logs.",
         "Chain TDG + SOVA."),
        ("Salesforce Console App Test", "salesforce-console-app-test.md",
         "Clicks by absolute XPath across console tabs.",
         "- Console tab flake\n- No tab helper",
         "- Centralize console navigation helper\n- Role-based tab selection",
         "```ts\nawait consoleNav.openTab(page, 'Cases');\nawait expect(page.getByRole('tab', { name: 'Cases', selected: true })).toBeVisible();\n```",
         "Centralize console helpers.",
         "Salesforce Compatibility Review focus."),
        ("Experience Cloud Test", "experience-cloud-test.md",
         "Guest user test with admin storageState.",
         "- Wrong persona\n- Security false confidence",
         "- Guest vs member storageState\n- Chain PTA\n- No admin cookies for public pages",
         "```ts\ntest.use({ storageState: { cookies: [], origins: [] } }); // guest\n```",
         "Persona authenticity matters.",
         "Security + PTA chain."),
        ("Agentforce UI Test", "agentforce-ui-test.md",
         "Clicks Agentforce chat send; asserts any response text.",
         "- No grounding/guardrail evaluation\n- UI-only",
         "- Chain AFT for AI QA sections\n- UI checks for panel open/send only\n- Do not invent accuracy %",
         "```ts\nawait expect(page.getByRole('textbox', { name: /message/i })).toBeVisible();\n// Delegate response quality to AFT\n```",
         "Separate UI shell vs AI quality.",
         "Mandatory AFT cross-link."),
        ("Azure DevOps Pipeline Review", "azure-devops-pipeline-review.md",
         "ADO pipeline runs Playwright but no artifacts; PAT in YAML.",
         "- Secrets in source\n- No HTML report publish\n- No smoke vs full split",
         "- Variable group secrets\n- PublishPipelineArtifact for playwright-report\n- Smoke stage gate",
         "```yaml\n- task: PublishPipelineArtifact@1\n  inputs:\n    targetPath: playwright-report\n    artifact: playwright-report\n```",
         "Never commit PAT.",
         "CI/CD Readiness Critical until secrets fixed."),
    ]
    for title, slug, original, issues, improvements, refactored, practices, qa in examples:
        write(f"examples/{slug}", example_doc(title, original, issues, improvements, refactored, practices, qa))

    write(
        "examples/README.md",
        fm("Playwright Review — Examples", "QE Specialized Skill Example", "Guide", ["playwright-review"])
        + """# Playwright Review — Examples

| Example | Focus |
|---------|-------|
| [Login Test Review](login-test-review.md) | Auth |
| [Salesforce Record Creation Test](salesforce-record-creation-test.md) | CRUD UI |
| [Dynamic Locator Review](dynamic-locator-review.md) | Locators |
| [Page Object Review](page-object-review.md) | POM |
| [Fixture Review](fixture-review.md) | Fixtures |
| [API Test Review](api-test-review.md) | API |
| [Salesforce Console App Test](salesforce-console-app-test.md) | Console |
| [Experience Cloud Test](experience-cloud-test.md) | Experience |
| [Agentforce UI Test](agentforce-ui-test.md) | Agentforce |
| [Azure DevOps Pipeline Review](azure-devops-pipeline-review.md) | ADO CI |
""",
    )

    tests = [
        ("locator-quality", "Role/label/test-id preferred; brittle CSS/XPath flagged"),
        ("assertion-quality", "Business outcomes asserted; SOVA noted when data state matters"),
        ("framework-design", "Architecture and config assessed before script nitpicks"),
        ("synchronization", "Auto-wait over hard sleeps for Lightning"),
        ("retry-strategy", "Retries justified; not masking locator debt"),
        ("parallel-execution", "Worker isolation and data strategy reviewed"),
        ("salesforce-dynamic-ui-handling", "LEX/console/Experience sync patterns covered when UI in scope"),
        ("cicd-integration", "Artifacts, secrets, gates assessed"),
        ("reporting", "Trace/report on failure noted"),
        ("maintainability", "POM/fixtures scored with evidence"),
        ("performance", "Bottlenecks listed without invented timings"),
        ("scalability", "Parallel/projects extensibility assessed"),
    ]
    for slug, desc in tests:
        write(
            f"tests/scenario-{slug}.md",
            fm(f"Test — {slug}", "QE Specialized Skill Test", "Test Scenario", ["playwright-review"])
            + f"""# Test Scenario — {slug}

## Objective

{desc}

## Pass Criteria

- Framework context before line-by-line critique
- 1–5 scores with evidence or N/A
- No invented coverage/flake %
- Refactor suggestions as snippets unless rewrite requested

## Fail Criteria

- Script nitpicks without architecture context
- Invented metrics
- Secrets ignored when present in samples
- Selenium/Cypress treated as PWR primary (should be Sprint 8)
""",
        )

    write(
        "tests/README.md",
        fm("Playwright Review — Tests", "QE Specialized Skill Test", "Guide", ["playwright-review"])
        + """# Playwright Review — Tests

| Scenario | Focus |
|----------|-------|
| [locator-quality](scenario-locator-quality.md) | Locators |
| [assertion-quality](scenario-assertion-quality.md) | Assertions |
| [framework-design](scenario-framework-design.md) | Framework |
| [synchronization](scenario-synchronization.md) | Sync |
| [retry-strategy](scenario-retry-strategy.md) | Retries |
| [parallel-execution](scenario-parallel-execution.md) | Parallel |
| [salesforce-dynamic-ui-handling](scenario-salesforce-dynamic-ui-handling.md) | SF UI |
| [cicd-integration](scenario-cicd-integration.md) | CI/CD |
| [reporting](scenario-reporting.md) | Reporting |
| [maintainability](scenario-maintainability.md) | Maintainability |
| [performance](scenario-performance.md) | Performance |
| [scalability](scenario-scalability.md) | Scalability |
""",
    )

    print("Done.")


if __name__ == "__main__":
    main()
