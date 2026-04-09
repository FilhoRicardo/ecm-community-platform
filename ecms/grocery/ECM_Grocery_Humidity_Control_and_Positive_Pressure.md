---
Main System: "[[Humidity Control]]"
Category System: "[[HVAC]]"
Utility Affected: "[[Cooling]]"
Source Document: "[[AEDG50-GroceryStores-2015.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Positive Pressure and Humidity Control for Grocery Comfort and Product Quality

## Summary
Maintain positive store pressure and active humidity (dew point) control to protect refrigeration and HVAC ECM investments, ensure product quality, prevent condensation on refrigerated cases, and achieve customer comfort. Humidity control is not a standalone measure — it is the enabling infrastructure for multiple other ECMs to deliver their savings without adverse interactions. Store dew point control (not just dry-bulb temperature) is the key performance metric because product quality and anti-sweat heater performance are dew-point-dependent.

## Estimated Savings
- **CIBSE Guidance**: 5–15% of HVAC electricity through optimized latent removal and pressurization; protects 10–30% of other ECM savings that depend on humidity control (per CIBSE Guide B humidity control data)
- **ASHRAE Guidance**: 3–8% of total store energy through dew-point-based HVAC control vs. temperature-only control (per ASHRAE 62.1 and AEDG50-GroceryStores)
- **End-Uses Affected**: HVAC latent energy, anti-sweat heater demand (reduced when store dew point is controlled ≤55°F), refrigeration system latent load, and store comfort/product quality

## Basis / References

### CIBSE References
- **Guide B** (HVAC): Store humidity control, latent load management, and dew point control methodology
- **Guide A** (Environmental Design): Human comfort and indoor air quality at varying humidity levels
- **CIBSE TM39** (Building Energy Metering): HVAC latent energy monitoring and disaggregation

### ASHRAE References
- **62.1** (Ventilation for IAQ): §6.2 for demand-controlled ventilation and minimum outdoor air rates; humidity control interaction with ventilation rate
- **90.1** (Energy Standard): §6.4 for HVAC control requirements and humidity control sequences
- **AEDG50-GroceryStores-2015**: Humidity control and pressurization as critical interaction issues with case doors, kitchen exhaust, and refrigeration

### Other Standards
- **IEC 60068** (Environmental Testing): Humidity sensor performance and calibration standards
- **AHRI 1200** (Refrigerated Display Case Performance): Anti-sweat heater performance related to store humidity conditions

## Assumptions
Baseline store HVAC controls temperature (dry-bulb) without active dew point management, resulting in uncontrolled store humidity, excessive anti-sweat heater runtime, and latent control drift. Target store dew point: ≤55°F in hot-humid climates (store temperature 72–76°F, RH 45–55%); ≤45°F in cold climates (store temperature 65–70°F, RH 30–45%). Positive pressure target: ≥+0.003 in. WC relative to outdoors at all times. HVAC latent capacity target: ≥0.12 lb water/lb dry air at design conditions in hot-humid climates. Dew point sensor accuracy: ±2°F; calibrate annually.

## Climate Zone Relevance
Most important in hot-humid and mixed-humid climates (CZ 1–3, CZ 6A) where latent loads are high and dew point control has the largest impact on anti-sweat heater energy and product quality. Still important in temperate climates where day/night humidity swing causes morning condensation events. Cold climates (CZ 5–8) require winter humidification to maintain product quality and customer comfort; humidity control is not just a dehumidification issue — winter low humidity creates produce dehydration and customer discomfort.

## Interaction Notes
This measure is a prerequisite for ECM_Case_Doors_and_HVAC_Rebalance_Grocery (humidity rebalancing post-doors) and ECM_Refrigerant_Heat_Recovery_Grocery (heat recovery increases system heat load, affecting latent control). Supports kitchen exhaust integration (ECM_Kitchen_Exhaust_and_Makeup_Air_Grocery) by managing the latent load from kitchen makeup air. Complements ECM_Condenser_and_Head_Pressure_Optimization_Grocery (same HVAC system, different focus). Protects savings from all lighting, plug load, and refrigeration measures that depend on stable store humidity.

## Implementation Essentials
- **Dew point monitoring network**: Install dew point sensors at store entry points, refrigeration case lines, and central store location; minimum 3 locations for stores >15,000 ft²
- **HVAC latent capacity assessment**: Measure store latent load using psychrometric analysis or sub-metered HVAC energy; if latent capacity <0.12 lb water/lb dry air, consider adding dedicated dehumidification or upgrading HVAC latent coils
- **Positive pressure control**: Install building pressure sensor; configure makeup air dampers to maintain ≥+0.003 in. WC pressure relative to outdoors; modulate exhaust fans to coordinate with pressurization
- **Dew point control sequence**: Configure BAS to use store dew point as the primary control variable for HVAC latent coils (dehumidification setpoint: 52°F dew point for hot-humid; 42°F for temperate/mixed)
- **Entry air management**: Install air curtains or vestibule sealed doors at main entrances to reduce infiltration of warm, humid outdoor air; entry infiltration is a primary latent load driver
- **Kitchen pressure isolation**: Ensure kitchen area has dedicated exhaust and makeup air to prevent kitchen humidity from migrating to sales floor
- **Morning startup sequence**: Configure morning startup HVAC ramp-up to pre-condition store before opening, targeting dew point ≤55°F 30 minutes before opening

