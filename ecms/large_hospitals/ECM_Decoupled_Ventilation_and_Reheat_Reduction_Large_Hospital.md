---
Main System: "[[DOAS]]"
Category System: "[[Ventilation]]"
Utility Affected: "[[Heating and Cooling]]"
Source Document: "[[AEDG50-LargeHospitals-2012.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Decoupled Ventilation and Reheat Reduction

## Summary
Decouple outdoor air (OA) treatment from zone sensible conditioning using dedicated outdoor air systems (DOAS) with heat recovery, and apply aggressive supply air temperature (SAT) reset and zone-airflow setback to reduce one of the largest energy penalties in hospitals: conditioning and reheating large volumes of ventilation air. Separate OA treatment from zone cooling/heating allows each to be optimized independently rather than operating a single large AHU with simultaneous heating and cooling.

## Estimated Savings
- **CIBSE Guidance**: 20–40% of reheat energy in over-ducted or over-VAV systems (per CIBSE Guide B DOAS design data)
- **ASHRAE Guidance**: 15–35% reduction in fan, cooling, and reheat energy in continuously ventilated hospitals with decoupled OA (per ASHRAE 90.1 application guidance)
- **End-Uses Affected**: Reheat energy, ventilation fan energy, cooling plant load, boiler energy, and zone controls complexity

## Basis / References

### CIBSE References
- **Guide B** (HVAC): DOAS system design, decoupled OA treatment, and reheat reduction methodology
- **CIBSE AM10** (Commissioning Management): Commissioning requirements for decoupled systems and control sequence verification

### ASHRAE References
- **90.1** (Energy Standard): §6.5 for ducts, §6.4 for control sequences, §6.3 for minimum OA requirements; VAV box minimum flow limits and SAT reset requirements
- **62.1** (Ventilation for IAQ): §6.2 for minimum outdoor air rate procedure; OA treatment and decoupled OA requirements for high-density spaces
- **ASHRAE 170** (Ventilation for Healthcare Facilities): Pressure relationships and minimum OA by clinical function
- **AEDG50-LargeHospitals-2012**: Central HVAC recommendation — advanced VAV with separate OA treatment and decoupled ventilation/zone conditioning
- **Guideline 36** (High Performance HVAC Sequences): Multi-zone decoupled OA control sequences

### Other Standards
- **FGI 2018 Guidelines**: §5.1 for pressure relationships during SAT reset and setback conditions in clinical zones

## Assumptions
Baseline systems with single-duct VAV and simultaneous heating/cooling reheat are assumed. Effective decoupled OA requires: DOAS with heat recovery (≥65% sensible effectiveness), zone-level variable air volume boxes with SAT reset capability, and BAS control philosophy that can independently control OA flow and zone cooling/heating. Minimum ventilation rates per ASHRAE 170 must be maintained during all setback modes. SAT reset range: 50–58°F in occupied mode, 45–60°F in setback/unoccupied mode (clinical zones require recovery to occupied conditions within 15 minutes). Zone airflow setback: ≥50% of peak flow in unoccupied periods.

## Climate Zone Relevance
All climate zones; most effective in hot-humid and mixed-humid climates where latent cooling loads are significant and OA conditioning represents a large fraction of total cooling. Cold-dry climates benefit from improved dehumidification control through decoupled OA even when sensible cooling loads are lower. Extreme climates see the largest absolute savings due to high OA conditioning energy.

## Interaction Notes
Pairs with heat recovery (ECM_Air_Side_Heat_Recovery_Large_Hospital) and plant heat recovery (ECM_Heat_Recovery_Chillers_Large_Hospital) — each layer of heat recovery on the OA stream improves decoupled OA economics and reduces reheat demand simultaneously. Required prerequisite for ECM_Airflow_Setback_in_Procedure_Spaces_Large_Hospital. Synergizes with critical vs noncritical area programming (ECM_Critical_vs_Noncritical_Area_Programming_Large_Hospital): accurate area classification enables more aggressive SAT reset in noncritical zones. Compatible with chiller high-delta-T strategy (higher approach temperatures enable more recovery capacity).

## Implementation Essentials
- **DOAS design**: Size DOAS to handle 100% of OA requirements independently of zone cooling/heating; integrate heat recovery (enthalpy wheel or plate HX) for OA pretreatment
- **SAT reset schedule**: Configure SAT reset based on zone demand — use warmest zone call for cooling, coldest zone call for heating; deadband ≥4°F between heating and cooling reset bands
- **Zone VAV boxes**: Verify VAV boxes are capable of independent SAT and airflow control; minimum airflow setpoint per ASHRAE 90.1 §6.5 (≤30% of peak for cooling, ≥40% of peak for heating in VAV systems)
- **Reheat coil rightsizing**: Right-size reheat coils for actual heating load after decoupled OA optimization; do not size for original (larger) heating load
- **Humidity control**: Maintain humidity control explicit in DOAS — configure DOAS de humidification to keep supply air dew point ≤50°F in hot-humid climates; OA preheat coil required in cold climates to prevent frost on energy recovery media
- **Pressure management**: Verify building pressure remains positive during setback — DOAS OA flow must maintain minimum OA rate even during zone setback
- **BAS integration**: Configure multi-variable control: SAT reset, zone airflow setback, and building pressure monitoring must operate as coordinated system
- **Commissioning**: Test SAT reset at 25%, 50%, 75%, 100% zone load; verify no simultaneous heating and cooling in same zone; measure recovery time to full conditions after setback

