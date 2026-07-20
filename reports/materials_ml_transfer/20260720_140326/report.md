# Literature Update

- Generated: `2026-07-20T14:03:26`
- Profile: `materials_ml_transfer`
- Since: `2023-07-21`
- Papers retained: `30`

## Overview

Collected 30 deduplicated papers for profile `materials_ml_transfer`. This transfer profile keeps non-MOF ML papers when they carry a concrete method signal; 29 retained papers are outside direct MOF literature. 30 papers contain transferable method tags and 10 appear in priority journals or major venue families. 18 papers also carry explicit material-system tags, helping judge whether the chemistry is close enough to MOFs.

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

### 1. (Invited) Autonomous, Data-Driven Acceleration of Energy Storage Technology, from Electrons to Devices

- Date: `2026-07-07`
- Journal: ECS Meeting Abstracts
- Link: https://doi.org/10.1149/ma2026-016651mtgabs
- Tags: active_learning, battery, catalysis, crystal, dft, electrocatalysis, electrolyte, equivariant_ml, force_field, foundation_model, generative_model, gnn, h2, high_throughput, interatomic_potential, md, ml, surrogate_model, transfer_learning, uncertainty
- Authors: Arghya Bhowmik
- Why it matters: We introduce equivariant graph neural network frameworks that predict electron density across molecules, liquids, and solids at speeds orders of magnitude beyond density functional theory (DFT).
- Innovation: We introduce equivariant graph neural network frameworks that predict electron density across molecules, liquids, and solids at speeds orders of magnitude beyond density functional theory (DFT).
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 2. Artificial intelligence and the frontier of phonon engineering: a perspective on discovering extreme thermal materials

- Date: `2026-07-16`
- Journal: Journal of Materials Science Materials Theory
- Link: https://doi.org/10.1186/s41313-026-00083-7
- Tags: active_learning, crystal, generative_model, gnn, h2, high_throughput, interatomic_potential, ml, review, uncertainty
- Authors: Ming Hu
- Why it matters: The discovery of materials with extreme lattice thermal conductivity (κ L )—spanning from sub-air thermal insulators to metallic conductors that rival diamond—represents one of the most consequential frontiers in contemporary materials physics and engineering.
- Innovation: The discovery of materials with extreme lattice thermal conductivity (κ L )—spanning from sub-air thermal insulators to metallic conductors that rival diamond—represents one of the most consequential frontiers in contemporary materials physics and engineering.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 3. AI-Driven Analytical and Molecular Data Modeling for Environmental and Pharmaceutical Applications

- Date: `2026-07-11`
- Journal: Scholars International Journal of Chemistry and Material Sciences
- Link: https://doi.org/10.36348/sijcms.2026.v09i04.002
- Tags: electrocatalysis, equivariant_ml, foundation_model, gnn, high_throughput, ml, multimodal, reaction_dataset, remote_sensing, review, uncertainty
- Authors: Noman Hassan, Umar Farooq, Shumaila Raheem, Ariba Anwar, Tasawar Abbas
- Why it matters: It examines data obtained from spectroscopy, chromatography, mass spectrometry, electrochemical sensors, hyperspectral imaging, process monitoring, molecular descriptors, fingerprints, SMILES, graphs, three-dimensional structures, proteins, and omics.
- Innovation: It examines data obtained from spectroscopy, chromatography, mass spectrometry, electrochemical sensors, hyperspectral imaging, process monitoring, molecular descriptors, fingerprints, SMILES, graphs, three-dimensional structures, proteins, and omics.
- Likely limitations: Catalyst generality inferred from sparse historical reaction data can still reflect reporting bias and needs targeted validation. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Rebuild the workflow on MOF catalytic reaction families with explicit scaffold generality, reporting-bias, and validation splits. Test whether multi-scale segmentation or domain adaptation ideas help classify pore regions, topology families, or morphology maps.
- MOF relevance: Reaction-specific small-data workflow is useful for MOF catalysis if catalyst generality, literature bias, and scaffold validation are made explicit.

