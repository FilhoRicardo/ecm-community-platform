---
Main System: "[[Guestroom Controls]]"
Category System: "[[HVAC Controls]]"
Utility Affected: "[[Electricity and Gas]]"
Source Document: "[[AEDG30-HighwayLodging.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Guestroom Occupancy-Based Setback and Unoccupied Recovery

## Summary
Use occupancy sensing, door switch logic, or PMS integration to place guestroom HVAC into setback/setup mode when rooms are vacant while preserving fast recovery on check-in or return.

## Estimated Savings
- **Typical effect**: one of the most practical lodging control measures because vacancy is predictable and frequent.
- **End-Uses Affected**: guestroom heating, cooling, and fan energy.

## Basis / References
- The lodging AEDG emphasizes reducing loads first and controlling equipment in practical, repeatable ways.
- Occupancy-based control aligns with the guide’s quality-assurance and right-sizing logic.

## Assumptions
Requires reliable vacancy signal and reasonable recovery time. Works best where rooms are often unoccupied for extended periods.

## Climate Zone Relevance
All climate zones.

## Interaction Notes
Amplifies efficient unitary equipment upgrades and better envelope performance. Overlaps partly with thermostat band tightening.

## Implementation Essentials
- Define occupied, rented-vacant, and unrented room control states.
- Use moderate setbacks rather than excessive drift that creates guest complaints.
- Integrate with PMS where possible; otherwise use door/occupancy logic.
- Trend overrides and nuisance comfort events after rollout.

## Risks / Constraints
- Aggressive setbacks can create poor first impression at check-in.
- Sensor faults or housekeeping workflows can cause false vacancy.

## KPIs
- HVAC runtime in vacant rooms
- Recovery time to target temperature
- Occupied vs unrented room energy
- Comfort complaints at check-in

## M&V Plan
- Compare guestroom energy by occupancy state pre/post implementation.
- Normalize for weather and occupancy.

## Costs & Payback (indicative)
- Usually favorable because controls cost is modest relative to room count savings.


## Templates / Reuse
- ECM screening worksheet
- Climate-zone applicability note
- KPI / M&V checklist
