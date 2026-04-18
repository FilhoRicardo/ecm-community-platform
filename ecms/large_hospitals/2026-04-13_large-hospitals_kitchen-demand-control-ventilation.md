---
Main System: Kitchen / Commercial Kitchen Hood Exhaust
Secondary System: Make-Up Air Units (MUA) / Kitchen HVAC
Utility Affected: Natural Gas (heating), Electricity (exhaust fan kWh)
building: Large Hospitals
---

# ECM: Kitchen Hood Demand Control Ventilation

## Summary

Hospital kitchens (employee cafeterias, patient food service) run exhaust fans at full speed and supply makeup air units at full heat regardless of cooking load. Hospital kitchens typically run only 3–4 hours of peak cooking per day, leaving exhaust/MUA running at full capacity for 10–12 hours unnecessarily. Demand control ventilation (DCV) uses roof-mounted optical smoke/heat sensors or current sensors on cooking appliances to modulate exhaust fan speed and MUA heating output proportionally to actual cooking activity — maintaining capture velocity when needed and reducing to standby when hoods are cold.

## Estimated Savings

- **Electricity:** 30–50% reduction in kitchen exhaust fan kWh (fans run 40–60% of design airflow during idle periods)
- **Natural Gas:** 20–40% reduction in kitchen makeup air unit heating energy (MUA supplies conditioned air year-round)
- **Absolute range:** 15,000–50,000 kWh/yr fan savings + 5,000–15,000 therms/yr gas savings for a 400-meal/day hospital kitchen
- **Dollar savings:** $8,000–$22,000/yr
- **Source:** ASHRAE Journal, "Demand Control Kitchen Ventilation," T. Crabtree, Aug 2013 — 35–45% exhaust fan kWh savings in hospital kitchen with optical sensor DCV
- HPAC Engineering, "Smart Kitchen Hoods Cut Energy Costs," K. Wray, Feb 2016 — case study: 400-bed hospital cafeteria; $18,500/yr combined savings; 16-month payback
- **Basis:** Fan affinity law: BHP ∝ RPM³. Reducing exhaust fan speed from 60Hz to 30Hz cuts fan power to 12.5% of full load. MUA at idle (no cooking) can modulate to 20–30% of full heating capacity. Hospital kitchen idle periods (overnight prep, off-peak service) can be 60–70% of operating hours.

## Basis / References

- ASHRAE Journal, "Demand Control Kitchen Ventilation," T. Crabtree, Aug 2013 — ASHRAE Research Project 1620; lab and field validation of optical sensors vs. temperature-based DCV; hospital case study included
- HPAC Engineering, "Smart Kitchen Hoods Cut Energy Costs," K. Wray, Feb 2016 — 400-bed hospital kitchen, $18,500/yr savings, 16-month payback; optical sensor-based DCV
- ASHRAE Handbook—HVAC Applications, Chapter 33 (Mounted Kitchen Exhaust Hoods) — capture and containment velocity requirements; minimum exhaust rates at idle
- NFPA 96 (Standard for Ventilation Control and Fire Protection of Commercial Cooking Operations) — minimum exhaust rates,不允许 dropping below design velocity when cooking; DCV systems must comply with NFPA 96 §11 and maintain capture velocity of ≥50 fpm at hood face during active cooking
- Energy Star Food Service Equipment Calculator — savings methodology for DCV hoods

## Assumptions

- Hospital kitchen has Type I (grease) exhaust hood(s) over cooking appliances
- Existing exhaust fans and MUA are constant-speed; VFD-ready or can accept VFD retrofit
- Kitchen operates ≥8 hours/day, with identifiable idle periods
- Kitchen hood capture velocity currently meets NFPA 96 requirements (hood is not already marginal)
- Facilities has capacity to coordinate with hood cleaning contractor and fire alarm vendor

## Implementation Essentials

### Step 1 — Kitchen operating profile analysis (Weeks 1–2)
- Document current kitchen schedule: cooking hours, meal prep peaks, idle periods
- Typical hospital kitchen profile:
  - 4:30–7:00 AM: breakfast prep (low load)
  - 11:00 AM–1:30 PM: lunch service (peak)
  - 4:30–7:00 PM: dinner service (medium load)
  - 8:00 PM–4:00 AM: overnight prep (low, often one pilot appliance)
- Confirm which appliances are on which hood sections
- Note: hospital kitchens often run patient meal delivery 3× daily but most cooking uses only 30–50% of available hood capacity at any one time

