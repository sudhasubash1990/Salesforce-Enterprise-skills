---
title: "Example: Security Testing Assessment"
module: Salesforce Quality Engineering
category: QE Specialized Skill Examples
document_type: Example
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, security-testing, example]
---

# Example: Security Testing Assessment

> Security testing assessment for Experience Cloud partner portal with custom sharing model.

## 1. Intent

Assess security testing scope for a new Experience Cloud partner portal allowing channel partners to view their accounts, submit orders, and track cases — with a custom sharing model restricting visibility to partner-owned records.

## 2. Context

| Attribute | Value |
|-----------|-------|
| Salesforce Clouds | Sales Cloud, Service Cloud, Experience Cloud |
| Key Features | Partner Portal, Orders, Cases, Knowledge |
| Integrations | None (portal-only release) |
| Environment | Partial sandbox |

## 3. Assumptions

| ID | Assumption | Status |
|----|-----------|--------|
| A1 | Partner Community license used | Assumed |
| A2 | OWD for Account set to Private | Assumed |
| A3 | Sharing sets used for partner account access | Assumed |
| A4 | Guest user access limited to Knowledge articles | Assumed |

## 5. Testing Dimension Assessment

| Dimension | Required | Rationale | Chain Skill |
|-----------|----------|-----------|-------------|
| Security | Yes | Partner portal, sharing model, guest user | PTA |
| Integration | No | No external integrations | — |
| Data | No | No data migration | — |
| API | No | No custom APIs | — |
| Performance | No | Low initial user volume | — |
| Accessibility | Yes | Public-facing portal (WCAG AA) | — |
| Mobile | No | Desktop-only portal | — |
| Compatibility | Yes | Public portal across browsers | — |
| Regression | Yes | Sharing changes affect internal users | RBRR |
| Release/Deployment | Yes | Experience Cloud site + sharing config | MIA |

## 6. Security Assessment

### CRUD / FLS
| Object | Partner User | Guest User |
|--------|-------------|------------|
| Account | Read | None |
| Contact | Read | None |
| Order | Create, Read | None |
| Case | Create, Read | None |
| Knowledge | Read | Read |

### Sharing Model
- **OWD:** Account = Private, Order = Controlled by Parent, Case = Private
- **Sharing sets:** Partner users see Account and related records where they are the partner user's account
- **Restriction rules:** None identified — verify no oversharing via role hierarchy

### Guest User Risks
- Guest profile must not grant access to Account, Contact, Order, or Case objects
- Knowledge articles must be filtered to public categories only
- Guest user should not see internal-only knowledge
- Unauthenticated pages must not expose record IDs in URLs

### Experience Cloud
- Partner login flow (username/password + optional MFA)
- Session timeout and re-authentication
- Portal navigation limited to authorized tabs

**Chain to PTA** for detailed security test scenarios including negative paths (partner A cannot see partner B's records), guest user boundary testing, and SOQL validation of sharing enforcement.

## 11. Accessibility Assessment

- Experience Cloud portal requires WCAG AA compliance (A4)
- Custom theme contrast ratios must meet 4.5:1 for normal text
- Form fields for order submission and case creation need proper labels
- Error messaging must be accessible to screen readers

## 16. Quality Gates

| Gate | Status | Evidence |
|------|--------|----------|
| Dimension assessment complete | Pass | 10 dimensions assessed |
| Chain skills identified | Pass | PTA, RBRR, MIA |
| No invented metrics | Pass | No performance claims |
| Assumptions labeled | Pass | A1–A4 documented |

## 18. Recommended Next Actions

| # | Action | Skill | Priority |
|---|--------|-------|----------|
| 1 | Detailed security test scenarios for partner portal | PTA | Critical |
| 2 | Guest user boundary testing | PTA | Critical |
| 3 | Regression scope for sharing model changes | RBRR | High |
| 4 | Metadata impact analysis | MIA | Medium |
| 5 | Accessibility audit of portal pages | Manual | Medium |
| 6 | Browser compatibility testing for portal | Manual | Low |
