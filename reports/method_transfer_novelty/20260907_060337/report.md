# Method Transfer Novelty Report

- Generated: `2026-09-07T06:03:37`
- Logic: non-MOF transfer scans provide candidate ideas; recent MOF literature checks current adoption; long-horizon MOF prior art checks older adoption.

## Source Runs

- Recent MOF literature: profile `mof_latest_custom`, since `2025-09-07`, papers `1`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/weekly_mof_latest/20260907_060337/report.md`
- Cross-material ML transfer: profile `materials_ml_transfer`, since `2023-09-08`, papers `30`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/materials_ml_transfer/20260907_060345/report.md`
- Reaction/catalyst ML transfer: profile `reaction_catalyst_ml_transfer`, since `2016-09-09`, papers `28`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/reaction_catalyst_ml_transfer/20260907_060404/report.md`
- Long-horizon MOF method prior art: profile `mof_ml_method_prior_art`, since `2016-09-09`, papers `18`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/mof_ml_method_prior_art/20260907_060422/report.md`

## Triage Summary

- Fresh MOF transfer candidates: `7`
- Older MOF prior art exists: `49`
- Already active in recent MOF literature: `0`

## Method-Class Baseline

| Method class | Candidate transfer scans | Recent MOF | Long-horizon MOF prior art |
|---|---:|---:|---:|
| active learning / Bayesian optimization | 16 | 0 | 4 |
| catalyst active-site descriptor | 6 | 0 | 4 |
| equivariant ML | 8 | 0 | 2 |
| foundation or pretrained model | 15 | 0 | 6 |
| generative / diffusion / inverse design | 16 | 0 | 2 |
| graph neural network | 12 | 0 | 0 |
| ML interatomic potential | 15 | 0 | 3 |
| multimodal or literature-mining model | 9 | 0 | 0 |
| physics-informed ML | 8 | 0 | 1 |
| reaction-specific dataset learning | 1 | 0 | 0 |
| self-supervised learning | 5 | 0 | 0 |
| surrogate or multi-fidelity model | 6 | 0 | 1 |
| symbolic regression / descriptor discovery | 2 | 0 | 1 |
| transfer learning / domain adaptation | 6 | 0 | 2 |
| uncertainty / OOD | 11 | 0 | 4 |

## Transfer Opportunities

### 1. [Fresh MOF transfer candidate] Scaling multimodal materials representation learning with synthetic narratives

- Journal/date: Nature Communications; `2026-08-26`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41467-026-76378-7
- Method tags: multimodal or literature-mining model, self-supervised learning
- Transfer distance: adjacent materials
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 2. [Fresh MOF transfer candidate] TAME: Element-wise Mixture-of-Experts Fusion for Data-Efficient and Interpretable Molecular Property Prediction

- Journal/date: ChemRxiv; `2026-09-03`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.26434/chemrxiv.15008270/v1
- Method tags: graph neural network, multimodal or literature-mining model, self-supervised learning
- Transfer distance: adjacent materials
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 3. [Fresh MOF transfer candidate] Decoding Multiscale Degradation of Layered Cathodes in All‐Solid‐State Lithium Batteries: An Advanced Diagnostics‐Driven Framework

- Journal/date: Advanced Energy Materials; `2026-09-02`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1002/aenm.71528
- Method tags: multimodal or literature-mining model
- Transfer distance: adjacent materials
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 4. [Fresh MOF transfer candidate] Materials Behavior as Mechanism Ensembles: A Probabilistic Framework for Emergent Behaviors

- Journal/date: arXiv (Cornell University); `2026-07-29`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://arxiv.org/abs/2607.27163
- Method tags: multimodal or literature-mining model
- Transfer distance: distant method analogy
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 5. [Fresh MOF transfer candidate] Competition-Derived Relative Reactivity and 3D Electronic-State Analysis of Site- and Facial Selectivity in NaBH4/MeOH Ketone Reductions

- Journal/date: ChemRxiv; `2026-09-01`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.26434/chemrxiv.15002906/v3
- Method tags: reaction-specific dataset learning
- Transfer distance: distant method analogy
- Candidate MOF route: Adapt catalyst-generality scoring to MOF catalytic reaction families, biased literature data, and targeted experimental or DFT validation.
- MOF transfer note: Reaction-specific small-data workflow is useful for MOF catalysis if catalyst generality, literature bias, and scaffold validation are made explicit.
- Suggested next step: Rebuild the workflow on MOF catalytic reaction families with explicit scaffold generality, reporting-bias, and validation splits. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 6. [Fresh MOF transfer candidate] Work Function and High-Coverage Adsorption Energy as Hydrogen-Evolution Descriptors on Ag-Au-Pd-Pt Alloys

