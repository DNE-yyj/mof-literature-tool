# Literature Update

- Generated: `2026-11-09T07:54:34`
- Profile: `materials_ml_transfer`
- Since: `2023-11-10`
- Papers retained: `30`

## Overview

Collected 30 deduplicated papers for profile `materials_ml_transfer`. This transfer profile keeps non-MOF ML papers when they carry a concrete method signal; 30 retained papers are outside direct MOF literature. 30 papers contain transferable method tags and 5 appear in priority journals or major venue families. 17 papers also carry explicit material-system tags, helping judge whether the chemistry is close enough to MOFs.

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

### 1. Computational Modeling of Electrolytes and the Solid–Electrolyte Interphase (SEI) in Li-Ion Batteries: A 30-Year Odyssey from DFT/MD/MC to AI–A Comprehensive Review

- Date: `2026-11-04`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15011695/v1
- Tags: active_learning, battery, dft, electrocatalysis, electrolyte, force_field, foundation_model, generative_model, h2, high_throughput, md, ml, physics_informed, review, uncertainty
- Authors: Ilya V. Chepkasov, Alexey Sergeevich Galushko, Viktor S. Baidyshev, Mikhail Khrizanforov, Vladimir Ya. Lee
- Why it matters: The review further examines ML applications—from property prediction and spectroscopic signature forecasting to MLIPs achieving first-principles accuracy at classical force-field speeds, generative molecular design, high-throughput screening, active learning, and integration with autonomous experimentation.
- Innovation: The review further examines ML applications—from property prediction and spectroscopic signature forecasting to MLIPs achieving first-principles accuracy at classical force-field speeds, generative molecular design, high-throughput screening, active learning, and integration with autonomous experimentation.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 2. OptiMat Alloys: a FAIR-aligned living database of multi-principal element alloys enabled by a conversational agent

- Date: `2026-11-04`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02377-3
- Tags: alloy, foundation_model, high_throughput, interatomic_potential, ml, priority_journal, uncertainty
- Authors: Yang Hu, Vladyslav Turlo
- Why it matters: We present OptiMat Alloys, a large language model-powered conversational agent for multi-principal element alloy exploration.
- Innovation: We present OptiMat Alloys, a large language model-powered conversational agent for multi-principal element alloy exploration.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 3. Machine learning-driven inverse design of high-hardness multi-principal element alloys through symbolic regression

- Date: `2026-10-23`
- Journal: Scientific Reports
- Link: https://doi.org/10.1038/s41598-026-74491-7
- Tags: active_learning, alloy, generative_model, h2, high_throughput, ml, physics_informed, separation, surrogate_model, symbolic_regression
- Authors: Peiyi Li
- Why it matters: A comprehensive descriptor library is constructed by integrating elemental fractions, pymatgen-derived atomic physicochemical properties and classical Hume-Rothery metallurgical parameters, which quantitatively captures lattice distortion, electronic effects and phase transformation mechanisms governing alloy hardness.
- Innovation: A comprehensive descriptor library is constructed by integrating elemental fractions, pymatgen-derived atomic physicochemical properties and classical Hume-Rothery metallurgical parameters, which quantitatively captures lattice distortion, electronic effects and phase transformation mechanisms governing alloy hardness.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 4. Machine Learning for Predicting Dielectric Energy-Storage Properties of Perovskite Oxides

- Date: `2026-11-03`
- Journal: Applied and Computational Engineering
- Link: https://doi.org/10.54254/2755-2721/2027.md38630
- Tags: equivariant_ml, generative_model, gnn, h2, ml, multimodal, oxide, perovskite, review
- Authors: Gengyu Liu
- Why it matters: The works are compared along the evolution of methods, from manual descriptors and ensemble learning to graph neural networks, small-sample strategies, and generative inverse design, with dataset size, verification level, and accuracy documented.
- Innovation: The works are compared along the evolution of methods, from manual descriptors and ensemble learning to graph neural networks, small-sample strategies, and generative inverse design, with dataset size, verification level, and accuracy documented.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 5. Empirical and physics-based computational approaches to explosive power, brisance, and underwater detonation response: A critical review with selected machine-learning applications

