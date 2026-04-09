---
Main System: "[[Chillers]]"
Category System: "[[Heat Recovery]]"
Utility Affected: "[[Heating and Cooling]]"
Source Document: "[[AEDG30-SmallHealthcare-2009.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Condenser Heat Recovery for Reheat and DHW Preheat

## Summary
Recover waste heat from cooling equipment to offset reheat or domestic hot-water loads in small healthcare buildings with simultaneous cooling and heating demand. Small healthcare facilities often have persistent reheat requirements driven by ventilation standards, and this reheat load overlaps significantly with cooling plant operation — making condenser heat recovery a practical and cost-effective measure.

## Estimated Savings
- **CIBSE Guidance**: 15–30% of boiler fuel for space heating and 25–45% of DHW heating in small healthcare facilities with significant concurrent loads (per CIBSE Guide B heat recovery data)
- **ASHRAE Guidance**: 10–25% of heating energy in small healthcare facilities with simultaneous cooling and reheat/DHW loads (per ASHRAE HVAC Applications and AEDG30-SmallHealthcare)
- **End-Uses Affected**: Boiler fuel (gas/oil) for space heating, DHW heating energy, refrigeration plant interaction, and reheat coil energy

## Basis / References

### CIBSE References
- **Guide B** (HVAC): Condenser heat recovery configurations, control strategies, and sizing for small healthcare applications
- **Guide J** (Weather and Solar Data): Seasonal heat recovery load profile analysis

### ASHRAE References
- **Handbook — Refrigeration**: Chapter 11 — Condenser Heat Recovery configurations and control strategies
- **Handbook — HVAC Applications**: Ch. 12 — Commercial Refrigeration Heat Recovery
- **AEDG30-SmallHealthcare-2009**: Condenser heat recovery as a notable small healthcare opportunity where cooling and reheat occur simultaneously

### Other Standards
- **AHRI 550/590**: Heat recovery chiller performance rating
- **ASHRAE 188** (Legionella): DHW return temperature requirements — heat recovery must maintain DHW return ≥110°F

## Assumptions
Effective heat recovery requires: simultaneous cooling load ≥20 tons and heating/DHW load ≥30,000 BTU/hr. Recovery temperature band: 85–115°F for space heating preheat; 110–140°F for DHW preheat. Small healthcare facility (typically 10,000–50,000 ft²): heat recovery loop is typically smaller than large hospital installations. Minimum concurrent load threshold: ≥2,000 hours/year of simultaneous demand for economic viability. Small healthcare facilities often have smaller chiller plant (1–2 chillers), making condenser heat recovery more straightforward to integrate than in large central plants.

## Climate Zone Relevance
All climate zones, especially where dehumidification and ventilation drive persistent reheat loads. Most effective in climates with significant concurrent cooling/heating overlap (hot-humid, mixed-humid) where refrigeration runs frequently and heating loads are present. Shoulder seasons (spring/autumn) often provide the highest recovery utilization. Winter months in cold climates may have limited cooling loads, reducing winter recovery potential.

## Interaction Notes
Pairs with ECM_DOAS_with_Heat_Recovery_Small_Healthcare: DOAS reduces but does not eliminate reheat; heat recovery offsets the remaining reheat load. Complements ECM_SWH_Distribution_and_Point_of_Use_Small_Healthcare when DHW preheat is the recovery sink. Synergizes with chilled-water systems and WSHP systems. Does not conflict with any other ECM; must be sequenced correctly with chiller plant control.

## Implementation Essentials
- **Simultaneous load analysis**: Model or measure hourly overlap between cooling capacity (tons) and heating/DHW demand (BTU/hr) — minimum 1 year of hourly data recommended; heat recovery viable if concurrent load ≥30% of operating hours
- **Sink definition**: Reheat coil loop (85–115°F), DHW preheat (110–140°F), or both — prioritize DHW preheat first (highest temperature, clearest use case for infection control)
- **Plant coordination**: Configure chiller condenser water temperature setpoint to float up by 10–15°F when heat recovery is active; coordinate with chiller unloading to prevent excessive lift
- **Control sequencing**: Heat recovery enable when condensing temperature is above recovery setpoint (e.g., ≥85°F leaving water temperature); disable when condensing temperature drops below minimum recovery temperature
- **Legionella protection**: Configure DHW return temperature monitoring; heat recovery must maintain DHW return ≥110°F — if return drops below 110°F for >5 minutes, heat recovery control must automatically increase recovery or supplementary heating
- **Seasonal logic**: Enable heat recovery mode based on outdoor temperature and concurrent load — spring/autumn typically highest utilization; winter may require boiler backup
- **Trend monitoring**: Install heat exchanger supply/return temperature sensors and flow meters on recovery loop; calculate recovered heat (BTU/hr) from temperature differential × flow rate

