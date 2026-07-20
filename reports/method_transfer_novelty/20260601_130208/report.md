# Method Transfer Novelty Report

- Generated: `2026-06-01T13:02:08`
- Logic: cross-material ML methods are candidate ideas; recent MOF literature checks current adoption; long-horizon MOF prior art checks older adoption.

## Source Runs

- Recent MOF literature: profile `mof_latest_custom`, since `2025-06-01`, papers `0`
  - Report: `D:\rose_data\博士阶段\research_complate\work1\literature_tool\reports\weekly_mof_latest\20260601_130208\report.md`
- Cross-material ML transfer: profile `materials_ml_transfer`, since `2023-06-02`, papers `30`
  - Report: `D:\rose_data\博士阶段\research_complate\work1\literature_tool\reports\materials_ml_transfer\20260601_130224\report.md`
- Long-horizon MOF method prior art: profile `mof_ml_method_prior_art`, since `2016-06-03`, papers `15`
  - Report: `D:\rose_data\博士阶段\research_complate\work1\literature_tool\reports\mof_ml_method_prior_art\20260601_130258\report.md`

## Triage Summary

- Fresh MOF transfer candidates: `4`
- Older MOF prior art exists: `26`
- Already active in recent MOF literature: `0`

## Method-Class Baseline

| Method class | Cross-material ML | Recent MOF | Long-horizon MOF prior art |
|---|---:|---:|---:|
| active learning / Bayesian optimization | 11 | 0 | 0 |
| equivariant ML | 8 | 0 | 3 |
| foundation or pretrained model | 11 | 0 | 7 |
| generative / diffusion / inverse design | 10 | 0 | 0 |
| graph neural network | 5 | 0 | 2 |
| ML interatomic potential | 12 | 0 | 7 |
| multimodal or literature-mining model | 4 | 0 | 1 |
| physics-informed ML | 6 | 0 | 0 |
| self-supervised learning | 1 | 0 | 0 |
| surrogate or multi-fidelity model | 4 | 0 | 0 |
| symbolic regression / descriptor discovery | 1 | 0 | 0 |
| transfer learning / domain adaptation | 6 | 0 | 3 |
| uncertainty / OOD | 10 | 0 | 1 |

## Transfer Opportunities

### 1. [Fresh MOF transfer candidate] Symmetry-aware Bayesian flow networks for crystal generation

- Journal/date: npj Computational Materials; `2026-05-19`
- Link: https://doi.org/10.1038/s41524-026-02140-8
- Method tags: generative / diffusion / inverse design, physics-informed ML
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 2. [Fresh MOF transfer candidate] Artificial intelligence in additive Manufacturing: advances in smart materials, lattice optimization, and process intelligence

- Journal/date: The International Journal of Advanced Manufacturing Technology; `2026-04-18`
- Link: https://doi.org/10.1007/s00170-026-18072-y
- Method tags: active learning / Bayesian optimization, physics-informed ML
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 3. [Fresh MOF transfer candidate] CrystalCGAIN: efficient generation and inverse design of porous crystal structures with target properties

- Journal/date: npj Computational Materials; `2026-05-28`
- Link: https://doi.org/10.1038/s41524-026-02138-2
- Method tags: generative / diffusion / inverse design
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 4. [Fresh MOF transfer candidate] Autonomous closed-loop framework for reproducible perovskite solar cells

- Journal/date: Apollo (University of Cambridge); `2026-04-21`
- Link: https://www.repository.cam.ac.uk/handle/1810/401657
- Method tags: active learning / Bayesian optimization, symbolic regression / descriptor discovery
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 5. [Older MOF prior art exists] Uncertainty-aware Machine Learning Interatomic Potentials via Learned Functional Perturbations

- Journal/date: ArXiv.org; `2026-05-19`
- Link: https://arxiv.org/abs/2605.19939
- Method tags: active learning / Bayesian optimization, equivariant ML, foundation or pretrained model, ML interatomic potential, transfer learning / domain adaptation, uncertainty / OOD
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - equivariant ML: Evaluating mechanical property prediction across material classes using molecular dynamics simulations with universal machine-learned interatomic potentials (Communications Chemistry, 2026-05-06)
  - equivariant ML: Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry (ArXiv.org, 2026-04-28)
  - foundation or pretrained model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)

### 6. [Older MOF prior art exists] From High-Throughput Screening to Generative Design: Artificial Intelligence-Driven Dielectric Materials Discovery

