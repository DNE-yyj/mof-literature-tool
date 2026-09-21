# Literature Update

- Generated: `2026-09-21T06:16:57`
- Profile: `materials_ml_transfer`
- Since: `2023-09-22`
- Papers retained: `30`

## Overview

Collected 30 deduplicated papers for profile `materials_ml_transfer`. This transfer profile keeps non-MOF ML papers when they carry a concrete method signal; 29 retained papers are outside direct MOF literature. 30 papers contain transferable method tags and 7 appear in priority journals or major venue families. 14 papers also carry explicit material-system tags, helping judge whether the chemistry is close enough to MOFs.

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

### 1. A Review of Atomistic Machine Learning for Grain Boundaries in Advanced Manufacturing: From Metastable Structures to Processing–Structure–Property Design

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

### 2. Benchmarking Machine-Learning Interatomic Potentials for Dynamical Stability in Inorganic Semiconductor Nanocrystals: A CdSe Case Study

- Date: `2026-09-14`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2609.15299
- Tags: active_learning, crystal, dft, equivariant_ml, force_field, h2, high_throughput, interatomic_potential, md, uncertainty
- Authors: M. Usman, M. Suleymanova, Z. U. Abideen, M. Fernández-Pendás, I. Infante
- Why it matters: Machine-learning interatomic potentials (MLIPs) enable nanosecond-scale atomistic simulations of inorganic semiconductor nanocrystals, but low errors on held-out configurations do not necessarily guarantee stable molecular dynamics.
- Innovation: Machine-learning interatomic potentials (MLIPs) enable nanosecond-scale atomistic simulations of inorganic semiconductor nanocrystals, but low errors on held-out configurations do not necessarily guarantee stable molecular dynamics.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 3. Physics-guided diffusion models for inverse design of disordered metamaterials

- Date: `2026-09-17`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02328-y
- Tags: generative_model, h2, md, ml, physics_informed, priority_journal
- Authors: Ziyuan Xie, Weipeng Xu, Dazhi Zhao, Wenchang Zhang, Daoyang Dong
- Why it matters: Drawing inspiration from classifier guidance, we develop a sampling strategy that directly incorporates physics guidance into the reverse stochastic differential equations.
- Innovation: Drawing inspiration from classifier guidance, we develop a sampling strategy that directly incorporates physics guidance into the reverse stochastic differential equations.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 4. Physics-informed automated surface reconstruction via low-energy electron diffraction based on Bayesian optimization

- Date: `2026-09-09`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02297-2
- Tags: active_learning, crystal, physics_informed, priority_journal
- Authors: Xiankang Tang, Ruiwen Xie, Jan P. Hofmann, Hongbin Zhang
- Why it matters: Abstract Low-energy electron diffraction (LEED) is a cornerstone technique for determining surface atomic structures 1 , yet the quantitative analysis of electron diffraction intensity as a function of incident electron energy—that is, LEED- I(V) analysis—remains a complex inverse problem.
- Innovation: Abstract Low-energy electron diffraction (LEED) is a cornerstone technique for determining surface atomic structures 1 , yet the quantitative analysis of electron diffraction intensity as a function of incident electron energy—that is, LEED- I(V) analysis—remains a complex inverse problem.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 5. Machine Learning for Structural Steels: Materials Design, Property Prediction, Durability, and Future Directions

- Date: `2026-08-25`
- Journal: Materials
- Link: https://doi.org/10.3390/ma19173612
- Tags: active_learning, h2, ml, multimodal, physics_informed, review, uncertainty
- Authors: Guomin Wei, Minghe Li, Bo Cui, Wencui Xiu, Asmawan Mohd Sarman
- Why it matters: Machine learning (ML) provides new opportunities to model the nonlinear relationships among composition, processing, microstructure, defects, properties, and in-service degradation of structural steels.
- Innovation: Machine learning (ML) provides new opportunities to model the nonlinear relationships among composition, processing, microstructure, defects, properties, and in-service degradation of structural steels.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 6. DFT-based machine-learning for the rational design of magnetocaloric high-entropy alloys

