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
- **8–18% HVAC energy** HVAC energy
- 15–35 kBtu/sq ft/yr

## Basis / References
- ASHRAE Journal 'OA Reset in Commercial Buildings' 2019
- LBNL-56718
- ASHRAE 62.1-2019 §6.2.7

## Assumptions
- CO₂ sensors are not already present in high-density zones (installation required)
- BAS has available points for OA damper modulation
- Building is not under infectious disease protocol requiring 100% OA at all times
- Occupancy schedule allows OA reduction during unoccupied hours

## Implementation Essentials
1. Install CO₂ sensors in high-density zones. 2) Program BAS to modulate OA dampers 15–100% based on zone CO₂ differential. 3) Add OAT-based heating setpoint reset (lower OA intake at warmer OAT).

## Risks / Constraints
- **Code compliance:** ASHRAE 62.1 minimum OA rates must be maintained at all times — program must never reduce OA below code minimum
- **Infection control:** In buildings with immune-compromised occupants, freeze OA reduction to minimum setpoint
- **Zone conflicts:** Verify temperature satisfaction in perimeter zones that may have higher internal gains
- **BAS programming:** Requires qualified BAS technician — coordinate with building controls vendor

## KPIs
- OA damper position (%), Zone CO₂ (ppm), Fan kW, Heating valve position (%)

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
- **Payback:** 3–8 months

## Templates / Reuse
- Standard ECM template (Office / K-12)
