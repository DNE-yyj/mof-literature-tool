# Literature Update

- Generated: `2026-07-20T14:03:57`
- Profile: `reaction_catalyst_ml_transfer`
- Since: `2016-07-22`
- Papers retained: `27`

## Overview

Collected 27 deduplicated papers for profile `reaction_catalyst_ml_transfer`. This transfer profile keeps non-MOF ML papers when they carry a concrete method signal; 27 retained papers are outside direct MOF literature. 27 papers contain transferable method tags and 4 appear in priority journals or major venue families. 18 papers also carry explicit material-system tags, helping judge whether the chemistry is close enough to MOFs.

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

### 1. Strength of Interlayer Metal–Metal Coupling as Key Active Site Configuration and Atomic Descriptor for Single-Atom Catalysts

- Date: `2026-07-09`
- Journal: Journal of the American Chemical Society
- Link: https://doi.org/10.1021/jacs.6c04989
- Tags: catalysis, catalyst_descriptor, electrocatalysis, h2, ml, priority_journal, separation, uncertainty
- Authors: Liangliang Xu, Yi-Xiang Wang, Hanxu Yao, Jinpei Huang, Zijing Li
- Why it matters: Using machine learning and data mining, we further identify local electronic-structure descriptors that enable quantitative structure-activity relationships to guide catalyst design.
- Innovation: Using machine learning and data mining, we further identify local electronic-structure descriptors that enable quantitative structure-activity relationships to guide catalyst design.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.

### 2. Strength of InterlayerMetal–Metal Couplingas Key Active Site Configuration and Atomic Descriptor for Single-AtomCatalysts

- Date: `2026-07-09`
- Journal: Figshare
- Link: https://figshare.com/articles/journal_contribution/Strength_of_Interlayer_Metal_Metal_Coupling_as_Key_Active_Site_Configuration_and_Atomic_Descriptor_for_Single-Atom_Catalysts/32948290
- Tags: catalysis, catalyst_descriptor, electrocatalysis, h2, ml, separation, uncertainty
- Authors: Liangliang Xu (3202521), Jiankang Wang (227527), Hanxu Yao, Jinpei Huang, Zijing Li (1999390)
- Why it matters: Using machine learning and data mining, we further identify local electronic-structure descriptors that enable quantitative structure–activity relationships to guide catalyst design.
- Innovation: Using machine learning and data mining, we further identify local electronic-structure descriptors that enable quantitative structure–activity relationships to guide catalyst design.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.

### 3. Accelerating Catalyst Materials Discovery With Large Artificial Intelligence Models

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

### 5. Machine Learning-Guided Discovery of PGM-Lean High-Entropy Alloys for Efficient Solar Hydrogen Evolution

- Date: `2026-07-07`
- Journal: ECS Meeting Abstracts
- Link: https://doi.org/10.1149/ma2026-01412092mtgabs
- Tags: adsorption, alloy, catalysis, catalyst_descriptor, dft, electrocatalysis, force_field, h2, high_throughput, ml, uncertainty
- Authors: Matthew Ryan Curry, Abdennaceur Karoui, Bijandra Kumar
- Why it matters: Despite this progress, the atomic-scale origins of HER activity in HEAs—specifically the geometric and electronic descriptors governing optimal hydrogen binding—remain insufficiently understood.
- Innovation: Despite this progress, the atomic-scale origins of HER activity in HEAs—specifically the geometric and electronic descriptors governing optimal hydrogen binding—remain insufficiently understood.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.

### 6. Underexplored Catalysts as General Structures: Application of Machine Learning Techniques for Reaction‐Specific Datasets

- Date: `2026-07-10`
- Journal: Angewandte Chemie
- Link: https://doi.org/10.1002/ange.8169897
- Tags: catalysis, h2, high_throughput, ml, priority_journal, reaction_dataset
- Authors: Jiajing Li, Isaiah O. Betinol, Junshan Lai, Soresu Juyo, Jolene P. Reid
- Why it matters: General catalysts are usually identified through broad experimental screening to find structures that perform reliably across many substrates and reaction classes.
- Innovation: General catalysts are usually identified through broad experimental screening to find structures that perform reliably across many substrates and reaction classes.
- Likely limitations: Catalyst generality inferred from sparse historical reaction data can still reflect reporting bias and needs targeted validation. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Rebuild the workflow on MOF catalytic reaction families with explicit scaffold generality, reporting-bias, and validation splits. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Reaction-specific small-data workflow is useful for MOF catalysis if catalyst generality, literature bias, and scaffold validation are made explicit.

