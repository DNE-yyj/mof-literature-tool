# Literature Update

- Generated: `2026-06-01T13:02:58`
- Profile: `mof_ml_method_prior_art`
- Since: `2016-06-03`
- Papers retained: `15`

## Overview

Collected 15 deduplicated papers for profile `mof_ml_method_prior_art`. `ML` appears in 8 papers and `DFT` in 8. `Catalysis` themes appear more often (4) than `adsorption/separation` themes (1). `Interatomic-potential` or MLIP-style work appears in 7 papers and is a notable transfer path from COF-side methods to MOFs.

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

### 1. Evaluating mechanical property prediction across material classes using molecular dynamics simulations with universal machine-learned interatomic potentials

- Date: `2026-05-06`
- Journal: Communications Chemistry
- Link: https://doi.org/10.1038/s42004-026-02057-9
- Tags: dft, equivariant_ml, force_field, gnn, h2, high_throughput, interatomic_potential, md, ml, mof
- Authors: Konstantin Stracke, Connor Edwards, Jack D. Evans
- Why it matters: Simulating the mechanical and thermal properties of materials requires accurate treatment of interatomic interactions, yet quantum-mechanical methods can be computationally prohibitive for the time scales needed.
- Innovation: Simulating the mechanical and thermal properties of materials requires accurate treatment of interatomic interactions, yet quantum-mechanical methods can be computationally prohibitive for the time scales needed.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 2. Harnessing AtomisticSkills for Agentic Atomistic Research

- Date: `2026-05-18`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2605.24002
- Tags: battery, catalysis, co2, dft, electrolyte, foundation_model, h2, high_throughput, interatomic_potential, md, ml, mof, multimodal, oxide, separation, transfer_learning
- Authors: Bowen Deng, Bohan Li, Matthew Cox, Hoje Chun, Juno Nam
- Why it matters: Here, we introduce AtomisticSkills, an open-source harness framework that empowers general-purpose AI coding agents to conduct atomistic research across materials science, chemistry, and drug discovery.
- Innovation: Here, we introduce AtomisticSkills, an open-source harness framework that empowers general-purpose AI coding agents to conduct atomistic research across materials science, chemistry, and drug discovery.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 3. PoroNet: An Intrinsically Interpretable Pore Graph Neural Network for Resolving Pore-Level Adsorption in Metal–Organic Frameworks

- Date: `2026-05-28`
- Journal: Journal of Chemical Theory and Computation
- Link: https://doi.org/10.1021/acs.jctc.6c00100
- Tags: adsorption, catalysis, gnn, h2, high_throughput, ml, mof, separation
- Authors: Chao Zheng, Arun Gopalan, Kaihang Shi
- Why it matters: In this work, we introduce PoroNet, an intrinsically interpretable graph neural network architecture built on a graph representation of the pore network (i.e., pore graph).
- Innovation: In this work, we introduce PoroNet, an intrinsically interpretable graph neural network architecture built on a graph representation of the pore network (i.e., pore graph).
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 4. Smart Catalyst Design: Integrating Structure–Activity Relationships with Computational and Data-Driven Approaches

- Date: `2026-04-22`
- Journal: International Journal of Creative and Open Research in Engineering and Management
- Link: https://doi.org/10.55041/ijcope.v2i4.571
- Tags: catalysis, co2, electrocatalysis, high_throughput, ml, mof, review, separation
- Authors: Ramandeep Singh Ramandeep Singh, Rekha Rana Rekha Rana, Subhi Sharma Subhi Sharma, Jeewanjot Singh Jeewanjot Singh, Isha dhiman Isha dhiman
- Why it matters: Special attention is given to the emerging approaches based on the exploitation of designer-like methods, high-throughput experimentation, and data-driven approaches, to explore huge compositional and structural spaces.
- Innovation: Special attention is given to the emerging approaches based on the exploitation of designer-like methods, high-throughput experimentation, and data-driven approaches, to explore huge compositional and structural spaces.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 5. aim2dat: A Python infrastructure for automated ab initio material modeling and data analysis

