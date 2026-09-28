# Literature Update

- Generated: `2026-09-28T06:48:39`
- Profile: `materials_ml_transfer`
- Since: `2023-09-29`
- Papers retained: `30`

## Overview

Collected 30 deduplicated papers for profile `materials_ml_transfer`. This transfer profile keeps non-MOF ML papers when they carry a concrete method signal; 30 retained papers are outside direct MOF literature. 30 papers contain transferable method tags and 5 appear in priority journals or major venue families. 21 papers also carry explicit material-system tags, helping judge whether the chemistry is close enough to MOFs.

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

### 1. Quantum-inspired inverse design of heterogeneous catalysts for hydrogen evolution reaction

- Date: `2026-09-18`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02324-2
- Tags: catalysis, generative_model, h2, ml, priority_journal, review, transfer_learning, uncertainty
- Authors: Sangro Lee, Chang Woo Kim, Hyun Woo Kim
- Why it matters: To address these challenges, we introduce a quantum-inspired generative framework for discovering catalytic materials for hydrogen evolution reactions (HER).
- Innovation: To address these challenges, we introduce a quantum-inspired generative framework for discovering catalytic materials for hydrogen evolution reactions (HER).
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 2. A Review of Atomistic Machine Learning for Grain Boundaries in Advanced Manufacturing: From Metastable Structures to Processing–Structure–Property Design

- Date: `2026-09-17`
- Journal: JOM
- Link: https://doi.org/10.1007/s11837-026-08693-9
- Tags: crystal, generative_model, h2, interatomic_potential, ml, physics_informed, review, symbolic_regression, uncertainty
- Authors: Anqi Qiu, Yue Fan
- Why it matters: We first discuss digital representations of grain boundaries, including crystallographic descriptors, SOAP-based local atomic environment fingerprints, and physics-informed descriptors for predicting grain-boundary energy and segregation behavior.
- Innovation: We first discuss digital representations of grain boundaries, including crystallographic descriptors, SOAP-based local atomic environment fingerprints, and physics-informed descriptors for predicting grain-boundary energy and segregation behavior.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 3. OMC-bench and AtomBit-OMC: task-aligned benchmarks and robust, interpretable machine-learned interatomic potentials for organic molecular crystals

- Date: `2026-09-21`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02315-3
- Tags: crystal, equivariant_ml, h2, high_throughput, interatomic_potential, md, physics_informed, priority_journal, uncertainty
- Authors: Muyu Lu, Chengxi Zhao, Siyu Hu, Danyang Chen, Chen Wang
- Why it matters: Here we introduce OMC-bench, a benchmark spanning four practical tasks—large-cell OOD force/stress prediction, lattice dynamics, cocrystal relaxation, and polymorph energy ranking—and an extensive OMC training dataset sampled from near-equilibrium to strongly perturbed regimes.
- Innovation: Here we introduce OMC-bench, a benchmark spanning four practical tasks—large-cell OOD force/stress prediction, lattice dynamics, cocrystal relaxation, and polymorph energy ranking—and an extensive OMC training dataset sampled from near-equilibrium to strongly perturbed regimes.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 4. Overcoming Sampling Limitations Using Machine-Learned Interatomic Potentials: The Case of Water-in-Salt Electrolytes

- Date: `2026-09-21`
- Journal: Journal of Chemical Theory and Computation
- Link: https://doi.org/10.1021/acs.jctc.6c00579
- Tags: battery, dft, electrolyte, equivariant_ml, foundation_model, h2, interatomic_potential, md, ml, surrogate_model, transfer_learning, uncertainty
- Authors: Luca Brugnoli, Mathieu Salanne, A. Marco Saitta, Alessandra Serva, Arthur France‐Lanord
- Why it matters: Here we evaluate the performances of various MACE potentials in modeling a 21 m water-in-salt electrolyte based on lithium bis(trifluoromethanesulfonyl)imide.
- Innovation: Here we evaluate the performances of various MACE potentials in modeling a 21 m water-in-salt electrolyte based on lithium bis(trifluoromethanesulfonyl)imide.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 5. Topology-aware E(3)-equivariant learning for physically consistent piezoelectric tensor prediction

