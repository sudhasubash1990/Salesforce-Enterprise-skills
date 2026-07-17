---
title: Requirement Review Report
module: Salesforce Quality Engineering
category: Template
document_type: Template
version: 0.7.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
review_cycle: quarterly
keywords: [requirement-review-report, template, documentation-generator]
tags: [template, sprint-5]
---

# Requirement Review Report

**Template ID:** TPL-REQUIREMENT_REVIEW_REPORT  
**Lifecycle phase:** Discover / Refine  
**Methodology fit:** Agile / Scrum / SAFe / Waterfall (tailor sections)

---

## Purpose

Document QE requirement review outcomes: quality score, gaps, questions, risks, and recommendations—without inventing scope.

## Business Context

After Requirement Analysis Engine run on a story/epic/BRD excerpt.

Consulting-grade artifact for Salesforce Quality Engineering programs. Reuse across industries; tailor depth to project size and risk.

## Audience

- QE team
- Delivery leadership
- BA
- Development

## Owner

**Primary owner:** QE Analyst / Test Lead

## Document Intelligence

| Attribute | Guidance |
|-----------|----------|
| **When to create** | After Requirement Analysis Engine run on a story/epic/BRD excerpt. |
| **Owner** | QE Analyst / Test Lead |
| **Reviewers** | BA, SA (as applicable), Delivery Lead |
| **Approvers** | Delivery Lead / Release Manager |
| **Project phase** | Discover / Refine |

## Inputs

- Requirement / story / AC
- Sprint 2 analysis outputs

## Outputs

- Review report
- Clarification questions
- Quality score

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

1. **Executive Summary**
2. **Quality Score**
3. **Gaps**
4. **Questions**
5. **Risks**
6. **Salesforce Component Impact**
7. **Recommendations**
8. **Next Steps**

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

1. Author (QE Analyst / Test Lead) → draft complete  
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
- [Requirement Gap Analysis](requirement-gap-analysis.md)
- [Requirement Quality Assessment](requirement-quality-assessment.md)
- [Risk Assessment](risk-assessment.md)
- [Document Intelligence](../guidelines/document-intelligence.md)
- [Deliverable Selection](../guidelines/deliverable-selection.md)
- [README.md](README.md)

## Example Output

_Illustrative skeleton — replace with project content._

**Requirement Review Report** — Project PRJ-XXX | Sprint/Release N | Status: Draft

## Future Enhancements

- Sprint 6: deeper Azure DevOps field mapping
- Industry-specific examples under `scenarios/`