- Date: `2026-11-02`
- Journal: Next Materials
- Link: https://doi.org/10.1016/j.nxmate.2026.103938
- Tags: active_learning, h2, ml, physics_informed, review, surrogate_model, uncertainty
- Authors: Mohammad Hossein Keshavarz
- Why it matters: ML studies are included where they directly inform the reviewed domains, including QSPR/read-across estimation of thermochemical properties, prediction of density and detonation descriptors, and surrogate modeling of underwater fluid or structural response.
- Innovation: ML studies are included where they directly inform the reviewed domains, including QSPR/read-across estimation of thermochemical properties, prediction of density and detonation descriptors, and surrogate modeling of underwater fluid or structural response.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 6. Scope, Challenges, and Future of Agentic AI in Geotechnical and Earthquake Engineering: A Critical Review

- Date: `2026-11-04`
- Journal: Bulletin of Computational Intelligence
- Link: https://doi.org/10.53941/bci.2026.100016
- Tags: active_learning, foundation_model, generative_model, h2, ml, physics_informed, review, uncertainty
- Authors: Ishwor Thapa, Rojan Subedi, Garima Shrestha, Sundar Adhikari, Pratik Rana Magar
- Why it matters: Agentic artificial intelligence (agentic AI) refers to systems that pursue goals by planning, invoking external tools, maintaining memory and acting on the results with a defined degree of autonomy.
- Innovation: Agentic artificial intelligence (agentic AI) refers to systems that pursue goals by planning, invoking external tools, maintaining memory and acting on the results with a defined degree of autonomy.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 7. Unveiling catalytic microenvironments: the convergence of conventional computations and machine learning paradigms

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

### 8. From Atoms to Reactors: A Critical Review of a Decade of Machine Learning in Heterogeneous Catalysis (2017–2026)

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

### 9. Physics-informed Bayesian optimization for quantitative high-resolution transmission electron microscopy

- Date: `2026-11-04`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02364-8
- Tags: active_learning, crystal, physics_informed, priority_journal
- Authors: Xiankang Tang, Yixuan Zhang, Juri Barthel, Chun-Lin Jia, Rafal E. Dunin-Borkowski
- Why it matters: Using a BaTiO 3 single crystal that contains heavy, medium, and light elements as a model system, we demonstrate that the three-dimensional crystal structure can be determined from a single HRTEM image with a three- to four-order-of-magnitude improvement in time efficiency.
- Innovation: Using a BaTiO 3 single crystal that contains heavy, medium, and light elements as a model system, we demonstrate that the three-dimensional crystal structure can be determined from a single HRTEM image with a three- to four-order-of-magnitude improvement in time efficiency.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 10. Data-driven discovery of water-splitting electrocatalysts: From predictive machine learning to autonomous optimization

- Date: `2026-10-23`
- Journal: Artificial Intelligence Chemistry
- Link: https://doi.org/10.1016/j.aichem.2026.100136
- Tags: active_learning, adsorption, catalysis, h2, ml, physics_informed
- Authors: Mahalakshmi Vedanarayanan, Chandrasekaran Pitchai, Chia‐Yu Chen, Utkarsh Kumar, Liu Heng-Jui
- Why it matters: By integrating physically meaningful descriptors with predictive algorithms, ML provides a pathway to accelerate catalyst optimization and uncover underlying reaction mechanisms.
- Innovation: By integrating physically meaningful descriptors with predictive algorithms, ML provides a pathway to accelerate catalyst optimization and uncover underlying reaction mechanisms.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 11. Next-generation process monitoring and control for metal additive manufacturing: toward a physics-informed digital twin framework

