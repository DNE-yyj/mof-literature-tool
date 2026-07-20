# Method Transfer Novelty Report

- Generated: `2026-06-09T12:54:36`
- Logic: cross-material ML methods are candidate ideas; recent MOF literature checks current adoption; long-horizon MOF prior art checks older adoption.

## Source Runs

- Recent MOF literature: profile `mof_latest_custom`, since `2025-06-09`, papers `1`
  - Report: `D:\rose_data\博士阶段\research_complate\work1\literature_tool\reports\weekly_mof_latest\20260609_125436\report.md`
- Cross-material ML transfer: profile `materials_ml_transfer`, since `2023-06-10`, papers `30`
  - Report: `D:\rose_data\博士阶段\research_complate\work1\literature_tool\reports\materials_ml_transfer\20260609_125455\report.md`
- Long-horizon MOF method prior art: profile `mof_ml_method_prior_art`, since `2016-06-11`, papers `16`
  - Report: `D:\rose_data\博士阶段\research_complate\work1\literature_tool\reports\mof_ml_method_prior_art\20260609_125540\report.md`

## Triage Summary

- Fresh MOF transfer candidates: `0`
- Older MOF prior art exists: `30`
- Already active in recent MOF literature: `0`

## Method-Class Baseline

| Method class | Cross-material ML | Recent MOF | Long-horizon MOF prior art |
|---|---:|---:|---:|
| active learning / Bayesian optimization | 6 | 0 | 0 |
| equivariant ML | 6 | 0 | 3 |
| foundation or pretrained model | 9 | 0 | 8 |
| generative / diffusion / inverse design | 12 | 0 | 1 |
| graph neural network | 8 | 0 | 3 |
| ML interatomic potential | 10 | 0 | 7 |
| multimodal or literature-mining model | 9 | 0 | 1 |
| physics-informed ML | 10 | 0 | 0 |
| self-supervised learning | 5 | 0 | 0 |
| symbolic regression / descriptor discovery | 1 | 0 | 0 |
| transfer learning / domain adaptation | 9 | 0 | 3 |
| uncertainty / OOD | 7 | 0 | 2 |

## Transfer Opportunities

### 1. [Older MOF prior art exists] Prototype-Guided Latent Alignment for Data-Efficient Fine-Tuning of Molecular Foundation Models

- Journal/date: ArXiv.org; `2026-05-28`
- Link: https://arxiv.org/abs/2605.29969
- Method tags: equivariant ML, foundation or pretrained model, graph neural network, ML interatomic potential, transfer learning / domain adaptation, uncertainty / OOD
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - equivariant ML: Evaluating mechanical property prediction across material classes using molecular dynamics simulations with universal machine-learned interatomic potentials (Communications Chemistry, 2026-05-06)
  - equivariant ML: Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry (ArXiv.org, 2026-04-28)
  - foundation or pretrained model: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)

### 2. [Older MOF prior art exists] MEIDNet: multimodal generative AI framework for inverse materials design

- Journal/date: npj Computational Materials; `2026-05-29`
- Link: https://doi.org/10.1038/s41524-026-02153-3
- Method tags: equivariant ML, generative / diffusion / inverse design, graph neural network, multimodal or literature-mining model, self-supervised learning
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - equivariant ML: Evaluating mechanical property prediction across material classes using molecular dynamics simulations with universal machine-learned interatomic potentials (Communications Chemistry, 2026-05-06)
  - equivariant ML: Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry (ArXiv.org, 2026-04-28)
  - generative / diffusion / inverse design: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)

### 3. [Older MOF prior art exists] A graph neural network for the era of large atomistic models

- Journal/date: npj Computational Materials; `2026-05-25`
- Link: https://doi.org/10.1038/s41524-026-02146-2
- Method tags: foundation or pretrained model, graph neural network, ML interatomic potential, transfer learning / domain adaptation
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)
  - foundation or pretrained model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - foundation or pretrained model: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)

### 4. [Older MOF prior art exists] Towards Automated Discovery: A Review of Generative Models, Multimodal Learning and Closed-Loop Workflows in Inverse Materials Design

- Journal/date: ArXiv.org; `2026-06-01`
- Link: https://arxiv.org/abs/2606.02507
- Method tags: active learning / Bayesian optimization, generative / diffusion / inverse design, multimodal or literature-mining model, physics-informed ML
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)
  - multimodal or literature-mining model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)

### 5. [Older MOF prior art exists] Towards Automated Discovery: A Review of Generative Models, Multimodal Learning and Closed-Loop Workflows in Inverse Materials Design

