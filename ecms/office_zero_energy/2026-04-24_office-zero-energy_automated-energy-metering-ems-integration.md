---
Main System: Metering / BMS Integration
Secondary System:
Utility Affected: Electricity, Natural Gas
Building: Office — European Portfolio
---

# ECM: Automated Energy Metering / EMS Integration (Modbus/BACnet to SavIQ)

## Summary

**What:** Connect existing utility meters to a remote EMS (SavIQ or equivalent) via Modbus/BACnet/OPC-IP to replace manual monthly reads with automated half-hourly data. At UN Studio Tower, reads are twice-yearly — effectively useless for anomaly detection.

**Why:** Manual reads at monthly or twice-yearly frequency make billing validation and anomaly detection impossible. Half-hourly automated data is prerequisite for IPMVP Option C M&V, AI overlay, and Baselining.

## Estimated Savings
- Indirect (infrastructure)
- N/A

## Basis / References
- Portfolio basis: XYZ Building, Radisson Blu Stansted, SOM, ITO, UN Studio Tower

## Assumptions
- Building-specific survey required before implementation
- Energy audit recommended to quantify baseline and savings

## Implementation Essentials
1. 1) Survey all utility meters — note communication protocol (Modbus, BACnet, pulse output). 2) Install protocol converters or new meters where pulse output is the only option. 3) Configure EMS gateway to poll meters. 4) Set up automated data push to SavIQ or equivalent. 5) Establish baseline and configure anomaly alerts.

## Risks / Constraints
- Infrastructure, not direct saving. Prerequisite for all performance-contracted ECMs.

## KPIs
- Meter data resolution (reads/day)
- Anomaly detection alerts (#/month)
- Manual vs automated data effort (hrs/month)

## M&V Plan (IPMVP Option C with submetering where feasible)
- Pre-installation baseline: 90-day continuous monitoring
- Post-installation: compare same period following year (weather-normalised)
- IPMVP Option C: Whole-building metering with regression analysis

## Costs & Payback (indicative)
- Payback: 6–18 months
- Cost: Requires building-specific survey and contractor pricing