### 4. From Newton to Neural Networks: A Review of Data-Driven Physical Modelling and the Rise of Physics-Informed AI

- Date: `2026-07-17`
- Journal: INTERNATIONAL JOURNAL OF MULTIDISCIPLINARY RESEARCH AND ANALYSIS
- Link: https://doi.org/10.47191/ijmra/v9-i7-28
- Tags: active_learning, dft, foundation_model, high_throughput, md, ml, physics_informed, review, uncertainty
- Authors: Eshit Dhiman
- Why it matters: This review examines the evolution of physical modelling from classical first-principles approaches to contemporary data-driven and physics-informed learning frameworks.
- Innovation: This review examines the evolution of physical modelling from classical first-principles approaches to contemporary data-driven and physics-informed learning frameworks.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 5. The evolution of AI from image interpretation toward scientific inference in nanoparticle electron microscopy

- Date: `2026-07-11`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2607.10388
- Tags: active_learning, foundation_model, h2, high_throughput, image_analysis, md, ml, multimodal, physics_informed, review, self_supervised
- Authors: Evropi Toulkeridou, Jiafei Li, Leonardo Lari, Panagiotis Grammatikopoulos
- Why it matters: Artificial intelligence (AI) is transforming electron microscopy by enabling quantitative analysis of increasingly large and complex datasets for nanoparticle characterization.
- Innovation: Artificial intelligence (AI) is transforming electron microscopy by enabling quantitative analysis of increasingly large and complex datasets for nanoparticle characterization.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Map the method onto MOF structure images, spectra, isotherm curves, or generated-structure consistency checks. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Distant-domain method can be useful if it maps to a concrete MOF object such as structure images, spectra, isotherms, pore maps, or multimodal consistency checks.

### 6. Artificial Intelligence and Machine Learning in the Design of Nanomaterials for Next-Generation Solar Cells

- Date: `2026-07-09`
- Journal: Scholars Journal of Engineering and Technology
- Link: https://doi.org/10.36347/sjet.2026.v14i07.002
- Tags: active_learning, dft, generative_model, high_throughput, ml, perovskite, review, uncertainty
- Authors: Mohammad Arsalan Aslam, Muhammad Rafi Ud Din Farhan, Ihsan Ullah, Syed Muhammad Abu Bakar Shah, Aqsa Nisar
- Why it matters: Through training on curated experimental datasets, high-throughput density functional theory (DFT) calculations, and multi-scale simulations, ML models can approximate complex structure–property relationships, identify optimal synthesis windows, and guide experimental efforts with quantifiable uncertainty.
- Innovation: Through training on curated experimental datasets, high-throughput density functional theory (DFT) calculations, and multi-scale simulations, ML models can approximate complex structure–property relationships, identify optimal synthesis windows, and guide experimental efforts with quantifiable uncertainty.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 7. Machine Learning in Materials Science: Data-Driven Discovery and Functional Applications

- Date: `2026-07-06`
- Journal: Encyclopedia
- Link: https://doi.org/10.3390/encyclopedia6070150
- Tags: dft, high_throughput, md, ml, physics_informed, review, surrogate_model, uncertainty
- Authors: Mihail Kolev
- Why it matters: It is also distinct from materials informatics, which is the wider data-centered framework that includes databases, descriptors, metadata, workflows, visualization, and knowledge management.
- Innovation: It is also distinct from materials informatics, which is the wider data-centered framework that includes databases, descriptors, metadata, workflows, visualization, and knowledge management.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 8. FLOWR.ROOT – A flow matching-based foundation model for joint multi-purpose structure-aware 3D ligand generation and affinity prediction

