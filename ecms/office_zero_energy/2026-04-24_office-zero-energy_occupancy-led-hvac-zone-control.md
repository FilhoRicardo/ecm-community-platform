---
Main System: HVAC / Zone Control
Secondary System:
Utility Affected: Natural Gas, Electricity
Building: Office — European Portfolio
---

# ECM: Occupancy-Led HVAC Zone Control

## Summary

**What:** Use occupancy data (access control, booking systems, PIR sensors) to batch HVAC to only serve occupied zones/floors, rather than conditioning whole floors on a fixed schedule. Works where zone isolation exists.

**Why:** At XYZ, Radisson, One Coleman Street, Akzo Nobel, UN Studio, and 5 Keizers, HVAC serves entire floors regardless of actual occupancy. Zoning capability varies — fan-coil and VRF systems are easiest to control per-room.

## Estimated Savings
- 10–20% HVAC energy in multi-zone buildings
- Building-specific

## Basis / References
- Portfolio basis: XYZ, Radisson Blu Stansted, One Coleman Street, Akzo Nobel, UN Studio, 5 Keizers

## Assumptions
- Building-specific survey required before implementation
- Energy audit recommended to quantify baseline and savings

## Implementation Essentials
1. 1) Audit HVAC distribution — confirm zones are physically isolatable (VAV boxes, FCU loops, VRF branches). 2) Install occupancy sensors or integrate access control data (ECM-06). 3) Program BMS: zone valve/branch OFF when occupancy signal <10% for 30 min
2. pre-condition 30 min before occupancy. 4) Commission to verify no temperature complaints from adjacent unoccupied zones. 5) Exempt critical zones (server rooms, reception).

## Risks / Constraints
- AHU-served open-plan floors are hard to zone without physical modifications. Works best in FCU or VRF systems.

## KPIs
- Zone temperature deviation (°F)
- HVAC runtime in unoccupied zones (hrs/day)
- Energy per occupied zone (kBtu/sq ft/yr)

## M&V Plan (IPMVP Option C with submetering where feasible)
- Pre-installation baseline: 90-day continuous monitoring
- Post-installation: compare same period following year (weather-normalised)
- IPMVP Option C: Whole-building metering with regression analysis

## Costs & Payback (indicative)
- Payback: 4–12 months
- Cost: Requires building-specific survey and contractor pricing