## Risks / Constraints
- **Poor control can create IAQ, pressure, or humidity issues**: Commission each control loop independently before integrating into coordinated control; use FDD to detect control failures — Mitigate: monthly BAS trend review of SAT, zone temperatures, and building pressure
- **Over-aggressive SAT reset can compromise dehumidification**: In hot-humid climates, resetting SAT too high (>55°F) reduces latent removal capacity and can cause comfort issues — maintain DOAS supply air dew point ≤52°F (or code minimum) regardless of SAT reset
- **Operators may disable aggressive sequences if not trained**: Provide quarterly training to operations staff on decoupled control philosophy; document expected behavior in O&M manual and trend logs
- **Zone minimum flow conflicts with reheat reduction**: VAV minimum flow that is too high forces simultaneous heating/cooling in perimeter zones — reduce VAV minimum flow to ≤30% of peak per ASHRAE 90.1 §6.5 where zone heating load permits
- **High-delta-T chiller strategy prerequisite**: Decoupled OA and SAT reset increase chilled water delta-T; verify chiller can operate at design approach temperature (≥12°F) without performance degradation

## KPIs
- Reheat energy intensity (kBtu/ft²/year) by zone type — target: ≥25% reduction from baseline in decoupled zones
- Zone-level simultaneous heating/cooling hours (% of occupied hours where both heating and cooling coils are >5% open simultaneously) — target: <5% of occupied hours
- Supply air temperature reset range achieved (°F) — verify reset covers 50–58°F design range
- Zone airflow during setback (% of peak flow) — target: ≤50% of peak during unoccupied setbacks
- Building pressure relative to outdoors (in. WC) — maintain ≥0.001 in. WC positive in all occupied zones
- DOAS OA flow vs ASHRAE 170 minimum (verify compliance during all modes)
- Zone temperature deviation from setpoint during recovery from setback (target: within ±2°F within 15 minutes)
- Fan energy (kWh) by system — verify net fan energy reduction after decoupled OA optimization

## M&V Plan
**Option B (Retrofit Isolation — Subsystem Level)** per IPMVP; Option C for whole-building validation where subsystem metering is unavailable

**Quantification approach:**
- Baseline: 12 months of reheat energy (BTU from hot water or steam metering) and simultaneous heating/cooling valve positions; characterize baseline SAT reset range and zone airflow during unoccupied periods
- Post-implementation: Measure reheat energy monthly; track SAT reset range and zone airflow setback performance; normalize for weather (HDD/CDD) and clinical occupancy (patient count, OR schedule)
- Calculate avoided reheat energy: baseline reheat intensity (per HDD) − post-implementation reheat intensity (per HDD) × post HDD
- Apply fan energy correction: verify net fan energy reduction after decoupled OA optimization

**Data collection:**
- Zone-level reheat valve position (%) and heating coil energy (BTU/hr) at 15-minute intervals
- Zone-level cooling valve position (%) and cooling coil energy (BTU/hr) at 15-minute intervals
- Supply air temperature reset (°F) by AHU at 15-minute intervals
- Zone airflow (CFM or % of peak flow) at 15-minute intervals during occupied and unoccupied periods
- Building pressure relative to outdoors (in. WC) at key locations
- OA flow rate by AHU (CFM) vs ASHRAE 170 minimum requirement
- Outside air temperature, humidity, HDD, CDD for normalization
- Patient count or OR procedure count as clinical occupancy proxy

## Costs & Payback (Indicative)
- **Capex**: DOAS addition or modification: £80,000–250,000 for large hospital central plant; BAS controls reprogramming and integration: £30,000–80,000; metering and commissioning: £15,000–40,000
- **Opex**: Annual SAT reset optimization review and DOAS filter replacement: £3,000–8,000/year
- **Simple payback**: 3–7 years in large hospitals with high reheat loads; strategic measure with high persistence value
- **ROI**: One of the highest-impact hospital HVAC ECMs — addresses simultaneous heating/cooling waste, excess ventilation, and poor SAT reset simultaneously

## Templates / Reuse
*Boilerplate footer removed. Reference ASHRAE 90.1 §6.5, ASHRAE 170-2017, and CIBSE Guide B for decoupled OA design guidance.*
