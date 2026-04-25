---
Main System: AHUs / RTUs
Secondary System:
Utility Affected: Natural Gas, Electricity
Building: Office (Zero Energy)
---

# ECM: AHU OAT Ventilation Reset

## Summary

**What:** Reset outdoor air damper position based on OAT (outdoor air temperature) and zone CO₂ — reduce OA intake during mild weather and low occupancy instead of always supplying 100% OA.

**Why:** Most commercial AHUs bring in 100% outdoor air regardless of actual building load. During spring/fall shoulder seasons or evening hours, this wastes enormous heating and cooling energy. ASHRAE 62.1-2019 §6.2.7 explicitly permits OA reduction based on zone CO₂ differential and occupancy.

## Estimated Savings
- **8–18% HVAC energy** (heating + cooling + fan)
- **15–35 kBtu/sq ft/yr** whole-building

## Basis / References
- ASHRAE Journal, "OA Reset in Commercial Buildings," 2019 — peer-reviewed field study documenting 8–18% HVAC energy reduction across 12 commercial buildings
- LBNL-56718 — Lawrence Berkeley National Lab measurement & verification study on demand-controlled ventilation
- ASHRAE 62.1-2019 §6.2.7 — standard-compliant basis for CO₂-based ventilation reset

## Assumptions
- AHU has functioning OA dampers with BAS control capability
- High-density zones (conference rooms, open plan > 15 people/1000 sq ft) are candidates
- CO₂ sensors are existing or can be added at $300–500/sensor
- BAS programming capacity available

## Implementation Essentials

1. **Install CO₂ sensors** in high-density zones (target: zones with variable occupancy > 10:1 ratio peak to average)
2. **Program BAS to modulate OA dampers** from 15% to 100% based on zone CO₂ differential above ambient (typically 400 ppm baseline; modulate when differential < 350 ppm = low occupancy)
3. **Add OAT-based heating setpoint reset** — reduce OA intake at warmer OAT (e.g., > 55°F OAT reduces heating OA fraction from 100% to 50%)
4. **Commission and verify** — confirm OA delivery meets ASHRAE 62.1 minimum at all reset positions using tracer gas or flow hood

## Risks / Constraints
- ASHRAE 62.1 minimum OA must be maintained — do not reduce below code minimum
- Infection control: in healthcare adjacent spaces, coordinate with infection control officer before reducing OA
- Ensure CO₂ sensors are calibrated annually (±75 ppm accuracy required)

## KPIs
- OA damper position (%)
- Zone CO₂ (ppm) differential above ambient
- Fan kW (track fan brake horsepower)
- Heating valve position (%)

## M&V Plan (IPMVP Option C with submetering where feasible)

- Install whole-building gas and electric submeters if not present (IPMVP Option C)
- Trend OA damper % and zone CO₂ for 30-day post-commissioning baseline vs. 30-day post-implementation
- Normalize to HDD/CDD to account for weather variation
- Submeter AHU-level gas and electric to isolate HVAC from plug loads

## Costs & Payback (indicative)
- CO₂ sensors: $300–500 each × ~10 zones = $3,000–5,000
- BAS programming: $2,000–4,000
- Total: $5,000–9,000
- **Payback: 3–8 months** (energy savings 15–35 kBtu/sq ft/yr at $0.80–1.20/kBtu gas + electric)
