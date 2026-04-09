---
Main System: "[[Heat Recovery Chiller]]"
Category System: "[[HVAC Plant]]"
Utility Affected: "[[Heating and Cooling]]"
Source Document: "[[AEDG50-LargeHospitals-2012.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Heat-Recovery Chillers and Concurrent-Load Optimization

## Summary
Install heat-recovery chillers where large hospitals have persistent simultaneous heating and cooling loads, enabling waste heat from refrigeration plant to offset boiler energy for space heating, domestic hot water, and sterilizer steam preheat — eliminating simultaneous heating and cooling waste.

## Estimated Savings
- **CIBSE Guidance**: 20–35% of boiler fuel in facilities with high concurrent heating and cooling loads (per CIBSE Guide B heat recovery design data)
- **ASHRAE Guidance**: 15–30% of boiler energy in continuously operating hospitals with simultaneous loads (per ASHRAE HVAC Applications Chiller-Heat-Recovery guidance)
- **End-Uses Affected**: Boiler fuel (gas/oil), chiller plant efficiency, DHW heating, sterilizerPreheat, and plant dispatch optimization

## Basis / References

### CIBSE References
- **Guide B** (HVAC): Heat recovery system design, concurrent load sizing, and plant integration
- **CIBSE AM12** (Building Energy Performance): Whole-building plant integration and heat recovery performance metrics
- **CIBSE Guide J** (Weather and Solar Data): Seasonal load profile analysis for heat recovery optimization

### ASHRAE References
- **90.1** (Energy Standard): Table 6.8.1 for centrifugal chiller COP and heat recovery chiller efficiency requirements
- **HVAC Applications**: Chiller heat recovery Chapter 12 — concurrent load sizing and control philosophy
- **AEDG50-LargeHospitals-2012**: Advanced HVAC/plant strategy — heat-recovery chillers as executive summary recommendation

### Other Standards
- **AHRI 550/590**: Heat recovery chiller performance rating standards
- **FGI 2018 Guidelines**: Sterilizer and DHW system integration must maintain clinical performance

## Assumptions
Large hospitals (typically >200 beds) have the concurrent cooling/heating diversity needed to justify heat-recovery chillers. Effective heat recovery requires: simultaneous cooling load ≥150 tons and heating load ≥500,000 BTU/hr. Hot water temperature target: 110–140°F for DHW; heat recovery chillers can typically deliver 95–120°F leaving water temperature efficiently. Boiler efficiency 85–93% (natural gas) is the displaced baseline. Heat recovery chiller efficiency target: COP ≥5.5 at design conditions. Seasonal utilization: heat recovery is most effective in shoulder seasons (spring/autumn) when heating loads are moderate and cooling loads are present; winter months may require boiler backup if recovery capacity is insufficient.

## Climate Zone Relevance
All climate zones; strongest in climates with significant cooling loads year-round (hot-humid, mixed-humid) where concurrent heating/cooling is most frequent. Winter-dominant climates (cold-dry) may have limited cooling loads in winter, reducing heat recovery utilization hours.

## Interaction Notes
Pairs strongly with decoupled ventilation (ECM_Decoupled_Ventilation_and_Reheat_Reduction_Large_Hospital) because reduced reheat demand increases net heating load available for recovery. Complements DHW central plant optimization ( ECM_DHW_Central_Plant_Optimization_Lodging from lodging ECM library). Synergizes with high-delta-T chilled-water strategy (higher delta-T allows more heat recovery per unit flow). Does not conflict with air-side heat recovery (ECM_Air_Side_Heat_Recovery_Large_Hospital) — these are additive; the chiller heat recovery operates at a different temperature band.

## Implementation Essentials
- **Concurrent load analysis**: Model or measure hourly overlap between cooling and useful heating loads (DHW, space heating, sterilizer Preheat, kitchen loads) — minimum 1 year of hourly data recommended; heat recovery is viable if concurrent load exceeds threshold ≥30% of operating hours
- **Heat recovery chiller sizing**: Size heat recovery bundle to ≤50% of total chiller capacity to maintain chiller efficiency at design conditions — do not let heat recovery degrade chiller COP below design intent
- **Hot water temperature targets**: Configure heat recovery to priority-sequence DHW Preheat (140°F setpoint), then space heatingPreheat (100–110°F), then sterilizer Preheat (180°F for steam generation) — control sequence must prevent overheating and optimize dispatch
- **Boiler staging integration**: Program boiler lead/lag to utilize recovered heat before firing boiler; heat recovery should displace boiler Stage 1 firing first
- **Plant dispatch optimization**: Configure BAS to prioritize heat recovery when concurrent loads are present and chiller is operating above minimum load
- **Seasonal logic**: Implement seasonal heat recovery mode (enable/disable based on heating degree days and concurrent load correlation); winter months may have insufficient cooling for economic recovery
- **Trend monitoring**: Install flow and temperature sensors on heat recovery loop; track recovered heat (BTU/hr or kW), chiller COP, boiler runtime, and DHW temperatures

