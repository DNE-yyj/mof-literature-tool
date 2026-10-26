# Literature Update

- Generated: `2026-10-26T06:07:20`
- Profile: `mof_latest_custom`
- Since: `2025-10-26`
- Papers retained: `3`

## Overview

Collected 3 deduplicated papers for profile `mof_latest_custom`. `ML` appears in 2 papers and `DFT` in 2. `Adsorption/separation` themes appear more often (1) than `catalysis` themes (1). `Interatomic-potential` or MLIP-style work appears in 1 papers and is a notable transfer path from COF-side methods to MOFs.

## Innovation Patterns

- Data-driven screening is increasingly paired with physically grounded descriptors rather than pure geometry-only filters.
- Machine-learning models are commonly used as surrogates for expensive adsorption, electronic-structure, or catalytic calculations.
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

### 1. Mechanism‐Guided and Data‐Driven Design of COF/MOF Photocatalysts Toward H 2 O 2 Production

- Date: `2026-10-22`
- Journal: Chemistry - A European Journal
- Link: https://doi.org/10.1002/chem.71815
- Tags: adsorption, catalysis, cof, crystal, dft, h2, high_throughput, ml, mof, oxide, review, water
- Authors: Shu‐Ya Guo, Guo‐Hong Ning, Dan Li
- Why it matters: This review summarizes recent advances in COF/MOF photocatalysts for H 2 O 2 production, focusing on density functional theory (DFT)‐based mechanistic insights, descriptor construction, and data‐driven catalyst discovery enabled by artificial intelligence (AI) and machine learning (ML).
- Innovation: This review summarizes recent advances in COF/MOF photocatalysts for H 2 O 2 production, focusing on density functional theory (DFT)‐based mechanistic insights, descriptor construction, and data‐driven catalyst discovery enabled by artificial intelligence (AI) and machine learning (ML).
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 2. Flexible force field-based screening and machine learning predictions for CO2 sorption and diffusion in MOFs

- Date: `2026-10-21`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15010813/v1
- Tags: co2, dft, force_field, high_throughput, md, ml, mof, separation
- Authors: Clare B. Martin, Samir Budhathoki, Janice A. Steckel
- Why it matters: We investigated different ML algorithms, featurization methods, and the role of physical descriptors in predicting CO2 sorption and self-diffusion in MOFs.
- Innovation: We investigated different ML algorithms, featurization methods, and the role of physical descriptors in predicting CO2 sorption and self-diffusion in MOFs.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 3. Mechanical versus thermal amorphization of ZIF-4: from local rearrangements to network disorder

- Date: `2026-10-21`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15010773/v1
- Tags: crystal, h2, interatomic_potential, md, mof, porous_material, separation
- Authors: Léna Triestram, François‐Xavier Coudert
- Why it matters: Focusing on the two main synthesis methods, which are melt-quenching and ball-milling, we use molecular dynamics simulations with a machine-learning interatomic potential to compare different glasses obtained from ZIF-4.
- Innovation: Focusing on the two main synthesis methods, which are melt-quenching and ball-milling, we use molecular dynamics simulations with a machine-learning interatomic potential to compare different glasses obtained from ZIF-4.
- Likely limitations: Abstract-level evidence is promising, but validation breadth is unclear without reading the full paper.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.
