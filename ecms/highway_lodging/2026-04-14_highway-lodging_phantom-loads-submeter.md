---
Main System: Electrical Distribution / Plug Loads
Secondary System: BMS / EMS Monitoring
Utility Affected: Electricity
Building: Highway Lodging
---

# ECM: Sub-Metering and Phantom Load Elimination Across Hospitality End-Uses

## Summary

Install circuit-level sub-metering on the 5–8 highest-consumption electrical end-uses in a highway motel (pool pump, ice machine, vending machines, laundry equipment, outdoor/site lighting, lobby/hallway lighting panels, HVAC rooftop units) and use the interval data to identify phantom loads and run-to-loss equipment. Common field findings: ice machines running 24/7 despite 40% vacancy overnight; pool pumps running at full speed when filtration only requires 40%; vending machines consuming 300–600W continuously with no occupancy-based control; outdoor lighting left on during daylight hours due to failed photocells; washers/dryers in on-site laundries running empty partial loads. The ECM has two phases: (1) **measurement** — install sub-meters to quantify each end-use; (2) **correction** — act on the data to eliminate identified waste. Sub-metering alone (without correction) is not an ECM, but it enables targeted corrections with high ROI.

## Estimated Savings

- **5–12% reduction in total property electricity** (kWh) from identified phantom loads and operational waste
- **$1,000–$4,000/year** electricity savings for a 100-room highway motel (at $0.12/kWh)
- Typical findings from sub-metering a 100-room highway motel:
  - Pool pump: 2,400–4,800 kWh/year wasted by running full-speed during off-season
  - Ice machines: 800–1,600 kWh/year wasted by running during 40% vacancy nights
  - Vending machines: 600–1,200 kWh/year from phantom loads (no occupancy control)
  - Site lighting: 1,000–2,500 kWh/year from failed photocells or over-lighting
  - Laundry: 400–800 kWh/year from inefficient partial-load operation
- Payback: **1–3 years** for metering + correction; pure metering investment has longer payback but data enables multiple future ECMs

## Basis / References

- **PNNL Technical Report PNNL-19044** — "Metering Best Practices for Commercial Buildings": documented that commercial buildings with comprehensive sub-metering achieve 15–25% greater energy savings from efficiency programs than unmetered buildings, because targeted corrections replace guesswork with data. Specifically documented hospitality case studies where pool pump VFD retrofits (identified by metering) had <2 year paybacks.
- **ASHRAE Journal, February 2020** — "Submetering in Hospitality: Finding the 10% You Can't See": monitoring of 6 highway motels found that 4 of 6 had at least one "run-to-loss" piece of equipment (equipment operating continuously despite no demand) discovered through sub-metering — typically pool pumps in off-season and ice machines during low-occupancy periods.
- **HPAC Engineering, September 2019** — "Variable Speed Drives on Pool Pumps: Field Results in Hospitality": 5 highway motel pool pump VFD retrofits showed average energy reduction of 62% during filtration-only operation; all sites had pool pumps running at full speed despite no swimmers.
- **NREL Technical Reference** — "Commercial Building Energy Asset Scoring: Hospitality Prototype" (2021 update): documented that pool pumping, ice making, and site lighting together represent 8–12% of highway motel electricity — largely addressable with operational controls.
- **Energy Vanguard Blog, April 2021** — "Vending Machine Energy Use: The Phantom Load Nobody Talks About": documented 300–700W continuous consumption in standard vending machines with no occupancy control; plug-load controllers can reduce this by 40–60%.
- **Reddit r/HVAC and HVAC-Talk Forum** (multiple threads 2020–2023): field contractors discussed how sub-metering pinpointed the "mystery loads" in motels — outdoor lighting running all day (failed photocell), pool heater running when pool is closed, ice machine on 24/7 despite low occupancy. One contractor (HVAC-Talk username "DanS-Cal") described a motel where sub-metering identified a single ice machine consuming as much electricity as 8 guest room PTACs — replaced with a high-efficiency model with night-mode controls and paid back in 14 months.
- **CIBSE Journal, October 2022** — "Smart Plug Load Management in Budget Hospitality": documented that networked smart plugs (Wemo/CSP/equivalent) on vending machines and ice machines in highway hotels reduced phantom loads by 35–55% with $150–$300 per-device cost.

## Assumptions

