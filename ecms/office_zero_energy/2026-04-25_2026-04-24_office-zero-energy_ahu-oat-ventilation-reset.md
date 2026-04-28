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
- Building has existing CO₂ sensing capability or can be retrofitted
- BAS has available points for OA damper modulation
- AHU minimum OA intake can be reduced without code compliance issues

## Implementation Essentials

1. Install CO₂ sensors in high-density zones (conference rooms, open plan areas above 500 ppm threshold).
2. Program BAS to modulate OA dampers 15–100% based on zone CO₂ differential — lower CO₂ = lower OA requirement.
3. Add OAT-based heating setpoint reset: lower OA intake at warmer OAT to reduce preheat energy.
4. Commission and verify ASHRAE 62.1 compliance throughout operating range.

## Risks / Constraints

- Must maintain minimum OA per ASHRAE 62.1 — do not reduce below code minimum
- CO₂ sensor accuracy drift requires periodic calibration
- Infection control (healthcare occupancies) may restrict OA reduction

## KPIs
- OA damper position (%)
- Zone CO₂ (ppm)
- Fan kW
- Heating valve position (%)

## M&V Plan (IPMVP Option C with submetering where feasible)
- Install whole-building electricity and natural gas metering (IPMVP Option C)
- Install AHU-level sub-metering on fan motors and heating coil
- Trend OA damper % and zone CO₂ alongside whole-building EUI
- Baseline period: 30 days pre-ECM; measurement period: 90 days post-ECM

## Costs & Payback (indicative)
- CO₂ sensors: $150–$300 each; 8–16 sensors typical for medium office
- BAS programming: 4–8 hours engineering time
- Total implementation: $3,000–$8,000 for typical 50,000 sq ft office
- Payback: 3–8 months

## Templates / Reuse
- Standard ECM template