- Journal/date: arXiv (Cornell University); `2026-06-01`
- Link: https://doi.org/10.48550/arxiv.2606.02507
- Method tags: active learning / Bayesian optimization, generative / diffusion / inverse design, multimodal or literature-mining model, physics-informed ML
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)
  - multimodal or literature-mining model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)

### 6. [Older MOF prior art exists] Guided diffusion for the discovery of new superconductors

- Journal/date: npj Computational Materials; `2026-05-28`
- Link: https://doi.org/10.1038/s41524-026-02117-7
- Method tags: foundation or pretrained model, generative / diffusion / inverse design
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)
  - foundation or pretrained model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - foundation or pretrained model: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)

### 7. [Older MOF prior art exists] Stein Kernelized Molecular Dynamics for Active Learning of Interatomic Potentials

- Journal/date: ArXiv.org; `2026-06-02`
- Link: https://arxiv.org/abs/2606.04100
- Method tags: active learning / Bayesian optimization, equivariant ML, ML interatomic potential, physics-informed ML, transfer learning / domain adaptation
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - equivariant ML: Evaluating mechanical property prediction across material classes using molecular dynamics simulations with universal machine-learned interatomic potentials (Communications Chemistry, 2026-05-06)
  - equivariant ML: Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry (ArXiv.org, 2026-04-28)
  - ML interatomic potential: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)

### 8. [Older MOF prior art exists] Differentiable Particle-Mesh Ewald with Cartesian Tensor Message Passing for Learning Long-Range Electrostatics and Dipole Response

- Journal/date: arXiv (Cornell University); `2026-06-01`
- Link: https://arxiv.org/abs/2606.01598
- Method tags: equivariant ML, graph neural network, ML interatomic potential, physics-informed ML, uncertainty / OOD
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - equivariant ML: Evaluating mechanical property prediction across material classes using molecular dynamics simulations with universal machine-learned interatomic potentials (Communications Chemistry, 2026-05-06)
  - equivariant ML: Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry (ArXiv.org, 2026-04-28)
  - graph neural network: Are Atoms Enough? An Explainable Graph Neural Network for Carbon Capture and Gas Separation in Metal-Organic Frameworks (ChemRxiv, 2026-06-02)

### 9. [Older MOF prior art exists] Non-covalent Interactions at cm$^{-1}$ Accuracy: Data Efficient Physics-Informed Distillation for Machine Learning Interatomic Potentials

- Journal/date: ArXiv.org; `2026-06-03`
- Link: https://arxiv.org/abs/2606.05127
- Method tags: foundation or pretrained model, ML interatomic potential, physics-informed ML, transfer learning / domain adaptation
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)
  - foundation or pretrained model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - foundation or pretrained model: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)

### 10. [Older MOF prior art exists] A Systematic Survey and Benchmark of Deep Learning for Molecular Property Prediction in the Foundation Model Era

- Journal/date: Journal of Chemical Theory and Computation; `2026-05-07`
- Link: https://doi.org/10.1021/acs.jctc.5c02081
- Method tags: foundation or pretrained model, multimodal or literature-mining model, uncertainty / OOD
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)
  - foundation or pretrained model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - foundation or pretrained model: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)

### 11. [Older MOF prior art exists] Escaping the hydrolysis trap: a react agent for inverse design of durable photocatalytic covalent organic frameworks

- Journal/date: npj Computational Materials; `2026-06-03`
- Link: https://doi.org/10.1038/s41524-026-02168-w
- Method tags: active learning / Bayesian optimization, foundation or pretrained model, generative / diffusion / inverse design
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)
  - foundation or pretrained model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - foundation or pretrained model: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)

### 12. [Older MOF prior art exists] Latent Diffusion Pretraining for Crystal Property Prediction

- Journal/date: arXiv (Cornell University); `2026-05-30`
- Link: https://arxiv.org/abs/2606.00776
- Method tags: generative / diffusion / inverse design, graph neural network, self-supervised learning, transfer learning / domain adaptation
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)
  - graph neural network: Are Atoms Enough? An Explainable Graph Neural Network for Carbon Capture and Gas Separation in Metal-Organic Frameworks (ChemRxiv, 2026-06-02)
  - graph neural network: PoroNet: An Intrinsically Interpretable Pore Graph Neural Network for Resolving Pore-Level Adsorption in Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-05-28)

### 13. [Older MOF prior art exists] A multimodal large language model for materials science

- Journal/date: Nature Machine Intelligence; `2026-04-24`
- Link: https://doi.org/10.1038/s42256-026-01214-y
- Method tags: foundation or pretrained model, ML interatomic potential, multimodal or literature-mining model
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)
  - foundation or pretrained model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - foundation or pretrained model: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)

