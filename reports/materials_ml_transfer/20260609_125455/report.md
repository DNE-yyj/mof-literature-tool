# Literature Update

- Generated: `2026-06-09T12:54:55`
- Profile: `materials_ml_transfer`
- Since: `2023-06-10`
- Papers retained: `30`

## Overview

Collected 30 deduplicated papers for profile `materials_ml_transfer`. This transfer profile keeps cross-material ML papers when they carry a concrete method signal; 30 retained papers are outside direct MOF literature. 30 papers contain transferable method tags and 9 appear in priority journals or major venue families. 12 papers also carry explicit material-system tags, helping judge whether the chemistry is close enough to MOFs.

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

### 1. Prototype-Guided Latent Alignment for Data-Efficient Fine-Tuning of Molecular Foundation Models

- Date: `2026-05-28`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2605.29969
- Tags: dft, equivariant_ml, foundation_model, gnn, h2, high_throughput, interatomic_potential, ml, transfer_learning, uncertainty
- Authors: Rushikesh Pawar, Harshit Rawat, Ayush Kumar, Phani Motamarri
- Why it matters: Machine learning interatomic potentials (MLIPs) have transformed materials discovery by leveraging graph neural networks (GNNs) to predict material properties with near density functional theory (DFT) accuracy.
- Innovation: Machine learning interatomic potentials (MLIPs) have transformed materials discovery by leveraging graph neural networks (GNNs) to predict material properties with near density functional theory (DFT) accuracy.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 2. MEIDNet: multimodal generative AI framework for inverse materials design

- Date: `2026-05-29`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02153-3
- Tags: dft, equivariant_ml, generative_model, gnn, h2, ml, multimodal, perovskite, priority_journal, self_supervised
- Authors: Anand Babu, Rogério Almeida Gouvêa, Pierre Vandergheynst, Gian-Marco Rignanese
- Why it matters: In this work, we present Multimodal Equivariant Inverse Design Network (MEIDNet), a framework that jointly learns structural information and materials properties through contrastive learning, while encoding structures via an equivariant graph neural network (EGNN).
- Innovation: In this work, we present Multimodal Equivariant Inverse Design Network (MEIDNet), a framework that jointly learns structural information and materials properties through contrastive learning, while encoding structures via an equivariant graph neural network (EGNN).
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 3. A graph neural network for the era of large atomistic models

- Date: `2026-05-25`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02146-2
- Tags: battery, catalysis, dft, foundation_model, gnn, h2, interatomic_potential, ml, priority_journal, transfer_learning, two_d_material
- Authors: Duo Zhang, Anyang Peng, Chun Cai, Wentao Li, Yuanchang Zhou
- Why it matters: We present DPA3, a multi-layer graph neural network founded on line graph series (LiGS), designed for the era of LAMs.
- Innovation: We present DPA3, a multi-layer graph neural network founded on line graph series (LiGS), designed for the era of LAMs.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 4. Towards Automated Discovery: A Review of Generative Models, Multimodal Learning and Closed-Loop Workflows in Inverse Materials Design

- Date: `2026-06-01`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2606.02507
- Tags: active_learning, crystal, generative_model, h2, high_throughput, md, multimodal, physics_informed, review
- Authors: Anand Babu, Rogério Almeida Gouvêa, Gian-Marco Rignanese
- Why it matters: Inverse materials design is shifting materials discovery from forward prediction to targeted proposal of candidates that satisfy objectives under physical constraints.
- Innovation: Inverse materials design is shifting materials discovery from forward prediction to targeted proposal of candidates that satisfy objectives under physical constraints.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 5. Towards Automated Discovery: A Review of Generative Models, Multimodal Learning and Closed-Loop Workflows in Inverse Materials Design

- Date: `2026-06-01`
- Journal: arXiv (Cornell University)
- Link: https://doi.org/10.48550/arxiv.2606.02507
- Tags: active_learning, crystal, generative_model, h2, high_throughput, md, multimodal, physics_informed, review
- Authors: Anand Babu, Rogério Almeida Gouvêa, Gian-Marco Rignanese
- Why it matters: Inverse materials design is shifting materials discovery from forward prediction to targeted proposal of candidates that satisfy objectives under physical constraints.
- Innovation: Inverse materials design is shifting materials discovery from forward prediction to targeted proposal of candidates that satisfy objectives under physical constraints.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 6. Guided diffusion for the discovery of new superconductors

