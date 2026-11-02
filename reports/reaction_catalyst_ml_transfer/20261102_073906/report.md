# Literature Update

- Generated: `2026-11-02T07:39:06`
- Profile: `reaction_catalyst_ml_transfer`
- Since: `2016-11-04`
- Papers retained: `28`

## Overview

Collected 28 deduplicated papers for profile `reaction_catalyst_ml_transfer`. This transfer profile keeps non-MOF ML papers when they carry a concrete method signal; 28 retained papers are outside direct MOF literature. 28 papers contain transferable method tags and 5 appear in priority journals or major venue families. 23 papers also carry explicit material-system tags, helping judge whether the chemistry is close enough to MOFs.

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
- Tags: active_learning, catalysis, foundation_model, h2, high_throughput, interatomic_potential, ml, multimodal, priority_journal, review
- Authors: Di Zhang, Yuanzheng Chen, Chuanyu Liu, Y. H. Liu, Hongliang Xin
- Why it matters: The integration of artificial intelligence (AI) into catalysis is fundamentally reshaping the research paradigm of catalyst discovery.
- Innovation: The integration of artificial intelligence (AI) into catalysis is fundamentally reshaping the research paradigm of catalyst discovery.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 2. From Atoms to Reactors: A Critical Review of a Decade of Machine Learning in Heterogeneous Catalysis (2017–2026)

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

### 3. Machine learning approaches for electrocatalyst design in water splitting: a review for green hydrogen production

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

### 5. Machine learning-accelerated inverse design of energy materials: A critical review of graph neural networks, physics-informed models, and generative AI for batteries, perovskite solar cells, and electrocatalysts

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

### 6. Explicit Spin Regulation as an Emerging Design Paradigm in Heterogeneous Catalysis

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

### 7. Closing the learning loop in lithium–sulfur batteries through physics-informed and trustworthy artificial intelligence

- Date: `2026-10-05`
- Journal: Energy and AI
- Link: https://doi.org/10.1016/j.egyai.2026.100934
- Tags: active_learning, battery, catalysis, electrolyte, high_throughput, ml, multimodal, physics_informed, review, uncertainty
- Authors: Ka Chun Li, King-cheong Antony LAM, Chi Ho Wong, Wai Kwan LIU
- Why it matters: It critically examines data infrastructure, text and multimodal extraction, descriptor learning, catalyst and electrolyte design, physics-informed state inference, degradation prognosis, autonomous experimentation, and digital twins.
- Innovation: It critically examines data infrastructure, text and multimodal extraction, descriptor learning, catalyst and electrolyte design, physics-informed state inference, degradation prognosis, autonomous experimentation, and digital twins.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 8. Machine Learning‐Assisted Discovery of Unconventional Molybdenum Nitride Nano‐Facets as Hydrogen Evolution Electrocatalysts

- Date: `2026-10-29`
- Journal: Small Methods
- Link: https://doi.org/10.1002/smtd.71163
- Tags: catalysis, dft, h2, ml, priority_journal, uncertainty
- Authors: Xutao Gao, Chun Kit Chan, Eric Pok Man Kan, Edmund C. M. Tse
- Why it matters: To accelerate the identification of energetically favourable high‐Miller‐index facets of Mo nitrides, we complement our DFT approach with a machine learning (ML) model trained on computed results for low‐Miller‐index facets.
- Innovation: To accelerate the identification of energetically favourable high‐Miller‐index facets of Mo nitrides, we complement our DFT approach with a machine learning (ML) model trained on computed results for low‐Miller‐index facets.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 9. Enhanced Oxygen Reduction of Biatom Catalysts on g-CN with Heteroatom Doped: A Theoretical Investigation by Density Functional Theory and Machine Learning

- Date: `2026-10-22`
- Journal: ACS Omega
- Link: https://doi.org/10.1021/acsomega.6c08354
- Tags: catalysis, catalyst_descriptor, dft, h2, high_throughput, ml
- Authors: Yiran Wang, Riming Hu, Jiaxiang Shang, Ming Qiu
- Why it matters: Herein, by employing density functional theory (DFT) calculations and machine-learning (ML) algorithms, we propose a data-driven high-throughput design approach for the rapid screening of ORR catalysts consisting of 3d, 4d, and 5d transition metal dimers (TM2) inserted in pristine and heteroatom (S, C, B, P)-doped g-CN support with excellent activity.
- Innovation: Herein, by employing density functional theory (DFT) calculations and machine-learning (ML) algorithms, we propose a data-driven high-throughput design approach for the rapid screening of ORR catalysts consisting of 3d, 4d, and 5d transition metal dimers (TM2) inserted in pristine and heteroatom (S, C, B, P)-doped g-CN support with excellent activity.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.

