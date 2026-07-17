---
title: Business Impact Analysis (Operations)
version: 0.11.1
tags: [production-support, sprint-9, operations-intelligence]
---

# Business Impact Analysis (Operations)

## Purpose

Frame operational incidents and risks in business terms (journeys, revenue, compliance, customer experience)—not only technical symptoms.

## Business Context

Executives act on impact; engineers act on components. Ops intelligence must translate both ways.

## Lifecycle

Identify affected journeys/personas → Estimate impact scale → Map to severity → Communicate → Drive priority.

## Roles / Responsibilities

Business Product Owner confirms impact; Support Lead drafts BIA; Compliance engaged when regulatory.

## Inputs

Affected processes, volume of users/transactions (if known), time window, workaround availability, regulatory flags.

## Outputs

Impact statement, severity recommendation, executive one-liner, confidence, open questions.

## Activities

1. Name the business journey (e.g., Case intake, Order submit, Field Service dispatch).  
2. Note workaround existence.  
3. Align severity matrix.  
4. Feed release deferral or major-incident declaration decisions.  

## KPIs / SLAs

Impact accuracy vs PIR findings (qualitative learning).

## Risks

- Overstating impact to force priority  
- Understating compliance-relevant access issues  

## Best Practices

- Never invent transaction volumes—mark TBC.  
- Separate customer-facing vs internal-admin impact.  

## Examples

Experience Cloud login failure for partners during business hours → High CX + revenue risk → Sev1 candidate.

## Interview Questions

- How do you write a business impact statement for Salesforce outages?  

## References

- [../incident-management/business-impact-assessment.md](../incident-management/business-impact-assessment.md)
- [../incident-management/severity-matrix.md](../incident-management/severity-matrix.md)

## Related Documents

- [Dependency Mapping](dependency-mapping.md)
- [Recommendations Engine](recommendations-engine.md)

## Navigation

- **Previous:** [sla-breach-prediction.md](sla-breach-prediction.md)
- **Next:** [dependency-mapping.md](dependency-mapping.md)

## Future Enhancements

- Journey→component impact catalog  
