---
Main System: "[[Ventilation]]"
Category System: "[[Ventilation]]"
Utility Affected: "[[Heating and Cooling]]"
Source Document: "[[AEDG30-HighwayLodging.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Guestroom and Bathroom Ventilation Optimization

## Summary
Reduce unnecessary outside-air and exhaust fan energy while maintaining moisture control and IAQ in guestrooms, bathrooms, and corridors. In highway lodging with intermittent occupancy, ventilation settings designed for continuous full occupancy can waste 20–40% of fan and conditioning energy with no measurable IAQ benefit (ASHRAE 62.1-2019 Section 6.2 — Ventilation Rate Procedure).

## Estimated Savings
- **Exhaust fan runtime reduction**: 25–60% reduction in bathroom exhaust fan kWh through demand-based scheduling and intermittent operation.
- **Ventilation heating/cooling reduction**: 10–20% reduction in perimeter ventilation loads through OA damper scheduling and pressurization control (CIBSE Guide B:2019, Section 5.4).
- **End-Uses Affected**: exhaust fan electricity, outside-air heating and cooling, corridor pressurization.

## Basis / References
**CIBSE**
- CIBSE Guide B:2019, Section 5.4: Demand-controlled ventilation strategies and intermittent exhaust scheduling — indicates 20–40% fan energy reduction potential in intermittent-occupancy buildings.

**ASHRAE**
- ASHRAE 62.1-2019 Table 6.2.2.1: Minimum Ventilation Rates in Liters per Second per Person for Hotel/Motel Guest Rooms — requires 2.5 L/s·person (5 cfm/person) for guest rooms and 10 L/s·person (20 cfm/person) for bathrooms during occupancy.
- ASHRAE 62.1-2019 Section 6.2.5.2: ASHRAE 62.1-2019 allows occupant-sensor-driven ventilation reduction during unoccupied periods for hotel guest rooms, reducing to 0.5 L/s·person during unoccupied periods.
- ASHRAE 90.1-2019 Section 6.4.9: Kitchen and Bath Exhaust — requires intermittent exhaust controls and minimum 5 ACH purge for bathrooms during unoccupied periods.

**Other**
- AEDG30-HighwayLodging.pdf: Treats ventilation control as a "bonus savings" area, emphasizing quality assurance and commissioning to ensure poor ventilation settings do not erode other ECM savings.

## Assumptions
- Bathrooms have dedicated exhaust fans (either inline or integral to PTAC/PTHP) with simple continuous or time-clock control.
- Guestroom OA is supplied via PTAC/PTHP outdoor-air intake or corridor pressurization, not a dedicated DOAS.
- Property is not subject to re-circulating single-pass exhaust hood requirements (those apply to kitchen exhaust, not guestroom bathrooms).

## Climate Zone Relevance
- **Hot-humid climates (Zones 1–3)**: Highest value from reducing latent load associated with unnecessary OA intake; exhaust fan runtime reduction directly reduces moisture removal load.
- **Cold climates (Zones 6–8)**: Highest value from reducing heating energy associated with OA intake; demand-controlled exhaust reduces heated infiltration losses.
- **Mixed climates (Zones 4–5)**: Both heating and dehumidification benefits apply; demand-controlled exhaust provides the most year-round value.

## Interaction Notes
- Supports corridor pressurization strategy: reducing guestroom exhaust during vacancy reduces the demand for makeup air from corridors, allowing corridor pressurization fans to operate at lower speed.
- Complements occupancy-based HVAC setback: when guestroom HVAC is in setback, exhaust fans should also reduce to maintain positive pressure relative to the corridor.
- Pairs with envelope air sealing: reduced infiltration from sealing makes demand-controlled exhaust more effective by reducing the baseline exfiltration rate that fans must compensate.

## Implementation Essentials
1. Audit current exhaust fan runtime using a runtime meter or current transformer (CT) logger on each bathroom fan circuit; record 7 consecutive days of runtime including weekend patterns to capture vacancy periods.
2. Verify bathroom pressure relationship with a manometer: during occupied operation, bathrooms should be slightly negative relative to the guestroom (-5 to -15 Pa) to capture odors and moisture; during unoccupied periods, exhaust can reduce to purge rate (5 ACH per ASHRAE 62.1-2019 Section 6.2.5.2) or be intermittent.
3. Install occupancy or door-switch sensors in each guestroom bathroom: trigger full exhaust on occupancy detection; reduce to intermittent purge (5-minute on / 15-minute off cycle) during vacancy.
4. For PTAC/PTHP units with integral OA intakes: install motorized OA dampers linked to the occupancy sensor so that OA intake matches the reduced ventilation rate during vacancy (reduce from 5 cfm/person to 0.5 cfm/person per ASHRAE 62.1-2019 Section 6.2.5.2).
5. Where corridors are pressuriized: adjust supply fan speed or relief fan speed to maintain corridor-to-guestroom differential of +3 to +8 Pa during occupied hours and +5 to +10 Pa during unoccupied hours; rebalance after exhaust reduction changes.
6. Commission the pressure relationships seasonally: verify that bathroom exhaust reduction does not cause moisture accumulation in guestrooms during high-occupancy periods or create odor transfer between adjacent rooms.
7. Set up trend logs for exhaust fan runtime, PTAC/PTHP OA damper position, and corridor differential pressure.

