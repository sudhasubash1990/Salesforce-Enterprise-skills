---
title: Test Case Document
module: Salesforce Quality Engineering
category: Template
document_type: Template
version: 0.7.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
review_cycle: quarterly
keywords: [test-case-document, template, documentation-generator]
tags: [template, sprint-5]
---

# Test Case Document

**Template ID:** TPL-TEST_CASE_DOCUMENT  
**Lifecycle phase:** Design / Execute  
**Methodology fit:** Agile / Scrum / SAFe / Waterfall (tailor sections)

---

## Purpose

Author executable test cases for ADO, Excel, Jira Xray, Zephyr, or manual packs.

## Business Context

When executable steps are required—after scenario objectives exist. Prefer nested Given/When/Then style where ADO-compatible.

Consulting-grade artifact for Salesforce Quality Engineering programs. Reuse across industries; tailor depth to project size and risk.

## Audience

- QE team
- Delivery leadership
- BA
- Development

## Owner

**Primary owner:** QE Analyst / Tester

## Document Intelligence

| Attribute | Guidance |
|-----------|----------|
| **When to create** | When executable steps are required—after scenario objectives exist. Prefer nested Given/When/Then style where ADO-compatible. |
| **Owner** | QE Analyst / Tester |
| **Reviewers** | BA, SA (as applicable), Delivery Lead |
| **Approvers** | Delivery Lead / Release Manager |
| **Project phase** | Design / Execute |

## Inputs

- Approved scope / stories
- Risks
- Environment plan

## Outputs

- Completed Test Case Document

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

1. **Case ID**
2. **Title**
3. **Objective**
4. **Preconditions**
5. **Test Data**
6. **Steps**
7. **Expected Results**
8. **Postconditions**
9. **Priority**
10. **Requirement Mapping**
11. **Automation Candidate**
12. **Tags (Smoke/Regression/UAT)**
13. **Tool format notes (ADO/Excel/Xray/Zephyr)**

## Mandatory Fields

- Case ID
- Title
- Steps
- Expected Results
- Requirement/Scenario link
- Priority

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

1. Author (QE Analyst / Tester) → draft complete  
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
- [Test Scenario Document](test-scenario-document.md)
- [Requirement Traceability Matrix (RTM)](rtm.md)
- [Defect Report](defect-report.md)
- [Document Intelligence](../guidelines/document-intelligence.md)
- [Deliverable Selection](../guidelines/deliverable-selection.md)
- [README.md](README.md)

## Example Output

**TC-0142** — CSR updates preferred communication method  
Preconditions: CSR persona; Account with Contact  
| Step | Action | Expected |
|------|--------|----------|
| 1 | Open Contact | Record loads |
| 2 | Set Preferred Method = Email | Value saves; no error |

## Future Enhancements

- Sprint 6: deeper Azure DevOps field mapping
- Industry-specific examples under `scenarios/`
