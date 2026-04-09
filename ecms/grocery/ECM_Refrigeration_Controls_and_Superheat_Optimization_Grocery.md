---
Main System: "[[Refrigeration Controls]]"
Category System: "[[Refrigeration]]"
Utility Affected: "[[Electricity]]"
Source Document: "[[AEDG50-GroceryStores-2015.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Refrigeration Controls, EEVs, and Superheat Optimization

## Summary
Improve refrigeration system efficiency through better control logic, electronic expansion valves (EEVs), and tuned superheat rather than relying only on hardware nameplate upgrades. The majority of savings from refrigeration optimization come from controls tuning that costs far less than compressor replacement. EEVs and superheat optimization are the core measures; compressor staging and condenser control are companion measures that amplify the benefit.

## Estimated Savings
- **CIBSE Guidance**: 8–15% reduction in refrigeration electricity through EEV conversion and superheat optimization (per CIBSE Guide B commercial refrigeration efficiency data)
- **ASHRAE Guidance**: 5–12% of refrigeration energy through superheat optimization and EEV control (per ASHRAE Handbook Refrigeration and AEDG50-GroceryStores)
- **End-Uses Affected**: Refrigeration electricity (compressor and case energy), refrigeration system stability, and maintenance costs

## Basis / References

### CIBSE References
- **Guide B** (HVAC): Refrigeration control systems, EEV technology, and superheat optimization methodology
- **CIBSE TM39** (Building Energy Metering): Refrigeration system energy disaggregation and performance monitoring

### ASHRAE References
- **Handbook — Refrigeration**: Chapter 11 — Refrigeration Controls and EEV technology; Chapter 9 — Compressors and capacity control
- **90.1** (Energy Standard): §6.7 for refrigeration equipment performance and control requirements
- **AEDG50-GroceryStores-2015**: Controls-based refrigeration optimization as core grocery ECM

### Other Standards
- **AHRI 1200** (Refrigerated Display Case Performance): Case performance standards and superheat requirements
- **ARI 540** (Positive Displacement Compressors): Compressor efficiency and capacity control

## Assumptions
Baseline systems use thermostatic expansion valves (TXVs) or single-step electronic valves with fixed setpoints and no adaptive superheat control. Target superheat: 8–12°F for medium-temperature cases (33–41°F); 6–10°F for low-temperature cases (≤0°F). EEV performance requirement: modulating control 0–100%, response time <1 second, superheat control accuracy ±1°F. Compressor staging: minimum 3 stages of unloading for systems >15 tons; variable-speed compressor drive (VSD) for systems >25 tons. Control system must support: suction pressure optimization, EEV remote monitoring, and alarm logging.

## Climate Zone Relevance
All climate zones; refrigeration control quality is universally important. Most impactful in stores with high thermal load (hot-humid climates) and inconsistent superheat control where adaptive EEV control provides the largest improvement over fixed TXVs. In cold climates, suction pressure optimization is most valuable because lower ambient temperatures cause wider suction pressure variation.

## Interaction Notes
Pairs with ECM_Condenser_and_Head_Pressure_Optimization_Grocery: improved suction pressure control complements head pressure optimization by allowing lower suction pressure without compromising case temperatures. Complements ECM_Case_Doors_and_HVAC_Rebalance_Grocery: case doors reduce case load, enabling lower suction pressure; EEV control must be re-tuned post-door installation to capture the new load profile. Synergizes with ECM_Refrigerant_Heat_Recovery_Grocery when heat recovery raises condensing pressure — EEV control must compensate to maintain stable superheat. Does not conflict with any other ECM; amplifies savings from all refrigeration measures.

## Implementation Essentials
- **Superheat baseline mapping**: Use case controller data or handheld sensors to map superheat by case circuit during 48-hour baseline period; identify circuits with excessive superheat (>15°F) or unstable superheat (variation >5°F/hour)
- **EEV installation**: Replace fixed TXVs with modulating EEVs on all circuits with superheat variability >3°F; prioritize highest-load circuits first
- **Superheat tuning by circuit type**: Medium-temp (produce, dairy): target 10°F; low-temp (frozen): target 8°F; verify stable control across ambient temperature range 50–95°F outdoor
- **Suction pressure optimization**: Configure suction pressure setpoint to float with outdoor temperature — lower setpoint when ambient is low and case load is low; target: 55–65 psig for R-404A medium-temp suction at outdoor ≤75°F
- **Compressor staging optimization**: Verify compressor lead-lag staging responds to suction pressure without hunting; minimum 3 stages for systems >15 tons; configure VSD to modulate rather than cycle on/off
- **Alarm and fault logic review**: Configure alarms for: superheat out of range (<5°F or >15°F), suction pressure deviation >10% from setpoint, and EEV fault conditions
- **Data logging and trend review**: Implement 15-minute logging of suction pressure, superheat by circuit, EEV positions, and compressor stages — review weekly for first 4 weeks post-commissioning
- **Commissioning**: Test EEV response to step changes in case load; verify stable superheat control under夜间低温 and daytime peak conditions; document control parameters and transfer to O&M

