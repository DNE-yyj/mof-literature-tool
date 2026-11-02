# Literature Update

- Generated: `2026-11-02T07:38:27`
- Profile: `materials_ml_transfer`
- Since: `2023-11-03`
- Papers retained: `30`

## Overview

Collected 30 deduplicated papers for profile `materials_ml_transfer`. This transfer profile keeps non-MOF ML papers when they carry a concrete method signal; 30 retained papers are outside direct MOF literature. 30 papers contain transferable method tags and 3 appear in priority journals or major venue families. 14 papers also carry explicit material-system tags, helping judge whether the chemistry is close enough to MOFs.

## Innovation Patterns

- Selection lens: cross-material ML papers are retained when they show a concrete transferable method signal; generic MOF-side ML is treated as lower novelty unless it adds a new angle.

- Foundation, self-supervised, and transfer-learning models are the main route for reusing labels across sparse MOF property tasks.
- Generative and inverse-design workflows are most useful for MOFs when topology, charge, linker-node compatibility, and synthesizability are built in.
- Uncertainty-aware active learning offers a practical way to decide which MOF DFT, GCMC, or MD calculations to run next.

## Common Gaps

- Many cross-material ML methods report strong in-domain metrics but do not prove transfer to porous, metal-node-containing frameworks.
- Methods already used in recent MOF work are only useful here if they add a new representation, label space, uncertainty treatment, or experimental loop.
- High-impact venue status is helpful for triage, but MOF feasibility still depends on data availability, charge treatment, topology constraints, and validation cost.

## Next Opportunities

- For each retained method, run a quick MOF prior-art check and keep only routes that are not already saturated in recent MOF papers.
- Translate promising non-MOF methods into MOF-specific benchmarks with metal-node-aware descriptors, topology constraints, and guest-loaded validation cases.
- Prioritize workflows that reduce label-generation cost or open a new observable, such as flexibility, defects, humid adsorption, diffusion barriers, or active-site reconstruction.

## Paper Briefs

### 1. Direct simulation of LiNi₀.₈Mn₀.₁Co₀.₁O₂ transport properties using an efficient and accurate machine learning potential

- Date: `2026-10-29`
- Journal: NCCR MARVEL
- Link: https://doi.org/10.24435/materialscloud:16-07
- Tags: active_learning, battery, dft, equivariant_ml, force_field, foundation_model, gnn, h2, interatomic_potential, md, ml, oxide, uncertainty
- Authors: Jian He, Nongnuch Artrith
- Why it matters: The rate capability of layered lithium nickel manganese cobalt oxide (NMC) cathode materials is decisive for high-power applications such as fast charging, yet the mechanisms governing lithium-ion transport in NMC remain insufficiently understood, both experimentally and computationally.
- Innovation: The rate capability of layered lithium nickel manganese cobalt oxide (NMC) cathode materials is decisive for high-power applications such as fast charging, yet the mechanisms governing lithium-ion transport in NMC remain insufficiently understood, both experimentally and computationally.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 2. Machine learning-driven inverse design of high-hardness multi-principal element alloys through symbolic regression

- Date: `2026-10-23`
- Journal: Scientific Reports
- Link: https://doi.org/10.1038/s41598-026-74491-7
- Tags: active_learning, alloy, generative_model, h2, high_throughput, ml, physics_informed, separation, surrogate_model, symbolic_regression
- Authors: Peiyi Li
- Why it matters: A comprehensive descriptor library is constructed by integrating elemental fractions, pymatgen-derived atomic physicochemical properties and classical Hume-Rothery metallurgical parameters, which quantitatively captures lattice distortion, electronic effects and phase transformation mechanisms governing alloy hardness.
- Innovation: A comprehensive descriptor library is constructed by integrating elemental fractions, pymatgen-derived atomic physicochemical properties and classical Hume-Rothery metallurgical parameters, which quantitatively captures lattice distortion, electronic effects and phase transformation mechanisms governing alloy hardness.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 3. Universal machine learning force fields for materials simulation: From model construction to complex-system applications

