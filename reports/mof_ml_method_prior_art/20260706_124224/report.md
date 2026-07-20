# Literature Update

- Generated: `2026-07-06T12:42:24`
- Profile: `mof_ml_method_prior_art`
- Since: `2016-07-08`
- Papers retained: `11`

## Overview

Collected 11 deduplicated papers for profile `mof_ml_method_prior_art`. `ML` appears in 8 papers and `DFT` in 2. `Adsorption/separation` themes appear more often (6) than `catalysis` themes (4). `Interatomic-potential` or MLIP-style work appears in 1 papers and is a notable transfer path from COF-side methods to MOFs.

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

### 1. Smart Catalyst Design: Integrating Structure–Activity Relationships with Computational and Data-Driven Approaches

- Date: `2026-04-22`
- Journal: International Journal of Creative and Open Research in Engineering and Management
- Link: https://doi.org/10.55041/ijcope.v2i4.571
- Tags: catalysis, co2, electrocatalysis, high_throughput, ml, mof, review, separation
- Authors: Ramandeep Singh Ramandeep Singh, Rekha Rana Rekha Rana, Subhi Sharma Subhi Sharma, Jeewanjot Singh Jeewanjot Singh, Isha dhiman Isha dhiman
- Why it matters: Special attention is given to the emerging approaches based on the exploitation of designer-like methods, high-throughput experimentation, and data-driven approaches, to explore huge compositional and structural spaces.
- Innovation: Special attention is given to the emerging approaches based on the exploitation of designer-like methods, high-throughput experimentation, and data-driven approaches, to explore huge compositional and structural spaces.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 2. Descriptor Adequacy as a Materials-Regime Principle in MOF Adsorption Machine Learning

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

### 3. FLAMES – A flexible and extensible code for Monte Carlo simulations of nanoporous materials

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

### 4. Applied Design Strategies for MOFs in CO 2 Capture: Balancing Stability, Selectivity, and Scalability

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

### 5. Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era

- Date: `2026-05-27`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2605.29179
- Tags: adsorption, crystal, foundation_model, generative_model, h2, mof, review, separation, water
- Authors: Reid Coyle, Shyam Chand Pal, Peter Walther, Saeun Park, Bin Feng
- Why it matters: Metal-organic frameworks (MOFs) are excellent candidates for water harvesting due to their tunable pore environments, which can be precisely engineered to capture and release water in arid conditions.
- Innovation: Metal-organic frameworks (MOFs) are excellent candidates for water harvesting due to their tunable pore environments, which can be precisely engineered to capture and release water in arid conditions.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 6. AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications

- Date: `2026-07-03`
- Journal: Frontiers in Chemistry
- Link: https://doi.org/10.3389/fchem.2026.1864044
- Tags: active_learning, adsorption, catalysis, co2, dft, electrocatalysis, h2, high_throughput, ml, mof, separation
- Authors: Sreenivas Punna, Suvarshitha Pusuluru, Madhumita Ravikumar, Farid Menaa
- Why it matters: The incorporation of artificial intelligence (AI) into energy systems has become a transformative strategy for tackling global energy related challenges, particularly energy vulnerability (EVI).
- Innovation: The incorporation of artificial intelligence (AI) into energy systems has become a transformative strategy for tackling global energy related challenges, particularly energy vulnerability (EVI).
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 7. ReadMOF: Structure-Free Semantic Embeddings from Systematic MOF Nomenclature for Machine Learning

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

### 8. ReadMOF: Structure-Free Semantic Embeddings from Systematic MOF Nomenclature for Machine Learning

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

### 9. Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents

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

### 10. An XGBoost Framework for Predicting CO2 Adsorption Performance and Adsorbent Classification

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

### 11. Comparative entropy analysis of 2D transition metal tetrahydroxyquinones via machine learning approaches

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
