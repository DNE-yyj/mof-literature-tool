# Literature Update

- Generated: `2026-06-01T13:02:24`
- Profile: `materials_ml_transfer`
- Since: `2023-06-02`
- Papers retained: `30`

## Overview

Collected 30 deduplicated papers for profile `materials_ml_transfer`. This transfer profile keeps cross-material ML papers when they carry a concrete method signal; 30 retained papers are outside direct MOF literature. 30 papers contain transferable method tags and 13 appear in priority journals or major venue families. 17 papers also carry explicit material-system tags, helping judge whether the chemistry is close enough to MOFs.

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

### 1. Uncertainty-aware Machine Learning Interatomic Potentials via Learned Functional Perturbations

- Date: `2026-05-19`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2605.19939
- Tags: active_learning, dft, equivariant_ml, foundation_model, h2, high_throughput, interatomic_potential, ml, transfer_learning, uncertainty
- Authors: Olga Zaghen, Maksim Zhdanov, Dario Coscia, David R. Wessels, Erik J. Bekkers
- Why it matters: Machine Learning Interatomic Potentials (MLIPs) achieve near ab initio accuracy at a fraction of the cost of quantum-mechanical simulations, yet they remain prone to silent failures on out-of-distribution configurations, making principled uncertainty quantification (UQ) essential for error-aware simulations and active learning.
- Innovation: Machine Learning Interatomic Potentials (MLIPs) achieve near ab initio accuracy at a fraction of the cost of quantum-mechanical simulations, yet they remain prone to silent failures on out-of-distribution configurations, making principled uncertainty quantification (UQ) essential for error-aware simulations and active learning.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 2. From High-Throughput Screening to Generative Design: Artificial Intelligence-Driven Dielectric Materials Discovery

- Date: `2026-05-20`
- Journal: ACS Applied Materials & Interfaces
- Link: https://doi.org/10.1021/acsami.6c05353
- Tags: active_learning, crystal, foundation_model, generative_model, h2, high_throughput, md, ml, physics_informed, polymer, review, surrogate_model
- Authors: Jiayi Tang, Liang Cao, Guanghui Xu, Ming Li
- Why it matters: Traditional high-throughput screening is limited to existing chemical spaces and cannot resolve the inherent orthogonality between key dielectric metrics and multiphysics coupling conflicts.
- Innovation: Traditional high-throughput screening is limited to existing chemical spaces and cannot resolve the inherent orthogonality between key dielectric metrics and multiphysics coupling conflicts.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 3. Spatial statistics for screening molecular structures

- Date: `2026-05-16`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2605.17147
- Tags: active_learning, alloy, crystal, dft, equivariant_ml, generative_model, high_throughput, ml, physics_informed, review, surrogate_model
- Authors: Pranoy Ray, Surya R. Kalidindi
- Why it matters: The dominant paradigm in computational materials discovery relies on heavily parameterized deep architectures, including message-passing graph networks and equivariant models, that require millions of DFT-labeled training structures and produce non-convex latent representations that complicate continuous optimization for inverse design.
- Innovation: The dominant paradigm in computational materials discovery relies on heavily parameterized deep architectures, including message-passing graph networks and equivariant models, that require millions of DFT-labeled training structures and produce non-convex latent representations that complicate continuous optimization for inverse design.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 4. MEIDNet: multimodal generative AI framework for inverse materials design

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

### 5. A graph neural network for the era of large atomistic models

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

### 6. Direct Simulation of LiNi0.8Mn0.1Co0.1O2 Transport Properties Using an Efficient and Accurate Machine Learning Potential

- Date: `2026-05-19`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2605.19747
- Tags: active_learning, battery, dft, equivariant_ml, force_field, foundation_model, gnn, h2, interatomic_potential, md, ml, oxide, uncertainty
- Authors: Jian He, Constantijn H. J. A. van de Wetering, Rolande W. Nolsen, Nongnuch Artrith
- Why it matters: The rate capability of layered lithium nickel manganese cobalt oxide (NMC) cathode materials plays a decisive role in high-power applications such as fast charging, necessitating a detailed understanding of lithium-ion diffusion.
- Innovation: The rate capability of layered lithium nickel manganese cobalt oxide (NMC) cathode materials plays a decisive role in high-power applications such as fast charging, necessitating a detailed understanding of lithium-ion diffusion.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 7. Guided diffusion for the discovery of new superconductors

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

### 8. Training-free active learning framework in materials science with large language models

