---
Main System: "[[Procedure Spaces]]"
Category System: "[[HVAC Controls]]"
Utility Affected: "[[Heating and Cooling]]"
Source Document: "[[AEDG50-LargeHospitals-2012.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Airflow Setback in Surgery and Procedure Spaces

## Summary
Reduce airflow in surgery and procedure areas during documented unoccupied modes while preserving readiness for rapid procedural recovery, positive pressure relationships, and infection-control requirements. This measure requires tighter operational governance than normal office-style scheduling because clinical accreditation standards govern minimum airflow rates, pressure relationships, and recovery times for operating and procedure rooms.

## Estimated Savings
- **CIBSE Guidance**: 30–50% of fan and reheat energy in high-ACFH procedure spaces during unoccupied periods (per CIBSE Guide B operating theatre setback data)
- **ASHRAE Guidance**: 20–40% of procedure-area HVAC energy during unoccupied hours when permitted by clinical governance (per ASHRAE 90.1 application guidance for hospitals)
- **End-Uses Affected**: Fan energy, ventilation conditioning energy, reheat energy, and cooling plant load in procedure areas

## Basis / References

### CIBSE References
- **Guide B** (HVAC): Operating theatre energy management and setback control methodology
- **CIBSE AM10** (Commissioning Management): Clinical systems commissioning and FDD integration

### ASHRAE References
- **90.1** (Energy Standard): §6.4 for HVAC setback control and minimum ventilation rate requirements
- **ASHRAE 170** (Ventilation for Healthcare Facilities): Table 7-1 minimum ACH requirements for operating rooms, procedure rooms, and recovery areas
- **AEDG50-LargeHospitals-2012**: Surgery-suite airflow setback as additional HVAC strategy in the large hospital guide
- **Guideline 36** (High Performance HVAC Sequences): Clinical zone setback sequences and recovery control

### Other Standards
- **FGI 2018 Guidelines**: §5.1 for OR pressure relationships, minimum air changes, and recovery requirements from setback
- **AAMI/AORN**: Perioperative standards for temperature, humidity, and pressure recovery following HVAC setback
- **ANSI/ASHE/ASHRAE 170-2017**: Governs minimum ACH recovery requirements in operating and procedure rooms

## Assumptions
Clinical accreditation requirements and infection control governance must be satisfied as the primary constraint. Minimum occupied ACH rates per ASHRAE 170 Table 7-1: Operating rooms ≥20 ACH fresh OA; Procedure rooms ≥12 ACH; Recovery rooms ≥6 ACH. Setback mode is only applicable to spaces with confirmed unoccupied periods of ≥2 hours where clinical governance permits recovery delay. Recovery time to full occupied ACH must not exceed 15 minutes for operating rooms per FGI 2018 and AAMI/AORN guidelines. Positive pressure relative to adjacent corridors must be maintained throughout setback recovery. Procedure room scheduling must be integrated into BAS logic so setback is triggered by room booking calendar.

## Climate Zone Relevance
All climate zones; benefit is proportional to the energy intensity of the procedure space HVAC system and the frequency/duration of unoccupied periods. Cold-dry climates have higher reheat energy per ACH, making setback more valuable; hot-humid climates have higher cooling energy per ACH. The clinical governance constraint applies uniformly across all climates.

## Interaction Notes
Supports and is enabled by decoupled ventilation (ECM_Decoupled_Ventilation_and_Reheat_Reduction_Large_Hospital) — decoupled OA treatment allows more aggressive setback because OA is already independently conditioned. Pairs with critical vs noncritical area programming (ECM_Critical_vs_Noncritical_Area_Programming_Large_Hospital) for non-procedure zones within the same floor. Synergizes with BAS governance (ECM_BAS_and_Operational_Persistence_Large_Hospital) which ensures setback sequences remain active and are not overridden by clinical staff without formal change management. Requires coordination with LED surgical lighting (ECM_LED_Surgical_and_Clinical_Lighting_Large_Hospital) for coordinated scene control during setback.

## Implementation Essentials
- **Clinical governance approval**: Obtain formal written approval from clinical governance (Infection Control Officer, Perioperative Director, Facilities Director) before implementing setback — document eligible room states, maximum setback duration, and recovery time requirements
- **Room eligibility criteria**: Only spaces with confirmed unoccupied periods ≥2 hours where recovery to full ACH can be achieved within 15 minutes per FGI 2018 and AAMI/AORN
- **Setback ACH targets**: Operating room setback: ≥4 ACH outside of procedural hours (minimum for housekeeping/terminal cleaning per FGI); Procedure rooms: ≥6 ACH during setback; verify minimum OA rate maintained per ASHRAE 170 during all setback modes
- **Recovery control sequence**: Configure room booking calendar integration with BAS; upon room booking event, begin recovery sequence (pre-condition) ≥30 minutes before scheduled procedure start
- **Pressure relationship maintenance**: Maintain positive pressure relative to adjacent spaces throughout setback and recovery; pressure sensors in OR/procedure rooms must trigger immediate alarm if pressure drops below +0.001 in. WC during setback
- **Clinical override capability**: Provide clinical staff with single-action override to restore full ACH immediately (for emergency procedures, unscheduled patient care); override must be logged and reviewed quarterly
- **FDD integration**: Configure BAS fault detection for: abnormal pressure recovery times (>15 min), pressure relationship failures, and setpoint drift during setback
- **Commissioning**: Test recovery time under empty room conditions; verify pressure relationships at 0%, 50%, 100% recovery; document with clinical governance sign-off

