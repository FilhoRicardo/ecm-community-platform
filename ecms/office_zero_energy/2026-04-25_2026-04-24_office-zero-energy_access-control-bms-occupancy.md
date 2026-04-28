---
Main System: BMS / Access Control / Lighting Integration
Secondary System:
Utility Affected: Electricity
Building: Office — European Portfolio
---

# ECM: Link Access Control / Lighting System to BMS for Occupancy

## Summary

**What:** Use existing access card data (badge swipes, turnstile counts) or lighting system occupancy signals as a proxy for building/floor occupancy, fed into BMS to modulate HVAC and lighting in real time.

**Why:** At XYZ Building, One Coleman Street (Simmtronic), and Radisson Blu Stansted, existing badge/integration infrastructure can be repurposed for occupancy-based HVAC control without installing new sensors.

## Estimated Savings
- 8–15% HVAC + lighting energy
- Building-specific

## Basis / References
- Portfolio basis: XYZ Building, One Coleman Street (Simmtronic), Radisson Blu Stansted

## Assumptions
- Building-specific survey required before implementation
- Energy audit recommended to quantify baseline and savings

## Implementation Essentials
1. 1) Audit access control system data output (API, BACnet, or relay signals). 2) Map badge data to floor/zone level — aggregate, not individual room-level. 3) Configure BMS: HVAC ON when >10% badge count of design occupancy
2. setback when <10%. 4) Commission to avoid false triggers — badge in then leave still counts as occupied for 30 min. 5) Integrate lighting (Simmtronic at One Coleman) for combined HVAC + lighting occupancy logic.

## Risks / Constraints
- Badge data is a lagging indicator — someone badged in may have left. Works best as floor/zone aggregate, not room-level.

## KPIs
- Floor occupancy rate by hour (%)
- HVAC runtime in unoccupied zones (hrs/day)
- Badge-to-HVAC response time (min)

## M&V Plan (IPMVP Option C with submetering where feasible)
- Pre-installation baseline: 90-day continuous monitoring
- Post-installation: compare same period following year (weather-normalised)
- IPMVP Option C: Whole-building metering with regression analysis

## Costs & Payback (indicative)
- Payback: 3–9 months
- Cost: Requires building-specific survey and contractor pricing
