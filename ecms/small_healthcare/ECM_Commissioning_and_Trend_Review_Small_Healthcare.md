---
Main System: "[[Commissioning]]"
Category System: "[[Operations]]"
Utility Affected: "[[Multiple utilities]]"
Source Document: "[[AEDG30-SmallHealthcare-2009.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Small Healthcare Commissioning and Trend-Based Persistence

## Summary
Use commissioning, trend review, and early operational correction to preserve the value of ventilation, lighting, and DHW ECMs in healthcare settings. Small healthcare facilities are particularly vulnerable to operational drift because they typically have smaller facilities teams with less specialized controls expertise, and clinical workarounds can quickly erode savings from even well-commissioned systems.

## Estimated Savings
- **CIBSE Guidance**: 8–15% of total building energy through persistent commissioning and controls governance (per CIBSE Commissioning Code A data)
- **ASHRAE Guidance**: 10–20% of HVAC energy in buildings with established override drift (per ASHRAE Guideline 0.2 field evidence)
- **End-Uses Affected**: Whole-building operational persistence; HVAC, ventilation, lighting, and DHW systems that depend on sequence fidelity

## Basis / References

### CIBSE References
- **Commissioning Code A**: Persistent commissioning requirements and trend log governance
- **TM54** (Operational Energy Evaluation): Ongoing monitoring protocols for small healthcare buildings
- **Guide H** (Building Control Systems): BMS governance and alarm rationalization for healthcare facilities

### ASHRAE References
- **Guideline 0.2** (Ongoing Commissioning): Persistence framework and KPI trending
- **90.1** (Energy Standard): §10.4 and §6.4 for BAS performance monitoring requirements
- **AEDG30-SmallHealthcare-2009**: Chapter 8 — QA/commissioning as essential to achieving package savings target

### Other Standards
- **FGI 2018 Guidelines**: §5.1 for clinical controls governance and alarm rationalization in healthcare facilities

## Assumptions
Small healthcare facilities (typically <50,000 ft²) have smaller FM teams with less controls specialization, making persistence governance more challenging than in large hospitals. Clinical staff workarounds can silently eliminate savings within months of occupancy without structured review. BAS data infrastructure must support trending of at least 20–30 key control points. Named operational ownership is critical — one staff member must be designated as the commissioning lead.

## Climate Zone Relevance
All climate zones; clinical system complexity is load-shape dependent but persistence applies universally.

## Interaction Notes
Supports every major measure, especially DOAS, reheat reduction, and clinical lighting controls. This is the enabling infrastructure for all other ECMs to deliver persistent savings. Weak commissioning persistence erodes savings from ECM_DOAS_with_Heat_Recovery_Small_Healthcare, ECM_Condenser_Heat_Recovery_Small_Healthcare, and ECM_Patient_Room_and_Clinical_Lighting_Optimization_Small_Healthcare. Synergizes with ECM_Classify_Critical_vs_Noncritical_Areas_Small_Healthcare to ensure classified spaces maintain their design intent.

## Implementation Essentials
- **Commissioning completeness**: Commission airflow, pressure, humidity, lighting scenes, plant control sequences, and DHW temperature before occupancy; verify all sequences operate as designed across representative load conditions
- **Trend monitoring**: Trend at least 20–30 critical BMS points covering: OA flow by AHU, zone temperatures and reheat valve positions, lighting circuit status, DHW supply/return temperatures, alarm counts
- **Override management**: Define override policy; any zone with >5 manual overrides per week triggers investigation before month-end
- **Alarm rationalization**: Distinguish clinical safety alarms (mandatory) from operational nuisance alarms (candidates for suppression or logic correction)
- **Seasonal re-commissioning**: Re-verify control sequences after clinical moves, department changes, or major equipment replacement
- **Training**: Brief operations staff quarterly on intended operating envelopes; document control philosophy in O&M manual
- **FDD integration**: If BMS supports FDD, configure fault detection for persistent simultaneous heating/cooling, stuck valves, and abnormal runtime patterns

## Risks / Constraints
- **Staff turnover erodes institutional knowledge**: Document control philosophy and commissioning intent in O&M manual; require onboarding training for new FM staff; maintain commissioning records accessible to all FM staff
- **Clinical workarounds can silently eliminate savings**: Mitigate by tracking override counts per zone and reviewing with department heads quarterly; provide clinical staff with formal override request process so overrides are logged and reviewed
- **Small FM teams may lack commissioning expertise**: Consider engaging commissioning agent for seasonal checks; specify commissioning requirements clearly in vendor contracts
- **BAS vendor may limit access to trend logs**: Specify open-data trending architecture in BMS contract; ensure FM retains ability to export trend data without vendor mediation

## KPIs
- Override count per zone per week (baseline vs rolling monthly average)
- Monthly EUI by department (kBtu/ft² or kWh/m²) where sub-metering exists
- Reheat intensity (kBtu/ft²) by zone type — detect drift vs baseline
- Humidity excursions (count/month where zone RH exceeds ±10% of setpoint)
- Alarm closure rates (% of alarms resolved within 48 hours)
- Sequence-of-operations compliance rate: % of key control points within ±5% of design setpoint
- Trend data capture rate: % of key points with >95% data availability per reporting period
- Time to resolve FDD-identified fault (target: <48 hours for critical, <5 business days for non-critical)

## M&V Plan
**Option C (Whole Building with Targeted Subsystem Trend Review)** per IPMVP

**Quantification approach:**
- Establish baseline energy and override/alarm metrics during 4–12 weeks of pre-implementation monitoring
- Measure post-implementation performance quarterly: energy, override counts, alarm counts, sequence compliance
- Calculate avoided energy loss from eliminated override drift: quantify baseline simultaneous heating/cooling hours × marginal HVAC energy rate
- Normalize for clinical occupancy variations and weather (HDD/CDD)
- Pre/post comparison: minimum 3-month baseline vs 3-month post-implementation per year for persistence tracking

**Data collection:**
- BAS trend logs: valve positions, fan speeds, temperatures, pressures at 15-minute intervals
- Override event log (timestamp, zone, user, duration, reason if captured)
- Alarm log summary (alarm type, count, duration, resolution status)
- Sub-metered energy by major system: AHU, lighting panels, DHW (kWh)
- Outside air temperature, HDD, CDD for weather normalization

## Costs & Payback (Indicative)
- **Capex**: Commissioning agent (pre/post occupancy): £2,000–6,000; BAS trending configuration: £1,000–3,000; staff training: £500–1,500
- **Opex**: FM staff time for monthly review meetings (~1–2 hours/month); annual seasonal re-commissioning check: £1,000–3,000/year
- **Simple payback**: <1 year for buildings with existing override drift; immediate for well-tuned buildings (prevents future drift)
- **ROI**: Very high; this is a controls-maintenance measure, not a capital upgrade. Lifecycle value exceeds most hardware ECMs if governance is sustained

## Templates / Reuse
*Boilerplate footer removed. Reference CIBSE Commissioning Code A and ASHRAE Guideline 0.2 for ongoing commissioning frameworks.*
