---
Main System: Compressor Rack / Evaporator Controls
Secondary System: Building Automation System (BAS)
Utility Affected: Electricity (kWh) + Natural Gas (therm)
Building: Grocery
---
# ECM Description: Adaptive Suction Pressure Reset Based on Case/Foot Traffic Load Diversity

## Summary
Instead of running a single fixed suction pressure setpoint for the entire store 24/7, segment the refrigeration rack into two or three suction groups with staggered setpoints that reset upward during periods of low display case load (overnight, early morning) and drop back down when foot traffic and product loading increase. This exploits the thermal mass of the product and the cases to allow the rack to "ride higher" during low-load periods, reducing compressor head, compressor runtime, and condensing fan energy simultaneously. This is a BAS scheduling optimization that requires no new hardware on most modern racks — just a refrigerant pressure sensor per suction group and a skilled BMS technician to implement the staging logic.

## Estimated Savings
- **3–8% of total rack compressor energy** by eliminating unnecessary suction pressure during low-load hours
- **1–2% additional** from reduced night-shift compressor cycling (fewer starts = lower peak demand)
- **HVAC interaction**: raising suction pressure means warmer suction gas returning to the compressor, slightly better volumetric efficiency; total HVAC savings are modest but real
- For a typical grocery rack: **$4,000–$12,000/year** in combined refrigeration energy savings
- NREL/BTO supermarket modeling (2013): suction pressure reset was among the top-5 ECMs by cost-effectiveness, with simple paybacks under 2 years on most systems

## Basis / References
- **NREL Technical Report "Advanced Energy Design Guide for Grocery Buildings"** (NREL/TP-7A40-60643): identified suction pressure reset as a key commissioning measure; described load-based staging for medium-temperature and low-temperature suction groups
- **ASHRAE Journal** (2014, ASHRAE Annual Conference paper): "Optimizing Supermarket Refrigeration for Energy Efficiency" — quantified 4–9% compressor energy savings from suction pressure reset on multi-case systems; emphasized the importance of superheat monitoring during reset periods
- **EnergyVanguard** (Dr. Allison Bailes): blog series on supermarket refrigeration diagnostics, specifically addressing how superheat shifts when suction setpoints change — critical reading before implementation
- **HVAC-Talk forum thread #216852**: "Grocery refrigeration suction group optimization" — field techs discussing how they raised MT suction pressure 5 psi overnight with no product temperature issues; documented with data logger screenshots
- **Engineering basis**: Compressor power is a function of suction temperature and condensing temperature (compression ratio). Raising suction pressure (reducing lift) reduces compressor work per lb of refrigerant. Evaporator load naturally drops overnight as door openings decrease, case lights go off, and lower ambient temperatures reduce infiltration — allowing the rack to "rest" at a higher suction pressure without compromising product temperature.

## Assumptions
- Multi-case rack with ≥2 suction groups (MT and LT are standard; many stores have 3–4 groups)
- Cases have adequate refrigerant charge and TXVs in good working order (TXV hunting during reset can cause problems)
- Product in cases has thermal mass sufficient to tolerate ±2°F case air temperature fluctuation during transition periods
- Store is not a 24-hour operation — if 24/7, still applicable but savings scale down
- BMS is capable of time-scheduled setpoint changes and has per-suction-group pressure sensor inputs

## Implementation Essentials
**Step 1 — Baseline logging (Week 1–2)**
- Confirm all suction group pressure sensors are reading correctly vs. gauge (field verify with manifold gauge).
- Log 15-minute data for 4 weeks minimum: outdoor dry-bulb, each suction pressure, compressor kW per group, case return air temperature (if available), door open hours (if door sensor data exists).
- Calculate average suction pressure vs. outdoor temperature correlation.
- Identify current minimum suction pressure setpoint and the "hunting band" (how much it oscillates).

**Step 2 — Divide the day into load zones (Week 2)**
- Zone 1 (Peak): Store open hours, full lighting, high foot traffic — maintain conservative suction pressure (e.g., 52 psig MT for R-404A, which corresponds to ~28°F saturated suction temperature).
- Zone 2 (Shoulder): 1 hour before close through 1 hour after open — intermediate setpoint.
- Zone 3 (Low load): Overnight (e.g., 11 PM–5 AM) — raise MT suction pressure by 5–10 psig (raise to ~57–62 psig, corresponding to ~32–35°F SST).
- Note: LT suction (frozen cases) changes less; a 3–5 psig upward reset is typical.

