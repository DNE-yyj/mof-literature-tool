# Literature Update

- Generated: `2026-06-15T14:55:32`
- Profile: `mof_latest_custom`
- Since: `2025-06-15`
- Papers retained: `1`

## Overview

Collected 1 deduplicated papers for profile `mof_latest_custom`. `ML` appears in 0 papers and `DFT` in 1. `Adsorption/separation` themes appear more often (1) than `catalysis` themes (0). `Interatomic-potential` or MLIP-style work appears in 1 papers and is a notable transfer path from COF-side methods to MOFs.

## Innovation Patterns

- Several recent papers still focus on single-system mechanistic insight rather than broad screening.
- DFT remains the main source of labels, descriptors, or mechanistic interpretation even in ML-heavy studies.
- ML interatomic potentials are emerging as the clearest route to capture framework flexibility and guest dynamics beyond static screening.

## Common Gaps

- Many screening papers still rely on idealized, defect-free structures and do not fully capture flexibility, humidity, or multicomponent conditions.
- ML papers often leave transferability and uncertainty outside the training distribution only partially resolved.
- Catalysis papers frequently identify thermodynamic trends without equally strong kinetic or explicit-environment treatment.

## Next Opportunities

- Connect adsorption descriptors to humid, multicomponent, and process-level targets instead of reporting only uptake/selectivity.
- For catalysis, combine DFT, microkinetics, and uncertainty-aware ML rather than stopping at static intermediate energetics.
- For transferable COF-side methods, port them to MOFs by adding node-aware descriptors, charge treatment, and local cluster corrections around metal sites.

## Paper Briefs

### 1. FLAMES – A flexible and extensible code for Monte Carlo simulations of nanoporous materials

- Date: `2026-06-11`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15004623/v1
- Tags: adsorption, cof, dft, force_field, gcmc, h2, interatomic_potential, md, mof, porous_material, zeolite
- Authors: Felipe Lopes Oliveira, Holger‐Dietrich Saßnick, Guillaume Maurin
- Why it matters: Here, we introduce FLAMES (Flexible Lattice Adsorption by Monte Carlo Engine Simulation), a new software package designed to perform Monte Carlo-based simulations of nanoporous materials using MLIPs and other energy calculation methods, paving the way for more accurate and physically realistic molecular simulations.
- Innovation: Here, we introduce FLAMES (Flexible Lattice Adsorption by Monte Carlo Engine Simulation), a new software package designed to perform Monte Carlo-based simulations of nanoporous materials using MLIPs and other energy calculation methods, paving the way for more accurate and physically realistic molecular simulations.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.
