---
Main System: "[[DOAS]]"
Category System: "[[Ventilation]]"
Utility Affected: "[[Heating and Cooling]]"
Source Document: "[[AEDG30-SmallHealthcare-2009.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Dedicated Outdoor Air with Exhaust-Air Energy Recovery

## Summary
Use dedicated outdoor-air treatment with sensible or total energy recovery so healthcare ventilation loads are reduced without compromising air-change and IAQ requirements. Small healthcare facilities have high ventilation requirements relative to their size, and the ventilation load is a dominant fraction of total HVAC energy — making DOAS with energy recovery one of the highest-impact ECMs available for small healthcare.

## Estimated Savings
- **CIBSE Guidance**: 20–35% of OA treatment energy through energy recovery in continuously ventilated small healthcare facilities (per CIBSE Guide B DOAS data)
- **ASHRAE Guidance**: 15–30% reduction in outdoor-air heating/cooling burden where exhaust streams and code allow (per ASHRAE 90.1 and AEDG30-SmallHealthcare)
- **End-Uses Affected**: Ventilation heating, cooling, reheat, and fan energy

## Basis / References

### CIBSE References
- **Guide B** (HVAC): DOAS system design, energy recovery equipment selection, and decoupled OA treatment methodology
- **CIBSE AM13** (Mixed Mode Ventilation): Energy recovery effectiveness and application in healthcare buildings

### ASHRAE References
- **90.1** (Energy Standard): §6.5.6 for energy recovery requirements when outdoor air requirements and climate conditions exceed threshold criteria
- **62.1** (Ventilation for IAQ): §6.2 for minimum outdoor air rates and heat recovery interaction with ventilation requirements
- **ASHRAE 170** (Ventilation for Healthcare Facilities): Table 7-1 for minimum OA by clinical function
- **AEDG30-SmallHealthcare-2009**: DOAS with energy recovery as a high-value HVAC package measure for small healthcare facilities

### Other Standards
- **AHRI 380**: Heat recovery equipment certification standard
- **FGI 2018 Guidelines**: Cross-contamination prevention between exhaust and supply streams; recovery unit must maintain separation per ASHRAE 170
- **HEPA/ULPA filtration**: If exhaust contains pathogens, energy recovery must use run-around coils rather than enthalpic media to prevent cross-contamination

## Assumptions
Small healthcare facilities with OA flow rates >1,000 CFM per system and continuous operation provide favorable recovery economics. Minimum sensible effectiveness: ≥65%; latent effectiveness: ≥50% for enthalpy wheels. Cross-contamination risk assessment required for exhaust streams from procedure rooms, exam rooms, and isolation areas. Recovery device pressure drop should not exceed 0.5 in. wg to avoid fan power penalty.

## Climate Zone Relevance
All climate zones, especially humid and extreme climates where OA treatment energy is highest. ASHRAE 90.1 §6.5.6 mandates energy recovery when outdoor air requirements and climate conditions exceed threshold criteria — verify compliance. Cold-dry climates benefit from sensible recovery; hot-humid climates benefit from enthalpy recovery. Temperate climates may have marginal economics depending on OA flow rates.

## Interaction Notes
Pairs strongly with fan-coil units, WSHP systems, and condenser heat recovery. DOAS separates OA treatment from zone sensible loads, enabling independent optimization of each. Synergizes with ECM_Classify_Critical_vs_Noncritical_Areas_Small_Healthcare: accurate classification determines which zones need decoupled OA. Complements ECM_Condenser_Heat_Recovery_Small_Healthcare when heat recovery is the sink for recovered OA energy. Does not conflict with any other ECM.

