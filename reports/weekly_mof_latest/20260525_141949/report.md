# Literature Update

- Generated: `2026-05-25T14:19:49`
- Profile: `mof_latest_custom`
- Since: `2025-05-25`
- Papers retained: `1`

## Overview

Collected 1 deduplicated papers for profile `mof_latest_custom`. `ML` appears in 0 papers and `DFT` in 1. `Adsorption/separation` themes appear more often (1) than `catalysis` themes (0).

## Innovation Patterns

- Several recent papers still focus on single-system mechanistic insight rather than broad screening.
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

### 1. Modeling of CO2/CH4 Mixture Adsorption in Flexible Mg-MOF-74 via Machine-Learned Potentials

- Date: `2026-05-05`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15002721/v1
- Tags: adsorption, co2, dft, gcmc, h2, md, mof, separation
- Authors: Ömer Tayfuroğlu, Seda Keskin
- Why it matters: In this work, we developed a fragment-based machine-learned potential (MLP) trained on high-level density functional theory data (PBE-D4/def2-TZVP) to describe all intramolecular and intermolecular interactions between the components of CO2/CH4 mixture and Mg-MOF-74.
- Innovation: In this work, we developed a fragment-based machine-learned potential (MLP) trained on high-level density functional theory data (PBE-D4/def2-TZVP) to describe all intramolecular and intermolecular interactions between the components of CO2/CH4 mixture and Mg-MOF-74.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.
