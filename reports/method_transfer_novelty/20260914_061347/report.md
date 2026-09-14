# Method Transfer Novelty Report

- Generated: `2026-09-14T06:13:47`
- Logic: non-MOF transfer scans provide candidate ideas; recent MOF literature checks current adoption; long-horizon MOF prior art checks older adoption.

## Source Runs

- Recent MOF literature: profile `mof_latest_custom`, since `2025-09-14`, papers `3`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/weekly_mof_latest/20260914_061347/report.md`
- Cross-material ML transfer: profile `materials_ml_transfer`, since `2023-09-15`, papers `30`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/materials_ml_transfer/20260914_061400/report.md`
- Reaction/catalyst ML transfer: profile `reaction_catalyst_ml_transfer`, since `2016-09-16`, papers `24`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/reaction_catalyst_ml_transfer/20260914_061429/report.md`
- Long-horizon MOF method prior art: profile `mof_ml_method_prior_art`, since `2016-09-16`, papers `16`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/mof_ml_method_prior_art/20260914_061452/report.md`

## Triage Summary

- Fresh MOF transfer candidates: `3`
- Older MOF prior art exists: `36`
- Already active in recent MOF literature: `14`

## Method-Class Baseline

| Method class | Candidate transfer scans | Recent MOF | Long-horizon MOF prior art |
|---|---:|---:|---:|
| active learning / Bayesian optimization | 13 | 0 | 4 |
| catalyst active-site descriptor | 5 | 1 | 5 |
| equivariant ML | 7 | 0 | 2 |
| foundation or pretrained model | 12 | 0 | 6 |
| generative / diffusion / inverse design | 13 | 0 | 2 |
| graph neural network | 6 | 0 | 0 |
| ML interatomic potential | 11 | 0 | 2 |
| multimodal or literature-mining model | 7 | 0 | 0 |
| physics-informed ML | 10 | 1 | 2 |
| self-supervised learning | 5 | 0 | 0 |
| surrogate or multi-fidelity model | 3 | 0 | 1 |
| symbolic regression / descriptor discovery | 2 | 0 | 1 |
| transfer learning / domain adaptation | 8 | 0 | 2 |
| uncertainty / OOD | 13 | 0 | 2 |

## Transfer Opportunities

### 1. [Fresh MOF transfer candidate] TAME: Element-wise Mixture-of-Experts Fusion for Data-Efficient and Interpretable Molecular Property Prediction

- Journal/date: ChemRxiv; `2026-09-03`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.26434/chemrxiv.15008270/v1
- Method tags: graph neural network, multimodal or literature-mining model, self-supervised learning
- Transfer distance: adjacent materials
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 2. [Fresh MOF transfer candidate] Decoding Multiscale Degradation of Layered Cathodes in All‐Solid‐State Lithium Batteries: An Advanced Diagnostics‐Driven Framework

- Journal/date: Advanced Energy Materials; `2026-09-02`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1002/aenm.71528
- Method tags: multimodal or literature-mining model
- Transfer distance: adjacent materials
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 3. [Fresh MOF transfer candidate] Expert-Informed Contrastive Learning of Condition Space for Amide Coupling Reactions

- Journal/date: ChemRxiv; `2026-03-18`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.26434/chemrxiv.15001054/v1
- Method tags: self-supervised learning
- Transfer distance: distant method analogy
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 4. [Older MOF prior art exists] SHAP-guided Machine Learning for Interpretable Band Gap Prediction and Inverse Design in ABX₃ Perovskites

- Journal/date: International Journal of Computational Intelligence Systems; `2026-08-24`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1007/s44196-026-01454-1
- Method tags: generative / diffusion / inverse design, symbolic regression / descriptor discovery, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion (Materials Today Sustainability, 2026-09-03)
  - generative / diffusion / inverse design: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - symbolic regression / descriptor discovery: Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks via Machine Learning-Symbolic Regression (arXiv (Cornell University), 2026-08-15)

