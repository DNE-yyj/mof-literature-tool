# Method Transfer Novelty Report

- Generated: `2026-07-06T12:41:16`
- Logic: cross-material ML methods are candidate ideas; recent MOF literature checks current adoption; long-horizon MOF prior art checks older adoption.

## Source Runs

- Recent MOF literature: profile `mof_latest_custom`, since `2025-07-06`, papers `3`
  - Report: `D:\rose_data\博士阶段\research_complate\work1\literature_tool\reports\weekly_mof_latest\20260706_124116\report.md`
- Cross-material ML transfer: profile `materials_ml_transfer`, since `2023-07-07`, papers `30`
  - Report: `D:\rose_data\博士阶段\research_complate\work1\literature_tool\reports\materials_ml_transfer\20260706_124140\report.md`
- Long-horizon MOF method prior art: profile `mof_ml_method_prior_art`, since `2016-07-08`, papers `11`
  - Report: `D:\rose_data\博士阶段\research_complate\work1\literature_tool\reports\mof_ml_method_prior_art\20260706_124224\report.md`

## Triage Summary

- Fresh MOF transfer candidates: `2`
- Older MOF prior art exists: `11`
- Already active in recent MOF literature: `17`

## Method-Class Baseline

| Method class | Cross-material ML | Recent MOF | Long-horizon MOF prior art |
|---|---:|---:|---:|
| active learning / Bayesian optimization | 9 | 1 | 2 |
| equivariant ML | 6 | 0 | 0 |
| foundation or pretrained model | 8 | 0 | 4 |
| generative / diffusion / inverse design | 5 | 0 | 2 |
| graph neural network | 4 | 0 | 0 |
| ML interatomic potential | 12 | 0 | 1 |
| multimodal or literature-mining model | 3 | 0 | 0 |
| physics-informed ML | 4 | 0 | 0 |
| self-supervised learning | 3 | 0 | 0 |
| surrogate or multi-fidelity model | 3 | 0 | 0 |
| symbolic regression / descriptor discovery | 2 | 0 | 0 |
| transfer learning / domain adaptation | 5 | 0 | 0 |
| uncertainty / OOD | 12 | 1 | 1 |

## Transfer Opportunities

### 1. [Fresh MOF transfer candidate] Equivariant Graph Neural Networks Improve Optical Spectra Prediction for Materials Screening

- Journal/date: arXiv (Cornell University); `2026-06-17`
- Link: https://arxiv.org/abs/2606.19133
- Method tags: equivariant ML, graph neural network, surrogate or multi-fidelity model
- MOF transfer note: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
- Suggested next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 2. [Fresh MOF transfer candidate] Fourier-KAGAT: resolving activity cliffs in organic photocatalysts via Fourier-based learnable activations

- Journal/date: npj Computational Materials; `2026-06-20`
- Link: https://doi.org/10.1038/s41524-026-02194-8
- Method tags: graph neural network
- MOF transfer note: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
- Suggested next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 3. [Older MOF prior art exists] Adaptive fine-tuning of foundation models for crystal structure prediction: Discovery of high-pressure phases in the CaFeNi system

- Journal/date: arXiv (Cornell University); `2026-06-29`
- Link: https://arxiv.org/abs/2606.30870
- Method tags: foundation or pretrained model, ML interatomic potential, transfer learning / domain adaptation
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents (arXiv (Cornell University), 2026-06-28)
  - foundation or pretrained model: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (arXiv (Cornell University), 2026-05-27)
  - foundation or pretrained model: ReadMOF: Structure-Free Semantic Embeddings from Systematic MOF Nomenclature for Machine Learning (ChemRxiv, 2026-04-13)

### 4. [Older MOF prior art exists] CoTAR: Topology and Atomic State Reconstruction in Condensed Phases

- Journal/date: arXiv (Cornell University); `2026-06-26`
- Link: https://arxiv.org/abs/2606.27636
- Method tags: graph neural network, ML interatomic potential, transfer learning / domain adaptation
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - ML interatomic potential: FLAMES – A flexible and extensible code for Monte Carlo simulations of nanoporous materials (ChemRxiv, 2026-06-11)

### 5. [Older MOF prior art exists] Chemical intuition on bond-dissociation energies as an emergent ability of universal machine-learning interatomic potentials

- Journal/date: Nature Communications; `2026-07-02`
- Link: https://doi.org/10.1038/s41467-026-74919-8
- Method tags: equivariant ML, ML interatomic potential
- MOF transfer note: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
- Suggested next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- Long-horizon MOF prior art:
  - ML interatomic potential: FLAMES – A flexible and extensible code for Monte Carlo simulations of nanoporous materials (ChemRxiv, 2026-06-11)

### 6. [Older MOF prior art exists] Guided Adaptive Diffusion: An Evolutionary Framework for Multimodal Atomistic Structure Prediction

