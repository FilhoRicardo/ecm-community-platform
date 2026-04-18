---
Main System: Chiller Plant
Secondary System: Condenser Water System
Utility Affected: Electricity (kW/kWh)
building: Large Hospitals
---

# ECM: Chiller Plant Sequencing with VSD Condenser Water Pump Reset

## Summary

Most large hospitals run all chillers at full design condenser water flow regardless of load. This ECM implements two coordinated strategies: (1) chiller lead/lag sequencing based on real tonnage demand via BMS, and (2) VSD-controlled condenser water pumps with differential pressure reset — reducing pump speed from 60Hz to as low as 35–40Hz during shoulder seasons and part-load conditions. The combination targets the largest electricity end-use in hospital chilled water plants, typically 30–45% of total building EUI.

## Estimated Savings

- **Electricity:** 8–18% of chiller plant total kWh consumption (typical hospital chiller plant: 500,000–2,000,000 kWh/yr per strategy)
- **Absolute range:** 150,000–400,000 kWh/yr for a 400-bed hospital with 3–4 chillers
- **Demand reduction:** 50–150 kW coincident peak reduction
- **Source:** PNNL High Performance Buildings: "Hospital Chiller Plant Optimization" (PNNL-23019, 2013); ASHRAE Journal case studies showing 12–22% chiller plant kWh savings from combined sequencing + VSD control
- **Basis:** Chiller shaft power follows a nonlinear affinity law — pump BHP ∝ RPM³. At 50% speed, pump power drops to 12.5% of full load. Condenser pumps at hospital design are typically 40–75 HP each; running at 40Hz instead of 60Hz cuts pump power from ~50 HP to ~7 HP per pump.

## Basis / References

- PNNL, *Hospital Chiller Plant Optimization*, PNNL-23019 (2013) — documented 18% chiller plant kWh savings at a 500-bed regional medical center through optimized chiller sequencing and VSD condenser water pumps
- ASHRAE Journal, "Optimizing Hospital Chiller Plants," D. Beggs, Oct 2015 — detailed field data showing 8–14% savings from differential pressure reset on condenser water loops
- HPAC Engineering, "When One Chiller Isn't Enough," D. Redl, 2014 — lead/lag sequencing case study, 3-chiller plant, 11% annual kWh reduction
- ASHRAE Handbook—HVAC Systems and Equipment, Chapter 36 (Chillers) — affinity laws for pump/compressor power: BHP₂/BHP₁ = (RPM₂/RPM₁)³

## Assumptions

- Hospital has ≥2 chillers, at least one chiller ≤60% of plant capacity
- Existing BAS has capacity to add chiller staging logic and VSD control points
- Condenser water pumps are currently constant-speed, accept VSD retrofit
- Summer peak building load accounts for ≥40% of annual cooling degree-days (typical US climate)

## Implementation Essentials

### Step 1 — Baseline metering and trend logging (Weeks 1–4)
- Install or verify power meters on each chiller feed and each condenser water pump motor
- Log 1-minute interval data for ≥4 weeks covering a range of OAT (outdoor air temperature) conditions
- Document current lead chiller selection logic and staging thresholds
- Record current condenser water pump flow rates (verify at least one pump is bypassed or THW use confirmed)

### Step 2 — Develop chiller staging curve (Weeks 2–4, parallel)
- Using trend data, build a tonnage vs. OAT scatter plot
- Identify minimum stage loading thresholds — typically 60% of smallest chiller capacity before second chiller stages on
- Define staging curve: single-chiller band (e.g., 300–700 tons), two-chiller band (700–1,400 tons), etc.
- Configure BAS to automatically select lead chiller based on run hours equalization

### Step 3 — VSD installation on condenser water pumps (Weeks 3–6)
- Install VFDs on each condenser water pump (typically 2–4 pumps per chiller plant)
- Retain one pump as manual bypass for emergency operation
- Install differential pressure (DP) sensor at the furthest or most hydraulically remote condenser
- Connect VFD to BAS analog output (0–10VDC or 4–20mA)

### Step 4 — DP reset programming (Weeks 5–8)
- Establish DP setpoint range: typical high setpoint 15–25 psi (ΔP across condensers), minimum setpoint 8–10 psi
- Configure BAS to reset DP setpoint downward as building cooling load decreases
- Key trigger: chiller load ≤70% → begin DP reset; chiller load ≤40% → minimum DP setpoint
- Validate: ensure condenser water temperature rise across condensers stays ≥8°F (indicating adequate flow)

### Step 5 — Commissioning and seasonal verification
- Verify no nuisance chiller shutdowns during transitions
- Confirm lead-chiller run-hours equalization (target: no chiller >20% more run-hours than any other)
- Test at shoulder-season OAT 50–65°F and verify stable operation

## Risks / Constraints

- **Chiller safety lockouts:** Some older chillers require minimum condenser water flow — confirm with OEM before reducing pump speed. Minimum flow rates typically 1.5–2.0 GPM/ton.
- **Runabouts for oil lubrication:** Centrifugal chiller oil sumps need minimum flow — never reduce below OEM minimums.
- **Condenser tube fouling:** Reduced flow increases velocity through condenser tubes; fouling factor changes can alter performance curves.
- **Summer peak:** DP reset strategy must NOT reduce condenser water flow during periods when all chillers are at full load and OAT >90°F — test specifically at these conditions.

## KPIs

- kWh/chiller-ton-hour (seasonal average — compare pre/post same OAT band)
- Condenser water pump kW (trend daily peak, weekly average)
- Run-hour equalization ratio: (max run-hours − min run-hours) / average run-hours — target <0.20
- Condenser water ΔT (°F) — ensure ≥8°F rise maintained during reset operation
- Plant Coefficient of Performance (CoP): chiller tons ÷ chiller kW — monitor for degradation

## M&V Plan (IPMVP Option C with submetering where feasible)

**Baseline:** 12-month utility bills + spot measurements of chiller plant kW at 4–6 OAT bands (40°F, 55°F, 70°F, 85°F, 95°F) using a power meter on each chiller feeder.

**Post-installation:** 
- Continuous kW metering on each chiller and condenser pump (circuit-level meters)
- Report monthly: plant kWh vs. OAT-normalized baseline (degree-day regression)
- IPMVP Option C (whole building, if no tenant split available) or Option B (plant-in-system)
- Measurement period: minimum 12 months post-installation, including one full cooling season

**Savings uncertainty:** ±10% at 95% confidence with continuous metering; ±15% with monthly billing only.

## Costs & Payback (indicative)

- VFD installation per 50 HP pump (including BAS integration): $6,000–$10,000
- DP sensor and installation: $800–$1,500
- BAS programming and commissioning: $3,000–$8,000
- Power metering (if not existing): $1,500–$3,000 per circuit
- **Total for 2-pump plant:** $18,000–$34,000
- **Annual electricity savings (400-bed hospital):** $20,000–$55,000/yr (at $0.10–$0.14/kWh)
- **Simple payback:** 8–20 months (incentives may be available from utility DSM programs)

## Templates / Reuse

- BAS sequencing script template: "Chiller Lead-Lag Sequence v2" — reuse for any multi-chiller hospital
- Trend logging template: 4-week OAT-vs-tonnage data collection form
- Commissioning checklist: Condenser VSD Reset Pre/Post Form
