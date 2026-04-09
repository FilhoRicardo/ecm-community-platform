---
Main System: "[[Commissioning]]"
Category System: "[[Operations / Education]]"
Utility Affected: "[[Multiple utilities]]"
Source Document: "[[AEDG50-K12-2011.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: School Commissioning with Teaching-Tool and Staff Training Integration

## Summary
Commission the school building and integrate energy performance data into the educational program so the building performs as designed and can also serve as a visible, real-time learning tool for students and staff. Without active commissioning and engagement, K-12 schools typically operate at 15–25% above their designed EUI within 3 years of occupancy (CIBSE Guide M:2022, Section 8 — Commissioning and Operational Persistence).

## Estimated Savings
- **Operational savings from commissioning**: 8–15% reduction in whole-building EUI from commissioning alone in schools with no prior commissioning record (CIBSE Guide M:2022, Table 8.1).
- **Persistence benefit**: prevents 10–20% annual savings erosion that occurs without ongoing commissioning verification (CIBSE Guide M:2022, Section 8.3).
- **Occupant behavior engagement**: 3–8% additional EUI reduction from dashboard and engagement programs that reduce after-hours waste and plug-load intensity.
- **End-Uses Affected**: whole-building operations, indirectly all end uses.

## Basis / References
**CIBSE**
- CIBSE Guide M:2022, Table 8.1: Commissioning Savings by Building Type — indicates 8–15% EUI reduction from commissioning in educational buildings, with highest savings in buildings without prior commissioning.
- CIBSE Guide M:2022, Section 8.3: Ongoing Commissioning — recommends biennial verification of critical systems.

**ASHRAE**
- ASHRAE Standard 100-2018, Section 7: Building Operation and Maintenance — requires documented O&M procedures, control sequence verification, and performance tracking.
- ASHRAE Standard 100-2018, Section 7.3: Occupant Behavior and Control Persistence — addresses how operational drift erodes designed performance in schools.
- ASHRAE 90.1-2019 Section 6.7: Commissioning — requires commissioning for buildings > 10,000 ft².

**Other**
- AEDG50-K12-2011.pdf: Emphasizes commissioning, M&V, O&M training, and the building-as-teaching-tool concept as essential to achieving designed energy performance in K-12 schools.

## Assumptions
- School building is newly constructed or has undergone major renovation where commissioning was not previously performed.
- School district has a facilities management (FM) team with at least one dedicated HVAC technician and one electrical technician.
- School has or can install a building automation system (BAS) or standalone data logger infrastructure for trending.

## Climate Zone Relevance
All climate zones. The persistence benefit of ongoing commissioning is most valuable in climates with long heating or cooling seasons where equipment runtime is high and savings erosion compounds more rapidly.

## Interaction Notes
- Supports controls persistence for all other ECMs: without commissioning, occupancy sensor settings, daylight-responsive controls, and VAV box schedules drift within 12–18 months of occupancy.
- Complements the occupant dashboard ECM: dashboard data is most effective when FM staff have commissioning baseline data against which to measure drift.
- Essential for maintaining the performance of GSHP or VAV/DOAS systems which are highly sensitive to improper commissioning.

## Implementation Essentials
1. Conduct a pre-commissioning review: obtain design intent documentation (basis of design, O&M manuals, control sequences); compare to installed conditions; identify discrepancies before testing begins.
2. Perform commissioning per ASHRAE Standard 100-2018 Section 7.2 and the latest edition of ASHRAE Standard 180: HVAC Commissioning.
   - HVAC systems: test and verify all control sequences (VAV box reset schedules, AHU static pressure reset, CHW reset, mixed-air temp limits, exhaust fan interlock).
   - Lighting controls: test occupancy sensor coverage, time-delay settings, daylight sensor calibration, and override behavior.
   - Envelope: verify air barrier continuity, fenestration operation, and weatherstripping condition.
   - Kitchen equipment: test hood demand-control operation, appliance scheduling, and DHW setpoints.
