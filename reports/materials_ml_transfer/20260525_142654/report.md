# Literature Update

- Generated: `2026-05-25T14:26:54`
- Profile: `materials_ml_transfer`
- Since: `2023-05-26`
- Papers retained: `30`

## Overview

Collected 30 deduplicated papers for profile `materials_ml_transfer`. This transfer profile keeps cross-material ML papers when they carry a concrete method signal; 30 retained papers are outside direct MOF literature. 30 papers contain transferable method tags and 8 appear in priority journals or major venue families. 15 papers also carry explicit material-system tags, helping judge whether the chemistry is close enough to MOFs.

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

### 4. Machine Learning and Deep Learning in Quantum Materials: Symmetry, Topology, and the Rise of Altermagnets

- Date: `2026-04-17`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2604.15985
- Tags: crystal, dft, equivariant_ml, force_field, gnn, h2, high_throughput, ml, physics_informed, review, symbolic_regression
- Authors: Mahyar Hassani-Vasmejani, Hosein Alavi-Rad, Meysam Bagheri Tagani
- Why it matters: The landscape of condensed matter physics is facing an unprecedented data surge driven by high-throughput ab initio workflows and rapidly expanding experimental datasets.
- Innovation: The landscape of condensed matter physics is facing an unprecedented data surge driven by high-throughput ab initio workflows and rapidly expanding experimental datasets.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 5. Fast and Accurate Prediction of Lattice Thermal Conductivity via Machine Learning Surrogates

- Date: `2026-05-12`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2605.11610
- Tags: crystal, dft, generative_model, h2, high_throughput, interatomic_potential, ml, surrogate_model, uncertainty
- Authors: Zeyu Wang, Shuya Yamazaki, Martin Hoffmann Petersen, Masato Ohnishi, Tomiya Yamamoto
- Why it matters: To address this challenge, we present a comprehensive benchmark of 15 surrogate models for predicting \k{appa}lat using the Phonix database, which contains 6,966 entries with anharmonic phonon properties derived from first-principles calculations.
- Innovation: To address this challenge, we present a comprehensive benchmark of 15 surrogate models for predicting \k{appa}lat using the Phonix database, which contains 6,966 entries with anharmonic phonon properties derived from first-principles calculations.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 6. Predicting temperature-dependent optoelectronic properties of semiconductor defects with equivariant neural networks

- Date: `2026-05-11`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02111-z
- Tags: active_learning, dft, equivariant_ml, gnn, h2, md, ml, priority_journal
- Authors: Xiangzhou Zhu, Patrick Rinke, David A. Egger
- Why it matters: Here, we present a neural network-based framework to investigate the electronic properties of defective semiconductors at finite temperatures efficiently.
- Innovation: Here, we present a neural network-based framework to investigate the electronic properties of defective semiconductors at finite temperatures efficiently.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 7. Direct Simulation of LiNi0.8Mn0.1Co0.1O2 Transport Properties Using an Efficient and Accurate Machine Learning Potential

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

### 8. Data-Efficient and Fast Machine Learning Molecular Dynamics through Integrated Active Learning and Knowledge Distillation

- Date: `2026-05-11`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15002964/v1
- Tags: active_learning, dft, equivariant_ml, foundation_model, h2, interatomic_potential, md, ml, water
- Authors: Xiliang LIAN, Alfredo Pasquarello, Xiliang LIAN
- Why it matters: We develop data-efficient machine learning interatomic potentials (MLIPs) for fast molecular dynamics simulations combining DeePMD and MACE models within an active learning and knowledge distillation framework.
- Innovation: We develop data-efficient machine learning interatomic potentials (MLIPs) for fast molecular dynamics simulations combining DeePMD and MACE models within an active learning and knowledge distillation framework.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 9. Training-free active learning framework in materials science with large language models

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

### 10. Symmetry-aware Bayesian flow networks for crystal generation

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

### 11. AI for quality management: A review

- Date: `2026-05-14`
- Journal: ENGINEERING Management
- Link: https://doi.org/10.1007/s42524-026-5394-x
- Tags: active_learning, ml, multimodal, review, surrogate_model
- Authors: Yangyang Huang, Yu Tan, Yuanyuan Li, Yongxiang Li, Kwok‐Leung Tsui
- Why it matters: Abstract Recent advances in artificial intelligence (AI) have significantly enhanced quality management, enabling more effective handling of complex, high-dimensional, and multi-modal data.
- Innovation: Abstract Recent advances in artificial intelligence (AI) have significantly enhanced quality management, enabling more effective handling of complex, high-dimensional, and multi-modal data.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

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

### 17. Compact SO(3) Equivariant Atomistic Foundation Models via Structural Pruning

- Date: `2026-05-09`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2605.08885
- Tags: equivariant_ml, foundation_model, gnn, h2, ml, self_supervised, transfer_learning
- Authors: Chen Wang, Siyu Hu, Guangming Tan, Weile Jia
- Why it matters: We demonstrate that the method generalizes to other SO(3) equivariant architectures (SevenNet, eSCN) and can be combined with quantization and knowledge distillation for further gains.
- Innovation: We demonstrate that the method generalizes to other SO(3) equivariant architectures (SevenNet, eSCN) and can be combined with quantization and knowledge distillation for further gains.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 18. Design topological materials by reinforcement fine-tuned generative model

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

### 19. A multimodal large language model for materials science

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

