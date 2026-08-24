# Method Transfer Novelty Report

- Generated: `2026-08-24T02:36:06`
- Logic: non-MOF transfer scans provide candidate ideas; recent MOF literature checks current adoption; long-horizon MOF prior art checks older adoption.

## Source Runs

- Recent MOF literature: profile `mof_latest_custom`, since `2025-08-24`, papers `0`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/weekly_mof_latest/20260824_023606/report.md`
- Cross-material ML transfer: profile `materials_ml_transfer`, since `2023-08-25`, papers `30`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/materials_ml_transfer/20260824_023611/report.md`
- Reaction/catalyst ML transfer: profile `reaction_catalyst_ml_transfer`, since `2016-08-26`, papers `30`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/reaction_catalyst_ml_transfer/20260824_023623/report.md`
- Long-horizon MOF method prior art: profile `mof_ml_method_prior_art`, since `2016-08-26`, papers `15`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/mof_ml_method_prior_art/20260824_023635/report.md`

## Triage Summary

- Fresh MOF transfer candidates: `4`
- Older MOF prior art exists: `54`
- Already active in recent MOF literature: `0`

## Method-Class Baseline

| Method class | Candidate transfer scans | Recent MOF | Long-horizon MOF prior art |
|---|---:|---:|---:|
| active learning / Bayesian optimization | 20 | 0 | 2 |
| catalyst active-site descriptor | 6 | 0 | 3 |
| equivariant ML | 5 | 0 | 1 |
| foundation or pretrained model | 12 | 0 | 4 |
| generative / diffusion / inverse design | 14 | 0 | 1 |
| graph neural network | 11 | 0 | 0 |
| ML interatomic potential | 10 | 0 | 3 |
| multimodal or literature-mining model | 10 | 0 | 1 |
| physics-informed ML | 9 | 0 | 0 |
| self-supervised learning | 3 | 0 | 1 |
| surrogate or multi-fidelity model | 5 | 0 | 0 |
| symbolic regression / descriptor discovery | 4 | 0 | 1 |
| transfer learning / domain adaptation | 10 | 0 | 1 |
| uncertainty / OOD | 18 | 0 | 2 |

## Transfer Opportunities

### 1. [Fresh MOF transfer candidate] Redefining Tropical Photovoltaics: An AI–DFT-Driven Physics-Constrained Framework Linking Electronic Structure, Climate Response, and Device-Level Performance in CsPbI3 Perovskites

- Journal/date: Engineering Research Express; `2026-08-21`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1088/2631-8695/ae9cfe
- Method tags: graph neural network, physics-informed ML
- Transfer distance: adjacent materials
- Candidate MOF route: Benchmark the representation on periodic MOF graphs with explicit node/linker chemistry and pore topology.
- MOF transfer note: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
- Suggested next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 2. [Fresh MOF transfer candidate] TiO2-facet-dependent reconstruction of Pt nanoparticles during CO oxidation

- Journal/date: Nature Communications; `2026-08-08`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1038/s41467-026-76568-3
- Method tags: graph neural network
- Transfer distance: adjacent materials
- Candidate MOF route: Benchmark the representation on periodic MOF graphs with explicit node/linker chemistry and pore topology.
- MOF transfer note: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
- Suggested next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 3. [Fresh MOF transfer candidate] Ioc-Mldroid: a Hybrid Approach for Detection of Android Based Malicious Applications Using Indicators of Compromise (Iocs) and Machine Learning

- Journal/date: i-manager's Journal on Computer Science; `2027-06-15`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.26634/jcom.14.1.1372
- Method tags: surrogate or multi-fidelity model
- Transfer distance: distant method analogy
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 4. [Fresh MOF transfer candidate] Hierarchical Multi-Fidelity Learning for Predicting Three-Dimensional Flame Wrinkling and Turbulent Burning Velocity

- Journal/date: arXiv (Cornell University); `2026-05-06`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://arxiv.org/abs/2605.08232
- Method tags: surrogate or multi-fidelity model
- Transfer distance: distant method analogy
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 5. [Older MOF prior art exists] Integration of Machine Learning and Solid-State Chemistry for the Discovery of Electrochemical Materials for Fuel Cells and Electrolyzers

