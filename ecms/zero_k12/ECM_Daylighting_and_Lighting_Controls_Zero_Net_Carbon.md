---
Main System: "[[Lighting]]"
Category System: "[[Electric Lighting, Daylighting]]"
Utility Affected: "[[Electricity]]"
Source Document: "[[AEDG50-ZNC-2014.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Daylighting and Advanced Lighting Controls for Zero Net Carbon Schools

## Summary
Design classrooms and common spaces for effective daylighting using side-lighting and top-lighting strategies, pair with automatic daylight-responsive dimming controls, occupancy-based zoning, and demand-responsive lighting reduction so the ZNC school uses lighting energy as a minimal fraction of total building EUI. Combined, these strategies reduce lighting electricity by 40–65% vs. a code-minimum fluorescent system (CIBSE Guide LG:2022, Sections 4 and 6; ASHRAE 90.1-2019 Section 9).

## Estimated Savings
- **Daylight-responsive dimming**: 25–45% reduction in lighting electricity in daylit zones (classrooms, gym, library) compared to constant-output fluorescent/LED systems without daylight controls (CIBSE Guide LG:2022, Table 6.3 — Lighting Power Reduction from Daylight Harvesting).
- **Occupancy-based scheduling and shutoff**: 15–25% reduction in lighting electricity from time-based scheduling, after-hours shutoff, and occupancy sensor control in low-traffic zones (ASHRAE 90.1-2019 Section 9.4.1.2 — Occupancy Sensor Control).
- **High-reflectance ceiling and task tuning**: 5–10% additional reduction from specifying high-reflectance ceiling finishes (R c ≥ 0.90) and tuning fixture spacing to task rather than uniform layout (CIBSE Guide LG:2022, Section 4.5 — Lumen Maintenance and Spacing Criteria).
- **Demand-responsive lighting reduction**: 5–10% reduction during peak demand events (≥ 4 hours/year) when paired with building-wide demand response automation (ASHRAE 90.1-2019 Section 8.4.2 — Demand-Controlled Lighting).
- **End-Uses Affected**: interior lighting (primary), cooling energy (secondary — less lighting heat gain reduces cooling load).

## Basis / References
**CIBSE**
- CIBSE Guide LG:2022, Section 4: Daylighting Design — provides daylight factor targets (DF ≥ 2% at back of classroom, DF ≥ 5% at task plane for sidelit zones), photometric modeling guidance, and glare control criteria.
- CIBSE Guide LG:2022, Table 6.3: Lighting Power Reduction from Daylight Harvesting — indicates 30–50% lighting electricity reduction in sidelit zones and 40–65% in toplit zones with properly commissioned daylight-responsive dimming.
- CIBSE Guide LG:2022, Section 6: Lighting Controls — covers dimming curve commissioning, setpoint calibration, and sensor placement for effective daylight-responsive control.

**ASHRAE**
- ASHRAE 90.1-2019 Section 9.4.1.2: Occupancy Sensor Control — requires occupancy sensors in classrooms, conference rooms, and copy rooms; mandates automatic shutoff within 30 minutes of vacancy.
- ASHRAE 90.1-2019 Section 9.4.3: Daylight-Responsive Controls — requires automatic daylight-responsive dimming in daylight zones with connected lighting power ≥ 150W; requires continuous dimming (not step dimming) in these zones.
- ASHRAE 90.1-2019 Section 9.4.4: Demand-Controlled Lighting — requires a demand-responsive control that reduces lighting power by ≥ 30% during peak demand events.
- ASHRAE 189.3-2018 Section 7.3.4: Interior Lighting Controls — requires daylight zones to have automatic daylight-responsive controls with continuous dimming; requires demand-responsive controls for buildings > 5,000 ft².

**Other**
- AEDG50-ZNC-2014.pdf: Requires interior lighting power density ≤ 0.45 W/ft² in classrooms (compared to ASHRAE 90.1-2019 minimum); requires daylight zones in all regularly occupied spaces; recommends virtual occupancy sensors for after-hours use reduction.

## Assumptions
- Classroom and common spaces are designed with adequate window head height, glazing area, and interior reflectance to achieve minimum daylight factors per CIBSE Guide LG:2022 (DF ≥ 2% at 3 ft from window, ≥ 1% at back of room).
- The school has or will install a networked lighting control system (NLC) capable of zone-level dimming, occupancy sensing, time-scheduling, and integration with BAS for demand response.
- Existing lighting baseline is T8 or T5 fluorescent without daylight-responsive controls; connected lighting power is ≥ 0.8 W/ft² in classrooms.
- Electric utility cost: $0.08–$0.18/kWh; demand charge: $10–$25/kW-month.