- Journal/date: ACS Applied Materials & Interfaces; `2026-05-20`
- Link: https://doi.org/10.1021/acsami.6c05353
- Method tags: active learning / Bayesian optimization, foundation or pretrained model, generative / diffusion / inverse design, physics-informed ML, surrogate or multi-fidelity model
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - foundation or pretrained model: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)
  - foundation or pretrained model: Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry (ArXiv.org, 2026-04-28)

### 7. [Older MOF prior art exists] Spatial statistics for screening molecular structures

- Journal/date: ArXiv.org; `2026-05-16`
- Link: https://arxiv.org/abs/2605.17147
- Method tags: active learning / Bayesian optimization, equivariant ML, generative / diffusion / inverse design, physics-informed ML, surrogate or multi-fidelity model
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - equivariant ML: Evaluating mechanical property prediction across material classes using molecular dynamics simulations with universal machine-learned interatomic potentials (Communications Chemistry, 2026-05-06)
  - equivariant ML: Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry (ArXiv.org, 2026-04-28)

### 8. [Older MOF prior art exists] MEIDNet: multimodal generative AI framework for inverse materials design

- Journal/date: npj Computational Materials; `2026-05-29`
- Link: https://doi.org/10.1038/s41524-026-02153-3
- Method tags: equivariant ML, generative / diffusion / inverse design, graph neural network, multimodal or literature-mining model, self-supervised learning
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - equivariant ML: Evaluating mechanical property prediction across material classes using molecular dynamics simulations with universal machine-learned interatomic potentials (Communications Chemistry, 2026-05-06)
  - equivariant ML: Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry (ArXiv.org, 2026-04-28)
  - graph neural network: PoroNet: An Intrinsically Interpretable Pore Graph Neural Network for Resolving Pore-Level Adsorption in Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-05-28)

### 9. [Older MOF prior art exists] A graph neural network for the era of large atomistic models

- Journal/date: npj Computational Materials; `2026-05-25`
- Link: https://doi.org/10.1038/s41524-026-02146-2
- Method tags: foundation or pretrained model, graph neural network, ML interatomic potential, transfer learning / domain adaptation
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - foundation or pretrained model: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)
  - foundation or pretrained model: Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry (ArXiv.org, 2026-04-28)

### 10. [Older MOF prior art exists] Direct Simulation of LiNi0.8Mn0.1Co0.1O2 Transport Properties Using an Efficient and Accurate Machine Learning Potential

- Journal/date: ArXiv.org; `2026-05-19`
- Link: https://arxiv.org/abs/2605.19747
- Method tags: active learning / Bayesian optimization, equivariant ML, foundation or pretrained model, graph neural network, ML interatomic potential, uncertainty / OOD
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - equivariant ML: Evaluating mechanical property prediction across material classes using molecular dynamics simulations with universal machine-learned interatomic potentials (Communications Chemistry, 2026-05-06)
  - equivariant ML: Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry (ArXiv.org, 2026-04-28)
  - foundation or pretrained model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)

### 11. [Older MOF prior art exists] Guided diffusion for the discovery of new superconductors

- Journal/date: npj Computational Materials; `2026-05-28`
- Link: https://doi.org/10.1038/s41524-026-02117-7
- Method tags: foundation or pretrained model, generative / diffusion / inverse design
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - foundation or pretrained model: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)
  - foundation or pretrained model: Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry (ArXiv.org, 2026-04-28)

### 12. [Older MOF prior art exists] Training-free active learning framework in materials science with large language models

- Journal/date: npj Computational Materials; `2026-05-20`
- Link: https://doi.org/10.1038/s41524-026-02136-4
- Method tags: active learning / Bayesian optimization, foundation or pretrained model, transfer learning / domain adaptation
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - foundation or pretrained model: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)
  - foundation or pretrained model: Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry (ArXiv.org, 2026-04-28)

### 13. [Older MOF prior art exists] Neural network self-consistent fields for density functional theory

- Journal/date: npj Computational Materials; `2026-05-30`
- Link: https://doi.org/10.1038/s41524-026-02110-0
- Method tags: equivariant ML, uncertainty / OOD
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - equivariant ML: Evaluating mechanical property prediction across material classes using molecular dynamics simulations with universal machine-learned interatomic potentials (Communications Chemistry, 2026-05-06)
  - equivariant ML: Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry (ArXiv.org, 2026-04-28)
  - uncertainty / OOD: BaLoRA: Bayesian Low-Rank Adaptation of Large Scale Models (ArXiv.org, 2026-04-27)

