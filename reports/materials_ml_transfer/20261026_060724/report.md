# Literature Update

- Generated: `2026-10-26T06:07:24`
- Profile: `materials_ml_transfer`
- Since: `2023-10-27`
- Papers retained: `30`

## Overview

Collected 30 deduplicated papers for profile `materials_ml_transfer`. This transfer profile keeps non-MOF ML papers when they carry a concrete method signal; 30 retained papers are outside direct MOF literature. 30 papers contain transferable method tags and 11 appear in priority journals or major venue families. 20 papers also carry explicit material-system tags, helping judge whether the chemistry is close enough to MOFs.

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

### 1. Less can be more for predicting properties with large language models

- Date: `2026-10-12`
- Journal: Nature Computational Science
- Link: https://doi.org/10.1038/s43588-026-01045-2
- Tags: crystal, foundation_model, gnn, h2, high_throughput, ml, priority_journal, separation
- Authors: Nawaf Alampara, Santiago Miret, Kevin Maik Jablonka
- Why it matters: Here we report fundamental limitations in LLM’s ability to learn from coordinate information in coordinate–category data.
- Innovation: Here we report fundamental limitations in LLM’s ability to learn from coordinate information in coordinate–category data.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 2. Designing High-Entropy Alloys: From Physical Metallurgy to Machine Learning Enabled Discovery

- Date: `2026-10-18`
- Journal: Alloys
- Link: https://doi.org/10.3390/alloys5040029
- Tags: active_learning, alloy, h2, high_throughput, interatomic_potential, ml, review, transfer_learning
- Authors: Manish Mandal, Mohd Bilal Khan
- Why it matters: In the final section, we discuss how artificial intelligence (AI) and machine learning (ML) can be used to solve the problem of combinatorial explosion of the design space of HEAs: supervised classifiers for phase prediction, regression and ensemble models for hardness, strength, and elastic moduli, active learning and Bayesian optimization for closed-loop discovery, high-throughput screening with CALPHAD, and machine-learned interatomic potentials.
- Innovation: In the final section, we discuss how artificial intelligence (AI) and machine learning (ML) can be used to solve the problem of combinatorial explosion of the design space of HEAs: supervised classifiers for phase prediction, regression and ensemble models for hardness, strength, and elastic moduli, active learning and Bayesian optimization for closed-loop discovery, high-throughput screening with CALPHAD, and machine-learned interatomic potentials.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
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

