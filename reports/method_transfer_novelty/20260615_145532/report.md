# Method Transfer Novelty Report

- Generated: `2026-06-15T14:55:32`
- Logic: cross-material ML methods are candidate ideas; recent MOF literature checks current adoption; long-horizon MOF prior art checks older adoption.

## Source Runs

- Recent MOF literature: profile `mof_latest_custom`, since `2025-06-15`, papers `1`
  - Report: `D:\rose_data\博士阶段\research_complate\work1\literature_tool\reports\weekly_mof_latest\20260615_145532\report.md`
- Cross-material ML transfer: profile `materials_ml_transfer`, since `2023-06-16`, papers `30`
  - Report: `D:\rose_data\博士阶段\research_complate\work1\literature_tool\reports\materials_ml_transfer\20260615_145603\report.md`
- Long-horizon MOF method prior art: profile `mof_ml_method_prior_art`, since `2016-06-17`, papers `17`
  - Report: `D:\rose_data\博士阶段\research_complate\work1\literature_tool\reports\mof_ml_method_prior_art\20260615_145713\report.md`

## Triage Summary

- Fresh MOF transfer candidates: `0`
- Older MOF prior art exists: `22`
- Already active in recent MOF literature: `8`

## Method-Class Baseline

| Method class | Cross-material ML | Recent MOF | Long-horizon MOF prior art |
|---|---:|---:|---:|
| active learning / Bayesian optimization | 8 | 0 | 0 |
| equivariant ML | 8 | 0 | 2 |
| foundation or pretrained model | 8 | 0 | 7 |
| generative / diffusion / inverse design | 13 | 0 | 1 |
| graph neural network | 10 | 0 | 3 |
| ML interatomic potential | 8 | 1 | 7 |
| multimodal or literature-mining model | 4 | 0 | 1 |
| physics-informed ML | 14 | 0 | 0 |
| self-supervised learning | 2 | 0 | 0 |
| symbolic regression / descriptor discovery | 2 | 0 | 0 |
| transfer learning / domain adaptation | 7 | 0 | 3 |
| uncertainty / OOD | 8 | 0 | 2 |

## Transfer Opportunities

### 1. [Older MOF prior art exists] Towards Automated Discovery: A Review of Generative Models, Multimodal Learning and Closed-Loop Workflows in Inverse Materials Design

- Journal/date: ArXiv.org; `2026-06-01`
- Link: https://arxiv.org/abs/2606.02507
- Method tags: active learning / Bayesian optimization, generative / diffusion / inverse design, multimodal or literature-mining model, physics-informed ML
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)
  - multimodal or literature-mining model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)

### 2. [Older MOF prior art exists] Towards Automated Discovery: A Review of Generative Models, Multimodal Learning and Closed-Loop Workflows in Inverse Materials Design

- Journal/date: arXiv (Cornell University); `2026-06-01`
- Link: https://doi.org/10.48550/arxiv.2606.02507
- Method tags: active learning / Bayesian optimization, generative / diffusion / inverse design, multimodal or literature-mining model, physics-informed ML
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)
  - multimodal or literature-mining model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)

### 3. [Older MOF prior art exists] DSpinGNN: A Physics-Informed Equivariant Graph Neural Network for Dynamic Magnetic Exchange Prediction in Strain-Deformed Monolayer CrI$_3$

- Journal/date: ArXiv.org; `2026-06-10`
- Link: https://arxiv.org/abs/2606.11685
- Method tags: equivariant ML, graph neural network, physics-informed ML, uncertainty / OOD
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - equivariant ML: Evaluating mechanical property prediction across material classes using molecular dynamics simulations with universal machine-learned interatomic potentials (Communications Chemistry, 2026-05-06)
  - equivariant ML: Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry (ArXiv.org, 2026-04-28)
  - graph neural network: Are Atoms Enough? An Explainable Graph Neural Network for Carbon Capture and Gas Separation in Metal-Organic Frameworks (ChemRxiv, 2026-06-02)

### 4. [Older MOF prior art exists] Inverse Design of Amorphous Materials With Targeted Properties

- Journal/date: Advanced Materials; `2026-06-09`
- Link: https://doi.org/10.1002/adma.202522493
- Method tags: generative / diffusion / inverse design
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)

### 5. [Older MOF prior art exists] Physics-informed generative AI for semiconductor manufacturing: Enforcing hard physical constraints in generative models by construction

- Journal/date: ArXiv.org; `2026-06-08`
- Link: https://arxiv.org/abs/2606.11247
- Method tags: foundation or pretrained model, generative / diffusion / inverse design, multimodal or literature-mining model, physics-informed ML
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)
  - foundation or pretrained model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - foundation or pretrained model: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)

