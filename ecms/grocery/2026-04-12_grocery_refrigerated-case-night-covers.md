---
Main System: Display Cases (Remote Rack Refrigeration)
Secondary System: Building Automation System (BAS)
Utility Affected: Electricity (kWh)
Building: Grocery
---
# ECM Description: Refrigerated Display Case Night Covers

## Summary
Install insulated, close-fitting covers on open-front refrigerated display cases (dairy, deli, produce, fresh meat) during closed hours. Covers reduce radiative and convective heat ingress into cases, lowering compressor cycling frequency and rack load during unoccupied periods. This is one of the most widely discussed low-cost ECMs on HVAC-Talk and r/HVAC forums — straightforward enough for a night stocker crew to install, impactful enough to show up on utility sub-meter data within 30 days.

## Estimated Savings
- **15–30% reduction in display case refrigeration load during covered hours** (estimated 2,000–3,500 hours/year of cover use for a typical grocery with 10–12 hour overnight closures)
- **0.5–1.5 kWh/ft of case per year** for open-front multi-deck cases (typical grocery: 150–300 linear ft of open cases)
- **Annual savings: $3,000–$15,000 per store** depending on case footage, local utility rate ($0.08–$0.22/kWh), and HVAC system interaction
- A 45,000 ft² store with 250 linear ft of open-front cases at $0.12/kWh can expect **$7,000–$12,000/year in combined refrigeration and HVAC reduction**
- Note: If the store HVAC runs continuously, some of the refrigeration heat rejection is removed by HVAC — covering cases reduces both loads, so total building savings may partially overlap. Best to submeter case branch separately before/after.

## Basis / References
- **PNNL Field Study of Supermarket Refrigeration System Performance** (PNNL-25362, 2016) — monitored 8 supermarkets, found open-case infiltration loads represent 15–35% of total case refrigeration load; night covers reduce this directly
- **EnergyVanguard Blog** (Dr. Allison Bailes, now EnergyVanguard): multiple posts documenting 15–25% case load reduction with night covers; discussed in context of supermarket superheat/subcooling diagnostics (referenced widely on r/BuildingPhysics)
- **Hussmann Corporation case studies**: manufacturer documentation of energy savings from night covers on dairy/produce cases; referenced in field service literature
- **DOE Advanced Energy Design Guide for Grocery Buildings >50% Energy Savings**: lists night covers as Tier 1 low-cost measure
- **HVAC-Talk forum thread #214300**: "Refrigerated case covers — do they really work?" — field techs reporting 10–20% overnight rack load drop based on rack suction pressure tracings
- **Engineering judgment validated against**: NREL/BTO supermarket modeling showing 8–12% total store kWh savings from night covers alone

## Assumptions
- Store operates 70+ hours/week with minimum 9 hours of closed/covered time per day
- Existing cases have compatible mounting hardware or cases can accept clip-on/adhesive track systems
- Night stocking crew available to install/remove covers (10–15 min per side for a typical 8-ft case)
- Covers are PVC/nylon with closed-cell foam core (R-2 to R-4), sized per case model
- If anti-sweat heater circuits are on open cases, those should be de-energized during covered hours via time clock or BAS override — this adds additional savings but must be coordinated

