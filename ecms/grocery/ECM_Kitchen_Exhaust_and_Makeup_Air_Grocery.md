---
Main System: "[[Kitchen Exhaust]]"
Category System: "[[Interaction Between Systems]]"
Utility Affected: "[[Heating and Cooling]]"
Source Document: "[[AEDG50-GroceryStores-2015.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Kitchen Exhaust and Makeup Air Integration

## Summary
Integrate kitchen exhaust, makeup air, and store pressurization so prepared-food operations do not pull humid air through the building envelope or create unnecessary HVAC penalties. Uncontrolled kitchen exhaust without coordinated makeup air is one of the most common sources of store pressure imbalance, humidity control failures, and HVAC energy waste in grocery stores with active prepared-food operations.

## Estimated Savings
- **CIBSE Guidance**: 15–30% reduction in kitchen exhaust fan energy and 10–20% improvement in store latent control through optimized makeup air integration (per CIBSE Guide B kitchen ventilation data)
- **ASHRAE Guidance**: 10–25% of store HVAC energy in kitchens with significant exhaust when makeup air is properly managed (per ASHRAE 90.1 and AEDG50-GroceryStores)
- **End-Uses Affected**: Kitchen exhaust fan energy, makeup-air conditioning energy (heating and cooling), store latent load, and store pressurization

## Basis / References

### CIBSE References
- **Guide B** (HVAC): Kitchen ventilation design, exhaust/makeup air balancing, and heat recovery for kitchen exhaust
- **CIBSE AM10** (Commissioning Management): Kitchen ventilation commissioning and ongoing balancing verification

### ASHRAE References
- **90.1** (Energy Standard): §6.4 for kitchen ventilation requirements, exhaust flow standards, and makeup air control
- **62.1** (Ventilation for IAQ): §6.3 for minimum outdoor air requirements and demand-controlled kitchen ventilation
- **AEDG50-GroceryStores-2015**: Kitchen/HVAC interaction and makeup-air balance as a critical ECM in the grocery guide

### Other Standards
- **UL 710** (Exhaust Equipment): Kitchen exhaust hood certification and performance standards
- **NFPA 96** (Ventilation Control and Fire Protection): Kitchen exhaust system fire safety and control requirements
- **ANSI/AMCA 210** (Fan Testing): Kitchen exhaust fan performance and testing standards

## Assumptions
Baseline system: uncontrolled kitchen exhaust fans running at constant speed during prep hours, with no dedicated makeup air system, causing store infiltration through building envelope cracks. Target exhaust flow: match cooking appliance BTU input (cfm per 1,000 BTU/hr of cooking load). Target makeup air temperature: 60–65°F supply in heating season; ≤72°F supply in cooling season (dew point ≤55°F). Kitchen DCV (demand-controlled ventilation): VAV kitchen hood exhaust with cooking-load-dependent flow reduction when no cooking is active. Kitchen-to-store pressure separation: kitchen negative pressure ≤0.015 in. WC relative to sales floor.

## Climate Zone Relevance
All climate zones, especially hot-humid and mixed-humid climates where kitchen steam and humidity are most problematic. Hot-dry climates benefit from evaporative makeup air cooling. Cold climates require makeup air heating but humidity is less of an issue; focus on efficient heating of makeup air. The exhaust integration principle is universal; the specific energy impact depends on kitchen size and cooking intensity.

## Interaction Notes
Pairs with ECM_Grocery_Humidity_Control_and_Positive_Pressure: kitchen exhaust control is one of the largest latent load management opportunities — fixing kitchen exhaust integration directly reduces store humidity control burden. Complements ECM_Case_Doors_and_HVAC_Rebalance_Grocery: case doors and kitchen exhaust control together can reduce store HVAC latent capacity requirements by 20–30%. Synergizes with ECM_Refrigerant_Heat_Recovery_Grocery when kitchen loads are substantial (heat recovery from refrigeration canPreheat makeup air in winter). Works with ECM_DHW_Central_Plant_Optimization_Lodging from lodging ECM library when kitchen has large DHW loads. Does not conflict with any other ECM.

## Implementation Essentials
- **Exhaust characterization**: Measure exhaust flow rate (CFM) and temperature/humidity by cooking zone over 1-week baseline; correlate exhaust flow with cooking activity (stovetop, ovens, fryers) — size makeup air system to match peak exhaust at 90% (not 100%) to maintain slight negative pressure in kitchen
- **Demand-controlled kitchen ventilation (DCV)**: Install cooking activity sensors (heat sensors, smoke detectors, or hood temperature sensors) on kitchen hoods; configure VAV hood exhaust to reduce flow to 30–50% when no cooking is detected — target reduction: ≥40% exhaust flow during non-cooking hours
- **Makeup air temperature control**: Install makeup air unit with heating and cooling coils sized for makeup air temperature targets (60–65°F heating; ≤72°F with dew point ≤55°F cooling); integrate with store BAS for coordinated control
- **Pressure separation**: Maintain kitchen area at negative pressure relative to sales floor (≤0.015 in. WC) so kitchen humidity does not migrate to store; install pressure differential sensor between kitchen and store
- **Transfer air coordination**: Configure transfer air from store to kitchen where makeup air <100% of exhaust — reduces net HVAC load but requires store pressure management; coordinate with ECM_Grocery_Humidity_Control_and_Positive_Pressure for store pressurization
- **Kitchen hood runtime optimization**: Configure hood exhaust to operate at minimum speed during preheat and shutdown periods (30 minutes before/after cooking hours); integrate with store opening/closing schedule
- **Commissioning**: Test DCV response: verify exhaust flow reduction within 5 minutes of cooking cessation; test makeup air temperature control across outdoor temperature range; verify kitchen pressure separation

