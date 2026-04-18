---
Main System: AHUs / RTUs
Secondary System:
Utility Affected: Natural Gas, Electricity
Building: K-12 (50%)
---

# ECM: BAS Schedule Optimization — Classroom AHUs

## Summary

**What:** Audit and reprogram BAS schedules for classroom and office AHUs — many K-12 schools run HVAC 7 AM–9 PM regardless of actual occupancy. Align HVAC schedules with actual building use calendar (school hours vs. after-school hours vs. weekends).

**Why:** K-12 schools are typically occupied 8 AM–3 PM weekdays. After-school activities may use 10–20% of the building, and weekends near 0%. Without schedule optimization, HVAC runs 60–70 hours/week of unnecessary conditioning.

## Estimated Savings
- 15–30% HVAC energy during unoccupied hours
- Absolute: 4–10 kBtu/sq ft/yr

## Basis / References
- NREL Technical Report TP-5500-56451 K-12 Schools
- EnergyStar Portfolio Manager K-12


## Assumptions
- Implementation assumes existing functional BAS with trend logging capability
- Sensor accuracy ±50 ppm CO₂; recalibrate annually
- OA reset applies to AHUs with modulating OA dampers (not single-speed exhaust fans)

## Implementation Essentials
1) Export current BAS schedule. 2) Cross-reference with school calendar (principal/scheduler). 3) Program: weekday unoccupied (after 4 PM) setback, weekend shutdown, holiday override. 4) Commission — verify no spaces go outside temp limits during setback.

## Risks / Constraints
- ASHRAE 62.1 minimum OA requirements must be maintained — do not reduce below code minimum
- CO₂ sensor placement: install at breathing height (48–60 in AFF) in representative high-density zones
- Commission OA reset sequence before occupancy hours to avoid IAQ complaints
- BAS programming should include manual override / smoke purge mode

## KPIs
- HVAC runtime hours by AHU, Natural Gas (therms/HDD), AHU supply fan kW

## M&V Plan (IPMVP Option C with submetering where feasible)
- Install or verify existing whole-building electricity and natural gas meters as primary measurement boundary
- Submeter AHU fan power via existing VFD panel or add CTs; trend at 15-min intervals
- Collect 12-month baseline: HVAC kBtu/sq ft/yr normalized by HDD/CDD
- Post-installation: monthly comparison; IPMVP Option C whole-building metering with regression model

## Costs & Payback (indicative)
- Payback: 3–9 months
- CO₂ sensor installed (typical): $150–$300/sensor; 4–8 sensors per AHU
- BAS programming labor: 4–8 hours per AHU; $500–$1,200 per AHU
- Total estimated cost range: $1,500–$4,500 per AHU

## Templates / Reuse
- Standard ECM template: ECM full note milo.md
- Applicable to: commercial office, school, retail with packaged or built-up AHUs
- Sequence of operation template: BAS sequencing — OA reset MMIT v2
