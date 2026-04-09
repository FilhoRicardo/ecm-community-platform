---
Main System: "[[Service Water Heating]]"
Category System: "[[Hot Water Distribution]]"
Utility Affected: "[[Heating]]"
Source Document: "[[AEDG30-SmallHealthcare-2009.pdf]]"
Style Benchmark: "[[Uploaded ECM Examples]]"
---

# ECM: Domestic Hot Water Distribution and Point-of-Use Rationalization

## Summary
Reduce hot-water distribution losses by minimizing dead legs, improving recirculation control, and using point-of-use solutions for remote, low-demand healthcare loads. Small healthcare facilities often have DHW distribution systems that are oversized and poorly looped due to layout changes over time — reducing distribution losses is a practical measure with infection-control and service-quality benefits that complement energy savings.

## Estimated Savings
- **CIBSE Guidance**: 10–25% of DHW heating energy through distribution optimization in small healthcare facilities (per CIBSE Guide B DHW distribution data)
- **ASHRAE Guidance**: 8–20% of DHW energy in small healthcare facilities through pipe insulation, recirculation control, and point-of-use integration (per ASHRAE 90.1 and AEDG30-SmallHealthcare)
- **End-Uses Affected**: DHW heating energy, recirculation pump energy, and energy lost to hot water standby losses

## Basis / References

### CIBSE References
- **Guide B** (HVAC): DHW distribution system design, pipe insulation, recirculation control, and point-of-use technology
- **Guide G** (Public Health Engineering): Healthcare hot water temperature management and infection control requirements

### ASHRAE References
- **90.1** (Energy Standard): §10.4 for DHW system efficiency requirements, pipe insulation, and recirculation control
- **Handbook — HVAC Applications**: Ch. 6 — Service Water Heating systems and controls
- **AEDG30-SmallHealthcare-2009**: DHW distribution losses as a notable small healthcare opportunity, particularly in facilities with complex piping

### Other Standards
- **ASHRAE 188** (Legionella): DHW return temperature requirements — systems must maintain hot water ≥110°F to prevent Legionella proliferation; point-of-use systems must maintain temperature or be configured to prevent stagnation-related bacterial growth
- **NSF/ANSI 372** (Low Lead): Water heating equipment standards for commercial DHW
- **ISO 14040** (Environmental Performance): Pipe insulation environmental product declarations for embodied carbon

## Assumptions
Baseline system: centralized DHW heater with long uninsulated distribution piping, constant-speed recirculation pump running 24/7, multiple dead legs, and point-of-use electric boosters for remote sinks. Target recirculation return temperature: ≥110°F per ASHRAE 188. Recirculation pump control: timer-based or temperature-based setpoint modulation reducing nighttime recirculation by ≥70%. Pipe insulation: ≥1 inch fiberglass or equivalent for pipes ≤1.5 inches; ≥1.5 inches for pipes >1.5 inches. Point-of-use water heaters for sinks with long runs (>50 ft from central heater) and low draw volumes (<50 gal/day).

## Climate Zone Relevance
All climate zones; distribution losses are most significant in cold climates where heat loss from pipes is greatest and longer heating seasons increase the effective loss period. Hot climates still have DHW energy consumption year-round but pipe losses are lower due to higher ambient temperatures. The infection-control requirements (ASHRAE 188) apply uniformly across all climates.

## Interaction Notes
Pairs with ECM_Condenser_Heat_Recovery_Small_Healthcare when DHW preheat is the recovery sink — DHW distribution optimization increases the temperature differential available for heat recovery. Complements ECM_Commissioning_and_Trend_Review_Small_Healthcare: DHW temperature monitoring should be integrated into BAS trend monitoring. Synergizes with building envelope improvements that reduce overall heating loads (DHW is a year-round heating load that competes with space heating in winter). Does not conflict with any other ECM.

## Implementation Essentials
- **DHW distribution mapping**: Map all hot water piping runs, measure distances from central heater to each sink, identify dead legs and underutilized branches — any branch with <2 draws/day is a candidate for removal or point-of-use conversion
- **Pipe insulation**: Insulate all accessible hot water and recirculation piping — target: ≥1 inch fiberglass or equivalent for pipes ≤1.5 inches; ≥1.5 inches for pipes >1.5 inches; verify insulation is continuous through fittings and valves
- **Recirculation pump control upgrade**: Replace constant-speed recirculation pump with variable-speed or timer-controlled pump; configure to reduce nighttime recirculation (22:00–06:00) by ≥70% while maintaining ≥110°F return temperature at furthest fixture
- **Dead leg elimination**: Remove or isolate unused or rarely-used hot water branches; install shut-off valves on infrequently used branches so they can be isolated during low-demand periods
- **Point-of-use water heaters**: Install point-of-use electric or tankless water heaters for remote sinks with low draw volumes and long pipe runs — eliminates long pipe dead volume heating losses; target sinks >50 ft from central heater with <2 gal/min draw
- **Legionella temperature monitoring**: Install temperature sensors at key points in recirculation loop (at heater return, mid-loop, at furthest fixture); configure alarm if return temperature drops below 110°F
- **Commissioning**: Test recirculation return temperature at furthest fixture during nighttime setback; verify ≥110°F maintained within 5 minutes of any draw event; document recirculation curve and fixture response times

