# Literature Update

- Generated: `2026-05-11T09:00:10`
- Profile: `mof_latest_custom`
- Since: `2025-05-11`
- Papers retained: `2`

## Overview

Collected 2 deduplicated papers for profile `mof_latest_custom`. `ML` appears in 0 papers and `DFT` in 2. `Adsorption/separation` themes appear more often (1) than `catalysis` themes (0). `Interatomic-potential` or MLIP-style work appears in 1 papers and is a notable transfer path from COF-side methods to MOFs.

## Innovation Patterns

- Data-driven screening is increasingly paired with physically grounded descriptors rather than pure geometry-only filters.
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

### 1. Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry

- Date: `2026-04-28`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2604.25262
- Tags: co2, dft, h2, high_throughput, interatomic_potential, md, mof, separation
- Authors: Connor Edwards, Jack D. Evans
- Why it matters: Here, we present a new high-temperature benchmarking dataset of 40~ps ab~initio molecular dynamics (AIMD) trajectories simulated at 300, 1000, and 2000 K for nine zinc- and zirconium-based metal-organic frameworks (MOFs): ZIF-8, CALF-20, MOF-10, MOF-5, MIP-206, UiO-66, UiO-67, UiO-66-NH2, and NU-1000.
- Innovation: Here, we present a new high-temperature benchmarking dataset of 40~ps ab~initio molecular dynamics (AIMD) trajectories simulated at 300, 1000, and 2000 K for nine zinc- and zirconium-based metal-organic frameworks (MOFs): ZIF-8, CALF-20, MOF-10, MOF-5, MIP-206, UiO-66, UiO-67, UiO-66-NH2, and NU-1000.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Directly relevant to MOF work.

### 2. Modeling of CO2/CH4 Mixture Adsorption in Flexible Mg-MOF-74 via Machine-Learned Potentials

- Date: `2026-05-05`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15002721/v1
- Tags: adsorption, co2, dft, gcmc, h2, md, mof, separation
- Authors: Ömer Tayfuroğlu, Seda Keskin
- Why it matters: Metal-organic frameworks (MOFs), particularly Mg-MOF-74 with open metal sites, offer a promising platform for the selective adsorption of CO2 over CH4.However, accurately modeling multicomponent gas adsorption in flexible frameworks remains challenging.In this work, we developed a fragment-based machine-learned potential (MLP) trained on high-level density functional theory data (PBE-D4/def2-TZVP) to describe all intramolecular and intermolecular interactions between the components of CO2/CH4 mixture and Mg-MOF-74.By integrating this MLP with a combined molecular dynamic-grand canonical Monte Carlo (MD-GCMC) hybrid scheme, we captured both framework flexibility and adsorption thermodynamics, enabling simulations of competitive adsorption and diffusion in multicomponent systems.Our results demonstrate that fragment-based MLPs can accurately represent binary gas mixtures in MOFs and reveal the critical role of framework flexibility in governing adsorption and transport behavior.
- Innovation: Metal-organic frameworks (MOFs), particularly Mg-MOF-74 with open metal sites, offer a promising platform for the selective adsorption of CO2 over CH4.However, accurately modeling multicomponent gas adsorption in flexible frameworks remains challenging.In this work, we developed a fragment-based machine-learned potential (MLP) trained on high-level density functional theory data (PBE-D4/def2-TZVP) to describe all intramolecular and intermolecular interactions between the components of CO2/CH4 mixture and Mg-MOF-74.By integrating this MLP with a combined molecular dynamic-grand canonical Monte Carlo (MD-GCMC) hybrid scheme, we captured both framework flexibility and adsorption thermodynamics, enabling simulations of competitive adsorption and diffusion in multicomponent systems.Our results demonstrate that fragment-based MLPs can accurately represent binary gas mixtures in MOFs and reveal the critical role of framework flexibility in governing adsorption and transport behavior.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Directly relevant to MOF work.
