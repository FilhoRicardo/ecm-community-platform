---
Main System: Building Automation System
Secondary System:
Utility Affected: Electricity (grid)
Building: K-12 (Zero Energy)
---

# ECM: Advanced BAS Integration with On-Site Solar

## Summary

Program the BAS to shift flexible thermal loads — pre-cooling and thermal mass charging — to coincide with on-site solar generation periods. This maximizes self-consumption of PV electricity rather than exporting it to the grid at low value. Zero Energy K-12 buildings typically have abundant mid-day solar generation but low occupancy loads then; at night, loads rise with no solar available. Using the building's thermal mass as a "battery" smooths this mismatch and reduces grid dependence.

## Estimated Savings
- 10–20% grid electricity (peak shaving)
- Building-specific with PV system — measure baseline first

## Basis / References
- NREL Zero Energy Schools Study 2021
- DOE Zero Energy Schools Guide

## Assumptions
- Building has on-site PV system with capacity ≥ 50 kW
- BAS supports scheduling and setpoint override programming
- Building has thermal mass (concrete structure, chiller plant, or glycol loops) sufficient for 2–4 hour load shift
- Occupancy schedule allows 72°F–76°F drift band during afternoon peak

## Implementation Essentials
1. Install whole-building electricity metering (PV generation + building consumption) on BAS
2. Characterize building load profile: identify flexible loads (AHU fans, cooling, electric reheat) vs. inflexible base loads
3. Program pre-cooling strategy: starting ~10 AM, cool building to 72°F (below daytime setpoint), allowing temperature to drift to 76°F during peak solar afternoon (1–4 PM)
4. Use thermal mass as battery substitute — concrete slab, chilled water storage, or phase-change materials
5. Validate demand shifting with submetering: measure grid import reduction vs. baseline

## Risks / Constraints
- Occupant comfort must stay within ASHRAE 55 thermal comfort bands — confirm with occupancy sensors
- Control sequence must be fail-safe: if BAS loses communication, revert to standard setpoints
- Code compliance: verify pre-cooling setpoints do not violate any authority-having-jurisdiction (AHJ) requirements for minimum ventilation rates during occupied hours
- Commissioning required to ensure controls loop stability — avoid hunting between pre-cool and recovery

## KPIs
- Grid import/export profile (kW)
- Solar self-consumption rate (%)
- Peak demand (kW)

## M&V Plan (IPMVP Option C with submetering where feasible)
- IPMVP Option C: Whole-building electricity metering with regression baseline
- Submetering: dedicated PV generation meter + building consumption meter
- Measurement period: minimum 30 days pre- and post-implementation, same season
- Normalize for occupancy and weather (cooling degree days)

## Costs & Payback (indicative)
- Direct payback — improves solar self-consumption with minimal hardware
- Control programming cost: $5,000–$15,000 (BAS integrator)
- Additional metering: $2,000–$5,000 per circuit
- ROI highly favorable where time-of-use utility rates apply (peak export avoidance)

## Templates / Reuse
- Standard ECM template
