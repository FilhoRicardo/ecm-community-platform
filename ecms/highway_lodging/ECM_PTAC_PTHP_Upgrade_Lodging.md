---
Main System: "[[Guestroom HVAC]]"
Category System: "[[HVAC]]"
Utility Affected: "[[Electricity and Gas]]"
Source Document: "[[AEDG30-HighwayLodging.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: High-Efficiency Guestroom Unitary HVAC Upgrade

## Summary
Replace legacy guestroom PTAC (Package Terminal Air Conditioner) or PTHP (Package Terminal Heat Pump) with higher-efficiency models that improve part-load operation, reduce standby fan energy, and eliminate simultaneous heating/cooling waste. In highway lodging with many individually conditioned guestrooms, unit efficiency upgrades can reduce HVAC electricity by 15–35% and gas consumption where applicable (ASHRAE 90.1-2019 Table 6.8.1A — Minimum Efficiency Requirements for PTAC/PTHP).

## Estimated Savings
- **Cooling energy reduction**: 15–30% reduction in PTAC cooling kWh when replacing SEER 8–9 units with units meeting ASHRAE 90.1-2019 efficiency levels (EER ≥ 11.7 for PTAC in climate zones 1–2; ≥ 10.9 in climate zones 3–5).
- **Heating energy reduction**: 10–25% reduction in PTHP heating kWh (heat pump provides 1.5–2× heating energy per kWh vs. electric resistance, reducing gas use in dual-fuel or electric properties).
- **Fan standby energy**: 200–500 kWh/room/year reduction from eliminating continuous fan in unrented rooms through fan-delay-off or vacating logic.
- **End-Uses Affected**: guestroom cooling, guestroom heating, and fan energy.

## Basis / References
**CIBSE**
- CIBSE Guide H:2019, Table 5.2: PTAC/PTHP Efficiency Ranges and Savings Potentials — indicates 12–25% cooling energy reduction and 8–20% heating reduction from efficiency grade improvement.

**ASHRAE**
- ASHRAE 90.1-2019 Table 6.8.1A: Minimum Efficiency Requirements for PTAC and PTHP — requires EER ≥ 11.0 for PTAC in all climate zones (effective January 1, 2023 for new construction); PTHP requires COP ≥ 3.2 (electric resistance) or EER ≥ 10.9 (heat pump mode).
- ASHRAE 90.1-2019 Section 6.4.2: HVAC Control Requirements — requires automatic setback and OA damper closure for PTAC/PTHP in unoccupied rooms.
- ASHRAE 90.1-2019 Section 6.4.3: Outdoor Air Dampers — requires motorized OA dampers on PTAC/PTHP to close during unoccupied mode.

**Other**
- AEDG30-HighwayLodging.pdf: Built around small hotels and motels using unitary HVAC equipment; HVAC efficiency and control are core recommendation areas in the climate-zone guidance and implementation chapters.

## Assumptions
- Building has many individually conditioned guestrooms served by individual PTAC or PTHP units (typical highway lodging configuration).
- Units are 7–15 years old with degraded efficiency (typical real-world efficiency 70–85% of rated performance due to coil fouling, refrigerant charge loss, and compressor wear).
- Guestroom envelope has been evaluated (or will be addressed concurrently) so that right-sized units meet loads without significant oversizing.

## Climate Zone Relevance
- **Cold climates (Zones 5–8)**: PTHP upgrade provides highest value; heat pump COP of 3.0–3.5 can supply most heating at 1/3 the energy cost of electric resistance; gas PTHP reduces peak electric demand.
- **Hot climates (Zones 1–3)**: PTAC efficiency upgrade (higher EER) provides largest savings; focus on EER ≥ 12.0 and use of refrigerants with lower GWP.
- **Mixed climates (Zones 4)**: Both PTAC and PTHP efficiency matter; consider PTHP for properties with gas available (dual-fuel advantage).

## Interaction Notes
- Works synergistically with occupancy-based setback controls: efficient units achieve faster and more energy-efficient recovery from setback, making the setback ECM more valuable.
- Benefits from envelope air sealing: reduced infiltration means smaller, less expensive replacement units can meet load, improving first-cost economics.
- Complements corridor pressurization and ventilation controls: reduced PTAC OA intake during vacancy improves the effectiveness of envelope sealing and setback.

## Implementation Essentials
1. Audit installed equipment: document each PTAC/PTHP by location, age, rated efficiency (EER/COP), condition (coil cleanliness score 1–10, refrigerant pressure readings, amp draw vs. nameplate). Prioritize rooms with oldest and least-efficient units for replacement.
2. Right-size replacement units after envelope improvements: use ACCA Manual J or equivalent load calculation for each room orientation; target 400–450 cfm/ton for PTAC/PTHP (higher than residential split systems due to limited external static pressure).
3. Select replacement units meeting ASHRAE 90.1-2019 Table 6.8.1A minimums:
   - PTAC cooling: EER ≥ 11.0 (all zones); target EER ≥ 12.0 for climate zones 1–3.
   - PTHP heating: COP ≥ 3.2 (heat pump mode); or where gas is available, consider PTHP with gas furnace backup (thermal efficiency ≥ 80%).
   - Require integrated electronically commutated (ECM) fan motors for both occupied and standby fan modes.
