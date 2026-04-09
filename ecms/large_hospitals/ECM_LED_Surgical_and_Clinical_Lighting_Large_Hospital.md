---
Main System: "[[Clinical Lighting]]"
Category System: "[[Electric Lighting]]"
Utility Affected: "[[Electricity]]"
Source Document: "[[AEDG50-LargeHospitals-2012.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: LED Surgical and Clinical Lighting Optimization

## Summary
Upgrade surgical task lighting, patient-care area lighting, and support lighting to high-efficacy LED with scene control so lighting energy, heat gain, and cooling loads fall without compromising clinical function, color rendering, or caregiver task visibility. Night-time clinical lighting scenes (emergency, observation, sleep-safe modes) are a specific energy/IAQ opportunity in hospitals that most building types do not have.

## Estimated Savings
- **CIBSE Guidance**: 30–50% reduction in clinical lighting energy through LED conversion and scene control (per CIBSE LG7 and hospital lighting retrofit case studies)
- **ASHRAE Guidance**: 25–40% lighting electricity reduction for healthcare facilities (per ASHRAE 90.1 lighting power density requirements and AEDG50-LargeHospitals)
- **End-Uses Affected**: Interior lighting electricity, secondary cooling load (reduced heat gain from LED vs conventional sources), and maintenance costs

## Basis / References

### CIBSE References
- **LG7** (Lighting Guide 7): Healthcare lighting design, task lighting requirements, and control strategies
- **TM39** (Building Energy Metering): Lighting energy analysis and submetering for healthcare facilities
- **CIBSE Guide A** (Environmental Design): Illuminance levels by clinical task and area type

### ASHRAE References
- **90.1** (Energy Standard): Table 10.6.2 for healthcare facility lighting power density limits; §10.4 for lighting controls requirements
- **AEDG50-LargeHospitals-2012**: LED surgery task lighting as a major opportunity in the large hospital guide
- **ASHRAE 55** (Thermal Comfort): Heat gain reduction from LED lighting and impact on cooling load calculations

### Other Standards
- **IES RP-29** (Lighting Hospital Operating Rooms): Surgical task lighting illuminance (≥10,000 lux at 1 meter for general surgery) and color rendering requirements (CRI ≥90 for surgical fields)
- **CIE S 017** (ILV of Lighting): International lighting vocabulary for clinical task classification
- **BS EN 12464** (Lighting of Work Places): Indoor workplace lighting requirements including healthcare
- **IEC 60598** (Luminaires Particular Requirements): LED luminaire safety standards for clinical environments

## Assumptions
Existing systems are assumed to be T8/T5 fluorescent or older LED technology with minimal scene control. Target LED efficacy: ≥130 lm/W for general lighting; ≥100 lm/W for surgical task lights. Color temperature: 4000–5000K for surgical/task lighting (clinical blue-rich for tissue differentiation); 2700–3000K for patient rooms and sleep-safe modes. CRI ≥80 for general patient areas; ≥90 for surgical and examination lighting. Driver quality: <5% total harmonic distortion (THD) at any dimming level to prevent flicker. Dimming range: 0–100% for all clinical luminaires. Control system must support scene recall in <2 seconds per scene.

## Climate Zone Relevance
All climate zones; LED heat gain reduction has a secondary cooling load benefit that is most significant in hot-humid and hot-dry climates. In heating-dominant climates, the heat gain reduction from LEDs slightly increases heating load — net energy impact of LED conversion should be assessed on a whole-building basis. However, LED conversion remains beneficial for maintenance cost reduction, controllability, and clinical quality regardless of climate.

## Interaction Notes
Pairs with daylighting only in perimeter support areas where windows permit — clinical zones (OR, ICU, procedure rooms) typically do not use daylight due to infection control and glare management requirements. Works synergistically with BAS governance (ECM_BAS_and_Operational_Persistence_Large_Hospital) to ensure clinical lighting scenes are not overridden by staff without formal change management. Complements airflow setback in procedure spaces (ECM_Airflow_Setback_in_Procedure_Spaces_Large_Hospital): lighting scene control should be integrated with HVAC setback so "sleep-safe" or "observation" lighting scenes trigger HVAC setback coordination. Reduces secondary cooling load — important in hospitals where internal gains from lighting are a significant fraction of total cooling load.

## Implementation Essentials
- **Lighting audit by clinical area**: Map luminaires by clinical function: surgical task, examination, patient ambient, corridor/wayfinding, night-safe, emergency, and support lighting — each has different performance requirements
- **Scene control architecture**: Define clinical lighting scenes by operational mode: Full Surgery (all task and ambient on), Procedure (task + general), Observation (reduced ambient), Sleep-Safe (patient room night light only <10 lux), Emergency (100% egress compliance), Housekeeping (full ambient for cleaning)
- **Surgical task lighting requirements**: Verify ≥10,000 lux at 1 meter per IES RP-29; CRI ≥90 for tissue differentiation; color temperature 4000–5000K; no UV emission; adjustable intensity 30–100%
- **Patient room requirements**: 2700–3000K for sleep-safe mode; ≤50 lux for night-safe (below waking threshold per ASHRAE 55); dimming range 0–30% for night-safe scene
- **Driver quality specification**: Specify <5% THD at all dimming levels; verify no audible noise; flicker-free at all dimming levels (per IEEE 1789)
- **Integration with HVAC setback**: Coordinate lighting scene control with HVAC setback so Sleep-Safe and Observation scenes trigger HVAC setback via BMS signal; verify HVAC responds within 5 minutes of lighting scene change
- **Commissioning with clinical staff**: Commission all scene presets with end users (surgeons, nurses, facilities); document each scene configuration and obtain clinical sign-off
- **Sub-metering**: Install lighting panel metering where feasible for M&V; separate surgical panel, patient floor panels, and support area panels

