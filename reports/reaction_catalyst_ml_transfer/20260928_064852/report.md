# Literature Update

- Generated: `2026-09-28T06:48:52`
- Profile: `reaction_catalyst_ml_transfer`
- Since: `2016-09-30`
- Papers retained: `27`

## Overview

Collected 27 deduplicated papers for profile `reaction_catalyst_ml_transfer`. This transfer profile keeps non-MOF ML papers when they carry a concrete method signal; 26 retained papers are outside direct MOF literature. 27 papers contain transferable method tags and 4 appear in priority journals or major venue families. 22 papers also carry explicit material-system tags, helping judge whether the chemistry is close enough to MOFs.

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

### 1. Machine learning approaches for electrocatalyst design in water splitting: a review for green hydrogen production

- Date: `2026-07-31`
- Journal: Frontiers in Chemistry
- Link: https://doi.org/10.3389/fchem.2026.1894425
- Tags: active_learning, alloy, catalysis, catalyst_descriptor, dft, generative_model, gnn, h2, high_throughput, ml, review, water
- Authors: Vamsi Krishna Kudapa, Shoaib Mohd, Vijayakumar Sivasundar, Akanksha Mishra, Santosh Kumar Sahu
- Why it matters: First, the thermodynamic and kinetic principles of the hydrogen and oxygen evolution reactions are summarised, along with some well-adopted and accepted activity descriptors.
- Innovation: First, the thermodynamic and kinetic principles of the hydrogen and oxygen evolution reactions are summarised, along with some well-adopted and accepted activity descriptors.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints.
- MOF relevance: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.

### 2. Accelerating Catalyst Materials Discovery With Large Artificial Intelligence Models

- Date: `2026-02-17`
- Journal: Angewandte Chemie International Edition
- Link: https://doi.org/10.1002/anie.202526150
- Tags: active_learning, catalysis, foundation_model, h2, high_throughput, interatomic_potential, ml, multimodal, priority_journal
- Authors: Di Zhang, Yuanzheng Chen, Chuanyu Liu, Y. H. Liu, Hongliang Xin
- Why it matters: The integration of artificial intelligence (AI) into catalysis is fundamentally reshaping the research paradigm of catalyst discovery.
- Innovation: The integration of artificial intelligence (AI) into catalysis is fundamentally reshaping the research paradigm of catalyst discovery.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 3. Machine learning-accelerated inverse design of energy materials: A critical review of graph neural networks, physics-informed models, and generative AI for batteries, perovskite solar cells, and electrocatalysts

- Date: `2026-07-30`
- Journal: Next Materials
- Link: https://doi.org/10.1016/j.nxmate.2026.102969
- Tags: active_learning, battery, catalysis, crystal, dft, electrocatalysis, electrolyte, generative_model, gnn, h2, high_throughput, md, ml, perovskite, physics_informed, review, uncertainty
- Authors: Ignatius Echezona Ekengwu, Bonaventure Onyeka Ekengwu
- Why it matters: The global urgency to transition away from fossil fuels has placed extraordinary pressure on materials scientists to deliver breakthroughs in energy storage, solar energy conversion, and electrocatalysis — and to deliver them faster than the conventional trial-and-error research cycle allows.
- Innovation: The global urgency to transition away from fossil fuels has placed extraordinary pressure on materials scientists to deliver breakthroughs in energy storage, solar energy conversion, and electrocatalysis — and to deliver them faster than the conventional trial-and-error research cycle allows.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 4. Boosting Computational Catalysis and Chemical Reactivity with Artificial Intelligence

- Date: `2026-02-20`
- Journal: Journal of the American Chemical Society
- Link: https://doi.org/10.1021/jacs.5c17786
- Tags: catalysis, foundation_model, generative_model, interatomic_potential, ml, priority_journal, review, separation
- Authors: Konstantinos D. Vogiatzis, Clémence Corminbœuf, Ainara Nova, Kjell Jorner, Johannes Kästner
- Why it matters: Artificial intelligence (AI) and machine learning (ML) are rapidly reshaping the landscape of computational chemistry, offering new opportunities for accelerating catalyst discovery and deepening our understanding of chemical reactivity.
- Innovation: Artificial intelligence (AI) and machine learning (ML) are rapidly reshaping the landscape of computational chemistry, offering new opportunities for accelerating catalyst discovery and deepening our understanding of chemical reactivity.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 5. Kinetic Isotope Effects in CO 2 Reduction: Insights Into Reaction Mechanisms

