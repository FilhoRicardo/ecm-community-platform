---
Main System: "[[Heat Recovery]]"
Category System: "[[Refrigeration / HVAC]]"
Utility Affected: "[[Heating and Cooling]]"
Source Document: "[[AEDG50-GroceryStores-2015.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Refrigerant Heat Recovery for HVAC and Hot Water

## Summary
Recover refrigeration reject heat for HVAC preheat or domestic hot-water loads so useful heat is not thrown away while separate heating systems run. Grocery stores are uniquely suited to heat recovery because refrigeration runs continuously at high capacity, providing a reliable heat source that overlaps meaningfully with store heating and hot-water demands across all seasons.

## Estimated Savings
- **CIBSE Guidance**: 20–40% of natural gas for space heating and 30–50% of DHW heating energy in high-refrigeration-duty stores (per CIBSE Guide B heat recovery data for food retail)
- **ASHRAE Guidance**: 15–35% of heating fuel in stores with substantial refrigeration runtime and concurrent heating/DHW loads (per ASHRAE Handbook Refrigeration and AEDG50-GroceryStores)
- **End-Uses Affected**: Natural gas for space heating, DHW heating energy, refrigeration system interaction (condensing pressure), and sometimes bakery/delicatessen loads

## Basis / References

### CIBSE References
- **Guide B** (HVAC): Heat recovery system design, configuration types, and performance evaluation for food retail
- **CIBSE Guide J** (Weather and Solar Data): Seasonal heat recovery load profile analysis

### ASHRAE References
- **Handbook — Refrigeration**: Chapter 11 — Refrigerant Heat Recovery configurations and control strategies
- **Handbook — HVAC Applications**: Ch. 12 — Commercial and Industrial Refrigeration Heat Recovery
- **AEDG50-GroceryStores-2015**: Heat recovery as a major grocery-specific opportunity — refrigeration reject heat is a large, continuously available source

### Other Standards
- **AHRI 550/590**: Heat recovery chiller performance rating (if heat recovery chillers are used)
- **ASHRAE 188** (Legionella): DHW return temperature requirements — heat recovery must maintain DHW return ≥110°F to prevent Legionella
- **NSF/ANSI 372** (Low Lead): Water heating equipment standards for commercial DHW

## Assumptions
Effective heat recovery requires: simultaneous refrigeration reject heat ≥50,000 BTU/hr and heating/DHW load ≥30,000 BTU/hr. Recovery temperature band: 85–115°F for space heating Preheat; 110–140°F for DHW. Typical supermarket rack compressor rejection: 2–4 BTU/hr per BTU of refrigeration capacity at rated conditions. System configuration: desuperheater (high-temperature refrigerant gas heat exchange) for DHW Preheat, or full heat recovery (liquid subcooling) for combined space/DHW. Minimum heating load threshold for economic viability: ≥2,000 hours/year of simultaneous demand.

## Climate Zone Relevance
All climate zones; most effective in climates with significant concurrent heating loads (cold-dry, mixed-humid) where refrigeration runs year-round and heating season is ≥4 months. In hot-humid climates (CZ 1–2), heating loads are lower but DHW demand is consistent year-round. Shoulder seasons (spring, autumn) often provide the highest recovery utilization when both cooling and heating loads coexist. Winter months in cold climates may limit recovery utilization due to very low refrigeration loads.

## Interaction Notes
Pairs with ECM_Condenser_and_Head_Pressure_Optimization_Grocery: heat recovery increases condensing pressure when active, so coordination between heat recovery enable/disable and head pressure control is required. Complements ECM_Grocery_Humidity_Control_and_Positive_Pressure: recovered heat for space heating preheat reduces boiler energy and simultaneously reduces latent load from over-dried makeup air. Synergizes with ECM_Kitchen_Exhaust_and_Makeup_Air_Grocery when kitchen DHW loads are substantial. Does not conflict with any other ECM; must be sequenced correctly with head pressure optimization.

## Implementation Essentials
- **Simultaneous load analysis**: Model or measure hourly overlap between refrigeration reject heat (BTU/hr) and heating/DHW demand (BTU/hr) — minimum concurrent load threshold: ≥30,000 BTU/hr for ≥30% of refrigeration operating hours
- **Configuration selection**: Desuperheater (gas-side heat exchange, 110–140°F water) for DHW Preheat only; full heat recovery for combined space heating + DHW (requires larger heat exchangers)
- **Control sequencing**: Prioritize DHW Preheat first (highest temperature requirement); sequence space heating Preheat second; configure heat recovery to enable when condensing pressure is above threshold (e.g., ≥180 psig) to avoid excessive load on refrigeration
- **Legionella protection**: Configure DHW return temperature monitoring; heat recovery must maintain DHW return ≥110°F — if return drops below 110°F for >5 minutes, heat recovery control must automatically increase recovery or supplementary heating
- **Condensing pressure management**: Heat recovery raises condensing pressure; configure head pressure setpoint to float up by 10–15 psig when heat recovery is active — do not let recovery operation force excessive condensing pressure that degrades compressor efficiency
- **Seasonal logic**: Enable heat recovery mode when outdoor temperature is below threshold (e.g., ≤55°F for space heating; year-round for DHW); disable in summer when heating loads are minimal
- **Trend monitoring**: Install heat exchanger supply/return temperature sensors, flow meters on recovery loop, and refrigeration condensing pressure — calculate recovered heat (BTU/hr) from temperature differential × flow rate

