# Literature Update

- Generated: `2026-09-28T06:48:33`
- Profile: `mof_latest_custom`
- Since: `2025-09-28`
- Papers retained: `5`

## Overview

Collected 5 deduplicated papers for profile `mof_latest_custom`. `ML` appears in 1 papers and `DFT` in 2. `Adsorption/separation` themes appear more often (5) than `catalysis` themes (3). `Interatomic-potential` or MLIP-style work appears in 1 papers and is a notable transfer path from COF-side methods to MOFs.

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

### 1. Advances in Hydrocarbon Adsorptive Materials: Rational Design, Adsorption Chemistry, and Frontier Applications

- Date: `2026-09-23`
- Journal: ChemistrySelect
- Link: https://doi.org/10.1002/slct.74487
- Tags: adsorption, catalysis, h2, ml, mof, porous_material, review, separation, zeolite
- Authors: Junyan Chen, Bin Guan, Lei Zhu, Tiankui Zhu, Shiying Chang
- Why it matters: ABSTRACT This review comprehensively and critically examines the research progress on hydrocarbon (HC) adsorbent materials in three key application scenarios: engine cold‐start HC emission control, industrial VOC recovery, and petrochemical HC separation.
- Innovation: ABSTRACT This review comprehensively and critically examines the research progress on hydrocarbon (HC) adsorbent materials in three key application scenarios: engine cold‐start HC emission control, industrial VOC recovery, and petrochemical HC separation.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Catalytic conclusions are likely thermodynamics-heavy unless kinetics or explicit environment are included.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 2. From sparse quantum-computing data to atomistic simulation with universal machine-learning interatomic potentials

- Date: `2026-09-18`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2609.21536
- Tags: adsorption, alloy, dft, h2, interatomic_potential, md, mof, transfer_learning, water
- Authors: Tuan Minh Do, Yuichiro Yoshida, Kenji Ishihara, Wataru Mizukami
- Why it matters: We demonstrate the approach for three chemically distinct applications: the Menshutkin reaction, water adsorption in the metal-organic framework HKUST-1, and CO hopping on a high-entropy-alloy nanoparticle.
- Innovation: We demonstrate the approach for three chemically distinct applications: the Menshutkin reaction, water adsorption in the metal-organic framework HKUST-1, and CO hopping on a high-entropy-alloy nanoparticle.
- Likely limitations: Abstract-level evidence is promising, but validation breadth is unclear without reading the full paper.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 3. Lewis Acid Site Engineering in MOF‐Derived Aluminum Oxide/Carbon Composites for Dechlorination of Waste Plastic Pyrolysis Oil

- Date: `2026-09-24`
- Journal: Advanced Functional Materials
- Link: https://doi.org/10.1002/adfm.78694
- Tags: adsorption, catalysis, co2, dft, h2, md, mof, oxide, separation
- Authors: Seong Cheon Kim, Byeongju Jeon, Suk Hyun Lim, Eun Hee Kwon, Nam Sun Nho
- Why it matters: Here, we report a defect‐engineering strategy that enriches coordinatively unsaturated Al sites through the controlled carbonization of an aluminum‐fumarate metal–organic framework.
- Innovation: Here, we report a defect‐engineering strategy that enriches coordinatively unsaturated Al sites through the controlled carbonization of an aluminum‐fumarate metal–organic framework.
- Likely limitations: Abstract-level evidence is promising, but validation breadth is unclear without reading the full paper.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 4. Metal‐Organic Frameworks for Precise Separation of Radionuclides: Our Journey and Perspective

- Date: `2026-09-23`
- Journal: Chinese Journal of Chemistry
- Link: https://doi.org/10.1002/cjoc.70725
- Tags: adsorption, h2, md, mof, photocatalysis, review, separation
- Authors: Linwei He, Lingyi Li, Zhonglin Ma, Long Chen, Shuao Wang
- Why it matters: Comprehensive Summary The efficient separation of radionuclides is essential for sustainable nuclear energy and nuclear environmental safety.
- Innovation: Comprehensive Summary The efficient separation of radionuclides is essential for sustainable nuclear energy and nuclear environmental safety.
- Likely limitations: Abstract-level evidence is promising, but validation breadth is unclear without reading the full paper.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 5. Biological and bio-derived metal–organic frameworks for sustainable CO₂ capture: Evidence maturity, process readiness, and design criteria

- Date: `2026-09-22`
- Journal: Next Sustainability
- Link: https://doi.org/10.1016/j.nxsust.2026.100521
- Tags: adsorption, co2, h2, high_throughput, mof, oxide, review, separation, water
- Authors: Badril Azhar, Ariel Seanhan Haezer, Syah Sultan Ali Muzakhar, Ardila Hayu Tiwikrama
- Why it matters: Biological metal–organic frameworks (Bio-MOFs) and related bio-derived systems broaden the design space for adsorptive carbon dioxide (CO₂) capture through ligand-derived basic sites, charged pores, host cavities, hydrogen-bond networks, and confined reactive environments.
- Innovation: Biological metal–organic frameworks (Bio-MOFs) and related bio-derived systems broaden the design space for adsorptive carbon dioxide (CO₂) capture through ligand-derived basic sites, charged pores, host cavities, hydrogen-bond networks, and confined reactive environments.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.