## Risks / Constraints
- **Misapplication creates safety/compliance risk**: Only implement setback in rooms with formal clinical governance approval and documented recovery procedures — unauthorized setback in unapproved spaces creates accreditation and patient safety risk
- **Staff workarounds can permanently disable the sequence**: If clinical staff override setback for convenience rather than clinical need, savings are lost — Mitigate: track override events monthly; review with clinical governance if override frequency exceeds 2 events/month per room
- **Recovery time exceeds 15 minutes**: If recovery takes >15 minutes, procedural readiness is compromised and clinical governance approval will be withdrawn — Mitigate: test recovery at commissioning and seasonally; upgrade recovery fans if 15-minute target cannot be met
- **Pressure relationship reversal during setback**: Negative pressure in OR/procedure room relative to corridor creates infection risk — Mitigate: BAS must maintain pressure monitoring and alarm on pressure drop; setback must not proceed if pressure sensor fails
- **Scheduling conflicts with emergency procedures**: PACU and holding areas may have unpredictable occupancy — Mitigate: exclude holding and PACU from setback unless explicit clinical governance approval obtained

## KPIs
- Airflow (ACH or CFM) in occupied vs setback mode by procedure space — target: ≥60% reduction in airflow during setback
- Reheat energy (kBtu/hr) in procedure areas during setback — target: ≥50% reduction during setback periods
- Recovery time from setback to full occupied ACH (minutes) — target: ≤15 minutes for OR per AAMI/AORN; ≤10 minutes for procedure rooms
- Pressure differential (in. WC) relative to adjacent spaces during setback and recovery — maintain ≥+0.001 in. WC at all times
- Number of unplanned overrides from setback to full ACH (per room per month) — target: ≤2 per room per month
- Energy savings (kWh/month) from procedure area HVAC setback — calculate as avoided fan + reheat during setback hours
- Clinical incident log: any pressure excursions or IAQ complaints during or following setback (should be zero)
- Data capture rate for pressure and airflow trends — target: ≥95% availability

## M&V Plan
**Option B (Retrofit Isolation — Zone/Subsystem Level)** per IPMVP

**Quantification approach:**
- Baseline: 4–12 weeks of procedure area HVAC energy during equivalent unoccupied periods (before setback implementation) — measure fan energy, reheat energy, and cooling energy during unoccupied hours
- Post-implementation: Continuous monitoring of setback hours, airflow reduction, and energy during setback vs occupied conditions
- Calculate savings: Avoided fan energy = (Baseline ACH × Baseline fan kW) − (Setback ACH × Setback fan kW); similar calculation for reheat using reheat coil kW at reduced airflow
- Verify recovery energy penalty: recovery energy increase in first 30 minutes post-setback must be included in net savings calculation
- Normalize for number of setback-eligible procedure hours (excluding emergency procedures and holiday periods)
- Pre/post comparison: minimum 4 weeks baseline vs 4 weeks post-implementation (same season preferred)

**Data collection:**
- Room booking calendar (timestamps, duration, room ID) — for setback window identification
- Airflow rate (ACH or CFM) by procedure space at 15-minute intervals during occupied and setback periods
- Supply air temperature (°F) by procedure space at 15-minute intervals
- Reheat valve position (%) or reheat coil energy (BTU/hr) by procedure space at 15-minute intervals
- Pressure differential (in. WC) relative to adjacent corridors at key procedure room locations
- Override event log: timestamp, room ID, user, duration, reason
- Outside air temperature (°F) for weather correlation
- Clinical incident log: pressure excursions, IAQ complaints during recovery periods (should be zero; flag any events)

## Costs & Payback (Indicative)
- **Capex**: BAS programming for setback schedule and recovery logic: £3,000–8,000; pressure sensors and integration: £2,000–5,000; clinical governance documentation: £1,000–2,000; commissioning and testing: £2,000–4,000
- **Opex**: Quarterly override review and clinical governance reporting: £500–1,000/year; annual pressure sensor calibration: £500–1,000/year
- **Simple payback**: <1 year in hospitals with ≥6 hours/week of setback-eligible procedure room unoccupied time; payback extends to 2–3 years if procedure room utilization is high (>70% weekly utilization)
- **ROI**: High per-unit savings due to high ACH rates in procedure spaces; each setback hour saves proportionally more than general ward setback

## Templates / Reuse
*Boilerplate footer removed. Reference ASHRAE 170-2017 Table 7-1, FGI 2018 Guidelines §5.1, and AAMI/AORN for minimum ACH and recovery requirements.*
