# Literature Update

- Generated: `2026-09-07T06:04:04`
- Profile: `reaction_catalyst_ml_transfer`
- Since: `2016-09-09`
- Papers retained: `28`

## Overview

Collected 28 deduplicated papers for profile `reaction_catalyst_ml_transfer`. This transfer profile keeps non-MOF ML papers when they carry a concrete method signal; 26 retained papers are outside direct MOF literature. 28 papers contain transferable method tags and 2 appear in priority journals or major venue families. 20 papers also carry explicit material-system tags, helping judge whether the chemistry is close enough to MOFs.

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
- Tags: active_learning, catalysis, foundation_model, h2, high_throughput, interatomic_potential, ml, multimodal, priority_journal
- Authors: Di Zhang, Yuanzheng Chen, Chuanyu Liu, Y. H. Liu, Hongliang Xin
- Why it matters: The integration of artificial intelligence (AI) into catalysis is fundamentally reshaping the research paradigm of catalyst discovery.
- Innovation: The integration of artificial intelligence (AI) into catalysis is fundamentally reshaping the research paradigm of catalyst discovery.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 2. Machine learning approaches for electrocatalyst design in water splitting: a review for green hydrogen production

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

### 5. Computational and ML methods in MOF based supercapacitors - from mechanistic understanding to future materials design

- Date: `2026-08-29`
- Journal: Journal of Materials Science Materials Theory
- Link: https://doi.org/10.1186/s41313-026-00087-3
- Tags: active_learning, catalyst_descriptor, crystal, dft, electrocatalysis, high_throughput, ml, mof, physics_informed, porous_material, review, surrogate_model
- Authors: Achal Siddharth Fulmali, Himanshu Sekhar Panda
- Why it matters: Key insights from DFT are discussed in relation to three critical performance descriptors as electrical conductivity, electrochemical and structural stability, and redox activity.
- Innovation: Key insights from DFT are discussed in relation to three critical performance descriptors as electrical conductivity, electrochemical and structural stability, and redox activity.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 6. Development of AI-eChemist Laboratory

- Date: `2026-08-06`
- Journal: AI Agent
- Link: https://doi.org/10.20517/aiagent.2026.15
- Tags: active_learning, catalysis, electrocatalysis, h2, high_throughput, ml, multimodal, review
- Authors: Yicheng Tan, Lunbo Chen, Xiangyi Shan, Yuanhua Tu, Pengfei Wang
- Why it matters: As an autonomous experimental system tailored to electrochemical scenarios, the AI-eChemist Laboratory integrates front-end intelligent decision-making, automated high-throughput experimentation, multimodal characterization, and data-driven analysis, providing a new paradigm for the discovery, mechanistic understanding, and application validation of complex electrocatalytic materials.
- Innovation: As an autonomous experimental system tailored to electrochemical scenarios, the AI-eChemist Laboratory integrates front-end intelligent decision-making, automated high-throughput experimentation, multimodal characterization, and data-driven analysis, providing a new paradigm for the discovery, mechanistic understanding, and application validation of complex electrocatalytic materials.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 7. AI-Guided Single-Atom Electrocatalysts for Carbon-Neutral Chemical Manufacturing: from CO₂ Conversion to Green Ammonia Synthesis

- Date: `2026-07-25`
- Journal: Scholars International Journal of Chemistry and Material Sciences
- Link: https://doi.org/10.36348/sijcms.2026.v09i04.004
- Tags: active_learning, catalysis, co2, dft, h2, high_throughput, ml, oxide, review, separation
- Authors: Swaira Anjum, Amir Sohail, Muhammad Ibrahim, Shah Faisal, Noman Hassan
- Why it matters: Next, machine learning, density functional theory integration, high-throughput screening, explainable descriptors, and self-driving laboratory concepts are evaluated as tools for rational catalyst development.
- Innovation: Next, machine learning, density functional theory integration, high-throughput screening, explainable descriptors, and self-driving laboratory concepts are evaluated as tools for rational catalyst development.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 8. Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion

