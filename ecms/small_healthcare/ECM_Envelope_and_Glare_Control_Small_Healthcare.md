---
Main System: "[[Envelope]]"
Category System: "[[Envelope / Daylighting]]"
Utility Affected: "[[Heating, Cooling, and Lighting]]"
Source Document: "[[AEDG30-SmallHealthcare-2009.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Envelope, Glazing, and Solar-Control Upgrade for Small Healthcare

## Summary
Use better opaque envelope performance, glazing selection, and solar control to reduce perimeter loads while improving patient/staff visual comfort and daylight usability. Small healthcare facilities are particularly sensitive to envelope performance because their smaller floor plates have higher ratios of facade area to floor area, making perimeter loads a larger fraction of total energy than in larger buildings.

## Estimated Savings
- **CIBSE Guidance**: 10–20% of whole-building energy through envelope upgrades in small healthcare facilities (per CIBSE Guide A environmental design data)
- **ASHRAE Guidance**: 8–18% of HVAC energy through envelope and glazing upgrades (per ASHRAE 90.1 and AEDG30-SmallHealthcare)
- **End-Uses Affected**: Heating energy, cooling energy, perimeter lighting energy, and patient/staff thermal comfort

## Basis / References

### CIBSE References
- **Guide A** (Environmental Design): Opaque envelope and glazing performance targets by climate; daylighting strategy
- **Guide B** (HVAC): Fenestration thermal performance and solar control interactions with HVAC sizing

### ASHRAE References
- **90.1** (Energy Standard): Table 5.5.5 for climate-zone-specific opaque envelope requirements; Table 5.5.6 for fenestration U-factor and SHGC requirements; §5.4 for building envelope requirements
- **AEDG30-SmallHealthcare-2009**: Climate-zone prescriptions for roof, wall, glazing, and shading performance

### Other Standards
- **BS EN 13363** (Solar Protection Devices): Solar control device performance standards
- **NFRC** (National Fenestration Rating Council): Window performance rating methodology

## Assumptions
Most useful in new construction or major façade/roof renovation where envelope components are being replaced anyway. Retrofit envelope upgrades (wall/roof insulation, window replacement) have higher cost and longer payback than whole-building envelope upgrades done at construction. Target wall R-value: R-13 to R-20 depending on climate zone; roof R-value: R-30 to R-49. Target window U-factor: 0.30–0.50 BTU/hr·ft²·°F; SHGC: 0.25–0.40 depending on climate. Window-to-wall ratio: ≤30–40% depending on orientation and climate.

## Climate Zone Relevance
Stronger solar-control value in hot/mixed climates (CZ 1–4, CZ 6) where cooling loads dominate; stronger U-factor value in colder climates (CZ 5–8) where heating loads dominate. All climate zones benefit from improved envelope performance; the specific strategy differs by dominant load.

## Interaction Notes
Pairs with ECM_Patient_Room_and_Clinical_Lighting_Optimization_Small_Healthcare for daylighting strategy — improved glazing with low-E coating allows more daylight without thermal penalty. Complements ECM_DOAS_with_Heat_Recovery_Small_Healthcare: envelope upgrades reduce OA treatment loads, improving DOAS economics. Benefits depend on whether blinds remain open and controls are commissioned — shading control strategy is as important as glazing selection. Synergizes with ECM_Commissioning_and_Trend_Review_Small_Healthcare: post-envelope changes require HVAC rebalancing to capture the reduced loads.

## Implementation Essentials
- **Whole-assembly glazing performance**: Specify windows by assembly U-factor and SHGC (not just center-of-glass), accounting for frame effects — target: U-factor 0.30–0.50, SHGC 0.25–0.40 by climate
- **Orientation-specific solar strategy**: North facade: maximize daylight with low SHGC for heat gain control; South/East: shading devices for peak solar control; West: high SHGC control priority with overhangs or fins
- **Window-to-wall ratio discipline**: Limit WWR to 30–40% depending on climate; excessive glazing in small healthcare facilities causes significant perimeter heating/cooling penalties
- **Shading devices**: Add exterior or interior shading where solar exposure justifies it — overhangs for south-facing, fins for east/west-facing; interior blinds are less effective in hot climates
- **Opaque envelope upgrades**: Insulate walls to R-13 minimum in CZ 1–4, R-15 in CZ 5–7, R-20 in CZ 8; roof insulation R-30 minimum in CZ 1–4, R-38 in CZ 5–7, R-49 in CZ 8
- **HVAC sizing after envelope changes**: Re-evaluate heating and cooling loads after envelope upgrades; right-size HVAC equipment to avoid over-sizing penalties from conservative rules of thumb
- **Daylighting integration**: Coordinate glazing selection with daylighting strategy — visible light transmittance ≥0.30 for adequate daylight; specify low-E coating with high VLT for daylight without thermal penalty