### 5. [Older MOF prior art exists] Accelerating Catalyst Materials Discovery With Large Artificial Intelligence Models

- Journal/date: Angewandte Chemie International Edition; `2026-02-17`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1002/anie.202526150
- Method tags: active learning / Bayesian optimization, foundation or pretrained model, ML interatomic potential, multimodal or literature-mining model
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion (Materials Today Sustainability, 2026-09-03)
  - active learning / Bayesian optimization: Computational and ML methods in MOF based supercapacitors - from mechanistic understanding to future materials design (Journal of Materials Science Materials Theory, 2026-08-29)
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)

### 6. [Older MOF prior art exists] Machine learning for predicting the glass transition and melting temperatures of polymers: molecular representations, model architectures, and interpretability

- Journal/date: Frontiers in Materials; `2026-09-03`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.3389/fmats.2026.1919251
- Method tags: active learning / Bayesian optimization, graph neural network, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion (Materials Today Sustainability, 2026-09-03)
  - active learning / Bayesian optimization: Computational and ML methods in MOF based supercapacitors - from mechanistic understanding to future materials design (Journal of Materials Science Materials Theory, 2026-08-29)
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)

### 7. [Older MOF prior art exists] Boosting Computational Catalysis and Chemical Reactivity with Artificial Intelligence

- Journal/date: Journal of the American Chemical Society; `2026-02-20`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1021/jacs.5c17786
- Method tags: foundation or pretrained model, generative / diffusion / inverse design, ML interatomic potential
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - foundation or pretrained model: uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks (arXiv (Cornell University), 2026-08-28)
  - foundation or pretrained model: Generalized Machine Learning Potentials for Predicting Low-Pressure Water Adsorption in Flexible Al-Based Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-08-25)
  - foundation or pretrained model: An LLM agent for end-to-end computational materials discovery (arXiv (Cornell University), 2026-08-20)

### 8. [Older MOF prior art exists] Thermal conductivity predictions with foundation atomistic models

- Journal/date: Nature Communications; `2026-09-05`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41467-026-76391-w
- Method tags: foundation or pretrained model, transfer learning / domain adaptation
- Transfer distance: distant method analogy
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - foundation or pretrained model: uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks (arXiv (Cornell University), 2026-08-28)
  - foundation or pretrained model: Generalized Machine Learning Potentials for Predicting Low-Pressure Water Adsorption in Flexible Al-Based Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-08-25)
  - foundation or pretrained model: An LLM agent for end-to-end computational materials discovery (arXiv (Cornell University), 2026-08-20)

### 9. [Older MOF prior art exists] Out-of-Distribution Inverse Design of Elastic Networks with Differentiable Graph Neural Network Molecular Dynamics

- Journal/date: arXiv (Cornell University); `2026-09-06`
- Candidate source: Cross-material ML transfer
- Link: https://arxiv.org/abs/2609.06655
- Method tags: generative / diffusion / inverse design, graph neural network, uncertainty / OOD
- Transfer distance: distant method analogy
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion (Materials Today Sustainability, 2026-09-03)
  - generative / diffusion / inverse design: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - uncertainty / OOD: Machine learning approach for MOF-based photocatalytic CO2 reduction to fuels (Energy Conversion and Management X, 2026-09-01)

### 10. [Older MOF prior art exists] Deep learning in materials electron microscopy: models, applications, and emerging trends

- Journal/date: Machine Learning Science and Technology; `2026-08-24`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1088/2632-2153/ae9dea
- Method tags: foundation or pretrained model, generative / diffusion / inverse design, multimodal or literature-mining model
- Transfer distance: distant method analogy
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - foundation or pretrained model: uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks (arXiv (Cornell University), 2026-08-28)
  - foundation or pretrained model: Generalized Machine Learning Potentials for Predicting Low-Pressure Water Adsorption in Flexible Al-Based Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-08-25)
  - foundation or pretrained model: An LLM agent for end-to-end computational materials discovery (arXiv (Cornell University), 2026-08-20)