- Journal/date: Zenodo (CERN European Organization for Nuclear Research); `2026-08-20`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.5281/zenodo.22021890
- Method tags: active learning / Bayesian optimization, generative / diffusion / inverse design, graph neural network, physics-informed ML
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)

### 6. [Older MOF prior art exists] Integration of Machine Learning and Solid-State Chemistry for the Discovery of Electrochemical Materials for Fuel Cells and Electrolyzers

- Journal/date: Zenodo (CERN European Organization for Nuclear Research); `2026-08-20`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.5281/zenodo.22021889
- Method tags: active learning / Bayesian optimization, generative / diffusion / inverse design, graph neural network, physics-informed ML
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)

### 7. [Older MOF prior art exists] Machine learning-accelerated inverse design of energy materials: A critical review of graph neural networks, physics-informed models, and generative AI for batteries, perovskite solar cells, and electrocatalysts

- Journal/date: Next Materials; `2026-07-30`
- Candidate source: Cross-material ML transfer; Reaction/catalyst ML transfer
- Link: https://doi.org/10.1016/j.nxmate.2026.102969
- Method tags: active learning / Bayesian optimization, generative / diffusion / inverse design, graph neural network, physics-informed ML, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - uncertainty / OOD: Green and sustainable metal–organic framework catalysts for biodiesel production: Progress and energy circularity perspectives (Green Technologies and Sustainability, 2026-08-01)

### 8. [Older MOF prior art exists] Strength of Interlayer Metal–Metal Coupling as Key Active Site Configuration and Atomic Descriptor for Single-Atom Catalysts

- Journal/date: Journal of the American Chemical Society; `2026-07-09`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1021/jacs.6c04989
- Method tags: catalyst active-site descriptor, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt active-site model-selection and descriptor mining to MOF metal nodes, defects, bimetallic sites, or local-field catalytic motifs.
- MOF transfer note: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.
- Suggested next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - catalyst active-site descriptor: Metal-organic frameworks (MOF)-mediated improvement of cotton germination and early seedling resilience under salinity stress through explainable machine learning and non-destructive terahertz time-domain spectroscopy (THz-TDS) (Industrial Crops and Products, 2026-08-20)
  - catalyst active-site descriptor: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - catalyst active-site descriptor: Smart Catalyst Design: Integrating Structure–Activity Relationships with Computational and Data-Driven Approaches (International Journal of Creative and Open Research in Engineering and Management, 2026-04-22)

### 9. [Older MOF prior art exists] Autonomous laboratories for sustainable nanomaterials discovery

- Journal/date: Next Materials; `2026-07-23`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1016/j.nxmate.2026.102883
- Method tags: active learning / Bayesian optimization, foundation or pretrained model, generative / diffusion / inverse design, graph neural network, multimodal or literature-mining model, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - foundation or pretrained model: Chemically Meaningful Textualization Enables Explainable Validation of Metal-Organic Frameworks by Large Language Models (arXiv (Cornell University), 2026-08-11)

### 10. [Older MOF prior art exists] Data-driven design of carbon dots: Property prediction, optimization, and prospects for autonomous discovery

- Journal/date: Chemical Engineering Journal Advances; `2026-08-01`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1016/j.ceja.2026.101404
- Method tags: active learning / Bayesian optimization, generative / diffusion / inverse design, multimodal or literature-mining model, uncertainty / OOD
- Transfer distance: distant method analogy
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - multimodal or literature-mining model: Data-Driven Design of Metal-Organic Frameworks for Photoelectrochemical Reactions (ACS Energy Letters, 2026-07-16)

### 11. [Older MOF prior art exists] Machine learning approaches for electrocatalyst design in water splitting: a review for green hydrogen production

