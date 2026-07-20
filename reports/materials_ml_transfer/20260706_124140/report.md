# Literature Update

- Generated: `2026-07-06T12:41:40`
- Profile: `materials_ml_transfer`
- Since: `2023-07-07`
- Papers retained: `30`

## Overview

Collected 30 deduplicated papers for profile `materials_ml_transfer`. This transfer profile keeps cross-material ML papers when they carry a concrete method signal; 29 retained papers are outside direct MOF literature. 30 papers contain transferable method tags and 4 appear in priority journals or major venue families. 13 papers also carry explicit material-system tags, helping judge whether the chemistry is close enough to MOFs.

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

### 1. Machine-Learning-Driven Molecular Design and Structure–Property–Performance Relationships in Pharmaceutical Chemistry

- Date: `2026-06-19`
- Journal: Molecules
- Link: https://doi.org/10.3390/molecules31122162
- Tags: active_learning, catalysis, equivariant_ml, foundation_model, high_throughput, md, ml, multimodal, review, uncertainty
- Authors: Aisulu Zh. Kabdraisova, A. K. Umbetova, Gulfairuz Zh. Kairalapova, Yu. A. Litvinenko, L.R. Sassykova
- Why it matters: This review examines the emerging role of machine learning (ML) in pharmaceutical chemistry, with emphasis on molecular design, synthetic feasibility, and structure-property-performance (SPP) relationships.
- Innovation: This review examines the emerging role of machine learning (ML) in pharmaceutical chemistry, with emphasis on molecular design, synthetic feasibility, and structure-property-performance (SPP) relationships.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 2. Artificial Intelligence in Gas Hydrate Management: A Comprehensive Review

- Date: `2026-07-01`
- Journal: Petroleum Research
- Link: https://doi.org/10.1016/j.ptlrs.2026.06.002
- Tags: force_field, h2, high_throughput, md, ml, physics_informed, review, self_supervised, uncertainty
- Authors: Mehdi Razavifar, Zahra Amiri, Mohammad Jahed, Shanker Krishna, Ehsan Nikooee
- Why it matters: Gas hydrate applications range from energy extraction, carbon mitigation (CO 2 hydrates), hydrogen (H 2 ) storage, flow assurance to geohazards, but the thermodynamics, kinetics, and geology of gas hydrate systems are complex and lack sufficient experimental data.
- Innovation: Gas hydrate applications range from energy extraction, carbon mitigation (CO 2 hydrates), hydrogen (H 2 ) storage, flow assurance to geohazards, but the thermodynamics, kinetics, and geology of gas hydrate systems are complex and lack sufficient experimental data.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 3. The FAST Framework: Developing a Data-Efficient Machine Learning Potential to Decode Superionic Transition-Induced Thermophysical and Kinetic Anomalies in UO2 under Extreme Conditions

- Date: `2026-06-19`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.21796
- Tags: active_learning, dft, foundation_model, h2, interatomic_potential, md, ml, oxide, separation, transfer_learning
- Authors: Fengnian Zhuang, Gaosheng Yan, Hong Chen, Yi Zhang, Wenshan Yu
- Why it matters: To address this, we develop a versatile machine learning interatomic potential (MLIP) for $UO_2$ by proposing an efficient training strategy, termed the "FAST" (Fine-tuning via Active-learning and Superionic-Targeting) framework.
- Innovation: To address this, we develop a versatile machine learning interatomic potential (MLIP) for $UO_2$ by proposing an efficient training strategy, termed the "FAST" (Fine-tuning via Active-learning and Superionic-Targeting) framework.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 4. Breaking Bottlenecks in Solid Electrolyte Discovery with Large Artificial Intelligence Models

- Date: `2026-06-23`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.24480
- Tags: active_learning, battery, catalysis, dft, electrolyte, foundation_model, h2, high_throughput, interatomic_potential, ml, multimodal, uncertainty
- Authors: Eric Jianfeng Cheng, Min Hong, Zhiquan Zeng, Chuanyu Liu, Qian Wang
- Why it matters: Solid electrolytes (SEs) are central to next-generation metal batteries, yet their discovery remains constrained by fragmented data, limited transferability of simulations, and slow experimental iteration.
- Innovation: Solid electrolytes (SEs) are central to next-generation metal batteries, yet their discovery remains constrained by fragmented data, limited transferability of simulations, and slow experimental iteration.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 5. Adaptive fine-tuning of foundation models for crystal structure prediction: Discovery of high-pressure phases in the CaFeNi system

