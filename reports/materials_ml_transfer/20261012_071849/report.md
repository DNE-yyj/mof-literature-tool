# Literature Update

- Generated: `2026-10-12T07:18:49`
- Profile: `materials_ml_transfer`
- Since: `2023-10-13`
- Papers retained: `30`

## Overview

Collected 30 deduplicated papers for profile `materials_ml_transfer`. This transfer profile keeps non-MOF ML papers when they carry a concrete method signal; 30 retained papers are outside direct MOF literature. 30 papers contain transferable method tags and 6 appear in priority journals or major venue families. 21 papers also carry explicit material-system tags, helping judge whether the chemistry is close enough to MOFs.

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

### 1. AI-Driven Electrocatalyst Discovery: Integrating Machine Learning, Density Functional Theory, and High-Throughput Screening for Sustainable Energy Conversion

- Date: `2026-09-29`
- Journal: International Journal of Soft Computing and Engineering
- Link: https://doi.org/10.35940/ijsce.e3727.16051126
- Tags: active_learning, alloy, catalysis, co2, dft, electrocatalysis, foundation_model, gnn, h2, high_throughput, interatomic_potential, ml, multimodal, oxide, perovskite, review, surrogate_model
- Authors: Frank Onyiriuka, Obojobo Donatus Obukeajeta, Micheal Abimbola Oladosu, Moses Adondua Abah, Felix Sekayo Olagbenro
- Why it matters: This review summarizes recent advances in AI-driven electrocatalyst discovery in the past five years (2020–2025) with a focus on the three pillars that have enabled this development: (1) machine learning (ML) algorithms and interpretable/explainable frameworks that extract descriptors of catalytic data that are physically meaningful; (2) the ability to couple ML with DFT using surrogate models, graph neural network interatomic potentials, and large benchmark datasets that reduce computational costs by orders of magnitude at close to DFT accuracy; and (3) high throughput screening pipelines for virtual and experimental screening, involving active learning and Bayesian optimisation, that have been applied to a diverse range of electrocatalytic reactions, including the hydrogen evolution reaction, the oxygen evolution/reduction reaction, and the carbon dioxide reduction reaction.
- Innovation: This review summarizes recent advances in AI-driven electrocatalyst discovery in the past five years (2020–2025) with a focus on the three pillars that have enabled this development: (1) machine learning (ML) algorithms and interpretable/explainable frameworks that extract descriptors of catalytic data that are physically meaningful; (2) the ability to couple ML with DFT using surrogate models, graph neural network interatomic potentials, and large benchmark datasets that reduce computational costs by orders of magnitude at close to DFT accuracy; and (3) high throughput screening pipelines for virtual and experimental screening, involving active learning and Bayesian optimisation, that have been applied to a diverse range of electrocatalytic reactions, including the hydrogen evolution reaction, the oxygen evolution/reduction reaction, and the carbon dioxide reduction reaction.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 2. A Review of Artificial Intelligence Methods for Laser-Based Diagnostics: From Measurement Physics to Autonomous Sensing Systems

- Date: `2026-10-02`
- Journal: Engineering Technology & Applied Science Research
- Link: https://doi.org/10.48084/etasr.21437
- Tags: active_learning, generative_model, h2, ml, physics_informed, review, self_supervised, uncertainty
- Authors: Saleh Mahmoud, Turki AlQemlas
- Why it matters: Laser-based diagnostic techniques are indispensable for non-intrusive, high-resolution measurements in fluid mechanics, combustion, and multiphase flows.
- Innovation: Laser-based diagnostic techniques are indispensable for non-intrusive, high-resolution measurements in fluid mechanics, combustion, and multiphase flows.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 3. Toward automated discovery with generative models multimodal learning and closed loop workflows in inverse materials design

- Date: `2026-10-01`
- Journal: Cell Reports Physical Science
- Link: https://doi.org/10.1016/j.xcrp.2026.103561
- Tags: active_learning, crystal, generative_model, h2, md, multimodal, physics_informed, review
- Authors: Anand Babu, Rogério Almeida Gouvêa, Gian‐Marco Rignanese
- Why it matters: Summary: Inverse materials design is shifting materials discovery from forward prediction to targeted proposal of candidates that satisfy objectives under physical constraints.
- Innovation: Summary: Inverse materials design is shifting materials discovery from forward prediction to targeted proposal of candidates that satisfy objectives under physical constraints.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 4. Mechanism–AI fusion in refining simulation software: A module-level review