- Date: `2026-09-25`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02331-3
- Tags: crystal, equivariant_ml, gnn, h2, high_throughput, ml, priority_journal, surrogate_model
- Authors: Ruihan Liu, Jianbo Yu, Yu Ji, Hang Ruan, Xiaofeng Yang
- Why it matters: Here we present TopoTENet, a topology-aware E(3)-equivariant neural network that enriches geometric learning with discrete crystal topology through SLICES (string-based crystal representation using labeled quotient graphs) and optimizes message passing via topology-conditioned attention mechanisms.
- Innovation: Here we present TopoTENet, a topology-aware E(3)-equivariant neural network that enriches geometric learning with discrete crystal topology through SLICES (string-based crystal representation using labeled quotient graphs) and optimizes message passing via topology-conditioned attention mechanisms.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 6. Review of AI-driven discovery of cathode anode and electrolyte materials for advancing sodium-ion batteries

- Date: `2026-09-25`
- Journal: Discover Industrial Chemistry and Materials
- Link: https://doi.org/10.1007/s44508-026-00022-x
- Tags: active_learning, alloy, battery, electrolyte, generative_model, gnn, high_throughput, ml, oxide, review
- Authors: Zhong Hu
- Why it matters: AI-driven workflows are explored spanning inverse design, high-throughput screening, property prediction, and autonomous discovery, targeting high-performance materials for next-generation applications.
- Innovation: AI-driven workflows are explored spanning inverse design, high-throughput screening, property prediction, and autonomous discovery, targeting high-performance materials for next-generation applications.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 7. Large Language Models in Chemistry and Materials Science: A Comprehensive Survey

- Date: `2026-09-21`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15009184/v1
- Tags: active_learning, crystal, foundation_model, high_throughput, multimodal, self_supervised, transfer_learning, uncertainty
- Authors: JINSHI LI, CHENGCHUN LIU, CHENGRUI WEI, Yimi Wang, Boxuan Zhao
- Why it matters: We develop a non-exclusive representation-by-mechanism taxonomy linking text, molecular and crystal structures, spectra, images, and numerical properties with model adaptation, cross-representation grounding, external knowledge and tools, and workflow coordination.
- Innovation: We develop a non-exclusive representation-by-mechanism taxonomy linking text, molecular and crystal structures, spectra, images, and numerical properties with model adaptation, cross-representation grounding, external knowledge and tools, and workflow coordination.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 8. Artificial intelligence for predictive mixture toxicology

- Date: `2026-09-19`
- Journal: Toxicology
- Link: https://doi.org/10.1016/j.tox.2026.154589
- Tags: equivariant_ml, gnn, h2, high_throughput, ml, review
- Authors: José L. Domingo, Marilia Cristina Oliveira Souza, Fernando Barbosa
- Why it matters: Machine learning, deep learning, graph neural networks, Bayesian approaches, and natural-language processing can integrate heterogeneous data, including chemical structures, molecular descriptors, toxicokinetics, high-throughput screening results, omics profiles, adverse outcome pathways, biomonitoring data, and epidemiological findings.
- Innovation: Machine learning, deep learning, graph neural networks, Bayesian approaches, and natural-language processing can integrate heterogeneous data, including chemical structures, molecular descriptors, toxicokinetics, high-throughput screening results, omics profiles, adverse outcome pathways, biomonitoring data, and epidemiological findings.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 9. Machine learning kinetics from molecular dynamics data

- Date: `2026-09-15`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2609.17736
- Tags: generative_model, h2, md, ml, review, self_supervised
- Authors: Jonathan Weare, Aaron R. Dinner
- Why it matters: We develop a common operator viewpoint connecting generator-based partial differential equations, variational principles, Markov state models, dynamical Galerkin approximation, and neural networks.
- Innovation: We develop a common operator viewpoint connecting generator-based partial differential equations, variational principles, Markov state models, dynamical Galerkin approximation, and neural networks.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 10. Agent-E2MD: Autonomous Translation of Interatomic Potential Equations into Physically Validated Pair Styles for Molecular Dynamics in LAMMPS

- Date: `2026-09-22`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2609.26657
- Tags: crystal, high_throughput, interatomic_potential, md, oxide, physics_informed, symbolic_regression
- Authors: Bilvin Varughese, Orcun Yildiz, Aditya Koneru, Henry Chan, Tom Peterka
- Why it matters: We introduce Agent-E2MD, a knowledge-guided agentic workflow that translates user-specified interatomic models into executable LAMMPS pair styles.
- Innovation: We introduce Agent-E2MD, a knowledge-guided agentic workflow that translates user-specified interatomic models into executable LAMMPS pair styles.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.

