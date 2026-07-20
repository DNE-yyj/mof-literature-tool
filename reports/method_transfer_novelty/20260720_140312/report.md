# Method Transfer Novelty Report

- Generated: `2026-07-20T14:03:12`
- Logic: non-MOF transfer scans provide candidate ideas; recent MOF literature checks current adoption; long-horizon MOF prior art checks older adoption.

## Source Runs

- Recent MOF literature: profile `mof_latest_custom`, since `2025-07-20`, papers `3`
  - Report: `D:\rose_data\博士阶段\research_complate\work1\literature_tool\reports\weekly_mof_latest\20260720_140312\report.md`
- Cross-material ML transfer: profile `materials_ml_transfer`, since `2023-07-21`, papers `30`
  - Report: `D:\rose_data\博士阶段\research_complate\work1\literature_tool\reports\materials_ml_transfer\20260720_140326\report.md`
- Reaction/catalyst ML transfer: profile `reaction_catalyst_ml_transfer`, since `2016-07-22`, papers `27`
  - Report: `D:\rose_data\博士阶段\research_complate\work1\literature_tool\reports\reaction_catalyst_ml_transfer\20260720_140357\report.md`
- Long-horizon MOF method prior art: profile `mof_ml_method_prior_art`, since `2016-07-22`, papers `15`
  - Report: `D:\rose_data\博士阶段\research_complate\work1\literature_tool\reports\mof_ml_method_prior_art\20260720_140426\report.md`

## Triage Summary

- Fresh MOF transfer candidates: `9`
- Older MOF prior art exists: `27`
- Already active in recent MOF literature: `20`

## Method-Class Baseline

| Method class | Candidate transfer scans | Recent MOF | Long-horizon MOF prior art |
|---|---:|---:|---:|
| active learning / Bayesian optimization | 16 | 0 | 3 |
| catalyst active-site descriptor | 4 | 0 | 2 |
| equivariant ML | 9 | 0 | 1 |
| foundation or pretrained model | 11 | 0 | 4 |
| generative / diffusion / inverse design | 7 | 0 | 2 |
| graph neural network | 6 | 0 | 0 |
| ML interatomic potential | 18 | 1 | 2 |
| multimodal or literature-mining model | 3 | 1 | 1 |
| physics-informed ML | 8 | 0 | 0 |
| reaction-specific dataset learning | 4 | 0 | 0 |
| self-supervised learning | 6 | 0 | 0 |
| surrogate or multi-fidelity model | 8 | 0 | 0 |
| symbolic regression / descriptor discovery | 1 | 0 | 0 |
| transfer learning / domain adaptation | 12 | 0 | 0 |
| uncertainty / OOD | 25 | 0 | 1 |

## Transfer Opportunities

### 1. [Fresh MOF transfer candidate] Unlocking the Chemical Space for Rechargeable Batteries with a Generative Solvent Design System

- Journal/date: ACS Nano; `2026-07-16`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1021/acsnano.6c06255
- Method tags: physics-informed ML, transfer learning / domain adaptation
- Transfer distance: adjacent materials
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 2. [Fresh MOF transfer candidate] Underexplored Catalysts as General Structures: Application of Machine Learning Techniques for Reaction‐Specific Datasets

- Journal/date: Angewandte Chemie; `2026-07-10`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1002/ange.8169897
- Method tags: reaction-specific dataset learning
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt catalyst-generality scoring to MOF catalytic reaction families, biased literature data, and targeted experimental or DFT validation.
- MOF transfer note: Reaction-specific small-data workflow is useful for MOF catalysis if catalyst generality, literature bias, and scaffold validation are made explicit.
- Suggested next step: Rebuild the workflow on MOF catalytic reaction families with explicit scaffold generality, reporting-bias, and validation splits. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 3. [Fresh MOF transfer candidate] Harnessing machine learning for electrochemical CO 2 reduction: current progress and future perspectives

- Journal/date: Micro Nano Science; `2026-06-23`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.20517/mns.2025.06
- Method tags: physics-informed ML
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 4. [Fresh MOF transfer candidate] Interpretable Machine Learning of Nanoparticle Stability through Topological Layer Embeddings

- Journal/date: The Journal of Physical Chemistry A; `2026-06-27`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1021/acs.jpca.6c01508
- Method tags: symbolic regression / descriptor discovery
- Transfer distance: distant method analogy
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 5. [Fresh MOF transfer candidate] Machine Learning Prediction of Thermal Properties of PHB/PHBV-Based Materials: A Quantitative Structure–Property Relationship Approach Using an Integrated Polymer Database

- Journal/date: Polymers; `2026-06-23`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.3390/polym18131559
- Method tags: transfer learning / domain adaptation
- Transfer distance: adjacent materials
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 6. [Fresh MOF transfer candidate] Hierarchical Multi-Fidelity Learning for Predicting Three-Dimensional Flame Wrinkling and Turbulent Burning Velocity