- Date: `2026-10-01`
- Journal: Results in Engineering
- Link: https://doi.org/10.1016/j.rineng.2026.113315
- Tags: active_learning, foundation_model, h2, high_throughput, md, ml, physics_informed, review, surrogate_model, uncertainty
- Authors: Jiahang Han, Xueliang Zhao, Lijun Han
- Why it matters: Refining simulation software has remained functionally static for decades: property calculation, reaction kinetics, unit-operation modeling, and computational fluid dynamics (CFD) solving modules are hard-coded, unidirectional, and cannot be calibrated online against drifting plant conditions.
- Innovation: Refining simulation software has remained functionally static for decades: property calculation, reaction kinetics, unit-operation modeling, and computational fluid dynamics (CFD) solving modules are hard-coded, unidirectional, and cannot be calibrated online against drifting plant conditions.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 5. AIMNet2-rxn: A machine-learned potential for generalized reaction modeling on a millions-of-pathways scale

- Date: `2026-10-07`
- Journal: Science Advances
- Link: https://doi.org/10.1126/sciadv.aea1557
- Tags: dft, h2, high_throughput, interatomic_potential, md, priority_journal, transfer_learning
- Authors: Dylan M. Anstine, Qiyuan Zhao, R.I. Zubatyuk, Shuhao Zhang, Veerupaksh Singla
- Why it matters: Despite progress in machine-learned interatomic potentials (MLIPs), we demonstrate that available models lack the accuracy for diverse reaction modeling.
- Innovation: Despite progress in machine-learned interatomic potentials (MLIPs), we demonstrate that available models lack the accuracy for diverse reaction modeling.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 6. Tuning Pore Confinement and Chemistry of Fluorine-Free Membranes

- Date: `2026-10-09`
- Journal: Journal of the American Chemical Society
- Link: https://doi.org/10.1021/jacs.6c15621
- Tags: crystal, dft, h2, interatomic_potential, md, ml, priority_journal, water
- Authors: Muhammad Saad Naeem, Zan Lian, Jordi Guardià, Ranga Rohit Seemakurthi, Pol Sanz Berman
- Why it matters: Here, we optimize a fluorine-free, sustainable, and low-cost liquid crystalline poly(epichlorohydrin)membrane, based on the identification of key descriptors for proton mobility obtained using machine learning interatomic potentials (MLIPs) derived from first-principles calculations for extensive molecular dynamics.
- Innovation: Here, we optimize a fluorine-free, sustainable, and low-cost liquid crystalline poly(epichlorohydrin)membrane, based on the identification of key descriptors for proton mobility obtained using machine learning interatomic potentials (MLIPs) derived from first-principles calculations for extensive molecular dynamics.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.

### 7. Modeling Phase Separation in Polymer-Derived Silicon Carbonitride Ceramics through Extended Machine Learning Molecular Dynamics

- Date: `2026-10-06`
- Journal: ACS Nano
- Link: https://doi.org/10.1021/acsnano.6c11958
- Tags: crystal, h2, high_throughput, interatomic_potential, md, ml, polymer, priority_journal, separation, two_d_material
- Authors: Fabien Mortier, Sylvian Cadars, Olivier Masson, Mauro Boero, Guido Ori
- Why it matters: To address this issue, here, we develop and apply a machine learning interatomic potential for hydrogen-containing silicon carbonitride-based (SiCNH) ceramics, trained on a diversified database of over 9000 configurations─including amorphous models, high-temperature states, surfaces, and crystal structure predictions─to capture the full complexity of these materials.
- Innovation: To address this issue, here, we develop and apply a machine learning interatomic potential for hydrogen-containing silicon carbonitride-based (SiCNH) ceramics, trained on a diversified database of over 9000 configurations─including amorphous models, high-temperature states, surfaces, and crystal structure predictions─to capture the full complexity of these materials.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.

### 8. Closing the learning loop in lithium–sulfur batteries through physics-informed and trustworthy artificial intelligence