### 10. Charge Transfer Mediators in Photoelectrochemical Water Splitting: From Interfacial Regulation to Rational Design

- Date: `2026-10-09`
- Journal: Advanced Materials
- Link: https://doi.org/10.1002/adma.75313
- Tags: catalysis, electrocatalysis, force_field, h2, oxide, photocatalysis, priority_journal, review, two_d_material, uncertainty, water
- Authors: Yurou Song, Yuye Jiao, Wenjuan Yan, Xin Jin, Jungang Hou
- Why it matters: Photoelectrochemical (PEC) water splitting is a promising route for solar-to-chemical energy conversion and storage, yet its efficiency remains limited by interfacial charge recombination, inefficient carrier extraction, and sluggish reaction kinetics.
- Innovation: Photoelectrochemical (PEC) water splitting is a promising route for solar-to-chemical energy conversion and storage, yet its efficiency remains limited by interfacial charge recombination, inefficient carrier extraction, and sluggish reaction kinetics.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 11. Assessing the Transferability of General-Purpose MachineLearning Interatomic Potentials for Heterogeneous Catalysis with HetCat26

- Date: `2026-09-24`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2609.30621
- Tags: adsorption, catalysis, dft, equivariant_ml, foundation_model, h2, high_throughput, interatomic_potential, ml, oxide
- Authors: Alexandre Peuch, Giaan Kler-Young, Kaifeng Niu, Jinwoo Hwang, Manos Mavrikakis
- Why it matters: Here, we introduce HetCat26, a collection of benchmark tests designed to assess pre-trained MLIPs across key aspects of catalytic modeling, including surface energetics, metal-metal oxide interactions, adsorption, and catalytic reaction networks.
- Innovation: Here, we introduce HetCat26, a collection of benchmark tests designed to assess pre-trained MLIPs across key aspects of catalytic modeling, including surface energetics, metal-metal oxide interactions, adsorption, and catalytic reaction networks.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 12. Accelerating green heterocyclic synthesis: Convergence of AI , automation, and sustainable chemistry

- Date: `2026-10-14`
- Journal: Bulletin of the Korean Chemical Society
- Link: https://doi.org/10.1002/bkcs.70227
- Tags: equivariant_ml, ml, review, uncertainty
- Authors: Noor Aisyah Ahmad Shah, Amirreza Mottafegh, Su‐Hyun Yoo, Jongwoon Kim, Minseon Byeon
- Why it matters: Abstract Heterocyclic compounds are among the most prevalent scaffolds in bioactive molecules, with approximately 82% of small‐molecule drugs approved by the US Food and Drug Administration (FDA) during 2013–2023 containing nitrogen heterocycles.
- Innovation: Abstract Heterocyclic compounds are among the most prevalent scaffolds in bioactive molecules, with approximately 82% of small‐molecule drugs approved by the US Food and Drug Administration (FDA) during 2013–2023 containing nitrogen heterocycles.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Representation gains depend on whether periodicity, long-range electrostatics, and porous-framework topology are handled.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 13. Pathways for the integration of bioenergetic and food production: An artificial intelligence-assisted review

- Date: `2026-10-06`
- Journal: Energy Nexus
- Link: https://doi.org/10.1016/j.nexus.2026.100880
- Tags: catalyst_descriptor, high_throughput, review, uncertainty
- Authors: Yolvi Prada Millán, Manuel Francisco Polanco Puerta, ABÍLIO J. F. N. SOBRAL, G. Ojeda
- Why it matters: ABSTRACT The application of agricultural biomass as a renewable energy source is garnering global attention, particularly for its contribution to the circular economy.
- Innovation: ABSTRACT The application of agricultural biomass as a renewable energy source is garnering global attention, particularly for its contribution to the circular economy.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.

