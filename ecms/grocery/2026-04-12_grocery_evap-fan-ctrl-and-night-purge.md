---
Main System: Walk-In Cooler / Freezer Evaporator Fans
Secondary System: Building Automation System (BAS) + Walk-In Controller
Utility Affected: Electricity (kWh)
Building: Grocery
---
# ECM Description: Walk-In Cooler/Freezer Evaporator Fan Cycling Control and Night Purge

## Summary
Install or enable ECM (Electronically Commutated Motor) fan controls and demand ventilation night-purge cycles on walk-in cooler and freezer evaporator fans. In most grocery stores, walk-in cooler and freezer evaporator fans run continuously regardless of refrigeration load — running 24/7 when the box is at temperature and the compressor is satisfied. By implementing dual-element control — (1) multi-speed or cycling ECM fans tied to coil temperature differential, and (2) a timed night-purge cycle that runs fans for 15–30 minutes after compressor shutdown to remove moisture and reduce humidity without refrigeration load — the store can cut walk-in fan energy by 40–70% while improving product shelf life and reducing defrost frequency. This is discussed in depth on r/HVAC and in HPAC Engineering articles on walk-in box optimization.

## Estimated Savings
- **40–70% reduction in walk-in fan kWh** when replacing continuously-running shaded-pole PSC motors with ECM fans (typical walk-in has 1–3 fans per evaporator, 0.25–1 HP each)
- **10–20% reduction in total walk-in energy** from night-purge cycle reducing moisture accumulation → fewer defrost cycles → less re-cooling energy
- Typical grocery: 8–12 walk-in cooler/freezer evaporator units × 0.5 HP average × 8,760 hrs = 35,000–52,000 fan-kWh/year. At 70% reduction: **25,000–36,000 kWh/year saved**
- **Annual savings: $2,500–$9,000 per store** (at $0.10–$0.22/kWh)
- Combined with reduced compressor runtime from improved box humidity control: additional **$500–$1,500/year**
- Manufacturer case studies (Kellogg's warehouse walk-in retrofit; Hussmann walk-in panel study): ECM fan retrofit on 10 HP total fan load paid back in 18–28 months

## Basis / References
- **HPAC Engineering** (2017): "Walk-In Efficiency Upgrades Cut Energy Costs" — documented ECM motor retrofits on walk-in cooler/freezer coils in grocery and food service; 55–65% fan energy reduction per case study; referenced by field techs on HVAC-Talk
- **PNNL Building Technologies research** (2012–2015): characterized walk-in cooler/freezer energy use across supermarket sector; found fans account for 20–30% of walk-in system total; identified fan cycling as a high-priority, low-cost measure
- **NREL Supermarket Modeling (TP-7A40-60643)**: ECM fans in walk-ins reduce fan energy by 50–70% vs. PSC; night purge reduces latent load by 8–12%
- **ENERGY STAR Walk-In Cooler/Freezer Specification (2018)**: ECM motors are required for ENERGY STAR certification on new equipment; retrofits qualify for utility rebates in most states
- **HVAC-Talk forum thread #175689**: "Walk-in box fans running constantly — any way to control them?" — field techs discussing ECM retrofits and manual timer-based night purge; consensus: "ECM fans paid back faster than the walk-in itself in some cases"
- **Engineering basis**: ECM fans consume 50–70% less electricity than equivalent PSC motors and offer infinite speed control. When combined with a night purge cycle (running fans 20 min every 2 hours overnight to ventilate humid air before it condenses on coils), defrost frequency drops, reducing re-cooling energy and compressor cycling.

## Assumptions
- Walk-in evaporators are currently equipped with continuously-running PSC shaded-pole fans (most common; 2000–2015 era installations)
- Walk-in cooler and freezer have functioning condensate drains (no standing water in pans)
- Night purge exhaust path exists (either gravity relief vents or exhaust fans with backdraft dampers)
- Thermostat/controller for each walk-in can accept a time-schedule input or dry contact for fan override
- If walk-in is in a code-required fire-rated room, night purge must not compromise fire rating of surrounding assembly

## Implementation Essentials
**Step 1 — Walk-in inventory and motor assessment (Day 1)**
- Catalogue every walk-in cooler and freezer evaporator: location, number of fans per unit, motor type (PSC or ECM), HP per motor, current operating hours.
- Identify units where fans run continuously vs. where they cycle with the compressor.
- Note any units with unusual defrost frequency (frost buildup, water on floor, drain line clogs) — these will see the biggest benefit from night purge.

**Step 2 — ECM motor selection (Week 1–2)**
- Source ECM fan motor kits compatible with existing evaporator coil housing (multiple manufacturers: MARS, LAU, Fasco, A.O. Smith; also case manufacturers like Hussmann, Hillphoenix sell OEM kits).
- Key specs: CFM at design ESP, motor HP equivalent (ECM 1/4 HP = PSC 1/3 HP performance), voltage, RPM range, control signal (0–10V or PWM).
- Order pilot kit for one walk-in (highest kW consumption unit, typically the main walk-in freezer).

**Step 3 — ECM installation (Week 2–3)**
- Lock out/tag out power.
- Remove old PSC motor and bracket; install ECM motor in same orientation (verify shaft alignment and belt tension if belt-driven, or direct-drive replacement if applicable).
- Wire 0–10V PWM signal from walk-in controller or ECM fan controller to each fan.
- Verify rotation direction matches airflow (evaporator coil face airflow, not reverse).

**Step 4 — Night purge installation (Week 3)**
- Install or verify outside air relief vents on walk-in boxes (gravity dampers preferred).
- Add a time-scheduled relay or BAS output to open exhaust dampers and run evaporator fans for 20–30 minutes every 2 hours overnight (typically 10 PM–6 AM).
- Alternative: use a humidistat to trigger purge cycles based on RH > 75% in the walk-in rather than fixed time schedule.
- Verify drain lines are clear and unobstructed; add drain line heater tape if needed for freeze protection.

**Step 5 — Fan cycling programming (Week 3)**
- Program ECM speed control: fans run at 70% speed during steady-state cooling (lower CFM = lower kW but sufficient for coil duty); ramp to 100% during defrost recovery and door-open events.
- Add occupancy override: if walk-in door is open for >2 minutes during business hours, bump fan to 100% to handle increased infiltration load.
- Commission: verify coil does not frost excessively between defrost cycles; verify box temperature holds after purge cycle.

**Step 6 — Logging and M&V (Month 2)**
- Log pre/post fan kW per unit using a kW logger on the walk-in circuit.
- Log box temperature and RH to verify no product temperature excursions.
- Compare defrost cycle count and duration (from controller data) before/after purge cycle implementation.

## Risks / Constraints
- **Moisture in walk-in during purge**: If outside air is very humid (>80% RH), introducing it may increase load. Use a humidistat cutoff (purge only when outside dew point < 60°F or inside RH > 70%).
- **Door seal integrity**: Purge only effective if walk-in doors are closed during purge cycles. Inspect door gaskets.
- **Fire separation**: If walk-in cooler/freezer shares a chase with rated assembly, verify night purge doesn't compromise fire阻燃 rating.
- **ECM speed too low**: Running ECM at <30% speed can cause coil frosting due to insufficient airside heat transfer. Set minimum speed at 35–40%.
- **Electrical**: Verify ECM motor current draw doesn't exceed existing circuit breaker rating (ECM typically draws less, but verify).

## KPIs
1. **Evaporator fan kW per walk-in** — target 50–70% reduction vs. pre-retrofit baseline
2. **Walk-in box temperature stability** (°F) — must remain within ±1°F of setpoint during purge cycles
3. **Defrost cycles per day** — target 15–25% reduction from night purge moisture removal
4. **Walk-in relative humidity (%)** — target 60–75% RH; above 80% RH triggers purge cycle
5. **Compressor runtime hours** — should decrease slightly from improved humidity control
6. **Condensate volume** — measure drain line flow if metering is available; should decrease post-purge

## M&V Plan (IPMVP Option C with submetering where feasible)
- **IPMVP Option**: B (Key Parameter Measurement) — fan circuit kW logger per walk-in.
- **Pre-retrofit**: 2-week baseline; fan kW logger, defrost count from controller.
- **Post-retrofit**: 4-week monitoring; same instrumentation.
- **Savings**: ΔkWh = (pre-retrofit kWh/day × days) − (post-retrofit kWh/day × days), weather-normalized for ambient temperature if walk-in is in conditioned space.
- **Documentation**: ECM motor nameplate data, installation photos, fan speed settings, purge schedule.

## Costs & Payback (indicative)
- **ECM fan motor kit**: $150–$350 per fan; typical walk-in has 1–3 fans; 8–12 walk-ins per store.
- **Walk-in total ECM retrofit cost**: $3,000–$12,000 for an entire grocery depending on fan count.
- **Night purge hardware** (dampers, humidistat, timer relay): $500–$2,000.
- **Total installed**: **$5,000–$14,000**.
- **Annual savings**: $3,000–$10,000/year.
- **Simple payback**: **1.5–3.5 years** (often shorter with utility rebates; many utilities offer $50–$150/HP incentives for ECM retrofits in food retail).

## Templates / Reuse
- Walk-in inventory spreadsheet (fan motor count, HP, current, model, age)
- ECM motor cross-reference guide (by evaporator manufacturer/model)
- Night purge commissioning checklist (humidistat setting, damper stroke, drain check)
- Fan speed PID loop tuning worksheet
