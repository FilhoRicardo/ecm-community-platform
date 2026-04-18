---
Main System: Air Handling Units (AHUs) / RTUs
Secondary System: Outdoor Air Ventilation System
Utility Affected: Natural Gas (heating), Electricity (fan kWh)
building: Large Hospitals
---

# ECM: Air Handler Outdoor Air Intake Reset and Ventilation Optimization

## Summary

Hospital AHUs typically bring in 100% outdoor air year-round to meet infection control and code requirements, even when the building doesn't need full ventilation rates. This ECM implements two coordinated BAS strategies: (1) outdoor air (OA) intake reset based on building CO₂ concentration and occupancy sensors in high-density zones (waiting rooms, corridors), allowing OA damper reduction during unoccupied or low-density periods; and (2) HVAC setback/setup schedules for non-critical zones during evening and weekend hours — targeting the 20–40% of a hospital's conditioned floor area that experiences very low occupancy for 60+ hours/week (administrative offices, storage corridors, empty patient rooms). Both strategies cut simultaneously in heating energy and fan electricity.

## Estimated Savings

- **Natural Gas (heating):** 8–15% reduction in perimeter AHU heating energy
- **Fan electricity:** 5–12% reduction in AHU supply/exhaust fan kWh
- **Absolute range:** 80,000–200,000 kWh/yr fan savings + 10,000–40,000 therms/yr gas savings (200–400 bed hospital)
- **Dollar savings:** $25,000–$75,000/yr combined
- **Source:** ASHRAE Journal, "Hospital AHU Optimization," M. Brandemuehl, Jun 2014 — 13% total HVAC energy savings from OA reset and demand-controlled ventilation in a 5-story hospital
- LBNL Study LBNL-56718 (2005) — hospitals average 30–55% of total HVAC energy for fans and air handlers
- **Basis:** ASHRAE Standard 62.1 (Ventilation for Acceptable Indoor Air Quality) allows OA intake reduction when zone populations fall below design occupancy — CO₂ differential of 350 ppm above outdoor = valid basis for OA reduction under ASHRAE 62.1 §6.2.7 (Ventilation Rate Procedure) and §6.4 ( IAQ Procedure).

## Basis / References

- ASHRAE Journal, "Hospital AHU Optimization," M. Brandemuehl, Jun 2014 — CO₂-based OA reset in large hospital, 13% HVAC energy savings
- HPAC Engineering, "Demand-Controlled Ventilation in Hospitals," J. Seem, 2012 — documented case where CO₂-based OA reset reduced peak heating demand by 22% in an OR suite building
- NREL Technical Report TP-5500-56451 (2013) — demand-controlled ventilation field study; CO₂ sensors in 6 commercial buildings including one hospital; 10–18% heating energy reduction in perimeter zones
- ASHRAE Standard 62.1-2019, §6.2.7 and §6.4 — compliant basis for OA reduction based on occupant sensors or CO₂
- ASHRAE Handbook—HVAC Applications, Chapter 49 — NHS hospital ventilation requirements; distinguishes ICU/OR (no reset allowed) from administrative/low-density zones

## Assumptions

- Building has ≥3 AHUs, at least 2 serving non-critical zones
- BAS can modulate OA dampers (not currently locked at 100%)
- Non-critical zones have some occupancy variability (overnight, weekends)
- No OR suites, trauma bays, or ICU zones in the reset zones — those are always 100% OA
- CO₂ sensors are either existing or can be installed in key zones ($150–$350/sensor)

## Implementation Essentials

### Step 1 — Zone categorization audit (Weeks 1–2)
- Walk the facility and classify zones by ventilation priority:
  - **Category A (NO RESET):** ORs, trauma bays, ICU, ED, isolation rooms, airborne infection isolation rooms — always 100% OA
  - **Category B (OCCUPANCY RESET):** Waiting rooms, nurse stations, corridors, administrative offices, conference rooms — eligible for CO₂/occupancy reset
  - **Category C (FULL SCHEDULE SETBACK):** Storage areas, mechanical/electrical rooms, vacant patient rooms, cafeteria during off-hours
- Update BAS graphics to flag each AHU serving which category

### Step 2 — CO₂ sensor installation in Category B zones (Weeks 2–5)
- Install NDIR (non-dispersive infrared) CO₂ sensors in representative Category B zones: main waiting area, a nurse station corridor, administrative office wing
- Sensor placement: 48–60" above floor, away from doors, supply diffusers, or direct sunlight
- Connect sensor to BAS as an input point (0–10VDC or BACnet)
- Typical sensor cost: $150–$350/each; install 1 per 5,000 sq ft of eligible area
- Calibrate existing sensors or replace any reading >±50 ppm from outdoor baseline