- Date: `2026-05-20`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02136-4
- Tags: active_learning, force_field, foundation_model, h2, high_throughput, ml, priority_journal, transfer_learning
- Authors: Hongchen Wang, Rafael Castañeda, Jay R. Werber, Yao Fehlis, Edward Kim
- Why it matters: Here, we introduce an LLM-based active learning framework (LLM-AL) that operates in an iterative few-shot setting and benchmark it against conventional ML models across four diverse materials science datasets.
- Innovation: Here, we introduce an LLM-based active learning framework (LLM-AL) that operates in an iterative few-shot setting and benchmark it against conventional ML models across four diverse materials science datasets.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 9. Symmetry-aware Bayesian flow networks for crystal generation

- Date: `2026-05-19`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02140-8
- Tags: crystal, generative_model, h2, ml, physics_informed, priority_journal
- Authors: Laura Ruple, Luca Torresi, Henrik Schopmans, Pascal Friederich
- Why it matters: In this work, we introduce SymmBFN, a novel symmetry-aware Bayesian Flow Network (BFN) for crystalline material generation that accurately reproduces the distribution of space groups found in experimentally observed crystals.
- Innovation: In this work, we introduce SymmBFN, a novel symmetry-aware Bayesian Flow Network (BFN) for crystalline material generation that accurately reproduces the distribution of space groups found in experimentally observed crystals.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 10. Neural network self-consistent fields for density functional theory

- Date: `2026-05-30`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02110-0
- Tags: dft, equivariant_ml, h2, ml, priority_journal, uncertainty
- Authors: Feitong Song, J N Feng
- Why it matters: Kohn-Sham density functional theory (KS-DFT) has found widespread application in accurate electronic structure calculations.
- Innovation: Kohn-Sham density functional theory (KS-DFT) has found widespread application in accurate electronic structure calculations.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 11. Efficient Parallelization of Message Passing Neural Network Potentials for Large-Scale Molecular Dynamics

- Date: `2026-05-25`
- Journal: JACS Au
- Link: https://doi.org/10.1021/jacsau.6c00210
- Tags: alloy, gnn, h2, interatomic_potential, md, ml, priority_journal, two_d_material
- Authors: Junfan Xia, Bin Jiang
- Why it matters: Moreover, we develop a universal potential trained on a comprehensive data set of C, H, O, and N, and leverage this parallel algorithm to perform efficient reactive MD simulations of graphene formation via acetylene–oxygen detonation, a central process in carbon nanomaterial synthesis.
- Innovation: Moreover, we develop a universal potential trained on a comprehensive data set of C, H, O, and N, and leverage this parallel algorithm to perform efficient reactive MD simulations of graphene formation via acetylene–oxygen detonation, a central process in carbon nanomaterial synthesis.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 12. Dataset-aware entropy-maximized active learning for machine-learned interatomic potentials

- Date: `2026-05-19`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2605.20384
- Tags: active_learning, dft, equivariant_ml, foundation_model, interatomic_potential, md
- Authors: Meiyan Wang, Rishi Rao, Li Zhu
- Why it matters: We present an active learning framework for efficiently generating training data for machine-learned interatomic potentials (MLIPs).
- Innovation: We present an active learning framework for efficiently generating training data for machine-learned interatomic potentials (MLIPs).
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 13. LEAP: A closed-loop framework for perovskite precursor additive discovery

- Date: `2026-05-18`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2605.20242
- Tags: active_learning, foundation_model, h2, high_throughput, perovskite, review, transfer_learning, uncertainty
- Authors: Xin-De Wang, Zhi-Rui Chen, Ze-Feng Gao, Peng-Jie Guo, Cheng Mu
- Why it matters: We develop LEAP(LLM-driven Exploration via Active Learning for Perovskites), an expert-in-the-loop closed framework that couples a domain-specialized large language model(LLM) with active learning for iterative additive prioritization.
- Innovation: We develop LEAP(LLM-driven Exploration via Active Learning for Perovskites), an expert-in-the-loop closed framework that couples a domain-specialized large language model(LLM) with active learning for iterative additive prioritization.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 14. A Systematic Survey and Benchmark of Deep Learning for Molecular Property Prediction in the Foundation Model Era

- Date: `2026-04-20`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15002208/v1
- Tags: foundation_model, h2, high_throughput, ml, multimodal, review, uncertainty
- Authors: Zongru Li, Xingsheng Chen, Honggang Wen, Regina Qianru ZHANG, Ming Li
- Why it matters: This survey traces four complementary paradigms, including Quantum, Descriptor Machine Learning, Geometric Deep Learning, and Foundation Models, and outlines a unified taxonomy linking molecular representations, model architectures, and interdisciplinary applications.
- Innovation: This survey traces four complementary paradigms, including Quantum, Descriptor Machine Learning, Geometric Deep Learning, and Foundation Models, and outlines a unified taxonomy linking molecular representations, model architectures, and interdisciplinary applications.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 15. A Systematic Survey and Benchmark of Deep Learning for Molecular Property Prediction in the Foundation Model Era