- Journal/date: arXiv (Cornell University); `2026-08-28`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://arxiv.org/abs/2608.28347
- Method tags: graph neural network
- Transfer distance: adjacent materials
- Candidate MOF route: Benchmark the representation on periodic MOF graphs with explicit node/linker chemistry and pore topology.
- MOF transfer note: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
- Suggested next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 7. [Fresh MOF transfer candidate] Expert-Informed Contrastive Learning of Condition Space for Amide Coupling Reactions

- Journal/date: ChemRxiv; `2026-03-18`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.26434/chemrxiv.15001054/v1
- Method tags: self-supervised learning
- Transfer distance: distant method analogy
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 8. [Older MOF prior art exists] From bio-inspired concepts to intelligent design: evolution and development trends of bio-inspired mechanical structural design methods

- Journal/date: Advanced bionics.; `2026-09-01`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1016/j.abs.2026.08.008
- Method tags: active learning / Bayesian optimization, generative / diffusion / inverse design, graph neural network, surrogate or multi-fidelity model
- Transfer distance: distant method analogy
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion (Materials Today Sustainability, 2026-09-03)
  - active learning / Bayesian optimization: Computational and ML methods in MOF based supercapacitors - from mechanistic understanding to future materials design (Journal of Materials Science Materials Theory, 2026-08-29)
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)

### 9. [Older MOF prior art exists] uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks

- Journal/date: arXiv (Cornell University); `2026-08-28`
- Candidate source: Cross-material ML transfer
- Link: https://arxiv.org/abs/2608.28100
- Method tags: equivariant ML, foundation or pretrained model, ML interatomic potential, uncertainty / OOD
- Transfer distance: direct MOF
- Candidate MOF route: Use as direct MOF prior art or a benchmark for a more specific MOF task.
- MOF transfer note: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - equivariant ML: uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks (arXiv (Cornell University), 2026-08-28)
  - equivariant ML: Generalized Machine Learning Potentials for Predicting Low-Pressure Water Adsorption in Flexible Al-Based Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-08-25)
  - foundation or pretrained model: An LLM agent for end-to-end computational materials discovery (arXiv (Cornell University), 2026-08-20)

### 10. [Older MOF prior art exists] Mechanism-informed machine learning for intelligent design of rare-earth-containing magnesium-based alloys

- Journal/date: Journal of Magnesium and Alloys; `2026-09-02`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1016/j.jma.2026.102273
- Method tags: active learning / Bayesian optimization, generative / diffusion / inverse design, physics-informed ML, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion (Materials Today Sustainability, 2026-09-03)
  - active learning / Bayesian optimization: Computational and ML methods in MOF based supercapacitors - from mechanistic understanding to future materials design (Journal of Materials Science Materials Theory, 2026-08-29)
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)

### 11. [Older MOF prior art exists] Carbon Nanotube-Induced Magnetic Shielding Effects on 129Xe NMR from Equivariant Neural Networks

- Journal/date: ChemRxiv; `2026-08-27`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.26434/chemrxiv.15007956/v1
- Method tags: equivariant ML, foundation or pretrained model, graph neural network, ML interatomic potential
- Transfer distance: distant method analogy
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - equivariant ML: uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks (arXiv (Cornell University), 2026-08-28)
  - equivariant ML: Generalized Machine Learning Potentials for Predicting Low-Pressure Water Adsorption in Flexible Al-Based Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-08-25)
  - foundation or pretrained model: An LLM agent for end-to-end computational materials discovery (arXiv (Cornell University), 2026-08-20)

### 12. [Older MOF prior art exists] Improving Reliability of Machine Learning Interatomic Potentials with Physics-Informed Pretraining

- Journal/date: Journal of Chemical Information and Modeling; `2026-08-28`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1021/acs.jcim.6c00826
- Method tags: foundation or pretrained model, graph neural network, ML interatomic potential, physics-informed ML, self-supervised learning, transfer learning / domain adaptation
- Transfer distance: distant method analogy
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - foundation or pretrained model: uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks (arXiv (Cornell University), 2026-08-28)
  - foundation or pretrained model: Generalized Machine Learning Potentials for Predicting Low-Pressure Water Adsorption in Flexible Al-Based Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-08-25)
  - foundation or pretrained model: An LLM agent for end-to-end computational materials discovery (arXiv (Cornell University), 2026-08-20)

### 13. [Older MOF prior art exists] Computational and ML methods in MOF based supercapacitors - from mechanistic understanding to future materials design

