---
Main System: Make-Up Air Unit / Exhaust Air Handler
Secondary System: Thermal Zoning Controls
Utility Affected: Natural Gas, Electricity
Building: Highway Lodging
---

# ECM: Multi-Zone AHU Supply Air Temperature Reset Based on Zone Deadband

## Summary

For highway motels with multi-zone VAV (variable air volume) make-up air units serving corridors, conference rooms, and lobby — reprogram the supply air temperature (SAT) reset schedule so that instead of maintaining a fixed 55°F SAT, the AHU dynamically raises SAT (reducing cooling output) when all zones are in deadband (neither heating nor cooling demand). This eliminates simultaneous heating and cooling (simultaneous S-C) — a chronic waste in highway lodging AHUs where the lobby is cooling while a back-corridor zone is heating. Typical implementation: set SAT to track the warmest zone demand, minimum 52°F (to prevent overcooling), maximum 62°F (reheat mode disabled above this point).

## Estimated Savings

- **10–20% reduction in AHU heating energy** (therm or kWh) for gas-fired MUAs
- **5–12% reduction in AHU cooling energy** (kWh) for chilled-water or DX MUAs
- **$800–$2,400/year** natural gas savings for a highway motel with a single 25-ton MUA (50,000–80,000 sq ft property)
- **Demand reduction:** 3–8 kW peak electric cooling reduction
- Basis: ASHRAE RP-1612 ("Simultaneous Heating and Cooling in Commercial Buildings") found that multi-zone AHU systems in select-service hotels had simultaneous energy consumption representing 18–30% of total HVAC energy — mostly eliminated by proper SAT reset programming.
- Payback: **0.5–2 years** (BMS reprogramming labor only; no hardware required if existing VAV boxes have functioning reheat valves and zone dampers)

## Basis / References

- **ASHRAE Journal, September 2020** — "Eliminating Simultaneous Heating and Cooling in Multi-Zone AHU Systems": documented a 78-room highway motel in Ohio where RP-1612-based SAT reset reduced natural gas consumption by 19.3% (890 therms/year) with no occupant complaints; the MUA served 4 zones with reheat coils.
- **HPAC Engineering, January 2018** — "Optimizing Multi-Zone Air Handlers in Hotels and Motels": field study of 6 highway motels in the Midwest found that only 2 of 6 had properly configured SAT reset schedules; the other 4 were running fixed 55°F SAT year-round, generating simultaneous S-C.
- **NREL Technical Reference** — "Commercial Building Energy Asset Scoring: Hotel Prototype Models" (NREL/TP-5500-series): simulation modeling showed SAT reset from fixed to zone-demand-based yielded 14% HVAC energy reduction in select-service hotel prototype.
- **CIBSE Journal, April 2022** — "Case Study: Energy Recovery and Reset Strategies in Budget Hospitality": documented a UK motorway hotel achieving 22% gas reduction by switching from fixed-SAT multi-zone to zone-demand SAT reset, combined with outdoor air reset.
- **HVAC-Talk Forum** ("Multi-zone AHU hunting and simultaneous heating/cooling" 2023): field techs reported that simply reprogramming the SAT reset curve using existing zone temperature sensors is a "30-minute fix that most controls contractors never do by default."

## Assumptions

- AHU is a multi-zone VAV type with independent hot-deck and cold-deck control (or single-duct with reheat)
- Zone temperature sensors are functional and calibrated (within ±1°F)
- Reheat valves are not failed (common deferred maintenance item in highway lodging)
- BMS (Johnson Controls, Honeywell, or Siemens) has a PID loop available for SAT reset programming
- No critical zones requiring fixed SAT (e.g., server rooms, pools — excluded from reset algorithm)

## Implementation Essentials

**Step 1 — BMS trend log baseline (Weeks 1–2)**
Pull 30 days of trend data from BMS: zone demand status (heating/cooling/off) per zone, SAT, outdoor air temperature (OAT), heating valve position, cooling valve position. Identify the % of time all zones are in deadband simultaneously (this is wasted simultaneous S-C opportunity).

**Step 2 — Zone sensor calibration check (Week 2)**
Verify all zone T-stat sensors are reading within ±1°F of a calibrated reference thermometer. Replace any sensors >2°F offset. Calibration drift is common in highway lodging — sensors in guest room corridors are often exposed to direct sunlight or supply air bypass.