- Journal/date: Journal of Chemical Information and Modeling; `2026-06-25`
- Link: https://doi.org/10.1021/acs.jcim.6c00843
- Method tags: generative / diffusion / inverse design, ML interatomic potential, multimodal or literature-mining model, physics-informed ML
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents (arXiv (Cornell University), 2026-06-28)
  - generative / diffusion / inverse design: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (arXiv (Cornell University), 2026-05-27)
  - ML interatomic potential: FLAMES – A flexible and extensible code for Monte Carlo simulations of nanoporous materials (ChemRxiv, 2026-06-11)

### 7. [Older MOF prior art exists] Data Enrichment for Symbolic Regression Using Diffusion Models

- Journal/date: arXiv (Cornell University); `2026-05-31`
- Link: https://arxiv.org/abs/2606.00988
- Method tags: generative / diffusion / inverse design, physics-informed ML, symbolic regression / descriptor discovery
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents (arXiv (Cornell University), 2026-06-28)
  - generative / diffusion / inverse design: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (arXiv (Cornell University), 2026-05-27)

### 8. [Older MOF prior art exists] A Combined Tight Binding with Machine Learning Potential Model for Magnesium Compounds

- Journal/date: arXiv (Cornell University); `2026-06-24`
- Link: https://arxiv.org/abs/2606.25853
- Method tags: equivariant ML, ML interatomic potential
- MOF transfer note: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
- Suggested next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- Long-horizon MOF prior art:
  - ML interatomic potential: FLAMES – A flexible and extensible code for Monte Carlo simulations of nanoporous materials (ChemRxiv, 2026-06-11)

### 9. [Older MOF prior art exists] Neutron and X-ray Diffraction Reveal the Limits of Long-Range Machine Learning Potentials for Medium-Range Order in Silica Glass

- Journal/date: Journal of Physics Materials; `2026-07-03`
- Link: https://doi.org/10.1088/2515-7639/ae8643
- Method tags: equivariant ML, ML interatomic potential
- MOF transfer note: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
- Suggested next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- Long-horizon MOF prior art:
  - ML interatomic potential: FLAMES – A flexible and extensible code for Monte Carlo simulations of nanoporous materials (ChemRxiv, 2026-06-11)

### 10. [Older MOF prior art exists] Latent Genetic Algorithm for Crystal Structure Prediction

- Journal/date: arXiv (Cornell University); `2026-06-28`
- Link: https://arxiv.org/abs/2606.29220
- Method tags: generative / diffusion / inverse design, ML interatomic potential
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents (arXiv (Cornell University), 2026-06-28)
  - generative / diffusion / inverse design: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (arXiv (Cornell University), 2026-05-27)
  - ML interatomic potential: FLAMES – A flexible and extensible code for Monte Carlo simulations of nanoporous materials (ChemRxiv, 2026-06-11)

### 11. [Older MOF prior art exists] Optimizing Expert-Designed Crystal Graph Networks for Band-Gap Prediction with an Autonomous LLM Research Loop

- Journal/date: arXiv (Cornell University); `2026-06-29`
- Link: https://arxiv.org/abs/2606.29717
- Method tags: foundation or pretrained model, graph neural network, self-supervised learning
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents (arXiv (Cornell University), 2026-06-28)
  - foundation or pretrained model: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (arXiv (Cornell University), 2026-05-27)
  - foundation or pretrained model: ReadMOF: Structure-Free Semantic Embeddings from Systematic MOF Nomenclature for Machine Learning (ChemRxiv, 2026-04-13)

### 12. [Older MOF prior art exists] A general-purpose atomic cluster expansion interatomic potential for niobium

- Journal/date: arXiv (Cornell University); `2026-07-01`
- Link: https://arxiv.org/abs/2607.00540
- Method tags: ML interatomic potential
- MOF transfer note: MLIP route can transfer to MOFs if trained on flexible, guest-loaded, and charged configurations.
- Suggested next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- Long-horizon MOF prior art:
  - ML interatomic potential: FLAMES – A flexible and extensible code for Monte Carlo simulations of nanoporous materials (ChemRxiv, 2026-06-11)

### 13. [Older MOF prior art exists] Universal Interatomic Potentials as Configuration-Space Generators for One-Shot and Iterative Fine-Tuning of Ab Initio-Accurate Material-Specific Models

- Journal/date: arXiv (Cornell University); `2026-06-22`
- Link: https://arxiv.org/abs/2606.23214
- Method tags: foundation or pretrained model, ML interatomic potential, transfer learning / domain adaptation
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents (arXiv (Cornell University), 2026-06-28)
  - foundation or pretrained model: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (arXiv (Cornell University), 2026-05-27)
  - foundation or pretrained model: ReadMOF: Structure-Free Semantic Embeddings from Systematic MOF Nomenclature for Machine Learning (ChemRxiv, 2026-04-13)

### 14. [Already active in recent MOF] Machine-Learning-Driven Molecular Design and Structure–Property–Performance Relationships in Pharmaceutical Chemistry