- Date: `2026-10-05`
- Journal: Energy and AI
- Link: https://doi.org/10.1016/j.egyai.2026.100934
- Tags: active_learning, battery, catalysis, electrolyte, high_throughput, ml, multimodal, physics_informed, review, uncertainty
- Authors: Ka Chun Li, King-cheong Antony LAM, Chi Ho WONG, Wai Kwan LIU
- Why it matters: It critically examines data infrastructure, text and multimodal extraction, descriptor learning, catalyst and electrolyte design, physics-informed state inference, degradation prognosis, autonomous experimentation, and digital twins.
- Innovation: It critically examines data infrastructure, text and multimodal extraction, descriptor learning, catalyst and electrolyte design, physics-informed state inference, degradation prognosis, autonomous experimentation, and digital twins.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 9. Explainable Machine Learning in Composite Material Design Bridging Data Driven Models and Physical Interpretability

- Date: `2026-09-24`
- Journal: International Journal of Advanced Science and Engineering
- Link: https://doi.org/10.29294/ijase.13.1.2026.7254-7283
- Tags: catalyst_descriptor, h2, ml, physics_informed, review, symbolic_regression, uncertainty
- Authors: R Elayaraja, Divya Jagadeesan, S Suresh, D Subramaniam, V. Jayasree
- Why it matters: The increasing demand of composite materials in aerospace, automotive, marine and civil engineering applications including their superior strength-to-weight ratio and customizable properties has made them invaluable in these fields [1].Iterative experimental testing and empirical rules are the traditional approaches, which are time-consuming and economically inefficient.With the advent of machine learning, material discovery, and optimization have been transformed, with the ability to predict complex material properties from limited data, and to discover novel material compositions [2][3][4].One of the strengths of ML is its ability to identify non-linear relationships in large, highdimensional datasets that a human might not be able to spot.Other methods such as deep neural ABSTRACT: Machine learning (ML) has shown significant promise in the ability to make accurate predictions of material properties and optimize formulations to improve composite material development.But many ML models are "black-box" models and this lack of interpretability of the physics is a big obstacle to their use in engineering and manufacturing applications where physical interpretability is essential.This review delves into the current state of Explainable Artificial Intelligence (XAI) methods used in the design of composite materials, which spans from prediction to understanding the physical material.Various techniques of interpretability are explained, such as SHAP (SHapley Additive exPlanations), LIME (Local Interpretable Model-agnostic Explanations), feature importance and attention mechanisms, given in the context of composite material science.The review summarizes the existing issues, new solutions, and future prospects of trustworthy ML systems which complement but do not supplant domain expertise.Multi-scale modeling, uncertainty quantification and coupling to physics-informed machine learning are highlighted.This paper is intended to be used by materials scientists, engineers and ML practitioners interested in using explainable AI to help grow the development of composites.Most of the previous reviews focus on machine learning, materials informatics or EAI in isolation.A comprehensive review of the use of explainable machine learning techniques in composite material design, manufacture, performance prediction and physics-informed modeling, however, has not yet been done.The review addresses this gap, bringing together a holistic view of the methodologies of XAI, their engineering significance and recent use in sustainable composite systems.
- Innovation: The increasing demand of composite materials in aerospace, automotive, marine and civil engineering applications including their superior strength-to-weight ratio and customizable properties has made them invaluable in these fields [1].Iterative experimental testing and empirical rules are the traditional approaches, which are time-consuming and economically inefficient.With the advent of machine learning, material discovery, and optimization have been transformed, with the ability to predict complex material properties from limited data, and to discover novel material compositions [2][3][4].One of the strengths of ML is its ability to identify non-linear relationships in large, highdimensional datasets that a human might not be able to spot.Other methods such as deep neural ABSTRACT: Machine learning (ML) has shown significant promise in the ability to make accurate predictions of material properties and optimize formulations to improve composite material development.But many ML models are "black-box" models and this lack of interpretability of the physics is a big obstacle to their use in engineering and manufacturing applications where physical interpretability is essential.This review delves into the current state of Explainable Artificial Intelligence (XAI) methods used in the design of composite materials, which spans from prediction to understanding the physical material.Various techniques of interpretability are explained, such as SHAP (SHapley Additive exPlanations), LIME (Local Interpretable Model-agnostic Explanations), feature importance and attention mechanisms, given in the context of composite material science.The review summarizes the existing issues, new solutions, and future prospects of trustworthy ML systems which complement but do not supplant domain expertise.Multi-scale modeling, uncertainty quantification and coupling to physics-informed machine learning are highlighted.This paper is intended to be used by materials scientists, engineers and ML practitioners interested in using explainable AI to help grow the development of composites.Most of the previous reviews focus on machine learning, materials informatics or EAI in isolation.A comprehensive review of the use of explainable machine learning techniques in composite material design, manufacture, performance prediction and physics-informed modeling, however, has not yet been done.The review addresses this gap, bringing together a holistic view of the methodologies of XAI, their engineering significance and recent use in sustainable composite systems.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.