- Date: `2026-05-28`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02117-7
- Tags: dft, foundation_model, generative_model, high_throughput, md, ml, priority_journal
- Authors: Pawan Prakash, Jason B. Gibson, Z. Li, Gabriele Di Gianluca, Juan Carlos Contreras Esquivel
- Why it matters: We present a guided diffusion framework to accelerate the discovery of novel superconductors.
- Innovation: We present a guided diffusion framework to accelerate the discovery of novel superconductors.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 7. Stein Kernelized Molecular Dynamics for Active Learning of Interatomic Potentials

- Date: `2026-06-02`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2606.04100
- Tags: active_learning, equivariant_ml, h2, interatomic_potential, md, ml, physics_informed, transfer_learning
- Authors: Joanna Zou, Fraser Birks, Dallas Foster, Youssef Marzouk
- Why it matters: We introduce Stein kernelized molecular dynamics (SKMD), an enhanced sampling method that uses interacting particle dynamics to acquire informative training configurations for the active learning and fine-tuning of MLIPs.
- Innovation: We introduce Stein kernelized molecular dynamics (SKMD), an enhanced sampling method that uses interacting particle dynamics to acquire informative training configurations for the active learning and fine-tuning of MLIPs.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 8. Differentiable Particle-Mesh Ewald with Cartesian Tensor Message Passing for Learning Long-Range Electrostatics and Dipole Response

- Date: `2026-06-01`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.01598
- Tags: equivariant_ml, gnn, h2, interatomic_potential, md, ml, physics_informed, separation, uncertainty
- Authors: Zhiyue Guo, Junjie Wang (172690), Haoting Zhang, Zhixin Liang, Ziyang Yang
- Why it matters: Here we introduce a fully differentiable PME framework for learned charges and learned atomic dipoles within an E(n)-equivariant Cartesian tensor message passing network.
- Innovation: Here we introduce a fully differentiable PME framework for learned charges and learned atomic dipoles within an E(n)-equivariant Cartesian tensor message passing network.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 9. Non-covalent Interactions at cm$^{-1}$ Accuracy: Data Efficient Physics-Informed Distillation for Machine Learning Interatomic Potentials

- Date: `2026-06-03`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2606.05127
- Tags: foundation_model, h2, interatomic_potential, ml, physics_informed, transfer_learning
- Authors: Yulin Shen, Shahzad Akram, Louis Primeau, Gen Zu, Konstantinos D. Vogiatzis
- Why it matters: Here we show that knowledge distillation from a pretrained universal machine-learning interatomic potential (MLIP), followed by coupled-cluster fine-tuning with single and double excitations and perturbative triples [CCSD(T)], transfers not only low-cost labels but a physically meaningful prior on interaction length scales, anisotropy, and the repulsive-dispersive balance, which CCSD(T) data then sharpens to quantum-chemical accuracy.
- Innovation: Here we show that knowledge distillation from a pretrained universal machine-learning interatomic potential (MLIP), followed by coupled-cluster fine-tuning with single and double excitations and perturbative triples [CCSD(T)], transfers not only low-cost labels but a physically meaningful prior on interaction length scales, anisotropy, and the repulsive-dispersive balance, which CCSD(T) data then sharpens to quantum-chemical accuracy.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 10. A Systematic Survey and Benchmark of Deep Learning for Molecular Property Prediction in the Foundation Model Era

- Date: `2026-05-07`
- Journal: Journal of Chemical Theory and Computation
- Link: https://doi.org/10.1021/acs.jctc.5c02081
- Tags: foundation_model, h2, high_throughput, ml, multimodal, review, uncertainty
- Authors: Zongru Li, Xingsheng Chen, Honggang Wen, Regina Qianru ZHANG, M Li
- Why it matters: This survey traces four complementary paradigms, including Quantum, Descriptor Machine Learning, Geometric Deep Learning, and Foundation Models, and outlines a unified taxonomy linking molecular representations, model architectures, and interdisciplinary applications.
- Innovation: This survey traces four complementary paradigms, including Quantum, Descriptor Machine Learning, Geometric Deep Learning, and Foundation Models, and outlines a unified taxonomy linking molecular representations, model architectures, and interdisciplinary applications.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 11. Escaping the hydrolysis trap: a react agent for inverse design of durable photocatalytic covalent organic frameworks

