---
Main System: VAV Air Distribution
Secondary System:
Utility Affected: Electricity
Building: Office (Zero Energy)
---

# ECM: VAV Box Pressure-Independent Reset

## Summary

Verify and reset VAV box minimum position settings — reduce minimum CFM in lightly-loaded zones to actual minimum rather than design minimum (often set 30–50% higher than needed). VAV boxes are often left at manufacturer defaults or oversize for actual loads. Minimum position represents a significant constant fan load. Reducing it by even 10–15 CFM per box across a building compounds to large fan kWh savings.

## Estimated Savings
- 5–12% fan energy
- 0.3–0.8 W/sq ft fan power reduction

## Basis / References
- ASHRAE Journal 'VAV Box Optimization' 2018
- SMACNA HVAC Systems Application Guide

## Assumptions
- VAV boxes are pressure-independent type (PICV valves)
- Air balance report available or can be commissioned
- Zone temperature control maintained within ±1°F

## Implementation Essentials

1. Air balance contractor surveys actual minimum CFM at representative VAV boxes across building — sample 15–20% of boxes.
2. Adjust PICV or spring range to reduce minimum stop to actual observed minimum vs. design minimum.
3. Verify zone temperature control still maintained post-adjustment over 2-week observation period.
4. Update BAS setpoints and trending to monitor box positions post-change.
5. Re-balance affected VAV boxes if zone temperatures deviate.

## Risks / Constraints

- Code-required minimum ventilation rates must be maintained
- Excessive reduction can cause zone temperature swings and discomfort complaints
- Not applicable to constant-volume systems

## KPIs
- VAV box min position (%)
- Fan kW
- Zone temperature deviation

## M&V Plan (IPMVP Option C with submetering where feasible)
- Install or verify VFD power monitoring on AHU fans (submetering)
- Baseline: 30-day pre-implementation fan kW trend
- Post-implementation: 90-day fan kW trend at matched conditions (same weather, occupancy)
- IPMVP Option C: whole-building electricity use normalized for weather/occupancy

## Costs & Payback (indicative)
- Air balance survey: $2,000–$5,000 for typical 50,000 sq ft office
- BAS programming/adjustment: 4–8 hours
- Total: $3,000–$8,000
- Payback: 4–12 months

## Templates / Reuse
- Standard ECM template