- Date: `2026-09-03`
- Journal: Materials Today Sustainability
- Link: https://doi.org/10.1016/j.mtsust.2026.101445
- Tags: active_learning, catalysis, co2, electrocatalysis, generative_model, h2, mof, photocatalysis, porous_material, review, separation, water
- Authors: Fazal Raziq, Sharafat Ali, Rajwali Khan, Ashfaq Ahmad, Muhammad Shoaib
- Why it matters: Mesoporous architecture confinement engineering has become an effective approach to address major limitations of single-atom catalysts (SACs) and integrated CO 2 capture-conversion systems.
- Innovation: Mesoporous architecture confinement engineering has become an effective approach to address major limitations of single-atom catalysts (SACs) and integrated CO 2 capture-conversion systems.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 9. Harnessing Artificial Intelligence (AI) for a greener future: a review of AI advancements in green chemistry, chemical processes and sustainable materials

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

### 10. Fine-tuning large language models to generate single-atom catalyst synthesis procedures

- Date: `2026-06-19`
- Journal: Communications Chemistry
- Link: https://doi.org/10.1038/s42004-026-02046-y
- Tags: catalysis, foundation_model, h2, review, transfer_learning
- Authors: Manu Suvarna, Matteo Manica, Fillipo Ficarra, Andrés M. Bran, Andrea Ruiz‐Ferrando
- Why it matters: We demonstrate the model's practicality through a user interface allowing researchers to query procedures tailored to their design conditions.
- Innovation: We demonstrate the model's practicality through a user interface allowing researchers to query procedures tailored to their design conditions.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Catalytic conclusions are likely thermodynamics-heavy unless kinetics or explicit environment are included.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 11. Perovskite‐Based Catalysts for the Oxygen Evolution Reaction: Synthesis, Device Relevant Performance, and Scale‐Up Strategies

- Date: `2026-08-22`
- Journal: Small
- Link: https://doi.org/10.1002/smll.75231
- Tags: catalysis, electrocatalysis, h2, high_throughput, oxide, perovskite, review, uncertainty, water
- Authors: Jala Bib Khan, Norbert Kazamer, Marco Brand, Tim Hülser, Clemens Pollerberg
- Why it matters: Perovskite-based oxides are promising electrocatalysts for the oxygen evolution reaction due to their flexible composition, tunable electronic structure, and robust nature.
- Innovation: Perovskite-based oxides are promising electrocatalysts for the oxygen evolution reaction due to their flexible composition, tunable electronic structure, and robust nature.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 12. Few-Shot Ensemble Learning for Catalysis and Application to Trimetallics for Oxygen Reduction

- Date: `2026-03-02`
- Journal: ACS Catalysis
- Link: https://doi.org/10.1021/acscatal.5c08168
- Tags: adsorption, alloy, catalysis, dft, h2, high_throughput, interatomic_potential, transfer_learning, uncertainty
- Authors: Avery F. Hill, Andrea Ruiz-Escudero, M. M. Montemore
- Why it matters: Machine-learned interatomic potentials (MLIPs) are increasingly used to accelerate catalyst discovery, but their accuracy and utility are often unclear, particularly when applying them to different computational setups or design spaces than those of the training data.
- Innovation: Machine-learned interatomic potentials (MLIPs) are increasingly used to accelerate catalyst discovery, but their accuracy and utility are often unclear, particularly when applying them to different computational setups or design spaces than those of the training data.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 13. Materials Behavior as Mechanism Ensembles: A Probabilistic Framework for Emergent Behaviors

- Date: `2026-07-29`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2607.27163
- Tags: h2, ml, multimodal, review
- Authors: Brad L. Boyce, Mitchell Wood, Krishna Garikipati, Andreas E. Robertson, Jeffrey Larson
- Why it matters: Here we present a probabilistic framework that describes materials behavior as an ensemble of constituent mechanisms whose activation, interaction, and evolution determine emergent outcomes.
- Innovation: Here we present a probabilistic framework that describes materials behavior as an ensemble of constituent mechanisms whose activation, interaction, and evolution determine emergent outcomes.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 14. Trapped at Tier 1: Why machine learning-guided electrocatalyst discovery has not closed the lab-to-industry gap

