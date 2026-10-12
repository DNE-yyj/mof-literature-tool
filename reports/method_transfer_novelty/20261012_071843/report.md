# Method Transfer Novelty Report

- Generated: `2026-10-12T07:18:43`
- Logic: non-MOF transfer scans provide candidate ideas; recent MOF literature checks current adoption; long-horizon MOF prior art checks older adoption.

## Source Runs

- Recent MOF literature: profile `mof_latest_custom`, since `2025-10-12`, papers `0`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/weekly_mof_latest/20261012_071843/report.md`
- Cross-material ML transfer: profile `materials_ml_transfer`, since `2023-10-13`, papers `30`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/materials_ml_transfer/20261012_071849/report.md`
- Reaction/catalyst ML transfer: profile `reaction_catalyst_ml_transfer`, since `2016-10-14`, papers `30`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/reaction_catalyst_ml_transfer/20261012_071905/report.md`
- Long-horizon MOF method prior art: profile `mof_ml_method_prior_art`, since `2016-10-14`, papers `12`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/mof_ml_method_prior_art/20261012_071920/report.md`

## Triage Summary

- Fresh MOF transfer candidates: `12`
- Older MOF prior art exists: `45`
- Already active in recent MOF literature: `0`

## Method-Class Baseline

| Method class | Candidate transfer scans | Recent MOF | Long-horizon MOF prior art |
|---|---:|---:|---:|
| active learning / Bayesian optimization | 19 | 0 | 2 |
| catalyst active-site descriptor | 4 | 0 | 4 |
| equivariant ML | 5 | 0 | 3 |
| foundation or pretrained model | 18 | 0 | 3 |
| generative / diffusion / inverse design | 13 | 0 | 2 |
| graph neural network | 5 | 0 | 0 |
| ML interatomic potential | 12 | 0 | 1 |
| multimodal or literature-mining model | 9 | 0 | 0 |
| physics-informed ML | 14 | 0 | 0 |
| self-supervised learning | 3 | 0 | 0 |
| surrogate or multi-fidelity model | 5 | 0 | 0 |
| symbolic regression / descriptor discovery | 5 | 0 | 1 |
| transfer learning / domain adaptation | 9 | 0 | 2 |
| uncertainty / OOD | 18 | 0 | 0 |

## Transfer Opportunities

### 1. [Fresh MOF transfer candidate] Digital twins for energy wells through multiscale physics-data fusion: Review, challenges, and a conceptual framework

- Journal/date: Geoenergy Science and Engineering; `2026-10-07`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1016/j.geoen.2026.214860
- Method tags: physics-informed ML, surrogate or multi-fidelity model
- Transfer distance: distant method analogy
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 2. [Fresh MOF transfer candidate] A Comprehensive Review of Battery State of Health Estimation: Methods, Challenges and Future Perspectives

- Journal/date: International Journal of Automotive Science And Technology; `2026-10-03`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.30939/ijastech..1995891
- Method tags: multimodal or literature-mining model, physics-informed ML, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 3. [Fresh MOF transfer candidate] Artificial intelligence in microplastic and nanoplastic research: State-of-Art review from automated detection to environmental fate modeling

- Journal/date: Journal of Hazardous Materials Plastics; `2026-09-24`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1016/j.hazmp.2026.100083
- Method tags: multimodal or literature-mining model, physics-informed ML, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Translate visual-artifact or metadata-consistency logic to MOF structure images/renders, spectra, isotherm curves, generated CIF validation, or multimodal paper-structure consistency checks.
- MOF transfer note: Distant-domain method can be useful if it maps to a concrete MOF object such as structure images, spectra, isotherms, pore maps, or multimodal consistency checks.
- Suggested next step: Map the method onto MOF structure images, spectra, isotherm curves, or generated-structure consistency checks. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 4. [Fresh MOF transfer candidate] Tractable and Thermodynamically Consistent p K a Prediction via First-Dissociation Aggregation