### 4. Autonomous Laboratories and Foundry Scientific Discovery at the Limit A machine does not discover a mechanism until it creates evidence that could defeat it Core coupling Autonomous experiment x active learning x scientific falsification Research scale 30 linked derivations x 82 chapters x 410 research sections x 200 detailed Research Gates Main result A falsifiable framework for generating, attacking and eliminating process mechanisms rather than confusing recipe optimization with scientific discovery. Series lineage Semiconductor Foundry Technologies x Intelligent Nanomanufacturing - Flagship 20 Publication Abstract This monograph asks whether an autonomous foundry laboratory can do more than optimize an existing recipe. It develops a research architecture in which the system must register competing process mechanisms, identify what its sensors can and cannot distinguish, choose experiments for model discrimination, preserve negative evidence, and issue counterfactual predictions that survive a new tool or fab. Yield improvement, simulation fit, and automation speed are treated as useful engineering outcomes but not as proof of a new mechanism. The central falsifiable proposition is that active experiments chosen to separate rival predictions should reduce the set of observationally equivalent mechanisms and improve preregistered counterfactual forecasts under the same sample, metrology, time, energy, and safety budget as expert DOE and strong safe Bayesian optimization. If the experiment cannot distinguish the models, if failures are selectively forgotten, if the acquisition function exploits a biased proxy, or if cross-tool predictions fail, the scientific claim is narrowed, split, or stopped. Scientific Position and Hard Boundary The work begins with bounded thin-film, deposition, etch, interface, and defect-mechanism challenges in simulation, digital-physical twins, test vehicles, and low-risk equipment states. Autonomous execution is permitted only through typed process intent, equipment capability contracts, explicit authorization, independent metrology, abort logic, and recoverable physical states. No information-gain score may override safety, material irreversibility, chain of custody, environmental obligations, worker protection, or equipment interlocks. Candidate Research Expression Dsci = Delta H of competing models + counterfactual information - sample cost - unsafe risk - hype penalty • Delta H measures reduction in uncertainty over the preregistered mechanism set. • Counterfactual information rewards predictions about interventions or new platforms that were not used for fitting. • Sample cost includes material, metrology, time, energy, and opportunity cost. • Unsafe risk is a hard feasibility concern, not a term that can be purchased by predicted knowledge. • The hype penalty prevents an engineering improvement from being narrated as a causal discovery. Five Layer Research Architecture 01 Competing Mechanism Contract Register rival mechanisms, observable signatures, claim levels, strong baselines, and hard boundaries. 02 Observability and Evidence Graph Map sensors, latent state, calibration ancestry, identifiability, and equivalent model sets. 03 Discriminating Active Experiment Choose controls, interventions, and fidelities for information under sample, energy, and risk budgets. 04 Refutation Memory and Safe Execution Compile typed experiments, preserve failures, detect misspecification, abort safely, and record why models were rejected. 05 Independent Transfer and Successor Choice Demand cross-tool counterfactual predictions, third-party replay, and the right to split, downgrade, or retire a mechanism. Minimum Verifiable Prototype Two process mechanisms are constructed to explain the same historical thin-film or etch observations. Expert DOE, safe Bayesian optimization, and the autonomous discovery policy receive matched samples, metrology, wall time, energy, and safety envelopes. Before the hidden outcomes are revealed, each freezes its hypotheses, predicted signatures, next experiment, acquisition value, uncertainty, and stopping rule. The decisive test is whether independent terminal metrology and a new intervention eliminate or sharply narrow one mechanism, not whether the system merely finds a better recipe. Research Contributions • Separates optimization, prediction, mechanism discrimination, causal support, and cross-platform scientific claims. • Connects observability, identifiability, Fisher information, Bayesian experimental design, causal intervention, and model criticism. • Treats negative results, failed experiments, calibration ancestry, manual corrections, and eliminated models as first-class scientific records. • Maps thirty distinct derivations to chapter, experiment, and Research Gate corridors. • Provides eighty-two chapters with five research pages per chapter: boundary, identifiability, minimum test, adversarial refutation, and successor route.

- Date: `2026-10-18`
- Journal: Zenodo (CERN European Organization for Nuclear Research)
- Link: https://doi.org/10.5281/zenodo.23452112
- Tags: active_learning, h2, ml, physics_informed, review, uncertainty
- Authors: 33
- Why it matters: Autonomous Laboratories and Foundry Scientific Discovery at the Limit A machine does not discover a mechanism until it creates evidence that could defeat it Core coupling Autonomous experiment x active learning x scientific falsification Research scale 30 linked derivations x 82 chapters x 410 research sections x 200 detailed Research Gates Main result A falsifiable framework for generating, attacking and eliminating process mechanisms rather than confusing recipe optimization with scientific discovery.
- Innovation: Autonomous Laboratories and Foundry Scientific Discovery at the Limit A machine does not discover a mechanism until it creates evidence that could defeat it Core coupling Autonomous experiment x active learning x scientific falsification Research scale 30 linked derivations x 82 chapters x 410 research sections x 200 detailed Research Gates Main result A falsifiable framework for generating, attacking and eliminating process mechanisms rather than confusing recipe optimization with scientific discovery.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 5. Universal machine learning force fields for materials simulation: From model construction to complex-system applications

