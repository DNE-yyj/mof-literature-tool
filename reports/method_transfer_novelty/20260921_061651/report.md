# Method Transfer Novelty Report

- Generated: `2026-09-21T06:16:51`
- Logic: non-MOF transfer scans provide candidate ideas; recent MOF literature checks current adoption; long-horizon MOF prior art checks older adoption.

## Source Runs

- Recent MOF literature: profile `mof_latest_custom`, since `2025-09-21`, papers `3`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/weekly_mof_latest/20260921_061651/report.md`
- Cross-material ML transfer: profile `materials_ml_transfer`, since `2023-09-22`, papers `30`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/materials_ml_transfer/20260921_061657/report.md`
- Reaction/catalyst ML transfer: profile `reaction_catalyst_ml_transfer`, since `2016-09-23`, papers `25`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/reaction_catalyst_ml_transfer/20260921_061714/report.md`
- Long-horizon MOF method prior art: profile `mof_ml_method_prior_art`, since `2016-09-23`, papers `15`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/mof_ml_method_prior_art/20260921_061727/report.md`

## Triage Summary

- Fresh MOF transfer candidates: `2`
- Older MOF prior art exists: `39`
- Already active in recent MOF literature: `13`

## Method-Class Baseline

| Method class | Candidate transfer scans | Recent MOF | Long-horizon MOF prior art |
|---|---:|---:|---:|
| active learning / Bayesian optimization | 13 | 0 | 4 |
| catalyst active-site descriptor | 4 | 0 | 6 |
| equivariant ML | 6 | 0 | 2 |
| foundation or pretrained model | 9 | 0 | 4 |
| generative / diffusion / inverse design | 15 | 0 | 2 |
| graph neural network | 3 | 0 | 0 |
| ML interatomic potential | 13 | 1 | 2 |
| multimodal or literature-mining model | 6 | 0 | 0 |
| physics-informed ML | 7 | 0 | 2 |
| surrogate or multi-fidelity model | 5 | 0 | 1 |
| symbolic regression / descriptor discovery | 6 | 0 | 2 |
| transfer learning / domain adaptation | 5 | 0 | 2 |
| uncertainty / OOD | 17 | 0 | 2 |

## Transfer Opportunities

### 1. [Fresh MOF transfer candidate] Multiplexed embryo profiling links cellular state to zygotic genome activation in single cells

- Journal/date: Nature Communications; `2026-09-17`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41467-026-77784-7
- Method tags: multimodal or literature-mining model
- Transfer distance: distant cross-domain method
- Candidate MOF route: Translate visual-artifact or metadata-consistency logic to MOF structure images/renders, spectra, isotherm curves, generated CIF validation, or multimodal paper-structure consistency checks.
- MOF transfer note: Distant-domain method can be useful if it maps to a concrete MOF object such as structure images, spectra, isotherms, pore maps, or multimodal consistency checks.
- Suggested next step: Map the method onto MOF structure images, spectra, isotherm curves, or generated-structure consistency checks.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 2. [Fresh MOF transfer candidate] A multimodal semantic learning framework for data-driven discovery of nitrate-to-ammonia electrocatalysts

- Journal/date: npj Computational Materials; `2026-09-15`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1038/s41524-026-02327-z
- Method tags: multimodal or literature-mining model
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 3. [Older MOF prior art exists] Machine learning approaches for electrocatalyst design in water splitting: a review for green hydrogen production

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
  - active learning / Bayesian optimization: Computational and ML methods in MOF based supercapacitors - from mechanistic understanding to future materials design (Journal of Materials Science Materials Theory, 2026-08-29)
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)

### 4. [Older MOF prior art exists] Physics-guided diffusion models for inverse design of disordered metamaterials

- Journal/date: npj Computational Materials; `2026-09-17`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41524-026-02328-y
- Method tags: generative / diffusion / inverse design, physics-informed ML
- Transfer distance: distant method analogy
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion (Materials Today Sustainability, 2026-09-03)
  - generative / diffusion / inverse design: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - physics-informed ML: PORMAKE2: Topology-Based Generation of Hypothetical Metal-Organic Frameworks through Single-Metal Nodes and Symmetry-Aware Linker Rotation (ChemRxiv, 2026-09-09)

### 5. [Older MOF prior art exists] Physics-informed automated surface reconstruction via low-energy electron diffraction based on Bayesian optimization