- Date: `2026-08-25`
- Journal: Nature Communications
- Link: https://doi.org/10.1038/s41467-026-77123-w
- Tags: alloy, catalyst_descriptor, dft, h2, high_throughput, ml, physics_informed, priority_journal
- Authors: Zhe Cui, Carlos Romero‐Muñiz, Jia Yan Law, V. Franco
- Why it matters: Applying this framework to MM’X family uncovers a fundamental design dichotomy: mean electronic descriptors govern baseline phase stability, while dispersion descriptors, specifically the magnetic-moment dispersion, drive the critical transformation response.
- Innovation: Applying this framework to MM’X family uncovers a fundamental design dichotomy: mean electronic descriptors govern baseline phase stability, while dispersion descriptors, specifically the magnetic-moment dispersion, drive the critical transformation response.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.

### 7. Out-of-Distribution Inverse Design of Elastic Networks with Differentiable Graph Neural Network Molecular Dynamics

- Date: `2026-09-06`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2609.06655
- Tags: generative_model, gnn, h2, md, ml, uncertainty
- Authors: Sergey A. Shteingolts, Salman N. Salman, Ron Levie, Dan Mendels
- Why it matters: Here, we present a differentiable inverse design framework based on a graph neural network molecular dynamics simulator.
- Innovation: Here, we present a differentiable inverse design framework based on a graph neural network molecular dynamics simulator.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 8. Deep learning in materials electron microscopy: models, applications and emerging trends

- Date: `2026-08-24`
- Journal: Machine Learning Science and Technology
- Link: https://doi.org/10.1088/2632-2153/ae9dea
- Tags: foundation_model, generative_model, high_throughput, md, ml, multimodal, review
- Authors: Camilo Augusto Fernandes Salvador, Clovis Lapointe, Thomas Bilyk, E. Meslin, Mihai‐Cosmin Marinica
- Why it matters: Abstract The intersection of deep learning (DL) and materials electron microscopy (EM) has significantly expanded since the early 2010 s; however, the diversity of model architectures and use cases makes it hard to identify literature gaps and determine which models are well-established in this field of application.
- Innovation: Abstract The intersection of deep learning (DL) and materials electron microscopy (EM) has significantly expanded since the early 2010 s; however, the diversity of model architectures and use cases makes it hard to identify literature gaps and determine which models are well-established in this field of application.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 9. Domain-specific dataset enable accurate MLIPs for disordered halide-based solid electrolytes

- Date: `2026-09-10`
- Journal: Machine Learning Science and Technology
- Link: https://doi.org/10.1088/2632-2153/aea5d8
- Tags: battery, crystal, dft, electrolyte, equivariant_ml, foundation_model, h2, high_throughput, interatomic_potential, transfer_learning
- Authors: Chiku Parida, Arghya Bhowmik, J. M. Garcı́a-Lastra
- Why it matters: We present an MLIP training database for Li 3 MX 6 -type halide electrolytes, where M can be group-3, group-13, and group-15 elements as well as lanthanides, and X represents halogens.
- Innovation: We present an MLIP training database for Li 3 MX 6 -type halide electrolytes, where M can be group-3, group-13, and group-15 elements as well as lanthanides, and X represents halogens.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 10. Large language model-enabled automated data extraction for concrete materials informatics

- Date: `2026-09-14`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02304-6
- Tags: foundation_model, h2, high_throughput, ml, priority_journal, uncertainty
- Authors: Zhanzhao Li, Kengran Yang, Qiyao He, Kai Gong
- Why it matters: Here, we introduce a generalizable large language model (LLM)-powered pipeline for automated extraction and structuring of materials data from unstructured scientific literature, using concrete materials as a representative and particularly challenging example.
- Innovation: Here, we introduce a generalizable large language model (LLM)-powered pipeline for automated extraction and structuring of materials data from unstructured scientific literature, using concrete materials as a representative and particularly challenging example.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 11. AI-accelerated discovery of altermagnetic metal-organic frameworks via interpretable machine learning

- Date: `2026-09-14`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02323-3
- Tags: dft, h2, high_throughput, ml, mof, priority_journal, symbolic_regression
- Authors: Yue Ran, Jingyi Duan, Yikai Chen, Wei Jiang, Yugui Yao
- Why it matters: Altermagnetism has emerged as a third class of collinear magnetism, yet its exploration remains largely confined to inorganic materials.
- Innovation: Altermagnetism has emerged as a third class of collinear magnetism, yet its exploration remains largely confined to inorganic materials.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 12. Accelerating density functional theory calculations using conditional generative-adversarial neural networks

