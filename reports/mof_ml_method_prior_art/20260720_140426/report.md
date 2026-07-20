# Literature Update

- Generated: `2026-07-20T14:04:26`
- Profile: `mof_ml_method_prior_art`
- Since: `2016-07-22`
- Papers retained: `15`

## Overview

Collected 15 deduplicated papers for profile `mof_ml_method_prior_art`. `ML` appears in 12 papers and `DFT` in 4. `Adsorption/separation` themes appear more often (7) than `catalysis` themes (6). `Interatomic-potential` or MLIP-style work appears in 2 papers and is a notable transfer path from COF-side methods to MOFs.

## Innovation Patterns

- Data-driven screening is increasingly paired with physically grounded descriptors rather than pure geometry-only filters.
- Machine-learning models are commonly used as surrogates for expensive adsorption, electronic-structure, or catalytic calculations.
- DFT remains the main source of labels, descriptors, or mechanistic interpretation even in ML-heavy studies.

## Common Gaps

- Many screening papers still rely on idealized, defect-free structures and do not fully capture flexibility, humidity, or multicomponent conditions.
- ML papers often leave transferability and uncertainty outside the training distribution only partially resolved.
- Catalysis papers frequently identify thermodynamic trends without equally strong kinetic or explicit-environment treatment.

## Next Opportunities

- Connect adsorption descriptors to humid, multicomponent, and process-level targets instead of reporting only uptake/selectivity.
- For catalysis, combine DFT, microkinetics, and uncertainty-aware ML rather than stopping at static intermediate energetics.
- For transferable COF-side methods, port them to MOFs by adding node-aware descriptors, charge treatment, and local cluster corrections around metal sites.

## Paper Briefs

### 1. The impact of spurious imaginary phonon modes on thermal properties of Metal-organic Frameworks

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

### 2. Smart Catalyst Design: Integrating Structure–Activity Relationships with Computational and Data-Driven Approaches

- Date: `2026-04-22`
- Journal: International Journal of Creative and Open Research in Engineering and Management
- Link: https://doi.org/10.55041/ijcope.v2i4.571
- Tags: catalysis, catalyst_descriptor, co2, electrocatalysis, high_throughput, ml, mof, review, separation
- Authors: Ramandeep Singh Ramandeep Singh, Rekha Rana Rekha Rana, Subhi Sharma Subhi Sharma, Jeewanjot Singh Jeewanjot Singh, Isha dhiman Isha dhiman
- Why it matters: Special attention is given to the emerging approaches based on the exploitation of designer-like methods, high-throughput experimentation, and data-driven approaches, to explore huge compositional and structural spaces.
- Innovation: Special attention is given to the emerging approaches based on the exploitation of designer-like methods, high-throughput experimentation, and data-driven approaches, to explore huge compositional and structural spaces.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 3. AIM 2 DAT: A Python-based Automated Ab Initio MaterialModeling and Data Analysis Toolkit

- Date: `2026-07-11`
- Journal: Electronic Structure
- Link: https://doi.org/10.1088/2516-1075/ae8964
- Tags: battery, dft, h2, high_throughput, ml, mof
- Authors: Holger‐Dietrich Saßnick, Joshua Edzards, Timo Reents, Caterina Cocchi
- Why it matters: Herein, we introduce the Automated Ab Initio&#xD;Materials Modeling and Data Analysis Toolkit (aim 2 dat), a Python package offering a user-friendly interface to generate and handle big data, design high-throughput workflows based on density functional theory calculations, and analyze the output.
- Innovation: Herein, we introduce the Automated Ab Initio&#xD;Materials Modeling and Data Analysis Toolkit (aim 2 dat), a Python package offering a user-friendly interface to generate and handle big data, design high-throughput workflows based on density functional theory calculations, and analyze the output.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 4. Metal-organic frameworks (MOFs) based adsorbents for efficient removal of antibiotic pollutants from water

