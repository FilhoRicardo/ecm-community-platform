---
Main System: "[[Heat Recovery]]"
Category System: "[[Refrigeration / HVAC]]"
Utility Affected: "[[Heating and Cooling]]"
Source Document: "[[AEDG50-GroceryStores-2015.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Refrigerant Heat Recovery for HVAC and Hot Water

## Summary
Recover refrigeration reject heat for HVAC or domestic hot-water loads so useful heat is not thrown away while separate heating systems run.

## Estimated Savings
- **AEDG basis**: major grocery-specific opportunity because refrigeration runs continuously.
- **Typical effect**: strongest where there are concurrent heating or DHW loads.
- **End-Uses Affected**: heating energy, refrigeration system interaction, and sometimes DHW.

## Basis / References
- The grocery guide includes conventional and alternative heat-recovery configurations.
- Grocery stores often have enough refrigeration runtime to make heat recovery practical.

## Assumptions
Requires usable heat sink and seasonal logic that does not excessively raise condensing pressure.

## Climate Zone Relevance
All climate zones; strongest where there are meaningful heating or hot-water loads.

## Interaction Notes
Pairs with HVAC design, kitchen loads, and hot-water strategy.

## Implementation Essentials
- Quantify simultaneous refrigeration rejection and heat demand first.
- Choose conventional or alternate configuration based on store HVAC architecture.
- Sequence heat recovery so compressor efficiency is not sacrificed excessively.
- Trend recovered heat and condensing conditions after startup.

## Risks / Constraints
- Poor control can raise refrigeration energy and erase benefit.
- Shoulder-season operation can be hard to optimize.

## KPIs
- Recovered heat energy
- Heating fuel displacement
- Condensing pressure impact
- Heat-recovery runtime

## M&V Plan
- Use temperature/flow calculations or dedicated metering for recovered heat.
- Compare heating energy before/after with normalization.

## Costs & Payback (indicative)
- Moderate to high; strongest where heating or DHW loads are substantial and continuous.


## Templates / Reuse
- ECM screening worksheet
- Climate-zone applicability note
- KPI / M&V checklist
