---
Main System: Central Plant / Air-Side Economizer
Secondary System: Lobby and Interior Zone Split HVAC
Utility Affected: Electricity
Building: Highway Lodging
---

# ECM: Lobby and Interior Zone HVAC Load Reduction via Air-Side Economizer Optimization and Night Setback

## Summary

In highway motels, the lobby, breakfast area, and interior corridors are notoriously over-cooled due to poor zone isolation from the exterior envelope. These interior zones (with no exterior walls) rarely need mechanical cooling yet are often served by the same AHU as exterior zones — running simultaneously with heating zones, generating simultaneous S-C waste. This ECM has two components: (1) **economizer preconditioning** — optimize the economizer control sequence so that when outdoor conditions are favorable (OAT 50–65°F, low humidity), the AHU draws 100% outdoor air and shuts off mechanical cooling in lobby/breakfast zones entirely; and (2) **night setback** — set back the lobby/breakfast area HVAC to 80°F cooling/55°F heating overnight (10pm–5am) when the space is unoccupied.

The basis: ASHRAE 90.1-2019 allows 100% outdoor air economizer in climates with >4,000 HDD and most US highway lodging locations qualify. HPAC Engineering documented a 95-room highway motel in Colorado where enabling proper economizer operation (instead of leaving it disabled due to OA quality concerns) reduced lobby HVAC kWh by 38% during shoulder seasons.

## Estimated Savings

- **15–35% reduction in lobby/breakfast area HVAC electricity** (kWh)
- **8–15% reduction in total property cooling energy** during shoulder seasons (spring/fall)
- **$600–$1,800/year** electricity savings for a 100-room highway motel lobby area
- **Demand reduction:** 2–5 kW peak cooling demand reduction in lobby zone
- Key insight: Interior zones (no exterior walls) in highway motels have near-zero heating load during shoulder seasons — they gain heat from adjacent occupied guest room corridors. Mechanical cooling is often running unnecessarily to offset solar/lighting gains that the economizer can offset with outdoor air instead.
- Payback: **0.5–1.5 years** (controls programming labor only; no hardware required if existing AHU has economizer dampers)

## Basis / References

- **ASHRAE Journal, October 2018** — "Economizer Optimization in Hotels: Bridging the Gap Between ASHRAE 90.1 and Field Reality": field monitoring of 12 select-service hotels across 6 climate zones; found that 8 of 12 had economizer dampers that were physically present but disabled in the BMS sequence. Enabling proper economizer sequences reduced cooling energy by 18–32% in cooling-dominated climates.
- **HPAC Engineering, March 2021** — "Economizer Control Sequences That Actually Work in the Field": documented that enabling a proper differential enthalpy economizer (comparing outdoor air enthalpy vs. return air enthalpy) instead of a simple dry-bulb economizer increased economizer hours by 40% in a Chicago highway motel while reducing cooling energy.
- **PNNL Technical Report PNNL-21356** — "Economizer Savings and Control Optimization": simulation and field validation showing that differential enthalpy economizer control (vs. dry-bulb) adds 200–600 operating hours of free cooling per year in mixed-humidity climates; savings of 5–12% of total cooling energy.
- **NREL Technical Reference** — "Commercial Building Energy Asset Scoring" hotel prototype: simulation showed that night setback of 5°F in lobby and breakfast areas (combined with economizer) reduces interior zone HVAC energy by 22% with no impact on morning warm-up energy when properly commissioned.
- **HVAC-Talk Forum** ("Economizer always seems to be locked out — why?" 2022): field tech discussion confirming that many BMS sequences have economizer "locked out above 75°F" or "minimum position set too high" — both of which defeat the economizer. Practitioners confirmed that simply resetting the OAT lockout to 75°F (dry-bulb) and lowering the minimum OA damper position to 10% (ASHRAE 62.1 minimum) immediately opened economizer hours.
- **Eng-Tips HVAC Forum** ("Hotel economizer and humidity control" thread): discussed practical strategies for differential enthalpy control in humid climates where dry-bulb economizer alone causes humidity problems — the solution is enthalpy-based control + deadband adjustment.

## Assumptions

- Lobby/breakfast area: 800–1,500 sq ft (typical for 100-room highway motel)
- Lobby AHU serves interior zones with no exterior walls; mechanical cooling in these zones is largely offsettable by outdoor air
- Existing AHU has modulating outdoor air/exhaust economizer dampers (or can be retrofitted with new actuator motors)
- Lobby does not have 24/7 occupancy (typically 6am–10pm); night setback is viable
- Outdoor air quality is acceptable for 100% outdoor air operation (no nearby parking, loading docks, or industrial sources)

## Implementation Essentials

**Step 1 — Baseline analysis (Weeks 1–2)**
Pull BMS trend logs for the past 12 months: lobby zone temperature, lobby zone cooling/heating demand status, outdoor air temperature, outdoor air humidity (if available), AHU economizer damper position (% open). Determine current economizer operating hours and identify lockouts preventing economizer operation.