## Climate Zone Relevance
- **All climate zones**: daylight-responsive controls provide lighting energy savings in all climates; however, the interaction with cooling energy is climate-dependent:
  - In Climate Zones 1–3 (cooling-dominated): reducing lighting heat gain simultaneously reduces cooling load — combined benefit of 0.15–0.30 kBtu/ft²/year additional cooling savings per W/ft² lighting reduction.
  - In Climate Zones 6–8 (heating-dominated): reducing lighting heat gain slightly increases heating load; net benefit depends on relative fuel vs. electric cost; daylight harvesting is still beneficial for primary energy but may slightly increase heating fuel.
- Top-lighting strategies (skylights, clerestories) are most effective in Climate Zones 3–7 where daylighting potential is high and clear-sky irradiance is significant.

## Interaction Notes
- Pairs with the PV/renewable ECM: reduced lighting electricity reduces the renewable generation requirement for ZNC; for every 1 kWh/day of lighting electricity saved, the PV system size required decreases by approximately 1.5–2.5 kW (depending on solar fraction and location).
- Daylight-responsive dimming reduces cooling load in summer (coupled with HVAC optimization); in winter, the same dimming may increase heating load — the building automation system should account for this interaction via supply air temperature reset or zone reheat adjustment.
- The occupant dashboard and engagement ECM benefits from lighting runtime data: visible energy dashboards showing lighting kWh by zone create behavioral incentives for teachers and students to use daylight before artificial light.
- High-reflectance ceiling surfaces increase the effectiveness of toplit daylighting strategies (skylights/clerestories) by increasing the number of inter-reflection bounces; this is a low-cost complement to glazing upgrades.

## Implementation Essentials
1. Perform a daylighting analysis using Radiance or similar simulation tool during design phase: model interior reflectance (ceiling ≥ 0.90, walls ≥ 0.70, floor ≥ 0.30), window dimensions, glazing spec (VLT ≥ 0.50, SHGC ≤ 0.40 in Climate Zones 1–3, ≤ 0.55 in Zones 4–8), and exterior obstructions; verify DF targets are met at task plane (30 in. AFF) for typical classroom geometry.
2. Specify a networked lighting control (NLC) system with: zone-level addressable dimming (minimum 16 zones per classroom), continuous dimming drivers (0–10V or DALI), integral occupancy sensors, and BAS integration via BACnet or cloud API.
3. Size and space skylights/clerestories to meet the Daylight Factor targets: for flat roof classrooms, use clerestory windows or tubular daylight devices (TDDs) on 4–6 ft centers; for sidelighting, use high windows (head height ≥ 7 ft) with light shelves to push daylight to the back of the room.
4. Install interior light shelves (reflective upper surface, matte lower surface) in classrooms with sidelighting: depth of light shelf = 1.5–2.0× window height above shelf; verify daylight penetration to 60–70% of room depth.
5. Commission daylight-responsive controls per CIBSE Guide LG:2022 Section 6.3: set the dimming setpoint at 30–50 foot-candles at task plane; calibrate photosensors using the covered-sensor method (CIBSE TM-183:2020); verify continuous dimming range is 10–100% output; document photosensor setpoints and calibration in O&M manual.
6. Set occupancy sensor time delays to 15–20 minutes for classrooms (to avoid disruption during quiet activities), 10–15 minutes for offices, and 5–10 minutes for restrooms and storage; configure override bypass maximum to 2 hours.
7. Configure demand-responsive lighting control: integrate with BAS or NLC system; set demand response signal to reduce lighting to 50–70% of full output (or turn off non-critical zones entirely) when grid operator signals demand event; verify ≥ 30% power reduction is achieved.
8. Install high-reflectance ceiling tiles (R c ≥ 0.90) in all daylit zones; verify reflectance is maintained after cleaning; specify low-mounting-height fixtures (≤ 9 ft AFF) in classrooms to allow lower wattage fixtures for the same illuminance.
9. Task-tune lighting after occupancy: measure maintained illuminance at task plane in each zone; reduce fixture count or driver output if illuminance exceeds IESNA RP-1 (40 foot-candles for classrooms at task plane); document task-tuning adjustments and update fixture schedule in O&M manual.
10. Train FM staff on NLC system operation: minimum 4 hours covering zone configuration, photosensor recalibration procedure, occupancy sensor time-delay adjustment, and demand response override procedure.

## Risks / Constraints
**Failure Mode — Photosensor Calibration Drift**: photosensors drift out of calibration within 2–3 years of installation due to LED lumen depreciation being misinterpreted as reduced daylight; this causes chronic over-dimming or under-dimming in daylight zones.

**Mitigation**: require annual photosensor recalibration per CIBSE TM-183:2020 covered-sensor method; specify photosensors with ±3% long-term stability; include photosensor recalibration in the FM preventive maintenance schedule; replace photosensors every 5–7 years or per manufacturer specification.

**Failure Mode — NLC System Network Failure Causes Uniform Full-Output**: if the NLC hub or BACnet gateway fails, some systems default all zones to full output (worst-case energy consumption and occupant discomfort).

