# Literature Update

- Generated: `2026-11-09T07:54:57`
- Profile: `reaction_catalyst_ml_transfer`
- Since: `2016-11-11`
- Papers retained: `28`

## Overview

Collected 28 deduplicated papers for profile `reaction_catalyst_ml_transfer`. This transfer profile keeps non-MOF ML papers when they carry a concrete method signal; 28 retained papers are outside direct MOF literature. 28 papers contain transferable method tags and 6 appear in priority journals or major venue families. 21 papers also carry explicit material-system tags, helping judge whether the chemistry is close enough to MOFs.

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

### 1. Accelerating Catalyst Materials Discovery With Large Artificial Intelligence Models

- Date: `2026-02-17`
- Journal: Angewandte Chemie International Edition
- Link: https://doi.org/10.1002/anie.202526150
- Tags: active_learning, catalysis, foundation_model, h2, high_throughput, interatomic_potential, ml, multimodal, priority_journal, review
- Authors: Di Zhang, Yuanzheng Chen, Chuanyu Liu, Y. H. Liu, Hongliang Xin
- Why it matters: The integration of artificial intelligence (AI) into catalysis is fundamentally reshaping the research paradigm of catalyst discovery.
- Innovation: The integration of artificial intelligence (AI) into catalysis is fundamentally reshaping the research paradigm of catalyst discovery.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 2. Unveiling catalytic microenvironments: the convergence of conventional computations and machine learning paradigms

- Date: `2026-11-06`
- Journal: AI Agent
- Link: https://doi.org/10.20517/aiagent.2026.24
- Tags: adsorption, battery, catalysis, crystal, dft, electrocatalysis, electrolyte, foundation_model, h2, interatomic_potential, md, ml, review, symbolic_regression
- Authors: Xiansheng Yu, Letian Chen, Xu Hu, Fengjuan Chen, Xu Zhang
- Why it matters: Third, interpretable machine learning and symbolic regression are emerging as tools for identifying physically meaningful descriptors that connect local structural and electronic microenvironments with catalytic activity.
- Innovation: Third, interpretable machine learning and symbolic regression are emerging as tools for identifying physically meaningful descriptors that connect local structural and electronic microenvironments with catalytic activity.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 3. From Atoms to Reactors: A Critical Review of a Decade of Machine Learning in Heterogeneous Catalysis (2017–2026)

- Date: `2026-10-23`
- Journal: Angewandte Chemie International Edition
- Link: https://doi.org/10.1002/anie.4288841
- Tags: active_learning, adsorption, catalysis, dft, foundation_model, h2, ml, priority_journal, review, water, zeolite
- Authors: Rafael Larraz, Avelino Corma
- Why it matters: ABSTRACT This critical review traces the evolution of machine learning (ML) across the full value chain of heterogeneous catalysis over 2017–2026, from catalyst discovery to reactor and process design, and across the principal reaction families (CO 2 reduction, water splitting, nitrogen chemistry, zeolite‐catalyzed transformations).
- Innovation: ABSTRACT This critical review traces the evolution of machine learning (ML) across the full value chain of heterogeneous catalysis over 2017–2026, from catalyst discovery to reactor and process design, and across the principal reaction families (CO 2 reduction, water splitting, nitrogen chemistry, zeolite‐catalyzed transformations).
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 4. Machine learning-accelerated inverse design of energy materials: A critical review of graph neural networks, physics-informed models, and generative AI for batteries, perovskite solar cells, and electrocatalysts

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

### 5. Boosting Computational Catalysis and Chemical Reactivity with Artificial Intelligence

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

### 6. Machine Learning for Synthetic Organic Chemistry: Methods, Applications, and Best Practices

- Date: `2026-08-28`
- Journal: Angewandte Chemie Novit
- Link: https://doi.org/10.1002/anov.70032
- Tags: foundation_model, h2, ml, priority_journal, review
- Authors: Niklas Hölter, Felix Katzenburg, Florian Boser, Frank Glorius
- Why it matters: ABSTRACT The growing integration of artificial intelligence (AI) and machine learning (ML) is transforming experimental chemistry laboratories.
- Innovation: ABSTRACT The growing integration of artificial intelligence (AI) and machine learning (ML) is transforming experimental chemistry laboratories.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 7. A New Paradigm for Computational Chemistry

