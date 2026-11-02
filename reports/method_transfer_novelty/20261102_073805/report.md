# Method Transfer Novelty Report

- Generated: `2026-11-02T07:38:05`
- Logic: non-MOF transfer scans provide candidate ideas; recent MOF literature checks current adoption; long-horizon MOF prior art checks older adoption.

## Source Runs

- Recent MOF literature: profile `mof_latest_custom`, since `2025-11-02`, papers `3`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/weekly_mof_latest/20261102_073805/report.md`
- Cross-material ML transfer: profile `materials_ml_transfer`, since `2023-11-03`, papers `30`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/materials_ml_transfer/20261102_073827/report.md`
- Reaction/catalyst ML transfer: profile `reaction_catalyst_ml_transfer`, since `2016-11-04`, papers `28`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/reaction_catalyst_ml_transfer/20261102_073906/report.md`
- Long-horizon MOF method prior art: profile `mof_ml_method_prior_art`, since `2016-11-04`, papers `11`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/mof_ml_method_prior_art/20261102_073942/report.md`

## Triage Summary

- Fresh MOF transfer candidates: `7`
- Older MOF prior art exists: `24`
- Already active in recent MOF literature: `26`

## Method-Class Baseline

| Method class | Candidate transfer scans | Recent MOF | Long-horizon MOF prior art |
|---|---:|---:|---:|
| active learning / Bayesian optimization | 21 | 0 | 0 |
| catalyst active-site descriptor | 7 | 1 | 3 |
| equivariant ML | 11 | 1 | 0 |
| foundation or pretrained model | 10 | 0 | 0 |
| generative / diffusion / inverse design | 12 | 1 | 1 |
| graph neural network | 5 | 0 | 1 |
| ML interatomic potential | 17 | 0 | 1 |
| multimodal or literature-mining model | 5 | 0 | 0 |
| physics-informed ML | 10 | 0 | 0 |
| self-supervised learning | 2 | 0 | 0 |
| surrogate or multi-fidelity model | 10 | 0 | 0 |
| symbolic regression / descriptor discovery | 5 | 0 | 2 |
| transfer learning / domain adaptation | 8 | 0 | 1 |
| uncertainty / OOD | 23 | 0 | 1 |

## Transfer Opportunities

### 1. [Fresh MOF transfer candidate] From Atoms to Reactors: A Critical Review of a Decade of Machine Learning in Heterogeneous Catalysis (2017–2026)

- Journal/date: Angewandte Chemie International Edition; `2026-10-23`
- Candidate source: Cross-material ML transfer; Reaction/catalyst ML transfer
- Link: https://doi.org/10.1002/anie.4288841
- Method tags: active learning / Bayesian optimization, foundation or pretrained model
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 2. [Fresh MOF transfer candidate] Data-driven discovery of water-splitting electrocatalysts: From predictive machine learning to autonomous optimization

- Journal/date: Artificial Intelligence Chemistry; `2026-10-23`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1016/j.aichem.2026.100136
- Method tags: active learning / Bayesian optimization, physics-informed ML
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 3. [Fresh MOF transfer candidate] Machine learning surrogate modelling for enhanced heat transfer in heat exchangers: A state-of-the-art review

- Journal/date: Energy and AI; `2026-10-15`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1016/j.egyai.2026.100931
- Method tags: physics-informed ML, surrogate or multi-fidelity model
- Transfer distance: distant method analogy
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 4. [Fresh MOF transfer candidate] SIMPLEX: composition-space deep learning for bio-inspired hydrogel adhesion with prospective validation on model-discovered formulations and interpretable composition rules

- Journal/date: Frontiers in Materials; `2026-10-29`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.3389/fmats.2026.1966940
- Method tags: active learning / Bayesian optimization, multimodal or literature-mining model, surrogate or multi-fidelity model
- Transfer distance: distant method analogy
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 5. [Fresh MOF transfer candidate] Artificial intelligence in offshore wind geotechnical engineering: A lifecycle-oriented review

- Journal/date: Ocean; `2026-10-28`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.26599/ocean.2026.9470032
- Method tags: active learning / Bayesian optimization, physics-informed ML, surrogate or multi-fidelity model
- Transfer distance: distant method analogy
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 6. [Fresh MOF transfer candidate] Ioc-Mldroid: a Hybrid Approach for Detection of Android Based Malicious Applications Using Indicators of Compromise (Iocs) and Machine Learning

- Journal/date: i-manager's Journal on Computer Science; `2027-06-15`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.26634/jcom.14.1.1372
- Method tags: surrogate or multi-fidelity model
- Transfer distance: distant method analogy
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 7. [Fresh MOF transfer candidate] Artificial intelligence-driven platform for catalytic reactor discovery and optimization applied to carbon dioxide valorization

