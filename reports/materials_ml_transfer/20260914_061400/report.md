# Literature Update

- Generated: `2026-09-14T06:14:00`
- Profile: `materials_ml_transfer`
- Since: `2023-09-15`
- Papers retained: `30`

## Overview

Collected 30 deduplicated papers for profile `materials_ml_transfer`. This transfer profile keeps non-MOF ML papers when they carry a concrete method signal; 30 retained papers are outside direct MOF literature. 30 papers contain transferable method tags and 8 appear in priority journals or major venue families. 19 papers also carry explicit material-system tags, helping judge whether the chemistry is close enough to MOFs.

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

### 1. Generative artificial intelligence for nanomaterial discovery and nanoengineering: From data-driven design to autonomous laboratories

- Date: `2026-09-05`
- Journal: Next Nanotechnology
- Link: https://doi.org/10.1016/j.nxnano.2026.100728
- Tags: foundation_model, generative_model, h2, md, ml, multimodal, physics_informed, review
- Authors: Vilas A. Chavan
- Why it matters: From conventional trial-and-error experimentation, nanomaterials research is moving toward data-centric and autonomous discovery paradigms that couple nanotechnology with artificial intelligence (AI).
- Innovation: From conventional trial-and-error experimentation, nanomaterials research is moving toward data-centric and autonomous discovery paradigms that couple nanotechnology with artificial intelligence (AI).
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 2. Mechanism-informed machine learning for intelligent design of rare-earth-containing magnesium-based alloys

- Date: `2026-09-02`
- Journal: Journal of Magnesium and Alloys
- Link: https://doi.org/10.1016/j.jma.2026.102273
- Tags: active_learning, alloy, electrocatalysis, force_field, generative_model, high_throughput, ml, physics_informed, review, uncertainty
- Authors: LI Jiangwei, Haoran Shen, Tong Li, Huan Liu, Yuna Wu
- Why it matters: However, strict inverse design remains limited by scarce and heterogeneous data, incomplete physical descriptors, weak model transferability, and insufficient closed-loop validation.
- Innovation: However, strict inverse design remains limited by scarce and heterogeneous data, incomplete physical descriptors, weak model transferability, and insufficient closed-loop validation.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 3. SHAP-guided Machine Learning for Interpretable Band Gap Prediction and Inverse Design in ABX₃ Perovskites

- Date: `2026-08-24`
- Journal: International Journal of Computational Intelligence Systems
- Link: https://doi.org/10.1007/s44196-026-01454-1
- Tags: dft, generative_model, high_throughput, ml, perovskite, separation, symbolic_regression, uncertainty
- Authors: Aldrin Manon, Rajiv Kumar Gill, Vijay Kumar, Kapil Joshi, Arvind Dhaka
- Why it matters: Abstract The (ABX₃) perovskites form the basis of the future of optoelectronics, but the limiting DFT calculations remain the bottleneck to high-throughput density screening.
- Innovation: Abstract The (ABX₃) perovskites form the basis of the future of optoelectronics, but the limiting DFT calculations remain the bottleneck to high-throughput density screening.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 4. Machine learning for predicting the glass transition and melting temperatures of polymers: molecular representations, model architectures, and interpretability

- Date: `2026-09-03`
- Journal: Frontiers in Materials
- Link: https://doi.org/10.3389/fmats.2026.1919251
- Tags: active_learning, crystal, gnn, h2, high_throughput, ml, polymer, review, uncertainty
- Authors: Guo Haiqian, Yitian Zhang, Wei Zan, Jiejie Liu, Shuai Guo
- Why it matters: Experiments and simulations are accurate but costly, while classical structure–property models depend on hand-crafted descriptors; machine learning instead maps chemical structure to thermal transitions end to end.
- Innovation: Experiments and simulations are accurate but costly, while classical structure–property models depend on hand-crafted descriptors; machine learning instead maps chemical structure to thermal transitions end to end.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 5. Physics-informed automated surface reconstruction via low-energy electron diffraction based on Bayesian optimization

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

