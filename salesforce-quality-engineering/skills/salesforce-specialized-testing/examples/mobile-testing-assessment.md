---
title: "Example: Mobile Testing Assessment"
module: Salesforce Quality Engineering
category: QE Specialized Skill Examples
document_type: Example
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, mobile-testing, example]
---

# Example: Mobile Testing Assessment

> Mobile testing assessment for Field Service Lightning (FSL) mobile deployment.

## 1. Intent

Assess mobile testing scope for FSL mobile rollout enabling field technicians to manage work orders, service appointments, parts consumption, and customer signatures on mobile devices.

## 2. Context

| Attribute | Value |
|-----------|-------|
| Salesforce Clouds | Service Cloud, Field Service |
| Key Features | Work Orders, Service Appointments, Parts, Signatures |
| Integrations | Inventory system (REST API) |
| Environment | Full sandbox |

## 3. Assumptions

| ID | Assumption | Status |
|----|-----------|--------|
| A1 | iOS and Android devices supported | Assumed |
| A2 | Offline capability required for field work | Assumed |
| A3 | Barcode scanning for parts consumption | Assumed |
| A4 | Customer signature capture on completion | Assumed |

## 5. Testing Dimension Assessment

| Dimension | Required | Rationale | Chain Skill |
|-----------|----------|-----------|-------------|
| Security | Yes | Field technician profile, mobile access | PTA |
| Integration | Yes | Inventory system REST API | — |
| Data | No | No data migration | — |
| API | Yes | Inventory lookup API | — |
| Performance | Yes | Offline sync, large work order volumes | Advisory |
| Accessibility | No | Internal app, no WCAG mandate | — |
| Mobile | Yes | Primary use case is mobile | — |
| Compatibility | Yes | iOS + Android device matrix | — |
| Regression | Yes | Service Cloud changes affect desktop | RBRR |
| Release/Deployment | Yes | FSL package + custom config | MIA |

## 12. Mobile Assessment

### Salesforce Field Service Mobile App
- Work order lifecycle: assigned → traveling → on-site → completed
- Service appointment scheduling and status updates
- Parts consumption with barcode scanning (A3)
- Customer signature capture on work order completion (A4)
- Time sheet entry on mobile

### Offline Testing
- **Briefcase configuration:** Work orders, service appointments, parts for the day
- **Offline creation:** Create service report while offline
- **Sync on reconnect:** Verify data syncs without conflict when connectivity restored
- **Conflict resolution:** Two technicians update same work order offline — merge behavior

### Touch and Device
- Barcode scanner camera integration
- Signature pad touch accuracy
- Map navigation for service appointments
- Swipe gestures for work order status progression

### Device Matrix
| Device | OS | Priority |
|--------|----|----------|
| iPhone (latest) | iOS 17+ | Primary |
| iPad | iOS 17+ | Secondary |
| Samsung Galaxy | Android 14+ | Primary |
| Android tablet | Android 14+ | Tertiary |

## 13. Compatibility Assessment

- FSL mobile app versions per Salesforce release compatibility
- iOS and Android minimum version requirements
- Device-specific features: camera resolution for barcode, GPS accuracy

## 10. Performance Advisory

**Risk areas identified:**
- Offline briefcase sync time for large work order volumes
- Barcode scanning response time on lower-end devices
- GPS location accuracy in poor connectivity areas

*Performance evidence not provided — measurements required from performance engineering.*

## 16. Quality Gates

| Gate | Status | Evidence |
|------|--------|----------|
| Dimension assessment complete | Pass | 10 dimensions assessed |
| Chain skills identified | Pass | PTA, RBRR, MIA |
| No invented metrics | Pass | Performance stated as "evidence not provided" |
| Assumptions labeled | Pass | A1–A4 documented |

## 18. Recommended Next Actions

| # | Action | Skill | Priority |
|---|--------|-------|----------|
| 1 | Security test scenarios for field tech profile | PTA | High |
| 2 | Mobile functional testing on device matrix | Manual | High |
| 3 | Offline sync testing | Manual | High |
| 4 | Integration test for inventory API | Manual | Medium |
| 5 | Regression scope for Service Cloud | RBRR | Medium |
| 6 | Metadata impact for FSL deployment | MIA | Medium |
| 7 | Performance engineering for offline sync | External | Low |
