---
Main System: "[[Humidity Control]]"
Category System: "[[HVAC]]"
Utility Affected: "[[Cooling]]"
Source Document: "[[AEDG50-GroceryStores-2015.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Positive Pressure and Humidity Control for Grocery Comfort and Product Quality

## Summary
Maintain positive store pressure and active humidity control so customer comfort, case anti-sweat performance, and product presentation are not undermined by uncontrolled moisture.

## Estimated Savings
- **Typical effect**: protects the value of refrigeration and HVAC ECMs rather than only creating stand-alone savings.
- **End-Uses Affected**: cooling/latent energy, anti-sweat heater demand, comfort, and building durability.

## Basis / References
- The grocery guide repeatedly emphasizes humidity control and pressurization as critical interaction issues.
- This is especially important after case-door changes and kitchen/exhaust modifications.

## Assumptions
Requires humidity/dew-point sensing and active operational review.

## Climate Zone Relevance
Most important in humid climates, but still relevant everywhere.

## Interaction Notes
Supports case-door ECMs, kitchen makeup-air strategy, and refrigeration anti-sweat optimization.

## Implementation Essentials
- Control dew point, not just dry-bulb temperature.
- Maintain positive pressure during all major operating modes.
- Review entrance infiltration and kitchen exhaust impacts.
- Trend RH/dew point and anti-sweat behavior.

## Risks / Constraints
- If pressure and latent control are weak, multiple other ECMs can underperform.
- Operators may focus only on temperature and miss moisture problems.

## KPIs
- Store RH/dew point
- Pressure relationship
- Anti-sweat heater runtime
- Condensation complaints/events

## M&V Plan
- Use BAS trends for pressure and humidity.
- Compare anti-sweat and latent-related HVAC behavior before/after interventions.

## Costs & Payback (indicative)
- Low to moderate if mainly controls-based; can be higher if ventilation hardware changes are needed.


## Templates / Reuse
- ECM screening worksheet
- Climate-zone applicability note
- KPI / M&V checklist