4. Require new sleeves, grilles, and louvers matching the replacement unit dimensions; do not reuse old sleeves if they are corroded or undersized — improper sleeve fit is a primary cause of performance degradation in PTAC replacements.
5. Install condensate management: verify drain line slope and connection; install float switch cutoff to prevent water damage in high-humidity climates.
6. Integrate with occupancy setback controls: specify units with 24V relay or network communication (BACnet or similar) for integration with PMS or standalone occupancy controllers.
7. Commission each unit: verify refrigerant charge (subcooling or superheat method), airflow (cfm), temperature split (supply air °F vs. return air °F), and Amp draw vs. nameplate. Record baseline data for M&V documentation.
8. Set lockable guest setpoint range: limit guest adjustment to ±2°F from FM-defined occupied setpoint; lock extreme setpoints (below 60°F heating, above 82°F cooling) to prevent simultaneous heating and cooling cycles.

## Risks / Constraints
**Failure Mode — Improper Sleeve and Condensate Installation**: Reusing old sleeves or improper condensate routing causes thermal bypass, water damage, and premature unit failure within 2–3 years of installation.

**Mitigation**: Require all replacement projects to include new sleeve, exterior louver, and interior grille kit; verify condensate drain connection and slope; conduct water-test of drainage system before unit start-up.

**Failure Mode — Oversized Units**: If envelope improvements are not reflected in load calculations, replacement units may be larger than needed, causing short-cycling, reduced humidity control, and lower part-load efficiency.

**Mitigation**: Conduct post-envelope-load reduction calculations before ordering units; do not simply match old unit capacity — select based on actual measured loads; target 400–450 cfm/ton at design conditions.

**Failure Mode — Refrigerant Regulatory Compliance**: PTHP units using R-410A or R-134a may face future regulatory restrictions; selecting units with lower-GWP refrigerants (R-32, R-454B) future-proofs the investment.

**Mitigation**: Specify units using refrigerants with GWP < 750 (ASHRAE 34 designation A2L or A1); confirm availability with manufacturer for the property's voltage (208/230V single-phase typical for PTAC).

## KPIs
- PTAC/PTHP EER (Btu/hr·W) — target: ≥ 11.0 (ASHRAE 90.1-2019 minimum); ≥ 12.0 in climate zones 1–3.
- PTHP COP (heat pump mode) — target: ≥ 3.2 per ASHRAE 90.1-2019 Table 6.8.1A.
- HVAC kWh per occupied room-night — target: 15–30% reduction from pre-replacement baseline.
- Guest comfort complaints per 100 room-nights — target: < 1.0 complaints/100 room-nights related to temperature or humidity.
- Average guestroom HVAC runtime by season (hours/day) — target: maintain runtime within design range post-replacement; excessive runtime indicates undersizing.
- Refrigerant charge verification (% of nameplate) — target: within ±5% of nameplate charge.

## M&V Plan
- **IPMVP Option**: Option B (Modified Component Isolation) — isolate the HVAC system from other building loads using dedicated unit-level metering and whole-property normalization.
- **Quantification approach**: Install kWh meters on a representative sample of 10–20 replacement units and 10–20 control (pre-replacement) units; compare 12-month normalized cooling and heating energy. Use weather normalization (HDD/CDD) per ASHRAE 90.1-2019 Appendix D; extrapolate sample results to full building using unit count and occupancy distribution.
- **Data collection**:
  - Unit-level kWh (dedicated logger or BAS trend, 15-minute resolution, minimum 12 months pre and 12 months post for sampled units).
  - Refrigerant type and charge weight (service record).
  - Airflow (cfm) and temperature split (°F supply minus °F return) at commissioning (ASHRAE Standard 116 field-measurement form).
  - Outside air temperature and humidity (local weather station, hourly for HDD/CDD calculation).
  - Occupied room-nights per month (PMS export).
  - Guest complaint log categorized by room, complaint type, and date.

## Costs & Payback (indicative)
- **Capex**: PTAC replacement unit (cooling-only, EER 12.0, 230V): $900–$1,400/unit including labor and new sleeve/louver kit. PTHP replacement unit (heat pump + gas backup, EER 11.5, COP 3.3): $1,400–$2,200/unit. For a 100-room property with 50% unit replacement in year 1: $45,000–$75,000.
- **Opex**: $1,500–$3,000/year for annual maintenance, coil cleaning, and refrigerant leak inspection.
- **Simple Payback**: 4.5–8.0 years for PTAC cooling-only replacement; 3.5–6.5 years for PTHP replacement (dual-fuel advantage in climate zones 5–8). Payback improves by 1–2 years when replacement is timed with room refresh or reroom renovation cycle.
- **ROI**: 12–22% over 10 years (PTAC); 15–28% over 10 years (PTHP).

## Templates / Reuse
ASHRAE Standard 116-2010R Appendix A — Field Measurement Data Form for PTAC/PTHP Performance Verification and ACCA Manual J8:2020 Residential Load Calculation Procedure Worksheet provide standardized formats for unit commissioning data collection and right-sizing calculations applicable to guestroom unitary HVAC replacement projects.
