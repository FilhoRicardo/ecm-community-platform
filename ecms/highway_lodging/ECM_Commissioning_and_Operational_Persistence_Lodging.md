---
Main System: "[[Commissioning]]"
Category System: "[[Operations]]"
Utility Affected: "[[Multiple utilities]]"
Source Document: "[[AEDG30-HighwayLodging.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Lodging Commissioning, Scheduling, and Operational Persistence

## Summary
Use commissioning, scheduling discipline, and routine operational review to preserve savings from guestroom HVAC, lighting, DHW, and ventilation measures across the building life cycle. Without active persistence, even well-designed highway lodging properties erode savings within 2–3 years of occupancy through control overrides, schedule drift, and deferred maintenance.

## Estimated Savings
- **Persistence value**: protects 10–30% of installed ECM savings that would otherwise decay over 5 years without active management (CIBSE Guide M:2022, Section 8 — Operations and Maintenance).
- **End-Uses Affected**: whole-building operations; indirect savings across HVAC, lighting, DHW, and ventilation.

## Basis / References
**CIBSE**
- CIBSE Guide M:2022, Section 8: Systems commissioning and operational persistence — recommends ongoing M&V and periodic recommissioning at minimum 5-year intervals.

**ASHRAE**
- ASHRAE Standard 100-2018, Section 7: Occupant Behavior and Control Persistence — addresses how operational drift erodes designed performance in lodging buildings.
- ASHRAE 90.1-2019, Section 6.4: Building Operation and Maintenance — requires O&M documentation and periodic verification of control sequences.

**Other**
- AEDG30-HighwayLodging.pdf — emphasizes QA, commissioning, and operational discipline through the building life cycle as essential to realized savings.

## Assumptions
- Owner/operator is willing to commit to periodic review (at least annually).
- BAS or standalone control trending is available or can be added at reasonable cost.
- Property management system (PMS) integration can provide occupancy-state signals.

## Climate Zone Relevance
All climate zones. Persistence is especially critical in climates with long heating or cooling seasons where equipment runtime is high and savings erosion is proportionally larger.

## Interaction Notes
- Supports every other ECM in the lodging package — particularly guestroom occupancy setback, PTAC/PTHP upgrade, LED lighting, and DHW optimization.
- Poor persistence directly undermines envelope air sealing benefits by allowing HVAC equipment to compensate for increased infiltration from deferred maintenance.

## Implementation Essentials
1. Conduct a baseline commissioning report at project turnover covering all guestroom HVAC, lighting, DHW, and common-area systems per ASHRAE Standard 100 Section 7.2.
2. Install trend logs for guestroom unit schedules, exterior lighting runtimes, DHW return temperature, and HVAC fault counts — minimum 15-minute intervals.
3. Define three room control states: Occupied (full comfort), Rented-Vacant (setback active), and Unrented (deeper setback) — document the logic in the O&M manual.
4. Benchmark energy per occupied room-night monthly using normalized metrics (kBtu/room-night, adjusted for weather and occupancy).
5. Review complaint hot spots within 48 hours of receipt; do not allow permanent manual overrides without FM sign-off.
6. Recommission after major room refresh, PMS/control system changes, or staff turnover events.
7. Conduct a formal recommissioning sweep at years 1, 3, and 5 post-occupancy, addressing any drift from design intent.

## Risks / Constraints
**Failure Mode — Control Override Drift**: Housekeeping or engineering staff manually defeat occupancy sensors or setpoint locks to eliminate complaints, quietly removing 15–25% of HVAC savings within the first year.

**Mitigation**: Require override events to be logged and reviewed monthly; tie override counts to FM performance metrics; restore correct settings within 72 hours of any override.

**Failure Mode — Schedule Creep**: Exterior lighting and common-area HVAC schedules drift later into evening or earlier in morning over successive seasons as no one challenges the status quo.

**Mitigation**: Lock schedules in the BAS with documented change-control process; review all schedule changes quarterly.

**Failure Mode — Staff Turnover**: Institutional knowledge of control settings and persistence protocols is lost when maintenance or front-desk staff turnover.

**Mitigation**: Document all sequences in the O&M manual; require new-staff training as part of onboarding; keep persistence protocol visible on the BAS front-end.

## KPIs
- Energy per occupied room-night (kBtu/room-night or kWh/room-night) — target: ≤ 5% annual drift from commissioning baseline.
- Monthly override count per 100 rooms — target: < 5 overrides/month/100 rooms sustained.
- Complaint-to-resolution cycle time (hours) — target: < 48 hours for comfort complaints.
- HVAC fault recurrence rate (%) — target: < 10% of faults repeat within 90 days.
- Recommissioning findings closed (%) — target: 100% of critical findings closed within 30 days, 90% of non-critical within 90 days.

## M&V Plan
- **IPMVP Option**: Option C (Whole Building Metered Energy) with supplemental trend data for key end uses.
- **Quantification approach**: Establish a commissioning baseline EUI at year 0; compare monthly EUI per room-night against this baseline, normalized for heating degree days (HDD) and cooling degree days (CDD) using ASHRAE 90.1-2019 Appendix D weather normalization procedure.
- **Data collection**:
  - Whole-building electricity and natural gas consumption (monthly utility bills).
  - Guestroom occupancy rate (from PMS, daily).
  - HDD/CDD from local weather station (ASHRAE Climatic Data Region).
  - Guestroom HVAC runtime by control state (BAS trend logs, 15-minute resolution).
  - Override event log (BAS or standalone controller).
  - Complaint register (work order system).

## Costs & Payback (indicative)
- **Capex**: $2,000–$8,000 for BAS trend log configuration, sensor installation, and baseline commissioning report (100-room property).
- **Opex**: $1,500–$4,000/year for quarterly schedule review, annual recommissioning sweep, and FM staff time.
- **Simple Payback**: 1.2–3.5 years (based on preserving 10–20% of HVAC and lighting savings valued at $0.08–$0.12/kWh).
- **ROI**: 30–80% over 5 years, driven by avoided savings erosion rather than direct energy reduction.

## Templates / Reuse
ASHRAE Standard 100-2018 Appendix A — Operations and Maintenance Plan template provides a structured format for documenting persistence protocols and commissioning baselines applicable across lodging property types.
