# Literature Update

- Generated: `2026-11-02T07:39:42`
- Profile: `mof_ml_method_prior_art`
- Since: `2016-11-04`
- Papers retained: `11`

## Overview

Collected 11 deduplicated papers for profile `mof_ml_method_prior_art`. `ML` appears in 7 papers and `DFT` in 3. `Catalysis` themes appear more often (5) than `adsorption/separation` themes (4). `Interatomic-potential` or MLIP-style work appears in 1 papers and is a notable transfer path from COF-side methods to MOFs.

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

### 2. Revisiting Percolation and Molecular Diffusion in Disordered Pore Networks

- Date: `2026-10-25`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15011012/v1
- Tags: h2, high_throughput, md, ml, mof, porous_material, separation, symbolic_regression
- Authors: Chao Zheng, Arun Gopalan, Kaihang Shi
- Why it matters: Symbolic regression identifies the percolating backbone fraction as a key, yet largely overlooked, topology-related descriptor that captures a common diffusion trend across classes.
- Innovation: Symbolic regression identifies the percolating backbone fraction as a key, yet largely overlooked, topology-related descriptor that captures a common diffusion trend across classes.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 3. Predictive Synthesis of MOFs and COFs

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

### 4. Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks via Machine Learning-Symbolic Regression

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

### 5. Reliable methane storage screening and inverse design of metal organic frameworks under distribution shift

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

### 6. An adaptive deep learning for cross‐condition adsorption prediction in metal‐organic frameworks

- Date: `2026-10-29`
- Journal: AIChE Journal
- Link: https://doi.org/10.1002/aic.70731
- Tags: adsorption, high_throughput, ml, mof, separation
- Authors: Zhenglu Yang, Jiyu Cui, Lifeng Yang, Xiaofei Lu, Anyun Zhang
- Why it matters: Abstract Accurate prediction of gas adsorption across diverse scenarios is essential for accelerating the discovery of metal–organic frameworks (MOFs) tailored for gas separation, capture, and storage.
- Innovation: Abstract Accurate prediction of gas adsorption across diverse scenarios is essential for accelerating the discovery of metal–organic frameworks (MOFs) tailored for gas separation, capture, and storage.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 7. Mechanical versus thermal amorphization of ZIF-4: from local rearrangements to network disorder

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

### 8. Identifying Hidden Trends in Complex Data to Design Best Metal-Organic-Framework Catalysts for Oxygen Evolution Reaction

- Date: `2026-09-01`
- Journal: Research Square
- Link: https://doi.org/10.21203/rs.3.rs-10782265/v1
- Tags: catalysis, catalyst_descriptor, dft, h2, ml, mof
- Authors: Liangliang Xu, Jian Zhou, Canhui Zhang, Jiaqian Wang, Jinpei Huang
- Why it matters: Here we introduce hidden trend mining, integrating descriptor learning, gradient boosting regression, and subgroup discovery to identify local structure activity relationships.
- Innovation: Here we introduce hidden trend mining, integrating descriptor learning, gradient boosting regression, and subgroup discovery to identify local structure activity relationships.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 9. Metal–Organic Frameworks for Sustainable Photocatalytic and Electrocatalytic HMF‐to‐FDCA Conversion: From Catalyst Engineering to Energy‐Saving Paired Electrolysis Systems

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

### 10. Graph-dependent pooling: adaptive granularity in hierarchical graph neural networks

- Date: `2026-10-24`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2610.33623
- Tags: gnn, h2, high_throughput, ml, mof
- Authors: Bohan Yoon, Hyejin Jang
- Why it matters: Graph Neural Networks are widely used to learn structural representations of relational data.
- Innovation: Graph Neural Networks are widely used to learn structural representations of relational data.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 11. MOFjson: An Explicit Topological Representation of Metal-Organic Frameworks for Language Models

- Date: `2026-10-25`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2610.34549
- Tags: crystal, h2, high_throughput, mof
- Authors: Anabel Yong, Matthew Hart, Philippe Schwaller
- Why it matters: We present MOFjson, the first representation separating structural data into a raw atomic layer with explicit bond shift vectors and a derived layer exposing secondary building units (metal nodes and organic linkers) and network topology.
- Innovation: We present MOFjson, the first representation separating structural data into a raw atomic layer with explicit bond shift vectors and a derived layer exposing secondary building units (metal nodes and organic linkers) and network topology.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Validate the method on a broader material set and compare against experimental observables.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.
