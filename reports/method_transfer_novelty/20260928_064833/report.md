# Method Transfer Novelty Report

- Generated: `2026-09-28T06:48:33`
- Logic: non-MOF transfer scans provide candidate ideas; recent MOF literature checks current adoption; long-horizon MOF prior art checks older adoption.

## Source Runs

- Recent MOF literature: profile `mof_latest_custom`, since `2025-09-28`, papers `5`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/weekly_mof_latest/20260928_064833/report.md`
- Cross-material ML transfer: profile `materials_ml_transfer`, since `2023-09-29`, papers `30`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/materials_ml_transfer/20260928_064839/report.md`
- Reaction/catalyst ML transfer: profile `reaction_catalyst_ml_transfer`, since `2016-09-30`, papers `27`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/reaction_catalyst_ml_transfer/20260928_064852/report.md`
- Long-horizon MOF method prior art: profile `mof_ml_method_prior_art`, since `2016-09-30`, papers `10`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/mof_ml_method_prior_art/20260928_064904/report.md`

## Triage Summary

- Fresh MOF transfer candidates: `10`
- Older MOF prior art exists: `29`
- Already active in recent MOF literature: `17`

## Method-Class Baseline

| Method class | Candidate transfer scans | Recent MOF | Long-horizon MOF prior art |
|---|---:|---:|---:|
| active learning / Bayesian optimization | 15 | 0 | 3 |
| catalyst active-site descriptor | 2 | 0 | 4 |
| equivariant ML | 9 | 0 | 0 |
| foundation or pretrained model | 12 | 0 | 1 |
| generative / diffusion / inverse design | 12 | 0 | 2 |
| graph neural network | 9 | 0 | 0 |
| ML interatomic potential | 12 | 1 | 1 |
| multimodal or literature-mining model | 5 | 0 | 0 |
| physics-informed ML | 9 | 0 | 0 |
| self-supervised learning | 4 | 0 | 0 |
| surrogate or multi-fidelity model | 10 | 0 | 0 |
| symbolic regression / descriptor discovery | 6 | 0 | 2 |
| transfer learning / domain adaptation | 6 | 1 | 2 |
| uncertainty / OOD | 16 | 0 | 1 |

## Transfer Opportunities

### 1. [Fresh MOF transfer candidate] Topology-aware E(3)-equivariant learning for physically consistent piezoelectric tensor prediction

- Journal/date: npj Computational Materials; `2026-09-25`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41524-026-02331-3
- Method tags: equivariant ML, graph neural network, surrogate or multi-fidelity model
- Transfer distance: adjacent materials
- Candidate MOF route: Benchmark the representation on periodic MOF graphs with explicit node/linker chemistry and pore topology.
- MOF transfer note: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
- Suggested next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 2. [Fresh MOF transfer candidate] Artificial intelligence for predictive mixture toxicology

- Journal/date: Toxicology; `2026-09-19`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1016/j.tox.2026.154589
- Method tags: equivariant ML, graph neural network
- Transfer distance: distant method analogy
- Candidate MOF route: Benchmark the representation on periodic MOF graphs with explicit node/linker chemistry and pore topology.
- MOF transfer note: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
- Suggested next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 3. [Fresh MOF transfer candidate] Transferable Graph Neural Network Surrogates for Molecular Dynamics Across Crystal Symmetries

- Journal/date: ChemRxiv; `2026-09-21`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.26434/chemrxiv.15009166/v1
- Method tags: graph neural network, surrogate or multi-fidelity model
- Transfer distance: adjacent materials
- Candidate MOF route: Benchmark the representation on periodic MOF graphs with explicit node/linker chemistry and pore topology.
- MOF transfer note: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
- Suggested next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 4. [Fresh MOF transfer candidate] ARTIFICIAL INTELLIGENCE IN STEEL STRUCTURES: METHODS, APPLICATIONS AND PERSPECTIVES ON JOINT BEHAVIOUR