- Date: `2026-06-03`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02168-w
- Tags: active_learning, catalysis, cof, foundation_model, generative_model, h2, photocatalysis, priority_journal
- Authors: Iman Peivaste, Nicolas D. Boscher, Ahmed Makradi, Salim Belouettar
- Why it matters: Here we introduce Ara , a large-language-model (LLM) agent that leverages pretrained chemical knowledge, donor-acceptor theory, conjugation effects, and linkage stability hierarchies, to guide the search for photocatalytic COFs satisfying joint band-gap, band-edge, and hydrolytic-stability criteria.
- Innovation: Here we introduce Ara , a large-language-model (LLM) agent that leverages pretrained chemical knowledge, donor-acceptor theory, conjugation effects, and linkage stability hierarchies, to guide the search for photocatalytic COFs satisfying joint band-gap, band-edge, and hydrolytic-stability criteria.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 12. Latent Diffusion Pretraining for Crystal Property Prediction

- Date: `2026-05-30`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.00776
- Tags: crystal, dft, generative_model, gnn, md, ml, self_supervised, separation, transfer_learning
- Authors: Shrimon Mukherjee, Kishalay Das, Partha Basuchowdhuri, Pawan Goyal, Niloy Ganguly
- Why it matters: In this work, we introduce a novel latent diffusion based pretraining framework, CrysLDNet, designed to mitigate data scarcity.
- Innovation: In this work, we introduce a novel latent diffusion based pretraining framework, CrysLDNet, designed to mitigate data scarcity.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 13. A multimodal large language model for materials science

- Date: `2026-04-24`
- Journal: Nature Machine Intelligence
- Link: https://doi.org/10.1038/s42256-026-01214-y
- Tags: foundation_model, interatomic_potential, ml, multimodal, priority_journal
- Authors: Yingheng Tang, Wenbin Xu, Jie Cao, Weilu Gao, Steven Farrell
- Why it matters: In this work, we introduce MatterChat, a versatile structure-aware multimodal LLM that unifies material structural data and textual inputs into a single cohesive model.
- Innovation: In this work, we introduce MatterChat, a versatile structure-aware multimodal LLM that unifies material structural data and textual inputs into a single cohesive model.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 14. AI-Driven Image Processing for Microstructure and Surface Characterization: A Systematic Review of Methods, Materials, and Applications

- Date: `2026-05-30`
- Journal: Archives of Computational Methods in Engineering
- Link: https://doi.org/10.1007/s11831-026-10641-4
- Tags: force_field, generative_model, h2, ml, physics_informed, review, transfer_learning
- Authors: Ali Erçetin, Ibrahim Arpaci, Samet Memiş, Amila Akagić, Özgür Özgün
- Why it matters: Artificial intelligence (AI) has rapidly become a key enabler in materials science, facilitating automated, high-precision analysis of microstructure and surface characteristics.
- Innovation: Artificial intelligence (AI) has rapidly become a key enabler in materials science, facilitating automated, high-precision analysis of microstructure and surface characteristics.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 15. A Padding Method for Enhanced Encoding of Inorganic Structures with Varying Chemical Compositions

- Date: `2026-05-29`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2605.30743
- Tags: crystal, generative_model, h2, interatomic_potential, ml, physics_informed
- Authors: Thang Dang, Haderbache Amir, Tzanakakis Alexandros, Yoshimoto Yuta
- Why it matters: To address this, we introduce a novel method that redefines the encoding and generation of inorganic materials by utilizing domain-specific symmetry-aware representation.
- Innovation: To address this, we introduce a novel method that redefines the encoding and generation of inorganic materials by utilizing domain-specific symmetry-aware representation.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 16. Active learning of collinear magnetic Moment Tensor Potentials using the spin-MLIP package from soft-constrained spin-polarized DFT calculations: a case study of Fe-Pd

- Date: `2026-05-26`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2605.26897
- Tags: active_learning, crystal, dft, h2, interatomic_potential, md, uncertainty
- Authors: Arseniy Burov, Alexey S. Kotykhov, Dmitry A. Aksyonov, Ivan S. Novikov, Vladimir V. Ladygin
- Why it matters: In this study, we present a workflow for active learning of magnetic Moment Tensor Potential (mMTP) during molecular dynamics (MD) simulations.
- Innovation: In this study, we present a workflow for active learning of magnetic Moment Tensor Potential (mMTP) during molecular dynamics (MD) simulations.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 17. Generative modelling of inorganic materials with explicit electronic structure

- Date: `2026-06-02`
- Journal: Nature Communications
- Link: https://doi.org/10.1038/s41467-026-73985-2
- Tags: battery, crystal, generative_model, h2, priority_journal, separation
- Authors: Junkil Park, J H Choi, Yousung Jung
- Why it matters: In this work, we present ChargeDIFF, a generative model for inorganic materials that explicitly incorporates electronic structure into the generation process.
- Innovation: In this work, we present ChargeDIFF, a generative model for inorganic materials that explicitly incorporates electronic structure into the generation process.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 18. PhaseTransfer: A transfer learning framework for efficient phase diagram mapping