## Implementation Essentials
**Step 1 — Audit open-front cases (Day 1)**
- Walk the sales floor and catalogue every open-front refrigerated case: dairy, deli, produce, fresh meat, beverage. Note make/model, dimensions, and whether it currently has anti-sweat heater circuits.
- Count linear feet of open cases; identify any cases already equipped with sliding glass doors (those don't need covers).

**Step 2 — Sub-meter case refrigeration branch (Week 1–2)**
- Install a current transformer (CT) on the dedicated case lighting/refrigeration circuit breaker or on the suction group meter (if present) to establish a baseline.
- Log kW/kWh at 15-minute intervals for 2–4 weeks before cover installation. Include outdoor dry-bulb temperature as a co-variate.

**Step 3 — Select covers (Week 2)**
- Source from case manufacturer (Hussmann, Hillphoenix, Kysor/Warren, Zero-Zone) or third-party suppliers (Kool-Stop, Standard Refrigeration). Specify: case model, foam core thickness, fire rating (NFPA 701 or FMVSS 302), and "low-emissivity" inner surface if available.
- Order one cover set as a pilot for the highest-load case (usually the open-dairy multi-deck). Install per manufacturer instructions — typically magnetic strips, adhesive tracks, or bungee clips along case lips.

**Step 4 — Pilot test with BAS logging (Week 3)**
- Have BAS technician confirm that case suction pressure and rack superheat are being logged during the pilot period.
- Compare covered vs. uncovered night performance: suction pressure should drop (indicating lower load), compressor runtime per hour should decrease.

**Step 5 — Full rollout (Week 4+)**
- Procure remaining cover sets.
- Train night crew on install/removal procedure; post laminated instruction card on each case.
- If anti-sweat heaters are present, add a time-clock or BAS output to de-energize them during covered hours. Verify that case temperature stays within Food Code safe ranges (≤41°F for dairy/deli) during covered periods with product loaded.

## Risks / Constraints
- **Food temperature compliance**: Cases must stay at or below 41°F (refrigerated) or 0°F (frozen) during covered periods. Run a 48-hour validation test with product loaded before going live. If product temp rises, covers may reduce air circulation too much — consider perforated or vented covers.
- **Case model compatibility**: Some older cases lack mounting surfaces; custom-cut covers add cost.
- **Labor discipline**: If covers are removed inconsistently, savings evaporate. Integrate into night crew SOP with supervisor sign-off.
- **Interaction with store HVAC**: Covering cases reduces latent load on the dehumidification system. If store uses makeup air units, the net HVAC savings may be smaller than the rack savings alone — but total building savings are real.
- **Moisture accumulation**: In humid climates, covered cases can trap moisture under the cover, promoting mold. Require covers to be dry before folding/storing; inspect weekly.

## KPIs
1. **Case suction pressure (psig)** during covered hours — target 5–15 psig drop vs. pre-cover baseline (consistent across 3+ comparable nights)
2. **Compressor runtime fraction** per suction group during covered hours — target ≥15% reduction
3. **Display case branch kWh** during covered hours — target 20–35% reduction
4. **Food product temperature** at end of covered period (logged via wireless data logger) — must remain ≤41°F
5. **Anti-sweat heater energy** (if applicable) — verify de-energized during covered hours

## M&V Plan (IPMVP Option C with submetering where feasible)
- **IPMVP Option**: C (Whole Building) — use store-level electric meter with PRF regression; also B (Key Parameter Measurement) using suction pressure as proxy for case load.
- **Pre-retrofit period**: 4-week baseline with no covers; 15-min interval data on case branch kW, suction pressure, outdoor dry bulb.
- **Post-retrofit period**: Minimum 4 weeks of covered-night data; same interval logging.
- **Adjustment for weather**: Use PRF (Piecewise Linear or Change Point) regression: kWh = f(Tdb) to normalize for temperature differences between pre/post periods.
- **Savings calculation**: ΔkWh = (baseline model kWh) − (post-retrofit kWh), normalized to common weather conditions.
- **Report**: Monthly kWh trend chart; suction pressure overlay; simple payback calculation with utility cost.

## Costs & Payback (indicative)
- **Cover cost**: $30–$80 per linear foot (depends on manufacturer and foam thickness). Typical grocery: 250 linear ft × $50/ft = **$12,500 total**.
- **Installation labor**: $1,000–$2,500 (BAS integration, pilot validation, crew training).
- **Sub-metering hardware** (CT + logger): $800–$1,500 if not already present.
- **Total installed cost**: **$14,000–$16,000**.
- **Annual savings**: $7,000–$12,000/year.
- **Simple payback**: **1.3–2.3 years** (simple, high-ROI measure; often eligible for utility rebates).

## Templates / Reuse
- Kysor/Warren Night Cover Specification Sheet (per case model)
- Refrigeration night cover SOP template (crew instructions, sign-off log)
- BAS graphics: suction pressure trend with cover event overlay