- Date: `2026-07-08`
- Journal: Frontiers in Materials
- Link: https://doi.org/10.3389/fmats.2026.1865413
- Tags: adsorption, equivariant_ml, mof, porous_material, review, water
- Authors: Kosar Hikmat Hama Aziz
- Why it matters: Antibiotics in aquatic environments pose serious risks to ecosystems and human health due to their continuous release from pharmaceutical industries, hospitals, and urban wastewater.
- Innovation: Antibiotics in aquatic environments pose serious risks to ecosystems and human health due to their continuous release from pharmaceutical industries, hospitals, and urban wastewater.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 5. Descriptor Adequacy as a Materials-Regime Principle in MOF Adsorption Machine Learning

- Date: `2026-07-03`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15002252/v2
- Tags: adsorption, force_field, h2, high_throughput, ml, mof, separation, uncertainty
- Authors: Hossein Alimardani, Shayan Abaei, Mehrdad Asgari
- Why it matters: Machine learning is changing how metal--organic frameworks (MOFs) are screened for gas storage and separation, but its reliability depends on a basic question: does the descriptor contain the physics that controls the adsorption property?
- Innovation: Machine learning is changing how metal--organic frameworks (MOFs) are screened for gas storage and separation, but its reliability depends on a basic question: does the descriptor contain the physics that controls the adsorption property?
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 6. FLAMES – A flexible and extensible code for Monte Carlo simulations of nanoporous materials

- Date: `2026-06-11`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15004623/v1
- Tags: adsorption, cof, dft, force_field, gcmc, h2, interatomic_potential, md, mof, porous_material, zeolite
- Authors: Felipe Lopes Oliveira, Holger‐Dietrich Saßnick, Guillaume Maurin
- Why it matters: Here, we introduce FLAMES (Flexible Lattice Adsorption by Monte Carlo Engine Simulation), a new software package designed to perform Monte Carlo-based simulations of nanoporous materials using MLIPs and other energy calculation methods, paving the way for more accurate and physically realistic molecular simulations.
- Innovation: Here, we introduce FLAMES (Flexible Lattice Adsorption by Monte Carlo Engine Simulation), a new software package designed to perform Monte Carlo-based simulations of nanoporous materials using MLIPs and other energy calculation methods, paving the way for more accurate and physically realistic molecular simulations.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 7. Applied Design Strategies for MOFs in CO 2 Capture: Balancing Stability, Selectivity, and Scalability

- Date: `2026-06-01`
- Journal: ChemistrySelect
- Link: https://doi.org/10.1002/slct.73531
- Tags: co2, h2, high_throughput, ml, mof, oxide, porous_material, review, separation
- Authors: Richa Vinayak
- Why it matters: ABSTRACT Metal–organic frameworks (MOFs) have become promising materials for capturing carbon dioxide from industrial sources and the atmosphere due to their adjustable porosity, high surface areas, and customizable chemical properties.
- Innovation: ABSTRACT Metal–organic frameworks (MOFs) have become promising materials for capturing carbon dioxide from industrial sources and the atmosphere due to their adjustable porosity, high surface areas, and customizable chemical properties.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 8. AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications

- Date: `2026-07-03`
- Journal: Frontiers in Chemistry
- Link: https://doi.org/10.3389/fchem.2026.1864044
- Tags: active_learning, adsorption, catalysis, catalyst_descriptor, co2, dft, electrocatalysis, h2, high_throughput, ml, mof, separation
- Authors: Sreenivas Punna, Suvarshitha Pusuluru, Madhumita Ravikumar, Farid Menaa
- Why it matters: The incorporation of artificial intelligence (AI) into energy systems has become a transformative strategy for tackling global energy related challenges, particularly energy vulnerability (EVI).
- Innovation: The incorporation of artificial intelligence (AI) into energy systems has become a transformative strategy for tackling global energy related challenges, particularly energy vulnerability (EVI).
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 9. Data-Driven Design of Metal-Organic Frameworks for Photoelectrochemical Reactions