## Risks / Constraints
- **Poor load matching reduces annual utilization**: Heat recovery hours <2,000 hr/year indicate marginal economics — validate with 12 months of concurrent load data before committing capital
- **Heat recovery degrades chiller COP if oversized**: Sizing heat recovery bundle >50% of chiller capacity can increase chiller power consumption and erode net savings — size conservatively and verify chiller COP post-commissioning
- **Control complexity requires careful commissioning**: Multiple control loops (chiller, boiler, heat recovery, DHW) must be sequenced correctly — develop control sequence narrative and test at minimum 25%, 50%, 75%, 100% load before occupancy
- **Shoulder-season optimization is critical**: Spring and autumn present the highest recovery opportunity when concurrent loads overlap most frequently — dedicate commissioning time to these seasons
- **Legionella risk if DHW return temperatures drop**: Heat recovery control must maintain DHW return temperature ≥110°F to prevent Legionella proliferation per ASHRAE 188

## KPIs
- Recovered heat energy (MMBtu/month and MMBtu/year)
- Boiler fuel displacement (therms/year or kBtu/year) — target: ≥20% annual boiler energy displacement
- Heat recovery chiller runtime (hours/year) and COP at design and part-load conditions
- DHW return temperature (°F) — maintain ≥110°F to prevent Legionella; target: ≥120°F forPreheat efficiency
- Chiller COP with and without heat recovery active (compare at equivalent load and ambient conditions)
- Plant dispatch profile: % of heating load served by recovery vs boiler
- Concurrent load utilization hours (hours/year where both heating and cooling loads are present and recovery is active)
- Simple energy ratio: Total recovered heat (BTU) / Total chiller energy input (BTU) — target: ≥1.5

## M&V Plan
**Option B (Retrofit Isolation — Plant Level)** per IPMVP

**Quantification approach:**
- Baseline: 12 months of boiler fuel (therms or m³) and chiller energy (kWh) with heat recovery inactive
- Post-implementation: Track boiler fuel, chiller energy, and recovered heat quantities monthly
- Calculate boiler fuel displacement = (Baseline boiler intensity per HDD — Post boiler intensity per HDD) × Post HDD + correction for weather normalization
- Apply concurrent load utilization factor: savings = Recovered heat (BTU) × (1 / Boiler efficiency) × Utilization factor
- Normalize for weather using HDD and CDD; normalize for occupancy/census variations (patient bed count)
- Weather-normalized savings calculation: ΔFuel = (Pre fuel/HDD − Post fuel/HDD) × Post HDD

**Data collection:**
- Boiler fuel consumption (therms or m³) at 15-minute intervals (or monthly billing data with daily estimates)
- Heat recovery loop flow rate (GPM) and supply/return temperatures (°F) at 15-minute intervals
- Chiller instantaneous load (tons) and chiller energy input (kW) with heat recovery on/off status
- DHW supply and return temperatures (°F) — maintain ≥110°F return temperature monitoring
- Boiler on/off status and staging level (for dispatch profiling)
- Heating degree days (HDD) and cooling degree days (CDD) for weather normalization
- Patient bed count or occupancy proxy for clinical load normalization

## Costs & Payback (Indicative)
- **Capex**: Heat recovery chiller premium over standard chiller: £40,000–120,000 for 200–500 ton chiller; controls integration and commissioning: £15,000–40,000; flow/temperature metering: £3,000–8,000
- **Opex**: Annual commissioning check, heat recovery loop maintenance (water treatment): £1,000–3,000/year
- **Simple payback**: 5–10 years in hospitals with high concurrent loads and >2,000 recovery hours/year; marginal below 1,500 hours/year
- **ROI**: Strategic long-term measure; carbon reduction value is significant for net-zero pathways

## Templates / Reuse
*Boilerplate footer removed. Reference CIBSE Guide B Chiller Heat Recovery and ASHRAE HVAC Applications Chapter 12 for sizing and control guidance.*