## Risks / Constraints
- **Poor control raises refrigeration energy if condensing pressure is pushed too high**: Heat recovery that forces condensing pressure above optimal range increases compressor work and can erase the heating savings — mitigate by coordinating heat recovery with floating head pressure control; verify compressor efficiency is not degraded when recovery is active
- **Shoulder-season utilization is highest but control complexity is also highest**: Spring and autumn have the best concurrent load overlap but also require frequent enable/disable cycling — mitigate with automatic seasonal logic that responds to outdoor temperature and refrigeration load
- **DHW return temperature can drop below Legionella threshold if recovery is excessive**: If heat recovery pulls too much heat from the refrigeration loop, system efficiency degrades — mitigate by installing automatic temperature-limiting valves and DHW return temperature monitoring with Alarm
- **Winter utilization drops as refrigeration loads decrease**: In cold climates, winter refrigeration loads may be insufficient to provide meaningful recovery — verify minimum concurrent load threshold before system design
- **Maintenance of heat exchangers**: Scale buildup in desuperheater and recovery heat exchangers reduces efficiency — schedule annual heat exchanger cleaning; track approach temperature as an indicator of fouling

## KPIs
- Recovered heat energy (MMBtu/month and MMBtu/year) — target: ≥20 MMBtu/year per 100 tons of refrigeration capacity
- Heating fuel displacement (therms/year or MMBtu/year) — target: ≥30% of annual space heating fuel
- DHW energy displacement (kBtu/year) — target: ≥40% of annual DHW heating energy
- Heat recovery runtime (hours/year) — target: ≥2,000 hours/year where concurrent loads are sufficient
- Condensing pressure impact (psig increase when recovery is active) — verify increase ≤15 psig above floating setpoint
- DHW return temperature (°F) — maintain ≥110°F at all times; target: ≥120°F
- Refrigeration COP with and without heat recovery active — verify no more than 5% degradation in COP when recovery is operating
- Approach temperature on recovery heat exchanger (°F) — target: ≤10°F approach at design conditions; monitor for fouling (increase >15°F indicates cleaning needed)

## M&V Plan
**Option B (Retrofit Isolation — Plant/Subsystem Level)** per IPMVP where dedicated heat recovery metering exists; Option C for whole-store estimation

**Quantification approach:**
- Baseline: 12 months of heating fuel (therms or m³) and DHW fuel (kBtu) with heat recovery inactive
- Post-implementation: Track monthly fuel consumption; calculate heating fuel reduction vs weather-normalized baseline (using HDD for gas normalization)
- Calculate recovered heat: Q_recovered (BTU/hr) = Flow_rate (lb/hr) × Cp × ΔT (°F); track monthly recovered BTU
- Weather normalization: regress preheating energy against HDD; apply same regression to post-data for weather-normalized savings
- Verify refrigeration penalty: compare compressor kWh with heat recovery on/off at equivalent load and ambient conditions; calculate net savings = heating fuel saved + DHW fuel saved − refrigeration penalty

**Data collection:**
- Heating fuel consumption (therms/month) from gas meter
- DHW fuel consumption (therms or kBtu/month) if separately metered
- Heat recovery loop flow rate (GPM) and supply/return temperatures (°F) at 15-minute intervals
- Refrigeration condensing pressure (psig) at 15-minute intervals with heat recovery on/off status
- Compressor energy (kWh) with heat recovery on/off — for refrigeration penalty calculation
- DHW return temperature (°F) — maintain ≥110°F per ASHRAE 188
- Outside air temperature (°F) and HDD for weather normalization
- Hot water draw profile (gallons/day or number of draws) as demand proxy

## Costs & Payback (Indicative)
- **Capex**: Desuperheater (DHW Preheat): £4,000–12,000; full recovery system (space + DHW): £15,000–40,000; heat exchangers, controls, and commissioning: £8,000–25,000
- **Opex**: Annual heat exchanger cleaning and inspection: £500–1,500/year; water treatment if applicable: £300–800/year
- **Simple payback**: 3–7 years in stores with substantial concurrent heating/DHW loads and ≥2,000 recovery hours/year; marginal below 1,500 hours/year
- **ROI**: Strategic long-term measure; carbon reduction value is significant for net-zero pathways; synergies with HVAC upgrades

## Templates / Reuse
*Boilerplate footer removed. Reference ASHRAE Handbook Refrigeration Chapter 11 and CIBSE Guide B for heat recovery design guidance.*
