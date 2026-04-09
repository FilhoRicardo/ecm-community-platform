---
Main System: "[[Space Planning]]"
Category System: "[[HVAC / Clinical Planning]]"
Utility Affected: "[[Heating and Cooling]]"
Source Document: "[[AEDG50-LargeHospitals-2012.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Program Critical vs Noncritical Areas Before HVAC Escalation

## Summary
Classify hospital spaces accurately so the most energy-intensive ventilation, pressure, and thermal-control strategies are reserved only for truly critical areas. Overclassification — applying high-intensity HVAC to non-clinical and support areas — drives permanent fan, reheat, and plant energy waste across the entire building lifecycle.

## Estimated Savings
- **CIBSE Guidance**: 15–30% reduction in hospital air-side energy in over-classified facilities (per CIBSE Guide B HVAC commissioning data)
- **ASHRAE Guidance**: 20–40% of fan and reheat energy in buildings with significant overclassification (per ASHRAE 90.1 application guidance and AEDG50-LargeHospitals)
- **End-Uses Affected**: Ventilation fan energy, reheat energy, boiler and chiller plant load, and controls complexity

## Basis / References

### CIBSE References
- **Guide B** (HVAC): Air change rate requirements and energy-efficient classification strategies
- **CIBSE AM10** (Commissioning Management): Space classification as a design-stage commissioning input

### ASHRAE References
- **ASHRAE 170** (Ventilation for Healthcare Facilities): Table 7-1 defines minimum outdoor air rates and pressure relationships by clinical function
- **ASHRAE 90.1** (Energy Standard): §6.5 for VAV terminal minimum flow and zone isolation requirements
- **AEDG50-LargeHospitals-2012**: Chapter 3 — Critical vs Noncritical Area Planning as foundational hospital design strategy

### Other Standards
- **FGI 2018 Guidelines**: §5.1 for pressure relationships and minimum air changes by clinical space type (OR, ICU, patient ward, public areas)
- **ANSI/ASHE/ASHRAE 170-2017**: Governs clinical function classifications and corresponding HVAC design parameters

## Assumptions
Best applied at new construction or major renovation stage before system architecture and room standards are frozen. Post-occupancy classification corrections are costly but still valuable if operational drift has reclassified spaces. Clinical function is the primary constraint — patient safety and care quality are non-negotiable first-order inputs. Support, administrative, public, and storage spaces should never carry clinical-grade HVAC intensity without explicit justification. Overclassification is common at programming stage due to clinical staff requesting "just in case" margins.

## Climate Zone Relevance
All climate zones; the energy penalty of overclassification is most acute in extreme and humid climates where ventilation loads are highest, but the design principle applies universally.

## Interaction Notes
Shapes whether advanced VAV, decoupled OA, and airflow setback strategies are available and effective. If all spaces are classified critical, supply air reset, zone setbacks, and pressure decoupling become unavailable without violating operating room standards. Accurate classification is a prerequisite for ECM_Decoupled_Ventilation_and_Reheat_Reduction_Large_Hospital and ECM_Airflow_Setback_in_Procedure_Spaces_Large_Hospital. Synergizes with LED surgical lighting and BAS governance — each enabled area can carry lower-intensity HVAC for those zones.

## Implementation Essentials
- **Classification audit**: Review each department and room type against ASHRAE 170 Table 7-1 and FGI 2018 requirements; document current classification and clinical justification
- **Critical classification criteria**: Operating rooms (≥20 ACH fresh OA), procedure rooms (≥12 ACH), ICU (≥6 ACH), general wards (≥2 ACH), public corridors (minimum ventilation only)
- **Noncritical classification**: Administrative areas, storage, corridors, mechanical rooms — apply minimum code ventilation; exclude from reheat and high-intensity pressure control
- **Separate support and admin spaces**: Route support and administrative zones to lower-intensity air-handling units or VAV boxes with tighter minimum flow limits
- **Revisit classifications when department planning changes**: Formal review required when clinical departments are reorganized, added, or reduced
- **Design-stage controls**: Lock criticality decisions into room data sheets and BAS control philosophy so future operators cannot inadvertently escalate

## Risks / Constraints
- **Overclassification is common and difficult to undo**: If spaces are classified critical at design stage and built with high-capacity equipment, retrofit to lower classification requires equipment replacement or major rebalancing — involve clinical engineering at programming stage to prevent overclassification
- **Underclassification creates compliance and patient-safety risk**: Maintain ASHRAE 170 and FGI 2018 minimums; any area reclassification must be reviewed and approved by clinical governance before implementation
- **Pressure relationship requirements are asymmetric**: Critical areas require positive pressure relative to adjacent spaces; declassified spaces may require negative pressure relative to adjacent clinical zones — this must be verified at each review
- **Clinical staff may resist reclassification**: Present energy and comfort data to clinical leadership; emphasize that lower-intensity HVAC in nonclinical zones does not reduce clinical zone performance

## KPIs
- Area (m² or ft²) by criticality classification level (critical / support / administrative / public / storage)
- Airflow intensity by department: CFM/ft² or ACH — target: support/admin ≤50% of critical area intensity
- Reheat energy intensity (kBtu/ft²) by classification — target: noncritical zones <30% of critical zone reheat intensity
- Number of spaces currently operating at higher intensity than ASHRAE 170 Table 7-1 minimum requires
- Energy cost per ft² by classification: critical areas vs support areas (normalized for climate)
- Controls complexity score: number of unique pressure control zones — target: minimize number of independent pressure control domains

## M&V Plan
**Option B (Retrofit Isolation with Subsystem Verification)** per IPMVP for post-occupancy assessment; design-stage verification through room data sheets and airflow budgets for new construction

**Quantification approach:**
- Pre: Characterize baseline energy by zone classification using sub-metered or estimated energy proportional to airflow
- Post: Compare actual airflows against classified requirements; calculate avoided fan, reheat, and plant energy from declassified zones
- Apply ASHRAE 90.1 §6.5 fan power limits and reheat intensity benchmarks to estimate savings
- Normalize for occupancy and weather; focus on shoulder-season and shoulder-month data when simultaneous heating/cooling is most visible

**Data collection:**
- ASHRAE 170 Table 7-1 airflow requirements by room type (design reference)
- Actual measured airflows (CFM or m³/h) by zone post-occupancy
- Zone temperature and reheat valve position (% open) at 15-minute intervals by classification
- Sub-metered or estimated energy consumption by zone (kWh)
- Departmental occupancy counts and scheduling (for normalization)
- Outside air temperature for weather correlation

## Costs & Payback (Indicative)
- **Capex**: Design-stage analysis: minimal cost (£0–2,000 for classification study); post-occupancy retrofit may require rebalancing, controls reprogramming, and damper re-commissioning: £5,000–25,000 per floor/zone depending on scope
- **Opex**: Annual classification review: staff time (~4–8 hours/year)
- **Simple payback**: <1 year for design-stage intervention; 1–3 years for post-occupancy rebalancing
- **ROI**: Very high; each correctly declassified zone permanently reduces fan, reheat, and plant energy for the building lifetime

## Templates / Reuse
*Boilerplate footer removed. Reference ASHRAE 170-2017 Table 7-1 and FGI 2018 Guidelines §5.1 for minimum clinical ventilation requirements.*