### 7. Design paradigms for Pt-based electrocatalysts toward acidic oxygen reduction in proton exchange membrane fuel cells

- Date: `2026-07-08`
- Journal: Frontiers in Materials
- Link: https://doi.org/10.3389/fmats.2026.1865153
- Tags: alloy, battery, catalysis, catalyst_descriptor, h2, review
- Authors: Rong Nie, Haibin Wang, Yuan Wei, Hao Gou, Daqian Xu
- Why it matters: The widespread commercialization of proton exchange membrane fuel cells (PEMFCs) relies fundamentally on developing cost-effective, highly active Pt-based cathode electrocatalysts.
- Innovation: The widespread commercialization of proton exchange membrane fuel cells (PEMFCs) relies fundamentally on developing cost-effective, highly active Pt-based cathode electrocatalysts.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Catalytic conclusions are likely thermodynamics-heavy unless kinetics or explicit environment are included.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.

### 8. Harnessing machine learning for electrochemical CO 2 reduction: current progress and future perspectives

- Date: `2026-06-23`
- Journal: Micro Nano Science
- Link: https://doi.org/10.20517/mns.2025.06
- Tags: catalysis, co2, electrocatalysis, h2, ml, oxide, physics_informed, review, separation
- Authors: Yu Zhang, Junjun Li, Zhicheng Zhang
- Why it matters: Electrochemical carbon dioxide reduction (CO 2 RR) is regarded as a promising strategy for achieving sustainable carbon utilization, but the complexity and multi-scale characteristics of this reaction process pose significant challenges for the rational design of catalysts.The integration of machine learning (ML) with electrocatalysis can establish cross-scale connections among atomic structure, dynamic interfacial microenvironments, and macroscopic catalytic performance, thereby enabling predictive analysis of catalyst activity, product selectivity, reaction pathways, and electrochemical environment regulation.This outlook integrates recent advances in ML-assisted CO 2 RR, highlights the key challenges in data quality, feature interpretability, and multiscale integration, and proposes future directions for combining physics-informed modeling with realistic electrochemical reaction environments.With advances in ML, automated experimentation, and multi-source data integration, a self-evolving catalyst design platform is expected to be established.
- Innovation: Electrochemical carbon dioxide reduction (CO 2 RR) is regarded as a promising strategy for achieving sustainable carbon utilization, but the complexity and multi-scale characteristics of this reaction process pose significant challenges for the rational design of catalysts.The integration of machine learning (ML) with electrocatalysis can establish cross-scale connections among atomic structure, dynamic interfacial microenvironments, and macroscopic catalytic performance, thereby enabling predictive analysis of catalyst activity, product selectivity, reaction pathways, and electrochemical environment regulation.This outlook integrates recent advances in ML-assisted CO 2 RR, highlights the key challenges in data quality, feature interpretability, and multiscale integration, and proposes future directions for combining physics-informed modeling with realistic electrochemical reaction environments.With advances in ML, automated experimentation, and multi-source data integration, a self-evolving catalyst design platform is expected to be established.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Catalytic conclusions are likely thermodynamics-heavy unless kinetics or explicit environment are included.
- Next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 9. Fine-tuning large language models to generate single-atom catalyst synthesis procedures

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

### 10. Harnessing Artificial Intelligence (AI) for a greener future: a review of AI advancements in green chemistry, chemical processes and sustainable materials

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

### 11. Reactive Molecular Dynamics of Hydrogen Evolution at Charged Interfaces Using Machine Learning Potentials

- Date: `2026-07-14`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15006079/v1
- Tags: catalysis, dft, electrocatalysis, equivariant_ml, h2, interatomic_potential, md, ml, separation, two_d_material, water
- Authors: Md Sharif Khan, Oliviero Andreussi
- Why it matters: Here, we develop an equivariant machine learning interatomic potential trained on density functional theory data for electrochemically activated MoS2/water interfaces under charged conditions.
- Innovation: Here, we develop an equivariant machine learning interatomic potential trained on density functional theory data for electrochemically activated MoS2/water interfaces under charged conditions.
- Likely limitations: Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.