- Date: `2026-07-06`
- Journal: Nature Communications
- Link: https://doi.org/10.1038/s41467-026-74130-9
- Tags: crystal, equivariant_ml, foundation_model, priority_journal, self_supervised, separation, transfer_learning
- Authors: Julian Cremer, Tuan Le, Mohammad M Ghahremanpour, Emilia Sługocka, Filipe Menezes
- Why it matters: Abstract We present FLOWR.ROOT, an S E (3)-equivariant flow-matching foundation model that unifies pocket-aware 3D ligand generation with multi-endpoint binding affinity prediction (pIC 50 , p K i , p K d , pEC 50 ) and pLDDT-based confidence estimation in a single backbone.
- Innovation: Abstract We present FLOWR.ROOT, an S E (3)-equivariant flow-matching foundation model that unifies pocket-aware 3D ligand generation with multi-endpoint binding affinity prediction (pIC 50 , p K i , p K d , pEC 50 ) and pLDDT-based confidence estimation in a single backbone.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 9. Artificial intelligence and automation in enzyme engineering: evolution, advances, and future perspectives

- Date: `2026-07-10`
- Journal: Bioresources and Bioprocessing
- Link: https://doi.org/10.1186/s40643-026-01096-3
- Tags: active_learning, ml, reaction_dataset, review, self_supervised, uncertainty
- Authors: Kexin Hao, J C Liu, Hui Tang, Yan Zhang, Yandong Sun
- Why it matters: Natural enzymes often fail to meet industrial demands for catalytic efficiency, stability, and substrate specificity, creating a critical bottleneck in biomanufacturing.
- Innovation: Natural enzymes often fail to meet industrial demands for catalytic efficiency, stability, and substrate specificity, creating a critical bottleneck in biomanufacturing.
- Likely limitations: Catalyst generality inferred from sparse historical reaction data can still reflect reporting bias and needs targeted validation. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Rebuild the workflow on MOF catalytic reaction families with explicit scaffold generality, reporting-bias, and validation splits. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Reaction-specific small-data workflow is useful for MOF catalysis if catalyst generality, literature bias, and scaffold validation are made explicit.

### 10. Fine-tuning universal machine learning potentials for transition state search in surface catalysis

- Date: `2026-07-09`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02228-1
- Tags: active_learning, alloy, catalysis, dft, h2, high_throughput, interatomic_potential, ml, priority_journal, transfer_learning
- Authors: Raffaele Cheula, Mie Andersen, John R. Kitchin
- Why it matters: Here, we present a workflow based on active learning to iteratively fine-tune uMLPs for DFT-quality TS search.
- Innovation: Here, we present a workflow based on active learning to iteratively fine-tune uMLPs for DFT-quality TS search.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 11. Guiding generative models to uncover diverse and novel crystals via reinforcement learning

- Date: `2026-07-06`
- Journal: Nature Machine Intelligence
- Link: https://doi.org/10.1038/s42256-026-01262-4
- Tags: crystal, generative_model, h2, md, priority_journal, uncertainty
- Authors: Hyunsoo Park, Aron Walsh
- Why it matters: Here we introduce a reinforcement learning framework that guides latent denoising diffusion models in finding diverse and novel, yet thermodynamically viable, crystalline compounds.
- Innovation: Here we introduce a reinforcement learning framework that guides latent denoising diffusion models in finding diverse and novel, yet thermodynamically viable, crystalline compounds.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 12. Symmetry-Informed Deep Learning for Electromagnetic Scattering

- Date: `2026-07-14`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2607.12810
- Tags: crystal, dft, equivariant_ml, h2, ml, physics_informed, surrogate_model
- Authors: Viktor A. Lilja, Philippe Tassin
- Why it matters: Here we show that symmetry provides a powerful and largely untapped route to overcoming this limitation in electromagnetic scattering problems.
- Innovation: Here we show that symmetry provides a powerful and largely untapped route to overcoming this limitation in electromagnetic scattering problems.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 13. Bgolearn: a unified Bayesian optimization framework for accelerating materials discovery

- Date: `2026-07-14`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02226-3
- Tags: active_learning, alloy, h2, high_throughput, ml, priority_journal, surrogate_model, uncertainty
- Authors: Bin Cao, Jie Xiong, Jiaxuan Ma, Yuan Tian, Yirui Hu
- Why it matters: Here, we present Bgolearn, a versatile Python framework that brings BO to materials research through intuitive interfaces, robust algorithms, and materials-focused workflows.
- Innovation: Here, we present Bgolearn, a versatile Python framework that brings BO to materials research through intuitive interfaces, robust algorithms, and materials-focused workflows.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 14. Transferable Implicit Solvent Machine Learning Potential for Drugs and Proteins Approaching Ab Initio Accuracy