### 14. Machine Learning-Guided Design of Cu-Based Single-Atom Alloy Nanoclusters for Selective CO2 Electroreduction

- Date: `2026-10-29`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv.15011300/v1
- Tags: adsorption, alloy, catalyst_descriptor, co2, dft, electrocatalysis, high_throughput, ml
- Authors: Luyuan Wang, Jielin Chen, Wenjie Du, Jingwei Liu, Yongguang Zhang
- Why it matters: To clarify these effects, we synergistically couple high-throughput density functional theory (DFT) calculations and machine learning (ML) to evaluate *CO adsorption across 1,944 small Cu-SAAs nanocluster candidates.
- Innovation: To clarify these effects, we synergistically couple high-throughput density functional theory (DFT) calculations and machine learning (ML) to evaluate *CO adsorption across 1,944 small Cu-SAAs nanocluster candidates.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.

### 15. Toward Mild Conditions for N2 Activation: Progress and Challenges from Nitrogenase to Biomimetic Artificial Catalysts

- Date: `2026-10-29`
- Journal: ACS Omega
- Link: https://doi.org/10.1021/acsomega.6c07548
- Tags: catalysis, h2, review, two_d_material, uncertainty
- Authors: Li Zhao, Xiaofan Liu, Peixin Li, Qiuyue Wang, Yanyan Xi
- Why it matters: Abstract Nitrogen (N2), as the most abundant gas in the atmosphere, poses a long-standing challenge in chemistry and biochemistry due to its high bond energy (≈941 kJ·mol–1) and thus low reactivity under mild conditions.
- Innovation: Abstract Nitrogen (N2), as the most abundant gas in the atmosphere, poses a long-standing challenge in chemistry and biochemistry due to its high bond energy (≈941 kJ·mol–1) and thus low reactivity under mild conditions.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Catalytic conclusions are likely thermodynamics-heavy unless kinetics or explicit environment are included.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 16. Structure–Activity Relationships in Phloroglucinol‐Bridged Binuclear Versus Mononuclear Iron/Cobalt Phthalocyanine Electrocatalysts for the Oxygen Reduction Reaction: A Combined Experimental and Computational Investigation

- Date: `2026-10-28`
- Journal: ChemistrySelect
- Link: https://doi.org/10.1002/slct.74969
- Tags: adsorption, catalysis, catalyst_descriptor, dft, h2, photocatalysis
- Authors: Palesa Mathese Phooko, Aselefech Sorsa Wotango, Siraye Esubalew Debebe, Getachew Adam Workneh
- Why it matters: Critically, density functional theory (DFT) calculations of O 2 adsorption free energy correlated quadratically with experimental half‐wave potentials ( R 2 = 0.997), and the Fe dz 2 orbital energy emerged as a reliable electronic descriptor of activity, with nitro‐substituted bimetallic FeCoPc exhibiting a narrow HOMO–LUMO gap (∼1.05 eV).
- Innovation: Critically, density functional theory (DFT) calculations of O 2 adsorption free energy correlated quadratically with experimental half‐wave potentials ( R 2 = 0.997), and the Fe dz 2 orbital energy emerged as a reliable electronic descriptor of activity, with nitro‐substituted bimetallic FeCoPc exhibiting a narrow HOMO–LUMO gap (∼1.05 eV).
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.

### 17. From electronic descriptors to durable design: a multi-scale review of catalysts for LOHC dehydrogenation

- Date: `2026-10-25`
- Journal: Colloids and Interface Science Communications
- Link: https://doi.org/10.1016/j.colcom.2026.100924
- Tags: adsorption, alloy, catalysis, catalyst_descriptor, h2, ml, oxide, review, separation
- Authors: Ruolan Du, Yuanzhe Li
- Why it matters: This review provides a mechanism-focused synthesis connecting atomic-scale electronic descriptors to catalyst formulation and reactor performance.
- Innovation: This review provides a mechanism-focused synthesis connecting atomic-scale electronic descriptors to catalyst formulation and reactor performance.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.

### 18. A green solvent screening tool for emerging materials via uncertainty aware, transformer enhanced transfer learning

