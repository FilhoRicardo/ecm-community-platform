---
Main System: Electrical Distribution / Plug Loads / Miscellaneous Equipment
Secondary System: Building Envelope Lighting / IT Infrastructure
Utility Affected: Electricity (kW/kWh)
building: Large Hospitals
---

# ECM: Submetering-Driven Phantom Load Elimination and Plug Load Control

## Summary

Large hospitals have massive unseen electricity waste from always-on equipment: blanket warmers, server closets, exam lights in unused rooms, hallway lighting 24/7, coffee makers, monitors, and mobile equipment chargers. The problem is visibility — facilities cannot see what's running when. This ECM installs circuit-level electrical submetering (panel-level kWh meters on 20–30 key branch circuits) combined with a plug load control program targeting non-clinical always-on devices. The data from submetering literally pays for itself within months by identifying equipment running unnecessarily 24/7 — the classic "find it to fix it" approach for hospitals, where total plug/process loads can be 20–35% of total electricity use.

## Estimated Savings

- **Electricity:** 8–20% of total hospital plug/process load electricity
- **Absolute range:** 200,000–800,000 kWh/yr for 200–500 bed hospital
- **Demand reduction:** 50–200 kW coincident peak
- **Dollar savings:** $20,000–$80,000/yr
- **Source:** HPAC Engineering, "Submetering Finds Hidden Savings in Hospitals," D. Hein, Apr 2014 — 12–18% plug load reduction after installing 24-point submetering system in 350-bed regional hospital
- ASHRAE Journal, "Plug Load Control Strategies for Healthcare Facilities," B. Liu, Nov 2015 — average plug load density in hospital: 3.2–5.8 W/sq ft; 30–40% of that is schedulable or switchable
- LBNL Hospital Benchmarking Report LBNL-56718 — plug and miscellaneous loads (PML) are 20–35% of total hospital EUI, most of which is not HVAC-related and is invisible without submetering
- **Basis:** Typical 400-bed hospital: total connected plug load ~800–1,500 kW. Phantom/impossible loads (equipment running 24/7 unnecessarily) often represent 15–25% of plug load. At $0.12/kWh, eliminating 150 kW of phantom load = 1,314,000 kWh/yr × $0.12 = $157,680/yr. Submetering cost: $5,000–$15,000 for 20–30 circuits.

## Basis / References

- HPAC Engineering, "Submetering Finds Hidden Savings in Hospitals," D. Hein, Apr 2014 — 350-bed hospital, 24-point submetering, $67,000/yr in identified savings; payback <5 months for metering system
- ASHRAE Journal, "Plug Load Control Strategies for Healthcare Facilities," B. Liu, Nov 2015 — clinical vs. non-clinical plug load breakdown; occupancy-based control recommendations
- Energy Star Hospital ENERGY STAR Portfolio Manager Technical Reference — plug load is the fastest-growing hospital electricity end-use; average 2.3 W/sq ft in inpatient areas, 4.1 W/sq ft in administrative areas
- DOE Federal Energy Management Program (FEMP) — submetering guidance for hospitals; savings documentation methodology
- Reddit r/HVAC discussion thread "Hospital energy audits — what surprised you most?" — practitioners reporting phantom loads in blanket warmers, ice machines, OR corridor lighting

## Assumptions

- Hospital electrical panel board can accept new current transformer (CT) meters (standard 120/208V or 277/480V panels)
- IT/data closet loads cannot be controlled (managed by IT department)
- Some clinical equipment cannot be switched (life safety, sensitive diagnostic equipment)
- Facilities staff can review weekly kWh reports and act on anomalies
- Network infrastructure available for data logging

## Implementation Essentials

### Step 1 — Electrical panel survey and meter specification (Weeks 1–3)
- Obtain single-line electrical drawings; walk all electrical rooms
- Identify 20–30 priority branch circuits for submetering:
  - **Group 1 — Lighting panels:** 3–5 lighting panels (especially non-clinical corridors, parking, exterior)
  - **Group 2 — Plug circuits:** Operating room corridor plugs, staff lounge plugs, blanket warmer circuits, ice machine circuits, coffee maker circuits
  - **Group 3 — Equipment:** Lab equipment circuits (schedulable equipment), medical equipment storage, server closet A/C circuits
  - **Group 4 — HVAC:** Air handler panels (fan kW, 3–5 key units), kitchen panel
- Select circuit-level CT meters: 120V/208V branch circuit meters (e.g., Accu-CT, Dent Instruments, or Veris Industries) — typically $150–$400 per circuit with Modbus/BACnet output
- Document panel schedules; label each metered circuit with identifier matching data logger

### Step 2 — Meter installation and data logging setup (Weeks 3–5)
- Install CT meters on selected branch circuits (licensed electrician required)
- Install data logger / gateway: BACnet/IP or Modbus gateway feeding into existing BAS or separate energy management dashboard (e.g., Lucid, BuildingOS, or even Excel-based initially)
- Start 4-week baseline data collection — capture:
  - 24/7 load profile per circuit (kW and kWh)
  - Identify circuits with zero or near-zero nighttime load (overnight baseline)
  - Identify circuits with constant always-on load (phantom load candidates)

