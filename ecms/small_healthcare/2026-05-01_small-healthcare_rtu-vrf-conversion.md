---
Main System: HVAC — Air Distribution
Secondary System:
Utility Affected: Electricity, Natural Gas
Building: Small Healthcare
---

# ECM: RTU VAV to VRF Conversion

## Summary

Replace aging rooftop units serving individual zones with Variable Refrigerant Flow (VRF) heat pump systems to achieve zoned comfort control and 30–50% better part-load efficiency. Small healthcare facilities (clinics, medical offices) typically operate multiple small RTUs independently at low efficiency. VRF systems modulate capacity precisely to zone loads, eliminating simultaneous heating and cooling and dramatically improving part-load performance — a critical deficiency in constant-volume RTUs serving low-occupancy or varying-load zones.

## Estimated Savings
- 20–35% HVAC energy (whole-building, based on field data)
- Clinic-specific — meter before and after per IPMVP Option C

## Basis / References
- ASHRAE Handbook — HVAC Systems and Equipment, Chapter 23 "Variable Refrigerant Flow" (authoritative practitioner reference covering design, sizing, and performance of VRF systems)
- AHRI 1230/2012 — VRF Heat Pump Water-Source Heat Pump Multi-Split Factory Certified Standard (product performance and rating standard)
- DOE/NREL/PNNL (Elsevier, 2025): "Commercial building HVAC demand flexibility with model predictive control: Field demonstration and literature insights" — https://doi.org/10.1016/j.enbuild.2025.116097 (DOE-funded field study)

## Assumptions
- Existing RTUs are ≥15 years old with degraded efficiency
- Building envelope and internal gains are stable (no major renovation in scope)
- VRF outdoor unit sized at 80% of peak load to leverage part-load efficiency
- Dedicated outdoor air system (DOAS) may be required separately for ventilation — VRF alone does not provide fresh air
- Refrigerant charge testing and capacity verification required per AHRI 1230

## Implementation Essentials
1. Survey existing RTU ages, capacities, refrigerant type, and condition — flag units approaching end of life
2. Engineer VRF system: outdoor unit capacity at 80% peak load; branch circuits to each zone; indoor units sized per zone loads
3. Install refrigerant piping, branch circuits, and indoor units — coordinate with HVAC contractor and owner's representative
4. Commission: refrigerant charge verification, cooling capacity test, heating capacity test per AHRI 1230
5. Integrate with BMS if present — VRF systems offer BACnet integration for monitoring and control
6. Establish baseline from pre-installation utility data; set up sub-metering for post-installation M&V

## Risks / Constraints
- **Infection control (healthcare):** Maintain pressurisation and fresh air delivery during construction — temporary HVAC bridging may be required in clinical zones
- **Refrigerant regulation:** Ensure selected refrigerant meets current F-gas / ASHRAE 15 safety standards for occupied spaces
- **Operational continuity:** Schedule phased cutover to avoid disrupting clinical operations
- **Code compliance:** ASHRAE 15 (refrigerant safety) and ASHRAE 62.1 (ventilation) must be satisfied — DOAS sizing may add cost

## KPIs
- HVAC kBtu/sq ft/yr (whole-building, monthly)
- RTU runtime hours (pre vs post)
- Tenant/patient temperature complaint count
- Simultaneous heating/cooling events (if BMS-tracked)

## M&V Plan (IPMVP Option C with submetering where feasible)
- Install dedicated HVAC sub-meter on VRF outdoor unit circuit
- Collect 12 months pre-installation baseline (whole-building HVAC kBtu from utility bills + any existing sub-meters)
- Post-installation: monthly HVAC kBtu/sq ft/yr, compare to baseline; normalize for weather (HDD/CDD)
- If BMS integration is present, cross-check against VRF controller runtime data

## Costs & Payback (indicative)
- VRF system installed cost: £150–£300/tonne (mid-rise clinic, EU market; USD equivalent ~$160–$320/tonne)
- Payback: 5–10 years (favorable for clinics with high RTU runtime and varying loads; utility incentives may improve economics)

## Templates / Reuse
- Standard ECM template
