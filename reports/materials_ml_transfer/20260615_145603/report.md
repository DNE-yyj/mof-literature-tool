# Literature Update

- Generated: `2026-06-15T14:56:03`
- Profile: `materials_ml_transfer`
- Since: `2023-06-16`
- Papers retained: `30`

## Overview

Collected 30 deduplicated papers for profile `materials_ml_transfer`. This transfer profile keeps cross-material ML papers when they carry a concrete method signal; 30 retained papers are outside direct MOF literature. 30 papers contain transferable method tags and 7 appear in priority journals or major venue families. 16 papers also carry explicit material-system tags, helping judge whether the chemistry is close enough to MOFs.

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

### 2. Towards Automated Discovery: A Review of Generative Models, Multimodal Learning and Closed-Loop Workflows in Inverse Materials Design

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

### 3. Towards Automated Discovery: A Review of Generative Models, Multimodal Learning and Closed-Loop Workflows in Inverse Materials Design

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

### 4. Stein Kernelized Molecular Dynamics for Active Learning of Interatomic Potentials

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

### 5. Differentiable Particle-Mesh Ewald with Cartesian Tensor Message Passing for Learning Long-Range Electrostatics and Dipole Response

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

### 6. DSpinGNN: A Physics-Informed Equivariant Graph Neural Network for Dynamic Magnetic Exchange Prediction in Strain-Deformed Monolayer CrI$_3$

- Date: `2026-06-10`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2606.11685
- Tags: crystal, dft, equivariant_ml, gnn, h2, md, ml, physics_informed, uncertainty
- Authors: Isam A. Balghari, M. Faryad, M. Sabieh Anwar
- Why it matters: Here we introduce DSpinGNN, a bifurcated machine-learning architecture comprising an $E(3)$-equivariant graph neural network (E-GNN) for classical Langevin structural dynamics and a physics-informed $Δ$-MLP that maps instantaneous local Cr-I-Cr bond geometry to isotropic exchange couplings, with the Goodenough-Kanamori superexchange relationship embedded as an analytical inductive bias.
- Innovation: Here we introduce DSpinGNN, a bifurcated machine-learning architecture comprising an $E(3)$-equivariant graph neural network (E-GNN) for classical Langevin structural dynamics and a physics-informed $Δ$-MLP that maps instantaneous local Cr-I-Cr bond geometry to isotropic exchange couplings, with the Goodenough-Kanamori superexchange relationship embedded as an analytical inductive bias.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 7. Inverse Design of Amorphous Materials With Targeted Properties

- Date: `2026-06-09`
- Journal: Advanced Materials
- Link: https://doi.org/10.1002/adma.202522493
- Tags: catalysis, crystal, generative_model, h2, md, ml, priority_journal
- Authors: Jonas A. Finkler, Yan Lin, Tao Du, Jilin Hu, Morten M. Smedskjær
- Why it matters: First, we demonstrate the inherent challenges for diffusion models to generate relaxed structures.
- Innovation: First, we demonstrate the inherent challenges for diffusion models to generate relaxed structures.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 8. Physics-informed generative AI for semiconductor manufacturing: Enforcing hard physical constraints in generative models by construction

- Date: `2026-06-08`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2606.11247
- Tags: foundation_model, generative_model, h2, high_throughput, md, multimodal, physics_informed, review
- Authors: Yaser Mike Banad, Sarah Sharif
- Why it matters: Generative models are increasingly used to propose designs, data, and control actions for physical systems, yet many such systems are governed by hard physical constraints rather than by perceptual plausibility.
- Innovation: Generative models are increasingly used to propose designs, data, and control actions for physical systems, yet many such systems are governed by hard physical constraints rather than by perceptual plausibility.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 9. Inverse design of bespoke interatomic potentials via active learning by information-matching

- Date: `2026-06-06`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.08148
- Tags: active_learning, dft, generative_model, h2, interatomic_potential, uncertainty
- Authors: Yonatan Kurniawan, Logan Williams, Amit Samanta, Ilia Nikiforov, Daniel Schwalbe-Koda
- Why it matters: Interatomic potentials (IPs) enable large-scale atomistic simulations beyond the reach of first-principles methods, but their predictive reliability depends critically on the selection of training data, quantified uncertainty, and model expressiveness.
- Innovation: Interatomic potentials (IPs) enable large-scale atomistic simulations beyond the reach of first-principles methods, but their predictive reliability depends critically on the selection of training data, quantified uncertainty, and model expressiveness.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 10. Non-covalent Interactions at cm$^{-1}$ Accuracy: Data Efficient Physics-Informed Distillation for Machine Learning Interatomic Potentials

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

### 11. Phase prediction in high-entropy alloys through uncertainty sampling and symbolic classification-based parameter discovery

- Date: `2026-06-11`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02189-5
- Tags: active_learning, alloy, h2, ml, priority_journal, uncertainty
- Authors: Y Zhang, Shujian Ding, Shuangxiong Ma, J W Zhang, Weili Wang
- Why it matters: Data imbalance represents critical challenges for data-driven approaches in materials data modeling.
- Innovation: Data imbalance represents critical challenges for data-driven approaches in materials data modeling.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 12. Inverse Design of Novel Antiferromagnets Through Symmetry-aware Generation

