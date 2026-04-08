---
Main System: "[[Condensers]]"
Category System: "[[Refrigeration]]"
Utility Affected: "[[Electricity]]"
Source Document: "[[AEDG50-GroceryStores-2015.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Condenser Selection and Floating Head Pressure Optimization

## Summary
Optimize condenser type and control so the refrigeration system avoids unnecessarily high condensing pressure and fan energy.

## Estimated Savings
- **Typical effect**: meaningful refrigeration-plant electricity reduction where condensing pressure is held artificially high.
- **End-Uses Affected**: compressor and condenser fan energy.

## Basis / References
- The grocery guide dedicates content to condenser selection, condenser control, and climate-sensitive air-vs-evaporative condensing decisions.
- Head-pressure strategy is a core grocery refrigeration issue.

## Assumptions
Requires condenser type and control logic appropriate to climate, refrigerant, and maintenance capability.

## Climate Zone Relevance
All climate zones; strategy differs by climate and water constraints.

## Interaction Notes
Pairs with refrigerant choice, compressor staging, and heat recovery.

## Implementation Essentials
- Review whether air-cooled or evaporative condensing is actually best for the site.
- Use floating head pressure or equivalent optimized control where appropriate.
- Confirm condenser derating assumptions and fan staging logic.
- Trend condensing pressure against ambient conditions.

## Risks / Constraints
- Water quality/maintenance can weaken evaporative options.
- Conservative pressure setpoints are often kept unnecessarily high “for safety.”

## KPIs
- Condensing pressure vs ambient
- Compressor kWh
- Condenser fan kWh
- Heat-recovery opportunity hours

## M&V Plan
- Compare refrigeration energy and condensing pressure profile before/after tuning.
- Normalize for ambient conditions.

## Costs & Payback (indicative)
- Moderate; strong where controls rather than hardware are the main issue.


## Templates / Reuse
- ECM screening worksheet
- Climate-zone applicability note
- KPI / M&V checklist
