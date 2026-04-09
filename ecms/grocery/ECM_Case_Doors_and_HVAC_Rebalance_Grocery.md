---
Main System: "[[Refrigerated Cases]]"
Category System: "[[Refrigeration / HVAC Interaction]]"
Utility Affected: "[[Electricity and Heating/Cooling]]"
Source Document: "[[AEDG50-GroceryStores-2015.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Refrigerated Case Doors with HVAC and Humidity Rebalancing

## Summary
Add glass doors to open vertical and horizontal refrigerated cases, then rebalance HVAC, latent control, and anti-sweat heater operation so the refrigeration savings from reduced case infiltration are fully captured without creating new humidity, comfort, or product-quality problems. Critically, anti-sweat heater control must be addressed explicitly: doors reduce case convection load but increase anti-sweat heater kW — net refrigeration savings require anti-sweat heater control optimization as a mandatory companion measure.

## Estimated Savings
- **CIBSE Guidance**: 25–40% reduction in case sensible cooling load in open-display cases; anti-sweat heater optimization adds 5–10% net refrigeration savings (per CIBSE Guide B refrigeration case performance data)
- **ASHRAE Guidance**: 20–35% reduction in refrigeration electricity where open cases dominate and anti-sweat heaters are properly controlled (per ASHRAE Handbook HVAC Systems and Equipment — Refrigerated Case Studies)
- **End-Uses Affected**: Refrigeration electricity (case load reduction), HVAC latent load (reduced dehumidification demand), anti-sweat heater electricity (increase if uncontrolled), store comfort and product quality

## Basis / References

### CIBSE References
- **Guide B** (HVAC): Refrigeration system interactions with HVAC and latent load management in grocery stores
- **CIBSE TM39** (Building Energy Metering): Whole-store energy metering and case-by-case disaggregation methodology

### ASHRAE References
- **90.1** (Energy Standard): §6.4 for HVAC control and §10 for lighting — interactions with case door energy balance
- **62.1** (Ventilation for IAQ): Store minimum ventilation rate and interaction with pressurization after case door installation
- **AEDG50-GroceryStores-2015**: Case doors as a major HVAC/refrigeration interaction ECM — explicitly addresses store balance point and humidity changes after door adoption

### Other Standards
- **AHRI 1200** (Refrigerated Display Case Performance): Energy consumption standards for open and closed display cases
- **ENERGY STAR Certified Commercial Refrigerators/Freezers**: Anti-sweat heater control performance standards

## Assumptions
Baseline is open-display vertical and horizontal cases with no doors. Case door retrofits are most effective where open-case infiltration represents >40% of total case load (typical in stores with high customer traffic and high store HVAC latent load). Anti-sweat heater control optimization requires: door frame heaters, transparent glass doors with low-E coating (U-value ≤0.45 BTU/hr·ft²·°F), and anti-sweat heater controller with humidity compensation. Anti-sweat heater runtime reduction target: ≥60% reduction through humidity-based control vs. constant-on. HVAC latent capacity: ≥0.15 lb water/lb dry air in hot-humid climates for effective moisture removal. Positive store pressure: ≥+0.003 in. WC relative to outdoors.

## Climate Zone Relevance
Strongest in hot-humid climates (CZ 1–3, CZ 6A) where open-case infiltration is highest and HVAC latent loads are significant. In dry climates (CZ 3B, CZ 4B), anti-sweat heater loads are lower but HVAC rebalancing is still required. Cold climates (CZ 5–8) have lower latent loads but anti-sweat heater savings are still significant due to lower indoor humidity targets. All climate zones benefit from reduced case load; humidity control complexity is climate-dependent.

## Interaction Notes
This is not simply a refrigeration measure — it changes the store energy balance point, HVAC latent control strategy, and anti-sweat heater demand simultaneously. The refrigeration savings from case doors can be partially or fully offset by increased anti-sweat heater kW if heaters are left on constant. Anti-sweat heater optimization (humidity-compensated control) is a mandatory companion to case door installation for net positive savings. Complements ECM_Grocery_Humidity_Control_and_Positive_Pressure for store pressurization and latent management. Synergizes with ECM_Condenser_and_Head_Pressure_Optimization_Grocery for plant-level optimization. Pairs with ECM_Kitchen_Exhaust_and_Makeup_Air_Grocery for store pressure management after case door changes.

## Implementation Essentials
- **Case selection**: Select door types appropriate to case temperature class (medium-temp: 33–41°F; low-temp: ≤0°F); verify glass door thermal performance (U-value, condensation resistance)
- **Anti-sweat heater assessment**: Survey existing anti-sweat heater type (frame heaters, glass heaters, mullion heaters); quantify heater wattage per case before specifying control strategy
- **Humidity-compensated anti-sweat control**: Install humidity sensors inside case frame or on door glass; configure controller to modulate heater output based on dew point differential — target: anti-sweat heater on when glass dew point >55°F; off when glass dew point <50°F
- **HVAC latent capacity rebalancing**: After door installation, re-measure store sensible/latent loads; adjust dehumidification capacity or setpoint if store RH trends >55% (hot-humid) or <25% (cold-dry)
- **Positive pressure verification**: Measure store pressure relative to outdoors; install make-up air dampers if pressure drops below +0.003 in. WC after doors
- **Case temperature verification**: Doors change case internal convection; verify case temperature maintenance per AHRI 1200 after door installation — some cases require fan speed adjustment post-door
- **Commissioning**: Test anti-sweat heater control cycle over 24-hour period with varying store humidity; verify no condensation on glass at design conditions