- Date: `2026-10-22`
- Journal: Physica Scripta
- Link: https://doi.org/10.1088/1402-4896/aeb836
- Tags: battery, dft, electrolyte, force_field, h2, high_throughput, interatomic_potential, ml, physics_informed, review, self_supervised, surrogate_model, transfer_learning, uncertainty
- Authors: Guoyang Wang, Jing Yi, Yuanmao Hu, Shuai Zhao
- Why it matters: Abstract Machine learning force fields (MLFFs) can achieve first-principles accuracy within validated chemical and configurational domains while maintaining computational efficiency comparable to classical force fields for atomistic materials simulations.
- Innovation: Abstract Machine learning force fields (MLFFs) can achieve first-principles accuracy within validated chemical and configurational domains while maintaining computational efficiency comparable to classical force fields for atomistic materials simulations.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 4. From Atoms to Reactors: A Critical Review of a Decade of Machine Learning in Heterogeneous Catalysis (2017–2026)

- Date: `2026-10-23`
- Journal: Angewandte Chemie International Edition
- Link: https://doi.org/10.1002/anie.4288841
- Tags: active_learning, adsorption, catalysis, dft, foundation_model, h2, ml, priority_journal, review, water, zeolite
- Authors: Rafael Larraz, Avelino Corma
- Why it matters: ABSTRACT This critical review traces the evolution of machine learning (ML) across the full value chain of heterogeneous catalysis over 2017–2026, from catalyst discovery to reactor and process design, and across the principal reaction families (CO 2 reduction, water splitting, nitrogen chemistry, zeolite‐catalyzed transformations).
- Innovation: ABSTRACT This critical review traces the evolution of machine learning (ML) across the full value chain of heterogeneous catalysis over 2017–2026, from catalyst discovery to reactor and process design, and across the principal reaction families (CO 2 reduction, water splitting, nitrogen chemistry, zeolite‐catalyzed transformations).
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 5. Boltzmann generators for amorphous particle systems

- Date: `2026-10-28`
- Journal: The Journal of Chemical Physics
- Link: https://doi.org/10.1063/5.0353653
- Tags: crystal, equivariant_ml, generative_model, gnn, h2, ml, uncertainty
- Authors: Louis Grenioux, Leonardo Galliano, Ludovic Berthier, Giulio Biroli, Marylou Gabrié
- Why it matters: Here, we develop Boltzmann generators tailored to amorphous materials by building the required equivariances directly into Riemannian stochastic interpolants.
- Innovation: Here, we develop Boltzmann generators tailored to amorphous materials by building the required equivariances directly into Riemannian stochastic interpolants.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 6. Factorised Cartesian Atomic Cluster Expansion for Low-Cost Machine-Learning Interatomic Potentials

- Date: `2026-10-23`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15010957/v1
- Tags: dft, equivariant_ml, h2, interatomic_potential, md, physics_informed, uncertainty
- Authors: Albert Linda
- Why it matters: We present FACE, a factorised Cartesian atomic cluster expansion that removes this bottleneck.
- Innovation: We present FACE, a factorised Cartesian atomic cluster expansion that removes this bottleneck.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 7. Beyond Permeability Prediction: Machine Learning for Gas-Separation Membranes from Data Curation to Experimentally Validated Discovery

- Date: `2026-10-13`
- Journal: Membranes
- Link: https://doi.org/10.3390/membranes16100340
- Tags: active_learning, cof, generative_model, h2, ml, polymer, review, separation, surrogate_model, uncertainty
- Authors: Zhengda Lin, Bingjie Yan, Xinhao Sun, Zhe Fu, Xingwei Du
- Why it matters: We introduce a five-level evidence framework spanning retrospective interpolation, domain-disjoint generalization, physics or simulation confirmation, prospective membrane validation, and deployment-relevant testing.
- Innovation: We introduce a five-level evidence framework spanning retrospective interpolation, domain-disjoint generalization, physics or simulation confirmation, prospective membrane validation, and deployment-relevant testing.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Workflow is likely transferable to MOFs with node-aware descriptors and stronger charge treatment.

### 8. Retention-constrained fine-tuning of a pre-trained aluminium MACE potential for non-equilibrium defect dynamics and plasticity

- Date: `2026-10-26`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2610.35653
- Tags: active_learning, dft, equivariant_ml, h2, interatomic_potential, md, transfer_learning, uncertainty
- Authors: Yue Wu, Yuan Tian, Deng Pan, Mingwei Chen
- Why it matters: Here we achieve this balance for the aluminium MACE potential QP17 by integrating conditional readout uncertainty, iterative full-parameter updates and protocol-compatible relative-energy anchoring.
- Innovation: Here we achieve this balance for the aluminium MACE potential QP17 by integrating conditional readout uncertainty, iterative full-parameter updates and protocol-compatible relative-energy anchoring.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 9. Transfer learning on universal interatomic potential embeddings improves generalization in structure-property defect models