- Date: `2026-09-09`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02308-2
- Tags: dft, md, ml, priority_journal, surrogate_model
- Authors: Calin-Andrei Pantis-Simut, Nicolae Filipoiu, Andrei Manolescu, George Alexandru Nemneş
- Why it matters: We introduce the mcv2v-cGAN model based on conditional generative-adversarial networks (cGANs), which performs a multi-channel voxel-to-voxel mapping from readily available structural information to the final self-consistent charge density.
- Innovation: We introduce the mcv2v-cGAN model based on conditional generative-adversarial networks (cGANs), which performs a multi-channel voxel-to-voxel mapping from readily available structural information to the final self-consistent charge density.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 13. Defect engineering of semiconductor photocatalysts for solar energy conversion: from atomic-level design to AI-driven materials discovery for sustainable development and clean energy

- Date: `2026-09-08`
- Journal: Materials & Design
- Link: https://doi.org/10.1016/j.matdes.2026.116917
- Tags: catalysis, dft, force_field, generative_model, h2, high_throughput, md, ml, photocatalysis, review, separation
- Authors: N. Prabhu, Seifedine Kadry
- Why it matters: The solar energy conversion based on semiconductor photocatalysis suffers from the low absorption of visible light, the quick recombination of charge carriers, the slow surface reaction kinetics and the low long-term stability.
- Innovation: The solar energy conversion based on semiconductor photocatalysis suffers from the low absorption of visible light, the quick recombination of charge carriers, the slow surface reaction kinetics and the low long-term stability.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 14. Explicit modelling of lift characteristics for high-lift devices based on knowledge-guided symbolic regression using large language model

- Date: `2026-09-11`
- Journal: Engineering Applications of Computational Fluid Mechanics
- Link: https://doi.org/10.1080/19942060.2026.2728948
- Tags: foundation_model, md, ml, multimodal, surrogate_model, symbolic_regression
- Authors: Yiheng Wang, Kefeng Zheng, Chengpeng Liu, Wenping Song, Qingfu Zhang
- Why it matters: The High-Lift Device (HLD) plays a critical role in determining the low-speed aerodynamic performance of aircraft during takeoff and landing phases.
- Innovation: The High-Lift Device (HLD) plays a critical role in determining the low-speed aerodynamic performance of aircraft during takeoff and landing phases.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 15. Supporting data for "Multi-fidelity Machine Learning Interatomic Potentials for Charged Point Defects"

- Date: `2026-09-14`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2603.05238
- Tags: dft, equivariant_ml, h2, high_throughput, interatomic_potential, ml, surrogate_model
- Authors: Xinwei Wang, Irea Mosquera‐Lois, Aron Walsh
- Why it matters: This repository contains the data and models supporting the publication “Multi-fidelity Machine Learning Interatomic Potentials for Charged Point Defects” (DOI: 10.1103/tzwd-cl3y).
- Innovation: This repository contains the data and models supporting the publication “Multi-fidelity Machine Learning Interatomic Potentials for Charged Point Defects” (DOI: 10.1103/tzwd-cl3y).
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 16. Performance of universal machine learning potentials in global optimization of inorganic crystal structures

- Date: `2026-09-09`
- Journal: Machine Learning Science and Technology
- Link: https://doi.org/10.1088/2632-2153/ae94e1
- Tags: crystal, dft, equivariant_ml, foundation_model, h2, high_throughput, interatomic_potential, ml, separation
- Authors: Edan T. Marcial, L. N. Chaudhary, Olesya Gorbunova, Aleksey N. Kolmogorov
- Why it matters: Abstract Rapid development of universal machine learning potentials (uMLPs) and expansion of training data sets are reshaping the state of the art in atomistic simulation, highlighting the need for concurrent systematic benchmarking of their capabilities.
- Innovation: Abstract Rapid development of universal machine learning potentials (uMLPs) and expansion of training data sets are reshaping the state of the art in atomistic simulation, highlighting the need for concurrent systematic benchmarking of their capabilities.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 17. Artificial Intelligence in Materials Discovery: A Comprehensive Review of Methods, Applications, and Future Directions