### 11. Integration of density functional theory and machine learning for materials discovery in energy applications

- Date: `2026-09-22`
- Journal: Discover Chemistry.
- Link: https://doi.org/10.1007/s44371-026-00985-y
- Tags: active_learning, adsorption, battery, catalysis, dft, electrocatalysis, h2, high_throughput, ml, photocatalysis, review, uncertainty, water
- Authors: Jeslin Jebish G P
- Why it matters: Examine how DFT generated datasets, encompassing bandgap values, formation energies, adsorption energies, and electronic structure descriptors, serve as the foundation for training predictive ML models, and delineate the methodological pipeline that connects them.
- Innovation: Examine how DFT generated datasets, encompassing bandgap values, formation energies, adsorption energies, and electronic structure descriptors, serve as the foundation for training predictive ML models, and delineate the methodological pipeline that connects them.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 12. Boundary-driven phase transformation in layered 3R In2Se3 captured by long range machine learning molecular dynamics

- Date: `2026-09-22`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15009227/v1
- Tags: crystal, equivariant_ml, h2, interatomic_potential, md, ml, separation
- Authors: Igor Evangelista, Michaela Cohen, Atul C. Thakur, Anderson Janotti, Chris Benmore
- Why it matters: Here we develop a PBE+D3(BJ)-trained MACERSGA interatomic potential that adds a reciprocal-space gated-attention long-range correction to a short-range MACE backbone.
- Innovation: Here we develop a PBE+D3(BJ)-trained MACERSGA interatomic potential that adds a reciprocal-space gated-attention long-range correction to a short-range MACE backbone.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 13. Transferable Graph Neural Network Surrogates for Molecular Dynamics Across Crystal Symmetries

- Date: `2026-09-21`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15009166/v1
- Tags: crystal, gnn, h2, md, ml, separation, surrogate_model
- Authors: Judah Immanuel, Avik Mahata, Aniruddha Maiti
- Why it matters: We present a transferable graph neural network (GNN) surrogate framework for molecular dynamics (MD) that directly predicts atomic displacements and propagates atomistic configurations without explicit force evaluation or numerical time integration.
- Innovation: We present a transferable graph neural network (GNN) surrogate framework for molecular dynamics (MD) that directly predicts atomic displacements and propagates atomistic configurations without explicit force evaluation or numerical time integration.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 14. Computational Sustainability for Climate-Resilient Materials: AI-Driven Decarbonization Pathways for Cement and Industrial Systems

- Date: `2026-09-21`
- Journal: Science Engineering and Technology
- Link: https://doi.org/10.54327/set2026/v6.i2.351
- Tags: co2, h2, high_throughput, md, ml, physics_informed, review, separation, uncertainty
- Authors: Oluwafemi Ezekiel Ige, Musasa Kabeya
- Why it matters: Cement production remains a major industrial source of anthropogenic CO₂ because emissions arise from both limestone calcination and high-temperature fuel combustion.
- Innovation: Cement production remains a major industrial source of anthropogenic CO₂ because emissions arise from both limestone calcination and high-temperature fuel combustion.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 15. Embedding Physics Priors in Robot Learning: A Survey

- Date: `2026-09-15`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2609.22319
- Tags: foundation_model, h2, image_analysis, md, ml, physics_informed, review
- Authors: Mattia Piccinini, Lucas Schulze, Alice Plebe, Matteo Saveriano, Thomas Beckers
- Why it matters: The rapid progress of artificial intelligence is reshaping robotics and accelerating the adoption of learning-based approaches.
- Innovation: The rapid progress of artificial intelligence is reshaping robotics and accelerating the adoption of learning-based approaches.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Map the method onto MOF structure images, spectra, isotherm curves, or generated-structure consistency checks. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Distant-domain method can be useful if it maps to a concrete MOF object such as structure images, spectra, isotherms, pore maps, or multimodal consistency checks.

### 16. Polymer Informatics in the Era of Foundation Models: From Representation to Autonomous Design