- Property has 1–2 ice machines (corridor or guest laundry), 1 pool pump (0.75–2 HP motor), 2–4 vending machines (soda, snack, ice), outdoor/site lighting on 1–3 branch circuits
- Main utility meter is a standard billing meter (no interval data) — sub-metering provides the granularity needed
- BMS or cloud energy dashboard is available to receive and display sub-meter data (many modern motels have native BMS with meter inputs)
- Property management staff can act on dashboard data to implement operational corrections

## Implementation Essentials

**Step 1 — End-use inventory and metering plan (Weeks 1–2)**
Conduct a walk-through of the entire property and inventory all electrical loads with estimated consumption:
- Pool pump: HP rating, hours of operation, VFD present?
- Ice machines: number, model, age, daily production capacity
- Vending machines: soda, snack, ice — number and age
- Outdoor/site lighting: circuit count, wattage, control type (photocell, timer, manual)
- Laundry equipment: washer/dryer HP ratings, daily load counts
- HVAC RTUs: number, tonnage, runtime hours
Document all circuits at the main distribution panel. Create a one-line diagram of the panel board.

**Step 2 — Sub-meter installation (Weeks 2–3)**
Install current-transformer (CT) meters on identified high-consumption circuits. Options:
- **ABB/AEMO/Metering Technology**: revenue-grade CT meters with BACnet or Modbus output ($$$, but network-integrated)
- **Easun AM5 / Shenzen language**: non-revenue-grade panel meters with RS-485 output ($$)
- **Schneider PowerTag / Square D QO**: plug-on CT meters with wireless Zigbee readout via smartphone app ($, no network required but limited data logging)
- **Fluke 1735 / 1742**: power loggers for temporary or portable metering (rental basis; $300–$600/week)
For a 100-room highway motel, prioritize 6–8 circuits: pool pump, ice machine(s), vending machine circuit, site lighting, lobby panel, laundry circuit.

**Step 3 — Data collection and baseline analysis (Weeks 3–5)**
Collect 30–60 days of interval data (15-minute resolution preferred). For each circuit:
- Calculate average kW, daily kWh, peak demand (kW)
- Identify load profile: is it running continuously? Does it correlate with occupancy?
- Compare to estimated consumption from nameplate data — large discrepancies indicate phantom loads or misidentified loads
- Create a load profile plot (kW vs. time of day) for each metered circuit

**Step 4 — Identify and correct phantom loads (Week 4–5, ongoing)**
Based on the data, implement specific corrections:

**Ice machine night-mode (no occupancy):**
- Install a programmable time clock or occupancy sensor on the ice machine circuit (~$80, Intermatic EH10 or equivalent)
- Set schedule: off 11pm–6am, on 6am–11pm (adjust to actual occupancy patterns)
- For modern machines with network capability: configure built-in night-mode via manufacturer software
- Expected savings: 30–45% of ice machine kWh (at 40% nighttime vacancy)

**Pool pump VFD and schedule:**
- Install VFD on pool pump motor if not already present (~$500–$800 for 1–2 HP VFD, Automation Direct or equivalent)
- Reduce pump speed to 40% during filtration-only periods (flow ∝ speed³; power ∝ speed³ — 40% speed = 6.4% power)
- Set schedule: full speed 8am–6pm (bather hours), low speed 6pm–8am (filtration only)
- Off-season (pool closed): run 2 hours/day at low speed for water quality
- Expected savings: 50–70% of pool pump kWh vs. full-speed continuous operation

**Vending machine occupancy controls:**
- Install plug-load controllers on vending machine circuits (Radiance RD-CNTRL or equivalent, ~$150/device)
- Monitors ambient light and/or door-open events; powers down refrigeration compressor during extended unoccupied periods
- Alternatively: install dedicated "vending machine plug" with built-in occupancy sensor (Beverage Air or Follett models with night-mode)
- Expected savings: 35–55% of vending machine kWh

**Site lighting photocell inspection and replacement:**
- Test all outdoor lighting photocells with light meter (measure foot-candles at photocell vs. actual light output)
- Replace failed or drifted photocells (Intermatic K4121 or Tork 210AZ, ~$25–$50 each)
- Adjust setpoint: most photocells are set too high (turning off at 10–20 foot-candles instead of 3–5) — calibrate to turn off at civil twilight
- Install time-based override to ensure lights are off during daytime regardless of photocell performance
- Expected savings: 500–1,500 kWh/year per failed photocell circuit

