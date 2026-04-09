---
Main System: "[[Daylighting]]"
Category System: "[[Classrooms]]"
Utility Affected: "[[Electricity]]"
Source Document: "[[AEDG50-K12-2011.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Classroom Sidelighting and Toplighting Package

## Summary
Use classroom daylighting deliberately through sidelighting, toplighting, or both so electric lighting is reduced during school hours while visual comfort and teaching quality are preserved. In K-12 schools, electric lighting accounts for 25–40% of total electricity consumption (AEDG50-K12-2011.pdf, Section 3 — Lighting and Daylighting), and well-designed daylighting can reduce classroom lighting energy by 40–65% during occupied daylight hours (CIBSE Guide LG:2018, Table 7.2).

## Estimated Savings
- **Classroom lighting electricity reduction**: 40–65% reduction in classroom lighting kWh during daylight hours where daylighting design is well-implemented.
- **Toplighting contribution**: 50–75% reduction in electric lighting energy in top-lit zones (gyms, cafeterias, corridors with roof monitors) during daytime use.
- **Secondary cooling reduction**: 5–15% reduction in cooling energy from reduced lighting heat gain (approximately 3 W of heat reduction per 1 W of LED lighting reduction vs. fluorescent baseline).
- **End-Uses Affected**: classroom lighting, corridor/common-area lighting, and secondary cooling.

## Basis / References
**CIBSE**
- CIBSE Guide LG:2018, Table 7.2: Daylighting Energy Savings by Climate Zone and Glazing Configuration — indicates 40–65% classroom lighting reduction in sidelit zones and 50–75% in toplit zones for ASHRAE climate zones 4–7.
- CIBSE Guide LG:2018, Section 7.3: Side-Daylit Spaces — recommends window head height ≥ 36% of floor-to-ceiling height and visible light transmittance (VLT) ≥ 0.40 for effective sidelighting.

**ASHRAE**
- ASHRAE 90.1-2019 Section 8.2.2: Daylight-Responsive Controls — requires automatic daylighting controls for spaces with fenestration or roof apertures exceeding 24 ft²; controls must reduce lighting power by at least 50% at the daylight zone boundary.
- ASHRAE 90.1-2019 Table 8.2.2.1: Maximum Lighting Power Density for Educational Occupancies — sets maximum LPD of 0.96 W/ft² for classrooms, 0.72 W/ft² for corridors, and 0.64 W/ft² for libraries per ASHRAE 90.1-2019 Table 8.2.2.1.
- ASHRAE 90.1-2019 Section 8.4.3: Daylight-Responsive Controls — requires continuous dimming or stepped tuning with no more than three steps.

**Other**
- AEDG50-K12-2011.pdf: One of the strongest school-specific strategies in the 50% K-12 guide; dedicated sections for classroom sidelighting, toplighting, and combined strategies with shading and daylighting examples specific to schools.

## Assumptions
- Classroom depth is ≤ 25 ft from the window wall for effective sidelighting without reliance on toplighting.
- Roof structure and budget allow for roof monitors or skylights in appropriate areas.
- Teaching wall and AV systems (projectors, interactive whiteboards) are coordinated with daylighting design to avoid glare conflicts.

## Climate Zone Relevance
- **All climate zones**: Daylighting reduces electric lighting in all climates; the balance of heating and cooling impacts varies:
  - Cold climates (Zones 5–8): Winter daylighting adds beneficial solar heat gain; summer cooling penalty is minimal.
  - Hot climates (Zones 1–3): Exterior shading devices (overhangs, fins) are critical to prevent excessive cooling loads from direct sun; SHGC ≤ 0.25 recommended for south-facing glazing in climate zones 1–3.
  - Mixed climates (Zones 4): Both heating and cooling considerations apply; east/west glazing requires careful shading to control summer cooling loads.

## Interaction Notes
- Pairs with occupancy/daylight controls: daylighting only saves energy if electric lights are automatically dimmed or switched; manual override of daylight controls eliminates 60–80% of potential savings.
- Works with high-reflectance ceiling and wall surfaces: increasing ceiling reflectance from 0.70 to 0.85 improves daylight uniformity by 15–25% at the same window area.
- Complements classroom layout: desks oriented perpendicular to windows receive more uniform daylight; teachers facing the class (not the window) experience less glare.

## Implementation Essentials
1. Conduct a daylighting analysis using Climate-Based Daylight Modeling (CBDM) per IES LM-83-12 or equivalent: calculate Daylight Autonomy (DA ≥ 50% for ≥ 50% of floor area), Useful Daylight Illuminance (UDI 300–3000 lux), and Annual Solar Exposure (ASE ≤ 10% of floor area at ≥ 1000 lux for > 250 hours/year).
2. For sidelighting design:
   - Window head height: minimum 36% of floor-to-ceiling height (e.g., 3.6 ft head height for 10 ft ceilings) per CIBSE Guide LG:2018 Section 7.3.
   - Exterior shading: use horizontal overhangs for south-facing facades (overhang projection factor ≥ 0.5); vertical fins for east and west facades.
   - Interior light shelf: install reflective (≥ 0.80 reflectance) light shelves to redirect daylight onto the ceiling and deeper into the room.
   - Glazing specification: VLT ≥ 0.40, SHGC ≤ 0.30 for climate zones 1–3; VLT ≥ 0.40, SHGC ≤ 0.40 for climate zones 4–8.