- Date: `2026-11-06`
- Journal: Virtual and Physical Prototyping
- Link: https://doi.org/10.1080/17452759.2026.2751873
- Tags: active_learning, ml, physics_informed, review, surrogate_model
- Authors: Kunpeng Zhu, Yangkun Mao, Qi Zhou, Jiawei Yan, Jiangge Deng
- Why it matters: Metal additive manufacturing (MAM) enables fabrication of geometrically complex components but faces process-induced defects that undermine quality consistency.
- Innovation: Metal additive manufacturing (MAM) enables fabrication of geometrically complex components but faces process-induced defects that undermine quality consistency.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 12. A closed-loop framework for perovskite precursor additive discovery

- Date: `2026-11-04`
- Journal: Communications Materials
- Link: https://doi.org/10.1038/s43246-026-01407-3
- Tags: active_learning, foundation_model, h2, high_throughput, perovskite, transfer_learning, uncertainty
- Authors: Xin-De Wang, Zhi-Rui Chen, Ze-Feng Gao, Peng‐Jie Guo, Cheng Mu
- Why it matters: Here we show that LEAP (LLM-driven Exploration via Active Learning for Perovskites), a closed-loop framework combining a domain-specialized language model with active learning, prioritizes perovskite precursor additives under low-data conditions.
- Innovation: Here we show that LEAP (LLM-driven Exploration via Active Learning for Perovskites), a closed-loop framework combining a domain-specialized language model with active learning, prioritizes perovskite precursor additives under low-data conditions.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 13. AnyNav: Visual neuro-symbolic friction learning for off-road navigation

- Date: `2026-11-07`
- Journal: The International Journal of Robotics Research
- Link: https://doi.org/10.1177/02783649261496456
- Tags: h2, md, ml, physics_informed, self_supervised, separation
- Authors: Taimeng Fu, Zitong Zhan, Zhipeng Zhao, Yi Du, Shaoshu Su
- Why it matters: To address these limitations, we introduce AnyNav, a vision-based friction estimation and navigation framework grounded in neuro-symbolic principles.
- Innovation: To address these limitations, we introduce AnyNav, a vision-based friction estimation and navigation framework grounded in neuro-symbolic principles.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 14. Predictive Modelling of Electronic Materials: A Review of Deep Learning Techniques in Computer Engineering

- Date: `2026-12-01`
- Journal: ASEAN Journal for Science and Engineering in Materials
- Link: https://ejournal.bumipublikasinusantara.id/index.php/ajsem/article/view/938
- Tags: generative_model, gnn, h2, high_throughput, ml, review, separation, two_d_material
- Authors: Agis Abhi Rafdhi, Hanhan Maulana, Senny Luckyardi, Eddy Soeryanto Soegoto, Dostnazar Ximmataliyev
- Why it matters: This review evaluates the application of deep learning (DL) for the predictive modeling of electronic materials in computer engineering.
- Innovation: This review evaluates the application of deep learning (DL) for the predictive modeling of electronic materials in computer engineering.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 15. Toward Intelligent Thermal Fluids: AI-Driven Design of Zeta-Engineered Nanofluids and Self-Organized Thermal Transport Networks

- Date: `2026-11-04`
- Journal: Research Square
- Link: https://doi.org/10.21203/rs.3.rs-11352574/v1
- Tags: active_learning, h2, ml, oxide, physics_informed, review, two_d_material
- Authors: Zhong Hu, Haiping Hong
- Why it matters: Abstract The development of next-generation nanofluids requires a shift from empirical formulation approaches toward data-driven design strategies that simultaneously optimize thermal conductivity, dynamic viscosity, stability, and system-level performance.
- Innovation: Abstract The development of next-generation nanofluids requires a shift from empirical formulation approaches toward data-driven design strategies that simultaneously optimize thermal conductivity, dynamic viscosity, stability, and system-level performance.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 16. FACTO: fast atom-centered tensor operator for accurate and efficient foundational machine-learned interatomic potentials