- Date: `2026-09-14`
- Journal: Advanced Energy Materials
- Link: https://doi.org/10.1002/aenm.71591
- Tags: catalysis, co2, electrocatalysis, h2, oxide, priority_journal, review, separation, uncertainty, water
- Authors: Xuemei Diao, Yiyang Li, Xiaowei Zhang, Xiubing Huang, PENG WANG
- Why it matters: ABSTRACT Electrochemical and photochemical carbon dioxide reduction reactions (CO 2 RR) represent pivotal strategies for converting CO 2 into valuable chemicals, yet their multistep pathways and transient intermediates complicate the identification of the rate‐determining step (RDS).
- Innovation: ABSTRACT Electrochemical and photochemical carbon dioxide reduction reactions (CO 2 RR) represent pivotal strategies for converting CO 2 into valuable chemicals, yet their multistep pathways and transient intermediates complicate the identification of the rate‐determining step (RDS).
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Catalytic conclusions are likely thermodynamics-heavy unless kinetics or explicit environment are included.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 6. High-Entropy Catalysts for Lithium-Sulfur and Room-Temperature Sodium-Sulfur Batteries: Electronic Descriptors, Performance, and Design Challenges

- Date: `2026-09-14`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15008811/v1
- Tags: adsorption, alloy, battery, catalysis, catalyst_descriptor, dft, ml, oxide, review
- Authors: Nusrat Jahan Hridita, Md. Safin Mahmood Shomyo
- Why it matters: This review is organized around the electronic descriptors, principally the d-band center and its refinements, that are used to connect multi-element composition to polysulfide adsorption and to reaction barriers.
- Innovation: This review is organized around the electronic descriptors, principally the d-band center and its refinements, that are used to connect multi-element composition to polysulfide adsorption and to reaction barriers.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.

### 7. Harnessing Artificial Intelligence (AI) for a greener future: a review of AI advancements in green chemistry, chemical processes and sustainable materials

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

### 8. AI-Driven Optimization of Electrochemical Fertilizer Processes

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

### 9. A multimodal semantic learning framework for data-driven discovery of nitrate-to-ammonia electrocatalysts

- Date: `2026-09-15`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02327-z
- Tags: catalysis, h2, ml, multimodal, priority_journal, separation
- Authors: Jiajia Liu, Yuying Jiang, Ran Ma, Zhenhui Ma, Shuren Wang
- Why it matters: Here, we present a multimodal artificial intelligence (AI) framework, the Material Semantics Network (MatSemNet), which learns materials semantics by integrating textual, numerical, and reaction pathway information extracted from the literature.
- Innovation: Here, we present a multimodal artificial intelligence (AI) framework, the Material Semantics Network (MatSemNet), which learns materials semantics by integrating textual, numerical, and reaction pathway information extracted from the literature.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Catalytic conclusions are likely thermodynamics-heavy unless kinetics or explicit environment are included.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 10. Reliability assessment of machine learning models for single-atom alloy catalyst screening: A chemistry-aware validation framework for methane C–H activation barrier prediction

- Date: `2026-09-08`
- Journal: Computational Materials Today
- Link: https://doi.org/10.1016/j.commt.2026.100065
- Tags: alloy, catalysis, dft, h2, high_throughput, ml, uncertainty
- Authors: Md. Atik Faisal, Md. Amanullah Asif, Md. Shamim Al Razi, Mahbir Ahmed Maheen, Ahmed Sharif
- Why it matters: Single-atom alloy (SAA) catalysts are promising for methane C–H activation, but density-functional-theory (DFT) screening of the host–dopant–surface space is intractable, motivating machine-learning (ML) surrogates.
- Innovation: Single-atom alloy (SAA) catalysts are promising for methane C–H activation, but density-functional-theory (DFT) screening of the host–dopant–surface space is intractable, motivating machine-learning (ML) surrogates.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 11. Machine Learning for High-Entropy Catalysts: Methods and Applications

- Date: `2026-09-17`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2609.19837
- Tags: alloy, catalysis, foundation_model, h2, ml, review
- Authors: Hao Chen, Zongrui Pei, Xianglin Liu
- Why it matters: High-entropy alloys (HEAs) exhibit exceptional catalytic performance in various reactions due to their high configurational entropy, synergistic elemental effects, tunable electronic structures, and excellent structural stability.
- Innovation: High-entropy alloys (HEAs) exhibit exceptional catalytic performance in various reactions due to their high configurational entropy, synergistic elemental effects, tunable electronic structures, and excellent structural stability.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 12. Fine-tuning large language models to generate single-atom catalyst synthesis procedures