- Date: `2026-06-29`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.30870
- Tags: crystal, dft, foundation_model, h2, interatomic_potential, ml, transfer_learning
- Authors: N. M. Chtchelkatchev, M.V. Magnitskaya, R. E. Ryltsev
- Why it matters: Here we introduce a self-consistent, foundation-model-assisted CSP workflow that combines evolutionary search with adaptive data selection and fine-tuning.
- Innovation: Here we introduce a self-consistent, foundation-model-assisted CSP workflow that combines evolutionary search with adaptive data selection and fine-tuning.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 6. Phase prediction in high-entropy alloys through uncertainty sampling and symbolic classification-based parameter discovery

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

### 7. CoTAR: Topology and Atomic State Reconstruction in Condensed Phases

- Date: `2026-06-26`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.27636
- Tags: dft, force_field, gnn, h2, interatomic_potential, md, ml, transfer_learning
- Authors: Hodaka Mori, Yu Miyazaki, Takechika Kikkawa
- Why it matters: Here, we present CoTAR, a hybrid graph neural network (GNN)--hidden Markov model (HMM) framework that reconstructs molecular topology, formal charges, and unpaired electrons from atomic species, coordinates, and total charge by combining message passing on a proximity graph with a van der Waals prior, chemical constraints, and temporal smoothing.
- Innovation: Here, we present CoTAR, a hybrid graph neural network (GNN)--hidden Markov model (HMM) framework that reconstructs molecular topology, formal charges, and unpaired electrons from atomic species, coordinates, and total charge by combining message passing on a proximity graph with a van der Waals prior, chemical constraints, and temporal smoothing.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 8. Equivariant Graph Neural Networks Improve Optical Spectra Prediction for Materials Screening

- Date: `2026-06-17`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.19133
- Tags: equivariant_ml, gnn, high_throughput, ml, surrogate_model
- Authors: Kasper Helverskov Petersen, François R J Cornet, Martin Ovesen, Mikkel Jordahn, Kristian S. Thygesen
- Why it matters: Scalable prediction of optical spectra is a critical component of high-throughput materials screening for optoelectronic applications such as solar cells.
- Innovation: Scalable prediction of optical spectra is a critical component of high-throughput materials screening for optoelectronic applications such as solar cells.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 9. Chemical intuition on bond-dissociation energies as an emergent ability of universal machine-learning interatomic potentials

- Date: `2026-07-02`
- Journal: Nature Communications
- Link: https://doi.org/10.1038/s41467-026-74919-8
- Tags: equivariant_ml, h2, interatomic_potential, priority_journal
- Authors: Shinnosuke Hattori, Kohei Shimamura, Ken‐ichi Nomura, Aiichiro Nakano, Nitish Baradwaj
- Why it matters: Here we show that an E(3)-equivariant machine-learning interatomic potential learns local bond information without direct supervision of bond properties.
- Innovation: Here we show that an E(3)-equivariant machine-learning interatomic potential learns local bond information without direct supervision of bond properties.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 10. Active Learning for Generalizable Detonation Performance Prediction of Energetic Materials

- Date: `2026-06-30`
- Journal: Chemistry of Materials
- Link: https://doi.org/10.1021/acs.chemmater.6c01049
- Tags: active_learning, dft, h2, high_throughput, ml, surrogate_model
- Authors: R. Seaton Ullberg, Megan C. Davis, Jeremy N. Schroeder, Andrew Salij, M. J. Cawkwell
- Why it matters: The resulting high-throughput workflow iteratively expands the training data set by selecting new molecules in a targeted manner that balances the exploration of broad chemical space with the exploitation of promising high-performing candidates.
- Innovation: The resulting high-throughput workflow iteratively expands the training data set by selecting new molecules in a targeted manner that balances the exploration of broad chemical space with the exploitation of promising high-performing candidates.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 11. An active learning workflow for predicting misfit volume in body-centered cubic refractory high-entropy alloys

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

