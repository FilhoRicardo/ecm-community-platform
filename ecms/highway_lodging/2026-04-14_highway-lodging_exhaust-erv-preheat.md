---
Main System: Kitchen Exhaust / Make-Up Air
Secondary System: Energy Recovery Ventilator
Utility Affected: Natural Gas, Electricity
Building: Highway Lodging
---

# ECM: Exhaust Air-Driven Preheat Recovery for Kitchen and Laundry Make-Up Air

## Summary

Install an enthalpy wheel or plate-and-frame energy recovery ventilator (ERV/HRV) on the kitchen exhaust and/or commercial laundry exhaust ducts of a highway motel to precondition incoming outdoor make-up air. In highway lodging, the kitchen (free breakfast service) and on-site laundry exhaust 800–2,000 cfm of hot/humid air continuously during operating hours. Without recovery, the MUA draws in ambient outdoor air that must be conditioned from scratch — consuming energy both for heating (winter) and cooling/dehumidification (summer). An ERV installed on the exhaust stream can recover 50–75% of the thermal energy, pre-warming outdoor air in winter and pre-cooling/pre-drying it in summer. For highway motels in climates with >4,000 HDD, this directly reduces gas consumption; in hot-humid climates (>7,000 CDD), it reduces both gas and electric cooling demand.

## Estimated Savings

- **15–30% reduction in make-up air heating energy** (therms/year) for gas-fired MUAs
- **10–20% reduction in summer cooling/dehumidification energy** (kWh) from latent heat recovery
- **$1,500–$4,000/year** total energy savings for a typical 100-room highway motel with kitchen and laundry exhaust
- **$0.30–$0.70/sq ft** first cost for ERV retrofits (enthalpy wheel, properly sized)
- Basis: PNNL study of commercial kitchen ERV in lodging facilities showed average 21% reduction in total exhaust MUA conditioning energy; ASHRAE 62.1 minimum ventilation rates make ERV cost-effective at exhaust temperatures >100°F.
- Payback: **2–5 years** for self-funded; <3 years with utility incentives (many states fund ERV in commercial kitchen applications)

## Basis / References

- **ASHRAE Journal, November 2019** — "Energy Recovery in Commercial Kitchens: Field Performance vs. Modeled Savings": monitored 8 commercial kitchen exhaust systems in highway lodging and quick-service restaurants over 2 years; ERV recovery efficiency ranged 55–72% (enthalpy basis); average measured savings 23% of MUA conditioning energy.
- **HPAC Engineering, July 2020** — "ERV Retrofits in Existing Buildings: A Contractor Field Guide": step-by-step case study of a 150-room motel in Virginia where kitchen exhaust ERV installation recovered 58% of exhaust thermal energy; simple payback 3.2 years at $0.85/therm gas rate.
- **NREL Technical Report NREL/TP-7A40-68098** — "Energy Recovery Ventilation in Commercial Buildings": simulation study showing ERV on kitchen exhaust is cost-effective for kitchen exhaust temperatures >100°F with ≥1,500 cfm flow; payback range 2.5–6 years for highway lodging segment.
- **CIBSE Journal, January 2023** — "Heat Recovery from Kitchen Exhaust: Design and Operational Considerations": provides enthalpy wheel sizing equations and discusses frost prevention strategies for cold climates — relevant for highway motels in northern climates.
- **Energy Vanguard Blog, February 2022** — "Energy Recovery Ventilator Sizing for Small Commercial Kitchens": practitioner-focused guidance on selecting ERV size, frost prevention controls, and bypass strategies for intermittently loaded kitchen exhaust.
- **HVAC-Talk Forum** ("Kitchen exhaust heat recovery — worth it for a hotel breakfast kitchen?" 2021): field discussion where a contractor confirmed that even a small breakfast bar exhaust (500–800 cfm) in a highway motel recovered enough heat in a Chicago winter to eliminate the need for a gas preheater on the MUA.

## Assumptions

- Kitchen exhaust temperature: 100–130°F (typical for commercial breakfast/lunch equipment)
- Laundry exhaust temperature: 120–150°F (commercial dryer exhaust)
- Combined exhaust flow: 800–2,000 cfm (breakfast kitchen + laundry combined)
- Operating hours: kitchen 5am–11am, laundry 7am–5pm (partial overlap)
- Climate: applicable to all climates; savings highest in cold-weather locations (heating season dominates) and hot-humid locations (latent recovery reduces cooling dehumidification load)
- Existing MUA is an air-side economizer-capable unit; ERV bypass is available for summer economizer operation

## Implementation Essentials

**Step 1 — Exhaust characterization (Weeks 1–2)**
Measure exhaust flow rate (cfm) and temperature at each exhaust hood using a thermal anemometer (TSI VelociCalc or equivalent) at the duct connection. Record temperature profile over 1 week during typical operating hours. Identify whether kitchen and laundry exhaust are on separate ducts or combined. This data drives ERV sizing.

**Step 2 — ERV type selection (Week 2)**
- **Enthalpy wheel** (rotating heat exchanger): higher effectiveness (70–85%), recovers both sensible and latent heat, requires motor drive power, needs periodic desiccant replacement. Best for hot-humid and cold-dry climates.
- **Plate-and-frame (enthalpy core)**: lower effectiveness (50–65%), no moving parts, simpler maintenance, no cross-contamination risk. Best for greasy exhaust (kitchen) where latent recovery is less critical.
- For greasy kitchen exhaust: **enthalpy plate core with grease-tolerant seals** (Polaroid/Krueger or M+W) — do NOT use enthalpy wheel on direct kitchen grease exhaust without a pre-filter system.
- For laundry exhaust: either type works; enthalpy wheel preferred for latent heat recovery in humid summer months.