- Date: `2026-04-17`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2604.16586
- Tags: foundation_model, h2, high_throughput, ml, multimodal, review, uncertainty
- Authors: Zongru Li, Xingsheng Chen, Honggang Wen, Regina Qianru ZHANG, Ming Li
- Why it matters: This survey traces four complementary paradigms, including Quantum, Descriptor Machine Learning, Geometric Deep Learning, and Foundation Models, and outlines a unified taxonomy linking molecular representations, model architectures, and interdisciplinary applications.
- Innovation: This survey traces four complementary paradigms, including Quantum, Descriptor Machine Learning, Geometric Deep Learning, and Foundation Models, and outlines a unified taxonomy linking molecular representations, model architectures, and interdisciplinary applications.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 16. Attention-enhanced variational learning for physically informed discovery of exceptionally hard multicomponent bulk metallic glasses

- Date: `2026-05-12`
- Journal: Nature Communications
- Link: https://doi.org/10.1038/s41467-026-73008-0
- Tags: alloy, generative_model, h2, md, priority_journal, uncertainty
- Authors: Anurag Bajpai, Jaemin Wang, Barak Ratzker, Bilgehan M. Şeşen, Florian Kark
- Why it matters: We develop VIBANN, a variational information bottleneck-augmented attention-based neural network framework, for uncertainty-aware inverse design of exceptionally hard bulk multicomponent metallic glasses.
- Innovation: We develop VIBANN, a variational information bottleneck-augmented attention-based neural network framework, for uncertainty-aware inverse design of exceptionally hard bulk multicomponent metallic glasses.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 17. Design topological materials by reinforcement fine-tuned generative model

- Date: `2026-05-18`
- Journal: Nature Communications
- Link: https://doi.org/10.1038/s41467-026-73321-8
- Tags: crystal, generative_model, h2, high_throughput, priority_journal, transfer_learning, uncertainty
- Authors: Hu Xu, Dongheng Qian, Zhixuan Liu, Yadong Jiang, Jing Wang
- Why it matters: Topological insulators and topological crystalline insulators are characterized by robust surface states and insulating bulk behavior, rendering them highly valuable for quantum computing, spintronics, and other emerging technologies.
- Innovation: Topological insulators and topological crystalline insulators are characterized by robust surface states and insulating bulk behavior, rendering them highly valuable for quantum computing, spintronics, and other emerging technologies.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 18. A multimodal large language model for materials science

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

### 19. Active learning of collinear magnetic Moment Tensor Potentials using the spin-MLIP package from soft-constrained spin-polarized DFT calculations: a case study of Fe-Pd

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

### 20. Ab-initio Crystal Structure Determination from Powder X-Ray Diffraction

- Date: `2026-05-23`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2605.24594
- Tags: crystal, generative_model, ml, physics_informed, uncertainty
- Authors: Kaixiang Su, Osman Goni Ridwan, Hongfei Xue, Qiang Zhu
- Why it matters: In this work, we present a hybrid ab-initio approach that decomposes structure determination into a two-stage optimization problem: (1) discrete selection of space group symmetry, unit cell parameters, and Wyckoff site combinations; and (2) continuous optimization of atomic coordinates within the selected Wyckoff positions.
- Innovation: In this work, we present a hybrid ab-initio approach that decomposes structure determination into a two-stage optimization problem: (1) discrete selection of space group symmetry, unit cell parameters, and Wyckoff site combinations; and (2) continuous optimization of atomic coordinates within the selected Wyckoff positions.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 21. PhaseTransfer: A transfer learning framework for efficient phase diagram mapping

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

### 22. Accelerating point-defect simulations using data-driven and machine learning approaches

- Date: `2026-05-23`
- Journal: MRS Bulletin
- Link: https://doi.org/10.1557/s43577-026-01103-0
- Tags: dft, h2, high_throughput, interatomic_potential, ml, oxide, surrogate_model
- Authors: Arun Mannodi-Kanakkithodi, Menglin Huang, Prashun Gorai, Seán R. Kavanagh
- Why it matters: Data-driven and machine learning (ML) models trained on computational data can enable rapid defect property predictions and high-throughput screening.
- Innovation: Data-driven and machine learning (ML) models trained on computational data can enable rapid defect property predictions and high-throughput screening.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.

### 23. Artificial intelligence in additive Manufacturing: advances in smart materials, lattice optimization, and process intelligence

