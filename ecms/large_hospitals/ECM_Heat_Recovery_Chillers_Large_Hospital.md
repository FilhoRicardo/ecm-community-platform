---
Main System: "[[Heat Recovery Chiller]]"
Category System: "[[HVAC Plant]]"
Utility Affected: "[[Heating and Cooling]]"
Source Document: "[[AEDG50-LargeHospitals-2012.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Heat-Recovery Chillers and Concurrent-Load Optimization

## Summary
Use heat-recovery chillers where large hospitals have persistent simultaneous heating and cooling loads, allowing waste heat to offset boiler energy.

## Estimated Savings
- **AEDG basis**: highlighted in the large-hospital guide as an advanced HVAC/plant strategy.
- **Typical effect**: strongest where reheat, DHW, or hot-water loads overlap with substantial cooling.
- **End-Uses Affected**: boiler energy, cooling plant interaction, and potentially DHW.

## Basis / References
- The large-hospital guide references heat-recovery chillers and condenser-water heat recovery as advanced plant options.
- Large hospitals often have the load diversity to justify them.

## Assumptions
Requires simultaneous load profile analysis and a hot-water sink that can use recovered heat effectively.

## Climate Zone Relevance
All climate zones.

## Interaction Notes
Pairs with decoupled ventilation, DHW optimization, and high-delta-T chilled-water strategy.

## Implementation Essentials
- Quantify hourly overlap between cooling and useful heating loads.
- Define hot-water temperature targets and sequencing logic.
- Coordinate with boiler staging and plant redundancy philosophy.
- Trend recovered heat and plant dispatch after startup.

## Risks / Constraints
- Poor load matching can reduce annual utilization.
- Control complexity is significant and must be commissioned carefully.

## KPIs
- Recovered heat energy
- Boiler fuel displacement
- Heat-recovery chiller runtime
- Plant COP / integrated efficiency proxy

## M&V Plan
- Use plant metering or flow/temperature calculations.
- Compare boiler and chiller operating profiles before/after normalization.

## Costs & Payback (indicative)
- High capex; strongest in large, reheat-heavy, continuously operating facilities.


## Templates / Reuse
- ECM screening worksheet
- Climate-zone applicability note
- KPI / M&V checklist