- Date: `2026-10-20`
- Journal: Journal of the American Chemical Society
- Link: https://doi.org/10.1021/jacs.6c06653
- Tags: dft, h2, interatomic_potential, ml, priority_journal
- Authors: Raphael T. Husistein, Markus Reiher
- Why it matters: Computational chemistry has become an indispensable tool for generating data and insights, pervading all branches of experimental chemistry.
- Innovation: Computational chemistry has become an indispensable tool for generating data and insights, pervading all branches of experimental chemistry.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.

### 8. Reproducibility, Benchmarks, and Mechanistic Diversity: Building Trust in Computational Electrocatalysis for the AI Era

- Date: `2026-11-04`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15011651/v1
- Tags: catalysis, catalyst_descriptor, electrocatalysis, h2, high_throughput, review
- Authors: David Hernández‐Castillo, Kai Steffen Exner
- Why it matters: We examine the roles of surface structure, coverage, stability, mechanistic breadth, and descriptor choice under operating bias, and propose modular benchmarks spanning numerical verification, surface chemistry, electrified interfaces, and mechanistic validation.
- Innovation: We examine the roles of surface structure, coverage, stability, mechanistic breadth, and descriptor choice under operating bias, and propose modular benchmarks spanning numerical verification, surface chemistry, electrified interfaces, and mechanistic validation.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.

### 9. Machine Learning‐Assisted Discovery of Unconventional Molybdenum Nitride Nano‐Facets as Hydrogen Evolution Electrocatalysts

- Date: `2026-10-29`
- Journal: Small Methods
- Link: https://doi.org/10.1002/smtd.71163
- Tags: catalysis, dft, h2, ml, priority_journal, uncertainty
- Authors: Xutao Gao, Chun Kit Chan, Eric Pok Man Kan, Edmund C. M. Tse
- Why it matters: To accelerate the identification of energetically favourable high‐Miller‐index facets of Mo nitrides, we complement our DFT approach with a machine learning (ML) model trained on computed results for low‐Miller‐index facets.
- Innovation: To accelerate the identification of energetically favourable high‐Miller‐index facets of Mo nitrides, we complement our DFT approach with a machine learning (ML) model trained on computed results for low‐Miller‐index facets.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 10. Accelerating sustainable energy storage and conversion with AI and ML: A perspective on emerging directions

- Date: `2026-11-03`
- Journal: MRS Energy & Sustainability
- Link: https://doi.org/10.1557/s43581-026-00171-8
- Tags: active_learning, battery, catalysis, h2, ml, review, uncertainty
- Authors: G. Giannopoulos, Manish Chhowalla, Anja Bielefeld, Miaofang Chi, Yury Gogotsi
- Why it matters: Achieving global decarbonization goals by 2050 demands rapid progress in renewable energy and energy storage and conversion technologies.
- Innovation: Achieving global decarbonization goals by 2050 demands rapid progress in renewable energy and energy storage and conversion technologies.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 11. Assessing the Transferability of General-Purpose MachineLearning Interatomic Potentials for Heterogeneous Catalysis with HetCat26

- Date: `2026-09-24`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2609.30621
- Tags: adsorption, catalysis, dft, equivariant_ml, foundation_model, h2, high_throughput, interatomic_potential, ml, oxide
- Authors: Alexandre Peuch, Giaan Kler-Young, Kaifeng Niu, Jinwoo Hwang, Manos Mavrikakis
- Why it matters: Here, we introduce HetCat26, a collection of benchmark tests designed to assess pre-trained MLIPs across key aspects of catalytic modeling, including surface energetics, metal-metal oxide interactions, adsorption, and catalytic reaction networks.
- Innovation: Here, we introduce HetCat26, a collection of benchmark tests designed to assess pre-trained MLIPs across key aspects of catalytic modeling, including surface energetics, metal-metal oxide interactions, adsorption, and catalytic reaction networks.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 12. Accelerating green heterocyclic synthesis: Convergence of AI , automation, and sustainable chemistry

