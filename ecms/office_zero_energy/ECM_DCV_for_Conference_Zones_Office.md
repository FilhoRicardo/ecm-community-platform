---
Main System: "[[Ventilation Controls]]"
Category System: "[[HVAC Controls]]"
Utility Affected: "[[Heating and Cooling]]"
Source Document: "[[AEDGZE-SmallMedOfc-2019-20190614.pdf]]"
Style Benchmark: "[[Uploaded Office ECM Examples]]"
---

# ECM: Demand-Controlled Ventilation for Conference and Variable-Density Zones

## Summary
Use CO₂-based or equivalent demand-controlled ventilation in office zones with highly variable occupancy to reduce unnecessary outside-air conditioning.

## Estimated Savings
- **ASHRAE AEDG basis**: variable-density ventilation reduction strategy rather than an across-the-board office control.
- **Typical effect**: strongest in conference rooms, training rooms, and intermittently dense collaboration spaces.
- **End-Uses Affected**: ventilation heating/cooling and fan energy.

## Basis / References
- AEDGZE Small to Medium Office HVAC/control logic supports occupancy-responsive ventilation where suitable.
- The uploaded CO₂-DCV examples establish the preferred implementation detail for this ECM style.

## Assumptions
Only suitable where occupancy varies materially and the ventilation system can respond stably.

## Climate Zone Relevance
All climate zones; strongest in climates with high outdoor-air conditioning cost.

## Interaction Notes
Works well with DOAS, zone occupancy controls, and meeting-room conditioning logic.

## Implementation Essentials
- Target conference, training, and high-variance density areas first.
- Use calibrated sensors and define minimum ventilation floors clearly.
- Tune proportional response to avoid hunting or chronically elevated CO₂ levels.
- Trend CO₂, OA position, and occupancy patterns after commissioning.

## Risks / Constraints
- Poor sensor calibration or placement can compromise IAQ.
- Systems with weak turndown or poor zoning may not realize the expected benefit.

## KPIs
- Zone CO₂ ppm versus setpoint
- Outdoor-air fraction/runtime
- Ventilation-related HVAC energy
- IAQ complaints in controlled zones

## M&V Plan
- Use BAS trends for CO₂, airflow/OA position, and occupancy where available.
- Compare ventilation energy in target zones before and after implementation where practical.

## Costs & Payback (indicative)
- Moderate, best justified in variable-density spaces rather than universal deployment.