### 12. AI/ML-Enabled Advanced Oxidation for Real Wastewater Treatment: Mechanistic Evidence, Multi-Objective Optimization, and Scale-Up Roadmaps

- Date: `2026-06-29`
- Journal: Catalysts
- Link: https://doi.org/10.3390/catal16070596
- Tags: catalysis, h2, high_throughput, ml, review, uncertainty
- Authors: Bo Meng, Tingtao Liu, Yingning Wang, S Y Yu
- Why it matters: Advanced oxidation processes (AOPs) are widely applied to degrade recalcitrant organic contaminants in municipal effluents, industrial wastewaters, and water-reuse streams.
- Innovation: Advanced oxidation processes (AOPs) are widely applied to degrade recalcitrant organic contaminants in municipal effluents, industrial wastewaters, and water-reuse streams.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 13. Few-Shot Ensemble Learning for Catalysis and Application to Trimetallics for Oxygen Reduction

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

### 14. A green solvent screening tool for emerging materials via uncertainty aware, transformer enhanced transfer learning

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

### 15. Interpretable Machine Learning of Nanoparticle Stability through Topological Layer Embeddings

- Date: `2026-06-27`
- Journal: The Journal of Physical Chemistry A
- Link: https://doi.org/10.1021/acs.jpca.6c01508
- Tags: dft, h2, ml, symbolic_regression
- Authors: Felipe Hawthorne, Leandro Seixas, James M. Almeida, Cristiano F. Woellner, Raphael M. Tromer
- Why it matters: Here, we introduce a data-efficient and physically interpretable machine-learning framework based on a fragmented, layer-resolved descriptor that explicitly decomposes nanoparticles into surface, intermediate, and core environments using a topology-driven definition.
- Innovation: Here, we introduce a data-efficient and physically interpretable machine-learning framework based on a fragmented, layer-resolved descriptor that explicitly decomposes nanoparticles into surface, intermediate, and core environments using a topology-driven definition.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 16. A data-efficient reactive machine learning potential to accelerate automated exploration of complex reaction networks

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

### 17. Machine Learning Prediction of Thermal Properties of PHB/PHBV-Based Materials: A Quantitative Structure–Property Relationship Approach Using an Integrated Polymer Database

- Date: `2026-06-23`
- Journal: Polymers
- Link: https://doi.org/10.3390/polym18131559
- Tags: crystal, h2, high_throughput, ml, polymer, transfer_learning
- Authors: Nikolaos Sotiropoulos, Leonidas Mindrinos, Jean‐David Peltier, Konstantina Filippou, Marianna Kotzabasaki
- Why it matters: Two ML models, Random Forest (RF) and eXtreme Gradient Boosting (XGBoost), were utilized to predict values of Tg, Tc, and Tm using feature engineering methods that integrated chemistry-based descriptors with polymer-specific and experimental variables.
- Innovation: Two ML models, Random Forest (RF) and eXtreme Gradient Boosting (XGBoost), were utilized to predict values of Tg, Tc, and Tm using feature engineering methods that integrated chemistry-based descriptors with polymer-specific and experimental variables.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 18. Leveraging Hidden-Space Representations Effectively in Bayesian Optimization for Experiment Design through Dimension-Aware Hyperpriors

- Date: `2026-02-09`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.10001986/v2
- Tags: active_learning, foundation_model, gnn, h2, high_throughput, ml, uncertainty
- Authors: Guanming Chen, Maximilian Fleck, Thijs Stuyver
- Why it matters: We demonstrate that different chemical representations induce substantial variations in search-space dimensionality, which, when paired with fixed or mismatched lengthscale hyperpriors, lead to flat marginal likelihood landscapes and severely degrade surrogate learning and acquisition optimization.
- Innovation: We demonstrate that different chemical representations induce substantial variations in search-space dimensionality, which, when paired with fixed or mismatched lengthscale hyperpriors, lead to flat marginal likelihood landscapes and severely degrade surrogate learning and acquisition optimization.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 19. Machine learning approaches to optimization in chemical compound space