- Date: `2026-04-29`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2604.26551
- Tags: battery, dft, h2, high_throughput, ml, mof
- Authors: Holger‐Dietrich Saßnick, Joshua Edzards, Timo Reents, Caterina Cocchi
- Why it matters: Herein, we introduce the Automated Ab Initio Materials Modeling and Data Analysis Toolkit (aim2dat), a Python package offering a user-friendly interface to generate and handle big data, design high-throughput workflows based on density functional theory calculations, and analyze the output.
- Innovation: Herein, we introduce the Automated Ab Initio Materials Modeling and Data Analysis Toolkit (aim2dat), a Python package offering a user-friendly interface to generate and handle big data, design high-throughput workflows based on density functional theory calculations, and analyze the output.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 6. Supporting Dataset for Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry

- Date: `2026-04-28`
- Journal: The University of Adelaide
- Link: https://doi.org/10.25909/32061111
- Tags: crystal, dft, high_throughput, interatomic_potential, md, mof
- Authors: Connor Edwards, Jack D. Evans
- Why it matters: This dataset contains computational data supporting the research article "Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry." The repository includes ab initio molecular dynamics (AIMD) trajectories, CP2K input files, and analysis scripts used in the study.
- Innovation: This dataset contains computational data supporting the research article "Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry." The repository includes ab initio molecular dynamics (AIMD) trajectories, CP2K input files, and analysis scripts used in the study.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 7. Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry

- Date: `2026-04-28`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2604.25262
- Tags: co2, dft, equivariant_ml, foundation_model, h2, high_throughput, interatomic_potential, md, mof, separation
- Authors: Connor Edwards, Jack D. Evans
- Why it matters: Here, we present a new high-temperature benchmarking dataset of 40~ps ab~initio molecular dynamics (AIMD) trajectories simulated at 300, 1000, and 2000 K for nine zinc- and zirconium-based metal-organic frameworks (MOFs): ZIF-8, CALF-20, MOF-10, MOF-5, MIP-206, UiO-66, UiO-67, UiO-66-NH2, and NU-1000.
- Innovation: Here, we present a new high-temperature benchmarking dataset of 40~ps ab~initio molecular dynamics (AIMD) trajectories simulated at 300, 1000, and 2000 K for nine zinc- and zirconium-based metal-organic frameworks (MOFs): ZIF-8, CALF-20, MOF-10, MOF-5, MIP-206, UiO-66, UiO-67, UiO-66-NH2, and NU-1000.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 8. Supporting Dataset for Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry

- Date: `2026-04-28`
- Journal: The University of Adelaide
- Link: https://doi.org/10.25909/32061111.v1
- Tags: crystal, dft, high_throughput, interatomic_potential, md, mof
- Authors: Connor Edwards, Jack D. Evans
- Why it matters: This dataset contains computational data supporting the research article "Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry." The repository includes ab initio molecular dynamics (AIMD) trajectories, CP2K input files, and analysis scripts used in the study.
- Innovation: This dataset contains computational data supporting the research article "Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry." The repository includes ab initio molecular dynamics (AIMD) trajectories, CP2K input files, and analysis scripts used in the study.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 9. Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry

- Date: `2026-04-28`
- Journal: arXiv (Cornell University)
- Link: https://doi.org/10.48550/arxiv.2604.25262
- Tags: co2, dft, equivariant_ml, foundation_model, h2, high_throughput, interatomic_potential, md, mof, separation
- Authors: Connor Edwards, Jack D. Evans
- Why it matters: Here, we present a new high-temperature benchmarking dataset of 40~ps ab~initio molecular dynamics (AIMD) trajectories simulated at 300, 1000, and 2000 K for nine zinc- and zirconium-based metal-organic frameworks (MOFs): ZIF-8, CALF-20, MOF-10, MOF-5, MIP-206, UiO-66, UiO-67, UiO-66-NH2, and NU-1000.
- Innovation: Here, we present a new high-temperature benchmarking dataset of 40~ps ab~initio molecular dynamics (AIMD) trajectories simulated at 300, 1000, and 2000 K for nine zinc- and zirconium-based metal-organic frameworks (MOFs): ZIF-8, CALF-20, MOF-10, MOF-5, MIP-206, UiO-66, UiO-67, UiO-66-NH2, and NU-1000.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 10. ReadMOF: Structure-Free Semantic Embeddings from Systematic MOF Nomenclature for Machine Learning