- Date: `2026-09-23`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15009334/v1
- Tags: foundation_model, generative_model, h2, polymer, review, self_supervised
- Authors: Jianxin He, Ying Li
- Why it matters: Foundation models, pretrained on broad datasets and adapted to multiple tasks, offer a way to reuse chemical knowledge across polymer property prediction and inverse design.
- Innovation: Foundation models, pretrained on broad datasets and adapted to multiple tasks, offer a way to reuse chemical knowledge across polymer property prediction and inverse design.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 17. Triplet Pruning and Spatial Decomposition in M3GNet: Accuracy and Memory Trade-offs in Scaling Graph Neural Network Potentials

- Date: `2026-09-23`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15001250/v2
- Tags: alloy, foundation_model, gnn, h2, interatomic_potential, md, ml
- Authors: Linh La, Yugam Aggarwal, Truyen Tran, Svetha Venkatesh, Sherif Abdulkader Tawfik
- Why it matters: Machine-learning interatomic potentials of several functional forms now support large-scale atomistic simulation.Within this landscape, graph neural network (GNN) potentials such as M3GNet offer transferable message-passing models, but their application to very large systems remains limited by graph construction, message passing, and differentiable force-evaluation costs.In M3GNet, the explicit angular pathway is represented through line-graph triplets, whose construction can dominate inference cost.Here we examine the scalability of M3GNet molecular dynamics via inference-time triplet pruning.We first show that an apparent insensitivity to triplet removal in inspected MatGL implementations originates from an incorrect parent-bond index mapping; after correction, removing triplets substantially increases static energy, force, stress, and property-prediction errors.In short molecular-dynamics trajectories, however, the structural response is strongly system dependent, with some systems showing modest radial-distribution-function changes despite a threefold reduction in inference cost.We then implement and evaluate an owned-core/halo spatial chunking scheme that bounds activation memory during differentiable force evaluation and enables M3GNet simulations of million-atom alloy cells on GPU hardware.These results show that triplet pruning can provide useful acceleration when validated for the target observable, while spatial decomposition offers a more general route to extending GNN potentials to large atomistic systems.
- Innovation: Machine-learning interatomic potentials of several functional forms now support large-scale atomistic simulation.Within this landscape, graph neural network (GNN) potentials such as M3GNet offer transferable message-passing models, but their application to very large systems remains limited by graph construction, message passing, and differentiable force-evaluation costs.In M3GNet, the explicit angular pathway is represented through line-graph triplets, whose construction can dominate inference cost.Here we examine the scalability of M3GNet molecular dynamics via inference-time triplet pruning.We first show that an apparent insensitivity to triplet removal in inspected MatGL implementations originates from an incorrect parent-bond index mapping; after correction, removing triplets substantially increases static energy, force, stress, and property-prediction errors.In short molecular-dynamics trajectories, however, the structural response is strongly system dependent, with some systems showing modest radial-distribution-function changes despite a threefold reduction in inference cost.We then implement and evaluate an owned-core/halo spatial chunking scheme that bounds activation memory during differentiable force evaluation and enables M3GNet simulations of million-atom alloy cells on GPU hardware.These results show that triplet pruning can provide useful acceleration when validated for the target observable, while spatial decomposition offers a more general route to extending GNN potentials to large atomistic systems.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 18. Bayesian optimization in chemical compound sub-spaces using low-dimensional molecular descriptors

- Date: `2026-09-17`
- Journal: Machine Learning Science and Technology
- Link: https://doi.org/10.1088/2632-2153/aea960
- Tags: active_learning, h2, high_throughput, ml, physics_informed, surrogate_model
- Authors: Yun-Wen Mao, Roman V. Krems
- Why it matters: We present a data-efficient optimization framework that combines three components: (i) a very low-dimensional, physics-informed molecular descriptor that substantially reduces the dimensionality of the optimization problem, (ii) Bayesian optimization for efficient exploration of the resulting descriptor space, and (iii) a modular inverse mapping framework converting optimized descriptor vectors into chemically valid molecular structure.
- Innovation: We present a data-efficient optimization framework that combines three components: (i) a very low-dimensional, physics-informed molecular descriptor that substantially reduces the dimensionality of the optimization problem, (ii) Bayesian optimization for efficient exploration of the resulting descriptor space, and (iii) a modular inverse mapping framework converting optimized descriptor vectors into chemically valid molecular structure.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 19. UpTCR: a unified progressive knowledge transfer foundation model for robust T-cell receptor-antigen binding recognition