### 6. A physics-informed synthetic-to-experimental framework for few-shot structural segmentation of HRTEM images

- Date: `2026-09-01`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02306-4
- Tags: crystal, h2, physics_informed, priority_journal, self_supervised, separation, transfer_learning
- Authors: Shengmin Zhou, Xuehai Huang, Junjie Lin, Yu Wang
- Why it matters: Here we report a physics-informed synthetic-to-experimental framework that enables few-shot multiclass HRTEM segmentation.
- Innovation: Here we report a physics-informed synthetic-to-experimental framework that enables few-shot multiclass HRTEM segmentation.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 7. Thermal conductivity predictions with foundation atomistic models

- Date: `2026-09-05`
- Journal: Nature Communications
- Link: https://doi.org/10.1038/s41467-026-76391-w
- Tags: dft, foundation_model, h2, high_throughput, md, ml, priority_journal, transfer_learning
- Authors: Balázs Póta, Paramvir Ahlawat, Gábor Cśanyi, Michele Simoncelli
- Why it matters: Hitherto, the accuracy and utility of these models have been assessed relying on descriptors based on formation energies or idealized harmonic atomic vibrations.
- Innovation: Hitherto, the accuracy and utility of these models have been assessed relying on descriptors based on formation energies or idealized harmonic atomic vibrations.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 8. DFT-based machine-learning for the rational design of magnetocaloric high-entropy alloys

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

### 9. Out-of-Distribution Inverse Design of Elastic Networks with Differentiable Graph Neural Network Molecular Dynamics

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

### 10. Data-Driven Advances in Electrochemical Energy and Sensing: Artificial Intelligence Approaches from Concept to Application

- Date: `2026-09-02`
- Journal: Journal of The Electrochemical Society
- Link: https://doi.org/10.1149/1945-7111/aea1c0
- Tags: battery, dft, electrocatalysis, md, ml, physics_informed, review
- Authors: Sourav Ghosh, Barkha Rani
- Why it matters: Abstract The intersection of machine learning (ML) and electrochemical research is catalyzing transformative advancements in energy storage and conversion technologies.
- Innovation: Abstract The intersection of machine learning (ML) and electrochemical research is catalyzing transformative advancements in energy storage and conversion technologies.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 11. Deep learning in materials electron microscopy: models, applications, and emerging trends

- Date: `2026-08-24`
- Journal: Machine Learning Science and Technology
- Link: https://doi.org/10.1088/2632-2153/ae9dea
- Tags: foundation_model, generative_model, high_throughput, md, ml, multimodal, review
- Authors: Camilo Augusto Fernandes Salvador, Clovis Lapointe, Thomas Bilyk, E. Meslin, Mihai‐Cosmin Marinica
- Why it matters: Abstract The intersection of deep learning (DL) and materials electron microscopy has significantly expanded since the early 2010s; however, the diversity of model architectures and use cases makes it hard to identify literature gaps and determine which models are well-established in this field of application.
- Innovation: Abstract The intersection of deep learning (DL) and materials electron microscopy has significantly expanded since the early 2010s; however, the diversity of model architectures and use cases makes it hard to identify literature gaps and determine which models are well-established in this field of application.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 12. Domain-specific dataset enable accurate MLIPs for disordered halide-based solid electrolytes

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

### 13. Benchmarking on-the-Fly Machine Learning Force Fields for Ion Hydration: Structure, Coordination, and Exchange Dynamics across Monovalent and Divalent Cations

- Date: `2026-09-02`
- Journal: The Journal of Physical Chemistry B
- Link: https://doi.org/10.1021/acs.jpcb.6c02837
- Tags: battery, dft, electrolyte, equivariant_ml, force_field, foundation_model, h2, high_throughput, md, ml, water
- Authors: Mohammed S. Salha, Wuyang Lin, Gregory A. Chass, Devis Di Tommaso
- Why it matters: Targeted improvements such as augmented transition-state sampling, higher angular-resolution descriptors, and long-range electrostatic corrections are identified as high-priority directions for kinetic fidelity in next-generation electrolyte force fields.
- Innovation: Targeted improvements such as augmented transition-state sampling, higher angular-resolution descriptors, and long-range electrostatic corrections are identified as high-priority directions for kinetic fidelity in next-generation electrolyte force fields.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 14. Accelerating density functional theory calculations using conditional generative-adversarial neural networks

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

