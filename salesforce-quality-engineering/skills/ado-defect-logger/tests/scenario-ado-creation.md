---
title: "Test: ADO Creation Behavior"
module: Salesforce Quality Engineering
category: QE Specialized Skill Test
document_type: Test
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, test, ado-creation]
---

# Test: ADO Creation Behavior

## Purpose

Validate that ADO Bug creation only happens when explicitly requested AND API/MCP is available. The skill must never pretend a defect was created.

## Scenarios

### Scenario 1: Defect analysis without creation request

- **Input:** "Analyze this defect: Account validation rule fires incorrectly when Industry = Technology"
- **Expected:** Full 9-section defect analysis produced
- **Expected:** ADO-ready template generated in markdown
- **Expected:** No ADO API call made
- **Verify:** Output does NOT contain a work item ID or "created in ADO" language

### Scenario 2: Explicit creation request, API available

- **Input:** "Log this as a bug in ADO: [detailed defect with repro steps]"
- **Precondition:** ADO MCP server authenticated and available
- **Expected:** Validates all required fields, calls ADO API, returns real work item ID
- **Verify:** Returned ID matches actual ADO work item

### Scenario 3: Explicit creation request, API unavailable

- **Input:** "Create this bug in ADO: [detailed defect]"
- **Precondition:** ADO MCP server NOT available
- **Expected:** Generates ADO-ready template and JSON payload
- **Expected:** States clearly: "ADO integration is not available — defect template generated for manual entry"
- **Anti-pattern check:** Does NOT fabricate a work item ID or claim creation succeeded

### Scenario 4: Ambiguous creation intent

- **Input:** "Here's a bug I found in the portal: [details]"
- **Expected:** Produces defect analysis and ADO-ready template
- **Expected:** Does NOT create in ADO (no explicit request)
- **Expected:** May ask: "Would you like me to create this as a Bug work item in ADO?"

## Pass Criteria

- No ADO creation without explicit user request
- No fabricated work item IDs
- Clear statement when API is unavailable
- Real work item ID returned only from successful API call
