---
Main System: BMS / Data Infrastructure
Secondary System:
Utility Affected: Electricity
Building: Office — European Portfolio
---

# ECM: BMS Trend Analysis / Logging Module

## Summary

**What:** Enable BMS data logging and trend analysis — typically a licence unlock or configuration change on modern BMS platforms (Honeywell Niagara, Siemens Desigo, Tridium BAS).

**Why:** Zero direct saving, but unlocks every other BMS-based ECM. Without trend data, fault detection, schedule validation, and setpoint drift monitoring are impossible.

## Estimated Savings
- Indirect (enabler)
- N/A — infrastructure

## Basis / References
- Portfolio basis: XYZ Building, SOM Building, ITO Building

## Assumptions
- Building-specific survey required before implementation
- Energy audit recommended to quantify baseline and savings

## Implementation Essentials
1. 1) Audit current BMS licence status — identify which modules are disabled. 2) Purchase licence unlock from BMS vendor or configure onboard logging. 3) Set up trend logging for key points: zone temp, OA damper %, fan kW, heating valve %. 4) Integrate with EMS platform (SavIQ, Nagios) or designate a person to review weekly.

## Risks / Constraints
- Prerequisite for all other BMS ECMs. Assign a named person to act on data or it is worthless.

## KPIs
- Trend points logged (#)
- Data resolution (15-min vs hourly)
- Time spent on manual reads (hrs/week)

## M&V Plan (IPMVP Option C with submetering where feasible)
- Pre-installation baseline: 90-day continuous monitoring
- Post-installation: compare same period following year (weather-normalised)
- IPMVP Option C: Whole-building metering with regression analysis

## Costs & Payback (indicative)
- Payback: Enabler only
- Cost: Requires building-specific survey and contractor pricing
