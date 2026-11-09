# Method Transfer Novelty Report

- Generated: `2026-11-09T07:54:23`
- Logic: non-MOF transfer scans provide candidate ideas; recent MOF literature checks current adoption; long-horizon MOF prior art checks older adoption.

## Source Runs

- Recent MOF literature: profile `mof_latest_custom`, since `2025-11-09`, papers `1`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/weekly_mof_latest/20261109_075423/report.md`
- Cross-material ML transfer: profile `materials_ml_transfer`, since `2023-11-10`, papers `30`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/materials_ml_transfer/20261109_075434/report.md`
- Reaction/catalyst ML transfer: profile `reaction_catalyst_ml_transfer`, since `2016-11-11`, papers `28`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/reaction_catalyst_ml_transfer/20261109_075457/report.md`
- Long-horizon MOF method prior art: profile `mof_ml_method_prior_art`, since `2016-11-11`, papers `12`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/mof_ml_method_prior_art/20261109_075518/report.md`

## Triage Summary

- Fresh MOF transfer candidates: `5`
- Older MOF prior art exists: `36`
- Already active in recent MOF literature: `15`

## Method-Class Baseline

| Method class | Candidate transfer scans | Recent MOF | Long-horizon MOF prior art |
|---|---:|---:|---:|
| active learning / Bayesian optimization | 18 | 0 | 2 |
| catalyst active-site descriptor | 3 | 0 | 2 |
| equivariant ML | 7 | 0 | 0 |
| foundation or pretrained model | 15 | 0 | 1 |
| generative / diffusion / inverse design | 8 | 0 | 1 |
| graph neural network | 5 | 0 | 0 |
| ML interatomic potential | 15 | 1 | 3 |
| multimodal or literature-mining model | 4 | 0 | 0 |
| physics-informed ML | 13 | 0 | 0 |
| self-supervised learning | 3 | 0 | 0 |
| surrogate or multi-fidelity model | 7 | 0 | 0 |
| symbolic regression / descriptor discovery | 8 | 0 | 1 |
| transfer learning / domain adaptation | 7 | 0 | 1 |
| uncertainty / OOD | 17 | 0 | 1 |

## Transfer Opportunities

### 1. [Fresh MOF transfer candidate] AnyNav: Visual neuro-symbolic friction learning for off-road navigation

- Journal/date: The International Journal of Robotics Research; `2026-11-07`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1177/02783649261496456
- Method tags: physics-informed ML, self-supervised learning
- Transfer distance: distant method analogy
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 2. [Fresh MOF transfer candidate] Explainable artificial intelligence for laser powder bed fusion alloys: breaking the formability–performance trade-off via collaborative control

- Journal/date: Advanced Materials Joining; `2026-11-06`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1007/s44500-026-00023-y
- Method tags: multimodal or literature-mining model, physics-informed ML
- Transfer distance: adjacent materials
- Candidate MOF route: Translate visual-artifact or metadata-consistency logic to MOF structure images/renders, spectra, isotherm curves, generated CIF validation, or multimodal paper-structure consistency checks.
- MOF transfer note: Distant-domain method can be useful if it maps to a concrete MOF object such as structure images, spectra, isotherms, pore maps, or multimodal consistency checks.
- Suggested next step: Map the method onto MOF structure images, spectra, isotherm curves, or generated-structure consistency checks.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 3. [Fresh MOF transfer candidate] SlideGen: Collaborative Multimodal Agents for Scientific Slide Generation

- Journal/date: ACM International Conference on Multimedia (ACM MM); `2026-11-06`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1145/3767308.3835435
- Method tags: multimodal or literature-mining model
- Transfer distance: distant method analogy
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 4. [Fresh MOF transfer candidate] Ioc-Mldroid: a Hybrid Approach for Detection of Android Based Malicious Applications Using Indicators of Compromise (Iocs) and Machine Learning