### 20. Ductile Mg-Te-Pb thermoelectric materials with ultralow lattice thermal conductivity predicted by a deep learning potential model

- Date: `2026-05-21`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02149-z
- Tags: crystal, equivariant_ml, h2, high_throughput, md, ml, priority_journal
- Authors: Xin-Xuan Wang, Zhen-Shuai Lei, Wenjuan Li, Xiao-Bin Feng, Chen, Gang, 1964-
- Why it matters: In this work, we introduce functional units into deep learning molecular dynamics-accelerated crystal structure prediction to develop novel functional materials exhibiting both outstanding thermoelectric and mechanical properties.
- Innovation: In this work, we introduce functional units into deep learning molecular dynamics-accelerated crystal structure prediction to develop novel functional materials exhibiting both outstanding thermoelectric and mechanical properties.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 21. Accelerating point defect simulations using data-driven and machine learning approaches

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

### 22. Research on the Application of Machine Learning in the R&D of Automotive Solid-State Electrolyte Materials

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

### 23. CrystalREPA: Transferring Physical Priors from Universal MLIPs to Crystal Generative Models

- Date: `2026-05-09`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2605.08960
- Tags: crystal, generative_model, h2, high_throughput, interatomic_potential, ml
- Authors: Chengqian Zhang, Yucheng Jin, Duo Zhang, Tiejun Li, Han Wang
- Why it matters: Crystal generative models mainly learn what stable crystals look like, with little explicit supervision for what makes them stable.
- Innovation: Crystal generative models mainly learn what stable crystals look like, with little explicit supervision for what makes them stable.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 24. Tangent-Plane Evidential Uncertainty in Active Learning for Magnetic Interatomic Potentials

- Date: `2026-05-12`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2605.12353
- Tags: active_learning, dft, h2, high_throughput, interatomic_potential, uncertainty
- Authors: Yang Cheng, Hongyu Yu, Hongjun Xiang
- Why it matters: Here we extend the $\mathrm{e}^2\mathrm{IP}$ evidential framework to magnetic machine-learning interatomic potentials by formulating the projected spin-force likelihood and the corresponding epistemic uncertainty in the tangent plane orthogonal to the local spin direction.
- Innovation: Here we extend the $\mathrm{e}^2\mathrm{IP}$ evidential framework to magnetic machine-learning interatomic potentials by formulating the projected spin-force likelihood and the corresponding epistemic uncertainty in the tangent plane orthogonal to the local spin direction.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 25. Regret Analysis of Guided Diffusion for Black-Box Optimization over Structured Inputs

- Date: `2026-05-11`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2605.10385
- Tags: crystal, generative_model, h2, md, ml, surrogate_model, uncertainty
- Authors: Masaki Adachi, Anita Yang, Yakun Wang, Song Liu
- Why it matters: We develop a first certificate-based expected simple-regret framework for guided-diffusion BO that avoids maximum-information-gain bounds, RKHS assumptions, and exact acquisition maximization.
- Innovation: We develop a first certificate-based expected simple-regret framework for guided-diffusion BO that avoids maximum-information-gain bounds, RKHS assumptions, and exact acquisition maximization.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 26. NN-xTB: density functional accuracy at semi empirical speed with neural network extended tight binding

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

### 27. Artificial intelligence in additive Manufacturing: advances in smart materials, lattice optimization, and process intelligence

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

### 28. Enhancing composition-based materials property prediction

- Date: `2026-05-20`
- Journal: Scientific Reports
- Link: https://doi.org/10.1038/s41598-026-53182-3
- Tags: crystal, foundation_model, gnn, h2, high_throughput, ml, multimodal, self_supervised
- Authors: И. А. Рубцов, Ivan Dudakov, Yuri Kuratov, Vadim Korolev
- Why it matters: Here we present a universal approach for enhancing composition-based materials property prediction by means of cross-modal knowledge transfer.
- Innovation: Here we present a universal approach for enhancing composition-based materials property prediction by means of cross-modal knowledge transfer.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 29. CatalyticMLLM: A Graph-Text Multimodal Large Language Model for Catalytic Materials

- Date: `2026-05-17`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2605.17254
- Tags: active_learning, foundation_model, generative_model, h2, high_throughput, multimodal
- Authors: Yanjie Li, Jian Xu, Xu-Yao Zhang, Shiming Xiang, Nian Ran
- Why it matters: Property prediction and inverse structural design of catalytic materials are typically modeled as two independent tasks: the former predicts target properties from given structures, whereas the latter generates candidate structures according to desired properties.
- Innovation: Property prediction and inverse structural design of catalytic materials are typically modeled as two independent tasks: the former predicts target properties from given structures, whereas the latter generates candidate structures according to desired properties.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 30. TriForces: Augmenting Atomistic GNNs for Transferable Representations

- Date: `2026-05-20`
- Journal: ArXiv.org
- Link: https://arxiv.org/abs/2605.20581
- Tags: dft, interatomic_potential, ml, self_supervised
- Authors: Ali Ramlaoui, Alexandre Duval, Hannah Bull, Victor Schmidt, Hugues Talbot
- Why it matters: To address this, we present TriForces, a model-agnostic three-stream framework that separates composition and structure information, combined with self-supervised learning to preserve transferable representations.
- Innovation: To address this, we present TriForces, a model-agnostic three-stream framework that separates composition and structure information, combined with self-supervised learning to preserve transferable representations.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