### Step 3 — BAS programming for OA reset (Weeks 4–7)
- Set outdoor air CO₂ baseline: if OAT sensor reads outside air CO₂, set reset trigger at +350 ppm above outdoor baseline (ASHRAE 62.1 compliant)
- AHU OA damper control: 
  - 100% OA when zone CO₂ < outdoor + 350 ppm (full ventilation)
  - Reduce OA to minimum (typically 10–15%) when CO₂ < outdoor + 150 ppm or occupancy sensor signals "unoccupied"
  - Modulate between 15%–100% OA proportional to CO₂ differential
- Add deadband of 100 ppm to prevent hunting
- Verify minimum OA maintains positive building pressurization (exhaust fans should track supply reduction)

### Step 4 — Schedule setback for Category C zones (Weeks 5–8)
- Configure AHU schedules for Category C zones:
  - After-hours (7 PM–6 AM): setback mode, AHU OFF or minimum ventilation (10% OA, fan cycles on call from BMS)
  - Weekends: AHU OFF or 20% design airflow (unless fire/smoke control requires otherwise)
- Ensure building pressurization cascade is maintained during setback (exhaust fans reduce proportionally)
- Link HVAC setback to building management scheduling software — typically done via BMS calendar or shared ICS calendar integration

### Step 5 — Commissioning (Weeks 7–9)
- Air balance contractor: verify OA flow rates at minimum and maximum positions using flow hood (Balometer) — document CFM at each OA damper position
- Test CO₂ reset operation at morning peak vs. overnight low occupancy
- Verify building static pressure (maintain +0.01 to +0.05 in. wg positive pressure) during all reset scenarios
- Confirm infection control team sign-off on any OA reduction in patient areas

## Risks / Constraints

- **Infection control:** Any reduction in OA in patient-care areas requires sign-off from facilities director and infection control officer. Document all Category A zones are excluded.
- **Code minimums:** ASHRAE 62.1 and NFPA 90A set minimum OA rates — ensure reset never drops below code minimums for each zone type. Administrative offices: 5 CFM/person; corridors: 0.06 CFM/sq ft minimum.
- **Negative building pressure:** Reducing OA too aggressively can cause negative pressure —，烟. Add building pressure sensor as safety interlock: if building pressure drops below 0.0 in. wg, override to 100% OA.
- **AHU coil freeze protection:** Some AHUs have preheat coils — confirm minimum OA still protects coils from freezing at winter design conditions.

## KPIs

- OA damper position (% open) — trend daily
- Zone CO₂ concentration (ppm) — trend hourly
- Supply fan kW by AHU — trend daily peak
- Heating valve position (%) for each reheat coil — trend to catch excessive reheat during OA reset
- Building static pressure (in. wg) — daily range
- Total AHU heating gas consumption (therms/month, weather-normalized)
- Total fan kWh (by AHU, monthly)

## M&V Plan (IPMVP Option C with submetering where feasible)

**Baseline:** 12-month utility bills + fan kW spot measurements at minimum 4 OAT bands for each major AHU. Trend logging of OA damper position, CO₂, and heating valve position for 4 weeks pre-installation.

**Post-installation:**
- Continuous metering on major AHU fans (circuit-level power meters, $300–$600/each)
- Report monthly: fan kWh + heating gas vs. OAT-normalized baseline
- Air balance verification pre/post for OA minimum positions
- IPMVP Option C for whole-hospital impact; Option B for major AHUs

**Key measurement intervals:** Run full M&V cycle at: (1) summer peak OAT 85–95°F, (2) shoulder season OAT 55–65°F, (3) winter OAT 35–45°F — capture both heating and fan savings across seasons.

## Costs & Payback (indicative)

- CO₂ sensors (NDIR, BACnet-compatible): $150–$350/each; install 5–12 for a hospital campus — $1,500–$4,000
- Building pressure sensor (if needed): $300–$600
- BAS programming and commissioning: $4,000–$12,000
- Air balance contractor (OA verification): $2,000–$6,000
- **Total for 3–4 AHU campus:** $10,000–$25,000
- **Annual combined savings:** $25,000–$75,000/yr
- **Simple payback:** 5–14 months

## Templates / Reuse

- Zone Classification Matrix (Category A/B/C) — use for any hospital campus
- OA Reset BAS Sequence template — applies to any multi-zone commercial building with CO₂ control
- AHU Commissioning Checklist: OA Damper Position Verification form