## Implementation Essentials
- **Exhaust stream assessment**: Map all exhaust streams; assess contamination risk for each — procedure rooms, exam rooms, isolation rooms require run-around coils (enthalpy wheels not permitted per FGI 2018); general exhaust can use enthalpy wheels
- **Technology selection**: Enthalpy wheels for non-contaminated general exhaust; run-around coils for exhaust from clinical zones; plate HX as alternative for low-contamination streams
- **Effectiveness targets**: Sensible effectiveness ≥65%; latent effectiveness ≥50% for enthalpy wheels; plate HX sensible effectiveness 60–75%
- **Minimum separation distance**: Supply and exhaust intakes must maintain ≥25 ft separation or equivalent to prevent re-entrainment per ASHRAE 62.1 and FGI 2018
- **Frost protection (enthalpy wheels)**: Configure outdoor air preheat coil or wheel purge cycle for conditions when outdoor air ≤30°F; frost on media reduces effectiveness by >50%
- **Bypass and humidity control**: Configure summer/winter bypass mode for energy recovery units; integrate with DOAS humidification/dehumidification control
- **Pressure drop verification**: Verify total external static pressure at design flow includes recovery device pressure drop; adjust fan sizing if >0.5 in. wg
- **Commissioning**: Test recovery effectiveness at 25%, 50%, 75%, 100% flow; verify cross-contamination separation; document performance at design conditions

## Risks / Constraints
- **Clinical contamination concerns limit technology choice**: Exhaust from procedure, exam, and isolation rooms requires run-around coils — Mitigate by mapping exhaust streams at design stage and specifying run-around coils for all clinical zones
- **Pressure drop increases fan energy**: If recovery device pressure drop is not accounted for in fan selection, net savings may be partially offset by higher fan power — specify low-pressure-drop device or adjust fan motor size
- **Media fouling degrades effectiveness**: Establish quarterly media cleaning and belt tension schedule (enthalpy wheels) — fouling can reduce effectiveness by 15–25% within 12 months
- **Cross-contamination from exhaust re-entrainment**: Maintain ≥25 ft separation between supply and exhaust intakes; consult ASHRAE 62.1 and FGI 2018 for separation requirements by exhaust type
- **Frost formation on enthalpy wheels**: Wheel purge cycle or preheat coil is mandatory in cold climates; verify winter commissioning performance

## KPIs
- Recovery effectiveness — sensible (target: ≥65%) and latent (target: ≥50%) by season
- OA treatment energy (kBtu/month): heating and cooling energy for outdoor air pretreatment
- Supply air temperature and humidity vs design conditions (°F and %RH)
- Wheel speed and power consumption (enthalpy wheels — target: >95% uptime)
- Frost purge cycle frequency and duration (hours/year in cold weather)
- Pressure drop across recovery device (in. wg — verify ≤0.5 in. wg at design flow)
- Cross-contamination incidents: any documented supply air quality excursions traced to exhaust re-entrainment
- Maintenance compliance: quarterly media cleaning and belt inspection completion rate

## M&V Plan
**Option B (Retrofit Isolation — Subsystem Level)** per IPMVP

**Quantification approach:**
- Baseline: 12 months of OA treatment energy = heating + cooling coil energy for outdoor air pretreatment
- Post-implementation: Monitor supply/exhaust temperatures, wheel speed, and OA flow rate; calculate recovered energy using effectiveness curves
- Calculate avoided OA conditioning energy = Post OA coil load − Pre OA coil load (weather-normalized using HDD/CDD)
- Apply fan power correction if recovery device pressure drop changes fan power consumption
- Pre/post comparison: minimum 12 months baseline to 6 months post-implementation

**Data collection:**
- Supply air temperature and humidity (°F, %RH) at 15-minute intervals
- Exhaust air temperature and humidity (°F, %RH) at 15-minute intervals
- Outdoor air temperature and humidity (°F, %RH) for weather correlation
- Recovery device pressure drop (in. wg) at design flow post-commissioning
- Preheat coil energy (kW) for OA temperature maintenance
- Fan motor power (kW) pre/post at equivalent flow rates
- Outside air flow rate (CFM) — verify design flow maintained

## Costs & Payback (Indicative)
- **Capex**: Enthalpy wheel or plate HX unit: £10,000–40,000 per OA system; ductwork modifications and controls: £5,000–15,000; commissioning: £3,000–8,000
- **Opex**: Quarterly media cleaning and belt maintenance: £500–1,500/year; annual effectiveness verification: £500–1,000/year
- **Simple payback**: 4–8 years in small healthcare facilities with continuous high OA flows (>1,000 CFM/system) and >4,000 annual operating hours
- **ROI**: High utilization due to continuous operation makes this viable where office buildings would be marginal

## Templates / Reuse
*Boilerplate footer removed. Reference ASHRAE 90.1 §6.5.6 and CIBSE Guide B for energy recovery design guidance.*
