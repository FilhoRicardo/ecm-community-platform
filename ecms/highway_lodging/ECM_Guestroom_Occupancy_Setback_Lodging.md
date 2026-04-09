---
Main System: "[[Guestroom Controls]]"
Category System: "[[HVAC Controls]]"
Utility Affected: "[[Electricity and Gas]]"
Source Document: "[[AEDG30-HighwayLodging.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Guestroom Occupancy-Based Setback and Unoccupied Recovery

## Summary
Use occupancy sensing, door switch logic, or PMS integration to place guestroom HVAC into setback or setup mode when rooms are vacant, while preserving fast recovery to comfort conditions on check-in or guest return. In limited-service highway lodging where average occupancy rates are 55–70%, this measure can reduce guestroom HVAC energy by 15–30% without degrading guest comfort (CIBSE Guide H:2019, Table 6.3 — Occupancy-Based Control Savings Estimates).

## Estimated Savings
- **HVAC energy reduction in vacant rooms**: 15–30% of guestroom HVAC kBtu consumption in limited-service properties with occupancy rates of 55–70% (CIBSE Guide H:2019, Table 6.3).
- **Fan energy reduction**: 30–50% reduction in PTAC/PTHP standby fan energy through fan-delay-off or vacating logic.
- **End-Uses Affected**: guestroom heating, cooling, and fan energy.

## Basis / References
**CIBSE**
- CIBSE Guide H:2019, Table 6.3: Occupancy-Based HVAC Control Savings Estimates for Hotels — indicates 15–30% HVAC energy reduction for limited-service properties with occupancy-based setback, with highest savings in properties with occupancy rates below 65%.

**ASHRAE**
- ASHRAE 90.1-2019 Section 6.4.2: Maximum Fan Power — requires fan systems to have automatic shutoff controls for unoccupied periods.
- ASHRAE 90.1-2019 Section 6.4.3: Ventilation Controls — requires outdoor-air dampers to close when system is in unoccupied mode.
- ASHRAE Standard 100-2018 Section 5.4.2: Hotel Guest Room HVAC Controls — requires automatic setback/setup based on occupancy with manual override capability.

**Other**
- AEDG30-HighwayLodging.pdf: Identifies occupancy-based control as one of the most practical lodging control measures, aligned with the guide's quality-assurance and right-sizing logic.

## Assumptions
- Guestrooms are conditioned by individual PTAC/PTHP or similar unitary equipment with external control capability (24V relay or network integration).
- Property management system (PMS) provides occupancy-state signals (check-in/check-out) or can be integrated with door-card access.
- Average occupancy rate is between 55–75% (typical limited-service highway lodging); savings increase as occupancy rate decreases.
- Setback temperature differential is limited to ±4–6°F from occupied setpoint to ensure acceptable recovery time (< 20 minutes to within 2°F of occupied setpoint).

## Climate Zone Relevance
- **Cold climates (Zones 5–8)**: Highest absolute savings from heating setback, as setback periods accumulate more degree-hours; recovery heating load after setback is lower than continuous maintenance heating.
- **Hot climates (Zones 1–3)**: Cooling setback provides significant savings in warm-humid seasons; dehumidification during vacancy can be deferred.
- **Mixed climates (Zones 4)**: Both heating and cooling setback provide savings; the measure is valuable year-round.

## Interaction Notes
- Amplifies efficient unitary equipment upgrades: a high-efficiency PTAC/PTHP operating in occupancy-based setback achieves 20–35% more savings than the same unit without setback.
- Works best after envelope air sealing: reduced infiltration means the room temperature drifts more slowly during setback, maintaining guest comfort on re-entry without excessive recovery energy.
- Overlaps with thermostat band tightening (reducing the deadband from ±4°F to ±2°F reduces simultaneous heating and cooling in partially occupied rooms).
- PMS integration provides a cleaner vacancy signal than door switches, which can produce false positives when housekeeping enters rooms.

## Implementation Essentials
1. Define three explicit room control states with documented setpoints and transition logic:
   - **Occupied**: cooling setpoint 68–72°F (summer), heating setpoint 68–72°F (winter), fan auto.
   - **Rented-Vacant** (guest checked in but not present): cooling setpoint 78°F / heating setpoint 60°F, fan on-demand only (no continuous fan), OA damper closed.
   - **Unrented** (room available but not occupied): deeper setback, cooling 82°F / heating 55°F, fan off, OA damper closed.