### 14. [Older MOF prior art exists] AI-Driven Image Processing for Microstructure and Surface Characterization: A Systematic Review of Methods, Materials, and Applications

- Journal/date: Archives of Computational Methods in Engineering; `2026-05-30`
- Link: https://doi.org/10.1007/s11831-026-10641-4
- Method tags: generative / diffusion / inverse design, physics-informed ML, transfer learning / domain adaptation
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)
  - transfer learning / domain adaptation: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - transfer learning / domain adaptation: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)

### 15. [Older MOF prior art exists] A Padding Method for Enhanced Encoding of Inorganic Structures with Varying Chemical Compositions

- Journal/date: ArXiv.org; `2026-05-29`
- Link: https://arxiv.org/abs/2605.30743
- Method tags: generative / diffusion / inverse design, ML interatomic potential, physics-informed ML
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)
  - ML interatomic potential: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - ML interatomic potential: Evaluating mechanical property prediction across material classes using molecular dynamics simulations with universal machine-learned interatomic potentials (Communications Chemistry, 2026-05-06)

### 16. [Older MOF prior art exists] Active learning of collinear magnetic Moment Tensor Potentials using the spin-MLIP package from soft-constrained spin-polarized DFT calculations: a case study of Fe-Pd

- Journal/date: ArXiv.org; `2026-05-26`
- Link: https://arxiv.org/abs/2605.26897
- Method tags: active learning / Bayesian optimization, ML interatomic potential, uncertainty / OOD
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- Long-horizon MOF prior art:
  - ML interatomic potential: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - ML interatomic potential: Evaluating mechanical property prediction across material classes using molecular dynamics simulations with universal machine-learned interatomic potentials (Communications Chemistry, 2026-05-06)
  - ML interatomic potential: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)

### 17. [Older MOF prior art exists] Generative modelling of inorganic materials with explicit electronic structure

- Journal/date: Nature Communications; `2026-06-02`
- Link: https://doi.org/10.1038/s41467-026-73985-2
- Method tags: generative / diffusion / inverse design
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)

### 18. [Older MOF prior art exists] PhaseTransfer: A transfer learning framework for efficient phase diagram mapping

- Journal/date: npj Computational Materials; `2026-05-26`
- Link: https://doi.org/10.1038/s41524-026-02154-2
- Method tags: active learning / Bayesian optimization, transfer learning / domain adaptation
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - transfer learning / domain adaptation: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - transfer learning / domain adaptation: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)
  - transfer learning / domain adaptation: BaLoRA: Bayesian Low-Rank Adaptation of Large Scale Models (ArXiv.org, 2026-04-27)

### 19. [Older MOF prior art exists] Reducing bias and enhancing equity in AI-enabled precision nutrition: addressing measurement error across wearables, multiomics, and dietary data

- Journal/date: Frontiers in Digital Health; `2026-06-04`
- Link: https://doi.org/10.3389/fdgth.2026.1805704
- Method tags: multimodal or literature-mining model, uncertainty / OOD
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - multimodal or literature-mining model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - uncertainty / OOD: Are Atoms Enough? An Explainable Graph Neural Network for Carbon Capture and Gas Separation in Metal-Organic Frameworks (ChemRxiv, 2026-06-02)
  - uncertainty / OOD: BaLoRA: Bayesian Low-Rank Adaptation of Large Scale Models (ArXiv.org, 2026-04-27)

### 20. [Older MOF prior art exists] Book of Abstracts: Past, Present and Future of Particle Technology Conference 2026

- Journal/date: White Rose Research Online (University of Leeds, The University of Sheffield, University of York); `2026-06-03`
- Link: https://openalex.org/W7163721383
- Method tags: equivariant ML, graph neural network, physics-informed ML
- MOF transfer note: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
- Suggested next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - equivariant ML: Evaluating mechanical property prediction across material classes using molecular dynamics simulations with universal machine-learned interatomic potentials (Communications Chemistry, 2026-05-06)
  - equivariant ML: Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry (ArXiv.org, 2026-04-28)
  - graph neural network: Are Atoms Enough? An Explainable Graph Neural Network for Carbon Capture and Gas Separation in Metal-Organic Frameworks (ChemRxiv, 2026-06-02)

## Reading Rules

- Fresh means no same method-class tag was found in the recent or long-horizon MOF baselines. It still needs full-paper confirmation.
- Older prior art means the idea is not new to MOFs, but it may still be worth pursuing if the cross-material paper adds a new representation, label space, uncertainty loop, active-learning strategy, or validation regime.
- Recent MOF activity means lower novelty unless the new method opens a clearly different MOF task or implementation path.
