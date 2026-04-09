---
Main System: "[[Energy Recovery]]"
Category System: "[[HVAC]]"
Utility Affected: "[[Heating and Cooling]]"
Source Document: "[[AEDG50-LargeHospitals-2012.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Air-Side Heat Recovery for Large-Hospital Ventilation Streams

## Summary
Install air-side heat recovery (enthalpy recovery wheels, plate heat exchangers, or run-around coils) on large hospital exhaust streams to reduce the energy cost of conditioning high-volume outdoor air. Hospitals are especially well suited because ventilation rates are large, consistent, and required 24/7 — providing continuous recovery opportunity that most building types cannot match.

## Estimated Savings
- **CIBSE Guidance**: 20–35% of OA treatment energy in continuously ventilated hospitals (per CIBSE Guide B energy recovery data)
- **ASHRAE Guidance**: 15–30% of OA conditioning energy in high-ventilation facilities (per ASHRAE 90.1 energy recovery guidance and AEDG50-LargeHospitals)
- **End-Uses Affected**: Ventilation heating/cooling energy, reheat coil energy, fan energy (reduced thermal load on preheat coils), and boiler/chiller plant load

## Basis / References

### CIBSE References
- **Guide B** (HVAC): Air-to-air heat recovery equipment selection, effectiveness targets, and design methodology
- **CIBSE AM13** (Mixed Mode Ventilation): Recovery effectiveness and application in continuously ventilated buildings

### ASHRAE References
- **90.1** (Energy Standard): §6.5.6 for energy recovery requirements in systems with high outdoor air requirements; Table 6.5.6 for effectiveness requirements by climate
- **62.1** (Ventilation for IAQ): §6.3 for minimum outdoor air rates and heat recovery interaction with ventilation requirements
- **AEDG50-LargeHospitals-2012**: Air-Side Heat Recovery chapter element and executive summary measure for large hospitals

### Other Standards
- **AHRI 380** (Heat Recovery Equipment Rating): Certification standard for heat recovery equipment performance
- **FGI 2018 Guidelines**: Cross-contamination prevention between exhaust and supply streams in healthcare settings — recovery unit must maintain ≥25 ft separation or 100% effectiveness without air stream mixing
- **HEPA/ULPA filtration**: If exhaust contains pathogens or biological contaminants, energy recovery must use run-around coils rather than enthalpic media to prevent cross-contamination

## Assumptions
Hospitals with OA flow rates >5,000 CFM per system and continuous 24/7 operation provide the most favorable recovery economics. Minimum sensible effectiveness: ≥65%; latent effectiveness: ≥50% for enthalpy wheels. Recovery effectiveness degrades by 5–15% without regular media cleaning and drive belt maintenance. Cross-contamination risk must be assessed for exhaust streams from isolation rooms, ICU, OR, and biohazard areas. Air-side pressure drop through recovery device should not exceed 0.5 in. wg to avoid fan power penalty.

## Climate Zone Relevance
All climate zones; strongest in extreme (cold-dry, hot-humid) and mixed-humid climates where OA conditioning loads are highest and recovery utilization is maximized. In temperate climates, the annual benefit is lower but still positive due to 24/7 hospital operation. ASHRAE 90.1 §6.5.6 mandates energy recovery when outdoor air requirements and climate conditions exceed threshold criteria — verify compliance per local codes.

## Interaction Notes
Pairs with decoupled OA treatment (ECM_Decoupled_Ventilation_and_Reheat_Reduction_Large_Hospital) because recovery reduces OA pretreatment load, improving the economics of decoupled OA systems. Synergizes with pressure control and plant heat recovery strategies. Recovery does not conflict with chiller heat recovery (ECM_Heat_Recovery_Chillers_Large_Hospital) — these operate at different temperature bands and are additive. Must verify frost protection strategy when using enthalpy wheels in cold climates (outdoor air ≤30°F): preheat or purge cycle required to prevent frost formation on recovery media.

