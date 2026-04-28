---
Main System: Building Envelope / Window Controls
Secondary System:
Utility Affected: Natural Gas, Electricity
Building: Office — European Portfolio
---

# ECM: Automated Solar Shading (Smart Inputs: Weather + Occupancy + Lux)

## Summary

**What:** Motorised external or internal blinds/solar shades on south/west facades, controlled by a combination of lux levels, weather forecast API, and occupancy status. Reduces solar gain and cooling load in summer.

**Why:** At One Coleman Street (new install), Akzo Nobel HQ (optimise existing), UN Studio Tower, and 5 Keizers, solar shading exists but is manually operated or lux-only controlled. Adding weather forecast and occupancy logic improves performance.

## Estimated Savings
- 5–15% cooling energy in south/west facades
- Building-specific

## Basis / References
- Portfolio basis: One Coleman Street, Akzo Nobel HQ, UN Studio Tower, 5 Keizers

## Assumptions
- Building-specific survey required before implementation
- Energy audit recommended to quantify baseline and savings

## Implementation Essentials
1. 1) Audit existing shading system — motorised or manual, control capability. 2) If manual: replace with motorised actuators. 3) Install weather forecast API integration (BAS). 4) Configure control logic: shade deploys when solar intensity >X W/m² AND occupied AND cooling call. 5) Commission seasonal performance vs manual operation.

## Risks / Constraints
- In UK/NL climate, cooling loads are seasonal and moderate. Marginal gain from weather-forecast logic may not justify additional integration cost vs lux-only control.

## KPIs
- Solar shade position (% deployed)
- Cooling energy (kBtu/sq ft/yr)
- Occupant comfort complaints (glare)

## M&V Plan (IPMVP Option C with submetering where feasible)
- Pre-installation baseline: 90-day continuous monitoring
- Post-installation: compare same period following year (weather-normalised)
- IPMVP Option C: Whole-building metering with regression analysis

## Costs & Payback (indicative)
- Payback: 5–12 years
- Cost: Requires building-specific survey and contractor pricing
