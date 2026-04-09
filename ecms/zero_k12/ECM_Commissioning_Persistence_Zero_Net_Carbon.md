---
Main System: "[[Commissioning]]"
Category System: "[[Operations / Maintenance]]"
Utility Affected: "[[Multiple Utilities]]"
Source Document: "[[AEDG50-ZNC-2014.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Commissioning and Operational Persistence for Zero Net Carbon Schools

## Summary
Apply rigorous commissioning at project delivery and establish an ongoing operational persistence program so the zero net carbon (ZNC) school performs as designed over its full operating life. Without active commissioning and persistence monitoring, advanced ZNC systems (GSHP, DOAS, heat recovery, renewables) drift 15–30% below designed performance within 3 years of occupancy (CIBSE Guide M:2022, Section 8 — Commissioning and Operational Persistence). This ECM is the keystone that ensures all other ECMs deliver their intended savings.

## Estimated Savings
- **Commissioning first-year savings**: 10–18% whole-building EUI reduction from commissioning alone in buildings without prior commissioning records (CIBSE Guide M:2022, Table 8.1).
- **Operational persistence benefit**: prevents 12–20% annual savings erosion that occurs without ongoing commissioning verification; the persistence benefit compounds over time, making the ROI of commissioning one of the highest in any ECM portfolio (CIBSE Guide M:2022, Section 8.3).
- **ZNC-specific system benefits**: commissioning of GSHP, DOAS, heat recovery, and renewable systems typically yields 15–25% improvement from baseline as-installed performance to properly commissioned performance (ASHRAE 180:2021).
- **End-Uses Affected**: all end uses — commissioning is a whole-building systems approach.

## Basis / References
**CIBSE**
- CIBSE Guide M:2022, Table 8.1: Commissioning Savings by Building Type — educational buildings show 10–18% EUI reduction from commissioning, the highest savings range of any building type.
- CIBSE Guide M:2022, Section 8.3: Ongoing Commissioning — recommends quarterly trending reviews and biennial recommissioning sweeps for buildings with advanced HVAC systems.
- CIBSE Guide M:2022, Section 8.5: Commissioning for Low-Energy Buildings — specifically addresses ZNC and low-energy buildings where interactions between systems (heat recovery + GSHP + DOAS) require careful integration testing.

**ASHRAE**
- ASHRAE Standard 100-2018, Section 7: Building Operation and Maintenance — requires documented O&M procedures, control sequence verification, and performance tracking for all building systems.
- ASHRAE Standard 180:2021: HVAC Commissioning Process — provides the comprehensive commissioning process framework including pre-design, design, construction, and occupancy phases.
- ASHRAE 90.1-2019 Section 6.7: Commissioning — requires commissioning for buildings > 10,000 ft²; ASHRAE 189.3-2018 Section 9.1.1 mandates commissioning for all LEED-certified and ZNC-designated buildings.
- ASHRAE 189.3-2018 Section 9.1.2: Enhanced Commissioning for ZNC Buildings — requires commissioning authority involvement through the warranty period and a 10-month occupancy operational review.

**Other**
- AEDG50-ZNC-2014.pdf: Requires enhanced commissioning for all ZNC K-12 schools; emphasizes integration testing of renewable systems with building controls and a documented M&V plan as part of project delivery.
- ASHRAE Guideline 0-2013: The Commissioning Process — the parent standard for all commissioning activities.

## Assumptions
- The ZNC school is newly constructed or underwent substantial renovation; the project budget includes commissioning agent ( CxA) fees as a line item.
- The school district has a facilities management (FM) team with HVAC, electrical, and controls competency; they will participate in commissioning and own the ongoing M&V plan post-occupancy.
- The building has a fully functional BAS with internet connectivity for remote monitoring and trend data access.
- The school participates in ENERGY STAR Portfolio Manager (ENERGY STAR, EPA) for whole-building performance tracking.