- Date: `2026-10-29`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15003938/v2
- Tags: catalysis, dft, equivariant_ml, force_field, gnn, h2, high_throughput, interatomic_potential, ml, oxide, transfer_learning
- Authors: Matthew David Witman, Sebastian Pujet, Andrew J. E. Rowberg, Christopher Sutton, Joel Basile Varley
- Why it matters: We demonstrate practical impact by revisiting a prior screening of thermochemical water-splitting materials, where improved generalization alters ∼45 % of candidate classifications.
- Innovation: We demonstrate practical impact by revisiting a prior screening of thermochemical water-splitting materials, where improved generalization alters ∼45 % of candidate classifications.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 10. Data-driven discovery of water-splitting electrocatalysts: From predictive machine learning to autonomous optimization

- Date: `2026-10-23`
- Journal: Artificial Intelligence Chemistry
- Link: https://doi.org/10.1016/j.aichem.2026.100136
- Tags: active_learning, adsorption, catalysis, h2, ml, physics_informed
- Authors: Mahalakshmi Vedanarayanan, Chandrasekaran Pitchai, Chia‐Yu Chen, Utkarsh Kumar, Liu Heng-Jui
- Why it matters: By integrating physically meaningful descriptors with predictive algorithms, ML provides a pathway to accelerate catalyst optimization and uncover underlying reaction mechanisms.
- Innovation: By integrating physically meaningful descriptors with predictive algorithms, ML provides a pathway to accelerate catalyst optimization and uncover underlying reaction mechanisms.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 11. Controlling MXene termination ensembles for stability and performance

- Date: `2026-10-30`
- Journal: MRS Bulletin
- Link: https://doi.org/10.1557/s43577-026-01209-5
- Tags: dft, h2, interatomic_potential, md, ml, surrogate_model, two_d_material
- Authors: Bo Spinnler, Sanguk Han, Aleksandra Vojvodić
- Why it matters: Abstract The promise of MXene surface chemistry lies in tuning T $$_{x}$$ x , yet the relevant design variable is not the identity of an individual surface terminating group but the ensemble of local surface environments.
- Innovation: Abstract The promise of MXene surface chemistry lies in tuning T $$_{x}$$ x , yet the relevant design variable is not the identity of an individual surface terminating group but the ensemble of local surface environments.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.

### 12. Autonomous Discovery of Multi‐Material Metamaterials With Programmable Multimodal Thermal Responses via Reinforcement Learning

- Date: `2026-10-28`
- Journal: Advanced Materials
- Link: https://doi.org/10.1002/adma.75546
- Tags: generative_model, h2, ml, multimodal, priority_journal
- Authors: Chenxi Lu, Kewen Pan, Xingran Li, Zhaohui Qiu, Nianyao Chai
- Why it matters: Here we present an inverse design framework integrating Transformer encoder with reinforcement learning (RL) agent.
- Innovation: Here we present an inverse design framework integrating Transformer encoder with reinforcement learning (RL) agent.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 13. A thermodynamic correction layer for machine learning interatomic potentials

- Date: `2026-10-25`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2610.34551
- Tags: crystal, dft, foundation_model, h2, interatomic_potential, md, ml
- Authors: Sarath Kumar Menon, Braulio Sanchez Ortega, Ralf Drautz
- Why it matters: We introduce an additive thermodynamic correction layer that shifts phase free energies towards an assessed reference without retraining or modifying the base potential.
- Innovation: We introduce an additive thermodynamic correction layer that shifts phase free energies towards an assessed reference without retraining or modifying the base potential.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 14. A systematic review of advances in spatiotemporal machine learning for road traffic accident prediction in developing countries

- Date: `2026-10-31`
- Journal: Discover Artificial Intelligence
- Link: https://doi.org/10.1007/s44163-026-02476-6
- Tags: h2, ml, review, transfer_learning, uncertainty
- Authors: Fernaz Narin Nur, Avi Mondal, Sarbajit Paul Bappy, Md. Hasanuzzaman Dipu, Nazmun Nessa Moon
- Why it matters: Low and middle-income countries (LMICs) account for 93% of global road traffic fatalities, yet spatiotemporal machine learning (ML) research remains structurally anchored in high-income contexts.
- Innovation: Low and middle-income countries (LMICs) account for 93% of global road traffic fatalities, yet spatiotemporal machine learning (ML) research remains structurally anchored in high-income contexts.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 15. Machine learning surrogate modelling for enhanced heat transfer in heat exchangers: A state-of-the-art review

