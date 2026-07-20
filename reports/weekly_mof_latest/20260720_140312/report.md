# Literature Update

- Generated: `2026-07-20T14:03:12`
- Profile: `mof_latest_custom`
- Since: `2025-07-20`
- Papers retained: `3`

## Overview

Collected 3 deduplicated papers for profile `mof_latest_custom`. `ML` appears in 2 papers and `DFT` in 1. `Adsorption/separation` themes appear more often (2) than `catalysis` themes (2). `Interatomic-potential` or MLIP-style work appears in 1 papers and is a notable transfer path from COF-side methods to MOFs.

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

### 1. The impact of spurious imaginary phonon modes on thermal properties of Metal-organic Frameworks

- Date: `2026-07-17`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02231-6
- Tags: adsorption, co2, dft, h2, high_throughput, interatomic_potential, ml, mof, porous_material, priority_journal, separation
- Authors: P.S. Kamath, Kristin Persson
- Why it matters: Finally, we introduce a simple, rapid post-processing workflow that can be applied to standard phonon calculations to effectively correct heat capacity estimates and account for spurious imaginary modes in MOFs.
- Innovation: Finally, we introduce a simple, rapid post-processing workflow that can be applied to standard phonon calculations to effectively correct heat capacity estimates and account for spurious imaginary modes in MOFs.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 2. Data-Driven Design of Metal-Organic Frameworks for Photoelectrochemical Reactions

- Date: `2026-07-15`
- Journal: ACS Energy Letters
- Link: https://doi.org/10.1021/acsenergylett.6c00550
- Tags: battery, electrocatalysis, h2, high_throughput, ml, mof, multimodal, photocatalysis, porous_material, separation
- Authors: Hyunsoo Park, Tianshu Li, Ashna Jose, Seung‐Jae Shin, Aron Walsh
- Why it matters: We present a data-driven workflow integrating hybrid quantum chemical calculations with a multimodal AI model (MOFTransformer) to efficiently predict oxidation and reduction potentials for over 270,000 known and hypothetical MOFs.
- Innovation: We present a data-driven workflow integrating hybrid quantum chemical calculations with a multimodal AI model (MOFTransformer) to efficiently predict oxidation and reduction potentials for over 270,000 known and hypothetical MOFs.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 3. Performance Benchmarking of MOF-Based Adsorbents for Organic Dye Removal: A PRISMA-Guided Bibliometric and Statistical Analysis

- Date: `2026-07-14`
- Journal: Colorants
- Link: https://doi.org/10.3390/colorants5030025
- Tags: adsorption, high_throughput, mof, review, separation
- Authors: Arelly Montserrat Canton-Diaz, Juan Jose Alonso-Tijerina, Nancy Elizabeth Davila-Guzman
- Why it matters: This study presents a PRISMA-guided bibliometric and statistical analysis of MOF-based adsorbents for organic dye removal, covering publications from 2014 to 2026.
- Innovation: This study presents a PRISMA-guided bibliometric and statistical analysis of MOF-based adsorbents for organic dye removal, covering publications from 2014 to 2026.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.
