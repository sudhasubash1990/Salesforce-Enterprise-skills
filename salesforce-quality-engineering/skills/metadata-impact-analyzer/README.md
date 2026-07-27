---
title: Metadata Impact Analyzer — README
module: Salesforce Quality Engineering
category: Specialized Skill
document_type: Guide
version: 0.15.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [metadata-impact-analyzer]
---

# Metadata Impact Analyzer

## Purpose

Enterprise AI skill for analyzing Salesforce metadata changes **before deployment** and identifying downstream business, technical, security, integration, automation, and reporting impacts.

Thinks as a blend of **Technical Architect**, **Solution Architect**, **QA Architect**, and **Release Manager** — never as a test-case generator alone.

## Capabilities

- Metadata dependency graph construction
- Multi-dimensional impact analysis (business, technical, security, integration, automation, reporting)
- Risk-based regression scope (In / Out / Conditional)
- Deployment risk and Go/No-Go recommendation
- SOQL validation pack and manual test priorities (after analysis)
- Automation candidate advisory (design only — no full scripts)

## Folder Structure

```
metadata-impact-analyzer/
├── SKILL.md              ← Load first
├── README.md             ← This file
├── skill-config.yaml     ← Routing keywords and output schema
├── knowledge/            ← Reasoning models (cross-link Sprint 4A)
├── playbooks/            ← Ceremonies and workflows
├── templates/            ← Deliverable shells
├── prompts/              ← Reusable Cursor prompts
├── examples/             ← Realistic change scenarios
└── tests/                ← Validation scenarios
```

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Change manifest | Yes | package.xml, change set list, or metadata diff |
| Target environment | Recommended | Sandbox name, promotion path |
| Personas | Recommended | Profiles, permission sets, community users |
| Integration inventory | When applicable | Named credentials, connected apps, APIs |
| Release window | Recommended | For Go/No-Go context |

## Outputs

Every analysis produces **16 sections** (see [SKILL.md](SKILL.md#output-schema)):

Executive Summary · Metadata Changed · Dependency Analysis · Business Impact · Technical Impact · Security Impact · Integration Impact · Automation Impact · Reporting Impact · Regression Scope · Deployment Risk · Risk Rating · Automation Candidates · Recommended SOQL Validations · Recommended Manual Tests · Go / No-Go Recommendation

Primary template: [templates/metadata-impact-report.md](templates/metadata-impact-report.md)

## Usage

1. Load Tier-0 `framework-core/` and parent QE `skill.md`.
2. Confirm Enterprise Orchestrator routes to this skill.
3. Load [SKILL.md](SKILL.md) + [skill-config.yaml](skill-config.yaml).
4. Attach change manifest; run [prompts/impact-analysis.md](prompts/impact-analysis.md).
5. Save deliverable under `outputs/<project>/` and run output-engine conversion.

## Sample Prompts

```
Analyze this Salesforce deployment package. Perform complete dependency analysis
before any test recommendations. Produce all 16 Metadata Impact Analyzer sections.
Change: [paste package.xml or change list]
Personas: Sales Agent, Sales Manager, Integration User
Target: UAT → Production
```

See [prompts/README.md](prompts/README.md) for specialized prompts (Flow, VR, security, etc.).

## Examples

| Example | File |
|---------|------|
| Custom field + Flow | [examples/custom-field-added.md](examples/custom-field-added.md) |
| Validation rule + API | [examples/validation-rule-changed.md](examples/validation-rule-changed.md) |
| Profile / community | [examples/profile-updated.md](examples/profile-updated.md) |
| Integration / NC | [examples/integration-modified.md](examples/integration-modified.md) |

Full index: [examples/README.md](examples/README.md)

## Known Limitations

- Does not execute live Metadata API, Tooling API, or org queries (recommends SOQL packs for humans/tools).
- Does not generate full automation scripts (Sprint 8 design only).
- Does not invent coverage %, SLA, MTTR, or certification levels.
- Managed package internals require vendor release notes — mark Partial when unknown.

## Future Enhancements

- CI hook validating 16-section schema on agent output
- Golden dataset expansion per industry
- Optional linkage to ADO deployment work items (Sprint 6)

## Related Documents

- [SKILL.md](SKILL.md)
- [../../knowledge/metadata/metadata-impact-analysis.md](../../knowledge/metadata/metadata-impact-analysis.md)
- [../../enterprise-orchestrator/capability-routing-table.md](../../enterprise-orchestrator/capability-routing-table.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.15.0 | 2026-07-27 | QE Practice Lead | Initial release |