## Risks / Constraints
**Failure Mode — Moisture Accumulation and Mold**: Insufficient exhaust during high-occupancy periods (back-to-back room stays, high humidity activities) can lead to moisture accumulation in bathroom finishes and PTAC coils, creating mold and IAQ issues.

**Mitigation**: Ensure occupancy-triggered exhaust provides full design exhaust rate (≥ 10 L/s per bathroom per ASHRAE 62.1-2019); validate that purge cycle removes residual moisture between stays by monitoring relative humidity trends in treated bathrooms.

**Failure Mode — Odor Transfer Between Rooms**: If exhaust reduction creates positive pressure in guestrooms relative to bathrooms or corridors, odors from neighboring rooms or corridor service areas can migrate into the guestroom.

**Mitigation**: Maintain bathroom negative pressure relative to guestroom at all times during occupancy; test pressure relationships with tracer gas or manometer at maximum and minimum exhaust flow conditions; install backdraft dampers on exhaust outlets if needed.

**Failure Mode — Corridor Pressurization Imbalance**: Reducing guestroom exhaust can increase corridor pressurization if supply systems are not adjusted, causing corridor door difficult-to-close conditions or excessive infiltration into guestrooms.

**Mitigation**: Rebalance corridor supply and relief systems after exhaust changes; install corridor pressure monitoring (continuous manometer logging) for 30 days post-commissioning.

## KPIs
- Exhaust fan runtime (hours/day per bathroom) — target: reduction of ≥ 40% from baseline average daily runtime.
- Occupied vs. unoccupied exhaust runtime ratio — target: ≥ 60% of total daily exhaust occurs during occupied periods.
- Bathroom relative humidity (% RH) — target: < 65% RH during occupied periods; < 80% RH during purge cycle (no condensation on mirrors within 15 minutes of occupancy end).
- Corridor differential pressure (Pa) — target: +3 to +8 Pa (occupied), +5 to +10 Pa (unoccupied) relative to adjacent guestrooms.
- Guest bathroom/moisture-related complaints per 100 room-nights — target: < 0.2 complaints/100 room-nights.

## M&V Plan
- **IPMVP Option**: Option B (Modified Component Isolation) — isolate exhaust and ventilation system impacts with dedicated sub-metering.
- **Quantification approach**: Measure exhaust fan kWh and OA conditioning energy before and after demand-control installation; normalize for occupancy and weather. Apply ASHRAE 90.1-2019 Appendix D weather normalization to heating/cooling energy. Calculate fan energy reduction using fan power (kW) × runtime (hours) difference.
- **Data collection**:
  - Exhaust fan runtime (CT logger, 15-minute resolution, minimum 30 days pre and 30 days post).
  - Exhaust fan kWh (dedicated kWh meter or estimated from fan nameplate kW × runtime).
  - Guestroom occupancy state (PMS or door-switch log, daily).
  - Outside-air temperature and humidity (local weather station data for HDD/CDD; local sensor for humidity verification).
  - Corridor differential pressure (continuous manometer log, 15-minute resolution, 30 days post-commissioning).

## Costs & Payback (indicative)
- **Capex**: $150–$400 per guestroom for occupancy sensor and relay/controller ($120–$250), motorized OA damper retrofit on PTAC/PTHP ($150–$350 if needed); $15,000–$40,000 per 100-room property.
- **Opex**: $500–$1,000/year for annual balancing and pressure relationship verification.
- **Simple Payback**: 2.5–5.5 years for a 100-room property, based on exhaust fan energy savings of 400–900 kWh/room/year and ventilation heating/cooling savings of 1,500–3,500 kBtu/room/year.
- **ROI**: 18–40% over 5 years.

## Templates / Reuse
ASHRAE Standard 62.1-2019 Appendix A — Ventilation Rate Procedure Calculation Worksheet and ASHRAE Standard 100-2018 Appendix D — Exhaust and Ventilation System Verification Checklist provide standardized formats for demand-controlled ventilation design verification and ongoing commissioning.