- Date: `2026-09-28`
- Journal: Scientific Reports
- Link: https://doi.org/10.1038/s41598-026-72415-z
- Tags: battery, catalysis, h2, high_throughput, ml, transfer_learning, uncertainty
- Authors: Ioannis Kouroudis, Simon Ternes, Zhaosu Gu, Gohar Ali Siddiqui, Marina Ustinova
- Why it matters: Overall, we augment data on solubility descriptors by up to two orders of magnitude with high-quality predictions.
- Innovation: Overall, we augment data on solubility descriptors by up to two orders of magnitude with high-quality predictions.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 19. Fine-tuning large language models to generate single-atom catalyst synthesis procedures

- Date: `2026-06-19`
- Journal: Communications Chemistry
- Link: https://doi.org/10.1038/s42004-026-02046-y
- Tags: catalysis, foundation_model, h2, review, transfer_learning
- Authors: Manu Suvarna, Matteo Manica, Fillipo Ficarra, Andres M Bran, Andrea Ruiz‐Ferrando
- Why it matters: We demonstrate the model's practicality through a user interface allowing researchers to query procedures tailored to their design conditions.
- Innovation: We demonstrate the model's practicality through a user interface allowing researchers to query procedures tailored to their design conditions.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Catalytic conclusions are likely thermodynamics-heavy unless kinetics or explicit environment are included.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 20. Physics-Guided Design of Ammonia Decomposition Catalysts with Interpretable Machine Learning

- Date: `2026-10-09`
- Journal: Research Square
- Link: https://doi.org/10.21203/rs.3.rs-11284169/v1
- Tags: catalysis, dft, h2, high_throughput, ml, symbolic_regression
- Authors: Pragyansh Singh, Jiaqi Yang, Fanglin Che
- Why it matters: Abstract Rational catalyst design for ammonia decomposition requires navigating coupled structural and electronic effects that govern reaction energetics across a large configurational space.
- Innovation: Abstract Rational catalyst design for ammonia decomposition requires navigating coupled structural and electronic effects that govern reaction energetics across a large configurational space.
- Likely limitations: Likely sensitive to training-set coverage and transferability across chemistries. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Add kinetics, explicit environment effects, and active-site reconstruction checks. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF relevance: Potentially useful as a neighboring-method reference.

### 21. Ioc-Mldroid: a Hybrid Approach for Detection of Android Based Malicious Applications Using Indicators of Compromise (Iocs) and Machine Learning

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

### 22. ReactionAtlas: Ab origine exploration of chemical reaction networks with machine learning

- Date: `2026-06-29`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2606.30778
- Tags: catalysis, dft, force_field, generative_model, ml
- Authors: Stefan Gugler, Max Eissler, Khaled Kahouli, Klaus Robert Müller
- Why it matters: We introduce ReactionAtlas, which builds a reaction network $\textit{ab origine}$ from a handful of seed molecules and without hand-crafted rules.
- Innovation: We introduce ReactionAtlas, which builds a reaction network $\textit{ab origine}$ from a handful of seed molecules and without hand-crafted rules.
- Likely limitations: Generative candidates may need explicit topology, charge-balance, and synthesizability constraints before MOF transfer. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.

### 23. Feature Selection in Multivariate Linear Regression Models for Data-Efficient Reaction Optimization

- Date: `2026-09-04`
- Journal: ACS Catalysis
- Link: https://doi.org/10.1021/acscatal.6c04292
- Tags: catalysis, h2, high_throughput, separation, transfer_learning
- Authors: Alexandre A. Schoepfer, Rubén Laplaza, Jérôme Waser, Clémence Corminbœuf
- Why it matters: Abstract We introduce NaviCat ReaFS (reaction feature selection), a framework for testing and supporting multivariate linear regression models for reaction optimization in small, heterogeneous datasets, where overfitting risk is high and additional experiments are costly.
- Innovation: Abstract We introduce NaviCat ReaFS (reaction feature selection), a framework for testing and supporting multivariate linear regression models for reaction optimization in small, heterogeneous datasets, where overfitting risk is high and additional experiments are costly.
- Likely limitations: Screening conclusions may depend on idealized structures, force fields, and missing defects/flexibility. Catalytic conclusions are likely thermodynamics-heavy unless kinetics or explicit environment are included.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 24. Selenium‐Induced Interplay Between Processing, Phase Stability, and Hydrogen Evolution in Multicomponent Pentlandites