- Date: `2026-07-15`
- Journal: ACS Energy Letters
- Link: https://doi.org/10.1021/acsenergylett.6c00550
- Tags: battery, electrocatalysis, h2, high_throughput, ml, mof, multimodal, photocatalysis, porous_material, separation
- Authors: Hyunsoo Park, Tianshu Li, Ashna Jose, Seung‐Jae Shin, Aron Walsh
- Why it matters: We present a data-driven workflow integrating hybrid quantum chemical calculations with a multimodal AI model (MOFTransformer) to efficiently predict oxidation and reduction potentials for over 270,000 known and hypothetical MOFs.
- Innovation: We present a data-driven workflow integrating hybrid quantum chemical calculations with a multimodal AI model (MOFTransformer) to efficiently predict oxidation and reduction potentials for over 270,000 known and hypothetical MOFs.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 10. Large language model agents accelerate inverse design of metal-organic frameworks for gas separation

- Date: `2026-07-12`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2607.10559
- Tags: active_learning, foundation_model, gcmc, generative_model, h2, high_throughput, ml, mof, separation
- Authors: Zhaolin Hu, Hehe Fan, Wangyihan Guo, Meng Xu, Chenhao Rao
- Why it matters: Here, we present LEMO Agent, a large-language-model agent framework for closed-loop inverse design of gas-separation MOFs in MOFid space.
- Innovation: Here, we present LEMO Agent, a large-language-model agent framework for closed-loop inverse design of gas-separation MOFs in MOFid space.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 11. ReadMOF: Structure-Free Semantic Embeddings from Systematic MOF Nomenclature for Machine Learning

- Date: `2026-04-13`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15001888/v1
- Tags: foundation_model, h2, high_throughput, ml, mof
- Authors: Kewei Zhu, Cameron Wilson, Bartosz Mazur, Yi Li, Ashleigh M. Chester
- Why it matters: Here we introduce ReadMOF, which is, to our knowledge, the first nomenclature-free machine learning framework that leverages these names to model structure-property relationships without requiring atomic coordinates or connectivity graphs.
- Innovation: Here we introduce ReadMOF, which is, to our knowledge, the first nomenclature-free machine learning framework that leverages these names to model structure-property relationships without requiring atomic coordinates or connectivity graphs.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 12. ReadMOF: Structure-Free Semantic Embeddings from Systematic MOF Nomenclature for Machine Learning

- Date: `2026-04-12`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2604.10568
- Tags: foundation_model, h2, high_throughput, ml, mof
- Authors: Kewei Zhu, Cameron Wilson, Bartosz Mazur, Yi Li, Ashleigh M. Chester
- Why it matters: Here we introduce ReadMOF, which is, to our knowledge, the first nomenclature-free machine learning framework that leverages these names to model structure-property relationships without requiring atomic coordinates or connectivity graphs.
- Innovation: Here we introduce ReadMOF, which is, to our knowledge, the first nomenclature-free machine learning framework that leverages these names to model structure-property relationships without requiring atomic coordinates or connectivity graphs.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 13. Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents

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

### 14. An XGBoost Framework for Predicting CO2 Adsorption Performance and Adsorbent Classification

- Date: `2026-06-26`
- Journal: Processes
- Link: https://doi.org/10.3390/pr14132081
- Tags: adsorption, co2, h2, high_throughput, ml, mof, oxide, polymer, porous_material, separation, water, zeolite
- Authors: Chitresh Kumar Bhargava, B. Tiwari, Prakhar Bhatnagar, Sparsh Attri, Preeti Mittal
- Why it matters: In this project, a machine-learning-based framework is developed to predict CO2 adsorption capacity and identify the most suitable adsorbent material using process and material parameters.
- Innovation: In this project, a machine-learning-based framework is developed to predict CO2 adsorption capacity and identify the most suitable adsorbent material using process and material parameters.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 15. Comparative entropy analysis of 2D transition metal tetrahydroxyquinones via machine learning approaches

- Date: `2026-01-31`
- Journal: Scientific Reports
- Link: https://doi.org/10.1038/s41598-026-37731-4
- Tags: h2, ml, mof, oxide
- Authors: Muhammad Irfan, Nabeela Bashir, AbdulGuddoos S. A. Gaid, Turke Althobaiti, Hamood Ur Rehman
- Why it matters: To this end, we develop and compare three machine learning based regression models: logarithmic, random forest, and XGBoost.
- Innovation: To this end, we develop and compare three machine learning based regression models: logarithmic, random forest, and XGBoost.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.