- Date: `2026-07-12`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2607.10887
- Tags: crystal, dft, equivariant_ml, force_field, gnn, h2, high_throughput, interatomic_potential, ml, water
- Authors: Jan Eckwert, Julija Zavadlav
- Why it matters: Here, we introduce the Transferable Water Implicit Network (TWIN), an implicit water MLP parametrized entirely by an Equivariant Graph Neural Network and trained solely on ab initio and experimental labels.
- Innovation: Here, we introduce the Transferable Water Implicit Network (TWIN), an implicit water MLP parametrized entirely by an Equivariant Graph Neural Network and trained solely on ab initio and experimental labels.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 15. Unlocking the Chemical Space for Rechargeable Batteries with a Generative Solvent Design System

- Date: `2026-07-16`
- Journal: ACS Nano
- Link: https://doi.org/10.1021/acsnano.6c06255
- Tags: battery, electrolyte, h2, high_throughput, ml, physics_informed, priority_journal, transfer_learning
- Authors: Zhan-Yun Zhang, Rocío Mercado, T.T. Le, Chao Zhang
- Why it matters: High Resolution Image Download MS PowerPoint Slide Electrolyte discovery for rechargeable batteries today relies on heuristic trial-and-error or high-throughput screening of existing molecules.
- Innovation: High Resolution Image Download MS PowerPoint Slide Electrolyte discovery for rechargeable batteries today relies on heuristic trial-and-error or high-throughput screening of existing molecules.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 16. Machine learning for frontier orbital energetics: A review of HOMO–LUMO prediction methods

- Date: `2026-07-15`
- Journal: Carbon Trends
- Link: https://doi.org/10.1016/j.cartre.2026.100674
- Tags: dft, equivariant_ml, h2, high_throughput, ml, review, self_supervised, separation, uncertainty
- Authors: Luis José Mantilla Santa Cruz, Luis F. Faina, João Henrique de Souza Pereira
- Why it matters: The energies of the highest occupied and lowest unoccupied molecular orbitals (HOMO, LUMO) and their difference, the HOMO–LUMO gap, are a recurring evaluation target in molecular machine learning.
- Innovation: The energies of the highest occupied and lowest unoccupied molecular orbitals (HOMO, LUMO) and their difference, the HOMO–LUMO gap, are a recurring evaluation target in molecular machine learning.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 17. Girsanov Reweighting for Uncertainty Propagation in Rare-Event Kinetics

- Date: `2026-07-15`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2607.13757
- Tags: dft, h2, high_throughput, interatomic_potential, md, ml, surrogate_model, uncertainty
- Authors: Léonard Moracchini, Thomas Pigeon, Morgane Menz, Thibault Faney, Thomas D. Swinburne
- Why it matters: In this work, we introduce a framework for propagating MLIP uncertainty to the averaged committor probability, a kinetic observable that enables reaction-rate calculations.
- Innovation: In this work, we introduce a framework for propagating MLIP uncertainty to the averaged committor probability, a kinetic observable that enables reaction-rate calculations.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 18. The impact of spurious imaginary phonon modes on thermal properties of Metal-organic Frameworks

- Date: `2026-07-17`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02231-6
- Tags: adsorption, co2, dft, h2, high_throughput, interatomic_potential, ml, mof, porous_material, priority_journal, separation
- Authors: P.S. Kamath, Kristin Persson
- Why it matters: Finally, we introduce a simple, rapid post-processing workflow that can be applied to standard phonon calculations to effectively correct heat capacity estimates and account for spurious imaginary modes in MOFs.
- Innovation: Finally, we introduce a simple, rapid post-processing workflow that can be applied to standard phonon calculations to effectively correct heat capacity estimates and account for spurious imaginary modes in MOFs.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 19. Phase prediction in high-entropy alloys through uncertainty sampling and symbolic classification-based parameter discovery

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