### 12. Artificial intelligence-empowered biochar engineering: From design fundamentals to commercialization

- Date: `2026-06-30`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15005458/v1
- Tags: active_learning, adsorption, catalysis, foundation_model, ml, review
- Authors: L Chen, Xiangzhou Yuan, Lei Feng, Huiyan Zhang, Hirotomo Nishihara
- Why it matters: Engineered biochar is a promising carbon material for sustainable energy and environmental applications, yet its transition from laboratory-scale synthesis to commercial deployment remains constrained.
- Innovation: Engineered biochar is a promising carbon material for sustainable energy and environmental applications, yet its transition from laboratory-scale synthesis to commercial deployment remains constrained.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 13. ElemeNet: Multiscale Molecular Machine Learning with Uncertainty Quantification Across the Periodic Table

- Date: `2026-06-29`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.30961
- Tags: equivariant_ml, h2, high_throughput, ml, uncertainty
- Authors: Jacob Toney, Samir Darouich, Yiran Wang, Aaron Garrison, Johannes Kästner
- Why it matters: As well as more common atom-, bond-, and molecule-level predictions, we introduce moiety predictions.
- Innovation: As well as more common atom-, bond-, and molecule-level predictions, we introduce moiety predictions.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 14. Trustworthy Explainable AI for Asphalt Pavement Engineering: A Systematic Scoping Review of Materials, Performance, and Decision Support

- Date: `2026-06-25`
- Journal: Applied System Innovation
- Link: https://doi.org/10.3390/asi9070133
- Tags: high_throughput, ml, review, surrogate_model, uncertainty
- Authors: Yazeed S. Jweihan
- Why it matters: Machine learning has become a field of growing interest in asphalt pavement engineering, spanning mix design, material characterization, performance prediction, distress detection, sustainability, quality control, and maintenance planning.
- Innovation: Machine learning has become a field of growing interest in asphalt pavement engineering, spanning mix design, material characterization, performance prediction, distress detection, sustainability, quality control, and maintenance planning.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 15. Self-Supervised Calibration of Scientific Instruments Using Physical Consistency Constraints

- Date: `2026-06-28`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.29466
- Tags: h2, ml, physics_informed, self_supervised, uncertainty
- Authors: M. Rejmund, A. Lemasson
- Why it matters: We introduce a physics-informed self-supervised framework that jointly learns latent detector calibration parameters and task-specific predictions directly from raw measurements without requiring pre-calibrated signals or external labels.
- Innovation: We introduce a physics-informed self-supervised framework that jointly learns latent detector calibration parameters and task-specific predictions directly from raw measurements without requiring pre-calibrated signals or external labels.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 16. Guided Adaptive Diffusion: An Evolutionary Framework for Multimodal Atomistic Structure Prediction

- Date: `2026-06-25`
- Journal: Journal of Chemical Information and Modeling
- Link: https://doi.org/10.1021/acs.jcim.6c00843
- Tags: generative_model, high_throughput, interatomic_potential, md, multimodal, physics_informed
- Authors: Alexander Adel, Jakub Szmitek, Benedikt Hartl, Ralf Wanzenböck, Georg K. H. Madsen
- Why it matters: In this work, we introduce an adaptive diffusion framework that reinterprets the neural-network-based denoising process as an evolutionary search mechanism for structure optimization.
- Innovation: In this work, we introduce an adaptive diffusion framework that reinterprets the neural-network-based denoising process as an evolutionary search mechanism for structure optimization.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 17. Data Enrichment for Symbolic Regression Using Diffusion Models

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

### 18. A Combined Tight Binding with Machine Learning Potential Model for Magnesium Compounds

- Date: `2026-06-24`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.25853
- Tags: adsorption, co2, dft, equivariant_ml, h2, interatomic_potential, md, ml, water
- Authors: Jiwen Yu, Arash A. Mostofi, Andrew Horsfield
- Why it matters: We present a model for magnesium-based systems that combines density functional tight binding (DFTB) with MACE, a machine learning interatomic potential (DFTB+MACE).
- Innovation: We present a model for magnesium-based systems that combines density functional tight binding (DFTB) with MACE, a machine learning interatomic potential (DFTB+MACE).
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 19. Fourier-KAGAT: resolving activity cliffs in organic photocatalysts via Fourier-based learnable activations