### 14. [Older MOF prior art exists] Efficient Parallelization of Message Passing Neural Network Potentials for Large-Scale Molecular Dynamics

- Journal/date: JACS Au; `2026-05-25`
- Link: https://doi.org/10.1021/jacsau.6c00210
- Method tags: graph neural network, ML interatomic potential
- MOF transfer note: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
- Suggested next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Extend training to guest-loaded, distorted, and diffusion-transition configurations.
- Long-horizon MOF prior art:
  - graph neural network: PoroNet: An Intrinsically Interpretable Pore Graph Neural Network for Resolving Pore-Level Adsorption in Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-05-28)
  - graph neural network: Evaluating mechanical property prediction across material classes using molecular dynamics simulations with universal machine-learned interatomic potentials (Communications Chemistry, 2026-05-06)
  - ML interatomic potential: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)

### 15. [Older MOF prior art exists] Dataset-aware entropy-maximized active learning for machine-learned interatomic potentials

- Journal/date: ArXiv.org; `2026-05-19`
- Link: https://arxiv.org/abs/2605.20384
- Method tags: active learning / Bayesian optimization, equivariant ML, foundation or pretrained model, ML interatomic potential
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - equivariant ML: Evaluating mechanical property prediction across material classes using molecular dynamics simulations with universal machine-learned interatomic potentials (Communications Chemistry, 2026-05-06)
  - equivariant ML: Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry (ArXiv.org, 2026-04-28)
  - foundation or pretrained model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)

### 16. [Older MOF prior art exists] LEAP: A closed-loop framework for perovskite precursor additive discovery

- Journal/date: ArXiv.org; `2026-05-18`
- Link: https://arxiv.org/abs/2605.20242
- Method tags: active learning / Bayesian optimization, foundation or pretrained model, transfer learning / domain adaptation, uncertainty / OOD
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - foundation or pretrained model: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)
  - foundation or pretrained model: Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry (ArXiv.org, 2026-04-28)

### 17. [Older MOF prior art exists] A Systematic Survey and Benchmark of Deep Learning for Molecular Property Prediction in the Foundation Model Era

- Journal/date: ChemRxiv; `2026-04-20`
- Link: https://doi.org/10.26434/chemrxiv.15002208/v1
- Method tags: foundation or pretrained model, multimodal or literature-mining model, uncertainty / OOD
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - foundation or pretrained model: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)
  - foundation or pretrained model: Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry (ArXiv.org, 2026-04-28)

### 18. [Older MOF prior art exists] A Systematic Survey and Benchmark of Deep Learning for Molecular Property Prediction in the Foundation Model Era

- Journal/date: ArXiv.org; `2026-04-17`
- Link: https://arxiv.org/abs/2604.16586
- Method tags: foundation or pretrained model, multimodal or literature-mining model, uncertainty / OOD
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - foundation or pretrained model: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)
  - foundation or pretrained model: Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry (ArXiv.org, 2026-04-28)

### 19. [Older MOF prior art exists] Attention-enhanced variational learning for physically informed discovery of exceptionally hard multicomponent bulk metallic glasses

- Journal/date: Nature Communications; `2026-05-12`
- Link: https://doi.org/10.1038/s41467-026-73008-0
- Method tags: generative / diffusion / inverse design, uncertainty / OOD
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - uncertainty / OOD: BaLoRA: Bayesian Low-Rank Adaptation of Large Scale Models (ArXiv.org, 2026-04-27)

### 20. [Older MOF prior art exists] Design topological materials by reinforcement fine-tuned generative model

- Journal/date: Nature Communications; `2026-05-18`
- Link: https://doi.org/10.1038/s41467-026-73321-8
- Method tags: generative / diffusion / inverse design, transfer learning / domain adaptation, uncertainty / OOD
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - transfer learning / domain adaptation: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - transfer learning / domain adaptation: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)
  - transfer learning / domain adaptation: BaLoRA: Bayesian Low-Rank Adaptation of Large Scale Models (ArXiv.org, 2026-04-27)

## Reading Rules

- Fresh means no same method-class tag was found in the recent or long-horizon MOF baselines. It still needs full-paper confirmation.
- Older prior art means the idea is not new to MOFs, but it may still be worth pursuing if the cross-material paper adds a new representation, label space, uncertainty loop, active-learning strategy, or validation regime.
- Recent MOF activity means lower novelty unless the new method opens a clearly different MOF task or implementation path.
