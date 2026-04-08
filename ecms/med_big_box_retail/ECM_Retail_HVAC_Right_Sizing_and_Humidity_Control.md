---
Main System: "[[HVAC]]"
Category System: "[[HVAC Systems and Equipment]]"
Utility Affected: "[[Heating and Cooling]]"
Source Document: "[[AEDG50-MedBigBoxRetail-2011.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: HVAC Right-Sizing with Active Humidity Control

## Summary
Right-size retail HVAC using realistic internal loads and maintain active humidity control so lower lighting and better envelope measures do not create latent-control problems.

## Estimated Savings
- **AEDG basis**: major HVAC package impact in high-performance retail.
- **Typical effect**: meaningful cooling and fan savings with improved comfort and fewer moisture issues.
- **End-Uses Affected**: cooling, fan energy, and latent control.

## Basis / References
- The retail guide warns that humidity control becomes more important as lighting loads fall and envelopes improve.
- It also emphasizes avoiding oversizing and unnecessary redundancy.

## Assumptions
Most useful where stores currently rely on conservative sizing or struggle with humidity/comfort after efficiency upgrades.

## Climate Zone Relevance
All climate zones; especially important in humid climates.

## Interaction Notes
Strong interaction with lighting reductions, economizers, ventilation control, and envelope solar gains.

## Implementation Essentials
- Recalculate loads after lighting and envelope changes rather than preserving legacy tonnage.
- Review latent capacity explicitly, not only sensible cooling.
- Maintain positive pressure and acceptable dew point.
- Trend RH/dew point alongside runtime and compressor cycling.

## Risks / Constraints
- If humidity is ignored, efficiency gains can be reversed by comfort complaints and override behavior.
- Oversizing can increase cycling and poor part-load control.

## KPIs
- Cooling kWh
- Indoor RH/dew point
- Compressor cycling rate
- Customer/staff comfort complaints

## M&V Plan
- Compare HVAC energy and humidity stability before/after rework.
- Use BAS trends for runtime, RH, and pressure.

## Costs & Payback (indicative)
- Project-specific; strongest where prior HVAC was oversized or humidity-challenged.


## Templates / Reuse
- ECM screening worksheet
- Climate-zone applicability note
- KPI / M&V checklist