- Date: `2026-10-22`
- Journal: Physica Scripta
- Link: https://doi.org/10.1088/1402-4896/aeb836
- Tags: battery, dft, electrolyte, force_field, h2, high_throughput, interatomic_potential, ml, physics_informed, review, self_supervised, surrogate_model, transfer_learning, uncertainty
- Authors: Guoyang Wang, Jing Yi, Yuanmao Hu, Shuai Zhao
- Why it matters: Abstract Machine learning force fields (MLFFs) can achieve first-principles accuracy within validated chemical and configurational domains while maintaining computational efficiency comparable to classical force fields for atomistic materials simulations.
- Innovation: Abstract Machine learning force fields (MLFFs) can achieve first-principles accuracy within validated chemical and configurational domains while maintaining computational efficiency comparable to classical force fields for atomistic materials simulations.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 6. Multiscale Digital-Twin Modeling of Energy-Storage Materials by Integrating First-Principles Calculations and Machine-Learning Interatomic Potentials

- Date: `2026-10-14`
- Journal: EAI Endorsed Transactions on Energy Web
- Link: https://doi.org/10.4108/ew.14196
- Tags: active_learning, battery, dft, electrocatalysis, equivariant_ml, h2, interatomic_potential, md, physics_informed, uncertainty
- Authors: Yan Li, Duochang Tang
- Why it matters: Conventional modeling of energy-storage materials is constrained by the computational cost of first-principles calculations, limited electrochemical-state awareness in machine-learning interatomic potentials, and weak coupling between materials-scale models and online battery decision-making.
- Innovation: Conventional modeling of energy-storage materials is constrained by the computational cost of first-principles calculations, limited electrochemical-state awareness in machine-learning interatomic potentials, and weak coupling between materials-scale models and online battery decision-making.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 7. From Atoms to Reactors: A Critical Review of a Decade of Machine Learning in Heterogeneous Catalysis (2017–2026)

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

### 8. Spatial Statistics for Screening Molecular Structures

- Date: `2026-10-15`
- Journal: Small
- Link: https://doi.org/10.1002/smll.76291
- Tags: active_learning, alloy, crystal, dft, equivariant_ml, generative_model, high_throughput, review
- Authors: Pranoy Ray, Surya R. Kalidindi
- Why it matters: ABSTRACT The dominant paradigm in computational materials discovery relies on heavily parameterized deep architectures, including message‐passing graph and equivariant networks, that typically require large density functional theory (DFT)‐labeled training sets and produce nonconvex latent representations complicating inverse design, a limitation in the data‐scarce regimes common to exploratory screening.
- Innovation: ABSTRACT The dominant paradigm in computational materials discovery relies on heavily parameterized deep architectures, including message‐passing graph and equivariant networks, that typically require large density functional theory (DFT)‐labeled training sets and produce nonconvex latent representations complicating inverse design, a limitation in the data‐scarce regimes common to exploratory screening.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 9. Inverse materials design via joint generation of crystal structures and local electronic descriptors

- Date: `2026-10-15`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02322-4
- Tags: catalyst_descriptor, crystal, dft, generative_model, h2, md, priority_journal, separation
- Authors: Ibuki Okuda, Izumi Takahara, Teruyasu Mizoguchi
- Why it matters: We propose a diffusion framework that jointly denoises crystal-structure variables and site-resolved local electronic descriptors through a shared score network.
- Innovation: We propose a diffusion framework that jointly denoises crystal-structure variables and site-resolved local electronic descriptors through a shared score network.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints.
- MOF relevance: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.

### 10. Advanced engineering of inorganic semiconductor nanowires: Materials-by-design for next-generation green energy technologies

- Date: `2026-10-05`
- Journal: Energy Reviews
- Link: https://doi.org/10.1016/j.enrev.2026.100216
- Tags: active_learning, catalysis, crystal, dft, electrocatalysis, h2, md, ml, photocatalysis, review, uncertainty, water
- Authors: Sunday Temitope Oyinbo, Hoe-Gil Lee, Sikiru Oluwarotimi Ismail, Tien‐Chien Jen
- Why it matters: Inorganic semiconductor nanowires (NWs) provide an unusually versatile platform for green-energy technologies because composition, crystal phase, defects, interfaces, morphology, and dimensionality can be engineered across multiple length scales.
- Innovation: Inorganic semiconductor nanowires (NWs) provide an unusually versatile platform for green-energy technologies because composition, crystal phase, defects, interfaces, morphology, and dimensionality can be engineered across multiple length scales.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 11. Quantum machine learning: A comprehensive survey of models, tools, and challenges