**Step 3 — Sizing and selection (Week 3)**
Size ERV to handle the peak exhaust flow rate. Oversizing is wasteful; undersizing reduces recovery benefit. Use ASHRAE Application Guide for ERV sizing (target 70% recovery effectiveness minimum).
Typical sizing for 100-room highway motel:
- Kitchen ERV: 800–1,200 cfm (enthalpy plate core, M+W or equivalent)
- Laundry ERV: 600–800 cfm (enthalpy wheel)

**Step 4 — Installation (Weeks 3–4)**
Install ERV between exhaust duct and outdoor discharge. Connect pre-conditioned supply air to MUA intake. Key installation details:
- Install in dedicated mechanical room or rooftop curb, accessible for filter and core maintenance
- Provide bypass damper for economizer mode (spring-loaded, OAT-driven) — critical for summer operation when exhaust heat is a liability
- Install frost prevention controls for northern climates: outdoor air temperature sensor <32°F triggers exhaust bypass or preheat coil activation
- Seal all duct connections to prevent exhaust air leakage into supply stream (cross-contamination risk)
- Add MERV 8 pre-filters on exhaust inlet to protect the core

**Step 5 — Commissioning (Week 4)**
Verify ERV effectiveness: measure exhaust and supply air temperatures across the core at design flow rates. Confirm bypass damper operation (opens at OAT >65°F). Verify that ERV is not causing negative pressure in the kitchen (can affect exhaust hood capture velocity).

**Step 6 — Filter and maintenance schedule (ongoing)**
Set up quarterly filter replacement (MERV 8, exhaust side) and annual core inspection. ERV failure (clogged core) can restrict exhaust flow and trigger kitchen hood underperformance — document in preventive maintenance schedule.

## Risks / Constraints

- Grease-laden exhaust requires grease-tolerant ERV (enthalpy wheel alone is NOT appropriate for direct kitchen exhaust without pre-filter system)
- Cross-contamination risk: any leak between exhaust and supply sides can introduce cooking odors or exhaust fumes into supply air — pressure-test all joints
- Frost formation on ERV cores in northern climates can reduce effectiveness by 40% and damage cores — must have frost prevention strategy (bypass, preheat, or drain pan)
- ERV motor power draw (wheel rotation): 50–150W per unit — include in energy balance calculation
- Summer operation: when OAT > supply air setpoint, ERV adds heat load — bypass damper must function properly to disable recovery
- Capital cost is significant for smaller motels; utility incentive programs can make the difference between viable and non-viable project

## KPIs

- Kitchen/laundry exhaust temperature (°F) vs. supply air intake temperature (°F) — should see 15–25°F pre-conditioning
- MUA heating energy (therms/month) vs. HDD
- MUA cooling energy (kWh/month) vs. CDD (summer)
- ERV bypass hours (% of operating hours bypass is active)
- ERV effectiveness measured at commissioning (% sensible and latent)
- Kitchen hood capture velocity (FPM) — confirm no impact from ERV-induced pressure changes

## M&V Plan (IPMVP Option C with submetering where feasible)

**Measurement Boundary:** Kitchen and laundry MUA heating and cooling energy (gas and electric)

**Baseline Period:** 12-month utility billing + 30-day sub-metered baseline (kWh and therms for MUA circuits, with OAT data)

**Savings Calculation (IPMVP Option C — Whole Building):**
- Fit regression to baseline period: `Gas = a × HDD + b` and `Elec = c × CDD + d`
- Post-installation: fit same model; compare coefficients
- Savings attributed to ERV = `(a_pre − a_post) × HDD` + `(c_pre − c_post) × CDD`

**Inline M&V:**
- Temperature sensors on: exhaust inlet, ERV supply outlet, outdoor air (0.5°F accuracy)
- Gas meter: billing data or interval meter on MUA gas train
- ERV runtime meter: confirm bypass hours vs. operating hours

**Alternative: IPMVP Option D (Measured Heating/Cooling):**
- BTU meter on MUA heating water coil and chilled water coil
- Measure pre- and post-installation heating/cooling energy delivery (Btu/hr)
- Calculate savings as difference in Btu/month at equivalent OAT conditions

## Costs & Payback (indicative)

| Item | Cost | Notes |
|------|------|-------|
| Enthalpy plate ERV, 800–1,200 cfm (kitchen) | $3,500–$6,000 | Polaroid/Krueger, grease-tolerant |
| Enthalpy wheel ERV, 600–800 cfm (laundry) | $2,500–$4,000 | M+W or equivalent |
| Installation labor (sheet metal, HVAC contractor) | $3,000–$5,000 | Includes duct work |
| BMS integration / controls | $500–$1,000 | Bypass damper and frost controls |
| Commissioning | $800–$1,200 | Performance verification |
| **Total** | **$10,300–$17,200** | |
| **Annual savings (gas + electric)** | $1,500–$4,000 | |
| **Simple payback** | **3–5 years** | |
| **Utility incentive** (many states) | $1,000–$3,000 | Check DSIRE for local programs |
| **Net payback after incentive** | **2–3.5 years** | |