2. Integrate with PMS for check-in/check-out signals where available (preferred): use the PMS room-status change as the primary occupancy trigger, supplemented by door-card or PIR occupancy sensor for in-room presence detection.
3. Where PMS integration is unavailable: install door-card switches (magnetic contact on door frame) or passive infrared (PIR) occupancy sensors; use a timer to differentiate "rented-vacant" from "unrented" states.
4. Limit temperature setback to ±4–6°F from occupied setpoint: aggressive setbacks (> 8°F in cold climates) can cause guest discomfort on return and increase recovery loads, partially offsetting savings.
5. Configure recovery logic: on occupancy detection, begin recovery at a rate limited to avoid compressor short-cycling (maximum 3°F/minute recovery ramp for heat pump units); target recovery to within 2°F of occupied setpoint within 15 minutes.
6. Disable manual extreme setpoint overrides: lock thermostat range to 60–82°F with guest-adjustable ±2°F from base setpoint; require FM authorization to change locked range.
7. Commission and trend-verify: after installation, trend room temperature, HVAC runtime, and occupancy state for 30 days; confirm setback activation rate, recovery performance, and guest override frequency.
8. Train front-desk and engineering staff on the logic: ensure that housekeeping supervisors understand that HVAC setback is normal operation and that they should not defeat the controls by holding doors open or disabling sensors.

## Risks / Constraints
**Failure Mode — Aggressive Setback Causing Recovery Overload**: A setback of more than 10°F in cold climates can cause high heating demand spikes on re-occupancy, particularly with heat pump units that have limited reheat capacity at low outdoor temperatures.

**Mitigation**: Limit setback to ±6°F maximum; use a heat-pump-compatible recovery ramp (not electric resistance strip); validate recovery performance with field measurement during commissioning at worst-case outdoor temperature.

**Failure Mode — Sensor False Positives from Housekeeping**: PIR sensors can be triggered by housekeeping staff cleaning a vacant room, causing premature termination of setback and loss of savings for the remainder of the cleaning period.

**Mitigation**: Use a door-card system for rented-vacant detection (guest has checked in but is not present); PIR sensors only for in-room presence override; configure a 10–15 minute occupancy delay before setback terminates to prevent cleaning-triggered setbacks.

**Failure Mode — PMS System Doesn't Propagate Room Status Changes**: Integration failures between PMS and HVAC controls cause rooms to remain in occupied mode indefinitely after checkout, losing setback savings for multiple day-nights.

**Mitigation**: Set a PMS timeout: if no new occupancy is detected within 30 minutes of check-out signal, force room to unrented setback state regardless of PMS status; alert engineering to PMS-HVAC integration faults within 2 hours.

## KPIs
- HVAC runtime in vacant rooms (hours/day per room) — target: reduction of ≥ 40% compared to pre-implementation baseline.
- Recovery time from setback to occupied setpoint (minutes) — target: < 15 minutes to within 2°F of occupied setpoint.
- Occupied vs. unrented room energy ratio (kBtu/room-night) — target: ≥ 25% reduction in unrented room HVAC energy per room-night vs. pre-implementation.
- Guest comfort complaints at check-in (per 100 arrivals) — target: < 1.0 complaints per 100 arrivals related to room temperature on arrival.
- HVAC override count per 100 room-nights — target: < 2 overrides/100 room-nights from manual thermostat adjustment.
- PTAC/PTHP standby fan runtime reduction (%) — target: ≥ 50% reduction in fan runtime in unrented rooms.

## M&V Plan
- **IPMVP Option**: Option D (Calibrated Simulation) supplemented by Option C (Whole Building) — use room-block metered energy and weather normalization for the overall savings estimate; use trend data from a representative room sample for persistence verification.
- **Quantification approach**: Select a representative sample of 10–20 guestrooms with trending capability; compare HVAC runtime and energy consumption by occupancy state pre/post implementation; normalize for weather (HDD/CDD) and occupancy rate using the ASHRAE 90.1-2019 Appendix D normalization procedure. Extrapolate to whole-building estimate using room count and occupancy distribution.
- **Data collection**:
  - HVAC unit runtime by control state (BAS trend or data logger, 15-minute resolution, minimum 60 days pre and 60 days post).
  - Room temperature by control state (trend log, 15-minute resolution).
  - PMS occupancy state (check-in/check-out timestamps, daily export).
  - Outdoor air temperature (local weather station, hourly).
  - Monthly utility consumption by fuel type for treated room block.
  - Guest complaint log (room temperature on arrival, categorized by severity).

## Costs & Payback (indicative)
- **Capex**: $180–$350 per room for occupancy sensor/door card + relay/controller + integration commissioning; $18,000–$35,000 per 100-room property.
- **PMS integration additional cost**: $3,000–$12,000 if not already available (software integration or gateway).
- **Opex**: $800–$1,500/year for software integration maintenance, sensor replacement, and annual performance review.
- **Simple Payback**: 2.5–5.5 years for a 100-room property with 60–65% average occupancy, based on HVAC energy savings of 3,500–7,500 kBtu/room/year and fan runtime savings of 200–500 kWh/room/year.
- **ROI**: 18–40% over 5 years.

## Templates / Reuse
ASHRAE Standard 100-2018 Appendix C — HVAC Controls Sequence Verification Template and CIBSE Guide H:2019 Appendix 6.A — Hotel Occupancy Control Savings Estimation Worksheet provide standardized formats for sequencing documentation and savings estimation for occupancy-based guestroom HVAC controls.