- Date: `2026-10-19`
- Journal: Journal of King Saud University - Computer and Information Sciences
- Link: https://doi.org/10.1007/s44443-026-01177-5
- Tags: gnn, h2, ml, review, transfer_learning
- Authors: Taha M. Mahmoud, Marwa R. Hassan, Shenson Joseph, Issam Boukabou, Naima Kaabouch
- Why it matters: Abstract Quantum Machine Learning (QML) is an emerging interdisciplinary field that merges quantum computing with classical machine learning (ML) to enhance computational efficiency, scalability, and accuracy in data-driven tasks.
- Innovation: Abstract Quantum Machine Learning (QML) is an emerging interdisciplinary field that merges quantum computing with classical machine learning (ML) to enhance computational efficiency, scalability, and accuracy in data-driven tasks.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 12. A New Paradigm for Computational Chemistry

- Date: `2026-10-20`
- Journal: Journal of the American Chemical Society
- Link: https://doi.org/10.1021/jacs.6c06653
- Tags: dft, h2, interatomic_potential, ml, priority_journal
- Authors: Raphael T. Husistein, Markus Reiher
- Why it matters: Abstract Computational chemistry has become an indispensable tool for generating data and insights, pervading all branches of experimental chemistry.
- Innovation: Abstract Computational chemistry has become an indispensable tool for generating data and insights, pervading all branches of experimental chemistry.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.

### 13. Machine‐Learning‐Potential‐Driven Volcano Relationship in Grain Boundary Amorphicity and Ionic Transport of Antiperovskite Solid Electrolytes

- Date: `2026-10-23`
- Journal: Advanced Materials
- Link: https://doi.org/10.1002/adma.75492
- Tags: battery, electrolyte, h2, interatomic_potential, md, ml, perovskite, priority_journal
- Authors: Abdullah Bin Faheem, Haobo Li
- Why it matters: ABSTRACT Ionic transport in solid‐state electrolytes is governed by interfacial disorder and local chemical environments, yet their microscopic design principles remain challenging because large‐scale interfacial kinetics are simulated using molecular dynamics (MD), where predictive design requires quantum‐level accuracy.
- Innovation: ABSTRACT Ionic transport in solid‐state electrolytes is governed by interfacial disorder and local chemical environments, yet their microscopic design principles remain challenging because large‐scale interfacial kinetics are simulated using molecular dynamics (MD), where predictive design requires quantum‐level accuracy.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.

### 14. Scalable long-range machine learning interatomic potentials with electrical response for atomistic material modeling

- Date: `2026-10-16`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2610.23643
- Tags: dft, electrolyte, equivariant_ml, h2, interatomic_potential, ml, physics_informed
- Authors: Yicheng Chen, Xiaoyun Yu, Hyejeong Song, Xintian Wang, Zihui Li
- Why it matters: Accurate atomistic simulations of materials under electric fields require long-range electrostatics and electrical-response modeling at length scales beyond the reach of conventional first-principles methods.
- Innovation: Accurate atomistic simulations of materials under electric fields require long-range electrostatics and electrical-response modeling at length scales beyond the reach of conventional first-principles methods.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 15. Linear response for machine-learned interatomic potentials: phonons at arbitrary wave vectors from the primitive cell

- Date: `2026-10-16`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2610.23545
- Tags: crystal, equivariant_ml, foundation_model, h2, high_throughput, interatomic_potential
- Authors: Thalis H. B. da Silva, Hai-Chen Wang, Miguel A. L. Marques
- Why it matters: Here we show that the dynamical matrix of a message-passing potential can be obtained exactly in the primitive cell, at any wave vector, as the linear response of the forces to a displacement modulated by a Bloch phase, in the spirit of density-functional perturbation theory.
- Innovation: Here we show that the dynamical matrix of a message-passing potential can be obtained exactly in the primitive cell, at any wave vector, as the linear response of the forces to a displacement modulated by a Bloch phase, in the spirit of density-functional perturbation theory.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 16. Artificial Intelligence–Driven Molecular Imprinting for Efficient Polymer Design and Enhanced Liquid‐Phase Separation