## Risks / Constraints
- **Anti-sweat heater increase without control offsets savings**: Installing doors without anti-sweat heater control optimization can increase total store energy — anti-sweat heater power densities of 5–15 W/linear ft of door frame are common; mandatory companion control required
- **HVAC latent rebalancing is not optional**: If HVAC latent capacity is insufficient after doors, store humidity rises above 60% RH, causing product quality issues (meat discoloration, produce wilting) and customer discomfort — mitigate by commissioning HVAC latent performance within 30 days of door installation
- **Merchandising teams may resist door deployment**: Doors can reduce product visibility and impulse purchasing in some categories — mitigate by piloting in lower-traffic aisles or end-caps before full rollout; track sales data per case before/after door installation
- **Case temperature drift post-door**: Some cases experience temperature rise post-door due to reduced convection; verify case temperature after installation and adjust case fan speed if needed (increase 5–10% if temperature drifts >2°F above original)
- **Door frame structural preparation**: Older cases may not have structural reinforcement for door tracks — assess case frame condition before door installation; budget for frame reinforcement if needed

## KPIs
- Refrigeration electricity (kWh/month by case bank) — target: ≥25% reduction from baseline for open cases with doors + anti-sweat control
- Anti-sweat heater runtime (hours/month) and electricity (kWh/month) — target: ≥60% reduction from constant-on baseline through humidity-compensated control
- Store relative humidity (%) and dew point (°F) — maintain 40–60% RH and ≤55°F dew point in hot-humid climates; ≤35% RH in cold climates
- Store pressure relative to outdoors (in. WC) — maintain ≥+0.003 in. WC positive pressure
- Anti-sweat heater on/off events (count/day) — correlate with store humidity levels
- Case temperature compliance (°F) vs AHRI 1200 standards — verify no temperature drift >2°F post-door
- HVAC energy (kWh/month for store air conditioning) — measure before/after HVAC rebalancing to capture secondary latent control savings
- Product quality metrics: shrink % per case before/after doors (for merchandising acceptance tracking)

## M&V Plan
**Option B (Retrofit Isolation — Case/Refrigeration System Level)** per IPMVP where case-level submetering exists; Option C for whole-store estimation

**Quantification approach:**
- Baseline: 12 months of case refrigeration energy (kWh) from case controllers or sub-metering; baseline anti-sweat heater energy estimated from heater wattage × constant-on hours (0.8 utilization factor)
- Post-implementation: Track case refrigeration kWh monthly; track anti-sweat heater kWh from dedicated metering (if available); measure HVAC latent energy before/after rebalancing
- Calculate net savings: (Case refrigeration reduction + Anti-sweat heater reduction − HVAC latent change)
- Normalize for store traffic variations (customer count proxy), ambient temperature (weather normalization using CDD), and seasonal merchandising changes
- Pre/post comparison: minimum 12 months baseline to capture seasonal variation; post-implementation monitoring for 6 months minimum

**Data collection:**
- Case refrigeration energy (kWh) at monthly intervals by case bank or individual case
- Anti-sweat heater runtime (hours) and energy (kWh) — measure using logger on heater circuit
- Store relative humidity (%) and temperature at 15-minute intervals at multiple locations
- Store dew point temperature (°F) — maintain ≤55°F in hot-humid climates
- Store pressure relative to outdoors (in. WC) at 15-minute intervals
- HVAC air conditioning energy (kWh) from store utility meter or HVAC sub-meter
- Outside air temperature (°F) and relative humidity (%) for weather normalization
- Customer traffic count or POS transaction count (proxy for store traffic variations)

## Costs & Payback (Indicative)
- **Capex**: Glass doors (retrofits): £150–400 per linear ft of case; anti-sweat heater controller and sensors: £500–2,000 per case bank; HVAC latent rebalancing (dampers, sensors, recalibration): £2,000–8,000 per store; commissioning: £1,500–4,000
- **Opex**: Anti-sweat heater controller maintenance: £200–500/year; annual case door gasket inspection: £500–1,500/year
- **Simple payback**: 3–7 years in hot-humid stores with high open-case infiltration and significant anti-sweat heater loads; longer in cold-climate stores with low humidity
- **ROI**: Enhanced by anti-sweat heater control which reduces payback by 1–2 years vs. doors alone

## Templates / Reuse
*Boilerplate footer removed. Reference AHRI 1200 for refrigerated case performance and CIBSE Guide B for HVAC/refrigeration interactions.*
