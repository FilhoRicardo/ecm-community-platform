---
Main System: "[[Lighting]]"
Category System: "[[Lighting]]"
Utility Affected: "[[Electricity]]"
Source Document: "[[AEDG30-HighwayLodging.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: LED Lighting with Guestroom and Exterior Controls

## Summary
Upgrade interior and exterior lighting to LED and apply room-level, corridor, and site controls so lighting energy falls without reducing guest experience or safety. In highway lodging, lighting typically represents 15–25% of total electricity consumption (AEDG30-HighwayLodging.pdf, Section 2 — Lighting and Electrical), and LED retrofits in guestrooms, corridors, and exterior areas routinely achieve 50–75% reduction in lighting electricity.

## Estimated Savings
- **Guestroom lighting**: 60–75% reduction in guestroom lighting kWh when replacing 35–40W incandescent or 15–18W CFL luminaires with 8–12W LED equivalents (ENERGY STAR Lamp Standards).
- **Corridor and common-area lighting**: 45–65% reduction when replacing T8 or older CFL fixtures with LED fixtures plus occupancy controls.
- **Exterior/site lighting**: 50–70% reduction when replacing metal halide, high-pressure sodium, or older LED fixtures with high-efficacy LED and astronomical time-clock scheduling.
- **Secondary cooling reduction**: 2–5% reduction in cooling energy from reduced heat gain by LED fixtures (approximately 3× reduction in heat output vs. incandescent).
- **End-Uses Affected**: interior lighting electricity, exterior/site lighting electricity, and secondary cooling load.

## Basis / References
**CIBSE**
- CIBSE Guide SL:2020, Table 3.1: LED Retrofit Savings by Space Type — indicates 55–75% lighting electricity reduction in lodging guestrooms and corridors with direct LED replacement.
- CIBSE Guide SL:2020, Section 5.2: Controls Integration — emphasizes vacancy sensing and scheduled dimming as essential to maximizing LED savings.

**ASHRAE**
- ASHRAE 90.1-2019 Table 8.2.2.1: Maximum Lighting Power Density (LPD) for Hotel/Motel Guest Rooms — maximum 8.8 W/ft² for guest rooms, 0.9 W/ft² for corridors, 0.7 W/ft² for lobbies.
- ASHRAE 90.1-2019 Section 8.4.2: Lighting Controls — requires occupancy-based controls in guestrooms and automatic scheduling in common areas.
- ASHRAE 90.1-2019 Section 8.4.3: Daylight-Responsive Controls — requires automatic daylighting controls for spaces with fenestration.

**Other**
- AEDG30-HighwayLodging.pdf, Section 2: Lighting and Electrical — treats interior and exterior lighting as core recommendation areas, emphasizing practical implementation and quality assurance rather than purely theoretical design.

## Assumptions
- Guestrooms currently use incandescent (35–40W globe/vanity), CFL (15–18W), or older T8 fluorescent fixtures.
- Corridor and common-area fixtures use 32W T8 linear fluorescent or older pin-based CFL.
- Exterior fixtures use metal halide (150–250W) or high-pressure sodium (70–150W) HID lamps.
- Property operates 24/7 with exterior lighting running dusk-to-dawn or on simple time clock.

## Climate Zone Relevance
All climate zones. Exterior lighting savings are most impactful in northern climates where winter darkness extends the operating hours of exterior lighting. Interior lighting heat-rejection benefits are most valuable in hot climates, where reducing lighting heat gain reduces cooling loads.

## Interaction Notes
- LED retrofit in guestrooms reduces PTAC/PTHP cooling load slightly (1 W of LED replaces 3 W of incandescent heat gain), improving unit efficiency and reducing morning recovery loads after occupancy setback.
- Exterior lighting controls (astronomical time clock) reduce light pollution and operating hours without reducing safety lighting adequacy.
- Corridor occupancy sensor controls are most effective when paired with the guestroom occupancy setback logic: corridor lights can remain on at reduced output during deep vacancy periods.

## Implementation Essentials
1. Inventory all luminaires by type, wattage, location, and operating hours; calculate existing lighting energy density (W/ft² by zone) and compare to ASHRAE 90.1-2019 Table 8.2.2.1 maximums.
2. Guestroom lighting:
   - Replace vanity/vanity bar fixtures: install LED fixtures with ≥ 80 CRI, 2700–3000K color temperature, and dimming capability (forward-phase dimming for compatibility with standard dimmers).
   - Replace bedside read fixtures: use directional LED (BR30 or PAR20 equivalent, 7–10W) with occupancy-vacancy switch or dimming.
   - Target ≤ 8.8 W/ft² for guestrooms per ASHRAE 90.1-2019 Table 8.2.2.1.
3. Corridor and common-area lighting:
   - Replace T8 linear fluorescent (2×32W or 1×32W) with LED wrap fixtures (20–30W) with integral occupancy sensors.
   - Install 0–10V dimming or step-dimming controls: reduce output to 30% during unoccupied hours, 100% during occupied hours.
   - Commission photosensors at all daylit corridor sections: enable daylight-responsive dimming where corridor has windows or toplit sections.
