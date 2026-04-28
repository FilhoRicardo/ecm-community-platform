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
- Air balance report available or can be commissioned
- VAV boxes have adjustable minimum stops (PICV or spring range)
- BAS can read and write VAV box position

## Implementation Essentials
1. Air balance contractor surveys actual minimum CFM at representative VAV boxes (sample 15–20% of boxes)
2. Identify boxes where actual minimum is significantly below design minimum
3. Adjust PICV or spring range to reduce minimum stop to actual minimum needed
4. Verify zone temperature control still maintained post-adjustment over 2-week observation
5. Update BAS setpoints and as-built drawings

## Risks / Constraints
- Minimum position must still maintain minimum ventilation per ASHRAE 62.1
- Addresses only constant fan power — variable speed drives not addressed here
- Over-reduction can cause zone temperature hunting

## KPIs
- VAV box min position (%)
- Fan kW
- Zone temperature deviation

## M&V Plan (IPMVP Option C with submetering where feasible)
- Submeter: VAV box airflow (if equipped with velometers) and fan kW
- Whole-building: fan electricity from BAS trend logs
- Baseline: 30-day pre; Post: 90-day trend after adjustment
- Normalize to occupancy/HDD for weather adjustment

## Costs & Payback (indicative)
- Air balance survey: $3,000–8,000 (contractor, ~20 boxes sampled)
- BAS programming: $1,000–3,000
- Total: $4,000–11,000; Payback: 4–12 months

## Templates / Reuse
- Standard ECM template