### 20. Predicting interface structure using the minima hopping method with a machine learning interatomic potential

- Date: `2026-07-15`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02214-7
- Tags: dft, equivariant_ml, h2, high_throughput, interatomic_potential, ml, priority_journal
- Authors: Chang-Ti Chou, Menghang Wang, Chao Yang, Peter A. van Aken, Nicola H. Perry
- Why it matters: In this study, we present an effective approach for interface structure prediction that integrates the minima hopping method (MHM) with the state-of-the-art machine-learning interatomic potential (MLIP), Allegro.
- Innovation: In this study, we present an effective approach for interface structure prediction that integrates the minima hopping method (MHM) with the state-of-the-art machine-learning interatomic potential (MLIP), Allegro.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 21. AutoSurrogate: An LLM-driven multi-agent framework for autonomous construction of deep learning surrogate models in subsurface flow

- Date: `2026-07-17`
- Journal: Advanced Engineering Informatics
- Link: https://doi.org/10.1016/j.aei.2026.105058
- Tags: force_field, foundation_model, h2, ml, porous_material, surrogate_model, uncertainty
- Authors: Jiale Liu, Nanzhe Wang
- Why it matters: In this work, we present AutoSurrogate , a large-language-model-driven multi-agent framework that empowers practitioners without ML expertise to build high-quality surrogates for subsurface flow problems through natural-language instructions.
- Innovation: In this work, we present AutoSurrogate , a large-language-model-driven multi-agent framework that empowers practitioners without ML expertise to build high-quality surrogates for subsurface flow problems through natural-language instructions.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 22. Transport Novelty Distance: A Distributional Metric for Evaluating Material Generative Models

- Date: `2026-07-06`
- Journal: Journal of Physics Materials
- Link: https://doi.org/10.1088/2515-7639/ae869a
- Tags: crystal, generative_model, gnn, h2, high_throughput, ml, self_supervised, separation
- Authors: Paul Hagemann, Simon Müller, Janine George, Philipp Benner
- Why it matters: In this paper, we introduce the Transport Novelty Distance (TNovD) to judge generative models used for materials discovery jointly by the quality and novelty of the generated materials.
- Innovation: In this paper, we introduce the Transport Novelty Distance (TNovD) to judge generative models used for materials discovery jointly by the quality and novelty of the generated materials.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 23. Reactive Molecular Dynamics of Hydrogen Evolution at Charged Interfaces Using Machine Learning Potentials

- Date: `2026-07-14`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15006079/v1
- Tags: catalysis, dft, electrocatalysis, equivariant_ml, h2, interatomic_potential, md, ml, separation, two_d_material, water
- Authors: Md Sharif Khan, Oliviero Andreussi
- Why it matters: Here, we develop an equivariant machine learning interatomic potential trained on density functional theory data for electrochemically activated MoS2/water interfaces under charged conditions.
- Innovation: Here, we develop an equivariant machine learning interatomic potential trained on density functional theory data for electrochemically activated MoS2/water interfaces under charged conditions.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 24. A review of artificial intelligence in materials screening: Data, models, and applications in forensic science

- Date: `2026-07-14`
- Journal: Next Materials
- Link: https://doi.org/10.1016/j.nxmate.2026.102756
- Tags: catalysis, generative_model, h2, high_throughput, ml, polymer, remote_sensing, review
- Authors: Sahana Datta, Ripan Chakraborty, Riddhit Bhattacharjee, Aditya Kumar Kar
- Why it matters: In parallel, artificial intelligence (AI) has catalyzed a paradigm shift in high-throughput materials screening across domains such as energy storage, catalysis, and polymer science by leveraging large-scale computational and experimental datasets, engineered descriptors, and advanced machine learning (ML) and deep learning (DL) architectures.
- Innovation: In parallel, artificial intelligence (AI) has catalyzed a paradigm shift in high-throughput materials screening across domains such as energy storage, catalysis, and polymer science by leveraging large-scale computational and experimental datasets, engineered descriptors, and advanced machine learning (ML) and deep learning (DL) architectures.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Test whether multi-scale segmentation or domain adaptation ideas help classify pore regions, topology families, or morphology maps. Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints.
- MOF relevance: Distant-domain method can be useful if it maps to a concrete MOF object such as structure images, spectra, isotherms, pore maps, or multimodal consistency checks.

