---
Main System: Guest Room HVAC
Secondary System:
Utility Affected: Electricity
Building: Highway Lodging
---

# ECM: Guest Room Occupancy HVAC Control

## Summary

**What:** Integrate guest room door card switches or occupancy sensors with RTU/mini-split controls — automatically setback temperature when room is unoccupied (card removed) and recover to comfort before next guest arrival.

**Why:** Guest rooms are unoccupied 30–50% of the time during off-peak periods. HVAC systems continue running at full comfort settings despite no guests, wasting 10–25% of guest room conditioning energy.

## Estimated Savings
- 10–25% HVAC energy during unoccupied hours
- Absolute: 3–8 kBtu/sq ft/yr

## Basis / References
- HPAC Engineering 'Hotel Guest Room Energy Management' 2019
- 
- Reddit r/HVAC: I may have “lost” a new house for my family
- Reddit r/HVAC: Kicked Out a Group of Crybaby “Heat Stroke Victims” Full Refund, Full Regret

## Assumptions
- Guest rooms represent approximately 60-70% of total building energy use in highway lodging
- RTUs are single-packaged units serving individual guest rooms (typical 1-ton capacity)
- Mini-split COP of 3.0-4.0 at part-load conditions (inverter-driven)
- Occupancy patterns follow typical highway lodging profiles: 60-80% overnight occupancy

## Implementation Essentials
1) Install door card switch or PIR occupancy sensor in each guest room. 2) Integrate with RTU/mini-split — setback to 78°F cooling / 65°F heating when unoccupied for >30 min. 3) Pre-condition room 30 min before standard arrival times.

## Risks / Constraints
- Guest comfort complaints during transition period if setback temperatures are too aggressive
- Card switch/sensor reliability in humid coastal environments — specify NEMA 4X enclosures
- RTU removal requires coordination with guests; phased rollout by floor/wing recommended
- Local code may require refrigerants handling certification for mini-split installation
- Existing ductwork may be abandoned in place — verify with mechanical engineer

## KPIs
- Guest room temperature (occupied vs unoccupied)
- HVAC runtime hours
- Energy per occupied room night

## M&V Plan (IPMVP Option C with submetering where feasible)
- Install whole-building utility meters (electricity and natural gas) as primary measurement boundary
- Sub-meter guest room-level circuit-level kWh via panel-level CTs for granular HVAC end-use
- Collect pre-installation baseline: 12 months of whole-building kBtu/sq ft/yr and guest room kBtu/sq ft/yr
- Post-installation: monthly kBtu/sq ft/yr tracking; compare against degree-day normalized baseline
- IPMVP Option C: whole building metering with engineering model to isolate savings

## Costs & Payback (indicative)
- 6–18 months
- Estimated total implementation cost: $800-$1,500 per guest room (mini-split equipment + installation + electrical upgrades)
- 80-120 room property: ~$64,000-$180,000 total project cost

## Templates / Reuse
- ECM template: ECM full note milo.md
- Applicable to: all highway lodging, select-service hotels, extended-stay properties
- Mini-split spec sheet: Mitsubishi MXZ-SM Series (inverter-driven, SEER 20+, HSPF 10+)