### 15. Accelerated stable structure prediction of Li-intercalated bilayer graphene using a data-efficient deep learning framework

- Date: `2026-09-04`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02314-4
- Tags: battery, dft, h2, interatomic_potential, ml, priority_journal, two_d_material
- Authors: Hui Li, B. Gui, Hailong Zhang, Le Yang, H H Chen
- Why it matters: Here, we present DESSP, a data-efficient deep learning framework for accelerated stable structure prediction in Li-intercalated BLG.
- Innovation: Here, we present DESSP, a data-efficient deep learning framework for accelerated stable structure prediction in Li-intercalated BLG.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.

### 16. TAME: Element-wise Mixture-of-Experts Fusion for Reliable and Interpretable Molecular Property Prediction

- Date: `2026-09-07`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15008270/v2
- Tags: crystal, gnn, h2, ml, self_supervised, transfer_learning
- Authors: Robert Schiller, Christoph Weisser, Klaus-Robert Müller, Christian Ochsenfeld, Parastoo Semnani
- Why it matters: The three dominant molecular representations fail in complementary ways—physicochemical descriptors are exact but fixed, graph neural networks learn topology but degenerate under sparse supervision, and language models supply semantic context but cannot compute exact quantities— yet combining them is itself the learning problem, because modality-level scalar gating commits the whole model to one trust weight per source.
- Innovation: The three dominant molecular representations fail in complementary ways—physicochemical descriptors are exact but fixed, graph neural networks learn topology but degenerate under sparse supervision, and language models supply semantic context but cannot compute exact quantities— yet combining them is itself the learning problem, because modality-level scalar gating commits the whole model to one trust weight per source.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 17. Uncertainty-aware hybrid framework for melt pool geometry prediction and process map development in Laser Powder Bed Fusion of Inconel 718

- Date: `2026-09-05`
- Journal: Journal of Materials Processing Technology
- Link: https://doi.org/10.1016/j.jmatprotec.2026.119493
- Tags: active_learning, h2, ml, physics_informed, porous_material, uncertainty
- Authors: Sayed Ehsan Saghaian, Sayed Ehsan Saghaian, Milad Hemmati, Alvaro Cameo Hernanz, Li Yang
- Why it matters: This study presents an uncertainty-aware hybrid ML framework for melt pool geometry prediction and process qualification in L-PBF of Inconel 718 (IN718).
- Innovation: This study presents an uncertainty-aware hybrid ML framework for melt pool geometry prediction and process qualification in L-PBF of Inconel 718 (IN718).
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 18. TAME: Element-wise Mixture-of-Experts Fusion for Data-Efficient and Interpretable Molecular Property Prediction

- Date: `2026-09-03`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15008270/v1
- Tags: crystal, gnn, h2, ml, multimodal, self_supervised
- Authors: Robert Schiller, Christoph Weisser, Klaus-Robert Müller, Christian Ochsenfeld, Parastoo Semnani
- Why it matters: The three dominant molecular representations fail in complementary ways—physicochemical descriptors are exact but fixed, graph neural networks learn topology but degenerate under sparse supervision, and language models supply semantic context but cannot compute exact quantities—yet combining them is itself the learning problem, because modality-level scalar gating commits the whole model to one trust weight per source.
- Innovation: The three dominant molecular representations fail in complementary ways—physicochemical descriptors are exact but fixed, graph neural networks learn topology but degenerate under sparse supervision, and language models supply semantic context but cannot compute exact quantities—yet combining them is itself the learning problem, because modality-level scalar gating commits the whole model to one trust weight per source.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 19. Defect engineering of semiconductor photocatalysts for solar energy conversion: from atomic-level design to AI-driven materials discovery for sustainable development and clean energy

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