4. Exterior/site lighting:
   - Replace HID fixtures with LED area lights (50–120W LED replaces 150–250W HID) with Type III or Type V distribution suited to parking and walkway geometry.
   - Install astronomical time-clock or network-connected lighting controller: schedule dusk-to-dawn operation with a 20% output reduction during deep night hours (midnight to 5 AM) where safety allows.
   - For canopy and facade lighting: use occupancy sensor or scheduled dimming to reduce output when the property is closed (typically 11 PM – 6 AM for limited-service hotels).
5. Commissioning: verify all occupancy sensor coverage and time-delay settings; confirm dimming levels are acceptable to guests and meet brand standards; log fixture wattages post-retrofit for M&V verification.

## Risks / Constraints
**Failure Mode — LED Color Quality Complaints**: Low CRI (< 80) or incorrect color temperature (too cool at 4000K+ in guestrooms) causes guest complaints about room ambiance and triggers fixture replacement requests that add to operating costs.

**Mitigation**: Specify ≥ 80 CRI and 2700–3000K for guestrooms; require sample fixtures in 3–5 rooms before full property rollout; do not use the same product in guestrooms and corridors (corridors may use 3500–4000K).

**Failure Mode — Occupancy Sensor Nuisance Tripping in Corridors**: False activations from housekeeping carts, luggage, or hallway traffic create excessive dimming cycles that wear out fixtures faster and annoy guests.

**Mitigation**: Set sensor time-delay to 5–10 minutes (not 30 seconds); mount sensors at room entry points rather than mid-corridor; set minimum dimming level of 30% so guests are not startled by total darkness.

**Failure Mode — Exterior Lighting Reduction and Safety/Liability**: Over-aggressive exterior lighting reductions during late-night hours create dark zones that compromise guest safety and create liability exposure.

**Mitigation**: Coordinate with local security staff or management on minimum light levels; maintain full output at all building entrances, parking structures, and emergency egress paths; use uniform dimming rather than switching-off in critical safety zones.

## KPIs
- Lighting kWh by zone (guestroom, corridor, lobby, exterior) — target: ≥ 55% total lighting electricity reduction from baseline.
- Guestroom LPD (W/ft²) — target: ≤ 8.8 W/ft² per ASHRAE 90.1-2019 Table 8.2.2.1.
- Corridor lighting power (W/ft²) — target: ≤ 0.9 W/ft² per ASHRAE 90.1-2019 Table 8.2.2.1.
- Exterior lighting operating hours (hours/day) — target: ≤ 12 hours/day average (dusk-to-dawn basis) with 20% reduction during off-hours.
- Guest lighting quality complaints per 100 room-nights — target: < 0.3 complaints/100 room-nights.
- Maintenance callback rate for LED fixtures (failures/year) — target: < 1% annual failure rate.

## M&V Plan
- **IPMVP Option**: Option C (Whole Building Metered Energy) for lighting system — isolate lighting from other loads where sub-metering is available; otherwise use pre/post utility bill analysis normalized for occupancy.
- **Quantification approach**: Install dedicated lighting panel kWh meters on guestroom, corridor, and exterior lighting panels; compare 12-month pre and 12-month post normalized kWh. For small properties without panel metering, use ASHRAE 90.1-2019 Appendix F lighting power estimation procedure and apply measured fixture counts and post-retrofit wattages.
- **Data collection**:
  - Lighting panel kWh (dedicated meter, monthly read, minimum 12 months pre and 12 months post).
  - Fixture inventory with post-retrofit wattages (spreadsheet record).
  - Occupancy sensor time-delay and coverage verification (commissioning log).
  - Operating schedule for exterior lighting (time-clock or BAS schedule record).
  - Occupied room-nights per month (PMS export for normalization).
  - Annual exterior lighting runtime verification (hour meter or BAS log).

## Costs & Payback (indicative)
- **Capex**: Guestroom LED retrofit: $80–$150/room (including labor); Corridor LED + sensor: $120–$200/fixture; Exterior LED + time-clock: $400–$800/fixture for canopy/parking. Total for 100-room property: $28,000–$55,000.
- **Opex**: $500–$1,200/year for fixture replacement under warranty and sensor recalibration.
- **Simple Payback**: 2.5–4.5 years for guestroom + corridor LED retrofit; 2.0–4.0 years for exterior LED retrofit (excluding pole replacement if HID pole is reused).
- **ROI**: 22–40% over 5 years for integrated interior/exterior package.

## Templates / Reuse
ASHRAE 90.1-2019 Appendix Table 8.B: Lighting Power Density Calculation Worksheet and CIBSE Guide SL:2020 Appendix B — LED Retrofit Specification Template provide standardized formats for lighting inventory, power budget verification, and product specification for LED retrofits in lodging properties.