- Date: `2026-09-24`
- Journal: Nature Communications
- Link: https://doi.org/10.1038/s41467-026-78075-x
- Tags: foundation_model, h2, priority_journal, self_supervised
- Authors: Tianxu Lv, Yang Xiao, Li Chen, Bing He, Maiyi Zhong
- Why it matters: Here, we present UpTCR, a unified progressive knowledge-transfer foundation model that learns from incomplete data to predict TCR-antigen-HLA binding.
- Innovation: Here, we present UpTCR, a unified progressive knowledge-transfer foundation model that learns from incomplete data to predict TCR-antigen-HLA binding.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 20. Explicit modelling of lift characteristics for high-lift devices based on knowledge-guided symbolic regression using large language model

- Date: `2026-09-11`
- Journal: Engineering Applications of Computational Fluid Mechanics
- Link: https://doi.org/10.1080/19942060.2026.2728948
- Tags: foundation_model, md, ml, multimodal, surrogate_model, symbolic_regression
- Authors: Yiheng Wang, kefeng zheng, Chengpeng Liu, Wenping Song, Qingfu Zhang
- Why it matters: The High-Lift Device (HLD) plays a critical role in determining the low-speed aerodynamic performance of aircraft during takeoff and landing phases.
- Innovation: The High-Lift Device (HLD) plays a critical role in determining the low-speed aerodynamic performance of aircraft during takeoff and landing phases.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 21. ARTIFICIAL INTELLIGENCE IN STEEL STRUCTURES: METHODS, APPLICATIONS AND PERSPECTIVES ON JOINT BEHAVIOUR

- Date: `2026-09-22`
- Journal: unknown
- Link: https://doi.org/10.67563/asesconf2026057m
- Tags: h2, ml, physics_informed, review, surrogate_model
- Authors: Aleksa Milićević, Filip Ljubinković, Ana Francisca Santos, L R Silva
- Why it matters: Artificial intelligence (AI) is emerging as a powerful tool in structural engineering, enabling data-driven alternatives to traditional analytical and numerical methods.
- Innovation: Artificial intelligence (AI) is emerging as a powerful tool in structural engineering, enabling data-driven alternatives to traditional analytical and numerical methods.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 22. Generative AI and Neurosymbolic Frameworks in Next-Generation Digital Signal Processing

- Date: `2026-09-21`
- Journal: IntechOpen eBooks
- Link: https://doi.org/10.5772/intechopen.1017137
- Tags: generative_model, h2, md, ml, multimodal, review
- Authors: Joceli Mayer
- Why it matters: This perspective chapter presents a structured survey of the paradigm shift occurring at the intersection of generative artificial intelligence (GenAI) and digital signal processing (DSP), tracing the technical evolution from deterministic, human-engineered frameworks toward self-evolving neurosymbolic architectures.
- Innovation: This perspective chapter presents a structured survey of the paradigm shift occurring at the intersection of generative artificial intelligence (GenAI) and digital signal processing (DSP), tracing the technical evolution from deterministic, human-engineered frameworks toward self-evolving neurosymbolic architectures.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 23. Structure of Molten FeCl2 and FeCl3

- Date: `2026-09-17`
- Journal: ACS Materials Au
- Link: https://doi.org/10.1021/acsmaterialsau.6c00155
- Tags: battery, electrocatalysis, equivariant_ml, h2, high_throughput, interatomic_potential, md, ml, polymer
- Authors: Fakhrul Hasan Bhuiyan, Jicheng Guo, Christopher J. Benmore, Avery L. Blockmon, Denis Johnson
- Why it matters: Abstract Molten iron chlorides are central to emerging energy technologies including electrochemical iron production and redox flow batteries.
- Innovation: Abstract Molten iron chlorides are central to emerging energy technologies including electrochemical iron production and redox flow batteries.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 24. Process analytical technology (PAT) and real-time control in chemical manufacturing

- Date: `2026-09-24`
- Journal: Advances in Differential Equations and Control Processes
- Link: https://doi.org/10.59400/adecp3800
- Tags: active_learning, crystal, equivariant_ml, h2, polymer, review, uncertainty
- Authors: Yan Yan
- Why it matters: Process analytical technology (PAT) has expanded the ability to obtain timely information about manufacturing processes and product-related attributes.
- Innovation: Process analytical technology (PAT) has expanded the ability to obtain timely information about manufacturing processes and product-related attributes.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 25. MACHINE LEARNING FOR CELLULOSE MEMBRANES: A REPRESENTATION–MODEL–TASK FRAMEWORK FOR SMALL-DATA REGIMES