### 20. Decoding Multiscale Degradation of Layered Cathodes in All‐Solid‐State Lithium Batteries: An Advanced Diagnostics‐Driven Framework

- Date: `2026-09-02`
- Journal: Advanced Energy Materials
- Link: https://doi.org/10.1002/aenm.71528
- Tags: battery, electrolyte, h2, ml, multimodal, oxide, priority_journal, review
- Authors: Dayakar Gandla, Inyoung Jang, Ashok Kumar Kakarla, Se Hwan Park, Junghyun Choi
- Why it matters: ABSTRACT All‐solid‐state lithium batteries (ASSLBs) with layered oxide cathodes such as LiNi 1‐x‐y Mn x Co y O 2 (NMC), LiNi 1‐x‐y Co x Al y O 2 (NCA), LiNiO 2 (LNO), and lithium‐rich layered oxides (LLOs) offer superior energy density and safety, yet their performance is severely limited by complex, coupled degradation mechanisms at the cathode/inorganic solid‐state electrolyte (SSE) interface and within the cathode bulk.
- Innovation: ABSTRACT All‐solid‐state lithium batteries (ASSLBs) with layered oxide cathodes such as LiNi 1‐x‐y Mn x Co y O 2 (NMC), LiNi 1‐x‐y Co x Al y O 2 (NCA), LiNiO 2 (LNO), and lithium‐rich layered oxides (LLOs) offer superior energy density and safety, yet their performance is severely limited by complex, coupled degradation mechanisms at the cathode/inorganic solid‐state electrolyte (SSE) interface and within the cathode bulk.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 21. Large language models for applied superconductivity: towards physics-aware reasoning and integrated multi-modal generative AI

- Date: `2026-08-24`
- Journal: Superconductor Science and Technology
- Link: https://doi.org/10.1088/1361-6668/ae9df9
- Tags: foundation_model, generative_model, h2, ml, multimodal, review, uncertainty
- Authors: Yahao Wu, Wenjuan Song, Lurui Fang, Mohammad Yazdani-Asrami
- Why it matters: Abstract Applied superconductivity research spans materials science, physics, cryogenics, and large-scale device and system engineering, generating highly fragmented data, heterogeneous models, and disconnected domain-specific knowledge representations.
- Innovation: Abstract Applied superconductivity research spans materials science, physics, cryogenics, and large-scale device and system engineering, generating highly fragmented data, heterogeneous models, and disconnected domain-specific knowledge representations.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 22. Performance of universal machine learning potentials in global optimization of inorganic crystal structures

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

### 23. Data-driven approaches to rock typing in reservoir characterization: methodological advances, integration strategies, and challenges

- Date: `2026-09-10`
- Journal: Frontiers in Earth Science
- Link: https://doi.org/10.3389/feart.2026.1953635
- Tags: h2, ml, physics_informed, porous_material, review
- Authors: Stephen Adjei, Abdul Mumuni Ayuba, Kwesi Mensah Duodu-Turkson, Yen Adams Sokama-Neuyam, Jonathan Atuquaye Quaye
- Why it matters: Rock typing plays a pivotal role in reservoir characterization by categorizing reservoir rocks into distinct units based on their petrophysical and geological properties.
- Innovation: Rock typing plays a pivotal role in reservoir characterization by categorizing reservoir rocks into distinct units based on their petrophysical and geological properties.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 24. Simultaneous retrieval of 13 phytoplankton pigments from Sentinel-3 OLCI using convolutional neural networks and transfer learning