- Date: `2026-11-02`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2611.03276
- Tags: equivariant_ml, h2, high_throughput, interatomic_potential, md
- Authors: Siyuan Liu, Chang Han, Sheng Gong, Yanping Yang, Tianze Zheng
- Why it matters: High-throughput inference remains a central challenge for equivariant machine-learned interatomic potentials.
- Innovation: High-throughput inference remains a central challenge for equivariant machine-learned interatomic potentials.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 17. Gentle push: Fine-tuning foundation models for complex oxide surface reconstructions

- Date: `2026-11-04`
- Journal: Physical Review Research
- Link: https://doi.org/10.1103/vh5b-6ks5
- Tags: force_field, foundation_model, h2, high_throughput, interatomic_potential, ml, oxide, transfer_learning
- Authors: Ralf Wanzenböck, Eva Doloszeski, Georg K. H. Madsen
- Why it matters: Structure-prediction methods routinely sample highly distorted, far-from-equilibrium configurations.
- Innovation: Structure-prediction methods routinely sample highly distorted, far-from-equilibrium configurations.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 18. Interpretable Hybrid Surrogate Modeling for Diameter Deviation Prediction in Injection Molding Using Symbolic Regression and Gaussian Process Residual Correction

- Date: `2026-10-27`
- Journal: Research Square
- Link: https://doi.org/10.21203/rs.3.rs-11271710/v1
- Tags: ml, surrogate_model, symbolic_regression, uncertainty
- Authors: Amine Aboutaib, Hanaa Ouaomar, Souad Touairi, Mourad Kadiri
- Why it matters: Abstract Dimensional quality in injection molding is hard to model when process variables act through coupled pressure, flow, and cycle-history effects and the experimental budget is small.
- Innovation: Abstract Dimensional quality in injection molding is hard to model when process variables act through coupled pressure, flow, and cycle-history effects and the experimental budget is small.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 19. Universal machine learning potentials for two-dimensional materials mechanics and phonons

- Date: `2026-11-01`
- Journal: International Journal of Mechanical Sciences
- Link: https://doi.org/10.1016/j.ijmecsci.2026.112275
- Tags: dft, h2, high_throughput, interatomic_potential, md, ml, porous_material, two_d_material
- Authors: Bohayra Mortazavi, Mohammad Sadegh Eshaghi, Timon Rabczuk, Xiaoying Zhuang
- Why it matters: Overall, this work highlights the strong potential of uMLIPs for predictive modeling and high-throughput screening of functional 2D materials, with promising extensions toward multilayer heterostructures, nanocomposites, and biologically integrated systems beyond the reach of conventional approaches.
- Innovation: Overall, this work highlights the strong potential of uMLIPs for predictive modeling and high-throughput screening of functional 2D materials, with promising extensions toward multilayer heterostructures, nanocomposites, and biologically integrated systems beyond the reach of conventional approaches.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.

### 20. In the age of big data and AI: do we still need chemical bonds?

- Date: `2026-10-30`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2611.00228
- Tags: equivariant_ml, gnn, h2, ml, review, separation, symbolic_regression, uncertainty
- Authors: Mohammed Al-Fahdi, Aakash Naik, Katharina Ueltzen, Luc Walterbos, Tom Demeyere
- Why it matters: We show that, through linear probing, Allegro and MACE embeddings recover bonding descriptors with (R^2 > 0.95), indicating that bonding emerges naturally from Allegro's and MACE's latent spaces.
- Innovation: We show that, through linear probing, Allegro and MACE embeddings recover bonding descriptors with (R^2 > 0.95), indicating that bonding emerges naturally from Allegro's and MACE's latent spaces.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 21. Explainable artificial intelligence for laser powder bed fusion alloys: breaking the formability–performance trade-off via collaborative control