### 10. Advanced engineering of inorganic semiconductor nanowires: Materials-by-design for next-generation green energy technologies

- Date: `2026-10-01`
- Journal: Energy Reviews
- Link: https://doi.org/10.1016/j.enrev.2026.100216
- Tags: active_learning, catalysis, crystal, dft, electrocatalysis, h2, md, ml, photocatalysis, review, uncertainty, water
- Authors: Sunday Temitope Oyinbo, Hoe-Gil Lee, Sikiru Oluwarotimi Ismail, Tien‐Chien Jen
- Why it matters: Inorganic semiconductor nanowires (NWs) provide an unusually versatile platform for green-energy technologies because composition, crystal phase, defects, interfaces, morphology, and dimensionality can be engineered across multiple length scales.
- Innovation: Inorganic semiconductor nanowires (NWs) provide an unusually versatile platform for green-energy technologies because composition, crystal phase, defects, interfaces, morphology, and dimensionality can be engineered across multiple length scales.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 11. Cross-chemistry battery state-of-health estimation from adaptive partial charging using interpretable physics-informed Efficient Kolmogorov-Arnold networks

- Date: `2026-10-01`
- Journal: Energy and AI
- Link: https://doi.org/10.1016/j.egyai.2026.100928
- Tags: active_learning, battery, foundation_model, h2, md, physics_informed, separation, transfer_learning, uncertainty
- Authors: Zekariyas Yohannes, Yonghong Xu, Yidi Wei, Jian Li, Boru Jia
- Why it matters: Prefix-specific Bayesian optimization (PS-BO) selects the most informative state-of-charge window for each chemistry and extracts seven voltage-based descriptors; this feed-coupled solution and dynamics networks are trained under a bounded uncertainty-weighted objective that keeps the data, physics, and monotonicity constraints balanced.
- Innovation: Prefix-specific Bayesian optimization (PS-BO) selects the most informative state-of-charge window for each chemistry and extracts seven voltage-based descriptors; this feed-coupled solution and dynamics networks are trained under a bounded uncertainty-weighted objective that keeps the data, physics, and monotonicity constraints balanced.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 12. General-purpose LLMs as constrained crystal composition generators

- Date: `2026-10-09`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02339-9
- Tags: crystal, foundation_model, generative_model, h2, high_throughput, priority_journal, transfer_learning
- Authors: Hedda Oschinski, Maximilian L. Ach, Konstantin S. Jakob, Christian Carbogno, Karsten Reuter
- Why it matters: Here, we demonstrate that such models are capable of covering entire regions of the targeted property space effectively and systematically.
- Innovation: Here, we demonstrate that such models are capable of covering entire regions of the targeted property space effectively and systematically.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 13. Digital twins for energy wells through multiscale physics-data fusion: Review, challenges, and a conceptual framework

- Date: `2026-10-07`
- Journal: Geoenergy Science and Engineering
- Link: https://doi.org/10.1016/j.geoen.2026.214860
- Tags: co2, h2, md, ml, physics_informed, review, separation, surrogate_model
- Authors: Jiapei Du, Annan Zhou, Ergün Kuru
- Why it matters: The framework outlines an integrated architecture in which molecular- and mesoscale descriptors are systematically upscaled into continuum constitutive relationships, while top-down geological and operational constraints are incorporated to ensure cross-scale physical consistency.
- Innovation: The framework outlines an integrated architecture in which molecular- and mesoscale descriptors are systematically upscaled into continuum constitutive relationships, while top-down geological and operational constraints are incorporated to ensure cross-scale physical consistency.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 14. A review on foundation models for polymer informatics

- Date: `2026-10-05`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15009949/v1
- Tags: foundation_model, generative_model, ml, polymer, review, self_supervised
- Authors: Yihan Zhu, Eric Inae, Yuhan Liu, Weijiang Li, Sobin Alosious
- Why it matters: Foundation models have emerged as a powerful paradigm for learning transferable knowledge from broad, heterogeneous data and adapting them to diverse downstream tasks, driving a growing interest in AI-accelerated scientific discovery.
- Innovation: Foundation models have emerged as a powerful paradigm for learning transferable knowledge from broad, heterogeneous data and adapting them to diverse downstream tasks, driving a growing interest in AI-accelerated scientific discovery.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 15. Beyond Scalar Objectives: Expert-Feedback-Driven Autonomous Experimentation for Scientific Discovery at the Nanoscale