- Journal/date: Journal of Materials Science Materials Theory; `2026-08-29`
- Candidate source: Cross-material ML transfer; Reaction/catalyst ML transfer
- Link: https://doi.org/10.1186/s41313-026-00087-3
- Method tags: active learning / Bayesian optimization, catalyst active-site descriptor, physics-informed ML, surrogate or multi-fidelity model
- Transfer distance: direct MOF
- Candidate MOF route: Use as direct MOF prior art or a benchmark for a more specific MOF task.
- MOF transfer note: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.
- Suggested next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion (Materials Today Sustainability, 2026-09-03)
  - active learning / Bayesian optimization: Computational and ML methods in MOF based supercapacitors - from mechanistic understanding to future materials design (Journal of Materials Science Materials Theory, 2026-08-29)
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)

### 14. [Older MOF prior art exists] Inverse design of functional materials: a case study in thermoelectrics

- Journal/date: npj Computational Materials; `2026-08-31`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41524-026-02307-3
- Method tags: foundation or pretrained model, generative / diffusion / inverse design, graph neural network
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - foundation or pretrained model: uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks (arXiv (Cornell University), 2026-08-28)
  - foundation or pretrained model: Generalized Machine Learning Potentials for Predicting Low-Pressure Water Adsorption in Flexible Al-Based Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-08-25)
  - foundation or pretrained model: An LLM agent for end-to-end computational materials discovery (arXiv (Cornell University), 2026-08-20)

### 15. [Older MOF prior art exists] CrystalGRW: generative modeling of crystal structures with targeted crystallographic properties via geodesic random walks

- Journal/date: Scientific Reports; `2026-08-31`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41598-026-62470-x
- Method tags: equivariant ML, generative / diffusion / inverse design, graph neural network
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - equivariant ML: uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks (arXiv (Cornell University), 2026-08-28)
  - equivariant ML: Generalized Machine Learning Potentials for Predicting Low-Pressure Water Adsorption in Flexible Al-Based Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-08-25)
  - generative / diffusion / inverse design: Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion (Materials Today Sustainability, 2026-09-03)

### 16. [Older MOF prior art exists] MolCryst-MLIPs: A Machine-Learned Interatomic Potentials Database for Molecular Crystals

- Journal/date: Journal of Chemical Theory and Computation; `2026-08-27`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1021/acs.jctc.6c00735
- Method tags: equivariant ML, foundation or pretrained model, ML interatomic potential
- Transfer distance: adjacent materials
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - equivariant ML: uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks (arXiv (Cornell University), 2026-08-28)
  - equivariant ML: Generalized Machine Learning Potentials for Predicting Low-Pressure Water Adsorption in Flexible Al-Based Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-08-25)
  - foundation or pretrained model: An LLM agent for end-to-end computational materials discovery (arXiv (Cornell University), 2026-08-20)

### 17. [Older MOF prior art exists] PhononBench:A Large-Scale Phonon-Based Benchmark for Dynamical Stability in Crystal Generation

- Journal/date: AI for Science; `2026-08-26`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1088/3050-287x/ae9ee4
- Method tags: foundation or pretrained model, generative / diffusion / inverse design, graph neural network, ML interatomic potential
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response.
- Long-horizon MOF prior art:
  - foundation or pretrained model: uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks (arXiv (Cornell University), 2026-08-28)
  - foundation or pretrained model: Generalized Machine Learning Potentials for Predicting Low-Pressure Water Adsorption in Flexible Al-Based Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-08-25)
  - foundation or pretrained model: An LLM agent for end-to-end computational materials discovery (arXiv (Cornell University), 2026-08-20)

### 18. [Older MOF prior art exists] SHAP-guided Machine Learning for Interpretable Band Gap Prediction and Inverse Design in ABX₃ Perovskites

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

### 19. [Older MOF prior art exists] Accelerating Catalyst Materials Discovery With Large Artificial Intelligence Models

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

### 20. [Older MOF prior art exists] Machine learning for predicting the glass transition and melting temperatures of polymers: molecular representations, model architectures, and interpretability

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

## Reading Rules

- Fresh means no same method-class tag was found in the recent or long-horizon MOF baselines. It still needs full-paper confirmation.
- Distant cross-domain methods are allowed when the method can be mapped to a concrete MOF object, such as structure images, spectra, isotherms, pore maps, generated CIF checks, or multimodal literature-structure consistency.
- Older prior art means the idea is not new to MOFs, but it may still be worth pursuing if the cross-material paper adds a new representation, label space, uncertainty loop, active-learning strategy, or validation regime.
- Recent MOF activity means lower novelty unless the new method opens a clearly different MOF task or implementation path.