- Journal/date: ChemRxiv; `2025-02-20`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.26434/chemrxiv-2025-3gstc
- Method tags: active learning / Bayesian optimization
- Transfer distance: adjacent materials
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 8. [Older MOF prior art exists] Accelerating Catalyst Materials Discovery With Large Artificial Intelligence Models

- Journal/date: Angewandte Chemie International Edition; `2026-02-17`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1002/anie.202526150
- Method tags: active learning / Bayesian optimization, foundation or pretrained model, ML interatomic potential, multimodal or literature-mining model
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - ML interatomic potential: Mechanical versus thermal amorphization of ZIF-4: from local rearrangements to network disorder (ChemRxiv, 2026-10-21)

### 9. [Older MOF prior art exists] Universal machine learning force fields for materials simulation: From model construction to complex-system applications

- Journal/date: Physica Scripta; `2026-10-22`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1088/1402-4896/aeb836
- Method tags: ML interatomic potential, physics-informed ML, self-supervised learning, surrogate or multi-fidelity model, transfer learning / domain adaptation, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - ML interatomic potential: Mechanical versus thermal amorphization of ZIF-4: from local rearrangements to network disorder (ChemRxiv, 2026-10-21)
  - transfer learning / domain adaptation: Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks via Machine Learning-Symbolic Regression (arXiv (Cornell University), 2026-08-15)
  - uncertainty / OOD: Predictive Synthesis of MOFs and COFs (arXiv (Cornell University), 2026-10-08)

### 10. [Older MOF prior art exists] Controlling MXene termination ensembles for stability and performance

- Journal/date: MRS Bulletin; `2026-10-30`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1557/s43577-026-01209-5
- Method tags: ML interatomic potential, surrogate or multi-fidelity model
- Transfer distance: adjacent materials
- Candidate MOF route: Use the MLIP workflow for flexible, guest-loaded, charged, or diffusion-transition MOF configurations.
- MOF transfer note: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.
- Suggested next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - ML interatomic potential: Mechanical versus thermal amorphization of ZIF-4: from local rearrangements to network disorder (ChemRxiv, 2026-10-21)

### 11. [Older MOF prior art exists] A thermodynamic correction layer for machine learning interatomic potentials

- Journal/date: arXiv (Cornell University); `2026-10-25`
- Candidate source: Cross-material ML transfer
- Link: https://arxiv.org/abs/2610.34551
- Method tags: foundation or pretrained model, ML interatomic potential
- Transfer distance: adjacent materials
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- Long-horizon MOF prior art:
  - ML interatomic potential: Mechanical versus thermal amorphization of ZIF-4: from local rearrangements to network disorder (ChemRxiv, 2026-10-21)

### 12. [Older MOF prior art exists] A systematic review of advances in spatiotemporal machine learning for road traffic accident prediction in developing countries

- Journal/date: Discover Artificial Intelligence; `2026-10-31`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1007/s44163-026-02476-6
- Method tags: transfer learning / domain adaptation, uncertainty / OOD
- Transfer distance: distant method analogy
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - transfer learning / domain adaptation: Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks via Machine Learning-Symbolic Regression (arXiv (Cornell University), 2026-08-15)
  - uncertainty / OOD: Predictive Synthesis of MOFs and COFs (arXiv (Cornell University), 2026-10-08)

### 13. [Older MOF prior art exists] Interpretable Hybrid Surrogate Modeling for Diameter Deviation Prediction in Injection Molding Using Symbolic Regression and Gaussian Process Residual Correction

- Journal/date: Research Square; `2026-10-27`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.21203/rs.3.rs-11271710/v1
- Method tags: surrogate or multi-fidelity model, symbolic regression / descriptor discovery, uncertainty / OOD
- Transfer distance: distant method analogy
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - symbolic regression / descriptor discovery: Revisiting Percolation and Molecular Diffusion in Disordered Pore Networks (ChemRxiv, 2026-10-25)
  - symbolic regression / descriptor discovery: Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks via Machine Learning-Symbolic Regression (arXiv (Cornell University), 2026-08-15)
  - uncertainty / OOD: Predictive Synthesis of MOFs and COFs (arXiv (Cornell University), 2026-10-08)

### 14. [Older MOF prior art exists] Tangent-plane evidential uncertainty in active learning for magnetic interatomic potentials