## Risks / Constraints
- **Healthcare temperature-management and infection-control requirements limit aggressive setback**: ASHRAE 188 requires hot water ≥110°F at all times in healthcare facilities — any recirculation setback must maintain ≥110°F return temperature and rapid recovery to ≥110°F after any draw event
- **Too many small local heaters create maintenance complexity**: Point-of-use electric water heaters add maintenance points throughout the facility — limit to sinks where long runs make central DHW uneconomical; standardize on 1–2 point-of-use heater models for maintenance simplicity
- **Recirculation pump failure can cause Legionella risk**: Pump must maintain circulation during low-demand periods to prevent stagnation and bacterial growth — configure BMS alarm on pump failure or abnormal flow; require automatic backup pump or gravity circulation path for critical zones
- **Pipe insulation in existing buildings is disruptive**: Access to existing pipes for insulation may require ceiling removal or wall opening — phase insulation by priority (longest runs, highest temperature pipes first) to minimize disruption
- **Draw patterns may not support aggressive nighttime setback**: If nighttime draws are frequent (e.g., night nursing staff), aggressive recirculation reduction may cause temperature complaints — verify draw pattern before implementing nighttime setback

## KPIs
- DHW heating energy (kBtu/month) — target: ≥15% reduction from baseline through distribution optimization
- Recirculation pump energy (kWh/month) — target: ≥60% reduction through timer or variable-speed control
- Recirculation return temperature (°F) — maintain ≥110°F at all times; target: ≥120°F
- Dead leg count and total linear footage of removed piping — measure distribution simplification
- Pipe surface temperature (°F) — verify insulation performance; target: surface temperature within 10°F of water temperature
- Point-of-use heater count — measure reduction in long-run central DHW demand
- DHW complaint frequency (count/quarter) related to temperature or wait time — track for service quality
- Legionella monitoring: temperature excursion count (any instance return <110°F) — target: zero excursions per quarter

## M&V Plan
**Option B (Retrofit Isolation — DHW System Level)** per IPMVP where DHW system is sub-metered

**Quantification approach:**
- Baseline: 12 months of DHW heating energy (kBtu from gas meter or electric booster meter) and recirculation pump energy (kWh)
- Post-implementation: Monthly DHW heating energy and recirculation pump energy; verify recirculation return temperature compliance
- Calculate pipe loss reduction: baseline pipe loss (estimated from temperature differential and pipe surface area) − post pipe loss (improved with insulation and shorter runs)
- Calculate recirculation pump savings: baseline constant-speed pump kWh − post variable-speed/timer pump kWh
- Weather normalization: DHW heating is relatively weather-independent but pipe losses in unconditioned spaces are temperature-dependent; regress DHW energy against outdoor temperature for normalization if significant

**Data collection:**
- DHW heating energy (kBtu/month) from gas meter or electric booster submeter
- Recirculation pump energy (kWh/month) from pump motor meter
- Recirculation return temperature (°F) at key points at 15-minute intervals
- DHW supply temperature (°F) at heater outlet
- Dead leg inventory with linear footage before/after
- Pipe insulation R-value documentation and surface temperature measurements
- ASHRAE 188 Legionella temperature log: any instance return temperature <110°F (should be zero; flag all events)

## Costs & Payback (Indicative)
- **Capex**: Pipe insulation (labor and materials): £15–40/linear ft; recirculation pump control upgrade: £1,500–4,000; dead leg removal: £500–2,000 per branch; point-of-use heaters: £300–800 per unit; temperature sensors and BMS integration: £1,000–3,000
- **Opex**: Point-of-use heater maintenance (scale inspection): £200–500/year; annual pipe insulation inspection: £300–800/year
- **Simple payback**: 2–5 years for distribution optimization; 3–7 years if major pipe rerouting is required
- **ROI**: Enhanced by infection-control and service-quality benefits; total ROI including reduced risk and improved user satisfaction is favorable even when energy payback is modest

## Templates / Reuse
*Boilerplate footer removed. Reference ASHRAE 90.1 §10.4 for DHW system efficiency, ASHRAE 188 for Legionella requirements, and CIBSE Guide B for DHW distribution design.*
