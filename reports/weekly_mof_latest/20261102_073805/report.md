# Literature Update

- Generated: `2026-11-02T07:38:05`
- Profile: `mof_latest_custom`
- Since: `2025-11-02`
- Papers retained: `3`

## Overview

Collected 3 deduplicated papers for profile `mof_latest_custom`. `ML` appears in 0 papers and `DFT` in 2. `Catalysis` themes appear more often (3) than `adsorption/separation` themes (1).

## Innovation Patterns

- Data-driven screening is increasingly paired with physically grounded descriptors rather than pure geometry-only filters.
- DFT remains the main source of labels, descriptors, or mechanistic interpretation even in ML-heavy studies.

## Common Gaps

- Many screening papers still rely on idealized, defect-free structures and do not fully capture flexibility, humidity, or multicomponent conditions.
- ML papers often leave transferability and uncertainty outside the training distribution only partially resolved.
- Catalysis papers frequently identify thermodynamic trends without equally strong kinetic or explicit-environment treatment.

## Next Opportunities

- Connect adsorption descriptors to humid, multicomponent, and process-level targets instead of reporting only uptake/selectivity.
- For catalysis, combine DFT, microkinetics, and uncertainty-aware ML rather than stopping at static intermediate energetics.
- For transferable COF-side methods, port them to MOFs by adding node-aware descriptors, charge treatment, and local cluster corrections around metal sites.

## Paper Briefs

### 1. Metal–Organic Frameworks for Sustainable Photocatalytic and Electrocatalytic HMF‐to‐FDCA Conversion: From Catalyst Engineering to Energy‐Saving Paired Electrolysis Systems

- Date: `2026-10-30`
- Journal: Advanced Sustainable Systems
- Link: https://doi.org/10.1002/adsu.70700
- Tags: catalysis, catalyst_descriptor, dft, electrocatalysis, h2, mof, photocatalysis, review, separation
- Authors: Jianping Luo, Yuhan Nie, Xuemei Zhang, Weikang Wang, Qinqin Liu
- Why it matters: ABSTRACT Photocatalytic and electrocatalytic upgrading of lignocellulosic biomass into value‐added chemicals offers a sustainable route to carbon neutrality.
- Innovation: ABSTRACT Photocatalytic and electrocatalytic upgrading of lignocellulosic biomass into value‐added chemicals offers a sustainable route to carbon neutrality.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 2. Assessing Structural, Thermal, and Mechanical Properties of Zirconium‐Based Metal‐Organic Frameworks via DFTB3 / 3OB MD Simulations: A Benchmark Beyond UiO Frameworks

- Date: `2026-10-28`
- Journal: Journal of Computational Chemistry
- Link: https://doi.org/10.1002/jcc.70536
- Tags: co2, dft, equivariant_ml, h2, high_throughput, md, mof
- Authors: Andreas Penz, Thomas S. Hofer
- Why it matters: The exceptional stability and broad application potential of zirconium-based metal-organic frameworks call for reliable atomistic methods capable of describing their structural, thermal, and mechanical properties.
- Innovation: The exceptional stability and broad application potential of zirconium-based metal-organic frameworks call for reliable atomistic methods capable of describing their structural, thermal, and mechanical properties.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 3. Reliable methane storage screening and inverse design of metal organic frameworks under distribution shift

- Date: `2026-10-31`
- Journal: Discover Artificial Intelligence
- Link: https://doi.org/10.1007/s44163-026-02574-5
- Tags: adsorption, crystal, gcmc, generative_model, h2, high_throughput, mof
- Authors: Safiul Haque Chowdhury, Rakib Ahammed Diptho, Pial Ghosh
- Why it matters: We study the methane deliverable (working) capacity across a public database of 252,353 frameworks described by 14 geometric and 148 chemical descriptors, with uptake from grand canonical Monte Carlo simulation at 5.8 and 65 bar.
- Innovation: We study the methane deliverable (working) capacity across a public database of 252,353 frameworks described by 14 geometric and 148 chemical descriptors, with uptake from grand canonical Monte Carlo simulation at 5.8 and 65 bar.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.
