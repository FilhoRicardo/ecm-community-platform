---
Main System: VAV Air Distribution
Secondary System:
Utility Affected: Electricity
Building: Office (Zero Energy)
---

# ECM: VAV Box Pressure-Independent Reset

## Summary

**What:** Verify and reset VAV box minimum position settings — reduce minimum cfm in lightly-loaded zones to actual minimum rather than design minimum (often set 30–50% higher than needed).

**Why:** VAV boxes are often left at manufacturer defaults or oversize for actual loads. Minimum position represents a significant constant fan load. Reducing it by even 10–15 CFM per box across a building compounds to large fan kWh savings.

## Estimated Savings
- 5–12% fan energy
- Absolute: 0.3–0.8 W/sq ft fan power reduction

## Basis / References
- ASHRAE Journal 'VAV Box Optimization' 2018
- SMACNA HVAC Systems Application Guide


## Assumptions
- Implementation assumes existing functional BAS with trend logging capability
- Sensor accuracy ±50 ppm CO₂; recalibrate annually
- OA reset applies to AHUs with modulating OA dampers (not single-speed exhaust fans)

## Implementation Essentials
1) Air balance contractor surveys actual minimum CFM at representative VAV boxes. 2) Adjust PICV or spring range to reduce minimum stop. 3) Verify zone temperature control still maintained post-adjustment. 4) Update BAS setpoints.

## Risks / Constraints
- ASHRAE 62.1 minimum OA requirements must be maintained — do not reduce below code minimum
- CO₂ sensor placement: install at breathing height (48–60 in AFF) in representative high-density zones
- Commission OA reset sequence before occupancy hours to avoid IAQ complaints
- BAS programming should include manual override / smoke purge mode

## KPIs
- VAV box min position (%), Fan kW, Zone temperature deviation

## M&V Plan (IPMVP Option C with submetering where feasible)
- Install or verify existing whole-building electricity and natural gas meters as primary measurement boundary
- Submeter AHU fan power via existing VFD panel or add CTs; trend at 15-min intervals
- Collect 12-month baseline: HVAC kBtu/sq ft/yr normalized by HDD/CDD
- Post-installation: monthly comparison; IPMVP Option C whole-building metering with regression model

## Costs & Payback (indicative)
- Payback: 4–12 months
- CO₂ sensor installed (typical): $150–$300/sensor; 4–8 sensors per AHU
- BAS programming labor: 4–8 hours per AHU; $500–$1,200 per AHU
- Total estimated cost range: $1,500–$4,500 per AHU

## Templates / Reuse
- Standard ECM template: ECM full note milo.md
- Applicable to: commercial office, school, retail with packaged or built-up AHUs
- Sequence of operation template: BAS sequencing — OA reset MMIT v2