- Date: `2026-10-07`
- Journal: ACS Nano
- Link: https://doi.org/10.1021/acsnano.6c09449
- Tags: active_learning, h2, ml, priority_journal, separation
- Authors: Ralph Bulanadi, Jefferey Baxter, Arpan Biswas, Hiroshi Funakubo, V. Nagarajan
- Why it matters: Bayesian optimization (BO) is among the most widely used machine learning frameworks in self-driving laboratories, but these BO-based frameworks rely on predefined scalar descriptors to guide experimentation.
- Innovation: Bayesian optimization (BO) is among the most widely used machine learning frameworks in self-driving laboratories, but these BO-based frameworks rely on predefined scalar descriptors to guide experimentation.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 16. SSCHA-based evolutionary crystal structure prediction at finite temperatures with account for quantum nuclear motion

- Date: `2026-10-09`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02333-1
- Tags: crystal, h2, interatomic_potential, priority_journal, transfer_learning
- Authors: Daniil Poletaev, Artem Oganov
- Why it matters: We demonstrate that quantum anharmonicity simplifies the free-energy landscape and is essential for the correct energy ranking of LaH 10 structures.
- Innovation: We demonstrate that quantum anharmonicity simplifies the free-energy landscape and is essential for the correct energy ranking of LaH 10 structures.
- Likely limitations: Abstract-level evidence is promising, but validation breadth is unclear without reading the full paper.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 17. Integration of density functional theory and machine learning for materials discovery in energy applications

- Date: `2026-09-22`
- Journal: Discover Chemistry.
- Link: https://doi.org/10.1007/s44371-026-00985-y
- Tags: active_learning, adsorption, battery, catalysis, dft, electrocatalysis, h2, high_throughput, ml, photocatalysis, review, uncertainty, water
- Authors: Jeslin Jebish G P
- Why it matters: Examine how DFT generated datasets, encompassing bandgap values, formation energies, adsorption energies, and electronic structure descriptors, serve as the foundation for training predictive ML models, and delineate the methodological pipeline that connects them.
- Innovation: Examine how DFT generated datasets, encompassing bandgap values, formation energies, adsorption energies, and electronic structure descriptors, serve as the foundation for training predictive ML models, and delineate the methodological pipeline that connects them.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 18. Distilling First-Principles Accuracy into Compact Machine Learning Potentials for Condensed-Phase Chemistry

- Date: `2026-10-09`
- Journal: Journal of Chemical Theory and Computation
- Link: https://doi.org/10.1021/acs.jctc.6c01131
- Tags: catalysis, dft, foundation_model, h2, interatomic_potential, md, ml, transfer_learning, water
- Authors: Sijia Chen, Niamh O'Neill, Benjamin X. Shi, Venkat Kapil
- Why it matters: We demonstrate this across three problems of increasing sampling complexity: finite-temperature NPT simulations of ice Ih, classical and path-integral simulations of liquid water over 240–370 K, and path-integral umbrella-sampling simulations of water dissociation at the anatase TiO2(101)/water interface.
- Innovation: We demonstrate this across three problems of increasing sampling complexity: finite-temperature NPT simulations of ice Ih, classical and path-integral simulations of liquid water over 240–370 K, and path-integral umbrella-sampling simulations of water dissociation at the anatase TiO2(101)/water interface.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 19. From Trial-and-Error to Closed-Loop Design: A Data-Driven Review on Biomass-Derived Carbon for Supercapacitors

- Date: `2026-10-01`
- Journal: Environmental Surfaces and Interfaces
- Link: https://doi.org/10.1016/j.esi.2026.09.004
- Tags: active_learning, electrocatalysis, generative_model, h2, high_throughput, ml, porous_material, review
- Authors: Xin Ning, Honghui Wang, Yunping Chen, Cheng Chen, Haofeng Lu
- Why it matters: Supercapacitors are vital for sustainable energy storage, and biomass-derived carbons are promising electrode materials owing to their low cost, renewability, and inherent hierarchical porosity.
- Innovation: Supercapacitors are vital for sustainable energy storage, and biomass-derived carbons are promising electrode materials owing to their low cost, renewability, and inherent hierarchical porosity.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 20. Large language models, ChatGPT, and beyond: A new paradigm for condition monitoring and prognosis in power and energy systems