- Date: `2026-04-18`
- Journal: The International Journal of Advanced Manufacturing Technology
- Link: https://doi.org/10.1007/s00170-026-18072-y
- Tags: active_learning, h2, ml, physics_informed, review
- Authors: Saqlain Zaman, Md Shahjahan Mahmud, Ali Mollick, Tenzin Lhaden, Joshua Dantzler
- Why it matters: Artificial intelligence (AI) and additive manufacturing (AM) have propelled the next wave of technological innovation by integrating data-driven intelligence with design freedom, thereby enabling adaptive, efficient, and multifunctional systems.
- Innovation: Artificial intelligence (AI) and additive manufacturing (AM) have propelled the next wave of technological innovation by integrating data-driven intelligence with design freedom, thereby enabling adaptive, efficient, and multifunctional systems.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 24. Machine Learning Interatomic Potentials: Advancing Open-Source Software for Efficient and Scalable Molecular Simulation

- Date: `2026-05-21`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2605.22698
- Tags: dft, equivariant_ml, h2, interatomic_potential, ml, physics_informed
- Authors: Christoph Brunken, Titouan Cormier, Lucien Walewski, Marco Carobene, Yessine Khanfir
- Why it matters: We present mlip v2, a new generation of the mlip library that advances efficient and scalable molecular simulation through a unified and extensible framework.
- Innovation: We present mlip v2, a new generation of the mlip library that advances efficient and scalable molecular simulation through a unified and extensible framework.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 25. Accelerating point defect simulations using data-driven and machine learning approaches

- Date: `2026-04-22`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2604.21069
- Tags: dft, h2, high_throughput, interatomic_potential, ml, oxide, surrogate_model
- Authors: Arun Mannodi-Kanakkithodi, Menglin Huang, Prashun Gorai, Seán R. Kavanagh
- Why it matters: Data-driven and machine learning (ML) models trained on computational data can enable rapid defect property predictions and high-throughput screening.
- Innovation: Data-driven and machine learning (ML) models trained on computational data can enable rapid defect property predictions and high-throughput screening.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.

### 26. Benchmarking machine-learned interatomic potentials for molecular infrared spectroscopy

- Date: `2026-05-21`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2605.22367
- Tags: equivariant_ml, h2, high_throughput, interatomic_potential, md, ml, separation
- Authors: Nitik Bhatia, Ondřej Krejčí, Patrick Rinke
- Why it matters: Machine learning has transformed the field of atomistic simulations by enabling the development of interatomic potentials that are computationally efficient and highly accurate.
- Innovation: Machine learning has transformed the field of atomistic simulations by enabling the development of interatomic potentials that are computationally efficient and highly accurate.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 27. Research on the Application of Machine Learning in the R&D of Automotive Solid-State Electrolyte Materials

- Date: `2026-05-18`
- Journal: Theoretical and Natural Science
- Link: https://doi.org/10.54254/2753-8818/2026.dl33572
- Tags: battery, electrolyte, generative_model, gnn, h2, high_throughput, ml
- Authors: Weixuan Huang
- Why it matters: With the rapid development of the new energy vehicle industry, solid-state electrolytes, as key materials to improve the safety and energy density of lithium-ion batteries, have attracted extensive attention.
- Innovation: With the rapid development of the new energy vehicle industry, solid-state electrolytes, as key materials to improve the safety and energy density of lithium-ion batteries, have attracted extensive attention.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 28. CrystalCGAIN: efficient generation and inverse design of porous crystal structures with target properties

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

### 29. NN-xTB: density functional accuracy at semi empirical speed with neural network extended tight binding

- Date: `2026-05-20`
- Journal: Nature Communications
- Link: https://doi.org/10.1038/s41467-026-73184-z
- Tags: dft, h2, high_throughput, interatomic_potential, priority_journal
- Authors: Yufan Xia, Albert Thie, Joshua Soon, Giuseppe M. J. Barca
- Why it matters: Accurate prediction of molecular structure, energetics, and reactivity requires quantum chemistry methods that remain too costly for large-scale and high-throughput modeling.
- Innovation: Accurate prediction of molecular structure, energetics, and reactivity requires quantum chemistry methods that remain too costly for large-scale and high-throughput modeling.
- Likely limitations: Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.

### 30. Autonomous closed-loop framework for reproducible perovskite solar cells

- Date: `2026-04-21`
- Journal: Apollo (University of Cambridge)
- Link: https://www.repository.cam.ac.uk/handle/1810/401657
- Tags: active_learning, h2, high_throughput, ml, perovskite, symbolic_regression
- Authors: Dengpeng Gao, Shuaihua Lu, Chunlei Zhang, Ning Wang, Zexin Yutong
- Why it matters: Here, we introduce an autonomous closed-loop framework that integrates machine learning (ML)-driven material discovery with an automated manufacturing platform.
- Innovation: Here, we introduce an autonomous closed-loop framework that integrates machine learning (ML)-driven material discovery with an automated manufacturing platform.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