- Journal/date: Frontiers in Chemistry; `2026-07-31`
- Candidate source: Cross-material ML transfer; Reaction/catalyst ML transfer
- Link: https://doi.org/10.3389/fchem.2026.1894425
- Method tags: active learning / Bayesian optimization, catalyst active-site descriptor, generative / diffusion / inverse design, graph neural network
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt active-site model-selection and descriptor mining to MOF metal nodes, defects, bimetallic sites, or local-field catalytic motifs.
- MOF transfer note: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.
- Suggested next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - catalyst active-site descriptor: Metal-organic frameworks (MOF)-mediated improvement of cotton germination and early seedling resilience under salinity stress through explainable machine learning and non-destructive terahertz time-domain spectroscopy (THz-TDS) (Industrial Crops and Products, 2026-08-20)

### 12. [Older MOF prior art exists] Graph-theoretic active learning for the closed-loop discovery of stochastic heterogeneous composites

- Journal/date: PLoS ONE; `2026-08-18`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1371/journal.pone.0353692
- Method tags: active learning / Bayesian optimization, generative / diffusion / inverse design, physics-informed ML, surrogate or multi-fidelity model
- Transfer distance: distant method analogy
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)

### 13. [Older MOF prior art exists] Strength of Interlayer Metal–Metal Coupling as Key Active Site Configuration and Atomic Descriptor for Single-Atom Catalysts

- Journal/date: Figshare; `2026-07-09`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://figshare.com/articles/journal_contribution/Strength_of_Interlayer_Metal_Metal_Coupling_as_Key_Active_Site_Configuration_and_Atomic_Descriptor_for_Single-Atom_Catalysts/32948290
- Method tags: catalyst active-site descriptor, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt active-site model-selection and descriptor mining to MOF metal nodes, defects, bimetallic sites, or local-field catalytic motifs.
- MOF transfer note: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.
- Suggested next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - catalyst active-site descriptor: Metal-organic frameworks (MOF)-mediated improvement of cotton germination and early seedling resilience under salinity stress through explainable machine learning and non-destructive terahertz time-domain spectroscopy (THz-TDS) (Industrial Crops and Products, 2026-08-20)
  - catalyst active-site descriptor: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - catalyst active-site descriptor: Smart Catalyst Design: Integrating Structure–Activity Relationships with Computational and Data-Driven Approaches (International Journal of Creative and Open Research in Engineering and Management, 2026-04-22)

### 14. [Older MOF prior art exists] Nanophotonic Semiconductors and Advanced Materials Intelligence for Sustainable Computing and DeepTech Innovation

- Journal/date: unknown; `2026-07-30`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.62311/nesx/rb5jy-978-81-688921-5-6
- Method tags: generative / diffusion / inverse design, multimodal or literature-mining model, physics-informed ML, uncertainty / OOD
- Transfer distance: distant method analogy
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - multimodal or literature-mining model: Data-Driven Design of Metal-Organic Frameworks for Photoelectrochemical Reactions (ACS Energy Letters, 2026-07-16)
  - uncertainty / OOD: Green and sustainable metal–organic framework catalysts for biodiesel production: Progress and energy circularity perspectives (Green Technologies and Sustainability, 2026-08-01)

### 15. [Older MOF prior art exists] MOCLIP: a foundation model for large-scale nanophotonic inverse design

- Journal/date: Nature Communications; `2026-08-19`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41467-026-76714-x
- Method tags: foundation or pretrained model, generative / diffusion / inverse design, self-supervised learning
- Transfer distance: distant method analogy
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Chemically Meaningful Textualization Enables Explainable Validation of Metal-Organic Frameworks by Large Language Models (arXiv (Cornell University), 2026-08-11)
  - foundation or pretrained model: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - foundation or pretrained model: ReadMOF: Structure-Free Semantic Embeddings from Systematic MOF Nomenclature for Machine Learning (ChemRxiv, 2026-04-13)

### 16. [Older MOF prior art exists] Accelerating Catalyst Materials Discovery With Large Artificial Intelligence Models

- Journal/date: Angewandte Chemie International Edition; `2026-02-17`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1002/anie.202526150
- Method tags: active learning / Bayesian optimization, foundation or pretrained model, ML interatomic potential, multimodal or literature-mining model
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - foundation or pretrained model: Chemically Meaningful Textualization Enables Explainable Validation of Metal-Organic Frameworks by Large Language Models (arXiv (Cornell University), 2026-08-11)