- Date: `2026-10-05`
- Journal: Energy and AI
- Link: https://doi.org/10.1016/j.egyai.2026.100926
- Tags: battery, foundation_model, h2, multimodal, review, uncertainty
- Authors: Mohamed Benbouzid
- Why it matters: Large language models and related foundation models offer new capabilities for interpreting heterogeneous information, retrieving engineering knowledge, and supporting high-level decision processes in power and energy systems.
- Innovation: Large language models and related foundation models offer new capabilities for interpreting heterogeneous information, retrieving engineering knowledge, and supporting high-level decision processes in power and energy systems.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 21. A Comprehensive Review of Battery State of Health Estimation: Methods, Challenges and Future Perspectives

- Date: `2026-10-03`
- Journal: International Journal of Automotive Science And Technology
- Link: https://doi.org/10.30939/ijastech..1995891
- Tags: battery, h2, high_throughput, ml, multimodal, physics_informed, review, uncertainty
- Authors: Hakan Çoban, Koray Erhan, Mustafa Baysal
- Why it matters: Lithium-ion battery state of health (SOH) cannot be measured directly and must be inferred from capacity, resistance, voltage, current, temperature, and usage history.
- Innovation: Lithium-ion battery state of health (SOH) cannot be measured directly and must be inferred from capacity, resistance, voltage, current, temperature, and usage history.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 22. Reinforcement Learning on the Discrete Composition Channel of a Crystal Generator: Validated Gains and Reward Hacking

- Date: `2026-10-02`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2610.03880
- Tags: crystal, foundation_model, generative_model, high_throughput, md, uncertainty
- Authors: Pawan Prakash, Philipp Höllmer, Addis Fuhr, Peter Hirschfeld, P. Ganesh
- Why it matters: We introduce a reward function that raises the yield of metastable, unique and novel structures (mSUN) from 13.4% for the pretrained model to 45.5% for the reinforced model, as evaluated by a community benchmark.
- Innovation: We introduce a reward function that raises the yield of metastable, unique and novel structures (mSUN) from 13.4% for the pretrained model to 45.5% for the reinforced model, as evaluated by a community benchmark.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 23. GEODE: Symmetry-Preserving Cartesian Diffusion for Crystal Generation

- Date: `2026-10-01`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2610.01898
- Tags: crystal, equivariant_ml, generative_model, md, physics_informed
- Authors: Yuchen Lou, Alex M. Ganose
- Why it matters: We introduce Generative Equivariant Orbit Diffusion Engine (GEODE), to our knowledge the first model to combine coordinate and lattice diffusion in Cartesian space.
- Innovation: We introduce Generative Equivariant Orbit Diffusion Engine (GEODE), to our knowledge the first model to combine coordinate and lattice diffusion in Cartesian space.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 24. Artificial intelligence in microplastic and nanoplastic research: State-of-Art review from automated detection to environmental fate modeling

- Date: `2026-09-24`
- Journal: Journal of Hazardous Materials Plastics
- Link: https://doi.org/10.1016/j.hazmp.2026.100083
- Tags: force_field, h2, high_throughput, image_analysis, multimodal, physics_informed, polymer, review, uncertainty
- Authors: Jianqiao Song, Kaushik Venkiteshwaran, Shenghua Wu
- Why it matters: Microplastic and nanoplastic research has entered a data-intensive phase in which analytical throughput, interlaboratory comparability, and environmental interpretability determine whether monitoring results can support mechanistic understanding and management decisions.
- Innovation: Microplastic and nanoplastic research has entered a data-intensive phase in which analytical throughput, interlaboratory comparability, and environmental interpretability determine whether monitoring results can support mechanistic understanding and management decisions.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Map the method onto MOF structure images, spectra, isotherm curves, or generated-structure consistency checks. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Distant-domain method can be useful if it maps to a concrete MOF object such as structure images, spectra, isotherms, pore maps, or multimodal consistency checks.

### 25. Polymer Informatics in the Era of Foundation Models: From Representation to Autonomous Design