### 11. [Older MOF prior art exists] Domain-specific dataset enable accurate MLIPs for disordered halide-based solid electrolytes

- Journal/date: Machine Learning Science and Technology; `2026-09-10`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1088/2632-2153/aea5d8
- Method tags: equivariant ML, foundation or pretrained model, ML interatomic potential, transfer learning / domain adaptation
- Transfer distance: adjacent materials
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - equivariant ML: uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks (arXiv (Cornell University), 2026-08-28)
  - equivariant ML: Generalized Machine Learning Potentials for Predicting Low-Pressure Water Adsorption in Flexible Al-Based Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-08-25)
  - foundation or pretrained model: An LLM agent for end-to-end computational materials discovery (arXiv (Cornell University), 2026-08-20)

### 12. [Older MOF prior art exists] Benchmarking on-the-Fly Machine Learning Force Fields for Ion Hydration: Structure, Coordination, and Exchange Dynamics across Monovalent and Divalent Cations

- Journal/date: The Journal of Physical Chemistry B; `2026-09-02`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1021/acs.jpcb.6c02837
- Method tags: equivariant ML, foundation or pretrained model
- Transfer distance: adjacent materials
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - equivariant ML: uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks (arXiv (Cornell University), 2026-08-28)
  - equivariant ML: Generalized Machine Learning Potentials for Predicting Low-Pressure Water Adsorption in Flexible Al-Based Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-08-25)
  - foundation or pretrained model: An LLM agent for end-to-end computational materials discovery (arXiv (Cornell University), 2026-08-20)

### 13. [Older MOF prior art exists] Accelerating density functional theory calculations using conditional generative-adversarial neural networks

- Journal/date: npj Computational Materials; `2026-09-09`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41524-026-02308-2
- Method tags: surrogate or multi-fidelity model
- Transfer distance: distant method analogy
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - surrogate or multi-fidelity model: Computational and ML methods in MOF based supercapacitors - from mechanistic understanding to future materials design (Journal of Materials Science Materials Theory, 2026-08-29)

### 14. [Older MOF prior art exists] Accelerated stable structure prediction of Li-intercalated bilayer graphene using a data-efficient deep learning framework

- Journal/date: npj Computational Materials; `2026-09-04`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41524-026-02314-4
- Method tags: ML interatomic potential
- Transfer distance: adjacent materials
- Candidate MOF route: Use the MLIP workflow for flexible, guest-loaded, charged, or diffusion-transition MOF configurations.
- MOF transfer note: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.
- Suggested next step: Extend training to guest-loaded, distorted, and diffusion-transition configurations. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - ML interatomic potential: uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks (arXiv (Cornell University), 2026-08-28)
  - ML interatomic potential: Generalized Machine Learning Potentials for Predicting Low-Pressure Water Adsorption in Flexible Al-Based Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-08-25)

### 15. [Older MOF prior art exists] TAME: Element-wise Mixture-of-Experts Fusion for Reliable and Interpretable Molecular Property Prediction

- Journal/date: ChemRxiv; `2026-09-07`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.26434/chemrxiv.15008270/v2
- Method tags: graph neural network, self-supervised learning, transfer learning / domain adaptation
- Transfer distance: adjacent materials
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - transfer learning / domain adaptation: Generalized Machine Learning Potentials for Predicting Low-Pressure Water Adsorption in Flexible Al-Based Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-08-25)
  - transfer learning / domain adaptation: Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks via Machine Learning-Symbolic Regression (arXiv (Cornell University), 2026-08-15)

### 16. [Older MOF prior art exists] Defect engineering of semiconductor photocatalysts for solar energy conversion: from atomic-level design to AI-driven materials discovery for sustainable development and clean energy