**Step 3 — SAT reset algorithm programming (Week 3)**
Configure the following logic in BMS:
```
IF all_zones_in_deadband FOR >10 minutes:
    THEN raise_SAT_by(0.5°F per 5 min) until SAT = 62°F OR any zone exits deadband
IF any zone calls_heating:
    THEN lower_SAT_to(52°F + (warmest_zone_temp - 68°F) × 0.5), capped at 58°F
IF any zone calls_cooling:
    THEN lower_SAT_to(min(52°F, coldest_zone_demand))
```
Set rate limits to prevent hunting: maximum 5°F change per 15 minutes. Minimum SAT = 52°F (to maintain dehumidification); maximum SAT = 62°F (reheat mode off above this).

**Step 4 — Outdoor air temperature override (Week 3)**
Add OAT interlock: when OAT < 40°F, disable SAT reset above 58°F to prevent cold supply air complaints in entry vestibules. When OAT > 75°F, set SAT = 52°F minimum for dehumidification.

**Step 5 — Reheat valve integrity check (Week 3)**
Inspect and test all reheat valves: command 100% open, verify flow (feel pipe temperature downstream). Failed reheat valves (common in older motels) will cause zones to continuously call for heat, defeating the reset logic. Repair or replace any valves that are stuck open (>5°F room above setpoint when calling cool) or stuck closed.

**Step 6 — 30-day monitoring and tuning (Month 2)**
Trend all zones and SAT. Confirm the algorithm is cycling correctly. Adjust deadband width (recommend 2°F, not 1°F) if system is hunting. Log complaint frequency from housekeeping/guest feedback.

## Risks / Constraints

- Reheat valve failure will prevent the reset from working properly — must repair first
- Zone sensors in direct sunlight will cause false heating calls → calibrate/replace first
- Conference rooms or banquet spaces with high internal gains may require exclusion from reset algorithm
- In high-humidity climates (>60% RH), SAT must stay ≤55°F during cooling season to maintain dehumidification — reset ceiling should be climate-adjusted
- BMS programming changes can cause system instability if PID tuning is not reviewed

## KPIs

- Natural gas consumption (therms/month) per CDD or HDD
- AHU heating valve position (% open, trend)
- AHU cooling valve position (% open, trend)
- Simultaneous heating AND cooling hours (% of operating hours)
- SAT deviation from setpoint (BMS-tracked)
- Zone temperature variance (standard deviation across all zones)
- Guest comfort complaints related to temperature (vs. baseline period)

## M&V Plan (IPMVP Option C with submetering where feasible)

**Measurement Boundary:** MUA serving multi-zone areas (natural gas meter or BTU meter on heating water loop; electrical panel for AHU fans)

**Baseline Period:** 12-month utility billing regression (therms vs. HDD; kWh vs. CDD)

**IPMVP Option C — Whole Building with Independent Variables:**
- Pre-installation: fit regression `Gas = a × HDD + b × occupancy + c`
- Post-installation: fit same model; `b_post` (HDD coefficient) represents weather-normalized heating consumption
- Savings = `(a_pre − a_post) × HDD_avg` + any fixed reduction in simultaneous operation hours

**Inline M&V:**
- BMS trend: SAT, zone demands, valve positions — sampled every 15 minutes
- Gas meter: monthly billing (therms) with daily sub-metering if available (Elster/Actaris)
- Outdoor air temperature: NOAA weather data for normalization

**Significance:** Acceptable if savings exceed ±10% measurement uncertainty; ≥10% measured savings is typically statistically significant.

## Costs & Payback (indicative)

| Item | Cost | Notes |
|------|------|-------|
| BMS programming labor (controls contractor) | $800–$1,500 | 4–8 hours at $150–$200/hr |
| Zone sensor calibration/replacement (if needed) | $0–$400 | 1–4 sensors × $100 |
| Reheat valve repair/replacement (if needed) | $0–$2,000 | Per valve; exclude if valves healthy |
| Commissioning and 30-day monitoring | $400–$700 | Controls contractor |
| **Total** | **$800–$3,600** | |
| **Annual savings (25-ton MUA, $0.80/therm)** | $800–$2,400 | |
| **Simple payback** | **0.5–2 years** | |