## Implementation Essentials
- **Technology selection**: Enthalpy wheels preferred for hospitals with controlled exhaust streams (non-contaminated general exhaust); run-around coils required for exhaust from isolation rooms, OR, ICU, or biohazard areas; plate HX for low-contamination general exhaust
- **Cross-contamination review**: Map all exhaust streams; any exhaust from isolation, OR, or biohazard zones requires run-around coil configuration — enthalpy wheels not permitted in these streams per FGI 2018 and ASHRAE 170
- **Effectiveness targets**: Sensible effectiveness ≥65%; latent effectiveness ≥50% for enthalpy wheels; plate HX sensible effectiveness 60–75%
- **Minimum separation distance**: Supply and exhaust intakes must maintain ≥25 ft separation or equivalent to prevent re-entrainment of exhaust air — verify per ASHRAE 62.1 and FGI 2018 requirements
- **Frost protection (enthalpy wheels)**: Configure outdoor air preheat coil or wheel purge cycle for conditions when outdoor air ≤30°F — frost on media reduces effectiveness by >50%
- **Pressure drop verification**: Verify total external static pressure at design flow includes recovery device pressure drop; adjust fan sizing if >0.5 in. wg
- **Commissioning**: Test recovery effectiveness at 25%, 50%, 75%, 100% flow; verify cross-contamination separation; document performance at design conditions
- **Trend monitoring**: Track supply air temperature, exhaust air temperature, wheel speed (enthalpy), and preheat coil operation

## Risks / Constraints
- **Clinical contamination concerns limit technology choice**: Exhaust from isolation, OR, ICU, and biohazard areas must use run-around coils — enthalpy wheels are not permitted for these streams. Mitigate by mapping exhaust streams at design stage and specifying run-around coils for all high-risk zones
- **Pressure drop from recovery device increases fan energy**: If not accounted for in fan selection, net savings from recovery may be partially offset by higher fan power — specify low-pressure-drop device (≤0.3 in. wg) or adjust fan motor size
- **Media fouling degrades effectiveness without maintenance**: Establish quarterly media cleaning schedule and belt tension check (enthalpy wheels) — fouling can reduce effectiveness by 15–25% within 12 months
- **Cross-contamination from exhaust re-entrainment**: Maintain ≥25 ft separation between supply and exhaust intakes; consult ASHRAE 62.1 and FGI 2018 for specific separation requirements by exhaust type
- **Frost formation on enthalpy wheels**: Wheel purge cycle or preheat coil is mandatory in climates with sustained outdoor air <30°F; verify winter commissioning performance

## KPIs
- Recovery effectiveness — sensible (target: ≥65%) and latent (target: ≥50%) by season
- OA treatment energy (kBtu/month): heating and cooling energy for outdoor air pre-treatment
- Supply air temperature and humidity vs design conditions (°F and %RH)
- Wheel speed and power consumption (enthalpy wheels — target: >95% uptime)
- Frost purge cycle frequency and duration (hours/year in cold weather)
- Pressure drop across recovery device (in. wg — verify ≤0.5 in. wg at design flow)
- Cross-contamination incidents: any documented supply air quality excursions traced to exhaust re-entrainment
- Maintenance compliance: quarterly media cleaning and belt inspection completion rate

## M&V Plan
**Option B (Retrofit Isolation — Subsystem Level)** per IPMVP

**Quantification approach:**
- Baseline: 12 months of OA treatment energy = heating + cooling coil energy for outdoor air pretreatment (can be estimated from preheat coil kW and reheat kBtu if direct metering is unavailable)
- Post-implementation: Monitor supply air temperature, exhaust air temperature, wheel speed, and OA flow rate; calculate recovered energy using effectiveness curves and ASHRAE heat transfer equations
- Calculate avoided OA conditioning energy = Post OA coil load − Pre OA coil load (weather-normalized using HDD/CDD)
- Apply fan power correction if recovery device pressure drop changes fan power consumption
- Normalize for occupancy and clinical schedule changes; verify data capture rate ≥95%

**Data collection:**
- Supply air temperature and humidity (°F, %RH) at 15-minute intervals
- Exhaust air temperature and humidity (°F, %RH) at 15-minute intervals
- Outdoor air temperature and humidity (°F, %RH) for weather correlation
- Recovery device pressure drop (in. wg) at design flow post-commissioning
- Preheat coil energy (kW or BTU/hr) for OA temperature maintenance (enthalpy wheel purge mode)
- Fan motor power (kW) pre/post at equivalent flow rates — for net savings calculation
- Outside air flow rate (CFM) — verify design flow maintained

## Costs & Payback (Indicative)
- **Capex**: Enthalpy wheel or plate HX unit: £15,000–60,000 per OA system (size dependent); ductwork modifications and controls integration: £5,000–20,000; commissioning: £3,000–10,000
- **Opex**: Quarterly media cleaning and belt maintenance: £500–1,500/year; annual effectiveness verification: £500–1,000/year
- **Simple payback**: 5–10 years in hospitals with continuous high OA flows (>5,000 CFM/system) and >4,000 annual operating hours
- **ROI**: Long-life strategic measure; high utilization due to 24/7 hospital operation makes this viable where office buildings would be marginal

## Templates / Reuse
*Boilerplate footer removed. Reference ASHRAE 90.1 §6.5.6 for energy recovery requirements and CIBSE Guide B for equipment design guidance.*
