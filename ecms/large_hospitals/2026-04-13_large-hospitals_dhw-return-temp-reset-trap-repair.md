---
Main System: Domestic Hot Water (DHW)
Secondary System: Steam Plant / Boiler Plant
Utility Affected: Natural Gas (therms), Makeup Water
building: Large Hospitals
---

# ECM: DHW Return Temperature Reset and Steam Trap Repair Program

## Summary

Hospitals operate 24/7 DHW systems with large standby losses. Two interlocking measures: (1) implement DHW supply temperature reset based on actual demand — dropping supply temperature from the typical 140°F to 120°F during low-demand overnight hours; and (2) launch a formal steam trap repair program targeting the ~15–30% of steam traps that fail open each year in hospital steam plants, wasting live steam to drain. Together they address the second or third largest natural gas end-use in hospital facilities.

## Estimated Savings

- **Natural Gas:** 5–12% of total hospital gas consumption for DHW/steam system
- **Absolute range:** 15,000–80,000 therms/yr for 200–500 bed hospital
- **Dollar savings:** $10,000–$60,000/yr (at $0.60–$0.90/therm)
- **Makeup water:** 5–15 gallons/minute reduction in failed trap leakage across a 300-bed hospital
- **Source:** ASHRAE Journal, "Hospital Steam System Efficiency," R. Parsons, July 2013 — 6–18% steam system gas savings from combined DHW reset + trap repair
- LBNL Hospital Benchmarking Study (LBNL-56718, 2005) — median DHW system energy use in hospitals: 18,000–55,000 Btu/sq ft/yr
- **Basis:** DHW ΔT reset: each 10°F reduction in supply temperature cuts standing losses ~3–4% (proportional to temperature differential to ambient). Failed steam traps (¼" orifice, 100 psig): ~8 lb/hr steam loss per trap. A 300-bed hospital typically has 200–500 steam traps; 30 failed = ~6,000 lb/hr steam lost continuously.

## Basis / References

- ASHRAE Journal, "Hospital Steam System Efficiency," R. Parsons, Jul 2013 — field testing showed 15–25% of steam traps in a hospital campus were failed at any given time; repair program yielded 11% annual steam cost reduction
- CIBSE Journal, "Steam Trap Management in Healthcare Facilities," K. MacDonald, Oct 2014 — ROI of annual trap survey programs; traps typically pay back in <3 months
- HPAC Engineering, "Save Money with DHW Reset," S. Shapiro, 2011 — documented 9% DHW energy savings in 400-bed hospital through OAT-reset supply temperature schedule
- Energy Star Hospital ENERGY STAR Score technical reference — DHW heating = 6–10% of total site energy in hospitals
- ASHRAE Handbook — HVAC Applications, Chapter 49 (NHS Hospitals) — DHW temperature recommendations and standby loss factors

## Assumptions

- Existing DHW system uses gas-fired water heater or flash steam heat exchanger
- Steam system operating pressure: 80–150 psig (typical hospital)
- Existing BAS has points for DHW supply temperature sensor and outdoor air temperature
- Facilities staff can conduct steam trap surveys (no contractor needed for visual/ultrasonic inspection)

## Implementation Essentials

### Step 1 — DHW return temperature sensor and baseline (Weeks 1–3)
- Install return water temperature sensor on the recirculation loop (if not already present)
- Confirm proper mixing valve setup (ASSE 1017 rated for recirculation) — note: code may require TMV (thermostatic mixing valve) downstream of recirculation loop; confirm with AHJ
- Log recirculation return temperature vs. time-of-day for 2 weeks to establish demand profile
- Typical hospital profile: peak morning (5–9 AM), lunch (11 AM–1 PM), evening (4–7 PM); overnight <20% of peak demand

### Step 2 — DHW supply temperature reset schedule (Weeks 2–5)
- Configure BAS to implement a time-based reset schedule:
  - Peak demand hours (5 AM–9 PM, weekdays): 140°F supply
  - Low demand (9 PM–5 AM, plus weekends): 120°F supply
- Alternative: OAT-linked reset — if OAT >70°F (warm weather), reduce to 130°F peak, 110°F low-demand
- Verify mixing valve outlet remains at 105–110°F (code-required bathing temperature) at all times
- Safety interlock: if any recirculation return temperature drops <100°F, revert to full temperature immediately

### Step 3 — Steam trap survey program (Weeks 3–10)
- **Phase 1 (Month 1):** Ultrasound survey of ALL steam traps site-wide using ultrasonic trap tester (~$300 instrument cost, or hire testing contractor at $15–25/trap)
  - Inspect condensate return system, all hospital wings, kitchen, sterilizer supply
  - Categorize: OK / Failed Open (blowing steam — replace) / Failed Closed (blocked — replace) / Weeping (moderate leak — schedule replacement)
- **Phase 2 (Month 2):** Replace all failed-open and failed-closed traps immediately; weeping traps within 90 days
- **Phase 3 (ongoing):** Quarterly visual/ultrasonic inspection of all traps — assign to facilities tech as annual task

### Step 4 — Trap replacement documentation
- Document each trap: location, trap type, size, OEM part number, condition
- Calculate savings per trap: for a 100 psig, ½" orifice failed-open trap: ~15 lb/hr steam loss = ~$2,500–$4,000/yr per trap
- Track total traps, failed count, annualized steam loss, repair cost, simple payback per trap

## Risks / Constraints

- **Code compliance:** Many jurisdictions mandate minimum DHW temperature (typically 110–120°F) at point of use; confirm mixing valve settings maintain compliance during reset periods.
- **Legionella risk:** DHW supply below 124°F may support Legionella growth in tanks. **However**, maintaining return temperature ≥124°F (not supply) is the primary Legionella control — the AHJ-accepted approach per ASHRAE 188 is to maintain 124°F return; supply can drop to 110°F if recirculation return is ≥124°F. Consult infection control and facilities director.
- **Steam trap replacement in live systems:** Some high-pressure traps require system shutdown; schedule during planned maintenance windows.
- **Boiler short-cycling:** If DHW load suddenly drops (overnight reset), boiler may short-cycle — adjust boiler firing rate or staging logic in BAS.

## KPIs

- DHW supply temperature (°F) — daily max/min/avg by time band
- Recirculation return temperature (°F) — must remain ≥124°F for Legionella control
- Steam trap fail rate: (# failed / total traps) — target ≤5%
- Steam makeup water consumption (gallons/month) — correlate with trap condition
- Total natural gas consumption (therms/month) — weather-normalized

## M&V Plan (IPMVP Option C with submetering where feasible)

**Baseline:** 12-month gas utility bills (monthly data) + spot-check metering of DHW system gas consumption at time-of-day bands. Confirm steam trap count and approximate fail rate via ultrasound survey.

**Post-installation:**
- Continuous gas metering on DHW system gas train (or use dedicated submeter)
- Monthly reporting: weather-normalized gas consumption (HDD-adjusted) vs. baseline regression
- IPMVP Option C (whole facility) or Option A (paste-in-place metering for steam system)
- Steam trap program M&V: calculate steam loss per failed trap (based on orifice size and pressure), multiply by number repaired, convert to therms using steam tables

**Savings verification:** 
- DHW reset: compare gas consumption by OAT band pre vs. post (should see measurable drop in gas use at OAT >65°F)
- Trap repair: quantify steam loss avoided via ultrasonic measurement before and after each repair

## Costs & Payback (indicative)

- **DHW temperature sensor + installation:** $150–$400 per sensor
- **BAS programming for reset schedule:** $500–$2,000
- **Ultrasonic trap tester (ultrasonic stethoscope):** $300–$800 (one-time, reuseable)
- **Steam trap replacement (avg per trap):** $35–$150 parts + $75–$150 labor per trap (varies by size/type)
- **Contractor survey (if outsourced):** $2,000–$6,000 for campus-wide survey (300–600 traps)
- **Total for 300-bed hospital trap program:** $5,000–$20,000 first year
- **Annual gas savings:** $10,000–$55,000/yr (combined reset + trap repair)
- **Simple payback:** 4–14 months (trap repair alone often pays back in <90 days)

## Templates / Reuse

- Steam Trap Survey Form (per trap: location, trap no., type, size, pressure, condition, action)
- Monthly DHW Gas Trend Log template
- Hospital DHW Reset Schedule Template (time-band settings for BAS)