- Date: `2026-06-20`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02194-8
- Tags: catalysis, dft, gnn, h2, ml, photocatalysis, priority_journal, separation
- Authors: Iman Peivaste, Ahmed Makradi, Salim Belouettar
- Why it matters: Here, we introduce a Fourier-based Kolmogorov-Arnold Graph Attention Network (Fourier-KAGAT), a geometrically enhanced architecture that integrates learnable Fourier-based activation functions into the graph message-passing step, enabling the model to capture subtle stereoelectronic effects that fixed non-linearities miss.
- Innovation: Here, we introduce a Fourier-based Kolmogorov-Arnold Graph Attention Network (Fourier-KAGAT), a geometrically enhanced architecture that integrates learnable Fourier-based activation functions into the graph message-passing step, enabling the model to capture subtle stereoelectronic effects that fixed non-linearities miss.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 20. Neutron and X-ray Diffraction Reveal the Limits of Long-Range Machine Learning Potentials for Medium-Range Order in Silica Glass

- Date: `2026-07-03`
- Journal: Journal of Physics Materials
- Link: https://doi.org/10.1088/2515-7639/ae8643
- Tags: equivariant_ml, force_field, h2, interatomic_potential, md, ml
- Authors: Sai Harshit, Atul C. Thakur, Chris J. Benmore, Ganesh Sivaraman
- Why it matters: Abstract Glassy silica is a foundational material in optics and electronics, yet accurately predicting its medium-range order (MRO) remains a major challenge for machine-learning interatomic potentials (MLIPs).
- Innovation: Abstract Glassy silica is a foundational material in optics and electronics, yet accurately predicting its medium-range order (MRO) remains a major challenge for machine-learning interatomic potentials (MLIPs).
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 21. Predicting fatigue and failure in metals and composites: a machine learning enabled multiscale modeling perspective

- Date: `2026-06-13`
- Journal: Journal of Materials Science Materials Theory
- Link: https://doi.org/10.1186/s41313-026-00078-4
- Tags: h2, md, ml, review, uncertainty
- Authors: Somnath Ghosh
- Why it matters: The platform enables uncertainty-quantified efficient scale bridging with explicit representation of lower-scale descriptors (RAMPs) in higher-scale response functions.
- Innovation: The platform enables uncertainty-quantified efficient scale bridging with explicit representation of lower-scale descriptors (RAMPs) in higher-scale response functions.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 22. Semiconductor Nanotechnology and Advanced Materials for Photonic AI Chips and Quantum Information Systems

- Date: `2026-06-30`
- Journal: unknown
- Link: https://doi.org/10.62311/nesx/rb7j-978-81-688015-2-3
- Tags: generative_model, high_throughput, ml, uncertainty
- Authors: Murali Krishna Pasupuleti
- Why it matters: Abstract: This book develops a rigorous interdisciplinary framework for semiconductor nanotechnology and advanced materials as enabling foundations for photonic AI chips and quantum information systems.
- Innovation: Abstract: This book develops a rigorous interdisciplinary framework for semiconductor nanotechnology and advanced materials as enabling foundations for photonic AI chips and quantum information systems.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 23. Latent Genetic Algorithm for Crystal Structure Prediction

- Date: `2026-06-28`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.29220
- Tags: crystal, generative_model, h2, interatomic_potential, oxide, perovskite
- Authors: Kaixin Zheng, Wanjian Yin, Hongyu Yu, Hongjun Xiang
- Why it matters: Here we show that latent representations learned by pretrained universal interatomic potentials can serve as continuous evolutionary coordinates for crystal structure prediction.
- Innovation: Here we show that latent representations learned by pretrained universal interatomic potentials can serve as continuous evolutionary coordinates for crystal structure prediction.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 24. Machine-learned interatomic potentials for modeling multicomponent metallic systems: a comprehensive review