- Date: `2026-10-15`
- Journal: Energy and AI
- Link: https://doi.org/10.1016/j.egyai.2026.100931
- Tags: h2, ml, physics_informed, review, surrogate_model
- Authors: Martin Zálešák, Lubomír Klimeš, Pavel Charvát, Jakub Kůdela, Kyung Chun Kim
- Why it matters: Complex heat transfer and fluid flow in heat exchangers (HXs) with intricate geometry challenge conventional empirical correlations, while high-fidelity simulations remain computationally expensive.
- Innovation: Complex heat transfer and fluid flow in heat exchangers (HXs) with intricate geometry challenge conventional empirical correlations, while high-fidelity simulations remain computationally expensive.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 16. SIMPLEX: composition-space deep learning for bio-inspired hydrogel adhesion with prospective validation on model-discovered formulations and interpretable composition rules

- Date: `2026-10-29`
- Journal: Frontiers in Materials
- Link: https://doi.org/10.3389/fmats.2026.1966940
- Tags: active_learning, h2, high_throughput, ml, multimodal, separation, surrogate_model
- Authors: Tongfei Shen, Xueqin Lei, Hung Ka Lok, Huaicheng Li, 潘中泽
- Why it matters: Fast and accurate composition-to-property prediction is critical for accelerating the discovery of multicomponent bio-adhesive hydrogels, yet current surrogate models are predominantly evaluated under random data splits that do not reflect the distribution shift encountered in real-world iterative screening.
- Innovation: Fast and accurate composition-to-property prediction is critical for accelerating the discovery of multicomponent bio-adhesive hydrogels, yet current surrogate models are predominantly evaluated under random data splits that do not reflect the distribution shift encountered in real-world iterative screening.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 17. Tangent-plane evidential uncertainty in active learning for magnetic interatomic potentials

- Date: `2026-10-27`
- Journal: Physical Review Materials
- Link: https://doi.org/10.1103/9hcx-wmmm
- Tags: active_learning, dft, h2, high_throughput, interatomic_potential, uncertainty
- Authors: Yang Cheng, Hongyu Yu, Hongjun Xiang
- Why it matters: Here we extend the $\mathrm{e}^2\mathrm{IP}$ evidential framework to magnetic machine-learning interatomic potentials by formulating the projected spin-force likelihood and the corresponding epistemic uncertainty in the tangent plane orthogonal to the local spin direction.
- Innovation: Here we extend the $\mathrm{e}^2\mathrm{IP}$ evidential framework to magnetic machine-learning interatomic potentials by formulating the projected spin-force likelihood and the corresponding epistemic uncertainty in the tangent plane orthogonal to the local spin direction.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 18. Interpretable Hybrid Surrogate Modeling for Diameter Deviation Prediction in Injection Molding Using Symbolic Regression and Gaussian Process Residual Correction

- Date: `2026-10-27`
- Journal: Research Square
- Link: https://doi.org/10.21203/rs.3.rs-11271710/v1
- Tags: ml, surrogate_model, symbolic_regression, uncertainty
- Authors: Amine Aboutaib, Hanaa Ouaomar, Souad Touairi, Mourad Kadiri
- Why it matters: Abstract Dimensional quality in injection molding is hard to model when process variables act through coupled pressure, flow, and cycle-history effects and the experimental budget is small.
- Innovation: Abstract Dimensional quality in injection molding is hard to model when process variables act through coupled pressure, flow, and cycle-history effects and the experimental budget is small.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 19. A provenance-aware zirconia conductivity database and Arrhenius-constrained screening of doped electrolyte candidates