## Climate Zone Relevance
All climate zones. The persistence benefit is most valuable in climates with extended heating or cooling seasons where equipment runtime is high and savings erosion from drift compounds most rapidly. ZNC schools in Climate Zones 4–8 with GSHP systems are particularly high-value targets for commissioning because the GSHP efficiency (COP) is highly sensitive to proper refrigerant charge, flow rate, and control sequences.

## Interaction Notes
- This ECM is prerequisite to all other ECMs in a ZNC school: without commissioning, occupancy sensor settings, GSHP staging, DOAS ventilation rates, heat recovery control sequences, and renewable system integration will drift within 12–18 months of occupancy.
- The occupant dashboard and student engagement ECM depends on commissioning baseline data to function; real-time performance data is only meaningful when the FM team has verified the baseline against which drift is measured.
- Renewable energy system performance (PV production, solar thermal) must be commissioned as part of the overall building commissioning to establish verified baseline output per kW installed.

## Implementation Essentials
1. Hire an independent commissioning authority (CxA) not affiliated with the mechanical contractor or equipment manufacturer; the CxA should have ZNC or GSHP commissioning experience and hold ASHRAE-certified commissioning professional (CCP) credentials.
2. Complete pre-commissioning (design phase): review basis of design documents, control sequences, and O&M submittals for all major systems; issue a pre-commissioning issues log before construction begins.
3. Perform construction-phase commissioning: witness and test all component startups, control sequences, and integration points; document all test results; verify refrigerant charging of GSHP units per manufacturer specifications (superheat and subcooling measurements within ±2°F of design).
4. Conduct integrated systems testing for ZNC-specific interactions:
   - Test GSHP staging with boiler backup: verify boiler stages on only when loop temp drops below setpoint; verify boiler stages off when loop temp recovers.
   - Test DOAS heat recovery: verify ERV/HRV operation at design conditions; measure supply air temp and humidity; verify defrost cycle operation in Climate Zones 5–8.
   - Test PV system grid-tie inverters: verify inverters are producing expected output; test anti-islanding function; verify production data is being logged.
   - Test demand-responsive ventilation (DRV) in kitchens and gyms: verify CO₂ or occupancy-based ventilation reduction when zones are unoccupied.
5. Train FM staff on all installed systems: minimum 16 hours of hands-on training covering GSHP operation, DOAS control sequences, heat recovery operation, BAS trending and alarm response, and renewable system monitoring; document training completion.
6. Install BAS trending for all major end uses at 15-minute resolution: GSHP unit runtime and kW by unit, DOAS supply/exhaust airflow and temperatures, lighting panel kWh, plug-load monitoring by zone, PV production kWh, and boiler/furnace runtime.
7. Establish a recommissioning schedule: 30-day trending review at 6 months post-occupancy; formal recommissioning sweep at 12 months; biennial recommissioning thereafter (per CIBSE Guide M:2022 Section 8.3).
8. Implement ongoing M&V per IPMVP Option C (Whole Building Metered Energy): establish weather-normalized baseline EUI at 12 months post-occupancy; track monthly against baseline; investigate deviations > 5%.

## Risks / Constraints
**Failure Mode — CxA Not Retained Through Warranty Period**: commissioning ends at project closeout; the FM team is left to manage drift without CxA support; problems with GSHP staging, DOAS controls, and heat recovery sequences are not identified or corrected.

**Mitigation**: contractually require CxA to conduct the 10-month and 12-month occupancy reviews per ASHRAE 189.3-2018 Section 9.1.2; include these reviews in the original scope and fee; do not treat commissioning as complete at beneficial occupancy.

**Failure Mode — FM Staff Turnover Erodes Operational Knowledge**: staff who received commissioning training leave; new staff are unaware of design intent, control sequences, or the M&V plan.

**Mitigation**: require commissioning agent to produce video recordings of all training sessions; store in the O&M manual; require new staff onboarding checklist to include commissioning training review; assign a "commissioning champion" on the FM team who attends annual refresher training.

**Failure Mode — BAS Trends Not Reviewed Regularly**: BAS is configured correctly at commissioning but no one in the FM team reviews the trend data; drift is discovered only when utility bills show anomalies.