- Date: `2026-06-10`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02169-9
- Tags: crystal, generative_model, h2, high_throughput, physics_informed, priority_journal
- Authors: Feiyang Huang, Zhengming Zhang, Jianhu Gong, Dunhui Wang, Baomin Wang
- Why it matters: Here we present a symmetry-informed generative framework that explicitly encodes crystal symmetry into the structural representation, enabling targeted exploration of high-symmetry crystals in which antiferromagnetic states are favored.
- Innovation: Here we present a symmetry-informed generative framework that explicitly encodes crystal symmetry into the structural representation, enabling targeted exploration of high-symmetry crystals in which antiferromagnetic states are favored.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 13. A Systematic Survey and Benchmark of Deep Learning for Molecular Property Prediction in the Foundation Model Era

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

### 14. Distilling first-principles accuracy into compact machine learning potentials for condensed-phase chemistry

- Date: `2026-06-05`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.06848
- Tags: catalysis, dft, foundation_model, h2, interatomic_potential, md, ml, transfer_learning, water
- Authors: Sijia Chen, Niamh O'Neill, Benjamin X. Shi, Venkat Kapil
- Why it matters: We demonstrate this across three problems of increasing sampling complexity: finite-temperature NPT simulations of ice Ih, classical and path-integral simulations of liquid water over 240-370 K, and path-integral umbrella-sampling simulations of water dissociation at the anatase TiO2(101)/water interface.
- Innovation: We demonstrate this across three problems of increasing sampling complexity: finite-temperature NPT simulations of ice Ih, classical and path-integral simulations of liquid water over 240-370 K, and path-integral umbrella-sampling simulations of water dissociation at the anatase TiO2(101)/water interface.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 15. Escaping the hydrolysis trap: a react agent for inverse design of durable photocatalytic covalent organic frameworks

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

### 16. Latent Diffusion Pretraining for Crystal Property Prediction

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

### 17. MatMind: A Structure-Activity Knowledge-Driven Generative Foundation Model for Materials Science

- Date: `2026-06-05`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.07712
- Tags: crystal, foundation_model, gnn, h2, md, ml, physics_informed
- Authors: Zhan'ao Yao, Boxuan Zhang, 恕 井原, Xiaoyu Wu, Rongyan Wang
- Why it matters: Here we present MatMind, a generative foundation model purpose-built for crystal materials science under this paradigm, developed through the coordinated activation of structure-activity knowledge and physics-informed feedback within a progressive training framework -- combining structure-activity knowledge injection, a dual-head architecture that jointly trains language reasoning and numerical regression in a shared representation space, and multi-objective physics-informed reinforcement learning over stability, novelty, and structural diversity.
- Innovation: Here we present MatMind, a generative foundation model purpose-built for crystal materials science under this paradigm, developed through the coordinated activation of structure-activity knowledge and physics-informed feedback within a progressive training framework -- combining structure-activity knowledge injection, a dual-head architecture that jointly trains language reasoning and numerical regression in a shared representation space, and multi-objective physics-informed reinforcement learning over stability, novelty, and structural diversity.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 18. AI-Driven Image Processing for Microstructure and Surface Characterization: A Systematic Review of Methods, Materials, and Applications

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

### 19. Generative modelling of inorganic materials with explicit electronic structure

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

### 20. An electron-density point-cloud framework for robust protein-ligand interaction prediction

- Date: `2026-06-11`
- Journal: Nature Communications
- Link: https://doi.org/10.1038/s41467-026-74196-5
- Tags: gnn, h2, high_throughput, ml, priority_journal, separation, uncertainty
- Authors: Liu Y, Yutong Wang, Qingquan Wang, Meitang Peng, Yuan Chen
- Why it matters: We introduce E-CloudBind, a framework that fuses electron-density point clouds with intrinsic molecular graphs to model non-covalent and covalent interactions without relying on sub-ångström accuracy.
- Innovation: We introduce E-CloudBind, a framework that fuses electron-density point clouds with intrinsic molecular graphs to model non-covalent and covalent interactions without relying on sub-ångström accuracy.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 21. An active learning workflow for predicting misfit volume in body-centered cubic refractory high-entropy alloys

- Date: `2026-06-10`
- Journal: Scientific Reports
- Link: https://doi.org/10.1038/s41598-026-57006-2
- Tags: active_learning, alloy, dft, ml, separation, symbolic_regression, uncertainty
- Authors: Shunshun Liu, Prasanna V. Balachandran
- Why it matters: However, a mechanistic understanding of their yield strength requires accurate determination of the misfit volume descriptor (δ), which quantifies the local volume change due to the size and electronic heterogeneity of constituent elements in the solid solution.
- Innovation: However, a mechanistic understanding of their yield strength requires accurate determination of the misfit volume descriptor (δ), which quantifies the local volume change due to the size and electronic heterogeneity of constituent elements in the solid solution.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 22. Deep learning assisted modeling of Li-ion transport in SEI: a graph neural network based study