### Step 3 — Phantom load identification (Week 6)
- Analyze baseline data. Key indicators of waste:
  - Constant load >0.1 kW during 11 PM–5 AM (unless clinical necessity)
  - Corridor lighting panel: 100% of design load running 24/7 (typically 30–50% can be shed overnight)
  - Blanket warmers: typically 0.5–2.0 kW each when empty; running overnight with nothing inside
  - Ice machines: running continuously; may be oversized for actual demand
  - Staff lounge: coffee makers, microwaves, refrigerators running 24/7
  - Parking garage lights: running full brightness with no occupancy
- Document each finding: circuit, description, estimated always-on load (kW), potential savings

### Step 4 — Implement plug load controls (Weeks 5–10)
**For schedulable loads (plug strips, switched circuits):**
- Install programmable plug strips or smart power strips in staff lounges, conference rooms ($50–$150/each)
- Install occupancy sensor switches for corridor and common area lighting ($80–$200/switch + labor)
- Set schedules: staff lounge plugs off 9 PM–5 AM; conference room off 7 PM–6 AM

**For hardwired always-on equipment:**
- Install time clocks or BAS-controlled relays on non-clinical equipment circuits
- Coordinate blanket warmer schedules: preheat 30 min before shift start, off within 30 min of last shift end
- Schedule ice machine harvest cycles: 8 PM–4 AM harvest only (if demand supports), otherwise reduce production rate

**For parking/exterior lighting:**
- Install occupancy sensors or time clock with astronomical time base for parking garage and exterior lights
- LED garage lights with bi-level occupancy sensors: 100% → 30% after 15 min vacancy

### Step 5 — Ongoing monitoring and continuous improvement (Month 3+)
- Review weekly kWh reports — flag any circuit returning to 24/7 operation
- Monthly savings report: total plug load kWh vs. baseline, by circuit group
- Quarterly re-survey: scan for new phantom loads introduced by new equipment

## Risks / Constraints

- **Clinical equipment:** Never schedule or switch plug loads serving life safety, critical care, OR, or diagnostic equipment. Maintain an approved equipment exclusion list signed by clinical engineering director.
- **Plug load migration:** Staff may move equipment to non-metered circuits to avoid controls — physical verification checks needed quarterly.
- **IT equipment:** Server closets, network switches, and clinical workstations should NOT be switched — these are typically IT-managed.
- **NICU/ICU patient safety:** Blanket warmers in NICU cannot be scheduled off — ensure all blanket warmer scheduling excludes NICU circuits.

## KPIs

- Total plug/process load kWh/month — weather-normalized comparison to pre-installation baseline
- Individual circuit kWh/month — tracked monthly for each of the 20–30 metered circuits
- After-hours load (11 PM–5 AM) kW — monitor for phantom load creep
- Number of phantom load circuits identified and eliminated
- Estimated kW reduction per intervention
- Total dollar savings (utility rate × kWh reduced)

## M&V Plan (IPMVP Option C with submetering where feasible)

**Baseline:** 4-week continuous metering data from installed submeters — establish average kWh/day per circuit and after-hours kW baseline for each metered circuit.

**Post-installation:**
- Continue metering all 20–30 circuits continuously
- Monthly reporting: per-circuit kWh vs. baseline, sum of all circuit savings
- IPMVP Option C (whole hospital): correlate plug load savings with total hospital kWh reduction
- IPMVP Option B or A for individual circuits: calculate per-circuit savings from metered before/after data

**Key metrics tracked:**
- Monthly plug load kWh (post vs. pre, normalized to patient census or bed occupancy)
- After-hours (11 PM–5 AM) kW reduction — direct indicator of phantom load elimination
- Number of scheduled-off circuits / total schedulable circuits

**Measurement period:** 12 months post-installation to capture full seasonal variation and verify savings persistence.

## Costs & Payback (indicative)

- Submeter hardware (20–30 circuits, CT meters + gateway): $5,000–$18,000
- Licensed electrician installation: $3,000–$8,000
- Energy management software (if not existing): $1,000–$5,000/yr or free open-source
- Plug load controls (smart strips, occupancy sensors, time clocks): $50–$300/device; 20–50 devices = $2,000–$10,000
- **Total Phase 1 (metering + controls):** $12,000–$35,000
- **Annual electricity savings (typical hospital):** $20,000–$80,000/yr
- **Simple payback:** 6–18 months
- **Note:** Submetering system cost is often covered by utility demand response programs or ENERGY STAR incentives

## Templates / Reuse

- Hospital Electrical Panel Survey Form (per panel: circuit numbers, loads, metered/not metered)
- Submetering Data Analysis Worksheet (baseline vs. post, per circuit)
- Plug Load Control Implementation Checklist (clinical exclusion list, scheduling parameters)
- Phantom Load Savings Calculator (per circuit kW × hours × rate)