## Risks / Constraints
- **Clinical acceptance depends on visual quality, not energy metrics**: Any LED that fails to meet color rendering or illuminance requirements for clinical tasks must be replaced — do not compromise on CRI, color temperature, or flicker performance for energy savings. Mitigate: require luminaire submittals with IES LM-79 test data and clinical reference installations before bulk procurement
- **Poor usability causes permanent overrides**: If clinical staff find scene recall too complex or slow, they will override to a single static scene and lose savings. Mitigate: ensure scene recall is <2 seconds; provide physical scene control panels at room entrances (single button per scene); limit number of scenes to 4–6 per zone
- **Driver failure without BMS alarm causes darkness**: LED drivers can fail silently (no color shift or flicker) — Mitigate: integrate driver status monitoring into BMS; configure automatic alert on driver failure; stock spare drivers for critical clinical areas
- **Night-safe mode lighting levels too low for clinical response**: If a clinician needs to respond to a patient emergency, the lighting must reach ≥100 lux within 5 seconds of scene recall. Mitigate: verify emergency response lighting meets minimum clinical response illuminance (≥100 lux at 1 meter) in Sleep-Safe scene within 5 seconds
- **Dimming compatibility with older control systems**: Some legacy lighting control systems (DALI v1 vs DALI-2, DMX) have interoperability issues with newer LED drivers — Mitigate: verify protocol compatibility at design stage; specify gateway/translator if needed

## KPIs
- Lighting energy by area/panel (kWh/month) — target: ≥30% reduction from baseline for LED+scene control retrofit
- Lighting power density (W/m² or W/ft²) by clinical area vs ASHRAE 90.1 Table 10.6.2 limits
- Scene usage frequency: number of scene recalls per day per zone — monitor for scene abandonment or override events
- Illuminance levels (lux) per clinical task vs design minimums per IES RP-29 and BS EN 12464
- Color rendering index (CRI) — verify ≥80 general areas, ≥90 surgical/examination areas
- Driver status failures (count/year) — monitor for silent driver failures that compromise clinical lighting
- Override frequency (manual scene changes vs scheduled scene recalls) — target: >90% of scene events are scheduled not manual overrides
- Cooling load reduction (tons) from LED heat gain reduction in cooled zones (secondary benefit) — calculate from baseline vs post LED heat gain difference
- Maintenance cost reduction (£/year): lamp replacement costs eliminated by LED long-life

## M&V Plan
**Option B (Retrofit Isolation — Subsystem Level)** per IPMVP where panel-level submetering exists; Option C for area-level estimation where submetering is not available

**Quantification approach:**
- Baseline: 12 months of lighting panel kWh data by area (surgical, patient floors, support areas) from sub-metering or estimated from wattage survey
- Post-implementation: Monitor monthly panel kWh by area; calculate kWh reduction vs baseline — normalize for occupancy variations (patient census, OR procedure count)
- Calculate secondary cooling savings: ΔkWh_cooling = (LED heat gain reduction, BTU/hr) / (COP × 3,412 BTU/kW) — LED vs T8/T5 heat gain difference × operating hours
- Normalize for seasonal daylight changes (if applicable to perimeter zones) and clinical schedule variations
- Pre/post comparison: minimum 12 months baseline to capture seasonal variation vs 6 months post-implementation

**Data collection:**
- Lighting panel kWh at monthly intervals by area (surgical, patient floors, support, emergency, exterior)
- Scene recall log: timestamp, zone, scene name, manual vs scheduled trigger
- Override event log: timestamp, zone, reason (if captured)
- Spot illuminance measurements (lux) at representative task points post-installation (verify design minimums)
- Driver failure events and replacement log
- OR procedure count and patient census for occupancy normalization

## Costs & Payback (Indicative)
- **Capex**: LED luminaire replacement (surgical task lights: £3,000–8,000 per room; patient room and general areas: £50–150 per fitting); scene control system (BMS integration or standalone): £10,000–40,000 per floor; installation labour: £20,000–60,000; commissioning: £5,000–15,000
- **Opex**: Driver replacement (average 1–3% annual failure rate for critical areas); scene system maintenance: £1,000–3,000/year
- **Simple payback**: 5–10 years on energy alone; total ROI including maintenance reduction and clinical quality improvement: 3–6 years
- **ROI**: Clinical quality improvement (CRI, flicker-free, adjustable intensity) is as important as energy savings — clinical staff acceptance is near-100% when LED performance meets clinical requirements

## Templates / Reuse
*Boilerplate footer removed. Reference IES RP-29 for surgical lighting, CIBSE LG7 for healthcare lighting, and ASHRAE 90.1 Table 10.6.2 for lighting power density limits.*
