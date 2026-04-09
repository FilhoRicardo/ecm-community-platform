---
Main System: "[[Domestic Hot Water]]"
Category System: "[[Hot Water]]"
Utility Affected: "[[Gas and Electricity]]"
Source Document: "[[AEDG30-HighwayLodging.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Lodging Domestic Hot Water Plant Optimization

## Summary
Optimize central domestic hot water generation, storage, recirculation, and setpoint management to reduce one of the most persistent end uses in highway lodging, which typically accounts for 8–15% of total building energy use in motels and limited-service hotels (AEDG30-HighwayLodging.pdf, Section 4 — Service Water Heating).

## Estimated Savings
- **DHW fuel reduction**: 10–25% of central DHW plant energy through setpoint tuning, recirculation optimization, and insulation improvements (CIBSE Guide F:2019, Table 4.2 — DHW system efficiency measures).
- **Recirculation pump electricity**: 20–50% reduction in recirculation pump runtime through controls scheduling and variable-speed drive installation.
- **End-Uses Affected**: DHW fuel, recirculation pump electricity, and parasitic losses from uninsulated piping.

## Basis / References
**CIBSE**
- CIBSE Guide F:2019, Table 4.2: DHW system efficiency measures including setback scheduling, pump cycling, pipe insulation, and dead-leg elimination — indicates typical saving of 10–25% for central systems.
- CIBSE Guide G:2019, Section 5.3: Hot water recirculation system design and control — addresses optimal recirculation temperature differential (ΔT) of 10–15°F.

**ASHRAE**
- ASHRAE 90.1-2019, Section 7.4.7: Service Water Heating — requires shower heads ≤ 2.0 gpm and specifies minimum water heater efficiency by fuel type.
- ASHRAE Handbook — HVAC Systems and Equipment, Chapter 50: Service Water Heating — provides sizing guidance and distribution loss estimation procedures.

**Other**
- AEDG30-HighwayLodging.pdf, Section 4: Service Water Heating — treats DHW as a core recommendation area in highway lodging, emphasizing practical measures suited to small and mid-size properties.

## Assumptions
- Property has a central DHW plant (gas-fired or electric) serving guestroom and support-area loads.
- Baseline recirculation is continuous or operates on a simple time clock with no variable-speed control.
- Minimum delivery temperature of 110°F (140°F for sanitizing rinse per NSF/ANSI 170) is maintained at all times.

## Climate Zone Relevance
All climate zones. Hot-humid climates benefit most from reduced recirculation heat gain entering conditioned spaces; cold climates benefit most from distribution loss reduction and shorter recovery periods.

## Interaction Notes
- Pairs with low-flow fixture upgrades (shallower hot-water draw per flush reduces recirculation frequency).
- Complements laundry heat recovery if the property has on-site washers.
- DHW setpoint reductions reduce both plant efficiency and distribution losses; validate that dishwashing and sanitizing requirements are met at lower setpoints.
- Occupancy-based setback of DHW plant (overnight temperature reduction to 100°F) is viable in limited-service properties where check-in hours are predictable.

## Implementation Essentials
1. Audit the DHW plant: record heater efficiency (thermal efficiency or AFUE from nameplate), storage tank volume, recovery rate (Btu/hr), and actual setpoint vs. design setpoint.
2. Measure return-water temperature on the recirculation return leg — target a ΔT of 10–15°F across the recirculation loop; a return temperature above 115°F indicates unnecessary continuous circulation.
3. Install timer or occupancy-scheduled recirculation pump control: minimum runtime only during check-in hours (typically 06:00–23:00 for limited-service properties) with a 15-minute lead time before first expected draw.
4. Add variable-speed drive to recirculation pump if flow is constant; reduce to minimum flow required to maintain return temperature at design ΔT.
5. Insulate all accessible piping in the recirculation loop to minimum R-3 (ASHRAE 90.1-2019 Table 6.8.2); prioritize horizontal run piping in unconditioned spaces.
6. Eliminate dead-legs: map all branch piping that serves rarely used outlets; remove or consolidate where possible to reduce thermal buffer losses.
7. Adjust heater setpoint to the minimum consistent with guest comfort and code requirements (typically 120–130°F for guestroom delivery); validate at the furthest outlet monthly.
8. If the property has an on-site laundry, evaluate drain-water heat recovery (DWHR) units on the highest-volume wash drain cycles — can recover 20–35% of DHW heating energy in laundries running > 8 loads/day (CIBSE Guide F, Section 4.4).