- Date: `2026-06-19`
- Journal: Communications Chemistry
- Link: https://doi.org/10.1038/s42004-026-02046-y
- Tags: catalysis, foundation_model, h2, review, transfer_learning
- Authors: Manu Suvarna, Matteo Manica, Fillipo Ficarra, Andres M Bran, Andrea Ruiz‐Ferrando
- Why it matters: We demonstrate the model's practicality through a user interface allowing researchers to query procedures tailored to their design conditions.
- Innovation: We demonstrate the model's practicality through a user interface allowing researchers to query procedures tailored to their design conditions.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Catalytic conclusions are likely thermodynamics-heavy unless kinetics or explicit environment are included.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 13. Data-Driven Exploration of Literature-Derived Catalyst and Reaction Spaces for the Vapor-Phase Aldol Condensation of Acetate with Formaldehyde

- Date: `2026-09-17`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15008977/v1
- Tags: catalysis, h2, high_throughput, ml, oxide, polymer, symbolic_regression, transfer_learning
- Authors: Simon Verstraeten, Yayati Naresh Palai, Ekaterina V. Makshina, Bert F. Sels
- Why it matters: Herein, we demonstrate a robust approach for extracting mechanistic insights from such challenging datasets using interpretable machine learning.
- Innovation: Herein, we demonstrate a robust approach for extracting mechanistic insights from such challenging datasets using interpretable machine learning.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 14. A Catalyst Discovery Workflow Coupling MLIP with MOBO for Nitrite-to-Hydroxylamine Electroreduction

- Date: `2026-09-23`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15009355/v1
- Tags: active_learning, adsorption, catalysis, electrocatalysis, h2, high_throughput, interatomic_potential, ml, oxide, separation, surrogate_model, water
- Authors: Zhiyi Yu, Huaiwen Zhang, Weiming Zhao
- Why it matters: The selectivity of electrocatalytic nitrite reduction to hydroxylamine is governed by multiple coupled steps within the multi-electron nitrogen–oxygen reduction network, which cannot be represented simultaneously by a volcano relation based on a single adsorption descriptor.
- Innovation: The selectivity of electrocatalytic nitrite reduction to hydroxylamine is governed by multiple coupled steps within the multi-electron nitrogen–oxygen reduction network, which cannot be represented simultaneously by a volcano relation based on a single adsorption descriptor.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 15. Ioc-Mldroid: a Hybrid Approach for Detection of Android Based Malicious Applications Using Indicators of Compromise (Iocs) and Machine Learning

- Date: `2027-06-15`
- Journal: i-manager's Journal on Computer Science
- Link: https://doi.org/10.26634/jcom.14.1.1372
- Tags: h2, ml, surrogate_model
- Authors: V VENKATESWARA RAO
- Why it matters: Android operating system has taken over the mobile ecosystem across the world and thus is a prime target of more advanced malware that uses its ability to obfuscate, dynamically load code, encrypted communications and even environment aware evasion behaviors.
- Innovation: Android operating system has taken over the mobile ecosystem across the world and thus is a prime target of more advanced malware that uses its ability to obfuscate, dynamically load code, encrypted communications and even environment aware evasion behaviors.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 16. High-throughput screening of CuS-based single-atom catalysts for methanol oxidation reaction

- Date: `2026-09-23`
- Journal: Journal of the Taiwan Institute of Chemical Engineers
- Link: https://doi.org/10.1016/j.jtice.2026.107012
- Tags: adsorption, catalysis, dft, electrocatalysis, h2, high_throughput, separation, uncertainty
- Authors: Junhui Luo, Bo Xiong, Lei Hong, Mengjun Chen, Ying Wang
- Why it matters: Background Methanol electro-oxidation (MOR) plays a critical role in direct methanol fuel cells, yet its sluggish kinetics demands the rational design of efficient electrocatalysts with high activity and tunable pathway selectivity.
- Innovation: Background Methanol electro-oxidation (MOR) plays a critical role in direct methanol fuel cells, yet its sluggish kinetics demands the rational design of efficient electrocatalysts with high activity and tunable pathway selectivity.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 17. Machine‐Learning‐Powered Screening of CuNi@FeO Electrocatalyst for Nitrate‐to‐Ammonia Conversion in Industrial Wastewater Concentrate

