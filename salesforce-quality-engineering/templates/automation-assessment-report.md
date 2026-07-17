---
title: Automation Assessment Report
module: Salesforce Quality Engineering
category: Template
document_type: Template
version: 0.7.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
review_cycle: quarterly
keywords: [automation-assessment-report, template, documentation-generator]
tags: [template, sprint-5]
---

# Automation Assessment Report

**Template ID:** TPL-AUTOMATION_ASSESSMENT_REPORT  
**Lifecycle phase:** Plan / Design  
**Methodology fit:** Agile / Scrum / SAFe / Waterfall (tailor sections)

---

## Purpose

Assess automation feasibility, ROI themes, and readiness (no scripts required).

## Business Context

When deciding what to automate for a release or program.

Consulting-grade artifact for Salesforce Quality Engineering programs. Reuse across industries; tailor depth to project size and risk.

## Audience

- QE team
- Delivery leadership
- BA
- Development

## Owner

**Primary owner:** Automation Lead / QE Lead

## Document Intelligence

| Attribute | Guidance |
|-----------|----------|
| **When to create** | When deciding what to automate for a release or program. |
| **Owner** | Automation Lead / QE Lead |
| **Reviewers** | BA, SA (as applicable), Delivery Lead |
| **Approvers** | Delivery Lead / Release Manager |
| **Project phase** | Plan / Design |

## Inputs

- Approved scope / stories
- Risks
- Environment plan

## Outputs

- Completed Automation Assessment Report

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

1. **Purpose**
2. **Scope**
3. **Details**
4. **Risks**
5. **Approvals**

## Mandatory Fields

- Document ID
- Version
- Status
- Owner
- Date

## Optional Fields

- Screenshots
- Appendix

## Review Checklist

- Purpose and audience clear
- Inputs/outputs listed
- Traceability IDs present where required
- No client PII / credentials
- Aligned to engines (analysis → design → document)

## Approval Flow

1. Author (Automation Lead / QE Lead) → draft complete  
2. Reviewers (BA, SA (as applicable), Delivery Lead) → comments resolved  
3. Approvers (Delivery Lead / Release Manager) → approved  
4. Baseline version; link in RTM / release pack as applicable  

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.1.0 | YYYY-MM-DD | [Name] | Initial draft |
| 0.2.0 | YYYY-MM-DD | [Name] | Review updates |
| 1.0.0 | YYYY-MM-DD | [Name] | Approved baseline |

## Related Documents

- [QE Brain (Sprint 1)](../brain/README.md)
- [Requirement Analysis (Sprint 2)](../knowledge/requirement-analysis.md)
- [Test Design Engine (Sprint 3)](../knowledge/test-design-engine.md)
- [Platform Foundation 4A](../knowledge/platform/README.md)
- [Enterprise Knowledge 4B](../knowledge/clouds/README.md)
- [Automation Candidate Matrix](automation-candidate-matrix.md)
- [Document Intelligence](../guidelines/document-intelligence.md)
- [Deliverable Selection](../guidelines/deliverable-selection.md)
- [README.md](README.md)

## Example Output

_Illustrative skeleton — replace with project content._

**Automation Assessment Report** — Project PRJ-XXX | Sprint/Release N | Status: Draft

## Future Enhancements

- Sprint 6: deeper Azure DevOps field mapping
- Industry-specific examples under `scenarios/`
