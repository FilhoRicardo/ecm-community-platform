---
Main System: "[[Lighting]]"
Category System: "[[Interior Lighting]]"
Utility Affected: "[[Electricity]]"
Source Document: "[[AEDG30-SmallHealthcare-2009.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Patient, Clinical, and Staff Lighting Optimization

## Summary
Use low-LPD, layered LED lighting with task-appropriate scenes in patient, exam, nurse-station, and treatment spaces rather than blanket high ambient levels. Small healthcare facilities have diverse clinical lighting needs that are poorly served by uniform overhead lighting — layered LED lighting with scene control addresses both energy and clinical quality.

## Estimated Savings
- **CIBSE Guidance**: 30–50% reduction in clinical lighting energy through LED conversion and scene control (per CIBSE LG7 and small healthcare case studies)
- **ASHRAE Guidance**: 25–40% lighting electricity reduction for healthcare facilities (per ASHRAE 90.1 Table 10.6.2 LPD limits and AEDG30-SmallHealthcare)
- **End-Uses Affected**: Interior lighting electricity, secondary cooling load (reduced heat gain from LED vs conventional sources), and maintenance costs

## Basis / References

### CIBSE References
- **LG7** (Lighting Guide 7): Healthcare lighting design, task lighting requirements, and control strategies
- **Guide A** (Environmental Design): Illuminance levels by clinical task and area type
- **TM39** (Building Energy Metering): Lighting energy submetering for healthcare facilities

### ASHRAE References
- **90.1** (Energy Standard): Table 10.6.2 for healthcare facility LPD limits; §10.4 for lighting controls requirements
- **AEDG30-SmallHealthcare-2009**: Space-by-space lighting and control logic for patient rooms, nurse stations, ORs, exam rooms, and treatment spaces

### Other Standards
- **IES RP-29** (Lighting Hospital Operating Rooms): Surgical task lighting illuminance requirements for procedure rooms
- **BS EN 12464** (Lighting of Work Places): Indoor workplace lighting requirements including healthcare
- **IEC 60598** (Luminaires Particular Requirements): LED luminaire safety standards for clinical environments

## Assumptions
Existing systems are assumed to be T8/T5 fluorescent or older LED technology with manual switching. Target LED efficacy: ≥130 lm/W for general lighting. Color temperature: 4000–5000K for exam/treatment (clinical blue-rich for tissue differentiation); 2700–3000K for patient rooms and sleep-safe modes. CRI ≥80 for general areas; ≥90 for exam and procedure lighting. Dimming range: 0–100% for all clinical luminaires. Control system must support scene recall for at least 4 scenes per zone.

## Climate Zone Relevance
All climate zones; LED heat gain reduction has a secondary cooling load benefit most significant in hot-humid climates. In heating-dominant climates, the heat gain reduction from LEDs slightly increases heating load — net impact should be assessed on a whole-building basis. LED conversion remains beneficial for maintenance cost reduction, controllability, and clinical quality regardless of climate.

## Interaction Notes
Pairs with ECM_Envelope_and_Glare_Control_Small_Healthcare for daylighting integration — improved glazing with daylight harvesting supports perimeter zone lighting reduction. Synergizes with ECM_Commissioning_and_Trend_Review_Small_Healthcare: lighting scene control should be integrated into BAS trend monitoring to detect scene abandonment. Complements ECM_Classify_Critical_vs_Noncritical_Areas_Small_Healthcare: accurate classification defines which spaces need clinical-grade lighting vs standard commercial lighting. Does not conflict with any other ECM.

