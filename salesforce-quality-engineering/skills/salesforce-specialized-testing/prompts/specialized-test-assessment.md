---
title: Specialized Test Assessment Prompt
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompts
document_type: Prompt
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, prompt]
---

# Specialized Test Assessment Prompt

## Usage

Use this prompt when you need a full specialized testing assessment across all 10 dimensions.

## Prompt

```
Assess the specialized testing dimensions required for the following Salesforce implementation:

**Implementation context:**
[Describe the Salesforce implementation — clouds, features, objects, integrations, changes]

**Known requirements:**
- Security: [any known security requirements]
- Integration: [any known integrations]
- Performance: [any known SLAs or performance requirements]
- Accessibility: [any known WCAG requirements]
- Mobile: [any mobile requirements]

**Produce:**
1. Testing Dimension Assessment matrix (all 10 dimensions)
2. Detailed assessment for each required dimension
3. Chain recommendations to downstream skills (PTA, DMQA, MIA, RBRR)
4. Quality gates and recommended next actions

Follow the 18-section SST output schema. Do not invent performance metrics. Label all assumptions.
```

## Expected Output

18-section Specialized Testing Report per [templates/specialized-testing-report.md](../templates/specialized-testing-report.md).