- Date: `2026-06-16`
- Journal: Materials Research Letters
- Link: https://doi.org/10.1080/21663831.2026.2684721
- Tags: alloy, h2, interatomic_potential, review, uncertainty
- Authors: Yash Kokane, H. M. Jayaprakash, Akash A. Deshmukh, Prakhar Singh Rajput, Manish Sahoo
- Why it matters: Multicomponent alloys demonstrate outstanding mechanical, chemical, and physical performance, but their vast compositional space cannot be efficiently navigated using conventional trial-and-error strategies.
- Innovation: Multicomponent alloys demonstrate outstanding mechanical, chemical, and physical performance, but their vast compositional space cannot be efficiently navigated using conventional trial-and-error strategies.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 25. Optimizing Expert-Designed Crystal Graph Networks for Band-Gap Prediction with an Autonomous LLM Research Loop

- Date: `2026-06-29`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.29717
- Tags: crystal, foundation_model, gnn, h2, high_throughput, ml, self_supervised
- Authors: Chenmu Zhang, Boris I. Yakobson
- Why it matters: Predicting a material's properties from its structure is a central, fast-advancing problem in computational materials science.
- Innovation: Predicting a material's properties from its structure is a central, fast-advancing problem in computational materials science.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 26. A green solvent screening tool for emerging materials via uncertainty aware, transformer enhanced transfer learning

- Date: `2026-06-11`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.13060
- Tags: battery, catalysis, h2, high_throughput, ml, transfer_learning, uncertainty
- Authors: Ioannis Kouroudis, Simon Ternes, Zhaosu Gu, Gohar A. Siddiqui, Marina Ustinova
- Why it matters: Overall, we augment data on solubility descriptors by orders of magnitude with high quality predictions.
- Innovation: Overall, we augment data on solubility descriptors by orders of magnitude with high quality predictions.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 27. Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents

- Date: `2026-06-28`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.29459
- Tags: active_learning, adsorption, foundation_model, generative_model, h2, high_throughput, mof, separation
- Authors: Kyungmin Nam, Seunghee Han, Jihan Kim
- Why it matters: We introduce LLM4MOF, a closed-loop framework in which language-model agents reason about chemistry, build candidate MOFs, and test them in simulation, refining hypotheses over ten autonomous iterations.
- Innovation: We introduce LLM4MOF, a closed-loop framework in which language-model agents reason about chemistry, build candidate MOFs, and test them in simulation, refining hypotheses over ten autonomous iterations.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 28. A general-purpose atomic cluster expansion interatomic potential for niobium

- Date: `2026-07-01`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2607.00540
- Tags: dft, h2, interatomic_potential, md, ml, separation
- Authors: A. D. Egorov, Ralf Drautz, Thomas Hammerschmidt
- Why it matters: Niobium, a body-centered cubic transition metal, poses a challenge for interatomic potentials, which struggle to capture its properties, such as phonons, high-pressure behavior, energy barriers to dislocation glide, and others.
- Innovation: Niobium, a body-centered cubic transition metal, poses a challenge for interatomic potentials, which struggle to capture its properties, such as phonons, high-pressure behavior, energy barriers to dislocation glide, and others.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.

### 29. Universal Interatomic Potentials as Configuration-Space Generators for One-Shot and Iterative Fine-Tuning of Ab Initio-Accurate Material-Specific Models

- Date: `2026-06-22`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.23214
- Tags: dft, force_field, foundation_model, h2, high_throughput, interatomic_potential, md, transfer_learning
- Authors: Jonas Hänseroth, Aaron Flötotto, Christian Dreßler
- Why it matters: Universal machine-learning interatomic potentials (MLIPs) are rapidly becoming general-purpose tools for atomistic simulation, but their role in quantitative materials modeling when reactive events are involved remains unsettled.
- Innovation: Universal machine-learning interatomic potentials (MLIPs) are rapidly becoming general-purpose tools for atomistic simulation, but their role in quantitative materials modeling when reactive events are involved remains unsettled.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 30. Self-driving manufacturing: accelerating materials discovery with adaptive closed-loop processing

- Date: `2026-07-01`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02204-9
- Tags: active_learning, h2, priority_journal, review
- Authors: Seulwon Choi, Hanseong Ko, Kyeongjin Lee, Hwanyeol Park
- Why it matters: Conventional human-centered process operations and explicit physics-based models face scalability limitations in high-dimensional, partially observable semiconductor and advanced materials processing.
- Innovation: Conventional human-centered process operations and explicit physics-based models face scalability limitations in high-dimensional, partially observable semiconductor and advanced materials processing.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