### 17. [Older MOF prior art exists] Artificial intelligence and the paradigm shift in nanomechanics

- Journal/date: Results in Engineering; `2026-08-19`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1016/j.rineng.2026.112552
- Method tags: ML interatomic potential, surrogate or multi-fidelity model, uncertainty / OOD
- Transfer distance: distant cross-domain method
- Candidate MOF route: Translate visual-artifact or metadata-consistency logic to MOF structure images/renders, spectra, isotherm curves, generated CIF validation, or multimodal paper-structure consistency checks.
- MOF transfer note: Distant-domain method can be useful if it maps to a concrete MOF object such as structure images, spectra, isotherms, pore maps, or multimodal consistency checks.
- Suggested next step: Map the method onto MOF structure images, spectra, isotherm curves, or generated-structure consistency checks. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - ML interatomic potential: Fast Isotropic Li-Ion Diffusion in Zeolitic Imidazolate Framework Glass Electrolytes for Batteries (arXiv (Cornell University), 2026-08-07)
  - ML interatomic potential: Data-driven Design of Metal-Organic Frameworks with Tunable Negative Thermal Expansion (arXiv (Cornell University), 2026-07-21)
  - ML interatomic potential: The impact of spurious imaginary phonon modes on thermal properties of Metal-organic Frameworks (npj Computational Materials, 2026-07-17)

### 18. [Older MOF prior art exists] Simulating Ionic Liquid Fragmentation in Electrospray Thrusters with Foundation Models

- Journal/date: arXiv (Cornell University); `2026-08-12`
- Candidate source: Cross-material ML transfer
- Link: https://arxiv.org/abs/2608.11558
- Method tags: equivariant ML, foundation or pretrained model, ML interatomic potential, transfer learning / domain adaptation
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - equivariant ML: Data-driven Design of Metal-Organic Frameworks with Tunable Negative Thermal Expansion (arXiv (Cornell University), 2026-07-21)
  - foundation or pretrained model: Chemically Meaningful Textualization Enables Explainable Validation of Metal-Organic Frameworks by Large Language Models (arXiv (Cornell University), 2026-08-11)
  - foundation or pretrained model: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)

### 19. [Older MOF prior art exists] Microstructural insights into fast ion transport in solid electrolytes via multiscale modeling

- Journal/date: Nature Communications; `2026-08-20`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41467-026-76216-w
- Method tags: active learning / Bayesian optimization, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - uncertainty / OOD: Green and sustainable metal–organic framework catalysts for biodiesel production: Progress and energy circularity perspectives (Green Technologies and Sustainability, 2026-08-01)

### 20. [Older MOF prior art exists] MatUQ: a benchmark for uncertainty-aware out-of-distribution materials property prediction with graph neural networks

- Journal/date: npj Computational Materials; `2026-08-15`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41524-026-02272-x
- Method tags: graph neural network, uncertainty / OOD
- Transfer distance: distant method analogy
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - uncertainty / OOD: Green and sustainable metal–organic framework catalysts for biodiesel production: Progress and energy circularity perspectives (Green Technologies and Sustainability, 2026-08-01)
  - uncertainty / OOD: Metal–Organic Frameworks in Food Biotechnology: Opportunities, Challenges, and Future Perspectives for Probiotic Delivery, Precision Fermentation, and Circular Food Systems (Nanomaterials, 2026-07-31)

## Reading Rules

- Fresh means no same method-class tag was found in the recent or long-horizon MOF baselines. It still needs full-paper confirmation.
- Distant cross-domain methods are allowed when the method can be mapped to a concrete MOF object, such as structure images, spectra, isotherms, pore maps, generated CIF checks, or multimodal literature-structure consistency.
- Older prior art means the idea is not new to MOFs, but it may still be worth pursuing if the cross-material paper adds a new representation, label space, uncertainty loop, active-learning strategy, or validation regime.
- Recent MOF activity means lower novelty unless the new method opens a clearly different MOF task or implementation path.