- Date: `2026-04-13`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15001888/v1
- Tags: foundation_model, h2, high_throughput, ml, mof
- Authors: Kewei Zhu, Cameron Wilson, Bartosz Mazur, Yi Li, Ashleigh M. Chester
- Why it matters: Here we introduce ReadMOF, which is, to our knowledge, the first nomenclature-free machine learning framework that leverages these names to model structure-property relationships without requiring atomic coordinates or connectivity graphs.
- Innovation: Here we introduce ReadMOF, which is, to our knowledge, the first nomenclature-free machine learning framework that leverages these names to model structure-property relationships without requiring atomic coordinates or connectivity graphs.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 11. ReadMOF: Structure-Free Semantic Embeddings from Systematic MOF Nomenclature for Machine Learning

- Date: `2026-04-12`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2604.10568
- Tags: foundation_model, h2, high_throughput, ml, mof
- Authors: Kewei Zhu, Cameron Wilson, Bartosz Mazur, Yi Li, Ashleigh M. Chester
- Why it matters: Here we introduce ReadMOF, which is, to our knowledge, the first nomenclature-free machine learning framework that leverages these names to model structure-property relationships without requiring atomic coordinates or connectivity graphs.
- Innovation: Here we introduce ReadMOF, which is, to our knowledge, the first nomenclature-free machine learning framework that leverages these names to model structure-property relationships without requiring atomic coordinates or connectivity graphs.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 12. Hunting Structural Demons in Digital Reticular Chemistry: Lessons From Metal‐Organic Frameworks

- Date: `2026-05-21`
- Journal: Israel Journal of Chemistry
- Link: https://doi.org/10.1002/ijch.70028
- Tags: crystal, h2, high_throughput, mof, review
- Authors: Yongchul G. Chung, Myoung Soo Lah
- Why it matters: Digital reticular chemistry relies on accurate crystal structures to power computational screening, data‐driven discovery, and structure‐property analysis, yet recent studies reveal that more than half of the top‐performing candidates in major computational screening campaigns are chemically invalid.
- Innovation: Digital reticular chemistry relies on accurate crystal structures to power computational screening, data‐driven discovery, and structure‐property analysis, yet recent studies reveal that more than half of the top‐performing candidates in major computational screening campaigns are chemically invalid.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Validate the method on a broader material set and compare against experimental observables.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 13. Comparative entropy analysis of 2D transition metal tetrahydroxyquinones via machine learning approaches

- Date: `2026-01-31`
- Journal: Scientific Reports
- Link: https://doi.org/10.1038/s41598-026-37731-4
- Tags: h2, ml, mof, oxide
- Authors: Muhammad Irfan, Nabeela Bashir, AbdulGuddoos S. A. Gaid, Turke Althobaiti, Hamood Ur Rehman
- Why it matters: To this end, we develop and compare three machine learning based regression models: logarithmic, random forest, and XGBoost.
- Innovation: To this end, we develop and compare three machine learning based regression models: logarithmic, random forest, and XGBoost.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 14. Generation of magnetic metal-organic frameworks

- Date: `2026-04-30`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2604.27879
- Tags: battery, dft, foundation_model, high_throughput, interatomic_potential, mof, transfer_learning
- Authors: Alexander C. Tyner, Avinash Pathapati, Alexander V. Balatsky
- Why it matters: The potential to utilize metal-organic frameworks as a replacement for rare earth materials as well as in technological applications has prompted increased interested in this material class.
- Innovation: The potential to utilize metal-organic frameworks as a replacement for rare earth materials as well as in technological applications has prompted increased interested in this material class.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 15. BaLoRA: Bayesian Low-Rank Adaptation of Large Scale Models

- Date: `2026-04-27`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2605.08110
- Tags: foundation_model, h2, mof, transfer_learning, uncertainty
- Authors: Dario Coscia, Sindy Löwe, Max Welling
- Why it matters: We introduce BaLoRA, a Bayesian extension of LoRA with a novel input-adaptive Bayesian parameterization of LoRA matrices that adds minimal parameters and compute.
- Innovation: We introduce BaLoRA, a Bayesian extension of LoRA with a novel input-adaptive Bayesian parameterization of LoRA matrices that adds minimal parameters and compute.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.