## Risks / Constraints
- **Makeup air design errors can create humidity problems at store front**: If makeup air is unconditioned or inadequately filtered, outdoor humidity is introduced directly into store — mitigate by specifying makeup air with latent coils and filtration for hot-humid climates
- **Kitchen staff may bypass DCV controls if comfort suffers**: If kitchen staff feel the hood is "too slow to respond," they override DCV to full speed — mitigate by providing override for cleaning/prep periods (documented and logged) and ensuring DCV response time is <5 minutes
- **NFPA 96 compliance constraints on DCV**: Fire suppression system interlocks must be maintained; DCV systems must not reduce exhaust below minimum required for fire suppression — coordinate with fire protection engineer at design stage
- **Grease accumulation in ducts from low-speed operation**: Reduced exhaust flow during DCV mode can cause grease accumulation in ductwork — Mitigate: configure minimum exhaust during DCV mode at ≥40% of full flow and schedule quarterly duct cleaning
- **Makeup air and store pressurization conflict**: If makeup air is supplied from store air (transfer air), store pressurization can be affected — Mitigate by providing dedicated outdoor makeup air and monitoring store pressure per ECM_Grocery_Humidity_Control_and_Positive_Pressure

## KPIs
- Kitchen exhaust flow rate (CFM) during cooking vs non-cooking hours — target: ≥40% reduction in exhaust flow during non-cooking periods with DCV active
- Kitchen makeup air flow rate (CFM) vs exhaust flow — maintain makeup air at 85–90% of exhaust for slight negative pressure
- Kitchen hood fan energy (kWh/month) — target: ≥30% reduction from baseline through DCV and runtime optimization
- Store pressure relative to kitchen (in. WC) — maintain kitchen negative ≤0.015 in. WC relative to store
- Store relative humidity (%) and dew point (°F) — maintain humidity compliance per ECM_Grocery_Humidity_Control_and_Positive_Pressure
- Makeup air supply temperature (°F) — verify 60–65°F heating season, ≤72°F cooling season
- DCV override frequency (count/month) — track kitchen staff overrides; target: <4 override events per month
- Kitchen-associated HVAC energy (kWh/month for makeup air conditioning) — measure before/after to capture secondary savings

## M&V Plan
**Option B (Retrofit Isolation — Kitchen HVAC Level)** per IPMVP where kitchen exhaust and makeup air are sub-metered

**Quantification approach:**
- Baseline: 12 months of kitchen exhaust fan energy (kWh), makeup air conditioning energy (estimated from HVAC sub-meter), and store humidity metrics
- Post-implementation: Monthly kitchen fan energy, makeup air conditioning energy, and store humidity compliance rate
- Calculate avoided fan energy: baseline kitchen fan kWh at constant speed − post kitchen fan kWh with DCV active
- Calculate avoided HVAC energy from reduced infiltration: compare store HVAC latent energy before/after kitchen pressure isolation (using store humidity as proxy)
- Normalize for seasonal variations (cooking schedules change with holidays, summer vs regular)
- Pre/post comparison: minimum 3 months baseline (same season) to 3 months post-implementation

**Data collection:**
- Kitchen exhaust fan runtime hours and speed (%) at 15-minute intervals
- Kitchen hood temperature sensors (°F) for cooking activity detection
- Makeup air flow rate (CFM) and supply temperature (°F) at 15-minute intervals
- Store relative humidity (%) and temperature (°F) at multiple locations
- Store pressure relative to outdoors and relative to kitchen (in. WC)
- Kitchen makeup air unit energy (kWh) for heating/cooling coils
- DCV override events (timestamp, duration, reason)
- Outside air temperature (°F) and humidity (%) for weather correlation

## Costs & Payback (Indicative)
- **Capex**: DCV sensors and controls upgrade: £2,000–6,000 per kitchen hood; makeup air unit (heating/cooling): £8,000–25,000; pressure sensors and BAS integration: £1,500–4,000; commissioning: £2,000–5,000
- **Opex**: Quarterly DCV sensor calibration: £300–800/year; annual duct cleaning: £500–1,500/year; grease filter replacement: £200–600/year
- **Simple payback**: 2–5 years in kitchens with significant cooking hours (>6 hours/day); shorter in stores with very high kitchen utilization
- **ROI**: Enhanced by combined humidity control savings and case door savings — kitchen exhaust control amplifies savings from ECM_Grocery_Humidity_Control_and_Positive_Pressure and ECM_Case_Doors_and_HVAC_Rebalance_Grocery

## Templates / Reuse
*Boilerplate footer removed. Reference CIBSE Guide B for kitchen ventilation and NFPA 96 for fire safety requirements.*
