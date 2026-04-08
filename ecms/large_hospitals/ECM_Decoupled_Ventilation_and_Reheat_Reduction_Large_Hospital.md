---
Main System: "[[DOAS]]"
Category System: "[[Ventilation]]"
Utility Affected: "[[Heating and Cooling]]"
Source Document: "[[AEDG50-LargeHospitals-2012.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Decoupled Ventilation and Reheat Reduction

## Summary
Decouple ventilation from sensible conditioning and use aggressive reset/setback logic to reduce one of the largest energy penalties in hospitals: conditioning and reheating large volumes of air.

## Estimated Savings
- **AEDG basis**: one of the central HVAC recommendations in the large-hospital guide.
- **Typical effect**: major reduction in fan, cooling, and especially reheat energy where baseline systems overdeliver air or reheat constantly.
- **End-Uses Affected**: ventilation, reheat, fan energy, cooling plant.

## Basis / References
- The large-hospital AEDG explicitly recommends advanced VAV with separate outdoor-air treatment and decoupled ventilation/zone conditioning.
- Reheat reduction is a major theme in the executive summary.

## Assumptions
Requires accurate airflow control, humidity management, and zoning discipline.

## Climate Zone Relevance
All climate zones, especially humid and extreme climates.

## Interaction Notes
Pairs with heat recovery, surgery-suite setback, and high-delta-T chilled water.

## Implementation Essentials
- Separate OA treatment from zone sensible conditioning where feasible.
- Apply aggressive SAT reset and zone-airflow setback only where clinically appropriate.
- Keep humidity control explicit, not incidental.
- Trend airflow, reheat valve position, and supply conditions after startup.

## Risks / Constraints
- Poor control can create IAQ, pressure, or humidity issues.
- Operators may disable aggressive sequences if not trained.

## KPIs
- Reheat energy
- Airflow per area type
- Fan kWh
- Humidity excursions

## M&V Plan
- Use subsystem metering and BAS trends for airflow, SAT, and reheat.
- Compare seasonal reheat intensity pre/post or against modeled baseline.

## Costs & Payback (indicative)
- Moderate to high, but often one of the most consequential hospital HVAC ECMs.


## Templates / Reuse
- ECM screening worksheet
- Climate-zone applicability note
- KPI / M&V checklist