- Journal/date: Physical Review Materials; `2026-10-27`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1103/9hcx-wmmm
- Method tags: active learning / Bayesian optimization, ML interatomic potential, uncertainty / OOD
- Transfer distance: distant method analogy
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- Long-horizon MOF prior art:
  - ML interatomic potential: Mechanical versus thermal amorphization of ZIF-4: from local rearrangements to network disorder (ChemRxiv, 2026-10-21)
  - uncertainty / OOD: Predictive Synthesis of MOFs and COFs (arXiv (Cornell University), 2026-10-08)

### 15. [Older MOF prior art exists] A provenance-aware zirconia conductivity database and Arrhenius-constrained screening of doped electrolyte candidates

- Journal/date: Machine Learning Science and Technology; `2026-10-26`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1088/2632-2153/aeb9a7
- Method tags: foundation or pretrained model, physics-informed ML, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - uncertainty / OOD: Predictive Synthesis of MOFs and COFs (arXiv (Cornell University), 2026-10-08)

### 16. [Older MOF prior art exists] Explicit Spin Regulation as an Emerging Design Paradigm in Heterogeneous Catalysis

- Journal/date: Accounts of Materials Research; `2026-10-12`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1021/accountsmr.6c00167
- Method tags: active learning / Bayesian optimization, ML interatomic potential, multimodal or literature-mining model
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- Long-horizon MOF prior art:
  - ML interatomic potential: Mechanical versus thermal amorphization of ZIF-4: from local rearrangements to network disorder (ChemRxiv, 2026-10-21)

### 17. [Older MOF prior art exists] Synthesis-by-design of ferroelectric Dion–Jacobson two-dimensional hybrid organic–inorganic perovskites

- Journal/date: Nature Communications; `2026-10-27`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41467-026-78928-5
- Method tags: ML interatomic potential, symbolic regression / descriptor discovery
- Transfer distance: adjacent materials
- Candidate MOF route: Use the MLIP workflow for flexible, guest-loaded, charged, or diffusion-transition MOF configurations.
- MOF transfer note: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.
- Suggested next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- Long-horizon MOF prior art:
  - ML interatomic potential: Mechanical versus thermal amorphization of ZIF-4: from local rearrangements to network disorder (ChemRxiv, 2026-10-21)
  - symbolic regression / descriptor discovery: Revisiting Percolation and Molecular Diffusion in Disordered Pore Networks (ChemRxiv, 2026-10-25)
  - symbolic regression / descriptor discovery: Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks via Machine Learning-Symbolic Regression (arXiv (Cornell University), 2026-08-15)

### 18. [Older MOF prior art exists] Closing the learning loop in lithium–sulfur batteries through physics-informed and trustworthy artificial intelligence

- Journal/date: Energy and AI; `2026-10-05`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1016/j.egyai.2026.100934
- Method tags: active learning / Bayesian optimization, multimodal or literature-mining model, physics-informed ML, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- Long-horizon MOF prior art:
  - uncertainty / OOD: Predictive Synthesis of MOFs and COFs (arXiv (Cornell University), 2026-10-08)

### 19. [Older MOF prior art exists] Machine Learning‐Assisted Discovery of Unconventional Molybdenum Nitride Nano‐Facets as Hydrogen Evolution Electrocatalysts

- Journal/date: Small Methods; `2026-10-29`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1002/smtd.71163
- Method tags: uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- Long-horizon MOF prior art:
  - uncertainty / OOD: Predictive Synthesis of MOFs and COFs (arXiv (Cornell University), 2026-10-08)

### 20. [Older MOF prior art exists] Infrastructure-Aware Materials Discovery: Resource Allocation, Cost, and Carbon in AI-Driven Workflows

- Journal/date: Journal of Physics Materials; `2026-10-28`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1088/2515-7639/aebabe
- Method tags: active learning / Bayesian optimization, ML interatomic potential
- Transfer distance: distant method analogy
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- Long-horizon MOF prior art:
  - ML interatomic potential: Mechanical versus thermal amorphization of ZIF-4: from local rearrangements to network disorder (ChemRxiv, 2026-10-21)

## Reading Rules

- Fresh means no same method-class tag was found in the recent or long-horizon MOF baselines. It still needs full-paper confirmation.
- Distant cross-domain methods are allowed when the method can be mapped to a concrete MOF object, such as structure images, spectra, isotherms, pore maps, generated CIF checks, or multimodal literature-structure consistency.
- Older prior art means the idea is not new to MOFs, but it may still be worth pursuing if the cross-material paper adds a new representation, label space, uncertainty loop, active-learning strategy, or validation regime.
- Recent MOF activity means lower novelty unless the new method opens a clearly different MOF task or implementation path.