**Mitigation**: specify NLC system with zone-level autonomous operation (each fixture/sensor operates independently of hub communication); require failover mode configuration that maintains last-known state on hub loss; configure BAS alarm for NLC hub offline condition.

**Failure Mode — Glare from Uncontrolled Daylighting Causes Teacher Complaints**: daylighting design without adequate glare control (internal shades, external overhangs, or appropriate glazing spec) results in visual discomfort, causing teachers to close blinds permanently and defeat the daylighting strategy.

**Mitigation**: require operable interior blinds on all east- and west-facing glazing in classrooms; specify glazing with interior light shelves or diffusing lites to reduce glare potential; during commissioning, verify blinds are functional and teachers are trained on use; glare analysis per CIBSE Guide LG:2022 Section 4.4 (Daylight Glare Index ≤ 19 for classrooms).

**Failure Mode — Occupancy Sensor Nuisance Tripping**: occupancy sensors in classrooms misread occupancy during stationary activities (reading, testing) causing lights to extinguish, disrupting instruction.

**Mitigation**: specify dual-technology sensors (PIR + ultrasonic) for classrooms; set time delay to 15–20 minutes minimum; verify sensor coverage pattern during commissioning using the ASHRAE 90.1-2019 Section 9.4.1.2 coverage test; adjust sensitivity during post-occupancy review if complaints arise.

## KPIs
- Lighting electricity consumption (kWh/ft²/year) — target: ≤ 0.35 kWh/ft²/year in daylit classrooms with NLC system (vs. 0.60–0.80 kWh/ft²/year for code-minimum fluorescent); ≤ 0.20 kWh/ft²/year in toplit storage corridors.
- Connected lighting power density (W/ft²) — target: ≤ 0.45 W/ft² in classrooms per AEDG50-ZNC-2014.
- Daylight zone dimming fraction (average % output) — target: 40–60% average output in sidelit classrooms during school hours (9 AM–3 PM) in shoulder seasons.
- Occupancy sensor effectiveness (fixture-hours saved/100 fixture-hours) — target: ≥ 15% reduction in fixture-hours from occupancy control vs. always-on baseline.
- Demand-responsive lighting performance (kW reduction during events) — target: ≥ 30% reduction in lighting kW during demand response events; verify with utility or grid operator signal.
- Post-commissioning illuminance at task plane (foot-candles) — target: 35–50 foot-candles in classrooms per IESNA RP-1; verify annually.

## M&V Plan
- **IPMVP Option**: Option D (Part-Building — Lighting) for daylight-responsive and occupancy controls; Option A (Retrofit — Isolation, Key Parameter Measurement) as alternative where sub-metering is not practical.
- **Quantification approach**: measure lighting electricity consumption (kWh) by zone using NLC system logging or sub-meters for 90 days pre-installation (baseline) and 90 days post-commissioning at the same time of year; normalize for daylight hours and occupancy; calculate zonal savings (daylit zones vs. non-daylit zones) separately to isolate daylight-responsive dimming savings from occupancy scheduling savings. Use regression of daily kWh vs. daily solar insolation (kWh/ft²) to characterize daylight responsiveness.
- **Data collection**:
  - Lighting electricity consumption by zone (NLC trend log or panel sub-meter, 15-minute resolution, continuous).
  - Photosensor dimming level by zone (NLC trend log, 15-minute resolution, continuous).
  - Occupancy sensor on/off events and time-delay settings (NLC trend log, daily).
  - Illuminance measurements at task plane (lux meter survey, quarterly at minimum; document measurement grid and equipment).
  - Glazing conditions (blind position — open/closed, manually logged weekly by FM staff).
  - Outdoor horizontal solar irradiance (W/m² from on-site sensor or nearest weather station, for daylight normalization).

## Costs & Payback (indicative)
- **Capex**: NLC system with zone-level dimming: $2.00–$4.50/ft² for materials and installation. Clerestory windows or TDDs: $150–$350 per opening. Interior light shelves: $40–$80/linear ft. Photosensor calibration (annual): $500–$1,500/year. High-reflectance ceiling tiles: $0.20–$0.50/ft² incremental cost over standard tile.
- **Opex**: $1,500–$3,500/year for annual photosensor recalibration, NLC firmware updates, and FM training.
- **Simple Payback**: 3.0–6.5 years based on 40–65% lighting electricity reduction in daylit zones (valued at $0.08–$0.18/kWh) plus demand charge reduction. Combined with cooling load reduction in Climate Zones 1–3, payback may reach 2.5–4.5 years.
- **ROI**: 15–33% over 10 years.

## Templates / Reuse
CIBSE TM-183:2020: Daylight Metrics and Measurement Procedures for Buildings and ASHRAE 90.1-2019 Section 9.4 — Lighting Controls provide standardized specification and commissioning formats for daylight-responsive controls in K-12 school buildings.
