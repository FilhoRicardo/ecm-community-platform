---
Main System: AHUs / RTUs
Secondary System:
Utility Affected: Natural Gas, Electricity
Building: Office (Zero Energy)
---

# ECM: AHU OAT Ventilation Reset

## Summary

**What:** Reset outdoor air damper position based on OAT and zone CO₂ — reduce OA during mild weather and low occupancy instead of always supplying 100% OA.

**Why:** Most commercial AHUs bring in 100% OA regardless of building load. During spring/fall or evenings, this wastes enormous heating and cooling energy. ASHRAE 62.1 allows OA reduction based on occupancy/CO₂.

## Estimated Savings
- 8–18% HVAC energy
- Absolute: 15–35 kBtu/sq ft/yr

## Basis / References
- ASHRAE Journal 'OA Reset in Commercial Buildings' 2019
- LBNL-56718
  - ASHRAE 62.1-2019 §6.2.7

## Assumptions
- Implementation assumes existing functional BAS with trend logging capability
- Sensor accuracy ±50 ppm CO₂; recalibrate annually
- OA reset applies to AHUs with modulating OA dampers (not single-speed exhaust fans)

## Implementation Essentials
1) Install CO₂ sensors in high-density zones. 2) Program BAS to modulate OA dampers 15–100% based on zone CO₂ differential. 3) Add OAT-based heating setpoint reset (lower OA intake at warmer OAT).

## Risks / Constraints
- ASHRAE 62.1 minimum OA requirements must be maintained — do not reduce below code minimum
- CO₂ sensor placement: install at breathing height (48–60 in AFF) in representative high-density zones
- Commission OA reset sequence before occupancy hours to avoid IAQ complaints
- BAS programming should include manual override / smoke purge mode

## KPIs
- OA damper position (%), Zone CO₂ (ppm), Fan kW, Heating valve position (%)

## M&V Plan (IPMVP Option C with submetering where feasible)
- Install or verify existing whole-building electricity and natural gas meters as primary measurement boundary
- Submeter AHU fan power via existing VFD panel or add CTs; trend at 15-min intervals
- Collect 12-month baseline: HVAC kBtu/sq ft/yr normalized by HDD/CDD
- Post-installation: monthly comparison; IPMVP Option C whole-building metering with regression model

## Costs & Payback (indicative)
- Payback: 3–8 months
- CO₂ sensor installed (typical): $150–$300/sensor; 4–8 sensors per AHU
- BAS programming labor: 4–8 hours per AHU; $500–$1,200 per AHU
- Total estimated cost range: $1,500–$4,500 per AHU

## Templates / Reuse
- Standard ECM template: ECM full note milo.md
- Applicable to: commercial office, school, retail with packaged or built-up AHUs
- Sequence of operation template: BAS sequencing — OA reset MMIT v2
