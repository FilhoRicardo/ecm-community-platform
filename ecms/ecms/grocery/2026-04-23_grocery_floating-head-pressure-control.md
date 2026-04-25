---
Main System: Refrigeration Rack
Secondary System:
Utility Affected: Electricity
Building: Grocery
---

# ECM: Floating Head Pressure Control

## Summary

Install floating head pressure controls on the refrigeration rack — allow condenser pressure to float (rise) during cool weather rather than maintaining artificially high fixed head pressure, reducing compressor work significantly. Most refrigeration systems maintain a fixed, artificially-high condensing temperature (often 90–100°F) regardless of outdoor conditions. In a grocery store with a mechanical room, this means running the condenser fan at full blast even in 40°F weather. Floating head pressure allows the system to operate at much lower condensing temperatures when ambient is cool.

## Estimated Savings
- 10–20% refrigeration energy
- 5–15% total store electricity

## Basis / References
- ASHRAE 15 Safety Code for Refrigeration
- DOE Commercial Refrigeration Guide
- HPAC Engineering 'Floating Head Pressure' 2019

## Assumptions
- Refrigeration rack has staging capacity (multiple compressors or step unloading)
- Condenser is air-cooled (not evaporative or water-cooled)
- Mechanical room can accommodate VFD on fans or head pressure regulating valve
- Rack supports head pressure variation without short-cycling

## Implementation Essentials
1. Survey refrigeration rack capacity and compressor staging — verify minimum load ≥ 25% of rack capacity
2. Install head pressure regulating valve OR VFD on condenser fans (preferred: VFD for smoother control)
3. Program minimum head pressure based on coldest expected refrigerant temperature (typically 35–40°F saturated suction temperature)
4. Commission: verify no compressor short-cycling, suction pressure stable across operating range
5. M&V baseline: 30-day pre; post-commissioning trend for 90 days

## Risks / Constraints
- ASHRAE 15 minimum head pressure must be maintained for safety
- Transcritical CO₂ systems require specific head pressure management (different setpoints)
- Low head pressure can cause oil return issues — verify oil management
- Grocery code compliance: health department may require temperature monitoring

## KPIs
- Head pressure (psig)
- Condenser fan kW
- Compressor kW
- Refrigeration COP

## M&V Plan (IPMVP Option C with submetering where feasible)
- Submeter: refrigeration rack kW (dedicated panel), condenser fan kW
- Whole-building: store-level electricity from utility billing
- Baseline: 30-day pre; post: 90 days — adjust for ambient temperature using bin analysis

## Costs & Payback (indicative)
- VFD + installation on condenser fans: $5,000–15,000 (per rack)
- Controls integration: $2,000–5,000
- Total: $7,000–20,000; Payback: 6–18 months

## Templates / Reuse
- Standard ECM template