## Risks / Constraints
**Failure Mode — Legionella Growth**: Reducing recirculation or lowering setpoints below 110°F at any point in the system creates conditions favorable to Legionella pneumophila colonization in tank sediment and dead-leg piping.

**Mitigation**: Maintain storage tank temperature ≥ 140°F; use a thermostatic mixing valve (ASSE 1017-rated) at the plant outlet to deliver ≤ 120°F to guestroom branches; never reduce return water below 110°F at the heater inlet; conduct quarterly thermal shock to 165°F if occupancy is intermittent.

**Failure Mode — Guest Complaint Spike**: Over-aggressive setback during late-night hours causes cold water at shower on early-morning check-ins before recirculation restores temperature.

**Mitigation**: Use a compensated setback schedule that restores temperature 30 minutes before first expected occupancy; monitor return temperature trends and adjust lead time seasonally.

**Failure Mode — Piping Heat Loss in Conditioned Spaces**: Uninsulated DHW piping in corridors and mechanical rooms adds heat load to air-conditioned spaces in summer, partially offsetting DHW savings.

**Mitigation**: Insulate all piping in conditioned spaces to at least R-3; prioritize recirculation loop and horizontal run segments.

## KPIs
- DHW plant energy per occupied room-night (kBtu/room-night or kWh/room-night) — target: 15–30% reduction from baseline post-optimization.
- Recirculation return temperature (°F) — target: maintain return ≤ 115°F during scheduled off-hours; ΔT ≥ 10°F across loop during operation.
- Recirculation pump runtime (hours/day) — target: reduction of ≥ 40% from pre-control-optimization baseline.
- Hot-water delivery temperature at furthest outlet (°F) — target: ≥ 110°F within 30 seconds of draw start.
- DHW-related guest complaints (per 100 room-nights/month) — target: < 0.5 complaints/100 room-nights/month.

## M&V Plan
- **IPMVP Option**: Option B (Modified Component, Isolation) — isolate DHW plant and recirculation system from other building loads with dedicated metering.
- **Quantification approach**: Install a dedicated BTU meter or gas flow meter on the DHW plant and a kWh meter on the recirculation pump; compare pre/post 12-month normalized consumption, normalized for occupancy (room-nights occupied).
- **Data collection**:
  - DHW plant gas consumption (therms/month) or electric element kWh (for electric resistance or heat pump systems).
  - Recirculation pump kWh (monthly from sub-meter or estimated from pump curve and runtime).
  - Return water temperature (continuous trend log, 15-minute resolution).
  - Hot-water setpoint (record quarterly).
  - Occupied room-nights per month (from PMS).
  - HDD for weather normalization if plant efficiency varies seasonally.

## Costs & Payback (indicative)
- **Capex**: $1,500–$6,000 for recirculation pump VSD ($800–$2,500), timer control upgrade ($300–$800), piping insulation ($400–$1,500), and dead-leg elimination labor ($500–$1,500).
- **Opex**: $300–$600/year for quarterly return-temperature validation and annual heater inspection.
- **Simple Payback**: 1.5–3.5 years for a 100-room property, based on DHW energy savings of $1,200–$3,500/year (at $0.80–$1.20/therm and typical DHW consumption of 15,000–25,000 therms/year for 100 rooms).
- **ROI**: 28–65% over 5 years.

## Templates / Reuse
CIBSE Guide F:2019, Appendix F.A — Domestic Hot Water System Audit Worksheet provides a standardized format for DHW plant assessment and baseline documentation applicable to highway lodging and similar small hospitality property types.