- Date: `2026-05-26`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02154-2
- Tags: active_learning, h2, high_throughput, priority_journal, transfer_learning
- Authors: Eduardo González-García, Albert J. Markvoort, Nadia A. Erkamp, Tom F. A. de Greef
- Why it matters: Here we introduce PhaseTransfer, a transfer learning framework that leverages previously characterized phase diagrams to accelerate mapping of new systems.
- Innovation: Here we introduce PhaseTransfer, a transfer learning framework that leverages previously characterized phase diagrams to accelerate mapping of new systems.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 19. Reducing bias and enhancing equity in AI-enabled precision nutrition: addressing measurement error across wearables, multiomics, and dietary data

- Date: `2026-06-04`
- Journal: Frontiers in Digital Health
- Link: https://doi.org/10.3389/fdgth.2026.1805704
- Tags: h2, ml, multimodal, review, uncertainty
- Authors: Andi Mai, Yuanyuan Luan, See Ling Loy, Caihong Qin, Heyang Ji
- Why it matters: Artificial intelligence (AI) can offer individualized dietary guidance based on multimodal data collected from various sources, including wearable sensors, high-dimensional multiomics and biomarker analyses, behavioral tracking, and self-reported dietary intake, enabling the emergence of precision nutrition.
- Innovation: Artificial intelligence (AI) can offer individualized dietary guidance based on multimodal data collected from various sources, including wearable sensors, high-dimensional multiomics and biomarker analyses, behavioral tracking, and self-reported dietary intake, enabling the emergence of precision nutrition.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 20. Book of Abstracts: Past, Present and Future of Particle Technology Conference 2026

- Date: `2026-06-03`
- Journal: White Rose Research Online (University of Leeds, The University of Sheffield, University of York)
- Link: https://openalex.org/W7163721383
- Tags: equivariant_ml, gnn, h2, md, ml, physics_informed
- Authors: Unknown authors
- Why it matters: Ever since the EPSRC Specially-Promoted Programme on Particle Technology, coordinated by the late Leslie J.
- Innovation: Ever since the EPSRC Specially-Promoted Programme on Particle Technology, coordinated by the late Leslie J.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 21. Data Enrichment for Symbolic Regression Using Diffusion Models

- Date: `2026-05-31`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.00988
- Tags: generative_model, md, physics_informed, symbolic_regression
- Authors: Simon De Reuver, Tamas Kristof Toth, Teddy Lazebnik
- Why it matters: In this study, we introduce a physics-guided latent diffusion framework for DE for down the line SR models.
- Innovation: In this study, we introduce a physics-guided latent diffusion framework for DE for down the line SR models.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 22. World Models: A Comprehensive Survey of Architectures, Methodologies, Reasoning Paradigms, and Applications

- Date: `2026-05-28`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2606.00133
- Tags: high_throughput, md, ml, multimodal, physics_informed, review, uncertainty
- Authors: Arif Hassan Zidan, Yi Pan, Hanqi Jiang, Ruiyu Yan, Wei Ruan
- Why it matters: World models, internal simulators that learn the structure and dynamics of an environment, have emerged as a central paradigm in the pursuit of artificial general intelligence, enabling agents to predict, plan, and reason within learned representations.
- Innovation: World models, internal simulators that learn the structure and dynamics of an environment, have emerged as a central paradigm in the pursuit of artificial general intelligence, enabling agents to predict, plan, and reason within learned representations.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 23. CrystalCGAIN: efficient generation and inverse design of porous crystal structures with target properties

- Date: `2026-05-28`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02138-2
- Tags: crystal, dft, generative_model, priority_journal, separation, zeolite
- Authors: Ze Cai, Guanhua Qin, Shunbo Hu, Quan Qian
- Why it matters: The development of new materials is a key challenge in modern materials science.
- Innovation: The development of new materials is a key challenge in modern materials science.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 24. End-to-end multimodal structure elucidation from raw spectra combining contrastive learning and evolutionary algorithms

- Date: `2026-06-05`
- Journal: Nature Communications
- Link: https://doi.org/10.1038/s41467-026-73846-y
- Tags: h2, high_throughput, ml, multimodal, priority_journal, self_supervised
- Authors: A.H. Mirza, Luc Patiny, Kevin Maik Jablonka
- Why it matters: Here we present SECS, a framework that combines contrastive learning with evolutionary algorithms to automate structure elucidation directly from raw, multimodal spectroscopic data.
- Innovation: Here we present SECS, a framework that combines contrastive learning with evolutionary algorithms to automate structure elucidation directly from raw, multimodal spectroscopic data.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 25. Charting the thermodynamic stability of hybrid perovskite alloys with machine learning