## Risks / Constraints
- **Latent control drift without active monitoring**: Store humidity drifts gradually over weeks if dew point monitoring is absent; by the time dry-bulb temperature alerts trigger action, humidity damage is already done — mitigate by implementing continuous dew point logging and trend review (weekly)
- **Over-dehumidification in cold weather increases energy waste**: If dew point setpoint is too low in cold climates, HVAC overworks to remove moisture that is already low — set dew point targets by climate and season: winter humidification may be needed rather than dehumidification
- **Entry infiltration is often underestimated**: Without air curtains or vestibule seals, main entrance infiltration can represent 15–25% of total store latent load — mitigate by measuring entrance infiltration impact with door-open/door-closed testing
- **Kitchen humidity migrates to sales floor**: If kitchen exhaust is inadequate or makeup air is unconditioned, kitchen moisture migrates to sales floor and overwhelms HVAC latent capacity — mitigate by isolating kitchen pressure and providing dedicated makeup air with latent treatment
- **Sensor drift undermines control**: Dew point sensors drift ±3–5°F over 12 months without calibration — schedule annual calibration; install dual-sensor voting logic for critical control loops

## KPIs
- Store dew point (°F) at multiple locations — maintain ≤55°F in hot-humid climates; ≤45°F in temperate/cold climates; target: ≥95% of operating hours within setpoint band
- Store relative humidity (%) — maintain 40–55% RH in hot-humid; 30–45% RH in cold climates
- Building pressure relative to outdoors (in. WC) — maintain ≥+0.003 in. WC positive pressure; target: ≥98% of operating hours
- Anti-sweat heater runtime (hours/day) as indirect humidity control indicator — reduced runtime indicates successful humidity management
- HVAC latent energy (kBtu/month) — measure through sub-metered HVAC or estimate from sensible/latent coil split
- Product shrink percentage by department (grocery, produce, meat, bakery) — humidity-related shrink correlates with dew point control failures
- Condensation events on refrigerated cases (count/month) — any event indicates humidity control failure
- Entry air infiltration impact (estimated CFM of outdoor air through entrances) — benchmark before/after air curtain installation

## M&V Plan
**Option C (Whole Building)** per IPMVP where store-level utility metering is available

**Quantification approach:**
- Baseline: 12 months of store utility energy (electricity and gas) combined with humidity trend data; characterize baseline dew point distribution and HVAC latent energy
- Post-implementation: Track store dew point compliance rate (% of hours within target band); calculate avoided anti-sweat heater energy and humidity-related refrigeration losses
- Quantify avoided product shrink: compare shrink by department before/after humidity control improvement (requires store POS/shrink data)
- Normalize for occupancy variations (customer traffic) and seasonal changes; weather normalization using CDD relevant to latent load

**Data collection:**
- Store dew point (°F) at multiple locations at 15-minute intervals (minimum 3 sensors for stores >15,000 ft²)
- Store relative humidity (%) and temperature (°F) at 15-minute intervals
- Building pressure relative to outdoors (in. WC) at 15-minute intervals
- Anti-sweat heater runtime (hours/day) from case controller logs
- HVAC electricity (kWh/month) from utility meter or HVAC sub-meter
- Customer traffic count (proxy for internal moisture generation from foot traffic)
- Outside air temperature (°F) and relative humidity (%) for weather normalization
- Product shrink data by department (% by category) for quality correlation

## Costs & Payback (Indicative)
- **Capex**: Dew point sensors (3–6 units): £1,500–4,000; building pressure sensors (2–4 units): £500–2,000; BAS integration and programming: £3,000–10,000; air curtains at main entrances: £2,000–6,000; HVAC latent coil upgrade if needed: £8,000–25,000
- **Opex**: Annual dew point sensor calibration: £500–1,500/year; weekly dew point trend review (staff time): ~2 hours/week
- **Simple payback**: 1–3 years for controls-only retrofits; 4–8 years if HVAC latent coil upgrade is required
- **ROI**: High protect value — each humidity control failure that causes product shrink or anti-sweat heater waste costs more than annual humidity control maintenance

## Templates / Reuse
*Boilerplate footer removed. Reference CIBSE Guide B and ASHRAE 62.1 for humidity control methodology.*