### Step 2 — Sensor selection and specification (Weeks 2–4)
- **Option A — Optical/thermal array sensors:** Mounted above hood, detect heat and smoke plume from cooking appliances; output is a 0–10VDC or Modbus signal proportional to cooking intensity. Cost: $800–$2,500 per hood section.
- **Option B — Current transformers (CTs) on appliance circuits:** CTs clamp around appliance power leads; cooking activity triggers proportional fan speed signal. Cost: $200–$400 per appliance circuit.
- **Recommended for hospital kitchen:** Option A (optical sensors) — more reliable in 24/7 kitchen environments with variable appliance loads; CTs on major appliances (ovens, ranges) can supplement
- Specify VFD-compatible exhaust fans (or VFD retrofit if fans are direct-drive)

### Step 3 — VFD installation on exhaust fans (Weeks 3–6)
- Install VFDs on kitchen exhaust fans (typically 2–5 HP each) and MUA supply fan (typically 5–15 HP)
- Configure VFD to accept DCV signal (0–10VDC from sensor controller) as speed command
- **Critical NFPA 96 compliance:** Set minimum speed at 30% of design RPM (or minimum capture velocity 50 fpm) — never allow hood to fall below minimum exhaust requirement during active cooking
- Install HOA (Hand/Off/Auto) switch at each VFD for manual override
- Integrate with existing kitchen hood fire suppression system — fire alarm system override must close dampers and kill DCV to full speed on alarm

### Step 4 — BAS/Kitchen management system integration (Weeks 5–8)
- Connect DCV controller output to BAS as Modbus or BACnet IP
- Configure kitchen BMS to:
  - Track exhaust fan speed %, MUA heating valve position %, sensor input signal
  - Generate alarm if exhaust fan speed drops below NFPA minimum for >5 minutes during cooking hours
  - Log daily kitchen energy consumption by end-use (exhaust fan kWh, MUA gas)
- Coordinate with kitchen hood cleaning contractor to update service records with DCV modifications

### Step 5 — Commissioning and fire code verification (Weeks 7–9)
- Fire marshal inspection: confirm DCV system complies with NFPA 96 §11 (automatic shutoff, emergency override)
- Test emergency override: simulate fire alarm — exhaust fans must go to full speed, MUA dampers must close
- Verify capture velocity at minimum speed using anemometer — minimum 50 fpm at hood face with all appliances operating
- Document NFPA compliance with inspection sign-off

## Risks / Constraints

- **NFPA 96 compliance:** This is the single biggest constraint. NFPA 96 §11 requires DCV systems to maintain capture and containment during cooking. Minimum exhaust rates must be verified. Coordinate with fire marshal before implementation.
- **Grease-laden exhaust:** Sensor placement in the hood plenum must avoid grease accumulation — use sealed, IP66-rated sensors.
- **Steam from dishwashing:** Dishwasher exhaust (often on separate hood) can trigger false positives — ensure dish hood is on separate DCV circuit from cooking hood.
- **VFD harmonic distortion:** Large VFDs on kitchen exhaust fans can introduce harmonic distortion into facility electrical system — specify VFD with ≤5% THD or add harmonic filter if required by utility.

## KPIs

- Exhaust fan speed (%) — trend daily by hour (compare to cooking schedule)
- MUA heating valve position (%) — trend daily
- Kitchen exhaust fan kWh (monthly submeter)
- Kitchen MUA gas consumption (monthly submeter)
- Number of hours/day exhaust runs at <50% speed (indicator of DCV effectiveness)
- Kitchen capture velocity (fpm) — verify quarterly at minimum speed

## M&V Plan (IPMVP Option C with submetering where feasible)

**Baseline:** 4-week pre-installation logging of exhaust fan kW (power meter), MUA gas flow, sensor status. Document kitchen operating schedule.

**Post-installation:**
- Submeter kitchen exhaust fan circuit (kWh)
- Submeter kitchen MUA gas train (therms)
- Compare monthly energy use vs. pre-installation baseline, adjusted for kitchen meal count
- IPMVP Option A (isolated measurement) for kitchen exhaust system
- NFPA compliance test documentation = key deliverable

**Measurement period:** Minimum 3 months post-installation across a representative range of cooking schedules.

## Costs & Payback (indicative)

- Optical/thermal DCV sensors (per hood section): $1,500–$3,500
- VFD installation (per fan): $2,000–$5,000 (including disconnect, wiring, BAS integration)
- BAS programming: $1,500–$4,000
- Fire alarm integration: $500–$2,000
- Fire marshal inspection: $300–$800
- **Total for single-hood kitchen:** $8,000–$18,000
- **Annual savings:** $8,000–$22,000/yr
- **Simple payback:** 10–22 months (may qualify for food service energy incentives)

## Templates / Reuse

- Kitchen DCV Specification Template — applies to any commercial kitchen (hospital, university, hotel)
- NFPA 96 DCV Compliance Checklist
- Kitchen DCV Commissioning Form (capture velocity verification)