3. For toplighting design:
   - Skylight glazing: U-factor ≤ 0.30, SHGC ≤ 0.30; use diffusing rather than clear glazing to prevent direct-beam glare.
   - Skylight spacing: depth-to-spacing ratio ≤ 0.75 for flat roofs (center-to-center spacing ≤ 0.75 × height above ceiling) per IES RP-5-13.
   - Pair with translucent diffusers to distribute light uniformly across the space.
4. Daylight-responsive controls:
   - Install continuous dimming daylight sensors (photosensor +_CONTINUOUS Dimming) in all daylit zones; maximum zone depth per photosensor is 15 ft from the window wall for sidelit zones and 10 ft radius for toplit zones.
   - Configure control algorithm per ASHRAE 90.1-2019 Section 8.4.3: maximum lighting power reduction of 50% at the daylight zone boundary; continuous dimming between 50% and 100% of design illuminance.
   - Commission photosensors at two illuminance levels (daylight-only and electric + daylight) using a calibrated illuminance meter per IES NGLD-10.
5. Commissioning: verify daylight sensor response and calibration; confirm that electric lights dim to minimum output (not off) during peak daylight to maintain visual continuity; test override behavior and confirm that manual overrides revert to automatic within 4 hours.
6. Protect teaching-wall visibility: coordinate window blind specification (horizontal slats, ≥ 0.80 reflectance on top surface) so that blinds can block direct sun without fully eliminating the view or daylight contribution.

## Risks / Constraints
**Failure Mode — Blind Closure by Teachers**: Without glare control, teachers immediately and permanently close blinds, eliminating 80–100% of daylighting energy savings and defeating the purpose of the daylighting investment.

**Mitigation**: Involve teachers in blind specification and calibration during commissioning; specify blinds with toplight-transmitting horizontal slat geometry; install automated blinds linked to photosensors with a manual override that auto-returns to the programmed position within 2 hours.

**Failure Mode — Roof Aperture Thermal Penalties**: Skylights without adequate thermal breaks or high-performance glazing increase heating loads in winter and cooling loads in summer, partially or fully offsetting lighting energy savings.

**Mitigation**: Specify skylights with U-factor ≤ 0.30 and SHGC ≤ 0.30; add insulated diffusers and thermal breaks at the skylight curb; verify net energy benefit using annual energy model comparing lighting energy savings against HVAC energy change.

**Failure Mode — AV and Daylighting Conflict**: Direct sunlight on projection screens or interactive whiteboards forces teachers to darken the room, eliminating daylighting savings during the highest-illuminance hours.

**Mitigation**: Position teaching walls away from primary window walls; specify screens with high ambient-light rejection (ALR ≥ 0.8 gain); use motorized blackout shades in AV-heavy classrooms, controlled by the AV system rather than manual blinds.

## KPIs
- Classroom lighting kWh during occupied hours — target: 40–65% reduction from pre-daylighting baseline during daylight hours.
- Daylight Autonomy (DA) (%) — target: ≥ 50% of floor area at ≥ 300 lux for ≥ 50% of occupied hours.
- Useful Daylight Illuminance (UDI 300–3000 lux) (%) — target: ≥ 60% of occupied hours within this range.
- Blind closure rate (% of days with > 80% blind closure during school hours) — target: < 10% of school days.
- Electric lighting power density in daylit classrooms (W/ft²) — target: ≤ 0.48 W/ft² after daylight dimming (50% of LPD at full output).
- Annual daylighting HVAC interaction (net kBtu/ft²) — target: net positive (lighting + cooling savings exceed any heating penalty) per annual energy model.

## M&V Plan
- **IPMVP Option**: Option C (Whole Building Metered Energy) for lighting — isolate classroom lighting from other building loads with dedicated panel metering and trend data.
- **Quantification approach**: Install dedicated classroom lighting panel kWh meters; compare 12-month pre/post lighting kWh, normalized for school occupancy days (instructional hours). Use a calibrated daylight simulation model (e.g., EnergyPlus with Radiance-based daylighting) to estimate the fraction of lighting energy attributable to daylighting based on measured window area, glazing properties, and shading device state.
- **Data collection**:
  - Classroom lighting kWh by panel (dedicated meter, 15-minute resolution, 12 months pre and 12 months post).
  - School occupancy schedule (instructional hours per day, from school district calendar).
  - Window shade position (% closed) trend log (BAS or standalone shade controller log, daily average).
  - Photosensor output (foot-candles) trend at work plane height, monthly.
  - HDD and CDD for HVAC interaction analysis (local weather station data).

## Costs & Payback (indicative)
- **Capex**: Sidelighting (high-performance glazing, interior shading, light shelves): $15–$35/ft² of window area. Toplighting (skylights, diffusers, curbs): $30–$60/ft² of roof area. Daylight sensors and commissioning: $400–$800 per classroom. For a 5-classroom wing: $75,000–$150,000 (new construction); $40,000–$90,000 (major renovation).
- **Opex**: $500–$1,200/year for photosensor recalibration, shade motor maintenance, and annual daylight model verification.
- **Simple Payback**: 5–12 years for sidelighting with daylight-responsive controls; 8–15 years for toplighting in new construction; 6–10 years for toplighting in renovation (includes HVAC interaction benefit).
- **ROI**: 8–20% over 15 years.

## Templates / Reuse
IES LM-83-12: IES Daylight Metrics Committee Standard File Format for Daylight Simulation and CIBSE Guide LG:2018 Appendix 7.A — Daylighting Design Brief Template provide standardized formats for daylighting analysis documentation and performance verification applicable to K-12 school classroom daylighting projects.