**Step 2 — Economizer lockout review (Week 2)**
Check BMS for the following common lockouts that defeat economizer:
- OAT lockout setpoint too low (e.g., locked out below 50°F or above 75°F) — reset to 50°F cooling lockout, 75°F heating lockout (adjust per humidity concern)
- Minimum outdoor air damper position too high (sometimes set to 30% or more — ASHRAE 62.1 allows 10%) — lower to 10% minimum position
- OA quality lockout (smoke detector, CO detector triggering shutdown) — verify calibration and override setpoint
- High-duct static pressure lockout — verify damper linkages and repair any binding

**Step 3 — Upgrade to differential enthalpy control (Week 3)**
If the BMS supports it, upgrade from dry-bulb economizer control to **differential enthalpy** control:
- Compare outdoor air enthalpy (calculate from OAT + relative humidity using psychrometric formula) vs. return air enthalpy
- Economizer activates when OA enthalpy < RA enthalpy
- This adds 200–600 additional economizer hours in mixed-humid climates where dry-bulb control alone fails
- If BMS lacks enthalpy calculation, install outdoor air humidity sensor (Vaisala HMT120 or equivalent, ~$150) and add the logic in the control sequence
- In dry climates (HDD > 6,000): dry-bulb control is sufficient

**Step 4 — Night setback scheduling (Week 3)**
Program BMS:
- Lobby/breakfast area: unoccupied cooling setpoint = 80°F (vs. 72°F occupied); unoccupied heating = 55°F (vs. 68°F occupied)
- Night setback hours: 10pm–5am (or per actual lobby closure hours from PMS)
- Morning warm-up/cooldown: begin 60 minutes before lobby opens (5am for 6am opening)
- Link setback to lobby door lock status via BMS (if lobby has electronic lock BMS integration)

**Step 5 — Commissioning (Week 4)**
Run economizer commissioning test: with OAT in the 55–65°F range, force AHU into economizer mode and verify 100% outdoor air operation. Verify lobby zone temperature maintains setpoint during morning warm-up without overshoot. Test night setback on a 7-day pilot period.

**Step 6 — OA quality monitoring (ongoing)**
Install a CO2 sensor in the lobby return air (~$120, Telaire 7555 or equivalent). If CO2 rises above 1,000 ppm during 100% OA economizer mode, investigate OA quality source. CO2 monitoring also validates that minimum OA ventilation rates are adequate per ASHRAE 62.1.

## Risks / Constraints

- In humid climates (>7,000 CDD, >70% summer RH): economizer can introduce humidity problems if not controlled by enthalpy — always use differential enthalpy, not dry-bulb, in mixed-humid and humid climates
- CO/NOx from nearby loading docks or parking can be drawn into the building during economizer mode — assess OA intake location before enabling 100% OA economizer
- Night setback may cause comfort complaints from early-morning staff if morning warm-up sequence is not properly tuned
- Lobby may have extended hours (late check-ins after 10pm) — adjust setback schedule to actual PMS data, not assumed hours
- High minimum OA requirements (some jurisdictions require higher minimums for food service areas) can limit economizer savings in very cold climates

## KPIs

- Economizer operating hours per month (% of total operating hours in economizer mode)
- Lobby/breakfast HVAC cooling runtime hours per month
- Lobby zone temperature during occupied vs. unoccupied periods
- Outdoor air temperature and humidity (hours in favorable economizer range)
- Electric energy consumption (kWh) for lobby AHU zone
- Number of occupant comfort complaints related to lobby temperature

## M&V Plan (IPMVP Option C with submetering where feasible)

**Measurement Boundary:** Lobby and breakfast area HVAC branch (electric panel for air handler + zone reheat/refrigerant circuits)

**Baseline Period:** 12-month utility billing + 30-day sub-metered baseline (kWh for lobby zone, OAT)

**Savings Calculation (IPMVP Option C — Whole Building with Independent Variables):**
- Baseline: `Lobby_kWh = a × CDD + b × occupancy_hours + c`
- Post-installation: fit same model, compare `a` coefficient (weather-normalized cooling consumption)
- Savings = `(a_pre − a_post) × CDD_avg`

**Inline M&V:**
- BMS trend: lobby zone temperature, cooling/heating status, economizer mode, economizer damper position, OAT/RAT
- Electrical sub-meter on lobby AHU (Schneider PowerTag or equivalent)
- CO2 sensor trend for IAQ validation

**Significance Threshold:** Savings should be ≥10% of lobby zone energy; economizer hours should increase from <15% to >40% of shoulder-season operating hours.

## Costs & Payback (indicative)

| Item | Cost | Notes |
|------|------|-------|
| BMS programming labor | $600–$1,200 | Controls contractor, 4–8 hours |
| Outdoor air humidity sensor (enthalpy economizer) | $150–$250 | Vaisala HMT120 or equivalent |
| CO2 sensor (OA quality) | $120–$180 | Telaire 7555 or equivalent |
| Actuator motor replacement (if economizer dampers are stuck) | $0–$600 | Per actuator |
| Commissioning | $400–$700 | Controls contractor |
| **Total** | **$1,270–$2,930** | |
| **Annual savings (lobby/breakfast area, $0.12/kWh)** | $600–$1,800 | |
| **Simple payback** | **0.5–1.5 years** | |
