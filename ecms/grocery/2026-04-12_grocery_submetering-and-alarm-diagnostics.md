---
Main System: Building Management System (BMS) + Electrical Distribution
Secondary System: Refrigeration Rack Controller + HVAC Controls
Utility Affected: Electricity (kWh) + Natural Gas (therm)
Building: Grocery
---
# ECM Description: Submetering and BMS Alarm-Based Diagnostics to Target Phantom and Off-Hours Loads

## Summary
Install electrical sub-metering on the major end-use branches in a grocery store — refrigerated case racks, HVAC RTU/air handlers, walk-in cooler/freezer, lighting panels, and plug loads — and configure BMS alarm logic to flag anomalous consumption during unoccupied hours and identify equipment that runs when it shouldn't. Most grocery stores are "meter-deep": they have only a whole-building kWh meter, so operators can't see that a RTU is running at full capacity at 2 AM or that a walk-in compressor is short-cycling. Submetering (at $500–$3,000 per circuit branch) combined with a structured alarm response protocol transforms the BMS from a monitoring tool into an energy waste detection system. This is the ECM that enables all other ECMs — without data, no one knows what's broken.

## Estimated Savings
- **5–15% of total store electricity** is typically lost to off-hours phantom loads, mis-scheduled equipment, and unresolved equipment faults discovered only through sub-metering
- **Case study — DOE Femp Supermarket Case Study**: a 62,000 ft² supermarket installed $8,000 of sub-metering and discovered: RTU running 24/7 (should be setback 20 hrs/day), walk-in cooler compressor short-cycling (stuck TXV), and case lighting running fullbright 4 hours before open. Fixing these three issues alone saved $18,400/year.
- **Submetering cost**: $5,000–$15,000 installed for 8–12 branch CTs on a typical grocery.
- **Annual savings from discovered issues**: $10,000–$25,000/year for a typical store (highly variable — some stores have more waste than others).
- **Net benefit**: Submetering pays for itself within 6–18 months through waste identification alone, before any ECMs are even implemented.

## Basis / References
- **DOE/LBNL "Assessment of Energy Savings Potential in Supermarkets"** (LBNL-56602): found that the average supermarket has 12–18% of total energy use attributable to equipment running during unoccupied hours unnecessarily; identified sub-metering as the primary diagnostic tool to uncover this waste
- **HPAC Engineering** (2016): "Getting What You Pay For: Submetering in Commercial Buildings" — profiled grocery applications; documented case studies where sub-metering identified HVAC runtime excess of 30% above schedule
- **PNNL Supermarket Field Study** (PNNL-25362): recommended submetering as the first step in any supermarket energy audit; found that only 30% of surveyed stores had any sub-metering beyond the utility meter
- **Eng-Tips forum thread #447821**: "Supermarket energy audit — where is all the electricity going?" — engineers discussing submetering CT placement and how to use rack controller data for diagnostics; consensus: "You can't manage what you don't measure"
- **ASHRAE Guideline 14**: Measurement of Energy and Demand Savings — specifies M&V requirements; grocery end-use breakdown from ASHRAE research: refrigeration 40–50%, HVAC 20–25%, lighting 15–20%, plug loads 10–15%
- **Practical experience (HVAC-Talk field techs)**: multiple posts documenting that simply installing a BMS trend log on a RTU schedule and comparing to actual runtime revealed 200–400 hours/year of unnecessary RTU runtime per unit

## Assumptions
- Store has a BACnet, Modbus, or LonWorks BMS (most 2000s+ construction grocers have this; if not, a standalone data logger system is an alternative)
- Electrical panel has space for additional CTs on branch circuits (standard 200A panels with CT-ready meters)
- BMS operator has basic training and will respond to alarms within 24 hours (alarm fatigue is a real risk — thresholds must be set carefully)
- Utility rate schedule is known (kWh + demand charges); savings will be calculated in both

## Implementation Essentials
**Step 1 — Electrical distribution mapping (Week 1)**
- Obtain or create a one-line diagram of the store's electrical service: main breaker, distribution panels, major branch circuits.
- Identify the 8–12 highest-load branch circuits: (1) MT refrigeration rack compressor, (2) LT refrigeration rack compressor, (3) each RTU or air handler, (4) walk-in cooler/freezer panel, (5) display case lighting, (6) interior lighting panel, (7) exterior/Signage, (8) plug loads.
- Verify CT installation location: usually on the load side of the branch breaker in the distribution panel.

**Step 2 — Hardware selection and installation (Week 2)**
- Select sub-meter hardware:
  - **For BMS-integrated**: Veris, Belimo, Schneider PowerLogic, or Eaton sub-meters with BACnet/IP output (~$500–$1,200 per circuit).
  - **For standalone logging**: HOBO UX120-006M or similar 4-channel kW loggers (~$300–$600 per circuit; no BMS integration but easier to install).
  - CT size: match to breaker rating (100A, 200A, 400A panels; split-core CTs for easy installation without pulling conductors).
- Install CTs per manufacturer instructions; verify polarity and orientation.
- Commission: confirm all readings match whole-building meter within 5%.

