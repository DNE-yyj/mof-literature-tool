# Literature Update

- Generated: `2026-09-28T06:49:04`
- Profile: `mof_ml_method_prior_art`
- Since: `2016-09-30`
- Papers retained: `10`

## Overview

Collected 10 deduplicated papers for profile `mof_ml_method_prior_art`. `ML` appears in 7 papers and `DFT` in 3. `Catalysis` themes appear more often (11) than `adsorption/separation` themes (5). `Interatomic-potential` or MLIP-style work appears in 1 papers and is a notable transfer path from COF-side methods to MOFs.

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

### 1. AI-accelerated discovery of altermagnetic metal-organic frameworks via interpretable machine learning

- Date: `2026-09-14`
- Journal: npj Computational Materials
- Link: https://doi.org/10.1038/s41524-026-02323-3
- Tags: dft, h2, high_throughput, ml, mof, priority_journal, symbolic_regression
- Authors: Yue Ran, Jingyi Duan, Yikai Chen, Wei Jiang, Yugui Yao
- Why it matters: Altermagnetism has emerged as a third class of collinear magnetism, yet its exploration remains largely confined to inorganic materials.
- Innovation: Altermagnetism has emerged as a third class of collinear magnetism, yet its exploration remains largely confined to inorganic materials.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 2. Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion

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

### 3. Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks via Machine Learning-Symbolic Regression

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

### 4. Smart Catalyst Design: Integrating Structure–Activity Relationships with Computational and Data-Driven Approaches

- Date: `2026-04-22`
- Journal: International Journal of Creative and Open Research in Engineering and Management
- Link: https://doi.org/10.55041/ijcope.v2i4.571
- Tags: catalysis, catalyst_descriptor, co2, electrocatalysis, high_throughput, ml, mof, review, separation
- Authors: Ramandeep Singh Ramandeep Singh, Rekha Rana, Subhi Sharma Subhi Sharma, Jeewanjot Singh Jeewanjot Singh, Isha Dhiman
- Why it matters: Special attention is given to the emerging approaches based on the exploitation of designer-like methods, high-throughput experimentation, and data-driven approaches, to explore huge compositional and structural spaces.
- Innovation: Special attention is given to the emerging approaches based on the exploitation of designer-like methods, high-throughput experimentation, and data-driven approaches, to explore huge compositional and structural spaces.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 5. AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications

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

### 6. Advances in Hydrocarbon Adsorptive Materials: Rational Design, Adsorption Chemistry, and Frontier Applications

- Date: `2026-09-23`
- Journal: ChemistrySelect
- Link: https://doi.org/10.1002/slct.74487
- Tags: adsorption, catalysis, h2, ml, mof, porous_material, review, separation, zeolite
- Authors: Junyan Chen, Bin Guan, Lei Zhu, Tiankui Zhu, Shiying Chang
- Why it matters: ABSTRACT This review comprehensively and critically examines the research progress on hydrocarbon (HC) adsorbent materials in three key application scenarios: engine cold‐start HC emission control, industrial VOC recovery, and petrochemical HC separation.
- Innovation: ABSTRACT This review comprehensively and critically examines the research progress on hydrocarbon (HC) adsorbent materials in three key application scenarios: engine cold‐start HC emission control, industrial VOC recovery, and petrochemical HC separation.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Catalytic conclusions are likely thermodynamics-heavy unless kinetics or explicit environment are included.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 7. From sparse quantum-computing data to atomistic simulation with universal machine-learning interatomic potentials

- Date: `2026-09-18`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2609.21536
- Tags: adsorption, alloy, dft, h2, interatomic_potential, md, mof, transfer_learning, water
- Authors: Tuan Minh Do, Yuichiro Yoshida, Kenji Ishihara, Wataru Mizukami
- Why it matters: We demonstrate the approach for three chemically distinct applications: the Menshutkin reaction, water adsorption in the metal-organic framework HKUST-1, and CO hopping on a high-entropy-alloy nanoparticle.
- Innovation: We demonstrate the approach for three chemically distinct applications: the Menshutkin reaction, water adsorption in the metal-organic framework HKUST-1, and CO hopping on a high-entropy-alloy nanoparticle.
- Likely limitations: Abstract-level evidence is promising, but validation breadth is unclear without reading the full paper.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 8. Machine learning approach for MOF-based photocatalytic CO2 reduction to fuels

- Date: `2026-09-01`
- Journal: Energy Conversion and Management X
- Link: https://doi.org/10.1016/j.ecmx.2026.102268
- Tags: catalysis, co2, h2, ml, mof, photocatalysis, review, separation, uncertainty
- Authors: Udit Madhusoodan, Mavin Jason Pinto, S. Shanmuga Priya, I. Thirunavukkarasu, K. Sudhakar
- Why it matters: Herein, we present a machine learning framework trained on 417 experimental data points compiled from the MOF-based photocatalytic CO 2 reduction literature.
- Innovation: Herein, we present a machine learning framework trained on 417 experimental data points compiled from the MOF-based photocatalytic CO 2 reduction literature.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 9. Recent advances in the strategies of developing water-resistant catalysts for the removal of atmospheric pollutants

- Date: `2026-09-11`
- Journal: Greenverse Science
- Link: https://doi.org/10.20517/greenvsci.2026.13
- Tags: adsorption, catalysis, catalyst_descriptor, crystal, h2, md, mof, oxide, review, water
- Authors: Xiaoyang Wang, Xin Zhou, Mengwei Hua, Zhiquan Hou, Wenming Sun
- Why it matters: In the catalytic oxidation of atmospheric pollutants such as volatile organic compounds (VOCs), catalyst deactivation induced by water under realistic operating conditions has emerged as a critical bottleneck constraining the large-scale application of this technology.
- Innovation: In the catalytic oxidation of atmospheric pollutants such as volatile organic compounds (VOCs), catalyst deactivation induced by water under realistic operating conditions has emerged as a critical bottleneck constraining the large-scale application of this technology.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Test humid or multicomponent conditions and connect material metrics to process-level targets.
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