- Date: `2026-10-22`
- Journal: Electrophoresis
- Link: https://doi.org/10.1002/elps.70173
- Tags: active_learning, adsorption, dft, h2, md, ml, polymer, review, separation
- Authors: Erdoğan Özgür, Sena Pişkin, Canan Armutçu, M. Emin Çorman, Lokman Uzun
- Why it matters: ABSTRACT Molecularly imprinted polymers (MIPs) have become significantly more desirable as synthetic polymers with recognition sites designed for target molecules for use in liquid‐phase separation due to their high selectivity, stability, and robustness.
- Innovation: ABSTRACT Molecularly imprinted polymers (MIPs) have become significantly more desirable as synthetic polymers with recognition sites designed for target molecules for use in liquid‐phase separation due to their high selectivity, stability, and robustness.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 17. Explicit Spin Regulation as an Emerging Design Paradigm in Heterogeneous Catalysis

- Date: `2026-10-12`
- Journal: Accounts of Materials Research
- Link: https://doi.org/10.1021/accountsmr.6c00167
- Tags: active_learning, adsorption, catalysis, electrocatalysis, force_field, h2, high_throughput, interatomic_potential, multimodal, separation
- Authors: Tingyu Lu, Yuan Huang, Ang Cao, Wei Li, Hui Li
- Why it matters: In this Account, we develop explicit spin regulation as a framework for magnetism-informed catalysis.
- Innovation: In this Account, we develop explicit spin regulation as a framework for magnetism-informed catalysis.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 18. Bridging model attention to physical insights in structure-property dynamics

- Date: `2026-10-15`
- Journal: Science and Technology of Advanced Materials Methods
- Link: https://doi.org/10.1080/27660400.2026.2738286
- Tags: h2, md, ml, physics_informed, priority_journal, separation
- Authors: Duc-Anh Dao, Minh-Quyet Ha, Tien-Sinh Vu, Dinh-Cong Vuong, Keisuke Ishizuka
- Why it matters: By translating attention–derived emphasis into physical descriptors, this work establishes a pathway from predictive modeling to physical interpretation of hidden structure–property relationships.
- Innovation: By translating attention–derived emphasis into physical descriptors, this work establishes a pathway from predictive modeling to physical interpretation of hidden structure–property relationships.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 19. Thermal stabilization of defect charge states and finite-temperature charge transition levels

- Date: `2026-10-23`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02369-3
- Tags: h2, interatomic_potential, priority_journal
- Authors: Tobias Hainer, Ethan Berger, Esmée Berger, Olof Hildeberg, Paul Erhart
- Why it matters: Abstract Point defects introduce localized electronic states that critically affect carrier trapping, recombination, and transport in functional materials.
- Innovation: Abstract Point defects introduce localized electronic states that critically affect carrier trapping, recombination, and transport in functional materials.
- Likely limitations: Abstract-level evidence is promising, but validation breadth is unclear without reading the full paper.
- Next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.

### 20. A systematic review of DoS and DDoS attack detection in cloud environments: evolutionary trends and the emerging role of meta-learning for cross-domain adaptability

- Date: `2026-10-21`
- Journal: Frontiers in Artificial Intelligence
- Link: https://doi.org/10.3389/frai.2026.1958096
- Tags: h2, high_throughput, ml, review, transfer_learning
- Authors: Amit Tiwari, C. Navaneethan
- Why it matters: Denial of Service (DoS) and Distributed Denial of Service (DDoS) attacks continue to be one of the most persistent and rapidly evolving threats to current network infrastructures as they are becoming more sophisticated and increasingly disrupting the availability, reliability and security of cloud-based systems, Software-Defined Networks (SDNs), Internet of Things (IoT) ecosystems and next generation communication environments.
- Innovation: Denial of Service (DoS) and Distributed Denial of Service (DDoS) attacks continue to be one of the most persistent and rapidly evolving threats to current network infrastructures as they are becoming more sophisticated and increasingly disrupting the availability, reliability and security of cloud-based systems, Software-Defined Networks (SDNs), Internet of Things (IoT) ecosystems and next generation communication environments.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 21. SU(2)-Equivariant Spinor Message Passing for Molecular Magnetism