## Implementation Essentials
- **Lighting audit by clinical area**: Map luminaires by clinical function: patient room ambient, exam task, nurse station, corridor/wayfinding, night-safe, emergency, and support lighting
- **Task-appropriate lighting layers**: Separate ambient (general), task (examination/procedure), reading, and night-safe functions — each layer sized for its specific task illuminance requirement
- **Scene control architecture**: Define clinical lighting scenes: Full Clinical (exam + procedure), Routine Care (task + general), Night-Safe (patient room night light <10 lux), Housekeeping (full ambient), Emergency (100% egress compliance)
- **Exam/procedure lighting requirements**: Verify ≥5,000 lux at task plane for exam rooms per BS EN 12464; ≥10,000 lux at 1 meter for procedure rooms per IES RP-29; CRI ≥90; color temperature 4000–5000K
- **Patient room requirements**: 2700–3000K for sleep-safe mode; ≤50 lux for night-safe (below waking threshold per ASHRAE 55); dimming range 0–30% for night-safe scene
- **Daylighting integration**: In perimeter support areas with windows, install daylight harvesting sensors; configure dimming to supplement natural daylight before activating artificial lighting
- **Driver quality specification**: Specify <5% THD at all dimming levels; verify flicker-free at all dimming levels (per IEEE 1789); no audible noise
- **Commissioning with clinical staff**: Commission all scene presets with end users (nurses, physicians, facilities); document each scene configuration and obtain clinical sign-off

## Risks / Constraints
- **Clinical acceptance depends on visual quality**: Any LED that fails to meet color rendering or illuminance requirements must be replaced — require luminaire submittals with IES LM-79 test data and clinical reference installations before bulk procurement
- **Poor scene usability causes permanent overrides**: If clinical staff find scene recall too complex, they override to a single static scene — Mitigate: ensure scene recall is <2 seconds; provide physical scene control panels at room entries (single button per scene); limit scenes to 4–6 per zone
- **Night-safe mode too dark for clinical response**: If clinician needs to respond to patient emergency, lighting must reach ≥100 lux within 5 seconds of scene recall — Mitigate: verify emergency response illuminance in Sleep-Safe scene within 5 seconds
- **Dimming compatibility with legacy control systems**: Some older lighting control systems have interoperability issues with newer LED drivers — verify protocol compatibility (DALI, 0-10V, DMX) at design stage

## KPIs
- Lighting energy by area/panel (kWh/month) — target: ≥30% reduction from baseline for LED+scene control retrofit
- Lighting power density (W/m² or W/ft²) by clinical area vs ASHRAE 90.1 Table 10.6.2 limits
- Scene usage frequency: number of scene recalls per day per zone — monitor for scene abandonment
- Illuminance levels (lux) per clinical task vs design minimums per IES RP-29 and BS EN 12464
- Color rendering index (CRI) — verify ≥80 general areas, ≥90 exam/procedure areas
- Override frequency (manual scene changes vs scheduled) — target: >90% of scene events are scheduled not manual overrides
- Cooling load reduction (tons) from LED heat gain reduction — secondary benefit in cooled zones
- Maintenance cost reduction (£/year): lamp replacement costs eliminated by LED long-life

## M&V Plan
**Option B (Retrofit Isolation — Subsystem Level)** per IPMVP where panel-level submetering exists; Option C for area-level estimation

**Quantification approach:**
- Baseline: 12 months of lighting panel kWh data by area from sub-metering or estimated from wattage survey
- Post-implementation: Monitor monthly panel kWh by area; calculate kWh reduction vs baseline — normalize for occupancy variations
- Calculate secondary cooling savings: ΔkWh_cooling = (LED heat gain reduction, BTU/hr) / (COP × 3,412 BTU/kW)
- Pre/post comparison: minimum 12 months baseline to 6 months post-implementation

**Data collection:**
- Lighting panel kWh at monthly intervals by area (patient rooms, exam/treatment, nurse stations, corridors, support)
- Scene recall log: timestamp, zone, scene name, manual vs scheduled trigger
- Override event log: timestamp, zone, reason
- Spot illuminance measurements (lux) at representative task points post-installation
- Driver failure events and replacement log

## Costs & Payback (Indicative)
- **Capex**: LED luminaire replacement: £50–200 per fitting for general areas; £500–3,000 per room for exam/procedure fixtures; scene control system: £5,000–20,000; installation labor: £10,000–40,000
- **Opex**: Driver replacement (1–3% annual failure rate for critical areas); scene system maintenance: £500–2,000/year
- **Simple payback**: 5–10 years on energy alone; total ROI including maintenance reduction: 3–6 years
- **ROI**: Clinical quality improvement (CRI, flicker-free, adjustable intensity) is as important as energy savings

## Templates / Reuse
*Boilerplate footer removed. Reference CIBSE LG7 for healthcare lighting, IES RP-29 for procedure room lighting, and ASHRAE 90.1 Table 10.6.2 for LPD limits.*