- Journal/date: i-manager's Journal on Computer Science; `2027-06-15`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.26634/jcom.14.1.1372
- Method tags: surrogate or multi-fidelity model
- Transfer distance: distant method analogy
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 5. [Fresh MOF transfer candidate] Chemical short-range order as a conditional modifier of deformation and damage in void-containing high-entropy alloys under high-strain-rate loading

- Journal/date: Materials & Design; `2026-11-02`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1016/j.matdes.2026.117418
- Method tags: surrogate or multi-fidelity model
- Transfer distance: adjacent materials
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 6. [Older MOF prior art exists] Computational Modeling of Electrolytes and the Solid–Electrolyte Interphase (SEI) in Li-Ion Batteries: A 30-Year Odyssey from DFT/MD/MC to AI–A Comprehensive Review

- Journal/date: ChemRxiv; `2026-11-04`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.26434/chemrxiv.15011695/v1
- Method tags: active learning / Bayesian optimization, foundation or pretrained model, generative / diffusion / inverse design, physics-informed ML, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: RepMOBO: Representation-Guided Multi-Objective Bayesian Optimization for Pareto-Optimal MOF Discovery (Research Square, 2026-11-03)
  - active learning / Bayesian optimization: An auditable multi-agent forum for scientific workflows with a computational MOF case study (Materials Today Communications, 2026-11-03)
  - generative / diffusion / inverse design: Reliable methane storage screening and inverse design of metal organic frameworks under distribution shift (Discover Artificial Intelligence, 2026-10-31)

### 7. [Older MOF prior art exists] Machine learning-driven inverse design of high-hardness multi-principal element alloys through symbolic regression

- Journal/date: Scientific Reports; `2026-10-23`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41598-026-74491-7
- Method tags: active learning / Bayesian optimization, generative / diffusion / inverse design, physics-informed ML, surrogate or multi-fidelity model, symbolic regression / descriptor discovery
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: RepMOBO: Representation-Guided Multi-Objective Bayesian Optimization for Pareto-Optimal MOF Discovery (Research Square, 2026-11-03)
  - active learning / Bayesian optimization: An auditable multi-agent forum for scientific workflows with a computational MOF case study (Materials Today Communications, 2026-11-03)
  - generative / diffusion / inverse design: Reliable methane storage screening and inverse design of metal organic frameworks under distribution shift (Discover Artificial Intelligence, 2026-10-31)

### 8. [Older MOF prior art exists] Machine Learning for Predicting Dielectric Energy-Storage Properties of Perovskite Oxides

- Journal/date: Applied and Computational Engineering; `2026-11-03`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.54254/2755-2721/2027.md38630
- Method tags: equivariant ML, generative / diffusion / inverse design, graph neural network, multimodal or literature-mining model
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Reliable methane storage screening and inverse design of metal organic frameworks under distribution shift (Discover Artificial Intelligence, 2026-10-31)

### 9. [Older MOF prior art exists] Empirical and physics-based computational approaches to explosive power, brisance, and underwater detonation response: A critical review with selected machine-learning applications

- Journal/date: Next Materials; `2026-11-02`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1016/j.nxmate.2026.103938
- Method tags: active learning / Bayesian optimization, physics-informed ML, surrogate or multi-fidelity model, uncertainty / OOD
- Transfer distance: distant method analogy
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: RepMOBO: Representation-Guided Multi-Objective Bayesian Optimization for Pareto-Optimal MOF Discovery (Research Square, 2026-11-03)
  - active learning / Bayesian optimization: An auditable multi-agent forum for scientific workflows with a computational MOF case study (Materials Today Communications, 2026-11-03)
  - uncertainty / OOD: Predictive Synthesis of MOFs and COFs (arXiv (Cornell University), 2026-10-08)

### 10. [Older MOF prior art exists] Scope, Challenges, and Future of Agentic AI in Geotechnical and Earthquake Engineering: A Critical Review

