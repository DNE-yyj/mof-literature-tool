# Literature Update

- Generated: `2026-09-14T06:13:47`
- Profile: `mof_latest_custom`
- Since: `2025-09-14`
- Papers retained: `3`

## Overview

Collected 3 deduplicated papers for profile `mof_latest_custom`. `ML` appears in 0 papers and `DFT` in 0. `Adsorption/separation` themes appear more often (2) than `catalysis` themes (1).

## Innovation Patterns

- Data-driven screening is increasingly paired with physically grounded descriptors rather than pure geometry-only filters.

## Common Gaps

- Many screening papers still rely on idealized, defect-free structures and do not fully capture flexibility, humidity, or multicomponent conditions.
- ML papers often leave transferability and uncertainty outside the training distribution only partially resolved.
- Catalysis papers frequently identify thermodynamic trends without equally strong kinetic or explicit-environment treatment.

## Next Opportunities

- Connect adsorption descriptors to humid, multicomponent, and process-level targets instead of reporting only uptake/selectivity.
- For catalysis, combine DFT, microkinetics, and uncertainty-aware ML rather than stopping at static intermediate energetics.
- For transferable COF-side methods, port them to MOFs by adding node-aware descriptors, charge treatment, and local cluster corrections around metal sites.

## Paper Briefs

### 1. MOF-assisted cryo-adsorption delivers near-liquid volumetric capacity and suppressed boil-off for LH₂ transport

- Date: `2026-09-07`
- Journal: Nature Communications
- Link: https://doi.org/10.1038/s41467-026-77420-4
- Tags: adsorption, crystal, force_field, h2, high_throughput, mof, priority_journal
- Authors: J.-H. Park, J.-H. Park, Junsu Ha, Hong Kyu Lee, Hyunlim Kim
- Why it matters: We introduce a materials-based solution using metal–organic frameworks (MOFs) to suppress boil-off by enhancing gas–surface interactions and stabilizing confined hydrogen.
- Innovation: We introduce a materials-based solution using metal–organic frameworks (MOFs) to suppress boil-off by enhancing gas–surface interactions and stabilizing confined hydrogen.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 2. Recent advances in the strategies of developing water-resistant catalysts for the removal of atmospheric pollutants

- Date: `2026-09-11`
- Journal: Greenverse Science
- Link: https://doi.org/10.20517/greenvsci.2026.13
- Tags: adsorption, catalysis, catalyst_descriptor, crystal, h2, md, mof, oxide, review, water
- Authors: Xiaoyang Wang, Xin Zhou, Mengwei Hua, Zhiquan Hou, Wenming Sun
- Why it matters: In the catalytic oxidation of atmospheric pollutants such as volatile organic compounds (VOCs), catalyst deactivation induced by water under realistic operating conditions has emerged as a critical bottleneck constraining the large-scale application of this technology.
- Innovation: In the catalytic oxidation of atmospheric pollutants such as volatile organic compounds (VOCs), catalyst deactivation induced by water under realistic operating conditions has emerged as a critical bottleneck constraining the large-scale application of this technology.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 3. PORMAKE2: Topology-Based Generation of Hypothetical Metal-Organic Frameworks through Single-Metal Nodes and Symmetry-Aware Linker Rotation

- Date: `2026-09-09`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15008555/v1
- Tags: co2, h2, high_throughput, mof, oxide, physics_informed, separation
- Authors: Jungwoo Lee, Young-Hun Kim, Gunho Lee, Jihan Kim
- Why it matters: Here, we present PORMAKE2, an upgraded topology-based hypothetical MOF generator designed to improve both access to small-pore structures and geometric fidelity.
- Innovation: Here, we present PORMAKE2, an upgraded topology-based hypothetical MOF generator designed to improve both access to small-pore structures and geometric fidelity.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.