**Step 3 — BMS alarm configuration (Week 2–3)**
- Configure the following BMS alarm rules (examples, tuned to the specific store):
  - **Alarm: RTU Runtime > 2 hours during unoccupied hours** (trigger: any air handler running when store is unoccupied).
  - **Alarm: Any compressor running when all cases report satisfied** (indicates failed TXV, stuck reversing valve, or low-load runaway).
  - **Alarm: Case lighting kW > 10% of schedule during closed hours** (left-on overnight, signage left on).
  - **Alarm: Walk-in cooler/freezer temperature rise > 5°F in 30 minutes** (indicates fan failure or door left open).
  - **Alarm: Demand > 85% of billable demand threshold** (indicates equipment staggering failure).
  - **Alarm: Sub-meter kW > baseline + 3 sigma** during unoccupied hours (statistical anomaly detection).

**Step 4 — Baseline and benchmarking (Week 3–4)**
- Run 4 weeks of baseline with new submetering. Generate end-use breakdown chart:
  - % refrigeration, % HVAC, % lighting, % plug loads.
  - Compare to ASHRAE Guideline 14 end-use benchmarks for similar-size grocers.
  - Identify which end uses are outliers vs. peers.

**Step 5 — Alarm response SOP (Month 2)**
- Write a one-page alarm response protocol: who gets the alarm (facilities manager), how quickly they must respond, and what to look for.
- Example: RTU overnight runtime alarm → facilities tech checks BMS trend → confirms RTU is running → checks space temp sensor (is it reading wrong?) → checks occupancy schedule (was it accidentally changed?) → documents finding.
- Review alarm log monthly: categorize resolved issues by root cause; identify recurring patterns.

**Step 6 — Quarterly energy review (Ongoing)**
- Monthly: end-use kWh trend, off-hours runtime hours vs. schedule, demand peaks.
- Quarterly: compare to prior quarter, adjust alarm thresholds based on what constitutes a "real" issue vs. normal variation.
- Annual: full ECM prioritization update based on submeter data.

## Risks / Constraints
- **Alarm fatigue**: Too many alarms = ignored alarms. Start with 3–5 high-value alarms; add more as the team builds response discipline.
- **CT accuracy at low loads**: Some CTs have poor accuracy below 10% of rated current. Verify accuracy spec is ±2% or better across the range.
- **BMS integration complexity**: If BMS is older (legacy Johnson Controls or older Trane), BACnet integration may require additional gateway hardware ($1,000–$3,000).
- **Data overload**: Trend logging at 1-minute intervals generates large data sets. Use 15-minute for most KPIs; 1-minute for fault diagnosis only.
- **Utility data access**: Some utilities restrict interval data access. Request 15-minute interval data directly from utility — most will provide for free to commercial customers.

## KPIs
1. **Off-hours kWh** (% of total, by branch) — target: <5% of total store kWh in unoccupied hours
2. **RTU unoccupied runtime hours** (hours/year) — target: <500 hours/year (vs. 8,760 possible); current stores often see 1,500–3,000
3. **Alarm response time** (hours from alarm to investigation) — target: <24 hours
4. **Alarm resolution rate** (% alarms resolved within 7 days) — target: >80%
5. **Demand charge** ($/kW-month) — track monthly; reduction indicates better load management
6. **Energy Use Intensity (EUI)** (kBtu/ft²/year) — compare to ENERGY STAR Food Sales grocery benchmark (source energy)

## M&V Plan (IPMVP Option C with submetering where feasible)
- **IPMVP Option**: C (Whole Building) for store-level savings; Option B (Key Parameter Measurement) for specific discovered wastes.
- **Pre-retrofit**: Utility bill baseline + estimate from submeter audit (pre/post audit savings attribution).
- **Post-retrofit**: 12 months of submeter data; savings = (pre-level − post-level) adjusted for weather/occupancy.
- **Granularity**: With branch-level submetering, savings from each identified waste can be isolated and reported separately (e.g., "RTU overnight runtime eliminated: 2,100 kWh/year").
- **DOE 50001 Ready recognition** (optional): Submetering system can serve as the data collection infrastructure for ISO 50001 Energy Management System certification.

## Costs & Payback (indicative)
- **Sub-meter hardware** (8–12 CT channels + meter): $3,000–$12,000 (BACnet-integrated) or $1,500–$5,000 (standalone loggers).
- **BMS alarm configuration labor**: $1,500–$3,500 (controls contractor or in-house BAS tech).
- **Electrical installation labor** (CT installation): $1,000–$2,500 (licensed electrician).
- **Total installed**: **$6,000–$18,000**.
- **Annual savings**: $10,000–$30,000/year (waste elimination + demand charge reduction + utility rebate qualification).
- **Simple payback**: **0.5–1.8 years** — highest ROI first step in any grocery energy program.

## Templates / Reuse
- Grocery electrical branch inventory template (panel, breaker, CT channel, end use, HP/kW)
- BMS alarm configuration template (alarm name, trigger condition, threshold, recipient, SOP step)
- Monthly energy dashboard template (end-use pie chart, off-hours runtime bar chart, EUI trend)
- Submetering commissioning checklist (CT polarity check, accuracy verification vs. utility meter)