### 6. [Older MOF prior art exists] Phase prediction in high-entropy alloys through uncertainty sampling and symbolic classification-based parameter discovery

- Journal/date: npj Computational Materials; `2026-06-11`
- Link: https://doi.org/10.1038/s41524-026-02189-5
- Method tags: active learning / Bayesian optimization, uncertainty / OOD
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - uncertainty / OOD: Are Atoms Enough? An Explainable Graph Neural Network for Carbon Capture and Gas Separation in Metal-Organic Frameworks (ChemRxiv, 2026-06-02)
  - uncertainty / OOD: BaLoRA: Bayesian Low-Rank Adaptation of Large Scale Models (ArXiv.org, 2026-04-27)

### 7. [Older MOF prior art exists] Inverse Design of Novel Antiferromagnets Through Symmetry-aware Generation

- Journal/date: npj Computational Materials; `2026-06-10`
- Link: https://doi.org/10.1038/s41524-026-02169-9
- Method tags: generative / diffusion / inverse design, physics-informed ML
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)

### 8. [Older MOF prior art exists] A Systematic Survey and Benchmark of Deep Learning for Molecular Property Prediction in the Foundation Model Era

- Journal/date: Journal of Chemical Theory and Computation; `2026-05-07`
- Link: https://doi.org/10.1021/acs.jctc.5c02081
- Method tags: foundation or pretrained model, multimodal or literature-mining model, uncertainty / OOD
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)
  - foundation or pretrained model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - foundation or pretrained model: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)

### 9. [Older MOF prior art exists] Escaping the hydrolysis trap: a react agent for inverse design of durable photocatalytic covalent organic frameworks

- Journal/date: npj Computational Materials; `2026-06-03`
- Link: https://doi.org/10.1038/s41524-026-02168-w
- Method tags: active learning / Bayesian optimization, foundation or pretrained model, generative / diffusion / inverse design
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)
  - foundation or pretrained model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - foundation or pretrained model: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)

### 10. [Older MOF prior art exists] Latent Diffusion Pretraining for Crystal Property Prediction

- Journal/date: arXiv (Cornell University); `2026-05-30`
- Link: https://arxiv.org/abs/2606.00776
- Method tags: generative / diffusion / inverse design, graph neural network, self-supervised learning, transfer learning / domain adaptation
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)
  - graph neural network: Are Atoms Enough? An Explainable Graph Neural Network for Carbon Capture and Gas Separation in Metal-Organic Frameworks (ChemRxiv, 2026-06-02)
  - graph neural network: PoroNet: An Intrinsically Interpretable Pore Graph Neural Network for Resolving Pore-Level Adsorption in Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-05-29)

### 11. [Older MOF prior art exists] MatMind: A Structure-Activity Knowledge-Driven Generative Foundation Model for Materials Science

- Journal/date: arXiv (Cornell University); `2026-06-05`
- Link: https://arxiv.org/abs/2606.07712
- Method tags: foundation or pretrained model, graph neural network, physics-informed ML
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)
  - foundation or pretrained model: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - foundation or pretrained model: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)

### 12. [Older MOF prior art exists] AI-Driven Image Processing for Microstructure and Surface Characterization: A Systematic Review of Methods, Materials, and Applications

- Journal/date: Archives of Computational Methods in Engineering; `2026-05-30`
- Link: https://doi.org/10.1007/s11831-026-10641-4
- Method tags: generative / diffusion / inverse design, physics-informed ML, transfer learning / domain adaptation
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)
  - transfer learning / domain adaptation: Harnessing AtomisticSkills for Agentic Atomistic Research (arXiv (Cornell University), 2026-05-18)
  - transfer learning / domain adaptation: Generation of magnetic metal-organic frameworks (ArXiv.org, 2026-04-30)

### 13. [Older MOF prior art exists] Generative modelling of inorganic materials with explicit electronic structure

- Journal/date: Nature Communications; `2026-06-02`
- Link: https://doi.org/10.1038/s41467-026-73985-2
- Method tags: generative / diffusion / inverse design
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)

### 14. [Older MOF prior art exists] An electron-density point-cloud framework for robust protein-ligand interaction prediction

- Journal/date: Nature Communications; `2026-06-11`
- Link: https://doi.org/10.1038/s41467-026-74196-5
- Method tags: graph neural network, uncertainty / OOD
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - graph neural network: Are Atoms Enough? An Explainable Graph Neural Network for Carbon Capture and Gas Separation in Metal-Organic Frameworks (ChemRxiv, 2026-06-02)
  - graph neural network: PoroNet: An Intrinsically Interpretable Pore Graph Neural Network for Resolving Pore-Level Adsorption in Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-05-29)
  - graph neural network: Evaluating mechanical property prediction across material classes using molecular dynamics simulations with universal machine-learned interatomic potentials (Communications Chemistry, 2026-05-06)