- Date: `2026-07-23`
- Journal: Next Energy
- Link: https://doi.org/10.1016/j.nxener.2026.100826
- Tags: active_learning, battery, catalysis, electrolyte, h2, high_throughput, ml, review, water
- Authors: Raymond Taziwa
- Why it matters: Machine learning has transformed electrocatalyst discovery, enabling screening across millions of candidate compositions.
- Innovation: Machine learning has transformed electrocatalyst discovery, enabling screening across millions of candidate compositions.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 15. Junction-Engineered TiO2 Nanotube Photocatalysts for Efficient Solar Hydrogen Generation: Doping Strategies, Structure–Activity Relationships, and Future Perspectives

- Date: `2026-07-30`
- Journal: Journal of Materials Science Materials in Energy
- Link: https://doi.org/10.1007/s44308-026-00024-3
- Tags: catalysis, catalyst_descriptor, h2, high_throughput, oxide, photocatalysis, review, separation, water
- Authors: Jeslin Jebish G P
- Why it matters: The escalating global energy demand and the imperative to decarbonise the energy sector have established green hydrogen—produced via solar-driven photocatalytic water splitting—as a critical technology for a sustainable future.
- Innovation: The escalating global energy demand and the imperative to decarbonise the energy sector have established green hydrogen—produced via solar-driven photocatalytic water splitting—as a critical technology for a sustainable future.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.

### 16. Ioc-Mldroid: a Hybrid Approach for Detection of Android Based Malicious Applications Using Indicators of Compromise (Iocs) and Machine Learning

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

### 17. Competition-Derived Relative Reactivity and 3D Electronic-State Analysis of Site- and Facial Selectivity in NaBH4/MeOH Ketone Reductions

- Date: `2026-09-01`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15002906/v3
- Tags: h2, ml, reaction_dataset, separation
- Authors: Daimon Sakaguchi, Taisei Kawasaki, Mayu Itakura, Chihiro Tada, Hiroaki Gotoh
- Why it matters: A Lasso model trained on 83 of these reaction faces with three-dimensional electron-density, electrostatic-potential, and carbonyl-centered projected C=O π * descriptors achieved R 2 = 0.804 under strict nested outer leave-one-out cross-validation.
- Innovation: A Lasso model trained on 83 of these reaction faces with three-dimensional electron-density, electrostatic-potential, and carbonyl-centered projected C=O π * descriptors achieved R 2 = 0.804 under strict nested outer leave-one-out cross-validation.
- Likely limitations: Catalyst generality inferred from sparse historical reaction data can still reflect reporting bias and needs targeted validation. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Rebuild the workflow on MOF catalytic reaction families with explicit scaffold generality, reporting-bias, and validation splits. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Reaction-specific small-data workflow is useful for MOF catalysis if catalyst generality, literature bias, and scaffold validation are made explicit.

### 18. A green solvent screening tool for emerging materials via uncertainty aware, transformer enhanced transfer learning

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

### 19. ReactionAtlas: Ab origine exploration of chemical reaction networks with machine learning

- Date: `2026-06-29`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.30778
- Tags: catalysis, dft, force_field, generative_model, ml
- Authors: Stefan Gugler, Max Eissler, Khaled Kahouli, Klaus-Robert Müller
- Why it matters: We introduce ReactionAtlas, which builds a reaction network $\textit{ab origine}$ from a handful of seed molecules and without hand-crafted rules.
- Innovation: We introduce ReactionAtlas, which builds a reaction network $\textit{ab origine}$ from a handful of seed molecules and without hand-crafted rules.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 20. DASyR-LLM: Domain-Aware Symbolic Regression with LLMs for Kinetic Model Discovery

- Date: `2026-08-05`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2608.05120
- Tags: catalysis, foundation_model, h2, ml, symbolic_regression
- Authors: Roberto Aliaga Medina, Paulina Quintanilla, Antonio del Rio Chanona
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

### 22. Electron microscopy of carbon-supported metal catalysts: From atomic-scale structural characterization to o perando mechanistic insights

- Date: `2026-09-01`
- Journal: Carbon Future
- Link: https://doi.org/10.26599/cf.2026.9200084
- Tags: catalysis, catalyst_descriptor, force_field, h2
- Authors: Xinyi Cai, Xuetao Qin
- Why it matters: Abstract Carbon-supported metal catalysts, ranging from isolated single atoms and sub-nanometer clusters to nanoparticles, are widely used in heterogeneous catalysis because of the high surface area, conductivity, tunability and defect-rich nature of carbon supports.
- Innovation: Abstract Carbon-supported metal catalysts, ranging from isolated single atoms and sub-nanometer clusters to nanoparticles, are widely used in heterogeneous catalysis because of the high surface area, conductivity, tunability and defect-rich nature of carbon supports.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.

