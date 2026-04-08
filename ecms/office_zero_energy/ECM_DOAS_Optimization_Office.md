---
Main System: "[[DOAS]]"
Category System: "[[Ventilation]]"
Utility Affected: "[[Heating and Cooling]]"
Source Document: "[[AEDGZE-SmallMedOfc-2019-20190614.pdf]]"
Style Benchmark: "[[Uploaded Office ECM Examples]]"
---

# ECM: Dedicated Outdoor Air System Optimization

## Summary
Optimize dedicated outdoor air systems so ventilation air is conditioned efficiently and delivered reliably without overventilating or destabilizing humidity control.

## Estimated Savings
- **ASHRAE AEDG basis**: DOAS is a central enabling strategy across several office HVAC pathways.
- **Typical effect**: material where ventilation loads are meaningful and poorly handled in conventional mixed-air systems.
- **End-Uses Affected**: ventilation heating/cooling, latent control, and fan energy.

## Basis / References
- AEDGZE Small to Medium Office includes a specific DOAS section plus multiple HVAC pathways built around DOAS logic.
- The guide also includes a sidebar on air-to-air series energy recovery.

## Assumptions
Savings depend on correct outdoor-air rates, effective distribution, low leakage, and appropriate heat recovery.

## Climate Zone Relevance
All climate zones; especially valuable where ventilation loads are large relative to sensible loads.

## Interaction Notes
Pairs strongly with VRF, GSHP/WSHP, and fan-coil/chiller pathways.

## Implementation Essentials
- Keep ventilation calculations realistic and code-compliant.
- Use heat recovery where climate and exhaust streams justify it.
- Coordinate DOAS supply temperature, humidity targets, and terminal-system responsibilities clearly.
- Trend outdoor-air delivery, humidity, and heat-recovery behavior.

## Risks / Constraints
- DOAS can underperform badly if treated as a generic packaged unit without sequence rigor.
- Poor balancing or zoning can leave some areas under- or overventilated.

## KPIs
- DOAS kWh
- Outdoor-air delivery rates
- Supply-air dew point / humidity control
- Ventilation complaint count

## M&V Plan
- Use DOAS metering where available; otherwise rely on BAS trend-based M&V.
- Verify delivered outdoor air and latent performance in commissioning and early operation.

## Costs & Payback (indicative)
- Moderate to high depending on architecture; stronger value where the office is already moving toward decoupled ventilation.

