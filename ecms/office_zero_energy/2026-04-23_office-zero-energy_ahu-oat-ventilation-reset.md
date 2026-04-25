---
Main System: AHUs / RTUs
Secondary System:
Utility Affected: Natural Gas, Electricity
Building: Office (Zero Energy)
---

# ECM: AHU OAT Ventilation Reset

## Summary

Reset outdoor air damper position based on OAT and zone CO₂ — reduce OA during mild weather and low occupancy instead of always supplying 100% OA. Most commercial AHUs bring in 100% OA regardless of building load. During spring/fall or evenings, this wastes enormous heating and cooling energy. ASHRAE 62.1 allows OA reduction based on occupancy/CO₂.

## Estimated Savings
- 8–18% HVAC energy
- 15–35 kBtu/sq ft/yr

## Basis / References
- ASHRAE Journal 'OA Reset in Commercial Buildings' 2019
- LBNL-56718
- ASHRAE 62.1-2019 §6.2.7

## Assumptions
- CO₂ sensors available or installable in high-density zones
- BAS programmable for custom OA reset schedules
- Building has mechanical cooling (not all-electric with ERV)

## Implementation Essentials
1. Install CO₂ sensors in high-density zones (conference rooms, open plan > 10 people/1000 sq ft)
2. Program BAS to modulate OA dampers 15–100% based on zone CO₂ differential (target < 800 ppm CO₂ = reduced OA)
3. Add OAT-based heating setpoint reset: lower OA intake when OAT > 55°F, reduce heating coil load
4. Commission: verify ventilation rates still meet ASHRAE 62.1 minimum at reduced OA
5. Log OA damper % and zone CO₂ for 30 days post-commissioning

## Risks / Constraints
- ASHRAE 62.1 minimum ventilation must be maintained — do not reduce below code minimum
- Infection control risk in healthcare-adjacent spaces: maintain dilution ventilation during outbreak conditions
- CO₂ sensor drift requires annual calibration

## KPIs
- OA damper position (%)
- Zone CO₂ (ppm)
- Fan kW
- Heating valve position (%)

## M&V Plan (IPMVP Option C with submetering where feasible)
- Submeter: AHU supply fan kW, heating valve gpm
- Whole-building: natural gas and electricity from utility billing
- Baseline period: 30 days pre-implementation; reporting period: 90 days post
- Adjust for weather using Heating/Cooling Degree Days (HDD/CDD)

## Costs & Payback (indicative)
- CO₂ sensors: $150–400 each, ~10–20 per typical office floor
- BAS programming: $2,000–6,000 (contractor)
- Total: $4,000–12,000; Payback: 3–8 months

## Templates / Reuse
- Standard ECM template
