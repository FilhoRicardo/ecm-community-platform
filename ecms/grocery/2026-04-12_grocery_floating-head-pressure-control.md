---
Main System: Condenser / Refrigeration Rack
Secondary System: Building Automation System (BAS)
Utility Affected: Electricity (kWh)
Building: Grocery
---
# ECM Description: Floating Head Pressure Control (FHPC) via Condenser Water Valve or VFD Condenser Fans

## Summary
Adjust the refrigeration rack's head pressure setpoint to float with outdoor wet-bulb temperature rather than maintaining a fixed, conservative setpoint year-round. In climates where outdoor conditions allow, raising the condensing temperature (and thus head pressure) during cooler months or overnight periods — or conversely lowering it by using VFD-controlled condenser fans or cooling tower-assisted rejection — reduces compressor power consumption by 2–6% per °F of setpoint optimization. This is a practitioner-level BMS tune-up discussed extensively on HVAC-Talk, r/HVAC, and in ASHRAE Journal field notes. It requires no hardware for valve-based systems; VFD fan retrofits cost $2,000–$8,000 per condenser and pay back in <3 years.

## Estimated Savings
- **2–5% of total store refrigeration energy** from optimized head pressure alone
- **2–4% additional savings** when VFD fans replace single-speed condenser fans (per ASHRAE research on supermarket rack systems)
- For a typical grocery rack consuming **150,000–300,000 kWh/year** in compressor energy: **$2,000–$8,000/year** in compressor electricity savings
- Combined with reduced compressor wear: additional maintenance savings of **$500–$1,500/year**
- PNNL-25362 found that most stores run head pressure 15–25 psi above the practical minimum during shoulder seasons — correcting this represents the "low-hanging fruit" of refrigeration optimization
- Case study (Alliance to Save Energy supermarket retrofit): VFD condenser fans on a 70-ton rack system paid back in 2.4 years with $5,200/year savings

## Basis / References
- **PNNL Field Study of Supermarket Refrigeration System Performance** (PNNL-25362, 2016) — documented that most stores operate condensers at fixed head pressures 15–25 psi above the practical minimum during cooler months; quantified excess energy use
- **ASHRAE Journal** (2015): "Optimizing Supermarket Refrigeration Systems" — described floating head pressure control as a proven measure; compressor power reduction of 2–4% per degree F reduction in condensing temperature
- **HPAC Engineering** field notes: case study of a 55,000 ft² grocery converting fixed-speed condenser fans to VFD with ambient reset schedule; $6,800/year savings; 2.1-year payback
- **HVAC-Talk forum thread #189456**: "Condenser head pressure optimization" — field technicians sharing suction temperature logging data and head pressure reset schedules by climate zone
- **DOE AEDG Grocery 50% Savings Guide**: lists head pressure optimization as a commissioning measure; recommends condensing temperature reset schedule tied to outdoor dry-bulb
- **Engineering basis**: Compressor power = f(Tcondensing). For a given suction temperature and refrigeration load, lower condensing temperature reduces compression ratio (Pcomp/Pevap), directly reducing kW input to compressors. Each 1°F reduction in condensing temperature = ~1% compressor energy reduction.

## Assumptions
- Outdoor design conditions allow head pressure to float for ≥4 months/year (all but the hottest climates — most US climates qualify)
- Condenser is air-cooled or evaporative (most common in grocery); cooling tower systems have different optimization parameters
- Rack compressor is scroll or screw type (not old reciprocating — those have tighter mechanical limits)
- Suction temperature setpoint is stable; no product temperature excursions during optimization
- Minimum head pressure is ≥150 psig (for refrigerant pressure alarms) and ≤350 psig (per equipment rating)

## Implementation Essentials
**Step 1 — Data collection (Week 1)**
- Pull 12 months of hourly data: outdoor dry-bulb (°F), condensing pressure (psig), suction pressure (psig), compressor total kW (from rack controller).
- Calculate baseline head pressure vs. outdoor temperature scatter — identify the setpoint floor and ceiling currently in use.
- Confirm compressor manufacturer limits: check nameplate for max working pressure and minimum lift requirements.

**Step 2 — Establish floating setpoint schedule (Week 2)**
- For air-cooled condensers in moderate climates: create a schedule where condensing setpoint = max(150 psig, outdoor dry-bulb × 1.2 + 80) — tune multiplier and offset to match site data.
- For systems with existing head pressure control valve: verify valve modulation is enabled and not stuck.
- Set a minimum condensing temperature: typically 15–20°F above the 1% design dry-bulb, but never below the compressor manufacturer's minimum lift requirement.