### 15. [Older MOF prior art exists] An active learning workflow for predicting misfit volume in body-centered cubic refractory high-entropy alloys

- Journal/date: Scientific Reports; `2026-06-10`
- Link: https://doi.org/10.1038/s41598-026-57006-2
- Method tags: active learning / Bayesian optimization, symbolic regression / descriptor discovery, uncertainty / OOD
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- Long-horizon MOF prior art:
  - uncertainty / OOD: Are Atoms Enough? An Explainable Graph Neural Network for Carbon Capture and Gas Separation in Metal-Organic Frameworks (ChemRxiv, 2026-06-02)
  - uncertainty / OOD: BaLoRA: Bayesian Low-Rank Adaptation of Large Scale Models (ArXiv.org, 2026-04-27)

### 16. [Older MOF prior art exists] Deep learning assisted modeling of Li-ion transport in SEI: a graph neural network based study

- Journal/date: Frontiers in Batteries and Electrochemistry; `2026-06-08`
- Link: https://doi.org/10.3389/fbael.2026.1849012
- Method tags: generative / diffusion / inverse design, graph neural network, physics-informed ML
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)
  - graph neural network: Are Atoms Enough? An Explainable Graph Neural Network for Carbon Capture and Gas Separation in Metal-Organic Frameworks (ChemRxiv, 2026-06-02)
  - graph neural network: PoroNet: An Intrinsically Interpretable Pore Graph Neural Network for Resolving Pore-Level Adsorption in Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-05-29)

### 17. [Older MOF prior art exists] Transferable Machine Learning of Electronic Hamiltonians with Superposition-of-Atomic-Potentials Features

- Journal/date: ArXiv.org; `2026-06-10`
- Link: https://arxiv.org/abs/2606.12326
- Method tags: graph neural network, physics-informed ML
- MOF transfer note: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
- Suggested next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- Long-horizon MOF prior art:
  - graph neural network: Are Atoms Enough? An Explainable Graph Neural Network for Carbon Capture and Gas Separation in Metal-Organic Frameworks (ChemRxiv, 2026-06-02)
  - graph neural network: PoroNet: An Intrinsically Interpretable Pore Graph Neural Network for Resolving Pore-Level Adsorption in Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-05-29)
  - graph neural network: Evaluating mechanical property prediction across material classes using molecular dynamics simulations with universal machine-learned interatomic potentials (Communications Chemistry, 2026-05-06)

### 18. [Older MOF prior art exists] Book of Abstracts: Past, Present and Future of Particle Technology Conference 2026

- Journal/date: White Rose Research Online (University of Leeds, The University of Sheffield, University of York); `2026-06-03`
- Link: https://openalex.org/W7163721383
- Method tags: equivariant ML, graph neural network, physics-informed ML
- MOF transfer note: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
- Suggested next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - equivariant ML: Evaluating mechanical property prediction across material classes using molecular dynamics simulations with universal machine-learned interatomic potentials (Communications Chemistry, 2026-05-06)
  - equivariant ML: Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry (ArXiv.org, 2026-04-28)
  - graph neural network: Are Atoms Enough? An Explainable Graph Neural Network for Carbon Capture and Gas Separation in Metal-Organic Frameworks (ChemRxiv, 2026-06-02)

### 19. [Older MOF prior art exists] Score-based diffusion models for accurate crystal-structure inpainting and reconstruction of hydrogen positions

- Journal/date: npj Computational Materials; `2026-06-11`
- Link: https://doi.org/10.1038/s41524-026-02090-1
- Method tags: generative / diffusion / inverse design
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)

### 20. [Older MOF prior art exists] Data Enrichment for Symbolic Regression Using Diffusion Models

- Journal/date: arXiv (Cornell University); `2026-05-31`
- Link: https://arxiv.org/abs/2606.00988
- Method tags: generative / diffusion / inverse design, physics-informed ML, symbolic regression / descriptor discovery
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Sustainable Metal-Organic Framework Water Harvesters in the Artificial Intelligence Era (ArXiv.org, 2026-05-27)

## Reading Rules

- Fresh means no same method-class tag was found in the recent or long-horizon MOF baselines. It still needs full-paper confirmation.
- Older prior art means the idea is not new to MOFs, but it may still be worth pursuing if the cross-material paper adds a new representation, label space, uncertainty loop, active-learning strategy, or validation regime.
- Recent MOF activity means lower novelty unless the new method opens a clearly different MOF task or implementation path.