## Risks / Constraints
- **Service staff capability is the primary constraint**: EEVs and adaptive superheat control require service staff trained in digital control systems — if service staff are not capable, the EEV system will be set to manual mode and savings lost. Mitigate: require vendor training for service staff before procurement; specify vendor support contract
- **Over-aggressive suction pressure reduction causes case temperature drift**: Too-low suction pressure reduces case evaporator能力的 and can cause product temperature rise — mitigate by setting conservative initial suction setpoints and adjusting based on case temperature monitoring for first 4 weeks
- **EEV hunting from too-low gain settings**: If EEV PID gain is set too high, valve oscillates and superheat oscillates — mitigate by starting with conservative gain settings and increasing only after stable operation is confirmed for 48 hours
- **Legacy controller interoperability**: Some older refrigeration controllers cannot interface with new EEV systems — verify protocol compatibility (ECOBUS, RS-485, Modbus) at procurement stage
- **Fouling reduces heat exchanger performance over time**: Evaporator fouling changes superheat response; schedule quarterly superheat verification to detect fouling early

## KPIs
- Superheat by circuit (°F) — maintain 8–12°F medium-temp, 6–10°F low-temp; target: ≥95% of operating hours within ±2°F of setpoint
- Suction pressure stability (psig) — target: ±3 psig of setpoint at all times; no sustained hunting
- EEV position stability (% open) — target: <10% variation per hour in stable conditions (no load changes)
- Compressor energy (kWh/month) — normalize for ambient temperature; target: ≥8% reduction from baseline with EEV + superheat optimization
- Case temperature compliance (°F) vs AHRI 1200 — verify no temperature drift >2°F from baseline after control optimization
- Alarm frequency (count/month) — target: <5 unresolved alarms per month per system
- VSD compressor energy reduction (%) vs fixed-speed operation at equivalent load — target: ≥15% reduction at 50% load

## M&V Plan
**Option B (Retrofit Isolation — Refrigeration System Level)** per IPMVP where case-level or system-level submetering exists

**Quantification approach:**
- Baseline: 12 months of refrigeration system energy (kWh) from case controller logs or system metering; baseline superheat mapping (48-hour characterization study)
- Post-implementation: Monthly refrigeration energy; weekly superheat and suction pressure trend review for first 8 weeks; ongoing monthly review
- Weather normalization: regress refrigeration energy against outdoor temperature (°F) using baseline data; apply same regression to post-data for weather-normalized savings
- Calculate avoided compressor energy: baseline compressor kWh at equivalent load − post compressor kWh at equivalent load
- Pre/post comparison: minimum 12 months baseline to 6 months post-implementation

**Data collection:**
- Refrigeration system energy (kWh/month) from case controller or system meter
- Superheat (°F) by circuit at 15-minute intervals
- Suction pressure (psig) at 15-minute intervals
- EEV position (% open) by circuit at 15-minute intervals
- Compressor runtime hours and stages at 15-minute intervals
- Case temperatures (°F) by circuit at 15-minute intervals
- Outdoor air temperature (°F) at 15-minute intervals for weather normalization
- Alarm log: unresolved faults, fault type, duration, resolution

## Costs & Payback (Indicative)
- **Capex**: EEV replacement per circuit: £200–600 per circuit; control system integration and BMS gateway: £3,000–12,000; commissioning (per system): £1,500–4,000; suction pressure transducer addition: £500–1,500 per system
- **Opex**: Quarterly superheat verification and EEV maintenance: £500–1,500/year; annual controller firmware updates: £200–500/year
- **Simple payback**: 2–4 years for controls-only retrofits; <2 years when baseline superheat is significantly mis-tuned (>15°F)
- **ROI**: High — EEV and superheat control savings are persistent and compounding; each year of mis-tuned superheat costs more than annual EEV maintenance

## Templates / Reuse
*Boilerplate footer removed. Reference ASHRAE Handbook Refrigeration Chapter 11 and CIBSE Guide B for refrigeration controls guidance.*
