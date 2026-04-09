---
Main System: "[[Space Planning]]"
Category System: "[[HVAC / Clinical Planning]]"
Utility Affected: "[[Heating and Cooling]]"
Source Document: "[[AEDG30-SmallHealthcare-2009.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Classify Critical vs Noncritical Areas and Match HVAC Intensity Accordingly

## Summary
Separate truly critical-care or higher-intensity spaces from noncritical areas so ventilation, pressure, temperature, and system complexity are not overapplied everywhere. Small healthcare facilities are particularly vulnerable to overclassification because clinical staff with limited HVAC knowledge often request "hospital-grade" conditions for spaces that do not require them, permanently locking in excess fan, reheat, and plant energy.

## Estimated Savings
- **CIBSE Guidance**: 20–35% of total HVAC energy in small healthcare facilities with significant overclassification (per CIBSE Guide B healthcare HVAC data)
- **ASHRAE Guidance**: 15–30% reduction in fan, reheat, and plant energy through accurate clinical classification (per ASHRAE 90.1 application guidance and AEDG30-SmallHealthcare)
- **End-Uses Affected**: Ventilation fan energy, reheat energy, boiler/chiller plant load, and controls complexity

## Basis / References

### CIBSE References
- **Guide B** (HVAC): Healthcare HVAC classification, minimum air change rates, and energy-efficient system selection
- **CIBSE AM10** (Commissioning Management): Clinical area classification as design-stage commissioning input

### ASHRAE References
- **ASHRAE 170** (Ventilation for Healthcare Facilities): Table 7-1 minimum outdoor air rates, pressure relationships, and temperature/humidity by clinical function
- **90.1** (Energy Standard): §6.5 for VAV minimum flow limits and §6.4 for HVAC controls
- **AEDG30-SmallHealthcare-2009**: Chapter 3 — Space Classification as foundational design strategy for small healthcare facilities

### Other Standards
- **FGI 2018 Guidelines**: §5.1 for minimum air changes, pressure relationships, and temperature/humidity by clinical space type
- **ANSI/ASHE/ASHRAE 170-2017**: Governs clinical function classifications and corresponding HVAC design parameters

## Assumptions
Best addressed in early programming and schematic design when system architecture can still be influenced. Post-occupancy corrections are costly but still valuable where operational drift has escalated space requirements. Clinical function is the non-negotiable first-order input — patient safety and infection control are paramount. Support areas (administrative, storage, corridors, mechanical rooms) should never carry clinical-grade HVAC intensity. Overclassification is most common at programming stage when clinical staff request maximum flexibility "for future needs."

## Climate Zone Relevance
All climate zones; the energy penalty of overclassification is most acute in extreme and hot-humid climates where ventilation loads are highest. The design principle applies universally.

## Interaction Notes
Shapes the viability of VAV, fan-coil, WSHP, and setback measures throughout the project. This is the foundational decision that enables or disables all subsequent HVAC ECMs. Pairs with DOAS design (ECM_DOAS_with_Heat_Recovery_Small_Healthcare): accurate classification determines whether decoupled OA treatment is needed for a given space. Synergizes with clinical lighting optimization (ECM_Patient_Room_and_Clinical_Lighting_Optimization_Small_Healthcare): lighting levels by clinical task are defined by the space classification. Complements commissioning (ECM_Commissioning_and_Trend_Review_Small_Healthcare): commissioning should verify classification against actual clinical function.

## Implementation Essentials
- **Classification audit**: Review each department and room against ASHRAE 170 Table 7-1 and FGI 2018 requirements; document current classification and clinical justification — classify every space before determining HVAC system architecture
- **Critical classification examples** (per ASHRAE 170): Examination rooms (≥6 ACH fresh OA), treatment rooms (≥6 ACH), procedure rooms (≥12 ACH), patient rooms (≥2 ACH), nurse stations (≥4 ACH)
- **Noncritical classification examples**: Administrative areas (minimum ventilation only, no recirculated reheat), storage rooms (minimum ventilation, no temperature control), corridors (minimum ventilation, no individual temperature control), mechanical rooms (no recirculated air)
- **Separate support and admin systems**: Route nonclinical zones to lower-intensity air-handling units or terminal systems with tighter minimum flow limits
- **Lock classification into room data sheets**: Document clinical function and ASHRAE 170 requirements in room data sheets; use these as binding design inputs, not suggestions
- **Revisit classifications when departments change**: Formal review required when clinical departments are reorganized; involve clinical engineering before any space use change

## Risks / Constraints
- **Overclassification is common and difficult to reverse**: If spaces are classified critical at design stage and built with high-capacity equipment, retrofit to lower classification requires equipment replacement or major rebalancing — involve clinical engineering at programming stage to prevent overclassification; present energy and comfort data to clinical leadership
- **Underclassification creates compliance and patient-safety risk**: Maintain ASHRAE 170 and FGI 2018 minimums; any declassification must be reviewed and approved by clinical governance before implementation
- **Pressure relationship requirements are asymmetric**: Critical areas require positive pressure relative to adjacent spaces; declassified spaces may require negative pressure relative to adjacent clinical zones — verify at each review
- **Clinical staff resistance**: Clinical stakeholders may request higher classification for comfort or perceived safety — present measured energy and comfort data; emphasize that lower-intensity HVAC in nonclinical zones does not reduce clinical zone performance

## KPIs
- Area (m² or ft²) by criticality classification level (critical / support / administrative / public / storage)
- Airflow intensity by space (CFM/ft² or ACH) — target: support/admin ≤40% of critical area intensity
- Reheat energy intensity (kBtu/ft²) by classification — target: noncritical zones <25% of critical zone reheat intensity
- Number of spaces operating at higher intensity than ASHRAE 170 Table 7-1 minimum requires
- Fan energy intensity (kWh/ft²) by system — compare critical vs noncritical area HVAC systems
- Controls complexity score: unique pressure control zones — target: minimize number of independent pressure control domains

## M&V Plan
**Option B (Retrofit Isolation with Subsystem Verification)** per IPMVP for post-occupancy assessment; design-stage verification through room data sheets and airflow budgets for new construction

**Quantification approach:**
- Pre: Characterize baseline HVAC energy by zone classification using sub-metered or estimated energy proportional to airflow
- Post: Compare actual airflows against classified requirements; calculate avoided fan, reheat, and plant energy from declassified zones
- Apply ASHRAE 90.1 §6.5 fan power limits and reheat intensity benchmarks to estimate savings
- Normalize for occupancy and weather; focus on shoulder-season data when simultaneous heating/cooling is most visible

**Data collection:**
- ASHRAE 170 Table 7-1 airflow requirements by room type (design reference)
- Actual measured airflows (CFM or m³/h) by zone post-occupancy
- Zone temperature and reheat valve position (% open) at 15-minute intervals by classification
- Sub-metered or estimated energy consumption by zone (kWh)
- Departmental occupancy counts and scheduling (for normalization)
- Outside air temperature for weather correlation

## Costs & Payback (Indicative)
- **Capex**: Design-stage classification analysis: minimal cost (£0–2,000); post-occupancy rebalancing: £3,000–15,000 per zone depending on scope
- **Opex**: Annual classification review: staff time (~4–8 hours/year)
- **Simple payback**: <1 year for design-stage intervention; 1–3 years for post-occupancy rebalancing
- **ROI**: Very high; each correctly declassified zone permanently reduces fan, reheat, and plant energy for the building lifetime

## Templates / Reuse
*Boilerplate footer removed. Reference ASHRAE 170-2017 Table 7-1 and FGI 2018 Guidelines §5.1 for minimum clinical ventilation requirements.*
