# Literature Update

- Generated: `2026-09-07T06:04:22`
- Profile: `mof_ml_method_prior_art`
- Since: `2016-09-09`
- Papers retained: `18`

## Overview

Collected 18 deduplicated papers for profile `mof_ml_method_prior_art`. `ML` appears in 15 papers and `DFT` in 5. `Catalysis` themes appear more often (12) than `adsorption/separation` themes (6). `Interatomic-potential` or MLIP-style work appears in 3 papers and is a notable transfer path from COF-side methods to MOFs.

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

### 1. Computational and ML methods in MOF based supercapacitors - from mechanistic understanding to future materials design

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

### 2. uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks

- Date: `2026-08-28`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2608.28100
- Tags: adsorption, crystal, dft, equivariant_ml, foundation_model, h2, high_throughput, interatomic_potential, md, ml, mof, separation, uncertainty
- Authors: Théo Jaffrelot Inizan, P.S. Kamath, Alin M. Elena, Kristin A. Persson
- Why it matters: We introduce uMOF, a three-part contribution addressing this gap.
- Innovation: We introduce uMOF, a three-part contribution addressing this gap.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 3. Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion

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

### 4. Generalized Machine Learning Potentials for Predicting Low-Pressure Water Adsorption in Flexible Al-Based Metal–Organic Frameworks

- Date: `2026-08-25`
- Journal: Journal of Chemical Theory and Computation
- Link: https://doi.org/10.1021/acs.jctc.6c01162
- Tags: adsorption, dft, equivariant_ml, force_field, foundation_model, h2, high_throughput, interatomic_potential, md, ml, mof, separation, transfer_learning, water
- Authors: Yutao Li, Xiaoqi Zhang, Xin Jin, Berend Smit
- Why it matters: Classical force fields, such as UFF, often fail to capture the strong, directional hydrogen-bonding interactions between water and MOFs, while high-throughput density functional theory (DFT) calculations are computationally prohibitive.
- Innovation: Classical force fields, such as UFF, often fail to capture the strong, directional hydrogen-bonding interactions between water and MOFs, while high-throughput density functional theory (DFT) calculations are computationally prohibitive.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 5. Active Sites in Motion: Principles, Materials Platforms, and Sustainable Applications in Heterogeneous Catalysis

- Date: `2026-08-30`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15008045/v1
- Tags: catalysis, co2, h2, high_throughput, ml, mof, oxide, review, separation, zeolite
- Authors: John Sackey, Nana Abena Owusuwaa Ansah, Mohammed Islam Tahseen, Nelson Donkor
- Why it matters: Heterogeneous catalysis stands as a cornerstone of modern chemical science, underpinning the sustainable production of fuels, chemicals, and materials across industries ranging from petroleum refining to environmental protection.
- Innovation: Heterogeneous catalysis stands as a cornerstone of modern chemical science, underpinning the sustainable production of fuels, chemicals, and materials across industries ranging from petroleum refining to environmental protection.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 6. Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks via Machine Learning-Symbolic Regression

- Date: `2026-08-15`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2608.14990
- Tags: adsorption, catalyst_descriptor, co2, h2, md, ml, mof, symbolic_regression, transfer_learning
- Authors: Yimin Shao, Shengluo Ma, Shenghong Ju, Yijun Shi, Wei Li
- Why it matters: This work presents a machine learning-symbolic regression (ML-SR) strategy to develop a physically interpretable formula for predicting low pressure CO2 adsorption capacity in hypothetical metal-organic frameworks (hMOFs).
- Innovation: This work presents a machine learning-symbolic regression (ML-SR) strategy to develop a physically interpretable formula for predicting low pressure CO2 adsorption capacity in hypothetical metal-organic frameworks (hMOFs).
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 7. Smart Catalyst Design: Integrating Structure–Activity Relationships with Computational and Data-Driven Approaches

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

### 8. Machine learning approach for MOF-based photocatalytic CO2 reduction to fuels

- Date: `2026-09-01`
- Journal: Energy Conversion and Management X
- Link: https://doi.org/10.1016/j.ecmx.2026.102268
- Tags: catalysis, co2, h2, ml, mof, photocatalysis, review, separation, uncertainty
- Authors: Udit Madhusoodan, M.R. Pinto, S. Shanmuga Priya, I. Thirunavukkarasu, K. Sudhakar
- Why it matters: Herein, we present a machine learning framework trained on 417 experimental data points compiled from the MOF-based photocatalytic CO 2 reduction literature.
- Innovation: Herein, we present a machine learning framework trained on 417 experimental data points compiled from the MOF-based photocatalytic CO 2 reduction literature.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 9. AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications

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

### 10. Predicting CO₂ adsorption in Cu- and Zn-metal-organic frameworks using a permutation-invariant deep learning framework