- Date: `2026-11-06`
- Journal: Advanced Materials Joining
- Link: https://doi.org/10.1007/s44500-026-00023-y
- Tags: alloy, h2, high_throughput, image_analysis, multimodal, physics_informed, priority_journal, review
- Authors: Minghao Liu, Jiabo Fu, 康应成, Hao Yu, Xiaolu Wei
- Why it matters: Laser powder bed fusion (LPBF) enables the fabrication of metallic components with complex geometries and high performance.
- Innovation: Laser powder bed fusion (LPBF) enables the fabrication of metallic components with complex geometries and high performance.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Map the method onto MOF structure images, spectra, isotherm curves, or generated-structure consistency checks.
- MOF relevance: Distant-domain method can be useful if it maps to a concrete MOF object such as structure images, spectra, isotherms, pore maps, or multimodal consistency checks.

### 22. Synthesis-by-design of ferroelectric Dion–Jacobson two-dimensional hybrid organic–inorganic perovskites

- Date: `2026-10-27`
- Journal: Nature Communications
- Link: https://doi.org/10.1038/s41467-026-78928-5
- Tags: h2, high_throughput, interatomic_potential, perovskite, priority_journal, symbolic_regression
- Authors: Lulu Wang, Weixin He, Shurong Yuan, Chao Yang, Nihang Fu
- Why it matters: Here we show a staged, physically guided synthesis-by-design workflow that integrates learning from scarce ferroelectric data with structure-aware screening.
- Innovation: Here we show a staged, physically guided synthesis-by-design workflow that integrates learning from scarce ferroelectric data with structure-aware screening.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.

### 23. Applicability Domain of Universal Machine Learning Interatomic Potentials at Solid-State Battery Interfaces

- Date: `2026-11-05`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15011777/v1
- Tags: battery, dft, electrolyte, h2, high_throughput, interatomic_potential, ml, self_supervised, transfer_learning
- Authors: Umang Agarwal, Mengke Li, Gopalakrishnan Sai Gautam, Zeyu Deng
- Why it matters: Descriptor-based analysis traces the higher force errors to interfacial environments that lie outside the pretraining data.
- Innovation: Descriptor-based analysis traces the higher force errors to interfacial environments that lie outside the pretraining data.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 24. Solving the Computational Peptide Design Puzzle: Challenges and Opportunities

- Date: `2026-11-05`
- Journal: ACS Omega
- Link: https://doi.org/10.1021/acsomega.6c10380
- Tags: force_field, h2, high_throughput, md, ml, review, uncertainty
- Authors: Daniela Kalafatović, Aysenur Iscen, Mathijs F. J. Mabesoone, Ioana Mariuca Ilie, Goran Mauša
- Why it matters: Here, we present our perspective on the main challenges in the computational study and design of peptides and discuss how collective efforts toward standardized data generation and data-driven discovery frameworks may help advance the field.
- Innovation: Here, we present our perspective on the main challenges in the computational study and design of peptides and discuss how collective efforts toward standardized data generation and data-driven discovery frameworks may help advance the field.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 25. Self-supervised adaptation of vision foundation models for fine-grained plant species and damage assessment in herbicide trials

- Date: `2026-11-06`
- Journal: Computers and Electronics in Agriculture
- Link: https://doi.org/10.1016/j.compag.2026.112572
- Tags: foundation_model, h2, self_supervised
- Authors: Leire Benito-Del-Valle, Artzai Picón, Daniel Múgica, Manuel Ramos, Eva Portillo
- Why it matters: Herbicide field trials require accurate identification of plant species and assessment of herbicide-induced damage across diverse environments.
- Innovation: Herbicide field trials require accurate identification of plant species and assessment of herbicide-induced damage across diverse environments.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 26. Optimisation of Topical and Transdermal Pharmaceutical Formulations: Methods, Challenges and Opportunities