- Journal/date: Materials & Design; `2026-09-08`
- Candidate source: Cross-material ML transfer; Reaction/catalyst ML transfer
- Link: https://doi.org/10.1016/j.matdes.2026.116917
- Method tags: generative / diffusion / inverse design
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion (Materials Today Sustainability, 2026-09-03)
  - generative / diffusion / inverse design: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)

### 17. [Older MOF prior art exists] Large language models for applied superconductivity: towards physics-aware reasoning and integrated multi-modal generative AI

- Journal/date: Superconductor Science and Technology; `2026-08-24`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1088/1361-6668/ae9df9
- Method tags: foundation or pretrained model, generative / diffusion / inverse design, multimodal or literature-mining model, uncertainty / OOD
- Transfer distance: distant method analogy
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - foundation or pretrained model: uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks (arXiv (Cornell University), 2026-08-28)
  - foundation or pretrained model: Generalized Machine Learning Potentials for Predicting Low-Pressure Water Adsorption in Flexible Al-Based Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-08-25)
  - foundation or pretrained model: An LLM agent for end-to-end computational materials discovery (arXiv (Cornell University), 2026-08-20)

### 18. [Older MOF prior art exists] Performance of universal machine learning potentials in global optimization of inorganic crystal structures

- Journal/date: Machine Learning Science and Technology; `2026-09-09`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1088/2632-2153/ae94e1
- Method tags: equivariant ML, foundation or pretrained model, ML interatomic potential
- Transfer distance: adjacent materials
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - equivariant ML: uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks (arXiv (Cornell University), 2026-08-28)
  - equivariant ML: Generalized Machine Learning Potentials for Predicting Low-Pressure Water Adsorption in Flexible Al-Based Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-08-25)
  - foundation or pretrained model: An LLM agent for end-to-end computational materials discovery (arXiv (Cornell University), 2026-08-20)

### 19. [Older MOF prior art exists] Simultaneous retrieval of 13 phytoplankton pigments from Sentinel-3 OLCI using convolutional neural networks and transfer learning

- Journal/date: Frontiers in Remote Sensing; `2026-09-10`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.3389/frsen.2026.1880618
- Method tags: self-supervised learning, transfer learning / domain adaptation
- Transfer distance: distant method analogy
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - transfer learning / domain adaptation: Generalized Machine Learning Potentials for Predicting Low-Pressure Water Adsorption in Flexible Al-Based Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-08-25)
  - transfer learning / domain adaptation: Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks via Machine Learning-Symbolic Regression (arXiv (Cornell University), 2026-08-15)

### 20. [Older MOF prior art exists] Entropy-Guided Dataset Reduction for Machine-Learned Interatomic Potentials

- Journal/date: ChemRxiv; `2026-09-09`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.26434/chemrxiv.15008542/v1
- Method tags: ML interatomic potential, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- Long-horizon MOF prior art:
  - ML interatomic potential: uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks (arXiv (Cornell University), 2026-08-28)
  - ML interatomic potential: Generalized Machine Learning Potentials for Predicting Low-Pressure Water Adsorption in Flexible Al-Based Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-08-25)
  - uncertainty / OOD: Machine learning approach for MOF-based photocatalytic CO2 reduction to fuels (Energy Conversion and Management X, 2026-09-01)

## Reading Rules

- Fresh means no same method-class tag was found in the recent or long-horizon MOF baselines. It still needs full-paper confirmation.
- Distant cross-domain methods are allowed when the method can be mapped to a concrete MOF object, such as structure images, spectra, isotherms, pore maps, generated CIF checks, or multimodal literature-structure consistency.
- Older prior art means the idea is not new to MOFs, but it may still be worth pursuing if the cross-material paper adds a new representation, label space, uncertainty loop, active-learning strategy, or validation regime.
- Recent MOF activity means lower novelty unless the new method opens a clearly different MOF task or implementation path.
