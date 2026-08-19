---
title: Salesforce Mobile Testing
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, mobile-testing]
---

# Salesforce Mobile Testing

## Purpose

Reference for assessing mobile testing scope for Salesforce mobile experiences.

## Mobile Test Areas

| Area | What to Assess |
|------|----------------|
| **Salesforce Mobile app** | Record pages, compact layouts, mobile actions, quick actions |
| **Responsive UI** | Desktop-to-mobile breakpoint behavior, SLDS grid |
| **Mobile layouts** | Mobile cards, compact layouts, highlights panel |
| **Touch interactions** | Tap targets (≥44px), swipe gestures, pinch-to-zoom, long press |
| **Offline** | Offline briefcase, cached data, sync on reconnect, conflict resolution |
| **Mobile navigation** | Navigation bar items, utility bar, record actions |
| **LWC responsive** | CSS media queries, conditional rendering for mobile viewport |

## Platform Considerations

### Salesforce Mobile App
- iOS and Android supported versions per Salesforce release notes
- Mobile-only features: barcode scanning, voice, geolocation
- Compact layout drives mobile record header

### Field Service Lightning (FSL) Mobile
- Work order lifecycle on mobile
- Service appointment flow
- Parts consumption, asset management
- Offline-first with background sync

### Experience Cloud Mobile
- Responsive templates and custom themes
- Mobile navigation component
- Touch-optimized components

## Key Test Scenarios

1. Record creation and edit on mobile form factor
2. Offline record access and creation → sync verification
3. Push notification receipt and navigation
4. Mobile action execution (quick actions, global actions)
5. Responsive layout at phone and tablet breakpoints

## Related

- [Accessibility Testing](accessibility-testing.md) — Mobile accessibility overlap
- [Compatibility Testing](compatibility-testing.md) — Device matrix
- [Specialized Testing Model](specialized-testing-model.md)