- Date: `2026-09-15`
- Journal: WORLD JOURNAL OF INNOVATION AND MODERN TECHNOLOGY
- Link: https://doi.org/10.56201/wjimt.v10.no3.2026.pg9.25
- Tags: generative_model, h2, ml, review
- Authors: Imasuen Aishat Omoh
- Why it matters: Artificial intelligence (AI) is transforming the landscape of materials discovery by addressing the limitations of traditional experimental and computational approaches.
- Innovation: Artificial intelligence (AI) is transforming the landscape of materials discovery by addressing the limitations of traditional experimental and computational approaches.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 18. Study of ordering in (MoCrTi)100-xAlx refractory high-entropy alloys using machine learning interatomic potential

- Date: `2026-09-13`
- Journal: Journal of Materials Research and Technology
- Link: https://doi.org/10.1016/j.jmrt.2026.09.075
- Tags: alloy, force_field, h2, interatomic_potential, md, ml, uncertainty
- Authors: Jiyao Zhang, Klemens Lechner, Markus Maßwohl, Petra Spoerk-Erdely, David Holec
- Why it matters: Refractory high-entropy alloys are promising candidates for high-temperature applications, yet the effects of composition on their chemical-ordering pathways and mechanical properties remain insufficiently understood.
- Innovation: Refractory high-entropy alloys are promising candidates for high-temperature applications, yet the effects of composition on their chemical-ordering pathways and mechanical properties remain insufficiently understood.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 19. Entropy-Guided Dataset Reduction for Machine-Learned Interatomic Potentials

- Date: `2026-09-09`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15008542/v1
- Tags: crystal, h2, interatomic_potential, uncertainty
- Authors: Benjamin Laubach, Joshua A. Vita, Kyle Bushick, Logan Williams, Vincenzo Lordi
- Why it matters: We present a pruning framework that addresses this problem by adapting the bandwidth independently for distinct thermodynamic subsets of the training dataset using an automatable elbow criterion applied to QUESTS informationentropy metrics.
- Innovation: We present a pruning framework that addresses this problem by adapting the bandwidth independently for distinct thermodynamic subsets of the training dataset using an automatable elbow criterion applied to QUESTS informationentropy metrics.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 20. Multiplexed embryo profiling links cellular state to zygotic genome activation in single cells

- Date: `2026-09-17`
- Journal: Nature Communications
- Link: https://doi.org/10.1038/s41467-026-77784-7
- Tags: h2, high_throughput, image_analysis, md, multimodal, priority_journal
- Authors: M. W. Hess, Marvin F. Wyss, Edlyn Wu, Gian-Marco Schaniel, Joel Lüthi
- Why it matters: Here, we introduce high-throughput 3D in toto iterative immunofluorescence imaging (3D-4i) and a dedicated computer vision pipeline to quantify morphological and molecular features from subcellular to whole-embryo scales across hundreds of samples.
- Innovation: Here, we introduce high-throughput 3D in toto iterative immunofluorescence imaging (3D-4i) and a dedicated computer vision pipeline to quantify morphological and molecular features from subcellular to whole-embryo scales across hundreds of samples.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Map the method onto MOF structure images, spectra, isotherm curves, or generated-structure consistency checks.
- MOF relevance: Distant-domain method can be useful if it maps to a concrete MOF object such as structure images, spectra, isotherms, pore maps, or multimodal consistency checks.

### 21. Neural-Network Solutions to Real-Space Charge Density and Generalization

- Date: `2026-09-14`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2609.14906
- Tags: crystal, dft, h2, high_throughput, ml, uncertainty
- Authors: Yuxuan Zeng, Taoyuze Lv, Zhicheng Zhong
- Why it matters: The Hohenberg-Kohn theorem establishes that, in principle, the ground state (GS) charge density contains all GS information of a many-electron system, such that all GS observables can be expressed as functionals of the GS charge density.
- Innovation: The Hohenberg-Kohn theorem establishes that, in principle, the ground state (GS) charge density contains all GS information of a many-electron system, such that all GS observables can be expressed as functionals of the GS charge density.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 22. Navigating Sparse Singlet Fission Chemical Space: An Intelligent Generative-Predictive Paradigm