### 25. Machine learning Hamiltonian enables scalable and accurate defect calculations: the case of oxygen vacancies in amorphous SiO2

- Date: `2026-07-12`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02217-4
- Tags: dft, h2, interatomic_potential, ml, priority_journal
- Authors: Zhenxing Dai, Yang Zhong, Mingjue Ni, Menglin Huang, Hongjun Xiang
- Why it matters: Here, we present a machine learning Hamiltonian (MLH) model-based method for calculating total energies and atomic forces in defect supercells with linear-scaling computational cost, enabling efficient structural relaxation and accurate formation energy predictions.
- Innovation: Here, we present a machine learning Hamiltonian (MLH) model-based method for calculating total energies and atomic forces in defect supercells with linear-scaling computational cost, enabling efficient structural relaxation and accurate formation energy predictions.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.

### 26. Trustworthy Explainable AI for Asphalt Pavement Engineering: A Systematic Scoping Review of Materials, Performance, and Decision Support

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

### 27. Machine learning-driven analysis and process optimization of FePt-BN granular films for HAMR applications

- Date: `2026-07-16`
- Journal: Science and Technology of Advanced Materials
- Link: https://doi.org/10.1080/14686996.2026.2699076
- Tags: active_learning, h2, ml, priority_journal
- Authors: Daisuke Ogawa, Tetsuya Shoji, Masao Yano, Yusuke Matsuoka, Y. K. Takahashi
- Why it matters: The ever-increasing demand for high-density, energy-efficient data storage, propelled by AI and cloud infrastructures, is driving advancements in heat-assisted magnetic recording (HAMR) media.
- Innovation: The ever-increasing demand for high-density, energy-efficient data storage, propelled by AI and cloud infrastructures, is driving advancements in heat-assisted magnetic recording (HAMR) media.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 28. Data-driven atomistic modelling of hybrid halide perovskite passivation

- Date: `2026-07-06`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2607.05321
- Tags: crystal, foundation_model, h2, interatomic_potential, ml, perovskite, transfer_learning, uncertainty
- Authors: Laura-Bianca Pașca, Henry J. Snaith, Volker L. Deringer
- Why it matters: Molecular passivation of surface defects is key to improving the optoelectronic performance of hybrid halide perovskite materials, but the underlying atomistic mechanisms are incompletely understood.
- Innovation: Molecular passivation of surface defects is key to improving the optoelectronic performance of hybrid halide perovskite materials, but the underlying atomistic mechanisms are incompletely understood.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 29. Machine-learned interatomic potentials for modeling multicomponent metallic systems: a comprehensive review

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

### 30. XMCQDPT2-fidelity transfer-learning potentials and a wavepacket oscillation model for ultrafast photodynamics

- Date: `2026-07-14`
- Journal: The Journal of Chemical Physics
- Link: https://doi.org/10.1063/5.0315698
- Tags: force_field, h2, interatomic_potential, md, separation, transfer_learning
- Authors: Ivan V. Dudakov, Pavel M. Radzikovitsky, Dmitry S. Popov, Denis A. Firsov, Vadim V. Korolev
- Why it matters: Finally, we develop a wavepacket oscillation model for fitting excited-state population dynamics, which quantitatively reproduces the ultrafast non-exponential decay and extracts state- and channel-specific lifetimes, directly linking quantum transition probabilities to classical rate constants.
- Innovation: Finally, we develop a wavepacket oscillation model for fitting excited-state population dynamics, which quantitatively reproduces the ultrafast non-exponential decay and extracts state- and channel-specific lifetimes, directly linking quantum transition probabilities to classical rate constants.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