- Journal/date: arXiv (Cornell University); `2026-05-06`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://arxiv.org/abs/2605.08232
- Method tags: surrogate or multi-fidelity model
- Transfer distance: distant method analogy
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 7. [Fresh MOF transfer candidate] A GAN-Augmented Machine Learning Framework for Predicting Raman Characteristics in Carbon Nanofiber Synthesis

- Journal/date: Open MIND; `2026-01-14`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://hdl.handle.net/1880/123989
- Method tags: physics-informed ML, transfer learning / domain adaptation
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 8. [Fresh MOF transfer candidate] Expert-Informed Contrastive Learning of Condition Space for Amide Coupling Reactions

- Journal/date: ChemRxiv; `2026-03-18`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.26434/chemrxiv.15001054/v1
- Method tags: self-supervised learning
- Transfer distance: distant method analogy
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 9. [Fresh MOF transfer candidate] ScopeMap: An AI-Assisted, Human-in-the-Loop Workflow for Mapping Reaction Scope and Boundaries

- Journal/date: ChemRxiv; `2026-01-16`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.26434/chemrxiv-2026-kqz7d
- Method tags: reaction-specific dataset learning
- Transfer distance: distant method analogy
- Candidate MOF route: Adapt catalyst-generality scoring to MOF catalytic reaction families, biased literature data, and targeted experimental or DFT validation.
- MOF transfer note: Reaction-specific small-data workflow is useful for MOF catalysis if catalyst generality, literature bias, and scaffold validation are made explicit.
- Suggested next step: Rebuild the workflow on MOF catalytic reaction families with explicit scaffold generality, reporting-bias, and validation splits.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 10. [Older MOF prior art exists] Strength of Interlayer Metal–Metal Coupling as Key Active Site Configuration and Atomic Descriptor for Single-Atom Catalysts

- Journal/date: Journal of the American Chemical Society; `2026-07-09`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1021/jacs.6c04989
- Method tags: catalyst active-site descriptor, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt active-site model-selection and descriptor mining to MOF metal nodes, defects, bimetallic sites, or local-field catalytic motifs.
- MOF transfer note: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.
- Suggested next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - catalyst active-site descriptor: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - catalyst active-site descriptor: Smart Catalyst Design: Integrating Structure–Activity Relationships with Computational and Data-Driven Approaches (International Journal of Creative and Open Research in Engineering and Management, 2026-04-22)
  - uncertainty / OOD: Descriptor Adequacy as a Materials-Regime Principle in MOF Adsorption Machine Learning (ChemRxiv, 2026-07-03)

### 11. [Older MOF prior art exists] From Newton to Neural Networks: A Review of Data-Driven Physical Modelling and the Rise of Physics-Informed AI

- Journal/date: INTERNATIONAL JOURNAL OF MULTIDISCIPLINARY RESEARCH AND ANALYSIS; `2026-07-17`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.47191/ijmra/v9-i7-28
- Method tags: active learning / Bayesian optimization, foundation or pretrained model, physics-informed ML, uncertainty / OOD
- Transfer distance: distant method analogy
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - active learning / Bayesian optimization: Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents (arXiv (Cornell University), 2026-06-28)

### 12. [Older MOF prior art exists] Artificial Intelligence and Machine Learning in the Design of Nanomaterials for Next-Generation Solar Cells

- Journal/date: Scholars Journal of Engineering and Technology; `2026-07-09`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.36347/sjet.2026.v14i07.002
- Method tags: active learning / Bayesian optimization, generative / diffusion / inverse design, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - active learning / Bayesian optimization: Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents (arXiv (Cornell University), 2026-06-28)

### 13. [Older MOF prior art exists] Machine Learning in Materials Science: Data-Driven Discovery and Functional Applications

- Journal/date: Encyclopedia; `2026-07-06`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.3390/encyclopedia6070150
- Method tags: physics-informed ML, surrogate or multi-fidelity model, uncertainty / OOD
- Transfer distance: distant method analogy
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - uncertainty / OOD: Descriptor Adequacy as a Materials-Regime Principle in MOF Adsorption Machine Learning (ChemRxiv, 2026-07-03)

### 14. [Older MOF prior art exists] FLOWR.ROOT – A flow matching-based foundation model for joint multi-purpose structure-aware 3D ligand generation and affinity prediction

- Journal/date: Nature Communications; `2026-07-06`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41467-026-74130-9
- Method tags: equivariant ML, foundation or pretrained model, self-supervised learning, transfer learning / domain adaptation
- Transfer distance: adjacent materials
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - equivariant ML: Metal-organic frameworks (MOFs) based adsorbents for efficient removal of antibiotic pollutants from water (Frontiers in Materials, 2026-07-08)
  - foundation or pretrained model: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - foundation or pretrained model: Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents (arXiv (Cornell University), 2026-06-28)