- Date: `2026-10-21`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2610.29111
- Tags: crystal, equivariant_ml, gnn, ml, water
- Authors: Erh-Wei Sheng, Beom Seok Kang, Yuchao Lin, Danish Khan, Anima Anandkumar
- Why it matters: Inspired by the spinor nature of these electronic states, we develop eSpinor, an SU(2)-equivariant graph neural network that propagates spinor features.
- Innovation: Inspired by the spinor nature of these electronic states, we develop eSpinor, an SU(2)-equivariant graph neural network that propagates spinor features.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 22. Microscopic origin of polytype-dependent melting in SiC revealed by machine-learning molecular dynamics

- Date: `2026-10-19`
- Journal: The Journal of Chemical Physics
- Link: https://doi.org/10.1063/5.0350682
- Tags: crystal, equivariant_ml, h2, interatomic_potential, md
- Authors: Ljiljana Stojanović, S. J. Magorrian, Lara Kabalan, R.N. White, Fabian L. Thiemann
- Why it matters: Predicting how crystal structure influences high-temperature stability remains a key challenge in materials modeling and design.
- Innovation: Predicting how crystal structure influences high-temperature stability remains a key challenge in materials modeling and design.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 23. Hierarchical universal open structure dataset for atomistic modeling

- Date: `2026-10-15`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2610.21771
- Tags: foundation_model, h2, interatomic_potential, md
- Authors: Sofiia Chorna, Cesare Malosso, Jonathan Schmidt, Michele Ceriotti
- Why it matters: To address these problems, we introduce a protocol to stratify a dataset into a hierarchy of nested subsets, subsampling from the coarsest to the finest resolution based on an "ecumetric" built to reflect the latent space representation of several popular universal machine-learning interatomic potentials.
- Innovation: To address these problems, we introduce a protocol to stratify a dataset into a hierarchy of nested subsets, subsampling from the coarsest to the finest resolution based on an "ecumetric" built to reflect the latent space representation of several popular universal machine-learning interatomic potentials.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 24. Machine learning for high-performance alloy design: A review

- Date: `2026-10-06`
- Journal: Metals Advances
- Link: https://doi.org/10.1016/j.metadv.2026.09.003
- Tags: active_learning, alloy, generative_model, h2, high_throughput, ml, review
- Authors: Zinuo Wang, Qi Xu, Peng Zhou, Tao Zhang, Fuhui Wang
- Why it matters: The traditional trial-and-error paradigm in alloy design, which has become too slow and resource-intensive, is increasingly inadequate for meeting the rapid industrial demand for high-performance materials.
- Innovation: The traditional trial-and-error paradigm in alloy design, which has become too slow and resource-intensive, is increasingly inadequate for meeting the rapid industrial demand for high-performance materials.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 25. Spontaneous defect formation as the origin of superionic transitions in antifluorite-type structures

- Date: `2026-10-23`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15010965/v1
- Tags: active_learning, battery, dft, electrolyte, equivariant_ml, force_field, h2, md, uncertainty
- Authors: Timothée Jamin, Kasper Tolborg
- Why it matters: Solid-state electrolytes offer the possibility of safer and higher energy density batteries, yet only a limited number of materials achieve ionic conductivities suitable for practical applications.
- Innovation: Solid-state electrolytes offer the possibility of safer and higher energy density batteries, yet only a limited number of materials achieve ionic conductivities suitable for practical applications.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 26. Crystal Structure Based Graph Neural Network And LLM Multi-Modal Approach for Material Magnetic Ordering Prediction