- Date: `2026-09-10`
- Journal: Frontiers in Remote Sensing
- Link: https://doi.org/10.3389/frsen.2026.1880618
- Tags: h2, high_throughput, ml, self_supervised, transfer_learning
- Authors: Borja Sánchez-López, Marco Talone, Jesus Cerquides, Annalisa Di Cicco, Gonzalo Martínez-Fornos
- Why it matters: This study presents the first systematic benchmark of five ML architectures: Random Forest (RF), eXtreme Gradient Boosting (XGB), Dense Neural Network (DNN), one-dimensional Convolutional Neural Network (CNN), and Bidirectional Long Short-Term Memory Network (BiLSTM) for retrieving 13 pigments of interest to the ocean color community from OLCI-equivalent multi-spectral radiometry.
- Innovation: This study presents the first systematic benchmark of five ML architectures: Random Forest (RF), eXtreme Gradient Boosting (XGB), Dense Neural Network (DNN), one-dimensional Convolutional Neural Network (CNN), and Bidirectional Long Short-Term Memory Network (BiLSTM) for retrieving 13 pigments of interest to the ocean color community from OLCI-equivalent multi-spectral radiometry.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 25. Entropy-Guided Dataset Reduction for Machine-Learned Interatomic Potentials

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

### 26. The physical foundation beneath protein generative modeling

- Date: `2026-09-03`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2609.04465
- Tags: generative_model, h2, review, uncertainty
- Authors: Tianyu Lu, Po‐Ssu Huang
- Why it matters: We present a perspective that respecting the underlying physics of macromolecular systems, increasingly through learned representations that are physically grounded and updating generative models with experimental data, is foundational to generative modeling for functional protein design.
- Innovation: We present a perspective that respecting the underlying physics of macromolecular systems, increasingly through learned representations that are physically grounded and updating generative models with experimental data, is foundational to generative modeling for functional protein design.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 27. MLIP Detective: Active Failure Mode Discovery Beyond Benchmark Scores for Machine-Learning Interatomic Potentials

- Date: `2026-09-08`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2609.08399
- Tags: equivariant_ml, h2, high_throughput, interatomic_potential, physics_informed
- Authors: Ryuhei Okuno, Nontawat Charoenphakdee, Kaoru Hisama, Yuta Tsuboi
- Why it matters: We introduce MLIP Detective, an agentic framework for active failure mode discovery.
- Innovation: We introduce MLIP Detective, an agentic framework for active failure mode discovery.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 28. Critical benchmarking of machine-learned interatomic potentials for intermolecular and noncovalent interactions

- Date: `2026-09-07`
- Journal: Machine Learning Science and Technology
- Link: https://doi.org/10.1088/2632-2153/aea39f
- Tags: dft, equivariant_ml, h2, high_throughput, interatomic_potential, uncertainty
- Authors: Kamal Singh Nayal, Ilkwon Cho, Olexandr Isayev
- Why it matters: Abstract Accurate benchmarking of intermolecular interaction energies is central to evaluating quantum chemical methods and guiding the development of reliable machine-learned interatomic potentials (MLIPs).
- Innovation: Abstract Accurate benchmarking of intermolecular interaction energies is central to evaluating quantum chemical methods and guiding the development of reliable machine-learned interatomic potentials (MLIPs).
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 29. MutexaGPT: an intuition-to-design translator for physics-based enzyme engineering

- Date: `2026-09-10`
- Journal: Nature Computational Science
- Link: https://doi.org/10.1038/s43588-026-01049-y
- Tags: foundation_model, h2, high_throughput, md, priority_journal
- Authors: Qianzhen Shao, Yinjie Zhong, Sebastian Stull, Xinchun Ran, Ning Ding
- Why it matters: Here we introduce MutexaGPT, an open-access, multi-agent large language model platform that translates enzyme engineering intuition to physics-based simulations and thus variant designs.
- Innovation: Here we introduce MutexaGPT, an open-access, multi-agent large language model platform that translates enzyme engineering intuition to physics-based simulations and thus variant designs.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 30. Reusable Operators for Irreducible Cartesian Tensor Decomposition and Coupling

- Date: `2026-09-05`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2609.05971
- Tags: crystal, dft, equivariant_ml, h2, ml
- Authors: Mingjian Wen
- Why it matters: Here, we develop such a construction and obtain these operators explicitly.
- Innovation: Here, we develop such a construction and obtain these operators explicitly.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
