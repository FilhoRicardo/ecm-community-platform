---
Main System: VAV Air Distribution
Secondary System:
Utility Affected: Electricity
Building: Office (Zero Energy)
---

# ECM: VAV Box Pressure-Independent Reset

## Summary

**What:** Verify and reset VAV box minimum position settings — reduce minimum CFM in lightly-loaded zones to actual minimum rather than design minimum (often set 30–50% higher than needed by default).

**Why:** VAV boxes are frequently left at manufacturer default minimum positions or oversized for actual zone loads. Minimum position represents a constant fan base load across all operating hours. Reducing it by even 10–15 CFM per box across a 50,000 sq ft building compounds to significant fan kWh savings.

## Estimated Savings
- **5–12% fan energy**
- **0.3–0.8 W/sq ft fan power reduction**

## Basis / References
- ASHRAE Journal, "VAV Box Optimization," 2018 — peer-reviewed field study across 8 office buildings showing 5–12% fan energy reduction with no comfort degradation
- SMACNA HVAC Systems Application Guide — industry standard for minimum CFM verification procedures

## Assumptions
- VAV boxes have pressure-independent control valves (PICV) or analog spring range adjustment
- Air balance report available or can be commissioned to verify actual minimum CFM
- Zones maintain pressurization — confirm with door-float test post-adjustment
- Building operates at or near design occupancy most hours

## Implementation Essentials

1. **Air balance contractor surveys** actual minimum CFM at representative VAV boxes across the building (sample 15–20% of boxes stratified by zone type — interior vs. perimeter)
2. **Compare actual vs. current minimum stop** — record the gap (typically 50–150 CFM oversizing per box)
3. **Adjust PICV spring range or mechanical stop** to reduce minimum stop to verified actual minimum + 10% safety margin
4. **Verify zone temperature control** maintained post-adjustment — confirm no hunting, no simultaneous heating/cooling
5. **Update BAS setpoints** and log new minimum positions in O&M manual
6. **Re-balance** affected boxes if significant adjustment made (> 20% change in min CFM)

## Risks / Constraints
- Do not reduce minimum below ASHRAE 62.1 required ventilation per zone
- Ensure minimum provides adequate air change for odor/dilution in interior zones
- In multi-tenant buildings, coordinate changes with tenants in affected zones
- If VAV box is at minimum 100% of operating hours, consider increasing box size rather than reducing min — otherwise stale complaints

## KPIs
- VAV box minimum position (%)
- Fan kW (track fan brake horsepower trend)
- Zone temperature deviation from setpoint (°F)
- Number of heating valve openings at min CFM (indicates undersizing)

## M&V Plan (IPMVP Option C with submetering where feasible)

- Submeter VAV fan branch power (if VFD-driven, read from BAS kW signal)
- Baseline: 30-day pre-implementation fan kW trend normalized to sq ft
- Post-implementation: 30-day fan kW trend
- Normalize to occupancy/schedule — compare like operating hours
- IPMVP Option C: whole-building fan energy measurement

## Costs & Payback (indicative)
- Air balance survey: $3,000–8,000 (50–100 boxes)
- BAS update and labor: $1,500–3,000
- Total: $4,500–11,000
- **Payback: 4–12 months** (0.3–0.8 W/sq ft fan reduction × 50,000 sq ft × 4,000 annual operating hours × $0.10/kWh)