### 15. [Older MOF prior art exists] Artificial intelligence and automation in enzyme engineering: evolution, advances, and future perspectives

- Journal/date: Bioresources and Bioprocessing; `2026-07-10`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1186/s40643-026-01096-3
- Method tags: active learning / Bayesian optimization, reaction-specific dataset learning, self-supervised learning, uncertainty / OOD
- Transfer distance: distant method analogy
- Candidate MOF route: Adapt catalyst-generality scoring to MOF catalytic reaction families, biased literature data, and targeted experimental or DFT validation.
- MOF transfer note: Reaction-specific small-data workflow is useful for MOF catalysis if catalyst generality, literature bias, and scaffold validation are made explicit.
- Suggested next step: Rebuild the workflow on MOF catalytic reaction families with explicit scaffold generality, reporting-bias, and validation splits. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - active learning / Bayesian optimization: Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents (arXiv (Cornell University), 2026-06-28)

### 16. [Older MOF prior art exists] Strength of InterlayerMetal–Metal Couplingas Key Active Site Configuration and Atomic Descriptor for Single-AtomCatalysts

- Journal/date: Figshare; `2026-07-09`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://figshare.com/articles/journal_contribution/Strength_of_Interlayer_Metal_Metal_Coupling_as_Key_Active_Site_Configuration_and_Atomic_Descriptor_for_Single-Atom_Catalysts/32948290
- Method tags: catalyst active-site descriptor, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt active-site model-selection and descriptor mining to MOF metal nodes, defects, bimetallic sites, or local-field catalytic motifs.
- MOF transfer note: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.
- Suggested next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - catalyst active-site descriptor: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - catalyst active-site descriptor: Smart Catalyst Design: Integrating Structure–Activity Relationships with Computational and Data-Driven Approaches (International Journal of Creative and Open Research in Engineering and Management, 2026-04-22)
  - uncertainty / OOD: Descriptor Adequacy as a Materials-Regime Principle in MOF Adsorption Machine Learning (ChemRxiv, 2026-07-03)

### 17. [Older MOF prior art exists] Guiding generative models to uncover diverse and novel crystals via reinforcement learning

- Journal/date: Nature Machine Intelligence; `2026-07-06`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s42256-026-01262-4
- Method tags: generative / diffusion / inverse design, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - generative / diffusion / inverse design: Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents (arXiv (Cornell University), 2026-06-28)
  - uncertainty / OOD: Descriptor Adequacy as a Materials-Regime Principle in MOF Adsorption Machine Learning (ChemRxiv, 2026-07-03)

### 18. [Older MOF prior art exists] Bgolearn: a unified Bayesian optimization framework for accelerating materials discovery

- Journal/date: npj Computational Materials; `2026-07-14`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41524-026-02226-3
- Method tags: active learning / Bayesian optimization, surrogate or multi-fidelity model, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - active learning / Bayesian optimization: Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents (arXiv (Cornell University), 2026-06-28)

### 19. [Older MOF prior art exists] Symmetry-Informed Deep Learning for Electromagnetic Scattering

- Journal/date: arXiv (Cornell University); `2026-07-14`
- Candidate source: Cross-material ML transfer
- Link: https://arxiv.org/abs/2607.12810
- Method tags: equivariant ML, physics-informed ML, surrogate or multi-fidelity model
- Transfer distance: adjacent materials
- Candidate MOF route: Benchmark the representation on periodic MOF graphs with explicit node/linker chemistry and pore topology.
- MOF transfer note: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
- Suggested next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - equivariant ML: Metal-organic frameworks (MOFs) based adsorbents for efficient removal of antibiotic pollutants from water (Frontiers in Materials, 2026-07-08)

### 20. [Older MOF prior art exists] Machine learning for frontier orbital energetics: A review of HOMO–LUMO prediction methods

- Journal/date: Carbon Trends; `2026-07-15`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1016/j.cartre.2026.100674
- Method tags: equivariant ML, self-supervised learning, uncertainty / OOD
- Transfer distance: distant method analogy
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - equivariant ML: Metal-organic frameworks (MOFs) based adsorbents for efficient removal of antibiotic pollutants from water (Frontiers in Materials, 2026-07-08)
  - uncertainty / OOD: Descriptor Adequacy as a Materials-Regime Principle in MOF Adsorption Machine Learning (ChemRxiv, 2026-07-03)

## Reading Rules

- Fresh means no same method-class tag was found in the recent or long-horizon MOF baselines. It still needs full-paper confirmation.
- Distant cross-domain methods are allowed when the method can be mapped to a concrete MOF object, such as structure images, spectra, isotherms, pore maps, generated CIF checks, or multimodal literature-structure consistency.
- Older prior art means the idea is not new to MOFs, but it may still be worth pursuing if the cross-material paper adds a new representation, label space, uncertainty loop, active-learning strategy, or validation regime.
- Recent MOF activity means lower novelty unless the new method opens a clearly different MOF task or implementation path.