- Journal/date: unknown; `2026-09-22`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.67563/asesconf2026057m
- Method tags: physics-informed ML, surrogate or multi-fidelity model
- Transfer distance: distant method analogy
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 5. [Fresh MOF transfer candidate] Machine Learning Applications to Physical Processes

- Journal/date: Open Scholarship Institutional Repository (Washington University in St. Louis); `2026-09-22`
- Candidate source: Cross-material ML transfer
- Link: https://openscholarship.wustl.edu/art_sci_etds/3902
- Method tags: physics-informed ML
- Transfer distance: adjacent materials
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 6. [Fresh MOF transfer candidate] Classical DFT energies and equilibrium configurations obtained by GNN-driven Monte Carlo simulations for solvent-free polymer-grafted nanoparticles

- Journal/date: arXiv (Cornell University); `2026-09-24`
- Candidate source: Cross-material ML transfer
- Link: https://arxiv.org/abs/2605.30822
- Method tags: equivariant ML, graph neural network
- Transfer distance: adjacent materials
- Candidate MOF route: Benchmark the representation on periodic MOF graphs with explicit node/linker chemistry and pore topology.
- MOF transfer note: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
- Suggested next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 7. [Fresh MOF transfer candidate] A multimodal semantic learning framework for data-driven discovery of nitrate-to-ammonia electrocatalysts

- Journal/date: npj Computational Materials; `2026-09-15`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1038/s41524-026-02327-z
- Method tags: multimodal or literature-mining model
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 8. [Fresh MOF transfer candidate] Ioc-Mldroid: a Hybrid Approach for Detection of Android Based Malicious Applications Using Indicators of Compromise (Iocs) and Machine Learning

- Journal/date: i-manager's Journal on Computer Science; `2027-06-15`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.26634/jcom.14.1.1372
- Method tags: surrogate or multi-fidelity model
- Transfer distance: distant method analogy
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 9. [Fresh MOF transfer candidate] AI-assisted multi-objective optimization of Ni anode microstructure for enhanced electrochemical performance and long-term stability of solid oxide fuel cells

- Journal/date: Electrochemistry Communications; `2026-09-20`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1016/j.elecom.2026.108256
- Method tags: surrogate or multi-fidelity model
- Transfer distance: adjacent materials
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 10. [Fresh MOF transfer candidate] Hierarchical Multi-Fidelity Learning for Predicting Three-Dimensional Flame Wrinkling and Turbulent Burning Velocity

- Journal/date: arXiv (Cornell University); `2026-05-06`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://arxiv.org/abs/2605.08232
- Method tags: surrogate or multi-fidelity model
- Transfer distance: distant method analogy
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 11. [Older MOF prior art exists] Machine learning approaches for electrocatalyst design in water splitting: a review for green hydrogen production

- Journal/date: Frontiers in Chemistry; `2026-07-31`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.3389/fchem.2026.1894425
- Method tags: active learning / Bayesian optimization, catalyst active-site descriptor, generative / diffusion / inverse design, graph neural network
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt active-site model-selection and descriptor mining to MOF metal nodes, defects, bimetallic sites, or local-field catalytic motifs.
- MOF transfer note: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.
- Suggested next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion (Materials Today Sustainability, 2026-09-03)
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)

### 12. [Older MOF prior art exists] Review of AI-driven discovery of cathode anode and electrolyte materials for advancing sodium-ion batteries

- Journal/date: Discover Industrial Chemistry and Materials; `2026-09-25`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1007/s44508-026-00022-x
- Method tags: active learning / Bayesian optimization, generative / diffusion / inverse design, graph neural network
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion (Materials Today Sustainability, 2026-09-03)
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)

### 13. [Older MOF prior art exists] Machine learning-accelerated inverse design of energy materials: A critical review of graph neural networks, physics-informed models, and generative AI for batteries, perovskite solar cells, and electrocatalysts

- Journal/date: Next Materials; `2026-07-30`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1016/j.nxmate.2026.102969
- Method tags: active learning / Bayesian optimization, generative / diffusion / inverse design, graph neural network, physics-informed ML, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion (Materials Today Sustainability, 2026-09-03)
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)