- Date: `2026-10-14`
- Journal: Bulletin of the Korean Chemical Society
- Link: https://doi.org/10.1002/bkcs.70227
- Tags: equivariant_ml, ml, review, uncertainty
- Authors: Noor Aisyah Ahmad Shah, Amirreza Mottafegh, Su‐Hyun Yoo, Jongwoon Kim, Minseon Byeon
- Why it matters: Abstract Heterocyclic compounds are among the most prevalent scaffolds in bioactive molecules, with approximately 82% of small‐molecule drugs approved by the US Food and Drug Administration (FDA) during 2013–2023 containing nitrogen heterocycles.
- Innovation: Abstract Heterocyclic compounds are among the most prevalent scaffolds in bioactive molecules, with approximately 82% of small‐molecule drugs approved by the US Food and Drug Administration (FDA) during 2013–2023 containing nitrogen heterocycles.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 13. High‐Throughput Design of Efficient Dual‐Atom Catalysts Anchored on C 2 N for Electroreduction of CO and NH 3 to Acetamide via Atomic Modeling and Machine Learning

- Date: `2026-11-01`
- Journal: Rare Metals
- Link: https://doi.org/10.1002/rar2.70713
- Tags: catalysis, catalyst_descriptor, co2, dft, electrocatalysis, h2, high_throughput, ml, oxide, separation, symbolic_regression
- Authors: Haonan Li, Xinhu Liang, Yibing Yang, Xiao Yang, Yi Xiao
- Why it matters: Machine learning is adopted to explore the structure–activity relationship of the identified DACs, and the sure independence screening and sparsifying operator method is employed to construct a robust descriptor system, enabling accurate prediction of the maximum uphill Gibbs free‐energy change among the elementary steps of a given reaction pathway (Δ G max , eV).
- Innovation: Machine learning is adopted to explore the structure–activity relationship of the identified DACs, and the sure independence screening and sparsifying operator method is employed to construct a robust descriptor system, enabling accurate prediction of the maximum uphill Gibbs free‐energy change among the elementary steps of a given reaction pathway (Δ G max , eV).
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.

### 14. Reactive Molecular Dynamics of Hydrogen Evolution at Charged Interfaces Using Effective Machine Learning Potentials

- Date: `2026-10-30`
- Journal: ACS electrochemistry.
- Link: https://doi.org/10.1021/acselectrochem.6c00310
- Tags: catalysis, dft, electrocatalysis, equivariant_ml, h2, interatomic_potential, md, ml, separation, two_d_material, water
- Authors: Md Sharif Khan, Oliviero Andreussi
- Why it matters: Here, we develop an equivariant machine-learning interatomic potential trained on density functional theory data for electrochemically activated MoS2/water interfaces under charged conditions.
- Innovation: Here, we develop an equivariant machine-learning interatomic potential trained on density functional theory data for electrochemically activated MoS2/water interfaces under charged conditions.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 15. A green solvent screening tool for emerging materials via uncertainty aware, transformer enhanced transfer learning

- Date: `2026-09-28`
- Journal: Scientific Reports
- Link: https://doi.org/10.1038/s41598-026-72415-z
- Tags: battery, catalysis, h2, high_throughput, ml, transfer_learning, uncertainty
- Authors: Ioannis Kouroudis, Simon Ternes, Zhaosu Gu, Gohar Ali Siddiqui, Marina Ustinova
- Why it matters: Overall, we augment data on solubility descriptors by up to two orders of magnitude with high-quality predictions.
- Innovation: Overall, we augment data on solubility descriptors by up to two orders of magnitude with high-quality predictions.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 16. Cross-Adsorbate Scaling, Interpretable Machine Learning, and Adsorption Trade-Offs across M–N4–C Sites

- Date: `2026-11-03`
- Journal: Nano-electrochemistry & Nano-photochemistry
- Link: https://doi.org/10.53941/nenp.2026.100024
- Tags: adsorption, dft, h2, ml, symbolic_regression
- Authors: Simin Li, Bo Shen
- Why it matters: Gradient-boosting models evaluated by nested out-of-fold prediction recover descriptor-based signal for all three targets; *CO is predicted most accurately (R2 = 0.851; MAE = 0.272 eV), whereas *COOH and *CHO show moderate predictability.
- Innovation: Gradient-boosting models evaluated by nested out-of-fold prediction recover descriptor-based signal for all three targets; *CO is predicted most accurately (R2 = 0.851; MAE = 0.272 eV), whereas *COOH and *CHO show moderate predictability.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 17. Predicting Reactivity and Enantioselectivity from Small Experimental Datasets: A Case Study in Asymmetric Magnesium Catalysis

