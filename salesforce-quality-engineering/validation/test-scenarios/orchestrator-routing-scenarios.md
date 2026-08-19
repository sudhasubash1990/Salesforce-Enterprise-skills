---
title: Orchestrator Routing Scenarios
version: 0.14.0
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
| ORCH-07 | Test Service Cloud case creation and escalation | SFT |
| ORCH-08 | Test this LWC customer search component | LFUT |
| ORCH-09 | Act as Product Owner and prepare UAT scenarios for opportunity approval | SPUAT |
| ORCH-10 | Create test cases from this user story | ATCD |
| ORCH-11 | Log this Salesforce issue as an Azure DevOps bug | ADL |
| ORCH-12 | What specialized testing do we need for this Salesforce release? | SST |

---

### ORCH-07 — Salesforce Functional Testing routing

- **Input:** "Test Service Cloud case creation and escalation"
- **Expected primary:** SFT
- **Expected supports:** PTA (permission scenarios), SOVA (backend validation), TDG (test data)
- **Pass:** SFT primary selected; chains PTA/SOVA/TDG
- **Fail:** Routes to Sprint 4B or Sprint 3 instead of SFT

### ORCH-08 — LWC & Flow UI Testing routing

- **Input:** "Test this LWC customer search component"
- **Expected primary:** LFUT
- **Expected supports:** PWR (if Playwright automation requested)
- **Pass:** LFUT primary; chains PWR when automation intent present
- **Fail:** Routes to Sprint 4A or Sprint 8 instead of LFUT

### ORCH-09 — Salesforce PO/UAT Testing routing

- **Input:** "Act as Product Owner and prepare UAT scenarios for opportunity approval"
- **Expected primary:** SPUAT
- **Expected supports:** ATCD (ADO test cases), SFT (technical scenarios)
- **Pass:** SPUAT primary with business-language output; chains ATCD when ADO test cases requested
- **Fail:** Routes to Sprint 3 or Sprint 5 instead of SPUAT

### ORCH-10 — ADO Test Case Designer routing

- **Input:** "Create test cases from this user story"
- **Expected primary:** ATCD
- **Expected default format:** Azure DevOps test case
- **Pass:** ATCD selected; ADO format default; user template overrides when provided
- **Fail:** Routes to Sprint 5 or Sprint 6; uses wrong output format

### ORCH-11 — ADO Defect Logger routing

- **Input:** "Log this Salesforce issue as an Azure DevOps bug"
- **Expected primary:** ADL
- **Pass:** ADL selected; numbered repro steps; vague defects rejected
- **Fail:** Routes to Sprint 7 instead of ADL; pretends ADO creation without API

### ORCH-12 — Salesforce Specialized Testing routing

- **Input:** "What specialized testing do we need for this Salesforce release?"
- **Expected primary:** SST
- **Expected supports:** PTA (security), DMQA (data), MIA (deployment), RBRR (regression)
- **Pass:** SST primary; chains appropriate dimension skills; never invents performance metrics
- **Fail:** Routes to Sprint 3 or individual skill instead of SST orchestration