### 14. [Older MOF prior art exists] Machine learning kinetics from molecular dynamics data

- Journal/date: arXiv (Cornell University); `2026-09-15`
- Candidate source: Cross-material ML transfer
- Link: https://arxiv.org/abs/2609.17736
- Method tags: generative / diffusion / inverse design, self-supervised learning
- Transfer distance: distant method analogy
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion (Materials Today Sustainability, 2026-09-03)
  - generative / diffusion / inverse design: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)

### 15. [Older MOF prior art exists] Integration of density functional theory and machine learning for materials discovery in energy applications

- Journal/date: Discover Chemistry.; `2026-09-22`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1007/s44371-026-00985-y
- Method tags: active learning / Bayesian optimization, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion (Materials Today Sustainability, 2026-09-03)
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)

### 16. [Older MOF prior art exists] Computational Sustainability for Climate-Resilient Materials: AI-Driven Decarbonization Pathways for Cement and Industrial Systems

- Journal/date: Science Engineering and Technology; `2026-09-21`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.54327/set2026/v6.i2.351
- Method tags: physics-informed ML, uncertainty / OOD
- Transfer distance: distant method analogy
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- Long-horizon MOF prior art:
  - uncertainty / OOD: Machine learning approach for MOF-based photocatalytic CO2 reduction to fuels (Energy Conversion and Management X, 2026-09-01)

### 17. [Older MOF prior art exists] Embedding Physics Priors in Robot Learning: A Survey

- Journal/date: arXiv (Cornell University); `2026-09-15`
- Candidate source: Cross-material ML transfer
- Link: https://arxiv.org/abs/2609.22319
- Method tags: foundation or pretrained model, physics-informed ML
- Transfer distance: distant cross-domain method
- Candidate MOF route: Translate visual-artifact or metadata-consistency logic to MOF structure images/renders, spectra, isotherm curves, generated CIF validation, or multimodal paper-structure consistency checks.
- MOF transfer note: Distant-domain method can be useful if it maps to a concrete MOF object such as structure images, spectra, isotherms, pore maps, or multimodal consistency checks.
- Suggested next step: Map the method onto MOF structure images, spectra, isotherm curves, or generated-structure consistency checks. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)

### 18. [Older MOF prior art exists] Polymer Informatics in the Era of Foundation Models: From Representation to Autonomous Design

- Journal/date: ChemRxiv; `2026-09-23`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.26434/chemrxiv.15009334/v1
- Method tags: foundation or pretrained model, generative / diffusion / inverse design, self-supervised learning
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - generative / diffusion / inverse design: Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion (Materials Today Sustainability, 2026-09-03)

### 19. [Older MOF prior art exists] Bayesian optimization in chemical compound sub-spaces using low-dimensional molecular descriptors

- Journal/date: Machine Learning Science and Technology; `2026-09-17`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1088/2632-2153/aea960
- Method tags: active learning / Bayesian optimization, physics-informed ML, surrogate or multi-fidelity model
- Transfer distance: distant method analogy
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion (Materials Today Sustainability, 2026-09-03)
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)

### 20. [Older MOF prior art exists] UpTCR: a unified progressive knowledge transfer foundation model for robust T-cell receptor-antigen binding recognition

- Journal/date: Nature Communications; `2026-09-24`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41467-026-78075-x
- Method tags: foundation or pretrained model, self-supervised learning
- Transfer distance: distant method analogy
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)

## Reading Rules

- Fresh means no same method-class tag was found in the recent or long-horizon MOF baselines. It still needs full-paper confirmation.
- Distant cross-domain methods are allowed when the method can be mapped to a concrete MOF object, such as structure images, spectra, isotherms, pore maps, generated CIF checks, or multimodal literature-structure consistency.
- Older prior art means the idea is not new to MOFs, but it may still be worth pursuing if the cross-material paper adds a new representation, label space, uncertainty loop, active-learning strategy, or validation regime.
- Recent MOF activity means lower novelty unless the new method opens a clearly different MOF task or implementation path.