- Date: `2026-09-14`
- Journal: ACS Catalysis
- Link: https://doi.org/10.1021/acscatal.6c05090
- Tags: catalysis, h2, high_throughput, ml, separation, transfer_learning
- Authors: Paulina Baczewska, Damian Nowak, Joanna A. Jaszczewska‐Adamczak, Rafał Adam Bachorz, Marcin Hoffmann
- Why it matters: Using magnesium-catalyzed chalcone epoxidation and thia-Michael addition as experimentally grounded case studies, we developed a machine-learning workflow that combines reactivity classification, where appropriate, with enantioselectivity regression trained on internally consistent laboratory data.
- Innovation: Using magnesium-catalyzed chalcone epoxidation and thia-Michael addition as experimentally grounded case studies, we developed a machine-learning workflow that combines reactivity classification, where appropriate, with enantioselectivity regression trained on internally consistent laboratory data.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 18. Fine-tuning large language models to generate single-atom catalyst synthesis procedures

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

### 19. Generative Design and Graph Neural Network Screening of Novel Bimetallic Alloy Catalysts for the Hydrogen Evolution Reaction

- Date: `2026-10-30`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2610.41932
- Tags: adsorption, alloy, catalysis, dft, force_field, generative_model, gnn, h2, high_throughput, md, ml
- Authors: Vipin Kurian Elavunkel, Sylvain Le Tonquesse, Hadrien Vroylandt
- Why it matters: We present a computational pipeline that couples diffusion-based generative modelling, machine-learning force-field relaxation, and graph neural network (GNN) property prediction to discover bimetallic HER catalysts beyond the structures and stoichiometries covered by existing adsorption databases.
- Innovation: We present a computational pipeline that couples diffusion-based generative modelling, machine-learning force-field relaxation, and graph neural network (GNN) property prediction to discover bimetallic HER catalysts beyond the structures and stoichiometries covered by existing adsorption databases.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 20. Ioc-Mldroid: a Hybrid Approach for Detection of Android Based Malicious Applications Using Indicators of Compromise (Iocs) and Machine Learning

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

### 21. Theoretical Assessment of Hydrogen Evolution Reaction Activity on 3d, 4d, and 5d TM13 Transition-Metal Nanoclusters

- Date: `2026-10-31`
- Journal: ACS Omega
- Link: https://doi.org/10.1021/acsomega.6c08283
- Tags: adsorption, catalysis, catalyst_descriptor, dft, h2, high_throughput, md
- Authors: Antonio F. O. Santos, Juan Carlos Roldao, Pedro Ivo R. Moraes, Douglas Duarte de Vargas, Juarez L. F. Da Silva
- Why it matters: Here, density functional theory calculations quantify how structural and electronic descriptors control hydrogen binding on 13-atom transition-metal clusters.
- Innovation: Here, density functional theory calculations quantify how structural and electronic descriptors control hydrogen binding on 13-atom transition-metal clusters.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.

### 22. Ensemble Molecular Surface Electrostatic Potential Descriptors as Informative Features for Active Learning

- Date: `2026-11-03`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15011587/v1
- Tags: active_learning, catalysis, high_throughput, uncertainty
- Authors: Gian-Michele Cherchi, Tommaso Marchetti, Sijbren Otto, Robert Pollice
- Why it matters: General interaction properties function (GIPF) descriptors, which encode molecular surface electrostatic potential, are informative but usually computed by density functional approximations on individual structures, which is not only costly but also neglects conformational flexibility.
- Innovation: General interaction properties function (GIPF) descriptors, which encode molecular surface electrostatic potential, are informative but usually computed by density functional approximations on individual structures, which is not only costly but also neglects conformational flexibility.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 23. Literature-Scale Mössbauer Data Enable Prediction, Electronic-State Interpretation, and Chemical Insight in Molecular Iron Chemistry