- Journal/date: bioRxiv (Cold Spring Harbor Laboratory); `2026-10-06`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.64898/2026.09.30.755586
- Method tags: graph neural network, physics-informed ML
- Transfer distance: distant method analogy
- Candidate MOF route: Benchmark the representation on periodic MOF graphs with explicit node/linker chemistry and pore topology.
- MOF transfer note: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
- Suggested next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 5. [Fresh MOF transfer candidate] How Far Does an Active Site Reach? Defining Interaction Radii in Covalent Organic Framework Electrocatalysts for Nitrate Reduction

- Journal/date: ACS Catalysis; `2026-10-05`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1021/acscatal.6c05600
- Method tags: uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 6. [Fresh MOF transfer candidate] High-entropy alloy composites: A review of reinforcement architectures, interfacial thermodynamics, processing routes, and performance

- Journal/date: Journal of Alloys and Compounds; `2026-10-01`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1016/j.jallcom.2026.191566
- Method tags: physics-informed ML
- Transfer distance: adjacent materials
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 7. [Fresh MOF transfer candidate] Atoms to Processes: The Role of Artificial Intelligence and Machine Learning in Chemical Engineering

- Journal/date: Industrial & Engineering Chemistry Research; `2026-09-30`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1021/acs.iecr.6c01806
- Method tags: physics-informed ML
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 8. [Fresh MOF transfer candidate] A multimodal semantic learning framework for data-driven discovery of nitrate-to-ammonia electrocatalysts

- Journal/date: npj Computational Materials; `2026-09-15`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1038/s41524-026-02327-z
- Method tags: multimodal or literature-mining model
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 9. [Fresh MOF transfer candidate] Ioc-Mldroid: a Hybrid Approach for Detection of Android Based Malicious Applications Using Indicators of Compromise (Iocs) and Machine Learning

- Journal/date: i-manager's Journal on Computer Science; `2027-06-15`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.26634/jcom.14.1.1372
- Method tags: surrogate or multi-fidelity model
- Transfer distance: distant method analogy
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 10. [Fresh MOF transfer candidate] Tafel curvature analysis in electrocatalysis: theoretical foundations and microkinetic simulations

- Journal/date: ChemRxiv; `2026-09-28`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.26434/chemrxiv.15009586/v1
- Method tags: uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 11. [Fresh MOF transfer candidate] From non-centrosymmetry to surface Janus design: Sparse GW/BSE learning for excitonic two-dimensional photocatalysis candidates

- Journal/date: Chimica Techno Acta; `2026-09-10`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.15826/chimtech.10339
- Method tags: uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 12. [Fresh MOF transfer candidate] Hierarchical Multi-Fidelity Learning for Predicting Three-Dimensional Flame Wrinkling and Turbulent Burning Velocity

- Journal/date: arXiv (Cornell University); `2026-05-06`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://arxiv.org/abs/2605.08232
- Method tags: surrogate or multi-fidelity model
- Transfer distance: distant method analogy
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 13. [Older MOF prior art exists] AI-Driven Electrocatalyst Discovery: Integrating Machine Learning, Density Functional Theory, and High-Throughput Screening for Sustainable Energy Conversion

- Journal/date: International Journal of Soft Computing and Engineering; `2026-09-29`
- Candidate source: Cross-material ML transfer; Reaction/catalyst ML transfer
- Link: https://doi.org/10.35940/ijsce.e3727.16051126
- Method tags: active learning / Bayesian optimization, foundation or pretrained model, graph neural network, ML interatomic potential, multimodal or literature-mining model, surrogate or multi-fidelity model
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - foundation or pretrained model: MOF-VERIFY: A Failure-Aware Agentic Harness for MOF Hypothesis Verification (arXiv (Cornell University), 2026-10-02)

### 14. [Older MOF prior art exists] A Review of Artificial Intelligence Methods for Laser-Based Diagnostics: From Measurement Physics to Autonomous Sensing Systems

- Journal/date: Engineering Technology & Applied Science Research; `2026-10-02`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.48084/etasr.21437
- Method tags: active learning / Bayesian optimization, generative / diffusion / inverse design, physics-informed ML, self-supervised learning, uncertainty / OOD
- Transfer distance: distant method analogy
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - generative / diffusion / inverse design: GLASS: Global Latent Aggregation with Slot-based Set Decoding for Scalable All-Atom Crystal Generation (arXiv (Cornell University), 2026-09-29)

