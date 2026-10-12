# Literature Update

- Generated: `2026-10-12T07:19:20`
- Profile: `mof_ml_method_prior_art`
- Since: `2016-10-14`
- Papers retained: `12`

## Overview

Collected 12 deduplicated papers for profile `mof_ml_method_prior_art`. `ML` appears in 5 papers and `DFT` in 4. `Adsorption/separation` themes appear more often (6) than `catalysis` themes (4). `Interatomic-potential` or MLIP-style work appears in 1 papers and is a notable transfer path from COF-side methods to MOFs.

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

### 1. A Machine-Learned Interatomic Potential Free-Energy Surface for the First Step of MIL-101(Cr) Secondary Building Unit Formation

- Date: `2026-09-29`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2609.38518
- Tags: dft, equivariant_ml, foundation_model, h2, interatomic_potential, md, mof, transfer_learning, water
- Authors: Orlando A. Mendible-Barreto, Yamil J. Colón
- Why it matters: Metal-organic framework (MOF) self-assembly mechanisms remain poorly characterized because ab initio molecular dynamics (AIMD) are accurate but too computationally expensive to converge the free-energy surfaces (FES) that govern secondary building unit (SBU) nucleation and growth.
- Innovation: Metal-organic framework (MOF) self-assembly mechanisms remain poorly characterized because ab initio molecular dynamics (AIMD) are accurate but too computationally expensive to converge the free-energy surfaces (FES) that govern secondary building unit (SBU) nucleation and growth.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 2. Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks via Machine Learning-Symbolic Regression

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

### 3. AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications

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

### 4. From Computation-Ready to Claim-Ready: An Evidence Framework for MOF Machine Learning

- Date: `2026-10-04`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15009825/v1
- Tags: crystal, force_field, h2, ml, mof
- Authors: Natalia Lydia Papadantonaki, Shayan Abaei, Joshua Emptoz, Mehrdad Asgari
- Why it matters: Metal–organic frameworks (MOFs) make this problem especially clear: one nominal material may appear as an experimental crystal, an activated simulation structure, a charge-assigned model or a row of descriptors, while information about protonation, counterions, coordination environment or measurement conditions may disappear along the way.
- Innovation: Metal–organic frameworks (MOFs) make this problem especially clear: one nominal material may appear as an experimental crystal, an activated simulation structure, a charge-assigned model or a row of descriptors, while information about protonation, counterions, coordination environment or measurement conditions may disappear along the way.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 5. GLASS: Global Latent Aggregation with Slot-based Set Decoding for Scalable All-Atom Crystal Generation

- Date: `2026-09-29`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2609.37158
- Tags: crystal, equivariant_ml, generative_model, mof
- Authors: Hendrik Kraß, Seyed Mohamad Moosavi, Mathias Niepert
- Why it matters: To resolve this challenge, we introduce GLASS---Global Latent Aggregation with Slot-based Set Decoding, which encodes structures in a permutation-invariant global latent space and learns their distribution via flow matching.
- Innovation: To resolve this challenge, we introduce GLASS---Global Latent Aggregation with Slot-based Set Decoding, which encodes structures in a permutation-invariant global latent space and learns their distribution via flow matching.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 6. Hybrid sampling approach to machine-learning potentials for gas adsorption: Hydrogen adsorption in MOF-303

- Date: `2026-10-05`
- Journal: Physical Review Materials
- Link: https://doi.org/10.1103/d5b5-66b6
- Tags: adsorption, catalysis, co2, dft, force_field, gcmc, h2, high_throughput, md, mof, oxide, porous_material, separation
- Authors: Kartik Sau, Ikutaro Hamada, Tamio Ikeshoji, Yiming Lu, Susmita Roy
- Why it matters: Here, we present an approach to generating machine-learning potentials (MLPs) tailored for grand canonical Monte Carlo (GCMC) simulations of gas adsorption.
- Innovation: Here, we present an approach to generating machine-learning potentials (MLPs) tailored for grand canonical Monte Carlo (GCMC) simulations of gas adsorption.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 7. Machine learning-driven insights into metal-organic frameworks desalination: Predictive Modeling and sensitivity analysis for material selection

- Date: `2026-09-29`
- Journal: AI Thermal Fluids
- Link: https://doi.org/10.1016/j.aitf.2026.100055
- Tags: adsorption, h2, ml, mof
- Authors: Sajedeh Rooholamini, Farzin Hosseinifard, Mohsen Salimi, Amirhossein Amirfakhraei, Mona Zamani Pedram
- Why it matters: This study applies machine learning (ML) techniques to classify metal–organic frameworks (MOFs) for adsorption-based desalination considering multiple adsorption-related properties.
- Innovation: This study applies machine learning (ML) techniques to classify metal–organic frameworks (MOFs) for adsorption-based desalination considering multiple adsorption-related properties.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Directly relevant to MOF work, but likely less novel for this transfer-focused profile.

### 8. Recent advances in the strategies of developing water-resistant catalysts for the removal of atmospheric pollutants

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

### 9. Large language model agents accelerate inverse design of metal-organic frameworks for gas separation

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

### 10. From surface area to smog abatement: A data-mined structure-property framework of adsorbents with pores

- Date: `2026-10-07`
- Journal: Next Chemical Engineering
- Link: https://doi.org/10.1016/j.nxcen.2026.100120
- Tags: adsorption, catalyst_descriptor, cof, h2, mof, oxide, polymer, separation, water, zeolite
- Authors: Namra Nawaz, Muhammad Adeel Ishfaq, Iqra Khalid, Maryam Basharat, Aamer Saeed
- Why it matters: Urban smog is a multi-faceted pollution problem consisting of fine particles, VOCs, NO x and SO x , as well as the link between traffic and other sources, and the effects of meteorology.
- Innovation: Urban smog is a multi-faceted pollution problem consisting of fine particles, VOCs, NO x and SO x , as well as the link between traffic and other sources, and the effects of meteorology.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 11. Unraveling the mechanism for phonon based heat transport in metal-organic frameworks

- Date: `2026-10-05`
- Journal: TUGraz OPEN Library (Graz University of Technology)
- Link: https://doi.org/10.3217/56qk5-xwr37
- Tags: crystal, dft, equivariant_ml, force_field, h2, mof
- Authors: Florian P. Lindner, Marco Moser, Lukas Legenstein, Sandro Wieser, Egbert Zojer
- Why it matters: Data repository to "Unraveling the Mechanism for Phonon Based Heat Transport in Metal-Organic Frameworks" by Florian P.
- Innovation: Data repository to "Unraveling the Mechanism for Phonon Based Heat Transport in Metal-Organic Frameworks" by Florian P.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.

### 12. MOF-VERIFY: A Failure-Aware Agentic Harness for MOF Hypothesis Verification

- Date: `2026-10-02`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2610.03056
- Tags: force_field, foundation_model, h2, high_throughput, mof
- Authors: Donghyun Lee, Taehoon Lee, Geonhee Ahn, Jieun Kim, Jihyun Park
- Why it matters: We introduce a diagnostic benchmark with four task families covering structural grounding, synthesis-condition verification, evidence-sufficiency verification, and MLIP-based computational verification.
- Innovation: We introduce a diagnostic benchmark with four task families covering structural grounding, synthesis-condition verification, evidence-sufficiency verification, and MLIP-based computational verification.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF relevance: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.