- Journal/date: Bulletin of Computational Intelligence; `2026-11-04`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.53941/bci.2026.100016
- Method tags: active learning / Bayesian optimization, foundation or pretrained model, generative / diffusion / inverse design, physics-informed ML, uncertainty / OOD
- Transfer distance: distant method analogy
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: RepMOBO: Representation-Guided Multi-Objective Bayesian Optimization for Pareto-Optimal MOF Discovery (Research Square, 2026-11-03)
  - active learning / Bayesian optimization: An auditable multi-agent forum for scientific workflows with a computational MOF case study (Materials Today Communications, 2026-11-03)
  - generative / diffusion / inverse design: Reliable methane storage screening and inverse design of metal organic frameworks under distribution shift (Discover Artificial Intelligence, 2026-10-31)

### 11. [Older MOF prior art exists] From Atoms to Reactors: A Critical Review of a Decade of Machine Learning in Heterogeneous Catalysis (2017–2026)

- Journal/date: Angewandte Chemie International Edition; `2026-10-23`
- Candidate source: Cross-material ML transfer; Reaction/catalyst ML transfer
- Link: https://doi.org/10.1002/anie.4288841
- Method tags: active learning / Bayesian optimization, foundation or pretrained model
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: RepMOBO: Representation-Guided Multi-Objective Bayesian Optimization for Pareto-Optimal MOF Discovery (Research Square, 2026-11-03)
  - active learning / Bayesian optimization: An auditable multi-agent forum for scientific workflows with a computational MOF case study (Materials Today Communications, 2026-11-03)

### 12. [Older MOF prior art exists] Machine learning-accelerated inverse design of energy materials: A critical review of graph neural networks, physics-informed models, and generative AI for batteries, perovskite solar cells, and electrocatalysts

- Journal/date: Next Materials; `2026-07-30`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1016/j.nxmate.2026.102969
- Method tags: active learning / Bayesian optimization, generative / diffusion / inverse design, graph neural network, physics-informed ML, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: RepMOBO: Representation-Guided Multi-Objective Bayesian Optimization for Pareto-Optimal MOF Discovery (Research Square, 2026-11-03)
  - active learning / Bayesian optimization: An auditable multi-agent forum for scientific workflows with a computational MOF case study (Materials Today Communications, 2026-11-03)
  - generative / diffusion / inverse design: Reliable methane storage screening and inverse design of metal organic frameworks under distribution shift (Discover Artificial Intelligence, 2026-10-31)

### 13. [Older MOF prior art exists] Physics-informed Bayesian optimization for quantitative high-resolution transmission electron microscopy

- Journal/date: npj Computational Materials; `2026-11-04`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41524-026-02364-8
- Method tags: active learning / Bayesian optimization, physics-informed ML
- Transfer distance: adjacent materials
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: RepMOBO: Representation-Guided Multi-Objective Bayesian Optimization for Pareto-Optimal MOF Discovery (Research Square, 2026-11-03)
  - active learning / Bayesian optimization: An auditable multi-agent forum for scientific workflows with a computational MOF case study (Materials Today Communications, 2026-11-03)

### 14. [Older MOF prior art exists] Data-driven discovery of water-splitting electrocatalysts: From predictive machine learning to autonomous optimization

- Journal/date: Artificial Intelligence Chemistry; `2026-10-23`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1016/j.aichem.2026.100136
- Method tags: active learning / Bayesian optimization, physics-informed ML
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: RepMOBO: Representation-Guided Multi-Objective Bayesian Optimization for Pareto-Optimal MOF Discovery (Research Square, 2026-11-03)
  - active learning / Bayesian optimization: An auditable multi-agent forum for scientific workflows with a computational MOF case study (Materials Today Communications, 2026-11-03)

### 15. [Older MOF prior art exists] Next-generation process monitoring and control for metal additive manufacturing: toward a physics-informed digital twin framework

- Journal/date: Virtual and Physical Prototyping; `2026-11-06`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1080/17452759.2026.2751873
- Method tags: active learning / Bayesian optimization, physics-informed ML, surrogate or multi-fidelity model
- Transfer distance: distant method analogy
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: RepMOBO: Representation-Guided Multi-Objective Bayesian Optimization for Pareto-Optimal MOF Discovery (Research Square, 2026-11-03)
  - active learning / Bayesian optimization: An auditable multi-agent forum for scientific workflows with a computational MOF case study (Materials Today Communications, 2026-11-03)