- Date: `2026-09-22`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15009248/v1
- Tags: dft, generative_model, h2, ml, oxide, polymer, review, separation
- Authors: Ye O. Kolomiiets
- Why it matters: Cellulose membranes are a small-data problem with a chemically ambiguous object.
- Innovation: Cellulose membranes are a small-data problem with a chemically ambiguous object.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 26. AI-Driven Optimization of Electrochemical Fertilizer Processes

- Date: `2026-09-22`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15009257/v1
- Tags: active_learning, battery, catalysis, dft, electrocatalysis, electrolyte, h2, high_throughput, ml, review
- Authors: Muhammad Qamar Bilal
- Why it matters: Conventional fertilizer production relies on centralized, fossil-fuel-intensive processes such as Haber–Bosch ammonia synthesis, with high energy demand and associated carbon emissions.
- Innovation: Conventional fertilizer production relies on centralized, fossil-fuel-intensive processes such as Haber–Bosch ammonia synthesis, with high energy demand and associated carbon emissions.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 27. Machine Learning Applications to Physical Processes

- Date: `2026-09-22`
- Journal: Open Scholarship Institutional Repository (Washington University in St. Louis)
- Link: https://openscholarship.wustl.edu/art_sci_etds/3902
- Tags: crystal, dft, h2, ml, physics_informed
- Authors: W.D. Charles
- Why it matters: This thesis demonstrates how machine learning techniques can solve computationally challenging problems across diverse areas of physics, from high-energy astrophysics to condensed matter systems, accelerating traditional computation.
- Innovation: This thesis demonstrates how machine learning techniques can solve computationally challenging problems across diverse areas of physics, from high-energy astrophysics to condensed matter systems, accelerating traditional computation.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 28. Development of an automated evaluation system for the process-structure-property relationship of structural metallic materials towards autonomous exploration

- Date: `2026-09-18`
- Journal: Science and Technology of Advanced Materials Methods
- Link: https://doi.org/10.1080/27660400.2026.2735657
- Tags: active_learning, alloy, h2, high_throughput, priority_journal
- Authors: Yulin Xie, Sayaka Sekida, Masaya Inakawa, Ryo Tamura, Tadashi Furuhara
- Why it matters: Automated high-throughput experiments on the one- and two-step tempering of a JIS SCM435H alloy are performed to demonstrate the capability and efficiency of the system, and the accuracy of the resulting property data is validated by manually measured hardness.
- Innovation: Automated high-throughput experiments on the one- and two-step tempering of a JIS SCM435H alloy are performed to demonstrate the capability and efficiency of the system, and the accuracy of the resulting property data is validated by manually measured hardness.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 29. Classical DFT energies and equilibrium configurations obtained by GNN-driven Monte Carlo simulations for solvent-free polymer-grafted nanoparticles

- Date: `2026-09-24`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2605.30822
- Tags: dft, equivariant_ml, gnn, h2, md, ml, polymer
- Authors: Mehryar Jannesari Ghomsheh, Sarah Hormozi, Donald L. Koch
- Why it matters: This deposit contains the configuration–energy datasets and equilibrium configurations supporting the manuscript "Probing the many-body energy landscape of a soft glass with graph neural networks." We train an equivariant graph neural network (NequIP) on classical density functional theory energies of solvent-free polymer-grafted nanoparticles, a model soft glass in which grafted polymers uniformly fill the interstitial space and generate strong angular-dependent many-body interactions between the cores.
- Innovation: This deposit contains the configuration–energy datasets and equilibrium configurations supporting the manuscript "Probing the many-body energy landscape of a soft glass with graph neural networks." We train an equivariant graph neural network (NequIP) on classical density functional theory energies of solvent-free polymer-grafted nanoparticles, a model soft glass in which grafted polymers uniformly fill the interstitial space and generate strong angular-dependent many-body interactions between the cores.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 30. Label-Efficient Generative Inverse Design and Design-Rule Discovery in Freeform Topological Photonics

- Date: `2026-09-23`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2609.28401
- Tags: crystal, generative_model, h2, md
- Authors: Yuhan Zhang, Xin Xie, Bowen Song, Lixuan Chen, Liyue Shen
- Why it matters: % Here we report generative inverse design of freeform valley photonic crystals.
- Innovation: % Here we report generative inverse design of freeform valley photonic crystals.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
