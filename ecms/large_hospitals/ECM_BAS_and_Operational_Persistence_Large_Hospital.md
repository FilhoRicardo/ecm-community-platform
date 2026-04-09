---
Main System: "[[BAS]]"
Category System: "[[Controls / Operations]]"
Utility Affected: "[[Multiple utilities]]"
Source Document: "[[AEDG50-LargeHospitals-2012.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: BAS Governance, Trend Review, and Hospital Operational Persistence

## Summary
Use BAS governance, trend review, and alarm rationalization to keep high-complexity hospital HVAC sequences functioning as intended rather than slowly drifting into persistent overrides that silently eliminate savings from multiple ECMs.

## Estimated Savings
- **CIBSE Guidance**: 8–15% of total building energy through controls persistence and operational governance
- **ASHRAE Guidance**: 10–20% of HVAC energy in buildings with established override drift (per ASHRAE Guideline 0.2 field evidence)
- **End-Uses Affected**: Whole-building controls persistence; HVAC, ventilation, lighting, and plant systems that depend on sequence fidelity

## Basis / References

### CIBSE References
- **Guide H** (Building Control Systems): BMS governance and FDD integration
- **TM54** (Operational Energy Evaluation): Ongoing monitoring protocols for complex buildings
- **CIBSE Commissioning Code A**: Persistent commissioning and trend log governance

### ASHRAE References
- **Guideline 0.2** (Ongoing Commissioning): Persistence framework and KPI trending
- **90.1** (Energy Standard): §10.4 and §6.4 for BAS performance monitoring requirements
- **Guideline 36** (High Performance HVAC Sequences): Override management as a pre-condition for high-performance sequences

### Other Standards
- **FGI 2018 Guidelines**: §5.1 for clinical controls governance and alarm rationalization in healthcare facilities

## Assumptions
Hospital systems are too complex for one-time commissioning; drift begins within 6–12 months of occupancy without active governance. Named operational ownership (designated FM/clinical engineer) is the single most critical assumption. Clinical staff workarounds can silently eliminate savings for months or years without structured review. BAS data infrastructure must support trending of at least 50 key control points across HVAC, lighting, and plant systems.

## Climate Zone Relevance
All climate zones; hospital system complexity is load-shape dependent but persistence applies universally.

## Interaction Notes
Supports and protects savings from all other hospital ECMs: decoupled ventilation, heat recovery chillers, airflow setback in procedure spaces, LED surgical lighting, air-side heat recovery, and critical/noncritical area programming. Weak BAS governance erodes savings from every other HVAC and controls measure. This is the enabling infrastructure for all other advanced sequences.

## Implementation Essentials
- **Governance structure**: Appoint named BAS owner; define weekly trend review ritual; establish alarm rationalization cadence (monthly review of top 20 persistent alarms)
- **Trending points**: Select 50–100 critical BMS points covering: OA flow by AHU, room pressure (critical care areas), reheat valve positions, chiller/boiler plant dispatch, lighting circuit status, override event count
- **Alarm rationalization**: Distinguish clinical safety alarms (mandatory) from operational nuisance alarms (candidates for suppression or logic correction)
- **Override management**: Define override threshold policy; any zone with >10 manual overrides per week triggers investigation before month-end
- **Seasonal recommissioning**: Re-verify control sequences after clinical moves, department changes, or major equipment replacement
- **Training**: Brief operations staff quarterly on intended operating envelopes; document control philosophy so new staff understand rationale
- **FDD integration**: If BMS supports FDD, configure fault detection for persistent simultaneous heating/cooling, stuck valves, and abnormal runtime patterns

## Risks / Constraints
- **BAS data exist but go unused without governance ritual**: Establish mandatory monthly review meeting with FM manager and clinical engineering lead
- **Clinical workarounds can silently eliminate savings**: Mitigate by tracking override counts per zone and reviewing with department heads quarterly
- **Alarm fatigue leads to critical alarms being dismissed**: Separate clinical safety alarms from operational alarms; configure automatic escalation for unresolved clinical alarms
- **Staff turnover erodes institutional knowledge**: Document control philosophy and commissioning intent in O&M manual; require onboarding training for new FM staff
- **BMS vendor may limit access to trend logs**: Specify open-data trending architecture in BMS contract; ensure FM retains ability to export trend data without vendor mediation

## KPIs
- Override count per zone per week (baseline vs rolling monthly average)
- Persistent alarm count by category (clinical safety vs operational nuisance)
- Monthly EUI by department where sub-metering exists (kWh/m², kBtu/ft²)
- Sequence-of-operations compliance rate: % of key control points within ±5% of design setpoint
- Simultaneous heating/cooling hours (valve position >5% on both heating and cooling coils) — target: <5% of operating hours
- Alarm rationalization completion rate: % of top 20 persistent alarms resolved or formally accepted
- Trend data capture rate: % of key points with >95% data availability per reporting period
- Time to resolve FDD-identified fault (target: <48 hours for critical, <5 business days for non-critical)

## M&V Plan
**Option C (Whole Building with Targeted Subsystem Trend Review)** per IPMVP

**Quantification approach:**
- Establish baseline energy and override/alarm metrics during 4–12 weeks of pre-implementation monitoring (identify trending gaps before formal baseline)
- Measure post-implementation performance quarterly: energy, override counts, alarm counts, sequence compliance
- Calculate avoided energy loss from eliminated override drift: quantify baseline simultaneous heating/cooling hours × marginal HVAC energy rate
- Normalize for clinical occupancy variations (patient bed count, OR scheduling) and weather (HDD/CDD)
- Pre/post comparison: minimum 3-month baseline vs 3-month post-implementation per year for persistence tracking

**Data collection:**
- BAS trend logs: valve positions, fan speeds, temperatures, pressures at 15-minute intervals for key points
- Override event log (timestamp, zone, user, duration, reason if captured)
- Alarm log summary (alarm type, count, duration, resolution status)
- Sub-metered energy by major system: AHU, chiller, boiler, lighting panels (kWh)
- Departmental occupancy proxy: patient count, OR procedure count, bed occupancy rate
- Outside air temperature, HDD, CDD for weather normalization

## Costs & Payback (Indicative)
- **Capex**: BMS programming, trending configuration, staff training: £2,000–8,000 (governance setup is primarily soft cost)
- **Opex**: FM staff time for monthly review meetings (~2–4 hours/month); annual training refresh
- **Simple payback**: <1 year for buildings with existing override drift; immediate for well-tuned buildings (prevents future drift)
- **ROI**: Very high; this is a controls-maintenance measure, not a capital upgrade. Lifecycle value exceeds most hardware ECMs if governance is sustained

## Templates / Reuse
*Boilerplate footer removed. See CIBSE Commissioning Code A and ASHRAE Guideline 0.2 for ongoing commissioning frameworks.*