3. Train FM staff on installed systems and expected operating sequences: minimum 8 hours of hands-on training per major system (HVAC, lighting, kitchen); document training completion in the O&M manual.
4. Install trending for all major end uses: HVAC runtime by zone, lighting panel kWh, kitchen exhaust fan runtime, DHW plant energy, and CO₂ concentrations in classrooms; minimum 15-minute resolution for 90 days post-commissioning.
5. Use dashboards or visible energy metrics in the school: display whole-building EUI, classroom lighting runtime, and HVAC runtime on a hallway display or web portal accessible to students and staff.
6. Integrate energy data into curriculum: math and science teachers use real utility data for lesson exercises; green building or sustainability elective uses building performance data for project-based learning.
7. Establish a recommissioning cycle: conduct a 30-day trending review at 6 months post-commissioning; conduct formal recommissioning sweeps at 12 months and 24 months post-occupancy; address all critical findings within 30 days.
8. Develop an ongoing M&V plan per IPMVP Option C (Whole Building Metered Energy): establish baseline EUI at commissioning; track monthly against baseline; investigate deviations > 5% from expected performance.

## Risks / Constraints
**Failure Mode — Training Not Retained After Turnover**: FM staff who received commissioning training leave within 12–18 months; new staff lack the understanding of design intent that commissioning established.

**Mitigation**: Require commissioning agent to deliver training to all FM staff, not just those present on commissioning day; maintain video recordings of training sessions in the O&M manual; include commissioning training in new-staff onboarding checklist.

**Failure Mode — Dashboard Installed Without FM Ownership**: Dashboard displays building data but no one in the FM or administrative team takes responsibility for acting on anomalies, making the dashboard a decorative element rather than a management tool.

**Mitigation**: Assign FM ownership of dashboard review at least weekly; integrate anomaly alerts into work-order system; report dashboard findings to school administration monthly; tie energy performance to FM staff performance goals.

**Failure Mode — Dashboard Without Curriculum Integration**: Display is installed but teachers are not given lesson plans or data access to use it, reducing student engagement and eliminating the behavioral persistence benefit.

**Mitigation**: Partner with math and science department heads during dashboard installation; provide at least 3 ready-to-use lesson modules in the first semester; refresh lesson content each semester to maintain student interest.

## KPIs
- Whole-building EUI (kBtu/ft²/year) — target: ≤ 5% drift from commissioning baseline at 12 and 24 months post-commissioning.
- After-hours HVAC runtime (hours/week per zone) — target: < 10% increase from commissioning baseline at 12 months.
- Lighting override counts per 100 fixture-hours — target: < 2 overrides per 100 fixture-hours per month.
- FM staff training hours completed per technician per year — target: ≥ 8 hours/year per major system.
- Dashboard usage sessions per month (if web-based) — target: ≥ 50 unique sessions per month for a school with 500+ students.
- Critical commissioning findings open at 30 days post-commissioning (%) — target: 0% critical findings open; 100% of non-critical findings open within 90 days.

## M&V Plan
- **IPMVP Option**: Option C (Whole Building Metered Energy) with targeted system trend review.
- **Quantification approach**: Establish commissioning baseline EUI (kBtu/ft²/year) at year 0; compare monthly EUI against baseline, normalized for weather (HDD/CDD per ASHRAE 90.1-2019 Appendix D) and occupancy (student attendance days). Investigate deviations > 5% with targeted system-level trending to identify root cause. Calculate savings from commissioning and engagement separately using before/after whole-building utility data.
- **Data collection**:
  - Whole-building electricity and natural gas consumption (monthly utility bills, minimum 12 months pre- and post-commissioning).
  - Student attendance days per month (school registrar data for normalization).
  - HDD/CDD from nearest ASHRAE climatic data station.
  - HVAC subsystem runtime and setpoints (BAS trend, 15-minute resolution, 90-day windows at commissioning and annually).
  - Lighting panel kWh (meter or BAS trend, monthly).
  - Work order data for HVAC and lighting complaints (CMMS export).

## Costs & Payback (indicative)
- **Capex**: Commissioning agent fees: $0.50–$1.50/ft² for new construction; $1.00–$2.50/ft² for existing building recommissioning. BAS trending configuration: $3,000–$10,000 per school. Dashboard hardware and installation: $5,000–$15,000 per school.
- **Opex**: $2,000–$5,000/year for annual trending review, recommissioning sweep, and FM staff training.
- **Simple Payback**: 2.0–4.5 years based on 8–15% EUI reduction from commissioning alone (valued at $0.08–$0.12/kBtu). Engagement program adds 3–8% additional savings at very low incremental cost.
- **ROI**: 22–50% over 5 years.

## Templates / Reuse
ASHRAE Standard 180:2021 Commissioning Process for HVAC Systems Checklist Template and CIBSE Guide M:2022 Appendix 8.A — Ongoing Commissioning Scope Checklist provide standardized formats for commissioning documentation applicable to K-12 school buildings.