- Date: `2026-09-23`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15009334/v1
- Tags: foundation_model, generative_model, h2, polymer, review, self_supervised
- Authors: Jianxin He, Ying Li
- Why it matters: Foundation models, pretrained on broad datasets and adapted to multiple tasks, offer a way to reuse chemical knowledge across polymer property prediction and inverse design.
- Innovation: Foundation models, pretrained on broad datasets and adapted to multiple tasks, offer a way to reuse chemical knowledge across polymer property prediction and inverse design.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 26. Improved electrostatic machine learning embedding ML/MM scheme for a phosphoryl transfer reaction

- Date: `2026-10-07`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15010047/v1
- Tags: active_learning, catalysis, dft, equivariant_ml, force_field, h2, md, ml
- Authors: Laetitia Kantin, Iñaki Tuñón, Kirill Zinovjev, Élise Duboué-Dijon
- Why it matters: Here we test the Electrostatic ML Embedding (EMLE) scheme on a minimal model of RNA cleavage in water, which is already challenging due to a doubly charged reactant dissociating into two anions.
- Innovation: Here we test the Electrostatic ML Embedding (EMLE) scheme on a minimal model of RNA cleavage in water, which is already challenging due to a doubly charged reactant dissociating into two anions.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 27. OxiGen: Oxidation-State-Aware Crystal Generation

- Date: `2026-10-06`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2610.08296
- Tags: crystal, generative_model, md
- Authors: Dylan John, Kim E. Jelfs, Alex M. Ganose, Eleonora Giunchiglia
- Why it matters: Generative models have the potential to accelerate inorganic materials discovery by enabling inverse design, but generating experimentally realisable crystals remains challenging.
- Innovation: Generative models have the potential to accelerate inorganic materials discovery by enabling inverse design, but generating experimentally realisable crystals remains challenging.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 28. Machine-Learning-Driven Simulations of Hyperthermal Atomic Oxygen Impacts on (0001) Al2O3 for Low-Altitude Satellite Design.

- Date: `2026-10-08`
- Journal: PubMed
- Link: https://pubmed.ncbi.nlm.nih.gov/42848461
- Tags: active_learning, adsorption, dft, h2, interatomic_potential, md
- Authors: Nico Segreto, Јован Бошковић, Andrea Beck, Johannes Kästner
- Why it matters: We present a blueprint for developing machine-learned interatomic potentials for reactive gas-surface systems.
- Innovation: We present a blueprint for developing machine-learned interatomic potentials for reactive gas-surface systems.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 29. Tractable and Thermodynamically Consistent p K a Prediction via First-Dissociation Aggregation

- Date: `2026-10-06`
- Journal: bioRxiv (Cold Spring Harbor Laboratory)
- Link: https://doi.org/10.64898/2026.09.30.755586
- Tags: gnn, h2, high_throughput, ml, physics_informed, water
- Authors: Zhuoyan Liu, Qiuyin Zhu, Qingkun Li, Yuanxi Zhu, You Xu
- Why it matters: Here we derive an exact thermodynamic identity showing that the macroscopic first-dissociation constant is fully determined by protonated-microstate populations and unique first-deprotonation events, eliminating the deprotonated ensemble algebraically and reducing aggregation to O(n+E) operations.
- Innovation: Here we derive an exact thermodynamic identity showing that the macroscopic first-dissociation constant is fully determined by protonated-microstate populations and unique first-deprotonation events, eliminating the deprotonated ensemble algebraically and reducing aggregation to O(n+E) operations.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 30. Artificial intelligence for scanning probe microscopy: From data analysis to autonomous experimentation

- Date: `2026-10-02`
- Journal: Applied Physics Express
- Link: https://doi.org/10.35848/1882-0786/aeafac
- Tags: active_learning, foundation_model, h2, image_analysis, ml, review
- Authors: Masayuki Abe, Zhuo Diao
- Why it matters: Abstract Advanced scanning probe microscopy (SPM) measurements have traditionally required highly specialized skills, but the integration of artificial intelligence (AI) and machine learning has begun to transform how SPM is operated.
- Innovation: Abstract Advanced scanning probe microscopy (SPM) measurements have traditionally required highly specialized skills, but the integration of artificial intelligence (AI) and machine learning has begun to transform how SPM is operated.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Map the method onto MOF structure images, spectra, isotherm curves, or generated-structure consistency checks. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Distant-domain method can be useful if it maps to a concrete MOF object such as structure images, spectra, isotherms, pore maps, or multimodal consistency checks.