- Date: `2026-09-12`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2609.15136
- Tags: dft, generative_model, h2, high_throughput, ml
- Authors: Longfei Lv, Li Fu, Si Zhou, Lingzhi Zhao, Jijun Zhao
- Why it matters: Because of low hit rates and trial-and-error computational waste on nonviable structures, conventional high-throughput virtual screening faces significant constraints, even when accelerated by machine learning models.
- Innovation: Because of low hit rates and trial-and-error computational waste on nonviable structures, conventional high-throughput virtual screening faces significant constraints, even when accelerated by machine learning models.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 23. Fiber optic sensing for structural health monitoring in harsh environments advancing degradation physics signal robustness and long term reliability prediction

- Date: `2026-09-17`
- Journal: Discover Civil Engineering
- Link: https://doi.org/10.1007/s44290-026-00613-9
- Tags: h2, ml, physics_informed, review
- Authors: Muhammad Rafi, Khairul Arifin M Noh
- Why it matters: Fiber optic sensing (FOS) technologies have emerged as transformative platforms for structural health monitoring (SHM) of critical infrastructure operating in harsh environments.
- Innovation: Fiber optic sensing (FOS) technologies have emerged as transformative platforms for structural health monitoring (SHM) of critical infrastructure operating in harsh environments.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 24. Ensemble of Artificial Neural Network and Deep Learning for the Prevention of Real-Time Phishing of Financial Data: A Systematic Literature Review

- Date: `2026-09-17`
- Journal: INTERNATIONAL JOURNAL OF COMPUTER SCIENCE AND MATHEMATICAL THEORY E-ISSN
- Link: https://doi.org/10.56201/ijcsmt.vol.12.no2.2026.pg82.120
- Tags: h2, ml, review, uncertainty
- Authors: Gbolahan Babatunde Ajayi
- Why it matters: This study systematically reviewed relevant literatures on unsupervised machine learning models that have been used for detecting phishing in real-time.
- Innovation: This study systematically reviewed relevant literatures on unsupervised machine learning models that have been used for detecting phishing in real-time.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 25. Acoustic and Elastic Metamaterials for Vibration Control, Wave Manipulation, and Energy Harvesting: A Review

- Date: `2026-09-15`
- Journal: Engineering Research Express
- Link: https://doi.org/10.1088/2631-8695/aea801
- Tags: generative_model, h2, ml, review
- Authors: Borhan Uddin Chowdhury, Arafat Anzir, Sk Sazin Ahmed, Sonjoy Chandra Debnath, Mir Imran Bin Samad
- Why it matters: Abstract Acoustic and elastic metamaterials have emerged as a versatile class of architected materials capable of controlling wave propagation through structural design rather than intrinsic composition alone.
- Innovation: Abstract Acoustic and elastic metamaterials have emerged as a versatile class of architected materials capable of controlling wave propagation through structural design rather than intrinsic composition alone.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 26. Leveraging Machine Learning Interatomic Potentials into Fitting Fast and Accurate AMBER-Compatible Precise Force Field

- Date: `2026-09-14`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15008812/v1
- Tags: force_field, h2, interatomic_potential, md, ml, water
- Authors: 周序超, Xujian Wang, Jiahao Xie, Leshen Zhang, Junmei Wang
- Why it matters: Transferable force fields enable routine molecular dynamics simulations across broad chemical space, but finite transferable parameter sets may not describe unusual chemical environments with uniform accuracy.Here, we present ParmFit, an automated preciseforce-field parameterization framework within MAPLE that uses machine-learning interatomic potentials to efficiently construct and refine AMBER/GAFF-compatible parameters.ParmFit extends this strategy across small molecules, chemically modified biomolecular residues, and metal coordination environments while selectively retaining compatible force field terms.In a challenging subset of FreeSolv, UMA-based precise parameters reduced the average hydration free-energy prediction error by more than 1 kcal mol -1 , while ParmFit-generated models of covalently modified proteins and metalloproteins maintained stable structural and coordination behavior in molecular dynamics simulations.By integrating efficient MLIP calculations, selective parameter refinement, and direct compatibility with established force-field workflows, ParmFit provides a practical route toward broader use of precise force fields in molecular simulation.
- Innovation: Transferable force fields enable routine molecular dynamics simulations across broad chemical space, but finite transferable parameter sets may not describe unusual chemical environments with uniform accuracy.Here, we present ParmFit, an automated preciseforce-field parameterization framework within MAPLE that uses machine-learning interatomic potentials to efficiently construct and refine AMBER/GAFF-compatible parameters.ParmFit extends this strategy across small molecules, chemically modified biomolecular residues, and metal coordination environments while selectively retaining compatible force field terms.In a challenging subset of FreeSolv, UMA-based precise parameters reduced the average hydration free-energy prediction error by more than 1 kcal mol -1 , while ParmFit-generated models of covalently modified proteins and metalloproteins maintained stable structural and coordination behavior in molecular dynamics simulations.By integrating efficient MLIP calculations, selective parameter refinement, and direct compatibility with established force-field workflows, ParmFit provides a practical route toward broader use of precise force fields in molecular simulation.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.

