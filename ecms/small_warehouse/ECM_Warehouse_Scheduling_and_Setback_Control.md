---
Main System: "[[Scheduling]]"
Category System: "[[HVAC Controls]]"
Utility Affected: "[[Heating and Cooling]]"
Source Document: "[[AEDG30-SmallWarehouse-2008.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Warehouse Scheduling, Setback, and Preoccupancy Control

## Summary
Use time-of-day scheduling and temperature setback/setup so conditioned warehouse and office areas are not held at full comfort conditions when unoccupied.

## Estimated Savings
- **Typical effect**: practical HVAC savings where operating hours are predictable and after-hours use is limited.
- **End-Uses Affected**: heating, cooling, and some ventilation energy.

## Basis / References
- The warehouse guide’s energy-goal table explicitly recommends schedules, setback/setup, and preoccupancy purge logic.
- Warehouses often have clearer schedules than offices, which improves control viability.

## Assumptions
Best where occupancy is predictable and not 24/7.

## Climate Zone Relevance
All climate zones.

## Interaction Notes
Works with thermal zoning, motorized OA dampers, and office-area controls.

## Implementation Essentials
- Separate warehouse, office, and support-area schedules where they differ.
- Use moderate setbacks that preserve recovery and operational readiness.
- Review holiday and weekend schedules explicitly.
- Trend overrides and after-hours runtime.

## Risks / Constraints
- Cleaning, shipping, or overtime patterns can undermine simple schedules.
- Too-aggressive setbacks can create morning recovery issues.

## KPIs
- After-hours HVAC runtime
- Setback hours
- Morning recovery time
- Weekend kWh/therms

## M&V Plan
- Compare off-hours energy use pre/post implementation.
- Use trend data for schedule compliance and overrides.

## Costs & Payback (indicative)
- Usually favorable because the measure is largely control-based.


## Templates / Reuse
- ECM screening worksheet
- Climate-zone applicability note
- KPI / M&V checklist
