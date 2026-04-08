---
Main System: "[[Procedure Spaces]]"
Category System: "[[HVAC Controls]]"
Utility Affected: "[[Heating and Cooling]]"
Source Document: "[[AEDG50-LargeHospitals-2012.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Airflow Setback in Surgery and Procedure Spaces

## Summary
Reduce airflow in surgery and other procedure areas during approved unoccupied modes while preserving readiness, pressure relationships, and infection-control requirements.

## Estimated Savings
- **AEDG basis**: explicitly called out in the large-hospital guide as an additional HVAC strategy.
- **Typical effect**: strong savings in fan energy and reheat for high-air-change spaces with long unoccupied periods.
- **End-Uses Affected**: fan energy, ventilation conditioning, and reheat.

## Basis / References
- The large-hospital AEDG specifically references surgery-suite airflow setback.
- This measure is hospital-specific and must be handled through operational protocol, not just BAS programming.

## Assumptions
Only suitable where codes, accreditation, and clinical operations permit setback with documented recovery procedures.

## Climate Zone Relevance
All climate zones.

## Interaction Notes
Supports decoupled ventilation and reheat reduction but requires tighter operational governance than normal office-style scheduling.

## Implementation Essentials
- Define eligible room states and recovery times with clinical leadership.
- Tie setback logic to room status, scheduling, or procedural readiness.
- Trend pressure, airflow, and recovery performance.
- Include infection-control and perioperative signoff before activation.

## Risks / Constraints
- Misapplication can create safety/compliance concerns.
- Staff workarounds can permanently disable the sequence.

## KPIs
- Airflow in occupied vs setback mode
- Reheat energy in procedure areas
- Recovery time to full ready state
- Pressure/alarm events

## M&V Plan
- Trend room status, airflow, and reheat pre/post implementation.
- Review recovery tests during commissioning and periodic drills.

## Costs & Payback (indicative)
- Low to moderate controls cost with potentially high savings in high-airflow spaces.


## Templates / Reuse
- ECM screening worksheet
- Climate-zone applicability note
- KPI / M&V checklist