- Journal/date: npj Computational Materials; `2026-09-09`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41524-026-02297-2
- Method tags: active learning / Bayesian optimization, physics-informed ML
- Transfer distance: adjacent materials
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion (Materials Today Sustainability, 2026-09-03)
  - active learning / Bayesian optimization: Computational and ML methods in MOF based supercapacitors - from mechanistic understanding to future materials design (Journal of Materials Science Materials Theory, 2026-08-29)
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)

### 6. [Older MOF prior art exists] Machine learning-accelerated inverse design of energy materials: A critical review of graph neural networks, physics-informed models, and generative AI for batteries, perovskite solar cells, and electrocatalysts

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
  - active learning / Bayesian optimization: Computational and ML methods in MOF based supercapacitors - from mechanistic understanding to future materials design (Journal of Materials Science Materials Theory, 2026-08-29)
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)

### 7. [Older MOF prior art exists] Machine Learning for Structural Steels: Materials Design, Property Prediction, Durability, and Future Directions

- Journal/date: Materials; `2026-08-25`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.3390/ma19173612
- Method tags: active learning / Bayesian optimization, multimodal or literature-mining model, physics-informed ML, uncertainty / OOD
- Transfer distance: distant method analogy
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion (Materials Today Sustainability, 2026-09-03)
  - active learning / Bayesian optimization: Computational and ML methods in MOF based supercapacitors - from mechanistic understanding to future materials design (Journal of Materials Science Materials Theory, 2026-08-29)
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)

### 8. [Older MOF prior art exists] DFT-based machine-learning for the rational design of magnetocaloric high-entropy alloys

- Journal/date: Nature Communications; `2026-08-25`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41467-026-77123-w
- Method tags: catalyst active-site descriptor, physics-informed ML
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt active-site model-selection and descriptor mining to MOF metal nodes, defects, bimetallic sites, or local-field catalytic motifs.
- MOF transfer note: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.
- Suggested next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - catalyst active-site descriptor: Recent advances in the strategies of developing water-resistant catalysts for the removal of atmospheric pollutants (Greenverse Science, 2026-09-11)
  - catalyst active-site descriptor: Carboxylate-Ligand-Based Coordination Polymers and Metal Complexes: From Structural Diversity and Supramolecular Descriptors to Function-Oriented Design (Molecules, 2026-08-31)
  - catalyst active-site descriptor: Computational and ML methods in MOF based supercapacitors - from mechanistic understanding to future materials design (Journal of Materials Science Materials Theory, 2026-08-29)

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

### 10. [Older MOF prior art exists] Deep learning in materials electron microscopy: models, applications and emerging trends

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
  - foundation or pretrained model: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)

### 11. [Older MOF prior art exists] Large language model-enabled automated data extraction for concrete materials informatics

- Journal/date: npj Computational Materials; `2026-09-14`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41524-026-02304-6
- Method tags: foundation or pretrained model, uncertainty / OOD
- Transfer distance: distant method analogy
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - foundation or pretrained model: uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks (arXiv (Cornell University), 2026-08-28)
  - foundation or pretrained model: Generalized Machine Learning Potentials for Predicting Low-Pressure Water Adsorption in Flexible Al-Based Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-08-25)
  - foundation or pretrained model: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)

### 12. [Older MOF prior art exists] AI-accelerated discovery of altermagnetic metal-organic frameworks via interpretable machine learning

- Journal/date: npj Computational Materials; `2026-09-14`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41524-026-02323-3
- Method tags: symbolic regression / descriptor discovery
- Transfer distance: direct MOF
- Candidate MOF route: Use as direct MOF prior art or a benchmark for a more specific MOF task.
- MOF transfer note: Already in the MOF literature; keep it only if the method adds a new representation, label space, or uncertainty/active-learning angle.
- Suggested next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - symbolic regression / descriptor discovery: AI-accelerated discovery of altermagnetic metal-organic frameworks via interpretable machine learning (npj Computational Materials, 2026-09-14)
  - symbolic regression / descriptor discovery: Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks via Machine Learning-Symbolic Regression (arXiv (Cornell University), 2026-08-15)

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

### 14. [Older MOF prior art exists] Defect engineering of semiconductor photocatalysts for solar energy conversion: from atomic-level design to AI-driven materials discovery for sustainable development and clean energy

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

### 15. [Older MOF prior art exists] Explicit modelling of lift characteristics for high-lift devices based on knowledge-guided symbolic regression using large language model