## Risks / Constraints
- **Poor load matching weakens economics**: Heat recovery hours <1,500 hr/year indicate marginal economics — validate with concurrent load analysis before committing capital
- **Control complexity in small plants**: Smaller chiller plants have less staging flexibility; verify heat recovery does not cause chiller short-cycling or excessive on/off cycling
- **DHW return temperature can drop below Legionella threshold**: If heat recovery pulls too much heat from the refrigeration loop, system efficiency degrades — Mitigate: install automatic temperature-limiting valves and DHW return temperature monitoring with alarm
- **Shoulder-season is highest-value but most complex to optimize**: Spring and autumn have the best concurrent load overlap; dedicate commissioning time to these seasons; implement automatic seasonal logic
- **Winter utilization drops as refrigeration loads decrease**: In cold climates, winter refrigeration loads may be insufficient for meaningful recovery — verify minimum concurrent load threshold before design

## KPIs
- Recovered heat energy (MMBtu/month and MMBtu/year) — target: ≥10 MMBtu/year per 100 tons of refrigeration capacity
- Heating fuel displacement (therms/year or MMBtu/year) — target: ≥20% of annual space heating fuel where concurrent loads are sufficient
- DHW energy displacement (kBtu/year) — target: ≥30% of annual DHW heating energy
- Heat recovery runtime (hours/year) — target: ≥1,500 hours/year where concurrent loads are sufficient
- Condensing temperature impact (°F increase when recovery is active) — verify increase ≤15°F above baseline
- DHW return temperature (°F) — maintain ≥110°F at all times; target: ≥120°F
- Refrigeration COP with and without heat recovery active — verify no more than 5% degradation in COP when recovery is operating

## M&V Plan
**Option B (Retrofit Isolation — Plant/Subsystem Level)** per IPMVP where dedicated heat recovery metering exists; Option C for whole-store estimation

**Quantification approach:**
- Baseline: 12 months of heating fuel (therms) and DHW fuel with heat recovery inactive
- Post-implementation: Track monthly fuel consumption; calculate heating fuel reduction vs weather-normalized baseline (using HDD for gas normalization)
- Calculate recovered heat: Q_recovered (BTU/hr) = Flow_rate (lb/hr) × Cp × ΔT (°F); track monthly recovered BTU
- Weather normalization: regress preheating energy against HDD; apply same regression to post-data for weather-normalized savings
- Verify refrigeration penalty: compare compressor kWh with heat recovery on/off at equivalent load and ambient conditions

**Data collection:**
- Heating fuel consumption (therms/month) from gas meter
- DHW fuel consumption (therms or kBtu/month) if separately metered
- Heat recovery loop flow rate (GPM) and supply/return temperatures (°F) at 15-minute intervals
- Refrigeration condensing temperature (°F) with heat recovery on/off status
- Compressor energy (kWh) with heat recovery on/off — for refrigeration penalty calculation
- DHW return temperature (°F) — maintain ≥110°F per ASHRAE 188
- Outside air temperature (°F) and HDD for weather normalization

## Costs & Payback (Indicative)
- **Capex**: Desuperheater (DHW preheat): £3,000–10,000; full recovery system (space + DHW): £10,000–30,000; controls and commissioning: £5,000–15,000
- **Opex**: Annual heat exchanger cleaning: £500–1,500/year; water treatment if applicable: £300–800/year
- **Simple payback**: 3–7 years in facilities with substantial concurrent heating/DHW loads; marginal below 1,000 hours/year
- **ROI**: Strategic long-term measure; carbon reduction value is significant for net-zero pathways

## Templates / Reuse
*Boilerplate footer removed. Reference ASHRAE Handbook Refrigeration Chapter 11 and CIBSE Guide B for heat recovery design guidance.*