- Journal/date: Molecules; `2026-06-19`
- Link: https://doi.org/10.3390/molecules31122162
- Method tags: active learning / Bayesian optimization, equivariant ML, foundation or pretrained model, multimodal or literature-mining model, uncertainty / OOD
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Recent MOF evidence:
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - uncertainty / OOD: Descriptor Adequacy as a Materials-Regime Principle in MOF Adsorption Machine Learning (ChemRxiv, 2026-07-03)
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - active learning / Bayesian optimization: Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents (arXiv (Cornell University), 2026-06-28)
  - foundation or pretrained model: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (arXiv (Cornell University), 2026-05-27)

### 15. [Already active in recent MOF] Artificial Intelligence in Gas Hydrate Management: A Comprehensive Review

- Journal/date: Petroleum Research; `2026-07-01`
- Link: https://doi.org/10.1016/j.ptlrs.2026.06.002
- Method tags: physics-informed ML, self-supervised learning, uncertainty / OOD
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Recent MOF evidence:
  - uncertainty / OOD: Descriptor Adequacy as a Materials-Regime Principle in MOF Adsorption Machine Learning (ChemRxiv, 2026-07-03)
- Long-horizon MOF prior art:
  - uncertainty / OOD: Descriptor Adequacy as a Materials-Regime Principle in MOF Adsorption Machine Learning (ChemRxiv, 2026-07-03)

### 16. [Already active in recent MOF] The FAST Framework: Developing a Data-Efficient Machine Learning Potential to Decode Superionic Transition-Induced Thermophysical and Kinetic Anomalies in UO2 under Extreme Conditions

- Journal/date: arXiv (Cornell University); `2026-06-19`
- Link: https://arxiv.org/abs/2606.21796
- Method tags: active learning / Bayesian optimization, foundation or pretrained model, ML interatomic potential, transfer learning / domain adaptation
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Recent MOF evidence:
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - active learning / Bayesian optimization: Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents (arXiv (Cornell University), 2026-06-28)
  - foundation or pretrained model: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (arXiv (Cornell University), 2026-05-27)

### 17. [Already active in recent MOF] Breaking Bottlenecks in Solid Electrolyte Discovery with Large Artificial Intelligence Models

- Journal/date: arXiv (Cornell University); `2026-06-23`
- Link: https://arxiv.org/abs/2606.24480
- Method tags: active learning / Bayesian optimization, foundation or pretrained model, ML interatomic potential, multimodal or literature-mining model, uncertainty / OOD
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Recent MOF evidence:
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - uncertainty / OOD: Descriptor Adequacy as a Materials-Regime Principle in MOF Adsorption Machine Learning (ChemRxiv, 2026-07-03)
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - active learning / Bayesian optimization: Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents (arXiv (Cornell University), 2026-06-28)
  - foundation or pretrained model: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (arXiv (Cornell University), 2026-05-27)

### 18. [Already active in recent MOF] Phase prediction in high-entropy alloys through uncertainty sampling and symbolic classification-based parameter discovery

- Journal/date: npj Computational Materials; `2026-06-11`
- Link: https://doi.org/10.1038/s41524-026-02189-5
- Method tags: active learning / Bayesian optimization, uncertainty / OOD
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Recent MOF evidence:
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - uncertainty / OOD: Descriptor Adequacy as a Materials-Regime Principle in MOF Adsorption Machine Learning (ChemRxiv, 2026-07-03)
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - active learning / Bayesian optimization: Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents (arXiv (Cornell University), 2026-06-28)
  - uncertainty / OOD: Descriptor Adequacy as a Materials-Regime Principle in MOF Adsorption Machine Learning (ChemRxiv, 2026-07-03)

### 19. [Already active in recent MOF] Active Learning for Generalizable Detonation Performance Prediction of Energetic Materials

- Journal/date: Chemistry of Materials; `2026-06-30`
- Link: https://doi.org/10.1021/acs.chemmater.6c01049
- Method tags: active learning / Bayesian optimization, surrogate or multi-fidelity model
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Recent MOF evidence:
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - active learning / Bayesian optimization: Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents (arXiv (Cornell University), 2026-06-28)

### 20. [Already active in recent MOF] An active learning workflow for predicting misfit volume in body-centered cubic refractory high-entropy alloys

- Journal/date: Scientific Reports; `2026-06-10`
- Link: https://doi.org/10.1038/s41598-026-57006-2
- Method tags: active learning / Bayesian optimization, symbolic regression / descriptor discovery, uncertainty / OOD
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- Recent MOF evidence:
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - uncertainty / OOD: Descriptor Adequacy as a Materials-Regime Principle in MOF Adsorption Machine Learning (ChemRxiv, 2026-07-03)
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - active learning / Bayesian optimization: Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents (arXiv (Cornell University), 2026-06-28)
  - uncertainty / OOD: Descriptor Adequacy as a Materials-Regime Principle in MOF Adsorption Machine Learning (ChemRxiv, 2026-07-03)

## Reading Rules

- Fresh means no same method-class tag was found in the recent or long-horizon MOF baselines. It still needs full-paper confirmation.
- Older prior art means the idea is not new to MOFs, but it may still be worth pursuing if the cross-material paper adds a new representation, label space, uncertainty loop, active-learning strategy, or validation regime.
- Recent MOF activity means lower novelty unless the new method opens a clearly different MOF task or implementation path.
