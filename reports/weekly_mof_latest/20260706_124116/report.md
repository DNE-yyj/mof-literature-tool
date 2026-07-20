# Literature Update

- Generated: `2026-07-06T12:41:16`
- Profile: `mof_latest_custom`
- Since: `2025-07-06`
- Papers retained: `3`

## Overview

Collected 3 deduplicated papers for profile `mof_latest_custom`. `ML` appears in 2 papers and `DFT` in 2. `Adsorption/separation` themes appear more often (3) than `catalysis` themes (2).

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

### 1. AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications

- Date: `2026-07-03`
- Journal: Frontiers in Chemistry
- Link: https://doi.org/10.3389/fchem.2026.1864044
- Tags: active_learning, adsorption, catalysis, co2, dft, electrocatalysis, h2, high_throughput, ml, mof, separation
- Authors: Sreenivas Punna, Suvarshitha Pusuluru, Madhumita Ravikumar, Farid Menaa
- Why it matters: The incorporation of artificial intelligence (AI) into energy systems has become a transformative strategy for tackling global energy related challenges, particularly energy vulnerability (EVI).
- Innovation: The incorporation of artificial intelligence (AI) into energy systems has become a transformative strategy for tackling global energy related challenges, particularly energy vulnerability (EVI).
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 2. Pore Geometry–Driven Capture of Trace Aromatic Volatile Organic Compounds in Al-Based MOFs

- Date: `2026-07-02`
- Journal: ACS Nano
- Link: https://doi.org/10.1021/acsnano.6c05710
- Tags: adsorption, dft, h2, high_throughput, mof, porous_material, priority_journal, separation, water
- Authors: A. O. Blokhina, Yutao Li, Iurii Dovgaliuk, Debanjan Chakraborty, Aysu Ozturk
- Why it matters: Here, we identify pore geometry as an effective structural descriptor for discovering metal–organic frameworks (MOFs) capable of efficient trace-level VOC capture.
- Innovation: Here, we identify pore geometry as an effective structural descriptor for discovering metal–organic frameworks (MOFs) capable of efficient trace-level VOC capture.
- Likely limitations: Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 3. Descriptor Adequacy as a Materials-Regime Principle in MOF Adsorption Machine Learning

- Date: `2026-07-03`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15002252/v2
- Tags: adsorption, force_field, h2, high_throughput, ml, mof, separation, uncertainty
- Authors: Hossein Alimardani, Shayan Abaei, Mehrdad Asgari
- Why it matters: Machine learning is changing how metal--organic frameworks (MOFs) are screened for gas storage and separation, but its reliability depends on a basic question: does the descriptor contain the physics that controls the adsorption property?
- Innovation: Machine learning is changing how metal--organic frameworks (MOFs) are screened for gas storage and separation, but its reliability depends on a basic question: does the descriptor contain the physics that controls the adsorption property?
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.