## Risks / Constraints
- **Overglazing creates summer thermal discomfort**: Excessive window area in hot climates causes summer overheating even with low SHGC glazing — Mitigate: limit WWR to 30–40%; specify exterior shading; verify thermal comfort with modeling before construction
- **Blind use patterns undermine daylighting potential**: If occupants keep blinds closed year-round, daylighting potential is lost — Mitigate: specify easy-to-operate blinds; commission blind positions as part of occupancy onboarding; provide automated blind control linked to daylight sensor
- **HVAC over-sizing after envelope upgrade**: If envelope is upgraded but HVAC is not right-sized, the envelope upgrade appears to save less than modeled — Mitigate: require HVAC rebalancing study after envelope completion and verify actual loads vs design
- **Façade integration with clinical requirements**: Some clinical spaces (procedure rooms, exam rooms) may require specific lighting levels that conflict with daylighting strategy — coordinate clinical lighting requirements with envelope design early
- **Construction coordination**: Envelope upgrades during occupied renovation require infection control barriers and temporary HVAC adjustments — plan for phased construction with clinical operations continuity

## KPIs
- Wall R-value (ft²·°F·hr/BTU) and roof R-value — verify meets ASHRAE 90.1 Table 5.5.5 minimums for applicable climate zone
- Window U-factor and SHGC — verify meets ASHRAE 90.1 Table 5.5.6 minimums for applicable climate zone
- Window-to-wall ratio by facade (%) — target: ≤30–40% depending on orientation and climate
- Perimeter heating/cooling energy intensity (kBtu/ft²) vs interior zones — measure before/after envelope upgrade
- Lighting energy intensity in perimeter zones (kWh/ft²) — measure before/after daylighting optimization
- Patient/staff thermal comfort complaints (count/quarter) — track before/after envelope upgrade
- Glare complaints (count/quarter) — correlate with blind use patterns and shading control commissioning

## M&V Plan
**Option B (Retrofit Isolation — Building Envelope Level)** per IPMVP for post-occupancy assessment; design-stage verification through modeling for new construction

**Quantification approach:**
- Baseline: Pre-envelope whole-building energy (kBtu/ft²) and perimeter zone energy using utility bills or sub-metered data
- Post-implementation: Compare whole-building and perimeter zone energy after envelope upgrade; normalize for weather (HDD/CDD) and occupancy variations
- Calculate envelope-related savings: perimeter heating/cooling reduction + lighting reduction from daylighting (where applicable)
- ASHRAE 90.1 compliance check: verify envelope components meet or exceed minimum requirements for applicable climate zone

**Data collection:**
- Wall and roof insulation R-value documentation (construction records or as-built drawings)
- Window U-factor, SHGC, and VLT (manufacturer data)
- Window-to-wall ratio by facade (measured from drawings)
- Whole-building energy (kBtu/ft² or kWh/m²) monthly from utility bills
- Perimeter zone energy (kBtu/ft²) vs interior zones from sub-metering or modeling
- Outside air temperature, HDD, CDD for weather normalization
- Patient/staff comfort complaints log by zone

## Costs & Payback (Indicative)
- **Capex**: Wall/roof insulation upgrade: £5–15/ft² depending on existing condition; window replacement: £40–100/ft²; exterior shading devices: £15–50/ft²; commissioning and testing: £2,000–6,000
- **Opex**: Annual inspection of envelope integrity and sealants: £500–1,500/year
- **Simple payback**: 5–15 years for envelope-only retrofits in existing buildings; 3–7 years for whole-building envelope upgrades done during new construction or major renovation
- **ROI**: Enhanced when combined with daylighting and HVAC right-sizing; longer-term strategic value for building durability and comfort

## Templates / Reuse
*Boilerplate footer removed. Reference ASHRAE 90.1 Tables 5.5.5 and 5.5.6 for climate-zone-specific envelope requirements.*
