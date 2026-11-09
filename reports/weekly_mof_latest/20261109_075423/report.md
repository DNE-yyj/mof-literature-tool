# Literature Update

- Generated: `2026-11-09T07:54:23`
- Profile: `mof_latest_custom`
- Since: `2025-11-09`
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

### 1. Achieving Accurate Prediction of Water Adsorption in Mildly Hydrophobic MOFs

- Date: `2026-11-04`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15011663/v1
- Tags: adsorption, dft, h2, interatomic_potential, md, mof, porous_material, water
- Authors: Sabrina Grigoletto, Ruben Goeminne, Mohammad Wahiduzzaman, Louis Vanduyfhuys, Véronique Van Speybroeck
- Why it matters: Here, we develop a machine-learning interatomic potential (MLIP), trained on reliable density functional theory reference data, for the prototypical mildly hydrophobic channel MOF MIP-211(Al).
- Innovation: Here, we develop a machine-learning interatomic potential (MLIP), trained on reliable density functional theory reference data, for the prototypical mildly hydrophobic channel MOF MIP-211(Al).
- Likely limitations: Abstract-level evidence is promising, but validation breadth is unclear without reading the full paper.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.
