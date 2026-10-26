# Literature Update

- Generated: `2026-10-26T06:07:48`
- Profile: `mof_ml_method_prior_art`
- Since: `2016-10-28`
- Papers retained: `8`

## Overview

Collected 8 deduplicated papers for profile `mof_ml_method_prior_art`. `ML` appears in 6 papers and `DFT` in 3. `Adsorption/separation` themes appear more often (4) than `catalysis` themes (4). `Interatomic-potential` or MLIP-style work appears in 1 papers and is a notable transfer path from COF-side methods to MOFs.

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

### 2. Predictive Synthesis of MOFs and COFs

- Date: `2026-10-08`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2610.12739
- Tags: cof, crystal, h2, ml, mof, review, uncertainty
- Authors: Bin Feng, Reid A. Coyle, Shyam Chand Pal, Peter Walther, Saeun Park
- Why it matters: Predictive synthesis concerns the prospective modeling of how a targeted structure can be realized.
- Innovation: Predictive synthesis concerns the prospective modeling of how a targeted structure can be realized.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 3. Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks via Machine Learning-Symbolic Regression

- Date: `2026-08-15`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2608.14990
- Tags: adsorption, catalyst_descriptor, co2, h2, md, ml, mof, symbolic_regression, transfer_learning
- Authors: Yimin Shao, Shengluo Ma, Shenghong Ju, Yijun Shi, Wei Li
- Why it matters: This work presents a machine learning-symbolic regression (ML-SR) strategy to develop a physically interpretable formula for predicting low pressure CO2 adsorption capacity in hypothetical metal-organic frameworks (hMOFs).
- Innovation: This work presents a machine learning-symbolic regression (ML-SR) strategy to develop a physically interpretable formula for predicting low pressure CO2 adsorption capacity in hypothetical metal-organic frameworks (hMOFs).
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 4. AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications

- Date: `2026-07-03`
- Journal: Frontiers in Chemistry
- Link: https://doi.org/10.3389/fchem.2026.1864044
- Tags: active_learning, adsorption, catalysis, catalyst_descriptor, co2, dft, electrocatalysis, h2, high_throughput, ml, mof, separation
- Authors: Sreenivas Punna, Suvarshitha Pusuluru, Madhumita Ravikumar, Farid Menaa
- Why it matters: The incorporation of artificial intelligence (AI) into energy systems has become a transformative strategy for tackling global energy related challenges, particularly energy vulnerability (EVI).
- Innovation: The incorporation of artificial intelligence (AI) into energy systems has become a transformative strategy for tackling global energy related challenges, particularly energy vulnerability (EVI).
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 5. Mechanical versus thermal amorphization of ZIF-4: from local rearrangements to network disorder

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

### 6. Hybrid sampling approach to machine-learning potentials for gas adsorption: Hydrogen adsorption in MOF-303

- Date: `2026-10-05`
- Journal: Physical Review Materials
- Link: https://doi.org/10.1103/d5b5-66b6
- Tags: adsorption, catalysis, co2, dft, force_field, gcmc, h2, high_throughput, md, mof, oxide, porous_material, separation
- Authors: Kartik Sau, Ikutaro Hamada, Tamio Ikeshoji, Yiming Lu, Susmita Roy
- Why it matters: Here, we present an approach to generating machine-learning potentials (MLPs) tailored for grand canonical Monte Carlo (GCMC) simulations of gas adsorption.
- Innovation: Here, we present an approach to generating machine-learning potentials (MLPs) tailored for grand canonical Monte Carlo (GCMC) simulations of gas adsorption.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 7. A grouped split silently removes the chemistry entangled with its grouping variable: the case of MOF topology hold-out

- Date: `2026-10-20`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15010692/v1
- Tags: co2, h2, high_throughput, ml, mof, separation
- Authors: Tao Wang
- Why it matters: Machine learning screens metal–organic frameworks (MOFs) for CO2 capture, and 2026 studies on enumerated databases have converged on topology hold-out as a test of topological transferability, presupposing untested separability of topology and chemistry.
- Innovation: Machine learning screens metal–organic frameworks (MOFs) for CO2 capture, and 2026 studies on enumerated databases have converged on topology hold-out as a test of topological transferability, presupposing untested separability of topology and chemistry.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 8. Large language model agents accelerate inverse design of metal-organic frameworks for gas separation

- Date: `2026-07-12`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2607.10559
- Tags: active_learning, foundation_model, gcmc, generative_model, h2, high_throughput, ml, mof, separation
- Authors: Zhaolin Hu, Hehe Fan, Wangyihan Guo, Meng Xu, Chenhao Rao
- Why it matters: Here, we present LEMO Agent, a large-language-model agent framework for closed-loop inverse design of gas-separation MOFs in MOFid space.
- Innovation: Here, we present LEMO Agent, a large-language-model agent framework for closed-loop inverse design of gas-separation MOFs in MOFid space.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.