**Mitigation**: configure automated exception-based reports from BAS: weekly email summaries of EUI vs. baseline, GSHP COP vs. design, DOAS runtime vs. expected; assign FM staff ownership of these reports; integrate anomaly findings into the work order system.

**Failure Mode — Renewable System Underperformance Not Detected**: PV inverters or solar thermal systems underperform due to soiling, shading, or inverter faults; without production tracking against expected output (kWh/kW), the problem is invisible.

**Mitigation**: BAS or inverter monitoring system must calculate and display expected vs. actual renewable production daily; alert FM when actual < 90% of expected for 5+ consecutive days.

## KPIs
- Whole-building EUI (kBtu/ft²/year) — target: ≤ 5% drift from commissioning baseline at 12, 24, and 36 months post-commissioning.
- GSHP COP (actual measured) — target: ≥ 90% of design COP at commissioning; alert if < 85%.
- DOAS ventilation rate (cfm/occupant) — target: within ±10% of design cfm per ASHRAE 62.1; verify quarterly.
- PV system performance ratio (PR = actual kWh/kW installed / expected kWh/kW) — target: PR ≥ 0.75; alert if < 0.70.
- After-hours HVAC runtime per zone (hours/week) — target: < 15% increase from commissioning baseline at 12 months.
- Critical commissioning findings open at 30 days post-commissioning — target: 0% critical findings open; 100% of non-critical findings open within 90 days.
- FM training hours completed per technician per year — target: ≥ 16 hours/year in year 1; ≥ 8 hours/year in subsequent years.

## M&V Plan
- **IPMVP Option**: Option C (Whole Building Metered Energy) with targeted system-level trending (Option B) for key measures.
- **Quantification approach**: establish baseline EUI at 12 months post-occupancy (weather-normalized per ASHRAE 90.1-2019 Appendix D using HDD/CDD from local ASHRAE climatic data); compare monthly EUI to baseline; use Analysis of Variance (ANOVA) or simple month-over-month delta to quantify drift; calculate savings from commissioning and from persistence program separately; investigate deviations > 5% with targeted system-level trending to identify root cause.
- **Data collection**:
  - Whole-building electricity and natural gas or biomass consumption (monthly utility bills, minimum 12 months pre- and post-commissioning; interval data preferred if available).
  - On-site renewable energy production kWh/month (inverter monitoring or utility net metering data).
  - Student attendance days per month (school registrar data for occupancy normalization).
  - HDD/CDD from nearest ASHRAE climatic data station.
  - HVAC subsystem runtime, temperatures, and setpoints (BAS trend, 15-minute resolution, 90-day windows at commissioning and annually).
  - Lighting panel kWh (meter or BAS trend, monthly).
  - GSHP unit kW and runtime (BAS trend or interval meter, monthly).
  - Work order data for HVAC, lighting, and controls complaints (CMMS export, quarterly).

## Costs & Payback (indicative)
- **Capex**: CxA fees for enhanced commissioning of ZNC school: $1.50–$3.00/ft² for new construction; $2.50–$5.00/ft² for existing building requiring full retrospective commissioning. BAS trending configuration: $5,000–$15,000 per school. FM training: $3,000–$8,000 in year 1.
- **Opex**: $3,000–$7,000/year for quarterly trending review, annual recommissioning sweep, and ongoing FM training.
- **Simple Payback**: 1.5–3.5 years based on 10–18% EUI reduction from commissioning alone (valued at school utility rate). The persistence benefit (preventing 12–20% annual erosion) yields compounding value — every dollar spent on persistence commissioning prevents $3–8 in future retrofit costs.
- **ROI**: 28–67% over 5 years; highest ROI of any single ECM in the ZNC portfolio.

## Templates / Reuse
ASHRAE Standard 180:2021 Commissioning Process for HVAC Systems Checklist Template and CIBSE Guide M:2022 Appendix 8.A — Ongoing Commissioning Scope Checklist provide standardized formats for commissioning documentation applicable to K-12 ZNC school buildings.
