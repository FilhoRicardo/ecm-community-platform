---
Main System: "[[Condensers]]"
Category System: "[[Refrigeration]]"
Utility Affected: "[[Electricity]]"
Source Document: "[[AEDG50-GroceryStores-2015.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Condenser Selection and Floating Head Pressure Optimization

## Summary
Optimize condenser type and control so the refrigeration system avoids unnecessarily high condensing pressure and fan energy. Floating head pressure control — reducing condensing pressure during cooler outdoor conditions — is one of the highest-ROI refrigeration controls measures available in grocery stores because refrigeration plant runs continuously and ambient temperature varies significantly day-to-day and season-to-season.

## Estimated Savings
- **CIBSE Guidance**: 5–15% reduction in refrigeration plant electricity through floating head pressure control (per CIBSE Guide B HVAC plant optimization data)
- **ASHRAE Guidance**: 3–10% of total refrigeration energy through optimized head pressure control (per ASHRAE Handbook Refrigeration and AEDG50-GroceryStores)
- **End-Uses Affected**: Compressor energy, condenser fan energy, and refrigeration system COP

## Basis / References

### CIBSE References
- **Guide B** (HVAC): Condenser selection, head pressure control, and climate-sensitive air vs evaporative condensing decisions
- **CIBSE TM39** (Building Energy Metering): Refrigeration system energy disaggregation and performance monitoring

### ASHRAE References
- **90.1** (Energy Standard): §6.7 for refrigeration equipment efficiency and control requirements
- **Handbook — Refrigeration**: Chapter 11 — Condenser Types and Selection for commercial refrigeration
- **AEDG50-GroceryStores-2015**: Condenser selection and head pressure control as core grocery refrigeration ECM

### Other Standards
- **AHRI 550/590**: Heat recovery chiller performance rating (for heat recovery integration)
- **DOE/ENERGY STAR**: Commercial refrigeration condenser best practices and efficiency standards

## Assumptions
Baseline condensing pressure is held at unnecessarily high setpoint (typically 200–250 psig for air-cooled R-404A systems) due to conservative "safety" setpoints. Floating head pressure control allows condensing pressure to float with ambient temperature, typically reducing setpoint from 250 psig to 150–180 psig in mild weather (outdoor air ≤65°F). Target condensing temperature: 15–20°F above outdoor air dry-bulb temperature. Fan staging control: fans cycle on/off in stages rather than running continuously. Evaporative condensing efficiency (if applicable): 25–35% more efficient than air-cooled but requires water treatment and maintenance.

## Climate Zone Relevance
All climate zones; floating head pressure is most valuable where outdoor temperature varies significantly (diurnal swing ≥20°F) — temperate and cold climates benefit most. In hot climates (CZ 1–2), ambient temperature rarely drops below 65°F, limiting floating head potential. In cold climates (CZ 5–8), winter head pressure can drop too low, requiring minimum head pressure control to maintain adequate system performance. ASHRAE 90.1 §6.7 specifies minimum head pressure controls requirements — verify compliance.

## Interaction Notes
Pairs with ECM_Refrigeration_Controls_and_Superheat_Optimization_Grocery for integrated system optimization. Synergizes with ECM_Condenser_and_Head_Pressure_Optimization_Grocery (same ECM — this is a cross-reference). Complements ECM_Refrigerant_Heat_Recovery_Grocery when heat recovery is active. Does not conflict with any other refrigeration or HVAC measure. Fan staging from floating head control reduces fan energy but must be coordinated with compressor staging logic to prevent short-cycling.

## Implementation Essentials
- **Condenser survey**: Identify condenser type (air-cooled, evaporative, water-cooled); assess current head pressure setpoint, fan staging, and control logic
- **Floating head pressure configuration**: Set head pressure setpoint curve: 250 psig at outdoor air ≥85°F; 200 psig at 65°F; 150 psig at ≤45°F (interpolate between points); minimum head pressure protection: 130 psig
- **Fan staging logic**: Configure 2-speed or variable-speed fans where available; fan staging: Stage 1 on at 200 psig, Stage 2 on at 225 psig, all-off below 130 psig minimum
- **Subcooling verification**: If system includes subcooler, verify subcooling temperature targets are maintained during low-head-pressure operation
- **Compressor staging coordination**: Verify compressor unloading capability prevents short-cycling when head pressure drops rapidly during cooler nighttime conditions
- **Trend monitoring**: Install condensing pressure transducer and outdoor air temperature sensor; track head pressure vs ambient continuously via BMS or refrigeration controller
- **Commissioning**: Verify head pressure at 3 outdoor temperature bands (hot, mild, cool); confirm no nuisance compressor shutdowns at minimum head pressure