- Date: `2026-09-22`
- Journal: Advanced Functional Materials
- Link: https://doi.org/10.1002/adfm.78621
- Tags: catalysis, crystal, electrocatalysis, h2, high_throughput, ml, symbolic_regression
- Authors: Yongxin Wang, Yuanxin Yang, Mengxin Huang, Shiguang Zhang, Carlos Alberto Martínez-Huitle
- Why it matters: Herein we developed a literature‐informed interpretable machine learning (ML) framework to screen the CuNi@FeO electrocatalyst toward highly selective nitrate‐to‐ammonia conversion under high‐salinity conditions.
- Innovation: Herein we developed a literature‐informed interpretable machine learning (ML) framework to screen the CuNi@FeO electrocatalyst toward highly selective nitrate‐to‐ammonia conversion under high‐salinity conditions.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Add kinetics, explicit environment effects, and active-site reconstruction checks. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 18. Multi-Task Graph Neural Network Predictions of Auger-Electron and X-ray Photoelectron Spectroscopy

- Date: `2026-09-14`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2609.16339
- Tags: gnn, h2, ml, photocatalysis, uncertainty
- Authors: Adam E. A. Fouda, Patrick Phillips, Phay J. Ho
- Why it matters: Here we demonstrate that the physical connection, and thus inter-task relationship, between the generation of a core-hole and its corresponding Auger-Meitner decay enables inductive knowledge transfer through the training of a multi-task graph neural network to predict both observables from a common graph embedding.
- Innovation: Here we demonstrate that the physical connection, and thus inter-task relationship, between the generation of a core-hole and its corresponding Auger-Meitner decay enables inductive knowledge transfer through the training of a multi-task graph neural network to predict both observables from a common graph embedding.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 19. A green solvent screening tool for emerging materials via uncertainty aware, transformer enhanced transfer learning

- Date: `2026-06-11`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.13060
- Tags: battery, catalysis, h2, high_throughput, ml, transfer_learning, uncertainty
- Authors: Ioannis Kouroudis, Simon Ternes, Zhaosu Gu, Gohar Ali Siddiqui, Marina Ustinova
- Why it matters: Overall, we augment data on solubility descriptors by orders of magnitude with high quality predictions.
- Innovation: Overall, we augment data on solubility descriptors by orders of magnitude with high quality predictions.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 20. DASyR-LLM: Domain-Aware Symbolic Regression with LLMs for Kinetic Model Discovery

- Date: `2026-08-05`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2608.05120
- Tags: catalysis, foundation_model, h2, ml, symbolic_regression
- Authors: Roberto Aliaga Medina, Paulina Quintanilla, Ehecatl Antonio del Rio‐Chanona
- Why it matters: Here, we introduce an LLM-guided SR framework, embedding an LLM module within an iterative SR algorithm for automated kinetic model discovery.
- Innovation: Here, we introduce an LLM-guided SR framework, embedding an LLM module within an iterative SR algorithm for automated kinetic model discovery.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 21. A data-efficient reactive machine learning potential to accelerate automated exploration of complex reaction networks

- Date: `2026-01-12`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv-2025-sm7f3-v2
- Tags: active_learning, high_throughput, interatomic_potential, md, ml, separation
- Authors: Guoao Li, Haobo Ling, Chaoxu Su, Zhengxuan Liu, G. H. Wang
- Why it matters: Reactive machine learning potentials (MLPs) significantly benefits high-throughput exploration of complex reaction networks.
- Innovation: Reactive machine learning potentials (MLPs) significantly benefits high-throughput exploration of complex reaction networks.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 22. An Autonomous Platform for Reticular Materials Discovery

- Date: `2026-05-01`
- Journal: eScholarship (California Digital Library)
- Link: https://escholarship.org/uc/item/2tk455m3
- Tags: active_learning, cof, crystal, generative_model, h2, high_throughput, image_analysis, ml, mof, separation, uncertainty
- Authors: Zichao Rong
- Why it matters: To address this limitation, this dissertation introduces an autonomous platform, termed Algorithmic Iterative Reticular Synthesis (AIRES), which integrates high-throughput experimentation and machine learning to identify correlations between successful crystallization outcomes, building block properties, and reaction parameters and therefore to accelerate the discovery of new reticular materials.
- Innovation: To address this limitation, this dissertation introduces an autonomous platform, termed Algorithmic Iterative Reticular Synthesis (AIRES), which integrates high-throughput experimentation and machine learning to identify correlations between successful crystallization outcomes, building block properties, and reaction parameters and therefore to accelerate the discovery of new reticular materials.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Map the method onto MOF structure images, spectra, isotherm curves, or generated-structure consistency checks. Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 23. AI-assisted multi-objective optimization of Ni anode microstructure for enhanced electrochemical performance and long-term stability of solid oxide fuel cells