- Date: `2026-11-02`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15011512/v1
- Tags: dft, foundation_model, h2, uncertainty
- Authors: Zhibo Zhang, Haoran Li, Fang‐Wei Lin, Xin-Lin Li, 黄凯 Huang Kai
- Why it matters: Using FeMössDB, we developed FeMössML for three complementary aspects of Mössbauer analysis: isomer-shift/quadrupole-splitting (IS/QS) prediction, electronic-state interpretation, and analysis of structure–state–spectroscopy relationships.
- Innovation: Using FeMössDB, we developed FeMössML for three complementary aspects of Mössbauer analysis: isomer-shift/quadrupole-splitting (IS/QS) prediction, electronic-state interpretation, and analysis of structure–state–spectroscopy relationships.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 24. DASyR-LLM: Domain-Aware Symbolic Regression with LLMs for Kinetic Model Discovery

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

### 25. Feature Selection in Multivariate Linear Regression Models for Data-Efficient Reaction Optimization

- Date: `2026-09-04`
- Journal: ACS Catalysis
- Link: https://doi.org/10.1021/acscatal.6c04292
- Tags: catalysis, h2, high_throughput, separation, transfer_learning
- Authors: Alexandre A. Schoepfer, Rubén Laplaza, Jérôme Waser, Clémence Corminbœuf
- Why it matters: Abstract We introduce NaviCat ReaFS (reaction feature selection), a framework for testing and supporting multivariate linear regression models for reaction optimization in small, heterogeneous datasets, where overfitting risk is high and additional experiments are costly.
- Innovation: Abstract We introduce NaviCat ReaFS (reaction feature selection), a framework for testing and supporting multivariate linear regression models for reaction optimization in small, heterogeneous datasets, where overfitting risk is high and additional experiments are costly.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility. Catalytic conclusions are likely thermodynamics-heavy unless kinetics or explicit environment are included.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 26. Chemical short-range order as a conditional modifier of deformation and damage in void-containing high-entropy alloys under high-strain-rate loading

- Date: `2026-11-02`
- Journal: Materials & Design
- Link: https://doi.org/10.1016/j.matdes.2026.117418
- Tags: alloy, h2, md, ml, surrogate_model
- Authors: Lei Wu, Haonan Sui, Qi Zhu, An-Min He, Heng-An Wu
- Why it matters: Chemical short-range order (SRO) can markedly affect the mechanical response of high-entropy alloys (HEAs), but its role in void-containing alloys under high-strain-rate loading remains unclear.
- Innovation: Chemical short-range order (SRO) can markedly affect the mechanical response of high-entropy alloys (HEAs), but its role in void-containing alloys under high-strain-rate loading remains unclear.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 27. Automated Exploration of Complex Reaction Networks Accelerated by a Data-Efficient Machine Learning Potential

- Date: `2025-10-30`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv-2025-sm7f3
- Tags: active_learning, catalysis, dft, h2, high_throughput, interatomic_potential, md, ml, separation
- Authors: Guoao Li, Haobo Ling, C. Joanna Su, Zhengxuan Liu, Guoqiang Wang
- Why it matters: Here we present an integrated molecular dynamics/coordinate driving-active learning (MD/CD-AL) framework that efficiently samples diverse reactive configurations to construct MDCD20, a curated dataset of ~1.4 million H/C/N/O structures with radical species covered.
- Innovation: Here we present an integrated molecular dynamics/coordinate driving-active learning (MD/CD-AL) framework that efficiently samples diverse reactive configurations to construct MDCD20, a curated dataset of ~1.4 million H/C/N/O structures with radical species covered.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 28. Expanding frontiers of complex reaction network exploration through a general reactive machine learning potential

- Date: `2025-05-29`
- Journal: Research Square
- Link: https://doi.org/10.21203/rs.3.rs-6458754/v1
- Tags: active_learning, force_field, h2, high_throughput, interatomic_potential, md, ml
- Authors: Shuhua Li, Guoao Li, Haobo Ling, Guoqiang Wang, Manyi Yang
- Why it matters: Here, we introduce an MD/CD-AL framework integrating molecular dynamics/coordinate driving (MD/CD) method with active learning to generate the MDCD20 dataset that encompasses diverse reactive configurations with up to 20 heavy atoms.
- Innovation: Here, we introduce an MD/CD-AL framework integrating molecular dynamics/coordinate driving (MD/CD) method with active learning to generate the MDCD20 dataset that encompasses diverse reactive configurations with up to 20 heavy atoms.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