## Risks / Constraints
- **Water quality/maintenance weakens evaporative options**: Evaporative condensers require regular water treatment and basin cleaning; scale buildup can reduce heat transfer efficiency by 15–20% — mitigate by specifying water treatment system and establishing quarterly maintenance schedule
- **Conservative pressure setpoints are often kept unnecessarily high "for safety"**: This is the most common implementation barrier — the "safety margin" of 20–40 psig above necessary is typical; address through operator education and documented performance testing showing no adverse effects
- **Minimum head pressure protection is critical**: Too-low head pressure causes compressor flooding and damage; configure fail-safe minimum head pressure cutout at 115–120 psig; verify minimum head pressure at commissioning for winter conditions
- **Hot gas bypass valve wear**: If hot gas bypass is used to maintain minimum head pressure, valve wear increases — track hot gas bypass runtime as an indicator of valve health
- **Ambient temperature sensor placement**: If sensor is in direct sun or near condenser discharge air, readings are artificially high, causing excessive head pressure — position sensor in well-ventilated area away from heat sources

## KPIs
- Condensing pressure (psig) vs outdoor air temperature (°F) — verify floating setpoint curve is followed
- Compressor energy (kWh/month) — normalize for ambient temperature using regression model
- Condenser fan energy (kWh/month) — verify fan staging is active (not constant-on)
- Refrigeration system COP (ratio of case cooling capacity to compressor energy input) — target: ≥3.0 at design conditions; ≥2.0 at part-load
- Head pressure deviation from setpoint (% of operating hours within ±5 psig of setpoint) — target: ≥95%
- Hot gas bypass runtime (hours/month) — indicator of winter control stability
- Water consumption (gallons/month) for evaporative condensers — monitor for abnormal consumption indicating scale buildup

## M&V Plan
**Option B (Retrofit Isolation — Refrigeration Plant Level)** per IPMVP

**Quantification approach:**
- Baseline: 12 months of refrigeration plant energy (compressor + condenser fans, kWh) and condensing pressure setpoint
- Post-implementation: Monthly plant energy; track condensing pressure vs outdoor temperature; calculate plant energy reduction vs ambient-normalized baseline
- Weather normalization: regress plant energy against outdoor temperature (°F) using baseline data; apply same regression to post-data to calculate weather-normalized savings
- Calculate avoided fan energy from fan staging vs constant-on; calculate compressor efficiency improvement from reduced head pressure
- Pre/post comparison: minimum 12 months baseline to 6 months post-implementation

**Data collection:**
- Refrigeration plant total energy (kWh/month) — compressor and condenser fans combined
- Condensing pressure (psig) at 15-minute intervals
- Outdoor air temperature (°F) at 15-minute intervals
- Compressor runtime hours and stages (for load profiling)
- Condenser fan runtime hours and stages (if staged control implemented)
- Hot gas bypass runtime hours (if applicable)
- Subcooling temperature (°F) if subcooler present
- Water consumption (gallons) for evaporative condensers

## Costs & Payback (Indicative)
- **Capex**: Head pressure transducer and controller integration (if not in existing refrigeration controller): £500–2,000; condenser fan staging controls: £1,000–4,000; BMS integration and trend logging: £500–2,000; commissioning: £500–1,500
- **Opex**: Quarterly head pressure setpoint review and seasonal adjustment: £200–500/year
- **Simple payback**: <1 year in most stores — this is a pure controls measure with minimal capex; often pays back in 2–6 months in temperate climates with significant diurnal temperature swing
- **ROI**: Extremely high; highest ROI per unit effort of any refrigeration controls measure

## Templates / Reuse
*Boilerplate footer removed. Reference ASHRAE Handbook Refrigeration Chapter 11 and CIBSE Guide B for condenser optimization guidance.*