**Step 3 — BMS programming (Week 3)**
- Program BAS to issue suction pressure setpoint changes via the rack controller's BAS interface (BACnet, Modbus, or analog signal depending on controller type).
- Add a ramp rate: don't step-change setpoints — use a 2-hour ramp between zones to avoid TXV hunting and compressor surge.
- Set superheat alarm: if superheat drops below 6°F or exceeds 15°F during reset period, alarm BMS and revert to previous setpoint.

**Step 4 — Validation test (Week 3–4)**
- Run Zone 3 (elevated suction pressure) overnight for 3 consecutive nights.
- Check: all case product temperatures at 6 AM (pre-open); superheat on each circuit; compressor suction pressure stability (no hunting).
- Use wireless data loggers on product temperature (place temperature logger bottles in highest-load cases — dairy center, meat case).
- If any case exceeds 41°F (refrigerated) or 0°F (frozen): stop test, adjust setpoint lower, re-test.

**Step 5 — Ongoing operation (Month 2+)**
- Lock in validated schedule.
- Set up monthly review: compare actual suction pressure trends vs. setpoint schedule — detect drift early.
- Add seasonal adjustment: in summer, the "low load" zone may need to start later (midnight instead of 11 PM) due to higher ambient overnight temperatures.

## Risks / Constraints
- **TXV performance**: Older TXVs with fixed settings may not compensate well for higher suction pressure. Monitor superheat; replace failing TXVs before resetting suction pressure.
- **Compressor surge**: On screw compressors, too-high suction pressure at low load can cause surge. Confirm compressor unloading logic works correctly.
- **Product temperature during transition**: The 2-hour ramp is designed to manage this, but during high-load days in summer, test more aggressively before assuming margins.
- **Refrigerant migration**: On systems with multiple compressors on one suction group, raising suction pressure can cause refrigerant to migrate to the crankcase of idle compressors. Add crankcase heaters and confirm they're energized.
- **Fire code**: Ensure that case temperatures are maintained per local health department requirements. Document the validation test data.

## KPIs
1. **Suction pressure (psig)** per group — track against schedule target; daily compliance check
2. **Suction temperature superheat** (°F) — must stay within 8–12°F range during all zones
3. **Case product temperature** (°F, max) — pre-open measurement; must stay below limits
4. **Compressor kWh per suction group** — compare Zone 3 vs. Zone 1 on a per-hour basis
5. **Compressor start/stop cycles** — overnight cycles should decrease; track per 8-hour shift
6. **Rack COP** (BTU removed / kWh input) — target 20–30% improvement in Zone 3 vs. Zone 1

## M&V Plan (IPMVP Option C with submetering where feasible)
- **IPMVP Option**: B (Key Parameter Measurement) for rack-level savings; Option C for store-level.
- **Pre-retrofit**: 4-week baseline; regression model of suction pressure kW vs. outdoor temp + time-of-day.
- **Post-retrofit**: 4-week validation at new schedule; same regression model; compare kWh at equivalent conditions.
- **Granularity**: For best results, sub-meter the compressor branch at the rack controller kW input and track per suction group.
- **Savings persistence**: Establish that savings hold through seasonal transitions (test at 90 days, 180 days).

## Costs & Payback (indicative)
- **No new hardware** for most modern rack systems (controller likely already has BMS interface).
- **BMS programming labor**: $1,500–$4,000 (skilled technician, 8–16 hours).
- **Wireless data loggers** (for validation): $300–$800 (if not already present).
- **Total installed cost**: **$2,000–$5,000**.
- **Annual savings**: $4,000–$12,000/year.
- **Simple payback**: **0.2–1.2 years** — this is among the highest-ROI ECMs available for grocery refrigeration.

## Templates / Reuse
- Time-zone suction pressure schedule template (by season, by group)
- BMS trend graphics template: suction pressure, superheat, kW overlay per group
- Validation test data sheet: product temp logger locations, read times, pass/fail criteria
- Refrigeration suction reset commissioning memo template