### 16. [Older MOF prior art exists] A closed-loop framework for perovskite precursor additive discovery

- Journal/date: Communications Materials; `2026-11-04`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s43246-026-01407-3
- Method tags: active learning / Bayesian optimization, foundation or pretrained model, transfer learning / domain adaptation, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: RepMOBO: Representation-Guided Multi-Objective Bayesian Optimization for Pareto-Optimal MOF Discovery (Research Square, 2026-11-03)
  - active learning / Bayesian optimization: An auditable multi-agent forum for scientific workflows with a computational MOF case study (Materials Today Communications, 2026-11-03)
  - transfer learning / domain adaptation: Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks via Machine Learning-Symbolic Regression (arXiv (Cornell University), 2026-08-15)

### 17. [Older MOF prior art exists] Machine Learning for Synthetic Organic Chemistry: Methods, Applications, and Best Practices

- Journal/date: Angewandte Chemie Novit; `2026-08-28`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1002/anov.70032
- Method tags: foundation or pretrained model
- Transfer distance: distant method analogy
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - foundation or pretrained model: An auditable multi-agent forum for scientific workflows with a computational MOF case study (Materials Today Communications, 2026-11-03)

### 18. [Older MOF prior art exists] Predictive Modelling of Electronic Materials: A Review of Deep Learning Techniques in Computer Engineering

- Journal/date: ASEAN Journal for Science and Engineering in Materials; `2026-12-01`
- Candidate source: Cross-material ML transfer
- Link: https://ejournal.bumipublikasinusantara.id/index.php/ajsem/article/view/938
- Method tags: generative / diffusion / inverse design, graph neural network
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Reliable methane storage screening and inverse design of metal organic frameworks under distribution shift (Discover Artificial Intelligence, 2026-10-31)

### 19. [Older MOF prior art exists] Toward Intelligent Thermal Fluids: AI-Driven Design of Zeta-Engineered Nanofluids and Self-Organized Thermal Transport Networks

- Journal/date: Research Square; `2026-11-04`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.21203/rs.3.rs-11352574/v1
- Method tags: active learning / Bayesian optimization, physics-informed ML
- Transfer distance: adjacent materials
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: RepMOBO: Representation-Guided Multi-Objective Bayesian Optimization for Pareto-Optimal MOF Discovery (Research Square, 2026-11-03)
  - active learning / Bayesian optimization: An auditable multi-agent forum for scientific workflows with a computational MOF case study (Materials Today Communications, 2026-11-03)

### 20. [Older MOF prior art exists] Interpretable Hybrid Surrogate Modeling for Diameter Deviation Prediction in Injection Molding Using Symbolic Regression and Gaussian Process Residual Correction

- Journal/date: Research Square; `2026-10-27`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.21203/rs.3.rs-11271710/v1
- Method tags: surrogate or multi-fidelity model, symbolic regression / descriptor discovery, uncertainty / OOD
- Transfer distance: distant method analogy
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - symbolic regression / descriptor discovery: Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks via Machine Learning-Symbolic Regression (arXiv (Cornell University), 2026-08-15)
  - uncertainty / OOD: Predictive Synthesis of MOFs and COFs (arXiv (Cornell University), 2026-10-08)

## Reading Rules

- Fresh means no same method-class tag was found in the recent or long-horizon MOF baselines. It still needs full-paper confirmation.
- Distant cross-domain methods are allowed when the method can be mapped to a concrete MOF object, such as structure images, spectra, isotherms, pore maps, generated CIF checks, or multimodal literature-structure consistency.
- Older prior art means the idea is not new to MOFs, but it may still be worth pursuing if the cross-material paper adds a new representation, label space, uncertainty loop, active-learning strategy, or validation regime.
- Recent MOF activity means lower novelty unless the new method opens a clearly different MOF task or implementation path.