- Date: `2026-05-28`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2605.30012
- Tags: alloy, dft, gnn, h2, interatomic_potential, ml, perovskite
- Authors: Jarno Laakso, Armi Tiihonen, Patrick Rinke
- Why it matters: We present a machine-learning (ML) accelerated atomistic modeling approach for the phase stability of (Cs/FA)Pb(Br/I)3 and (Cs/FA)Sn(Br/I)3 perovskites, with FA being formamidinium.
- Innovation: We present a machine-learning (ML) accelerated atomistic modeling approach for the phase stability of (Cs/FA)Pb(Br/I)3 and (Cs/FA)Sn(Br/I)3 perovskites, with FA being formamidinium.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 26. A review of deep learning-based surface defect detection for castings

- Date: `2026-06-06`
- Journal: World Journal of Advanced Research and Reviews
- Link: https://doi.org/10.30574/wjarr.2026.30.3.1608
- Tags: force_field, h2, ml, multimodal, review, self_supervised
- Authors: Xiaobin Liu, Yantong Gong
- Why it matters: As a core technology in the high-end equipment manufacturing industry, casting requires crucial surface defect detection of products for quality control.
- Innovation: As a core technology in the high-end equipment manufacturing industry, casting requires crucial surface defect detection of products for quality control.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 27. SLUSCHI-UP: A Web Infrastructure for SLUSCHI Melting-Temperature Calculations Using Universal Machine-Learning Interatomic Potentials

- Date: `2026-06-03`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2606.04973
- Tags: crystal, dft, equivariant_ml, h2, high_throughput, interatomic_potential, md
- Authors: Qi‐Jun Hong
- Why it matters: Melting temperature is a critical property for high-temperature materials design, but first-principles melting calculations based on finite-temperature molecular dynamics can require substantial computational resources.
- Innovation: Melting temperature is a critical property for high-temperature materials design, but first-principles melting calculations based on finite-temperature molecular dynamics can require substantial computational resources.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 28. MatFormBench: A Benchmarking Evaluation Framework for Target-Driven Materials Formulation

- Date: `2026-05-26`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2605.26741
- Tags: foundation_model, generative_model, h2, high_throughput, md, ml
- Authors: Linhan Wu, Chenxi Wang, Chuhan Yang, Zhengwei Yang, Yuyang Liu
- Why it matters: Inverse design of materials has significantly advanced target-driven formulation optimization, yet existing materials machine learning benchmarks remain limited to forward property prediction, failing to systematically evaluate inverse optimization and generation algorithms, a critical gap that hinders the progress of target-driven materials design.
- Innovation: Inverse design of materials has significantly advanced target-driven formulation optimization, yet existing materials machine learning benchmarks remain limited to forward property prediction, failing to systematically evaluate inverse optimization and generation algorithms, a critical gap that hinders the progress of target-driven materials design.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 29. Graph neural networks for full waveform inversion

- Date: `2026-06-04`
- Journal: Computational Mechanics
- Link: https://doi.org/10.1007/s00466-026-02796-5
- Tags: gnn, h2, ml, self_supervised, transfer_learning
- Authors: Divya Shyam Singh, Leon Herrmann, Tim Bürchner, Felix Dietrich, Stefan Kollmannsberger
- Why it matters: Furthermore, we demonstrate that the inversion of the 3D elastic wave equation can be significantly accelerated by inexpensive pre-training on scalar 2D datasets, resulting in faster convergence and improved reconstruction accuracy.
- Innovation: Furthermore, we demonstrate that the inversion of the 3D elastic wave equation can be significantly accelerated by inexpensive pre-training on scalar 2D datasets, resulting in faster convergence and improved reconstruction accuracy.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 30. Multi-Task Crack Foundation Model for Engineering-Reliable Crack Representation and Topology Preservation in Civil Infrastructure

- Date: `2026-06-04`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.05641
- Tags: foundation_model, transfer_learning, uncertainty
- Authors: Blessing Agyei Kyem, Joshua Kofi Asamoah, Eugene Denteh, Armstrong Aboah
- Why it matters: Reliable crack assessment requires not only accurate pixel-level masks but also connected crack geometry and confidence estimates that remain stable under domain shift.
- Innovation: Reliable crack assessment requires not only accurate pixel-level masks but also connected crack geometry and confidence estimates that remain stable under domain shift.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