- Date: `2026-06-08`
- Journal: Frontiers in Batteries and Electrochemistry
- Link: https://doi.org/10.3389/fbael.2026.1849012
- Tags: battery, dft, electrolyte, generative_model, gnn, h2, md, ml, physics_informed
- Authors: Arjun S. Kulathuvayal, Yanqing Su
- Why it matters: In this work, we develop a deep-learning-assisted framework to model Li-ion transport across the inorganic SEI by combining density functional theory (nudged elastic band) calculations with graph neural network learning.
- Innovation: In this work, we develop a deep-learning-assisted framework to model Li-ion transport across the inorganic SEI by combining density functional theory (nudged elastic band) calculations with graph neural network learning.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 23. Transferable Machine Learning of Electronic Hamiltonians with Superposition-of-Atomic-Potentials Features

- Date: `2026-06-10`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2606.12326
- Tags: gnn, h2, high_throughput, ml, physics_informed, separation
- Authors: Chaoqun Zhang, Christian Venturella, Enzhi Chen, Tianyu Zhu
- Why it matters: We introduce a Hamiltonian learning framework built on electronic features derived from the superposition-of-atomic-potentials (SAP) approximation, an efficient self-consistent-field initial guess that captures essential electron-electron screening.
- Innovation: We introduce a Hamiltonian learning framework built on electronic features derived from the superposition-of-atomic-potentials (SAP) approximation, an efficient self-consistent-field initial guess that captures essential electron-electron screening.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 24. Book of Abstracts: Past, Present and Future of Particle Technology Conference 2026

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

### 25. Score-based diffusion models for accurate crystal-structure inpainting and reconstruction of hydrogen positions

- Date: `2026-06-11`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02090-1
- Tags: crystal, dft, generative_model, h2, high_throughput, md, priority_journal
- Authors: Timo Reents, Arianna Cantarella, Marnik Bercx, Pietro Bonfà, Giovanni Pizzi
- Why it matters: We present how this knowledge transfer across domains enables a much faster and more accurate completion of host structures, compared to unconditioned diffusion models or previous approaches solely based on density-functional theory (DFT).
- Innovation: We present how this knowledge transfer across domains enables a much faster and more accurate completion of host structures, compared to unconditioned diffusion models or previous approaches solely based on density-functional theory (DFT).
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 26. Data Enrichment for Symbolic Regression Using Diffusion Models

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

### 28. Harnessing Artificial Intelligence (AI) for a greener future: a review of AI advancements in green chemistry, chemical processes and sustainable materials

- Date: `2026-06-01`
- Journal: Applied Intelligence
- Link: https://doi.org/10.1007/s10489-026-07326-7
- Tags: active_learning, catalysis, equivariant_ml, h2, ml, polymer, review, separation
- Authors: Ahmed M. Elkhatat, Shaheen A. Al‐Muhtaseb
- Why it matters: The rise of artificial intelligence (AI), particularly machine learning (ML), is fundamentally reshaping how we pursue green chemistry and sustainable chemical processes.
- Innovation: The rise of artificial intelligence (AI), particularly machine learning (ML), is fundamentally reshaping how we pursue green chemistry and sustainable chemical processes.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 29. GFFMERGE: Efficient Merging of Graph Neural Force Fields and Beyond

- Date: `2026-06-02`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.03232
- Tags: force_field, foundation_model, gnn, high_throughput, ml, transfer_learning
- Authors: Parth Verma, Parv P. Singh, Vipul Garg, Ishita Thakre, N. M. Anoop Krishnan
- Why it matters: Inspired by model merging in vision and language processing, we introduce GFFMERGE, the first principled framework for closed-form model merging in GNNs.
- Innovation: Inspired by model merging in vision and language processing, we introduce GFFMERGE, the first principled framework for closed-form model merging in GNNs.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 30. DPA4: Pushing the Accuracy-Cost Frontier of Interatomic Potentials with EMFA SO(2) Convolution

- Date: `2026-06-01`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2606.02419
- Tags: equivariant_ml, h2, high_throughput, interatomic_potential, self_supervised
- Authors: Tiancheng Li, Wentao Li, Anyang Peng, Jianming Xue, Linfeng ZHANG
- Why it matters: We introduce DPA4, an SE(3)-equivariant interatomic-potential architecture with an EMFA (Edge-conditioned, Multi-Focus, Attention) SO(2)-equivariant convolution that combines a low-rank edge-node SO(2)-equivariant product, a multi-focus design for message nonlinearity, and envelope-gated attention for message aggregation.
- Innovation: We introduce DPA4, an SE(3)-equivariant interatomic-potential architecture with an EMFA (Edge-conditioned, Multi-Focus, Attention) SO(2)-equivariant convolution that combines a low-rank edge-node SO(2)-equivariant product, a multi-focus design for message nonlinearity, and envelope-gated attention for message aggregation.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
