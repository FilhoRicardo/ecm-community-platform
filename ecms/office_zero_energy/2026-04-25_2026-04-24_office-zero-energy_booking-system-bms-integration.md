---
Main System: BMS / HVAC Controls / Smart Controls
Secondary System:
Utility Affected: Natural Gas, Electricity
Building: Office — European Portfolio
---

# ECM: Link Booking / Reservation System to BMS

## Summary

**What:** API/Zapier/middleware integration between room booking system (hotel PMS or workplace app) and BMS to trigger HVAC only for occupied/pre-booked spaces. Hotel room HVAC running on fixed schedule regardless of occupancy wastes 15–20%. In offices, unoccupied meeting rooms with active conditioning are endemic.

**Why:** At Radisson Blu Stansted (Emma.ai → BMS via Zapier) and at One Coleman Street and Akzo Nobel HQ, HVAC runs for rooms with no occupants. Integration links actual occupancy (from booking) to HVAC activation.

## Estimated Savings
- 15–25% HVAC energy in hotel rooms; 10–20% in meeting rooms
- Building-specific

## Basis / References
- Portfolio basis: Radisson Blu Stansted, One Coleman Street, Akzo Nobel HQ

## Assumptions
- Building-specific survey required before implementation
- Energy audit recommended to quantify baseline and savings

## Implementation Essentials
1. 1) Audit booking/PMS system API availability. 2) Select middleware (Zapier, custom API, or BMS-native integration). 3) Map room zones to BMS points. 4) Configure BMS: room setpoint activates on booking check-in, setbacks on check-out. 5) Set 30-min pre-conditioning before booking start. 6) Monitor for integration failures — set alert for API disconnect.

## Risks / Constraints
- ⚠️ Integration fragility — third-party booking platforms change APIs. Needs monitoring. Not 'set and forget.'

## KPIs
- Room HVAC runtime hours (occupied vs unoccupied)
- Hotel guest temperature complaints
- API uptime (%)

## M&V Plan (IPMVP Option C with submetering where feasible)
- Pre-installation baseline: 90-day continuous monitoring
- Post-installation: compare same period following year (weather-normalised)
- IPMVP Option C: Whole-building metering with regression analysis

## Costs & Payback (indicative)
- Payback: 4–12 months
- Cost: Requires building-specific survey and contractor pricing