### 15. [Older MOF prior art exists] Toward automated discovery with generative models multimodal learning and closed loop workflows in inverse materials design

- Journal/date: Cell Reports Physical Science; `2026-10-01`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1016/j.xcrp.2026.103561
- Method tags: active learning / Bayesian optimization, generative / diffusion / inverse design, multimodal or literature-mining model, physics-informed ML
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - generative / diffusion / inverse design: GLASS: Global Latent Aggregation with Slot-based Set Decoding for Scalable All-Atom Crystal Generation (arXiv (Cornell University), 2026-09-29)

### 16. [Older MOF prior art exists] Mechanism–AI fusion in refining simulation software: A module-level review

- Journal/date: Results in Engineering; `2026-10-01`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1016/j.rineng.2026.113315
- Method tags: active learning / Bayesian optimization, foundation or pretrained model, physics-informed ML, surrogate or multi-fidelity model, uncertainty / OOD
- Transfer distance: distant method analogy
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - foundation or pretrained model: MOF-VERIFY: A Failure-Aware Agentic Harness for MOF Hypothesis Verification (arXiv (Cornell University), 2026-10-02)

### 17. [Older MOF prior art exists] AIMNet2-rxn: A machine-learned potential for generalized reaction modeling on a millions-of-pathways scale

- Journal/date: Science Advances; `2026-10-07`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1126/sciadv.aea1557
- Method tags: ML interatomic potential, transfer learning / domain adaptation
- Transfer distance: distant method analogy
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- Long-horizon MOF prior art:
  - ML interatomic potential: A Machine-Learned Interatomic Potential Free-Energy Surface for the First Step of MIL-101(Cr) Secondary Building Unit Formation (arXiv (Cornell University), 2026-09-29)
  - transfer learning / domain adaptation: Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks via Machine Learning-Symbolic Regression (arXiv (Cornell University), 2026-08-15)

### 18. [Older MOF prior art exists] Tuning Pore Confinement and Chemistry of Fluorine-Free Membranes

- Journal/date: Journal of the American Chemical Society; `2026-10-09`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1021/jacs.6c15621
- Method tags: ML interatomic potential
- Transfer distance: adjacent materials
- Candidate MOF route: Use the MLIP workflow for flexible, guest-loaded, charged, or diffusion-transition MOF configurations.
- MOF transfer note: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.
- Suggested next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - ML interatomic potential: A Machine-Learned Interatomic Potential Free-Energy Surface for the First Step of MIL-101(Cr) Secondary Building Unit Formation (arXiv (Cornell University), 2026-09-29)

### 19. [Older MOF prior art exists] Machine learning approaches for electrocatalyst design in water splitting: a review for green hydrogen production

- Journal/date: Frontiers in Chemistry; `2026-07-31`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.3389/fchem.2026.1894425
- Method tags: active learning / Bayesian optimization, catalyst active-site descriptor, generative / diffusion / inverse design, graph neural network
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt active-site model-selection and descriptor mining to MOF metal nodes, defects, bimetallic sites, or local-field catalytic motifs.
- MOF transfer note: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.
- Suggested next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - catalyst active-site descriptor: From surface area to smog abatement: A data-mined structure-property framework of adsorbents with pores (Next Chemical Engineering, 2026-10-07)

### 20. [Older MOF prior art exists] Accelerating Catalyst Materials Discovery With Large Artificial Intelligence Models

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
  - foundation or pretrained model: MOF-VERIFY: A Failure-Aware Agentic Harness for MOF Hypothesis Verification (arXiv (Cornell University), 2026-10-02)

## Reading Rules

- Fresh means no same method-class tag was found in the recent or long-horizon MOF baselines. It still needs full-paper confirmation.
- Distant cross-domain methods are allowed when the method can be mapped to a concrete MOF object, such as structure images, spectra, isotherms, pore maps, generated CIF checks, or multimodal literature-structure consistency.
- Older prior art means the idea is not new to MOFs, but it may still be worth pursuing if the cross-material paper adds a new representation, label space, uncertainty loop, active-learning strategy, or validation regime.
- Recent MOF activity means lower novelty unless the new method opens a clearly different MOF task or implementation path.