- Date: `2026-11-06`
- Journal: SmartSys
- Link: https://doi.org/10.1002/sys3.70047
- Tags: equivariant_ml, high_throughput, ml, review, uncertainty
- Authors: Yongrui Xiao, Yu Zhang, Chunlin Chen, Dimitrios A. Tsaoulidis, Kai Yang
- Why it matters: ABSTRACT Topical and transdermal pharmaceutical formulations are a large and diverse class of products, yet their optimisation remains a complex, resource‐intensive challenge.
- Innovation: ABSTRACT Topical and transdermal pharmaceutical formulations are a large and diverse class of products, yet their optimisation remains a complex, resource‐intensive challenge.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 27. Physics-informed data synthesis enables deep learning in data-scarce materials engineering

- Date: `2026-11-05`
- Journal: Results in Engineering
- Link: https://doi.org/10.1016/j.rineng.2026.113955
- Tags: alloy, h2, ml, physics_informed, uncertainty
- Authors: Haoxiang Zhang, Lihui Zhang, Feng Li, Pan Ding, Xiaodong Ren
- Why it matters: Here we present a physics-informed data-synthesis framework for probabilistic prediction under extreme data scarcity, demonstrated on hot-cracking control in K439B nickel-based superalloy aero-engine repair welding.
- Innovation: Here we present a physics-informed data-synthesis framework for probabilistic prediction under extreme data scarcity, demonstrated on hot-cracking control in K439B nickel-based superalloy aero-engine repair welding.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 28. Superior directional thermal conductivity and stiffness in rectangular γ-graphyne revealed by neuroevolution machine-learning potentials

- Date: `2026-11-04`
- Journal: International Journal of Heat and Mass Transfer
- Link: https://doi.org/10.1016/j.ijheatmasstransfer.2026.129810
- Tags: active_learning, dft, h2, interatomic_potential, md, separation
- Authors: Jhionathan de Lima, Cristiano Francisco Woellner
- Why it matters: Graphynes have emerged as promising carbon allotropes for next-generation nanoelectronics and thermoelectric devices due to their unique combination of porous frameworks, tunable bandgaps, and unconventional thermal transport.
- Innovation: Graphynes have emerged as promising carbon allotropes for next-generation nanoelectronics and thermoelectric devices due to their unique combination of porous frameworks, tunable bandgaps, and unconventional thermal transport.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 29. SlideGen: Collaborative Multimodal Agents for Scientific Slide Generation

- Date: `2026-11-06`
- Journal: ACM International Conference on Multimedia (ACM MM)
- Link: https://doi.org/10.1145/3767308.3835435
- Tags: h2, high_throughput, multimodal, separation
- Authors: Xin Liang, Zhilin Zhang, Xiang Zhang, Haoran Su, Yiwei Xu
- Why it matters: In this work, we introduce SlideGen, a collaborative vision-language multi-agent framework that coordinates narrative planning, multimodal grounding, and layout composition.
- Innovation: In this work, we introduce SlideGen, a collaborative vision-language multi-agent framework that coordinates narrative planning, multimodal grounding, and layout composition.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 30. Artificial intelligence in offshore wind geotechnical engineering: A lifecycle-oriented review

- Date: `2026-10-28`
- Journal: Ocean
- Link: https://doi.org/10.26599/ocean.2026.9470032
- Tags: active_learning, force_field, h2, high_throughput, ml, physics_informed, review, surrogate_model
- Authors: Jie Shi, Yimin Lu, Hongjiang Li, Songyu Liu, Mu Linlong
- Why it matters: Abstract As offshore wind develops toward deeper waters and larger turbine capacities, geotechnical challenges are becoming increasingly complex, involving more variable seabed conditions, larger foundation dimensions, and stricter lifecycle reliability and cost-control requirements.
- Innovation: Abstract As offshore wind develops toward deeper waters and larger turbine capacities, geotechnical challenges are becoming increasingly complex, involving more variable seabed conditions, larger foundation dimensions, and stricter lifecycle reliability and cost-control requirements.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