- Date: `2026-10-19`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2610.25775
- Tags: crystal, foundation_model, gnn, h2, ml, multimodal
- Authors: Adam Zheng, April Zheng, Sheng Ran
- Why it matters: This study presents a novel AI/ML-based multi-modal approach to predict material magnetic ordering using material crystal structure information as input to a Graph Neural Network model (GNN) and semantic text descriptions of the material's properties and structure as input to a Large Language Model (LLM), before performing information fusion of the GNN and LLM outputs to predict material magnetic ordering in four classes (Non-magnetic, Ferromagnetic, Antiferromagnetic, Ferrimagnetic).
- Innovation: This study presents a novel AI/ML-based multi-modal approach to predict material magnetic ordering using material crystal structure information as input to a Graph Neural Network model (GNN) and semantic text descriptions of the material's properties and structure as input to a Large Language Model (LLM), before performing information fusion of the GNN and LLM outputs to predict material magnetic ordering in four classes (Non-magnetic, Ferromagnetic, Antiferromagnetic, Ferrimagnetic).
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 27. Designing rigid protein fiducials to visualize GPCR conformational states

- Date: `2026-10-24`
- Journal: Nature Communications
- Link: https://doi.org/10.1038/s41467-026-78942-7
- Tags: equivariant_ml, h2, high_throughput, priority_journal
- Authors: Alina Vo Vo, Yuan-En Sun, Justin G. English, Michael J. Robertson
- Why it matters: Here we show that by combining generative protein design with deep-learning based ensemble prediction we can reliably design fiducial markers to facilitate cryogenic electron microscopy (cryoEM) of GPCRs at arbitrary fusion points, enabling the visualization of previously intractable states.
- Innovation: Here we show that by combining generative protein design with deep-learning based ensemble prediction we can reliably design fiducial markers to facilitate cryogenic electron microscopy (cryoEM) of GPCRs at arbitrary fusion points, enabling the visualization of previously intractable states.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 28. Predicting protein electrostatics with protein language models

- Date: `2026-10-24`
- Journal: Nature Communications
- Link: https://doi.org/10.1038/s41467-026-78406-y
- Tags: h2, high_throughput, ml, physics_informed, priority_journal
- Authors: Mingzhe Shen, Guy W. Dayhoff, Daniel Kortzak, Jana Shen
- Why it matters: Here we present KaML-ESMs, sequence-based neural networks built on the ESM protein language models and trained on the GAINES-augmented PKAD-3r dataset.
- Innovation: Here we present KaML-ESMs, sequence-based neural networks built on the ESM protein language models and trained on the GAINES-augmented PKAD-3r dataset.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 29. Physics-aware neural networks enable robust and full atomic structure determination via low-dose atomic electron tomography

- Date: `2026-10-23`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02363-9
- Tags: crystal, h2, high_throughput, ml, perovskite, physics_informed, priority_journal, zeolite
- Authors: Yao Zhang, Lanyi Cao, Zhen Sun, Jihan Zhou
- Why it matters: Here, we introduce a physics-aware, two-stage neural network (PANN) that incorporates physical constraints throughout its workflow to achieve accurate AET under low-dose imaging.
- Innovation: Here, we introduce a physics-aware, two-stage neural network (PANN) that incorporates physical constraints throughout its workflow to achieve accurate AET under low-dose imaging.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 30. Causality in liquid water as a hallmark of emergent glassy dynamics

- Date: `2026-10-20`
- Journal: Proceedings of the National Academy of Sciences
- Link: https://doi.org/10.1073/pnas.2616852123
- Tags: foundation_model, h2, md, priority_journal, separation, water
- Authors: Léon Huet, Vittorio Del Tatto, Debarshi Banerjee, Alessandro Laio, Ali A. Hassanali
- Why it matters: In molecular liquids such as water, time-delayed influences between microscopic or mesoscopic variables are typically probed using time-correlation functions, which are symmetric under detailed balance and therefore blind to dynamical asymmetries.
- Innovation: In molecular liquids such as water, time-delayed influences between microscopic or mesoscopic variables are typically probed using time-correlation functions, which are symmetric under detailed balance and therefore blind to dynamical asymmetries.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