- Date: `2026-08-22`
- Journal: Next Materials
- Link: https://doi.org/10.1016/j.nxmate.2026.103167
- Tags: adsorption, co2, h2, high_throughput, ml, mof, oxide, porous_material, separation
- Authors: Jaka Fajar Fatriansyah, Rayhan Hagel Safa, Sharen Ardyana Khintani, Andiko Putra Pratama Krisdiawan, Agrin Febrian Pradana
- Why it matters: The proposed framework combines string-based chemical descriptors (SMILES and SELFIES, with one-hot and ordinal encodings) with physical descriptors (pore-limiting diameter, largest cavity diameter, gravimetric and volumetric surface areas, void fraction, topology, and catenation), and incorporating a permutation-invariant aggregator over multiple MOFs linkers.
- Innovation: The proposed framework combines string-based chemical descriptors (SMILES and SELFIES, with one-hot and ordinal encodings) with physical descriptors (pore-limiting diameter, largest cavity diameter, gravimetric and volumetric surface areas, void fraction, topology, and catenation), and incorporating a permutation-invariant aggregator over multiple MOFs linkers.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 11. Fast Isotropic Li-Ion Diffusion in Zeolitic Imidazolate Framework Glass Electrolytes for Batteries

- Date: `2026-08-07`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2608.06902
- Tags: battery, crystal, electrolyte, h2, interatomic_potential, md, ml, mof
- Authors: Yong Li, Tao Du, Timothée Jamin, Zhencai Li, Kasper Tolborg
- Why it matters: This is realized by using a machine learning interatomic potential to simulate Li+ transport in crystalline and glassy ZIF-4 and ZIF-62.
- Innovation: This is realized by using a machine learning interatomic potential to simulate Li+ transport in crystalline and glassy ZIF-4 and ZIF-62.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 12. GFN1-xTB-Assisted Machine Learning for Electronic Structure Screening of Metal–Organic Frameworks

- Date: `2026-08-11`
- Journal: Journal of Chemical Theory and Computation
- Link: https://doi.org/10.1021/acs.jctc.6c00979
- Tags: crystal, dft, high_throughput, ml, mof
- Authors: Ashna Jose, Aron Walsh
- Why it matters: Metal-organic frameworks (MOFs) are versatile materials with tunable crystal structures, morphologies, and chemistries, offering diverse physical and chemical properties.
- Innovation: Metal-organic frameworks (MOFs) are versatile materials with tunable crystal structures, morphologies, and chemistries, offering diverse physical and chemical properties.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 13. Green metal–organic frameworks for circular soil remediation through pollutant sequestration and nutrient regeneration

- Date: `2026-09-01`
- Journal: Discover Green Chemistry
- Link: https://doi.org/10.1007/s44509-026-00032-0
- Tags: adsorption, h2, mof, review, uncertainty
- Authors: Irfan Haidri, Aneeza Ishfaq, Athakorn Promwee, Faisal Mahmood
- Why it matters: Agricultural soils are increasingly threatened by contamination from pesticides, herbicides, and potentially toxic metals, posing significant risks to food security, ecosystem functioning, and long-term agricultural sustainability.
- Innovation: Agricultural soils are increasingly threatened by contamination from pesticides, herbicides, and potentially toxic metals, posing significant risks to food security, ecosystem functioning, and long-term agricultural sustainability.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 14. Metal–Organic Frameworks in Food Biotechnology: Opportunities, Challenges, and Future Perspectives for Probiotic Delivery, Precision Fermentation, and Circular Food Systems

- Date: `2026-07-31`
- Journal: Nanomaterials
- Link: https://doi.org/10.3390/nano16150946
- Tags: catalysis, ml, mof, review, separation, uncertainty
- Authors: Huy Loc Nguyen
- Why it matters: Metal-organic frameworks (MOFs) have emerged as a versatile class of porous nanomaterials with exceptional surface area, tunable pore architectures, and customizable chemical functionalities, creating new opportunities for advanced food applications.
- Innovation: Metal-organic frameworks (MOFs) have emerged as a versatile class of porous nanomaterials with exceptional surface area, tunable pore architectures, and customizable chemical functionalities, creating new opportunities for advanced food applications.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 15. Large language model agents accelerate inverse design of metal-organic frameworks for gas separation

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

### 16. ReadMOF: Structure-Free Semantic Embeddings from Systematic MOF Nomenclature for Machine Learning

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

### 17. ReadMOF: Structure-Free Semantic Embeddings from Systematic MOF Nomenclature for Machine Learning

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

### 18. An LLM agent for end-to-end computational materials discovery

- Date: `2026-08-20`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2608.20434
- Tags: crystal, foundation_model, high_throughput, mof, separation
- Authors: Chen Yuntong, Huang Ju, Liu Yu, Zhao Dan, Sun Mingqi
- Why it matters: We report MAESTRO, a large language model (LLM) agent system capable of executing the entire screening pipeline for metal-organic frameworks (MOFs).
- Innovation: We report MAESTRO, a large language model (LLM) agent system capable of executing the entire screening pipeline for metal-organic frameworks (MOFs).
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.