### 27. Conditional deep generative modeling of blood-based infrared spectra enables controlled in-silico phenotyping studies

- Date: `2026-09-17`
- Journal: npj Digital Medicine
- Link: https://doi.org/10.1038/s41746-026-03226-9
- Tags: generative_model, h2, md, uncertainty
- Authors: Niklas Leopold-Kerschbaumer, Timo Halenke, Selina Süzeroğlu, Moritz Jung, Mariia Seleznova
- Why it matters: Here, we introduce a conditional deep generative framework for synthesizing blood-based infrared spectra that preserves individual-level structure while allowing controlled manipulation of demographic and anthropometric covariates.
- Innovation: Here, we introduce a conditional deep generative framework for synthesizing blood-based infrared spectra that preserves individual-level structure while allowing controlled manipulation of demographic and anthropometric covariates.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 28. Uncertainty-aware active-learning design of high-strength, corrosion-resistant as-extruded Mg–Al–Zn–Mn–Ca–Y alloys using Bayesian neural networks

- Date: `2026-09-16`
- Journal: Journal of Magnesium and Alloys
- Link: https://doi.org/10.1016/j.jma.2026.102293
- Tags: active_learning, alloy, electrocatalysis, h2, uncertainty
- Authors: Joung Sik Suh, Jae Hoon Jang, Jae‐Yeon Kim, Sung Hyuk Park
- Why it matters: The present study proposes an uncertainty-aware design framework for as-extruded Mg–Al–Zn–Mn–Ca–Y alloys by integrating Bayesian neural network (BNN)-based property prediction, uncertainty-driven active learning (AL), and experimental validation.
- Innovation: The present study proposes an uncertainty-aware design framework for as-extruded Mg–Al–Zn–Mn–Ca–Y alloys by integrating Bayesian neural network (BNN)-based property prediction, uncertainty-driven active learning (AL), and experimental validation.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 29. Breaking Extrapolation Barriers: Dual Innovations for Property and Component Design of Multi‐Component Alloy

- Date: `2026-09-16`
- Journal: Materials Genome Engineering Advances
- Link: https://doi.org/10.1002/mgea.70096
- Tags: alloy, h2, ml, symbolic_regression, transfer_learning
- Authors: Zhigang Yu, Boyu Zhao, Jianhua Chen, Jun Luan, Yunying Fan
- Why it matters: ABSTRACT Data‐driven materials science integrates domain knowledge with machine learning (ML), yet ML's extrapolation limitations on small datasets are often overlooked.
- Innovation: ABSTRACT Data‐driven materials science integrates domain knowledge with machine learning (ML), yet ML's extrapolation limitations on small datasets are often overlooked.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 30. Formation of Strong Brønsted Acid Sites on Aluminosilicate Surfaces during Catalytic Cracking

- Date: `2026-09-10`
- Journal: ACS Catalysis
- Link: https://doi.org/10.1021/acscatal.6c03544
- Tags: catalysis, dft, equivariant_ml, h2, interatomic_potential, porous_material, water
- Authors: Kaustubh J. Sawant, David Stockwell, Anthony DeBellis, Roel Sanchez-Carrera, Lucas Dorazio
- Why it matters: Using NH3 binding as a descriptor of Brønsted acidity, we find that mullite can host acid sites with strengths reaching ΔENH3 ≈ –140 kJ mol−1 in 3:2 mullite, which is comparable to external zeolitic acid sites and substantially stronger than those reported on Si-doped γ–Al2O3.
- Innovation: Using NH3 binding as a descriptor of Brønsted acidity, we find that mullite can host acid sites with strengths reaching ΔENH3 ≈ –140 kJ mol−1 in 3:2 mullite, which is comparable to external zeolitic acid sites and substantially stronger than those reported on Si-doped γ–Al2O3.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