### 23. Work Function and High-Coverage Adsorption Energy as Hydrogen-Evolution Descriptors on Ag-Au-Pd-Pt Alloys

- Date: `2026-08-28`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2608.28347
- Tags: adsorption, alloy, electrocatalysis, gnn, h2, ml
- Authors: Zacharias Liasi, Ridha Zerdoumi, Felix Thelen, Geovane Arruda de Oliveira, Rico Zehl
- Why it matters: Hydrogen-evolution activity is commonly rationalized through hydrogen adsorption energies and the Sabatier principle, yet this descriptor picture becomes ambiguous on multimetallic surfaces, where each composition exposes a distribution of local adsorption environments.
- Innovation: Hydrogen-evolution activity is commonly rationalized through hydrogen adsorption energies and the Sabatier principle, yet this descriptor picture becomes ambiguous on multimetallic surfaces, where each composition exposes a distribution of local adsorption environments.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 24. Gaussian Process Modeling of Bioorthogonal Cycloaddition Reactivity from Sparse Data

- Date: `2026-02-24`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15000346/v1
- Tags: h2, ml, separation, surrogate_model, transfer_learning
- Authors: Dennis Svatunek
- Why it matters: Bioorthogonal tetrazine ligations are widely used due to their exceptionally fast kinetics, yet quantitative prediction of their reactivity grounded in experiments remains challenging because experimentally measured rate constants are scarce and unevenly distributed across chemical space.In this work, we demonstrate that Gaussian process (GP) regression models can capture meaningful reactivity trends from sparse kinetic datasets of tetrazine ligations.Using a curated collection of experimental second-order rate constants, we show that GP models achieve competitive predictive performance despite limited data availability.We compare Gaussian process models to a neural network baseline and find that, while the deep learning approach can reach similar point-prediction accuracy, Gaussian processes exhibit more reliable performance in the low-data regime.Importantly, the flexibility of GP models enables data-efficient learning of structure-reactivity relationships without requiring large training datasets.Together, these results establish Gaussian processes as practical surrogate models for modeling reactivity trends in tetrazine ligations and related bioorthogonal cycloadditions, providing a foundation for data-efficient exploration and optimization of bioorthogonal reaction space.
- Innovation: Bioorthogonal tetrazine ligations are widely used due to their exceptionally fast kinetics, yet quantitative prediction of their reactivity grounded in experiments remains challenging because experimentally measured rate constants are scarce and unevenly distributed across chemical space.In this work, we demonstrate that Gaussian process (GP) regression models can capture meaningful reactivity trends from sparse kinetic datasets of tetrazine ligations.Using a curated collection of experimental second-order rate constants, we show that GP models achieve competitive predictive performance despite limited data availability.We compare Gaussian process models to a neural network baseline and find that, while the deep learning approach can reach similar point-prediction accuracy, Gaussian processes exhibit more reliable performance in the low-data regime.Importantly, the flexibility of GP models enables data-efficient learning of structure-reactivity relationships without requiring large training datasets.Together, these results establish Gaussian processes as practical surrogate models for modeling reactivity trends in tetrazine ligations and related bioorthogonal cycloadditions, providing a foundation for data-efficient exploration and optimization of bioorthogonal reaction space.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

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

### 26. Expert-Informed Contrastive Learning of Condition Space for Amide Coupling Reactions

- Date: `2026-03-18`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15001054/v1
- Tags: h2, high_throughput, ml, self_supervised, separation
- Authors: Matthew Ball, Felix A. Faber, Cassie Pratley, Thierry Kogej, Dragos Horvath
- Why it matters: Here, we present a novel machine learning framework designed to generate chemically relevant representations for sets of conditions.
- Innovation: Here, we present a novel machine learning framework designed to generate chemically relevant representations for sets of conditions.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 27. Artificial intelligence-driven platform for catalytic reactor discovery and optimization applied to carbon dioxide valorization

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

### 28. Expanding frontiers of complex reaction network exploration through a general reactive machine learning potential

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
