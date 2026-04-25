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
- **5–12% fan energy** HVAC energy
- 0.3–0.8 W/sq ft fan power reduction

## Basis / References
- ASHRAE Journal 'VAV Box Optimization' 2018
- SMACNA HVAC Systems Application Guide

## Assumptions
- CO₂ sensors are not already present in high-density zones (installation required)
- BAS has available points for OA damper modulation
- Building is not under infectious disease protocol requiring 100% OA at all times
- Occupancy schedule allows OA reduction during unoccupied hours

## Implementation Essentials
1. Air balance contractor surveys actual minimum CFM at representative VAV boxes. 2) Adjust PICV or spring range to reduce minimum stop. 3) Verify zone temperature control still maintained post-adjustment. 4) Update BAS setpoints.

## Risks / Constraints
- **Code compliance:** ASHRAE 62.1 minimum OA rates must be maintained at all times — program must never reduce OA below code minimum
- **Infection control:** In buildings with immune-compromised occupants, freeze OA reduction to minimum setpoint
- **Zone conflicts:** Verify temperature satisfaction in perimeter zones that may have higher internal gains
- **BAS programming:** Requires qualified BAS technician — coordinate with building controls vendor

## KPIs
- VAV box min position (%), Fan kW, Zone temperature deviation

## M&V Plan (IPMVP Option C with submetering where feasible)
1. Install whole-building electricity and natural gas metering (if not present)
2. Install AHU-level fan kW submetering to isolate fan energy changes
3. Install OA damper position feedback (analog signal, % open) on each AHU
4. Baseline period: 30 days pre-implementation, capture OA damper %, zone CO₂, fan kW, heating valve %
5. Post-implementation: same 30-day window, compare OA damper % and fan kW
6. Normalize for weather using Heating/Cooling Degree Days (HDD/CDD)

## Costs & Payback (indicative)
- **CO₂ sensors:** $150–$300 each; typical office needs 4–8 units
- **BAS programming:** $2,000–$5,000 (vendor-dependent)
- **Total estimated cost:** $3,000–$8,000
- **Payback:** 4–12 months

## Templates / Reuse
- Standard ECM template (Office / K-12)
