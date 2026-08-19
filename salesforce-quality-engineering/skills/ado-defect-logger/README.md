---
title: ADO Defect Logger — README
module: Salesforce Quality Engineering
category: QE Specialized Skill README
document_type: README
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, readme]
---

# ADO Defect Logger

Analyze Salesforce issues, structure them as ADO-ready Bug work items with evidence, and create ADO bugs when MCP/API integration is available.

## Quick Start

1. Load [SKILL.md](SKILL.md) and [skill-config.yaml](skill-config.yaml)
2. Provide defect input (error message, screenshot, test failure, user complaint)
3. Skill analyzes, structures, and produces an ADO-ready defect
4. If ADO integration is available and user explicitly requests creation → creates Bug work item

## Directory Structure

```
ado-defect-logger/
├── SKILL.md                 # Skill entry point
├── README.md                # This file
├── skill-config.yaml        # Routing, keywords, output schema
├── knowledge/
│   ├── ado-defect-model.md          # ADO Bug fields, states, transitions
│   ├── defect-quality.md            # Good defect report standards
│   ├── severity-priority-model.md   # Severity/Priority definitions
│   └── root-cause-analysis.md       # RCA hypothesis framework
├── playbooks/
│   ├── README.md
│   ├── defect-logging.md            # End-to-end defect logging process
│   ├── defect-triage.md             # Triage and prioritization
│   ├── severity-priority-assessment.md
│   └── defect-reproduction.md       # Reproducing and validating defects
├── templates/
│   ├── README.md
│   ├── ado-defect-template.md       # Full ADO Bug format
│   ├── defect-analysis-report.md    # 9-section analysis report
│   └── severity-priority-matrix.md  # Decision matrix
├── prompts/
│   ├── README.md
│   ├── analyze-defect.md
│   ├── generate-ado-defect.md
│   └── defect-triage.md
├── examples/
│   ├── README.md
│   ├── salesforce-flow-failure.md
│   ├── experience-cloud-access-error.md
│   └── integration-api-failure.md
└── tests/
    ├── README.md
    ├── scenario-defect-routing.md
    ├── scenario-vague-rejection.md
    ├── scenario-ado-creation.md
    └── scenario-repro-quality.md
```

## Key Principles

- **Never pretend** a defect was created in ADO without confirmed API success
- **Always ask** for evidence when defect description is vague
- **Repro steps** must be numbered and reproducible by another tester
- **Severity/priority** must be justified with business and technical impact
- **Root cause** hypothesis is always provided, labeled with confidence

## Upstream Skills

- [Salesforce Functional Testing](../salesforce-functional-testing/)
- [LWC/Flow UI Testing](../lwc-flow-ui-testing/)
- [Salesforce UAT/PO Testing](../salesforce-uat-po-testing/)
- [ADO Test Case Designer](../ado-test-case-designer/)

## Downstream Capabilities

- [Quality Intelligence](../../quality-intelligence/) — defect trend analysis
- [Metadata Impact Analyzer](../metadata-impact-analyzer/) — regression from metadata changes
- [Production Support](../../production-support/) — Sev1 escalation

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