- Date: `2026-10-26`
- Journal: Machine Learning Science and Technology
- Link: https://doi.org/10.1088/2632-2153/aeb9a7
- Tags: battery, dft, electrolyte, foundation_model, h2, high_throughput, md, oxide, physics_informed, uncertainty
- Authors: Qikai Zhang, Zhihao Jin, Xianfu Chen, Hao Xiong, Yan Yue
- Why it matters: Here we curate a provenance-aware zirconia conductivity database of 1,351 records and use it to compare an Arrhenius-constrained physics-informed machine-learning model (PIML) with an unconstrained deep neural network (DNN).
- Innovation: Here we curate a provenance-aware zirconia conductivity database of 1,351 records and use it to compare an Arrhenius-constrained physics-informed machine-learning model (PIML) with an unconstrained deep neural network (DNN).
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 20. Closed-Loop Reinforcement Learning in De Novo Molecular Design: Bridging Generative AI with Automated Chemical Synthesis

- Date: `2026-10-24`
- Journal: International Journal of Science and Research (IJSR)
- Link: https://doi.org/10.21275/sr261014212517
- Tags: active_learning, equivariant_ml, generative_model, review, uncertainty
- Authors: Michele Covington
- Why it matters: Closed-loop reinforcement learning offers a promising approach to integrating generative molecular design with automated chemical synthesis and experimental evaluation.
- Innovation: Closed-loop reinforcement learning offers a promising approach to integrating generative molecular design with automated chemical synthesis and experimental evaluation.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 21. Synthesis-by-design of ferroelectric Dion–Jacobson two-dimensional hybrid organic–inorganic perovskites

- Date: `2026-10-27`
- Journal: Nature Communications
- Link: https://doi.org/10.1038/s41467-026-78928-5
- Tags: h2, high_throughput, interatomic_potential, perovskite, priority_journal, symbolic_regression
- Authors: Lulu Wang, Weixin He, Shurong Yuan, Chao Yang, Nihang Fu
- Why it matters: Here we show a staged, physically guided synthesis-by-design workflow that integrates learning from scarce ferroelectric data with structure-aware screening.
- Innovation: Here we show a staged, physically guided synthesis-by-design workflow that integrates learning from scarce ferroelectric data with structure-aware screening.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.

### 22. Multi-Fidelity Training Reshapes Uncertainty Decomposition in Atomistic Models

- Date: `2026-10-26`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2610.35560
- Tags: equivariant_ml, h2, md, self_supervised, separation, surrogate_model, transfer_learning, uncertainty
- Authors: Matteo Tolloso, Davide Bacciu, Luigi Bonati
- Why it matters: Multi-fidelity training, which combines abundant low-fidelity data with scarce high-fidelity labels, is increasingly common in atomistic modeling, but its effect on predictive uncertainty remains largely unexplored.
- Innovation: Multi-fidelity training, which combines abundant low-fidelity data with scarce high-fidelity labels, is increasingly common in atomistic modeling, but its effect on predictive uncertainty remains largely unexplored.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 23. Physicochemical rule-embedded generative modeling for constrained peptide therapeutics

- Date: `2026-10-29`
- Journal: npj Drug Discovery.
- Link: https://doi.org/10.1038/s44386-026-00090-1
- Tags: generative_model, h2, md, review, uncertainty
- Authors: Yuzhou Wang, Dongsheng Cao, Xiangzheng Fu, Xiangxiang Zeng, Xiaojun Yao
- Why it matters: Constrained peptides couple covalent topology, stereochemistry, three-dimensional structure, conformational dynamics and developability.
- Innovation: Constrained peptides couple covalent topology, stereochemistry, three-dimensional structure, conformational dynamics and developability.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 24. Infrastructure-Aware Materials Discovery: Resource Allocation, Cost, and Carbon in AI-Driven Workflows

- Date: `2026-10-28`
- Journal: Journal of Physics Materials
- Link: https://doi.org/10.1088/2515-7639/aebabe
- Tags: active_learning, dft, h2, high_throughput, interatomic_potential
- Authors: Naveen Goel, Tridip Das, William A. Goddard
- Why it matters: High-throughput screening of metal–organic frameworks serves as a case study arguing that the optimal balance of elastic, stable, and interruptible resources follows from task duration, computational coupling, and recovery cost rather than from generic cloud-optimization heuristics.
- Innovation: High-throughput screening of metal–organic frameworks serves as a case study arguing that the optimal balance of elastic, stable, and interruptible resources follows from task duration, computational coupling, and recovery cost rather than from generic cloud-optimization heuristics.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 25. Active Learning of Conditional Generative Models via the Transport Neural Tangent Kernel

