# Literature Update

- Generated: `2026-08-24T02:36:35`
- Profile: `mof_ml_method_prior_art`
- Since: `2016-08-26`
- Papers retained: `15`

## Overview

Collected 15 deduplicated papers for profile `mof_ml_method_prior_art`. `ML` appears in 13 papers and `DFT` in 4. `Catalysis` themes appear more often (11) than `adsorption/separation` themes (3). `Interatomic-potential` or MLIP-style work appears in 3 papers and is a notable transfer path from COF-side methods to MOFs.

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

### 2. Interaction topology theory deciphers multiscale codes of MOF-like materials

- Date: `2026-08-21`
- Journal: Science Advances
- Link: https://doi.org/10.1126/sciadv.aee8016
- Tags: adsorption, catalysis, h2, ml, mof, porous_material, priority_journal, self_supervised, separation, transfer_learning
- Authors: Chen 晨 Dong 董, Jian Liu, Chun‐Long Chen, Guo‐Wei Wei
- Why it matters: We develop an interaction topology theory and propose the interaction topological transformer (ITT), a data-efficient framework that captures materials information across multiple scales and levels, including structural, elemental, atomic, and pairwise-elemental organization.
- Innovation: We develop an interaction topology theory and propose the interaction topological transformer (ITT), a data-efficient framework that captures materials information across multiple scales and levels, including structural, elemental, atomic, and pairwise-elemental organization.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 3. Data-driven Design of Metal-Organic Frameworks with Tunable Negative Thermal Expansion

- Date: `2026-07-21`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2607.18594
- Tags: dft, equivariant_ml, h2, high_throughput, interatomic_potential, ml, mof
- Authors: P U Kamath, Francesco Tavani, Alin M. Elena, Théo Jaffrelot Inizan, Yen-hsu Lin
- Why it matters: Here, we comprehensively evaluate the factors influencing NTE in MOFs by utilizing a high-throughput workflow based on MACE-MP-MOF0, a machine learning interatomic potential fine-tuned for MOFs with near-ab initio accuracy, to construct PhononMOFdb, a database of phonons, inelastic neutron scattering spectra, bulk moduli, and heat capacities for over 12,000 MOFs.
- Innovation: Here, we comprehensively evaluate the factors influencing NTE in MOFs by utilizing a high-throughput workflow based on MACE-MP-MOF0, a machine learning interatomic potential fine-tuned for MOFs with near-ab initio accuracy, to construct PhononMOFdb, a database of phonons, inelastic neutron scattering spectra, bulk moduli, and heat capacities for over 12,000 MOFs.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 4. Smart Catalyst Design: Integrating Structure–Activity Relationships with Computational and Data-Driven Approaches

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

### 5. AIM 2 DAT : a python-based automated ab initio material modeling and data analysis toolkit

- Date: `2026-07-13`
- Journal: Electronic Structure
- Link: https://doi.org/10.1088/2516-1075/ae8964
- Tags: battery, dft, h2, high_throughput, ml, mof
- Authors: Holger‐Dietrich Saßnick, Joshua Edzards, Timo Reents, Caterina Cocchi
- Why it matters: Herein, we introduce the automated ab initio materials modeling and data analysis toolkit ( aim 2 dat ), a Python package offering a user-friendly interface to generate and handle big data, design high-throughput workflows based on density functional theory calculations, and analyze the output.
- Innovation: Herein, we introduce the automated ab initio materials modeling and data analysis toolkit ( aim 2 dat ), a Python package offering a user-friendly interface to generate and handle big data, design high-throughput workflows based on density functional theory calculations, and analyze the output.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 6. Chemically Meaningful Textualization Enables Explainable Validation of Metal-Organic Frameworks by Large Language Models

- Date: `2026-08-11`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2608.11283
- Tags: crystal, foundation_model, h2, high_throughput, mof
- Authors: Guobin Zhao, Xiao-Yan Li
- Why it matters: Computation-ready metal-organic framework (MOF) databases are essential for high-throughput screening, yet many reported crystal structures remain chemically unreasonable or disordered, compromising simulation fidelity.
- Innovation: Computation-ready metal-organic framework (MOF) databases are essential for high-throughput screening, yet many reported crystal structures remain chemically unreasonable or disordered, compromising simulation fidelity.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 7. Fast Isotropic Li-Ion Diffusion in Zeolitic Imidazolate Framework Glass Electrolytes for Batteries

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

- Date: `2026-07-16`
- Journal: ACS Energy Letters
- Link: https://doi.org/10.1021/acsenergylett.6c00550
- Tags: battery, co2, electrocatalysis, h2, high_throughput, ml, mof, multimodal, photocatalysis, porous_material, separation
- Authors: Hyunsoo Park, Tianshu Li, Ashna Jose, Seung‐Jae Shin, Aron Walsh
- Why it matters: We present a data-driven workflow integrating hybrid quantum chemical calculations with a multimodal AI model (MOFTransformer) to efficiently predict oxidation and reduction potentials for over 270,000 known and hypothetical MOFs.
- Innovation: We present a data-driven workflow integrating hybrid quantum chemical calculations with a multimodal AI model (MOFTransformer) to efficiently predict oxidation and reduction potentials for over 270,000 known and hypothetical MOFs.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 10. Metal-organic frameworks (MOF)-mediated improvement of cotton germination and early seedling resilience under salinity stress through explainable machine learning and non-destructive terahertz time-domain spectroscopy (THz-TDS)

- Date: `2026-08-20`
- Journal: Industrial Crops and Products
- Link: https://doi.org/10.1016/j.indcrop.2026.124180
- Tags: catalyst_descriptor, h2, md, ml, mof, symbolic_regression, water
- Authors: Muhammad Tanveer Altaf, Kholoud Elmabruk, Salma Naimatullah Soomro, Sabeen Rehman Soomro, Tülay Aksoy
- Why it matters: Cobalt-based metal-organic framework (Co-MOF) and nickel-cobalt bimetallic MOF (Ni-Co-MOF) systems were evaluated for their effects on cotton germination under saline conditions induced through NaCl seed priming treatments.
- Innovation: Cobalt-based metal-organic framework (Co-MOF) and nickel-cobalt bimetallic MOF (Ni-Co-MOF) systems were evaluated for their effects on cotton germination under saline conditions induced through NaCl seed priming treatments.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 11. Green and sustainable metal–organic framework catalysts for biodiesel production: Progress and energy circularity perspectives

- Date: `2026-08-01`
- Journal: Green Technologies and Sustainability
- Link: https://doi.org/10.1016/j.grets.2026.100449
- Tags: catalysis, electrocatalysis, h2, mof, photocatalysis, review, uncertainty
- Authors: Lucky Adjun Pratama, Sumarno Sumarno, Mahfud Mahfud
- Why it matters: The global transition toward low-carbon and resource-efficient energy systems has increased the demand for sustainable catalytic technologies in biodiesel production.
- Innovation: The global transition toward low-carbon and resource-efficient energy systems has increased the demand for sustainable catalytic technologies in biodiesel production.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Catalytic conclusions are likely thermodynamics-heavy unless kinetics or explicit environment are included.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 12. Metal–Organic Frameworks in Food Biotechnology: Opportunities, Challenges, and Future Perspectives for Probiotic Delivery, Precision Fermentation, and Circular Food Systems

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

### 13. Large language model agents accelerate inverse design of metal-organic frameworks for gas separation

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

### 14. ReadMOF: Structure-Free Semantic Embeddings from Systematic MOF Nomenclature for Machine Learning

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

### 15. ReadMOF: Structure-Free Semantic Embeddings from Systematic MOF Nomenclature for Machine Learning

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