- Journal/date: Engineering Applications of Computational Fluid Mechanics; `2026-09-11`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1080/19942060.2026.2728948
- Method tags: foundation or pretrained model, multimodal or literature-mining model, surrogate or multi-fidelity model, symbolic regression / descriptor discovery
- Transfer distance: distant method analogy
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - foundation or pretrained model: uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks (arXiv (Cornell University), 2026-08-28)
  - foundation or pretrained model: Generalized Machine Learning Potentials for Predicting Low-Pressure Water Adsorption in Flexible Al-Based Metal–Organic Frameworks (Journal of Chemical Theory and Computation, 2026-08-25)
  - foundation or pretrained model: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)

### 16. [Older MOF prior art exists] Artificial Intelligence in Materials Discovery: A Comprehensive Review of Methods, Applications, and Future Directions

- Journal/date: WORLD JOURNAL OF INNOVATION AND MODERN TECHNOLOGY; `2026-09-15`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.56201/wjimt.v10.no3.2026.pg9.25
- Method tags: generative / diffusion / inverse design
- Transfer distance: distant method analogy
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion (Materials Today Sustainability, 2026-09-03)
  - generative / diffusion / inverse design: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)

### 17. [Older MOF prior art exists] High-Entropy Catalysts for Lithium-Sulfur and Room-Temperature Sodium-Sulfur Batteries: Electronic Descriptors, Performance, and Design Challenges

- Journal/date: ChemRxiv; `2026-09-14`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.26434/chemrxiv.15008811/v1
- Method tags: catalyst active-site descriptor
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt active-site model-selection and descriptor mining to MOF metal nodes, defects, bimetallic sites, or local-field catalytic motifs.
- MOF transfer note: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.
- Suggested next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- Long-horizon MOF prior art:
  - catalyst active-site descriptor: Recent advances in the strategies of developing water-resistant catalysts for the removal of atmospheric pollutants (Greenverse Science, 2026-09-11)
  - catalyst active-site descriptor: Carboxylate-Ligand-Based Coordination Polymers and Metal Complexes: From Structural Diversity and Supramolecular Descriptors to Function-Oriented Design (Molecules, 2026-08-31)
  - catalyst active-site descriptor: Computational and ML methods in MOF based supercapacitors - from mechanistic understanding to future materials design (Journal of Materials Science Materials Theory, 2026-08-29)

### 18. [Older MOF prior art exists] Kinetic Isotope Effects in CO 2 Reduction: Insights Into Reaction Mechanisms

- Journal/date: Advanced Energy Materials; `2026-09-14`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1002/aenm.71591
- Method tags: uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- Long-horizon MOF prior art:
  - uncertainty / OOD: Machine learning approach for MOF-based photocatalytic CO2 reduction to fuels (Energy Conversion and Management X, 2026-09-01)
  - uncertainty / OOD: uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks (arXiv (Cornell University), 2026-08-28)

### 19. [Older MOF prior art exists] Neural-Network Solutions to Real-Space Charge Density and Generalization

- Journal/date: arXiv (Cornell University); `2026-09-14`
- Candidate source: Cross-material ML transfer
- Link: https://arxiv.org/abs/2609.14906
- Method tags: uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - uncertainty / OOD: Machine learning approach for MOF-based photocatalytic CO2 reduction to fuels (Energy Conversion and Management X, 2026-09-01)
  - uncertainty / OOD: uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks (arXiv (Cornell University), 2026-08-28)

### 20. [Older MOF prior art exists] Navigating Sparse Singlet Fission Chemical Space: An Intelligent Generative-Predictive Paradigm

- Journal/date: arXiv (Cornell University); `2026-09-12`
- Candidate source: Cross-material ML transfer
- Link: https://arxiv.org/abs/2609.15136
- Method tags: generative / diffusion / inverse design
- Transfer distance: distant method analogy
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - generative / diffusion / inverse design: Mesoporous single-atom and nano-confined catalysts: Enabling low-energy integrated CO2 capture and direct conversion (Materials Today Sustainability, 2026-09-03)
  - generative / diffusion / inverse design: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)

## Reading Rules

- Fresh means no same method-class tag was found in the recent or long-horizon MOF baselines. It still needs full-paper confirmation.
- Distant cross-domain methods are allowed when the method can be mapped to a concrete MOF object, such as structure images, spectra, isotherms, pore maps, generated CIF checks, or multimodal literature-structure consistency.
- Older prior art means the idea is not new to MOFs, but it may still be worth pursuing if the cross-material paper adds a new representation, label space, uncertainty loop, active-learning strategy, or validation regime.
- Recent MOF activity means lower novelty unless the new method opens a clearly different MOF task or implementation path.