- Date: `2026-10-26`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2610.35652
- Tags: active_learning, generative_model, h2, high_throughput, separation
- Authors: Jayoung Ryu, Kyunghyun Cho, Romain Lopez
- Why it matters: Many high-throughput scientific experiments produce distributional outputs, requiring conditional generative models to interpret the data, and to predict outcomes at new inputs.
- Innovation: Many high-throughput scientific experiments produce distributional outputs, requiring conditional generative models to interpret the data, and to predict outcomes at new inputs.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 26. Building from the ground up: augmentation strategies to improve protein language model performance on protein sets

- Date: `2026-10-25`
- Journal: bioRxiv (Cold Spring Harbor Laboratory)
- Link: https://doi.org/10.64898/2026.10.20.760553
- Tags: active_learning, force_field, h2, ml, uncertainty
- Authors: Emily Stump, T. S. Hayden Dennison, Pietro Strobbia, George Stan, Ruxandra I. Dima
- Why it matters: Abstract An important underlying requirement for deep learning models is the availability of large datasets, however, in sciences such as chemistry and biology, generating experimental data of sufficient size represents a significant bottleneck.
- Innovation: Abstract An important underlying requirement for deep learning models is the availability of large datasets, however, in sciences such as chemistry and biology, generating experimental data of sufficient size represents a significant bottleneck.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 27. Probing the limits of forward screening and inverse design of crystal materials

- Date: `2026-10-23`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2610.32678
- Tags: crystal, equivariant_ml, generative_model, h2, high_throughput, ml
- Authors: Zhilong Song, Zijun Pang, Lixue Cheng
- Why it matters: Here we probe them by matching the crystals of 55 databases by structure into one self-extending database of 14.6 million crystals and 131.8 million property values, each traced to its source.
- Innovation: Here we probe them by matching the crystals of 55 databases by structure into one self-extending database of 14.6 million crystals and 131.8 million property values, each traced to its source.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 28. Hierarchical universal open structure dataset for atomistic modeling

- Date: `2026-10-15`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2610.21771
- Tags: foundation_model, h2, interatomic_potential, md
- Authors: Sofiia Chorna, Cesare Malosso, Jonathan Schmidt, Michele Ceriotti
- Why it matters: To address these problems, we introduce a protocol to stratify a dataset into a hierarchy of nested subsets, subsampling from the coarsest to the finest resolution based on an "ecumetric" built to reflect the latent space representation of several popular universal machine-learning interatomic potentials.
- Innovation: To address these problems, we introduce a protocol to stratify a dataset into a hierarchy of nested subsets, subsampling from the coarsest to the finest resolution based on an "ecumetric" built to reflect the latent space representation of several popular universal machine-learning interatomic potentials.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 29. Orochi: A Physics-Grounded Python Package for Pair Distribution Function Analysis of Crystalline and Low-Dimensional Materials

- Date: `2026-10-30`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15010802/v3
- Tags: crystal, equivariant_ml, h2, ml, oxide, physics_informed, uncertainty
- Authors: Satoshi Tominaka
- Why it matters: Atomic pair distribution function (PDF) analysis from X-ray total scattering is a powerful methodology for determining atomic structure and arrangements across crystalline, disordered, nanostructured, and low-dimensional materials on both laboratory and synchrotron instruments.
- Innovation: Atomic pair distribution function (PDF) analysis from X-ray total scattering is a powerful methodology for determining atomic structure and arrangements across crystalline, disordered, nanostructured, and low-dimensional materials on both laboratory and synchrotron instruments.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 30. Artificial intelligence in offshore wind geotechnical engineering: A lifecycle-oriented review

- Date: `2026-10-28`
- Journal: Ocean
- Link: https://doi.org/10.26599/ocean.2026.9470032
- Tags: active_learning, force_field, h2, high_throughput, ml, physics_informed, review, surrogate_model
- Authors: Jie Shi, Yimin Lu, Hongjiang Li, Songyu Liu, Mu Linlong
- Why it matters: Abstract As offshore wind develops toward deeper waters and larger turbine capacities, geotechnical challenges are becoming increasingly complex, involving more variable seabed conditions, larger foundation dimensions, and stricter lifecycle reliability and cost-control requirements.
- Innovation: Abstract As offshore wind develops toward deeper waters and larger turbine capacities, geotechnical challenges are becoming increasingly complex, involving more variable seabed conditions, larger foundation dimensions, and stricter lifecycle reliability and cost-control requirements.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