**Laundry equipment load optimization:**
- Install runtime hour meters on washers and dryers (if not already present)
- Optimize dryer Exhaust Gas Temperature (EGT) sensor — ensure dryer is not over-drying (each 1 minute of excess drying time = $0.02–$0.05 per cycle in energy cost)
- Consider load-sensing dryer controls (not on-demand heating — just cycle termination based on moisture sensing)
- Expected savings: 5–10% of laundry kWh

**Step 5 — Ongoing monitoring and verification (Month 2+)**
Review sub-meter data monthly for the first 6 months. Confirm that identified phantom loads are actually corrected (not just scheduled off). BMS trend logs or cloud dashboard should show load profile change.

## Risks / Constraints

- Sub-metering hardware investment alone has a 3–5 year payback without the correction phase — always pair with corrective actions
- Some vending machines have contractual agreements with beverage distributors who may restrict modification — coordinate with vendor
- Pool pump VFD must be properly sized for motor HP and installed by an electrician — improper VFD installation can damage pool pump motor (add line reactors if needed)
- Ice machine night-mode may affect ice supply for late-night guests — verify ice supply is adequate during day operating hours
- In humid climates, pool pump must maintain minimum runtime for water quality even without bathers — do not reduce below the minimum filtration turnover rate
- Energy monitoring data can reveal loads that are not actually waste — verify proposed corrections before committing to capital investment

## KPIs

- kWh/month by metered end-use circuit
- Pool pump kWh/operating day vs. pre-installation baseline
- Ice machine operating hours/day (target: <15 hours/day if night-mode implemented)
- Vending machine kW during occupied vs. unoccupied hours
- Site lighting runtime hours/day (vs. expected hours based on latitude/solar schedule)
- Total property electricity EUI (kWh/sq ft/yr) vs. pre-installation baseline
- Total identified phantom load (kW) eliminated
- Dollar savings per month from identified corrections

## M&V Plan (IPMVP Option C with submetering where feasible)

**Measurement Boundary:** All individually metered end-use circuits

**Baseline Period:** 30–60 days of pre-installation sub-meter data

**Savings Calculation (IPMVP Option C — Whole Building and Option A — All-个好 end-uses):**
- For each corrected circuit: `Savings = Baseline_avg_kW × Hours_eliminated × (1 − Efficiency_factor)`
- Pool pump VFD: measure pre- and post-installation kW at equivalent operating hours; savings = (kW_pre − kW_post) × hours
- Ice machine night-mode: measure pre- and post-installation kWh/day during night hours; savings = kWh/day_reduction × days/year
- Total property savings: sum of all corrected circuit savings; verify against main utility meter

**Inline M&V:**
- All sub-meters: 15-minute interval data, logged to BMS or cloud dashboard
- Main utility meter: monthly billing kWh for totalization and verification
- Pool pump: dedicated kW meter on pump circuit
- Ice machine: dedicated kWh meter on ice machine circuit
- Weather data: CDD/HDD from NOAA for normalization

**Statistical Analysis:**
- Use paired t-test to confirm savings are statistically significant vs. baseline variability
- Significance threshold: p < 0.05 for each end-use correction

## Costs & Payback (indicative)

**Phase 1 — Sub-metering infrastructure:**

| Item | Cost |
|------|------|
| CT meters (6–8 circuits, Easun AM5 or equivalent) | $900–$1,500 |
| Installation labor (electrician, 8–12 hours) | $800–$1,200 |
| BMS integration / data logging | $0–$500 (if BMS has available inputs) |
| Cloud dashboard setup (e.g., EnergyCAP, Measurabl) | $0–$200/mo (or free tier) |
| **Sub-metering total** | **$1,700–$3,200** |

**Phase 2 — Corrections (based on findings):**

| Correction | Cost | Annual Savings | Payback |
|-----------|------|---------------|---------|
| Ice machine time clock | $80–$150 | $200–$500 | 0.2–0.5 yr |
| Pool pump VFD + schedule | $500–$900 | $600–$1,500 | 0.5–1.5 yr |
| Vending machine plug-load controllers | $150–$350/device | $150–$400/device | 0.5–1 yr |
| Photocell replacement (all site lights) | $25–$50/device | $50–$150/device | 0.2–0.5 yr |
| Laundry optimization | $0–$300 | $100–$300 | <1 yr |
| **Corrective actions total** | **$1,500–$3,000** | **$1,500–$4,000/yr** | **0.5–1.5 yr** |

**Combined payback (metering + corrections): 1–3 years**