- Date: `2026-01-01`
- Journal: cIRcle (University of British Columbia)
- Link: http://hdl.handle.net/2429/94787
- Tags: active_learning, catalysis, h2, md, ml, physics_informed, transfer_learning
- Authors: Yun-Wen Mao
- Why it matters: This thesis develops data-driven strategies for optimization in molecular descriptor-property space, a central challenge in chemistry with applications ranging from drug discovery to catalyst design.
- Innovation: This thesis develops data-driven strategies for optimization in molecular descriptor-property space, a central challenge in chemistry with applications ranging from drug discovery to catalyst design.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 20. Hierarchical Multi-Fidelity Learning for Predicting Three-Dimensional Flame Wrinkling and Turbulent Burning Velocity

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

### 21. A GAN-Augmented Machine Learning Framework for Predicting Raman Characteristics in Carbon Nanofiber Synthesis

- Date: `2026-01-14`
- Journal: Open MIND
- Link: https://hdl.handle.net/1880/123989
- Tags: catalysis, ml, physics_informed, transfer_learning
- Authors: Amirhossein Foroughi
- Why it matters: This thesis explores a hybrid data-driven framework for predicting the structural quality of Carbon Nanofibers (CNFs) synthesized via Chemical Vapor Deposition (CVD).
- Innovation: This thesis explores a hybrid data-driven framework for predicting the structural quality of Carbon Nanofibers (CNFs) synthesized via Chemical Vapor Deposition (CVD).
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Catalytic conclusions are likely thermodynamics-heavy unless kinetics or explicit environment are included.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 22. Expert-Informed Contrastive Learning of Condition Space for Amide Coupling Reactions

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

### 23. An overview of reaction outcome prediction with physics-based and data-driven methods

- Date: `2026-01-01`
- Journal: Chemical Society Reviews
- Link: https://doi.org/10.1039/d6cs00079g
- Tags: h2, interatomic_potential, md, ml, review, separation, uncertainty
- Authors: Joonyoung F. Joung, Nicholas Casetti, Priyanka Raghavan, Connor W. Coley
- Why it matters: .
- Innovation: .
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 24. ScopeMap: An AI-Assisted, Human-in-the-Loop Workflow for Mapping Reaction Scope and Boundaries

- Date: `2026-01-16`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv-2026-kqz7d
- Tags: h2, reaction_dataset
- Authors: Jiawei Li, Xiao Xiao, Q. Yang, Baoguo Zhao, Sanzhong Luo
- Why it matters: Herein, we introduce ScopeMap, an iterative, human-in-the-loop workflow designed to efficiently map functional limits rather than merely maximizing performance.
- Innovation: Herein, we introduce ScopeMap, an iterative, human-in-the-loop workflow designed to efficiently map functional limits rather than merely maximizing performance.
- Likely limitations: Catalyst generality inferred from sparse historical reaction data can still reflect reporting bias and needs targeted validation.
- Next step: Rebuild the workflow on MOF catalytic reaction families with explicit scaffold generality, reporting-bias, and validation splits.
- MOF relevance: Reaction-specific small-data workflow is useful for MOF catalysis if catalyst generality, literature bias, and scaffold validation are made explicit.

### 25. Out-of-Distribution Generalization for Neural Physics Solvers

- Date: `2026-01-27`
- Journal: arXiv (Cornell University)
- Link: http://arxiv.org/abs/2601.19091
- Tags: h2, md, ml, uncertainty
- Authors: Zhao Wei, Chin Chun Ooi, Jian Cheng Wong, Abhishek K. Gupta, Pao-Hsiung Chiu
- Why it matters: We introduce NOVA, a route to generalizable neural physics solvers that can provide rapid, accurate solutions to scenarios even under distributional shifts in partial differential equation parameters, geometries and initial conditions.
- Innovation: We introduce NOVA, a route to generalizable neural physics solvers that can provide rapid, accurate solutions to scenarios even under distributional shifts in partial differential equation parameters, geometries and initial conditions.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 26. Expanding frontiers of complex reaction network exploration through a general reactive machine learning potential

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