- Date: `2026-10-23`
- Journal: ChemElectroChem
- Link: https://doi.org/10.1002/celc.70335
- Tags: adsorption, catalyst_descriptor, dft, electrocatalysis, h2, separation
- Authors: Maciej Kubowicz, Miłosz Kożusznik, Piotr Rusiniak, Joanna Klich‐Kafel, Mathias Smialkowski
- Why it matters: Hydrogen evolution reaction (HER) performance of selenium‐rich multicomponent pentlandites was investigated using the Co 9 −x −y Fe x Ni y S 4 Se 4 series prepared as powders, as‐cast ingots, and induction‐hot‐pressed pellets.
- Innovation: Hydrogen evolution reaction (HER) performance of selenium‐rich multicomponent pentlandites was investigated using the Co 9 −x −y Fe x Ni y S 4 Se 4 series prepared as powders, as‐cast ingots, and induction‐hot‐pressed pellets.
- Likely limitations: Descriptor transfer depends on whether the proposed active-site model remains physically faithful in MOF node or defect environments. Electronic-structure trends may be stronger than finite-temperature dynamics, solvent, or kinetics.
- Next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.

### 25. DASyR-LLM: Domain-Aware Symbolic Regression with LLMs for Kinetic Model Discovery

- Date: `2026-08-05`
- Journal: arXiv (Cornell University)
- Link: https://arxiv.org/abs/2608.05120
- Tags: catalysis, foundation_model, h2, ml, symbolic_regression
- Authors: Roberto Aliaga Medina, Paulina Quintanilla, Ehecatl Antonio del Rio‐Chanona
- Why it matters: Here, we introduce an LLM-guided SR framework, embedding an LLM module within an iterative SR algorithm for automated kinetic model discovery.
- Innovation: Here, we introduce an LLM-guided SR framework, embedding an LLM module within an iterative SR algorithm for automated kinetic model discovery.
- Likely limitations: Pretraining benefits may fade for underrepresented MOF metal nodes, defects, or guest-loaded structures. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF relevance: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.

### 26. Automated Exploration of Complex Reaction Networks Accelerated by a Data-Efficient Machine Learning Potential

- Date: `2025-10-30`
- Journal: ChemRxiv
- Link: https://doi.org/10.26434/chemrxiv-2025-sm7f3
- Tags: active_learning, catalysis, dft, h2, high_throughput, interatomic_potential, md, ml, separation
- Authors: Guoao Li, Haobo Ling, C. Joanna Su, Zhengxuan Liu, Guoqiang Wang
- Why it matters: Here we present an integrated molecular dynamics/coordinate driving-active learning (MD/CD-AL) framework that efficiently samples diverse reactive configurations to construct MDCD20, a curated dataset of ~1.4 million H/C/N/O structures with radical species covered.
- Innovation: Here we present an integrated molecular dynamics/coordinate driving-active learning (MD/CD-AL) framework that efficiently samples diverse reactive configurations to construct MDCD20, a curated dataset of ~1.4 million H/C/N/O structures with radical species covered.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 27. Expanding frontiers of complex reaction network exploration through a general reactive machine learning potential

- Date: `2025-05-29`
- Journal: Research Square
- Link: https://doi.org/10.21203/rs.3.rs-6458754/v1
- Tags: active_learning, force_field, h2, high_throughput, interatomic_potential, md, ml
- Authors: Shuhua Li, Guoao Li, Haobo Ling, Guoqiang Wang, Manyi Yang
- Why it matters: Here, we introduce an MD/CD-AL framework integrating molecular dynamics/coordinate driving (MD/CD) method with active learning to generate the MDCD20 dataset that encompasses diverse reactive configurations with up to 20 heavy atoms.
- Innovation: Here, we introduce an MD/CD-AL framework integrating molecular dynamics/coordinate driving (MD/CD) method with active learning to generate the MDCD20 dataset that encompasses diverse reactive configurations with up to 20 heavy atoms.
- Likely limitations: Acquisition functions and uncertainty estimates may be poorly calibrated outside the original chemistry domain. Likely sensitive to training-set coverage and transferability across chemistries.
- Next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- MOF relevance: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.

### 28. Artificial intelligence-driven platform for catalytic reactor discovery and optimization applied to carbon dioxide valorization

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
