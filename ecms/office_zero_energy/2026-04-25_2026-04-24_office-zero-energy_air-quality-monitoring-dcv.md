---
Main System: AHUs / RTUs / DCV
Secondary System:
Utility Affected: Natural Gas, Electricity
Building: Office — European Portfolio
---

# ECM: Air Quality Monitoring → Demand-Controlled Ventilation

## Summary

**What:** Install CO₂ and particulate sensors in occupied zones; modulate AHU fresh air dampers based on zone CO₂ rather than running fixed 100% outdoor air post-COVID. The energy cost of conditioning 100% OA vs 20–30% OA is 2–4× higher.

**Why:** Multiple properties (XYZ, Radisson, SOM, ITO, etc.) are explicitly still in 100% fresh-air Covid mode. Moving back to DCV with CO₂ confirmation is the highest-impact HVAC ECM for affected properties.

## Estimated Savings
- 20–35% HVAC energy at properties in 100% OA Covid mode
- Building-specific

## Basis / References
- Portfolio basis: all 8 properties (Covid 100% OA mode)
- ASHRAE 62.1-2019 §6.2.7 DCV

## Assumptions
- Building-specific survey required before implementation
- Energy audit recommended to quantify baseline and savings

## Implementation Essentials
1. 1) Verify current ventilation mode — confirm 100% OA is not required by code (ASHRAE 62.1). 2) Install room-level CO₂ sensors (duct sensors less reliable than room-level per One Coleman experience). 3) Configure BAS: OA damper modulates 15–100% based on zone CO₂ differential and OAT. 4) Add occupancy schedule override — reduce OA when building is unoccupied. 5) Commission and communicate IAQ benefits to tenants.

## Risks / Constraints
- ⚠️ HIGHEST IMPACT for properties still in Covid ventilation mode. Urgent priority. Requires clear sign-off from building management.

## KPIs
- OA damper position (%)
- Zone CO₂ (ppm)
- Fan kW by AHU
- Heating/cooling energy (kBtu/sq ft/yr)

## M&V Plan (IPMVP Option C with submetering where feasible)
- Pre-installation baseline: 90-day continuous monitoring
- Post-installation: compare same period following year (weather-normalised)
- IPMVP Option C: Whole-building metering with regression analysis

## Costs & Payback (indicative)
- Payback: 3–12 months
- Cost: Requires building-specific survey and contractor pricing