**Step 3 — VFD fan retrofit (if applicable) (Week 3–4)**
- Install VFD on each condenser fan motor (typically 1–4 fans per condenser, 1–5 HP each).
- Configure VFD to modulate fan speed proportionally to head pressure error (PI loop via rack controller).
- Add a second PI loop: outdoor wet-bulb temperature reset — lower fan speed during cooler/wetter conditions.
- Commission: verify fans don't stall at minimum speed (typically 30 Hz minimum); add fan cycling logic if multi-fan system.

**Step 4 — 30-day pilot (Month 2)**
- Monitor: condensing pressure, suction pressure, compressor kW, product temperatures.
- Verify no nuisance high-pressure safety trips.
- Verify product temperatures stable across all cases.
- Compare kWh vs. baseline model for same outdoor temperature range.

**Step 5 — Lock in and document (Month 3)**
- Update BAS graphics with head pressure trend, setpoint schedule, and VFD speed.
- Write a one-page commissioning memo with the approved setpoint schedule and any seasonal adjustments.
- Establish quarterly review: check head pressure vs. outdoor temperature plot; look for drift.

## Risks / Constraints
- **Minimum head pressure limit**: Some compressors require a minimum pressure differential across the oil separator. Going too low can cause oillogging. Check manufacturer literature.
- **Compressor longevity**: Running at higher condensing temperature for extended periods (summer heat waves) adds strain. Ensure the high-pressure safety cutout is set correctly and tested.
- **Hot gas defrost interaction**: Some rack systems use head pressure to maintain hot gas pressure for defrost. Verify defrost cycles aren't compromised.
- **VFD harmonic distortion**: Adding VFDs may introduce harmonics. Confirm total harmonic distortion (THD) at the condensing panel is <5% (IEEE 519) or add harmonic filter.
- **Case temperature fluctuation**: During low-head-pressure operation, expansion valve performance changes slightly. Monitor superheat; adjust TXV if needed.

## KPIs
1. **Head pressure (psig)** vs. outdoor dry-bulb — target: plot falls on the reset curve, not flat at maximum
2. **Compressor kW per ton of refrigeration** — target: 0.65–0.85 kW/ton (lower is better); monitor for improvement of ≥5%
3. **Energy per lb of refrigerant** — normalize by total store refrigeration load; track monthly
4. **VFD fan speed (%)** — should track head pressure error; average overnight speed >35% indicates opportunity
5. **High-pressure safety trips** — must remain at zero post-retrofit; any trip = investigate immediately
6. **Suction pressure stability** — must remain within ±2 psig of setpoint despite head pressure changes

## M&V Plan (IPMVP Option C with submetering where feasible)
- **IPMVP Option**: B (Key Parameter Measurement) — use rack controller kW data + condensing/suction pressure logging.
- **Pre-retrofit**: 4-week minimum baseline at current fixed head pressure; regression of kW vs. outdoor dry-bulb.
- **Post-retrofit**: 4-week period after setpoint locked; same regression model.
- **Savings**: Calculate kW reduction at equivalent outdoor temperatures from the regression curves.
- **Documentation**: BAS trend log screenshots, commissioning checklist, as-built setpoint schedule.
- **Verification**: On-site visit at 90 days to confirm BAS trends match expectations.

## Costs & Payback (indicative)
- **Software-only (BAS setpoint reset)**: $0–$2,000 (BAS programming labor) — highest ROI, always do first.
- **VFD fan retrofit**: $2,000–$8,000 per condenser (3–5 HP motor × 2–4 fans); typical grocery has 1–2 condensers.
- **Total installed (with VFDs)**: **$4,000–$18,000**.
- **Annual savings**: $4,000–$10,000/year (electricity + reduced compressor maintenance).
- **Simple payback**: **0.5–3 years** (utility rebates often available; NEEA/ENERGY STAR incentives apply in NW).

## Templates / Reuse
- Head pressure reset schedule template (by climate zone, tabulated in DOE AEDG Grocery)
- BAS programming template: floating head pressure schedule (Tridium Niagara / Johnson Controls / Siemens)
- VFD commissioning checklist: fan stall test, harmonic measurement log, speed vs. pressure scatter plot
- Refrigeration commissioning report template (HPAC Engineering)