- Date: `2026-09-20`
- Journal: Electrochemistry Communications
- Link: https://doi.org/10.1016/j.elecom.2026.108256
- Tags: battery, electrocatalysis, h2, ml, oxide, surrogate_model
- Authors: Mohamed S. Shaban, As’ad Alizadeh, Rashed Abu Hammour, Kamal Sharma, Safi Alshammari
- Why it matters: Nickel (Ni) agglomeration in porous anodes is a major microstructural degradation mechanism that progressively deteriorates the electrochemical performance and long-term durability of anode-supported solid oxide fuel cells (SOFCs).
- Innovation: Nickel (Ni) agglomeration in porous anodes is a major microstructural degradation mechanism that progressively deteriorates the electrochemical performance and long-term durability of anode-supported solid oxide fuel cells (SOFCs).
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 24. From non-centrosymmetry to surface Janus design: Sparse GW/BSE learning for excitonic two-dimensional photocatalysis candidates

- Date: `2026-09-10`
- Journal: Chimica Techno Acta
- Link: https://doi.org/10.15826/chimtech.10339
- Tags: catalysis, crystal, h2, high_throughput, photocatalysis, separation, uncertainty
- Authors: Hao Yu, Yongai Sun, Zishang Chen, Xiaowei Fan
- Why it matters: Here we develop a boundary-aware C2DB workflow that integrates structural surface classification, sparse GW/BSE label completion, formula-group validation, uncertainty-aware band-edge screening, and candidate audit.
- Innovation: Here we develop a boundary-aware C2DB workflow that integrates structural surface classification, sparse GW/BSE label completion, formula-group validation, uncertainty-aware band-edge screening, and candidate audit.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 25. Hierarchical Multi-Fidelity Learning for Predicting Three-Dimensional Flame Wrinkling and Turbulent Burning Velocity

- Date: `2026-05-06`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2605.08232
- Tags: h2, md, ml, separation, surrogate_model
- Authors: Saghar Zolfaghari, Yu Xie, Junfeng Yang, Safa Jamali
- Why it matters: Here, we develop a hierarchical multi-fidelity neural network framework (MuFiNNs) to address this challenge by integrating sparse high-fidelity experimental data with structured low-fidelity representations encoding dominant physical trends.
- Innovation: Here, we develop a hierarchical multi-fidelity neural network framework (MuFiNNs) to address this challenge by integrating sparse high-fidelity experimental data with structured low-fidelity representations encoding dominant physical trends.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 26. Artificial intelligence-driven platform for catalytic reactor discovery and optimization applied to carbon dioxide valorization

- Date: `2025-02-20`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv-2025-3gstc
- Tags: active_learning, co2, high_throughput, ml, oxide
- Authors: Cristopher Tinajero, Marcileia Zanatta, Eduardo García‐Verdugo, Víctor Sans
- Why it matters: It integrates the parametric design and analysis of advanced structures from mathematic models (Reac-Gen), the high-resolution 3D printing and functionalization of catalytic reactors (Reac-Fab) with an algorithm that validates the printability of reactor designs and a self-driving laboratory platform (Reac-Eval) capable of parallel multi-reactor evaluations featuring real-time NMR monitoring and machine learning (ML) simultaneous optimization of process parameters and topologic descriptors.
- Innovation: It integrates the parametric design and analysis of advanced structures from mathematic models (Reac-Gen), the high-resolution 3D printing and functionalization of catalytic reactors (Reac-Fab) with an algorithm that validates the printability of reactor designs and a self-driving laboratory platform (Reac-Eval) capable of parallel multi-reactor evaluations featuring real-time NMR monitoring and machine learning (ML) simultaneous optimization of process parameters and topologic descriptors.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 27. Expanding frontiers of complex reaction network exploration through a general reactive machine learning potential

- Date: `2025-05-29`
- Journal: Research Square
- Link: https://doi.org/10.21203/rs.3.rs-6458754/v1
- Tags: interatomic_potential, ml
- Authors: Shuhua Li, Guoao Li, Haobo Ling, Guoqiang Wang, Manyi Yang
- Why it matters: Expanding frontiers of complex reaction network exploration through a general reactive machine learning potential
- Innovation: Expanding frontiers of complex reaction network exploration through a general reactive machine learning potential
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.
