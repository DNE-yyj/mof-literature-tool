# Method Transfer Novelty Report

- Generated: `2026-10-26T06:07:20`
- Logic: non-MOF transfer scans provide candidate ideas; recent MOF literature checks current adoption; long-horizon MOF prior art checks older adoption.

## Source Runs

- Recent MOF literature: profile `mof_latest_custom`, since `2025-10-26`, papers `3`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/weekly_mof_latest/20261026_060720/report.md`
- Cross-material ML transfer: profile `materials_ml_transfer`, since `2023-10-27`, papers `30`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/materials_ml_transfer/20261026_060724/report.md`
- Reaction/catalyst ML transfer: profile `reaction_catalyst_ml_transfer`, since `2016-10-28`, papers `27`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/reaction_catalyst_ml_transfer/20261026_060739/report.md`
- Long-horizon MOF method prior art: profile `mof_ml_method_prior_art`, since `2016-10-28`, papers `8`
  - Report: `/home/runner/work/mof-literature-tool/mof-literature-tool/reports/mof_ml_method_prior_art/20261026_060748/report.md`

## Triage Summary

- Fresh MOF transfer candidates: `8`
- Older MOF prior art exists: `31`
- Already active in recent MOF literature: `16`

## Method-Class Baseline

| Method class | Candidate transfer scans | Recent MOF | Long-horizon MOF prior art |
|---|---:|---:|---:|
| active learning / Bayesian optimization | 17 | 0 | 2 |
| catalyst active-site descriptor | 6 | 0 | 2 |
| equivariant ML | 10 | 0 | 0 |
| foundation or pretrained model | 12 | 0 | 1 |
| generative / diffusion / inverse design | 8 | 0 | 1 |
| graph neural network | 6 | 0 | 0 |
| ML interatomic potential | 16 | 1 | 1 |
| multimodal or literature-mining model | 5 | 0 | 0 |
| physics-informed ML | 12 | 0 | 0 |
| self-supervised learning | 1 | 0 | 0 |
| surrogate or multi-fidelity model | 4 | 0 | 0 |
| symbolic regression / descriptor discovery | 3 | 0 | 1 |
| transfer learning / domain adaptation | 7 | 0 | 1 |
| uncertainty / OOD | 12 | 0 | 1 |

## Transfer Opportunities

### 1. [Fresh MOF transfer candidate] Bridging model attention to physical insights in structure-property dynamics

- Journal/date: Science and Technology of Advanced Materials Methods; `2026-10-15`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1080/27660400.2026.2738286
- Method tags: physics-informed ML
- Transfer distance: distant method analogy
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Test humid or multicomponent conditions and connect material metrics to process-level targets. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 2. [Fresh MOF transfer candidate] A quantum-informed gradient catalyst layer architecture for freeze-resistant proton exchange membrane fuel cell cold startup via DFT guided machine learning

- Journal/date: Scientific Reports; `2026-10-16`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1038/s41598-026-73810-2
- Method tags: physics-informed ML, surrogate or multi-fidelity model
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Add kinetics, explicit environment effects, and active-site reconstruction checks. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 3. [Fresh MOF transfer candidate] SU(2)-Equivariant Spinor Message Passing for Molecular Magnetism

- Journal/date: arXiv (Cornell University); `2026-10-21`
- Candidate source: Cross-material ML transfer
- Link: https://arxiv.org/abs/2610.29111
- Method tags: equivariant ML, graph neural network
- Transfer distance: adjacent materials
- Candidate MOF route: Benchmark the representation on periodic MOF graphs with explicit node/linker chemistry and pore topology.
- MOF transfer note: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
- Suggested next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 4. [Fresh MOF transfer candidate] Designing rigid protein fiducials to visualize GPCR conformational states

- Journal/date: Nature Communications; `2026-10-24`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41467-026-78942-7
- Method tags: equivariant ML
- Transfer distance: distant method analogy
- Candidate MOF route: Benchmark the representation on periodic MOF graphs with explicit node/linker chemistry and pore topology.
- MOF transfer note: Representation-learning advance may transfer to MOFs after adding porous-crystal topology and metal-node chemistry.
- Suggested next step: Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 5. [Fresh MOF transfer candidate] Predicting protein electrostatics with protein language models

- Journal/date: Nature Communications; `2026-10-24`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41467-026-78406-y
- Method tags: physics-informed ML
- Transfer distance: distant method analogy
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 6. [Fresh MOF transfer candidate] Physics-aware neural networks enable robust and full atomic structure determination via low-dose atomic electron tomography

- Journal/date: npj Computational Materials; `2026-10-23`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41524-026-02363-9
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

### 8. [Fresh MOF transfer candidate] Ioc-Mldroid: a Hybrid Approach for Detection of Android Based Malicious Applications Using Indicators of Compromise (Iocs) and Machine Learning

- Journal/date: i-manager's Journal on Computer Science; `2027-06-15`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.26634/jcom.14.1.1372
- Method tags: surrogate or multi-fidelity model
- Transfer distance: distant method analogy
- Candidate MOF route: Keep only if the full paper exposes a reusable representation, validation loop, or data-efficiency strategy for a concrete MOF task.
- MOF transfer note: Potentially useful as a neighboring-method reference.
- Suggested next step: Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- MOF baseline evidence: no same method-class match found in the two MOF scans.

### 9. [Older MOF prior art exists] Less can be more for predicting properties with large language models

- Journal/date: Nature Computational Science; `2026-10-12`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s43588-026-01045-2
- Method tags: foundation or pretrained model, graph neural network
- Transfer distance: adjacent materials
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - foundation or pretrained model: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)

### 10. [Older MOF prior art exists] Machine learning-driven inverse design of high-hardness multi-principal element alloys through symbolic regression

- Journal/date: Scientific Reports; `2026-10-23`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41598-026-74491-7
- Method tags: active learning / Bayesian optimization, generative / diffusion / inverse design, physics-informed ML, surrogate or multi-fidelity model, symbolic regression / descriptor discovery
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - symbolic regression / descriptor discovery: Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks via Machine Learning-Symbolic Regression (arXiv (Cornell University), 2026-08-15)

### 11. [Older MOF prior art exists] Autonomous Laboratories and Foundry Scientific Discovery at the Limit A machine does not discover a mechanism until it creates evidence that could defeat it Core coupling Autonomous experiment x active learning x scientific falsification Research scale 30 linked derivations x 82 chapters x 410 research sections x 200 detailed Research Gates Main result A falsifiable framework for generating, attacking and eliminating process mechanisms rather than confusing recipe optimization with scientific discovery. Series lineage Semiconductor Foundry Technologies x Intelligent Nanomanufacturing - Flagship 20 Publication Abstract This monograph asks whether an autonomous foundry laboratory can do more than optimize an existing recipe. It develops a research architecture in which the system must register competing process mechanisms, identify what its sensors can and cannot distinguish, choose experiments for model discrimination, preserve negative evidence, and issue counterfactual predictions that survive a new tool or fab. Yield improvement, simulation fit, and automation speed are treated as useful engineering outcomes but not as proof of a new mechanism. The central falsifiable proposition is that active experiments chosen to separate rival predictions should reduce the set of observationally equivalent mechanisms and improve preregistered counterfactual forecasts under the same sample, metrology, time, energy, and safety budget as expert DOE and strong safe Bayesian optimization. If the experiment cannot distinguish the models, if failures are selectively forgotten, if the acquisition function exploits a biased proxy, or if cross-tool predictions fail, the scientific claim is narrowed, split, or stopped. Scientific Position and Hard Boundary The work begins with bounded thin-film, deposition, etch, interface, and defect-mechanism challenges in simulation, digital-physical twins, test vehicles, and low-risk equipment states. Autonomous execution is permitted only through typed process intent, equipment capability contracts, explicit authorization, independent metrology, abort logic, and recoverable physical states. No information-gain score may override safety, material irreversibility, chain of custody, environmental obligations, worker protection, or equipment interlocks. Candidate Research Expression Dsci = Delta H of competing models + counterfactual information - sample cost - unsafe risk - hype penalty • Delta H measures reduction in uncertainty over the preregistered mechanism set. • Counterfactual information rewards predictions about interventions or new platforms that were not used for fitting. • Sample cost includes material, metrology, time, energy, and opportunity cost. • Unsafe risk is a hard feasibility concern, not a term that can be purchased by predicted knowledge. • The hype penalty prevents an engineering improvement from being narrated as a causal discovery. Five Layer Research Architecture 01 Competing Mechanism Contract Register rival mechanisms, observable signatures, claim levels, strong baselines, and hard boundaries. 02 Observability and Evidence Graph Map sensors, latent state, calibration ancestry, identifiability, and equivalent model sets. 03 Discriminating Active Experiment Choose controls, interventions, and fidelities for information under sample, energy, and risk budgets. 04 Refutation Memory and Safe Execution Compile typed experiments, preserve failures, detect misspecification, abort safely, and record why models were rejected. 05 Independent Transfer and Successor Choice Demand cross-tool counterfactual predictions, third-party replay, and the right to split, downgrade, or retire a mechanism. Minimum Verifiable Prototype Two process mechanisms are constructed to explain the same historical thin-film or etch observations. Expert DOE, safe Bayesian optimization, and the autonomous discovery policy receive matched samples, metrology, wall time, energy, and safety envelopes. Before the hidden outcomes are revealed, each freezes its hypotheses, predicted signatures, next experiment, acquisition value, uncertainty, and stopping rule. The decisive test is whether independent terminal metrology and a new intervention eliminate or sharply narrow one mechanism, not whether the system merely finds a better recipe. Research Contributions • Separates optimization, prediction, mechanism discrimination, causal support, and cross-platform scientific claims. • Connects observability, identifiability, Fisher information, Bayesian experimental design, causal intervention, and model criticism. • Treats negative results, failed experiments, calibration ancestry, manual corrections, and eliminated models as first-class scientific records. • Maps thirty distinct derivations to chapter, experiment, and Research Gate corridors. • Provides eighty-two chapters with five research pages per chapter: boundary, identifiability, minimum test, adversarial refutation, and successor route.

- Journal/date: Zenodo (CERN European Organization for Nuclear Research); `2026-10-18`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.5281/zenodo.23452112
- Method tags: active learning / Bayesian optimization, physics-informed ML, uncertainty / OOD
- Transfer distance: distant method analogy
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Benchmark uncertainty and out-of-domain behavior before broad screening claims.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - uncertainty / OOD: Predictive Synthesis of MOFs and COFs (arXiv (Cornell University), 2026-10-08)

### 12. [Older MOF prior art exists] From Atoms to Reactors: A Critical Review of a Decade of Machine Learning in Heterogeneous Catalysis (2017–2026)

- Journal/date: Angewandte Chemie International Edition; `2026-10-23`
- Candidate source: Cross-material ML transfer; Reaction/catalyst ML transfer
- Link: https://doi.org/10.1002/anie.4288841
- Method tags: active learning / Bayesian optimization, foundation or pretrained model
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)

### 13. [Older MOF prior art exists] Machine learning approaches for electrocatalyst design in water splitting: a review for green hydrogen production

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
  - catalyst active-site descriptor: Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks via Machine Learning-Symbolic Regression (arXiv (Cornell University), 2026-08-15)

### 14. [Older MOF prior art exists] Spatial Statistics for Screening Molecular Structures

- Journal/date: Small; `2026-10-15`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1002/smll.76291
- Method tags: active learning / Bayesian optimization, equivariant ML, generative / diffusion / inverse design
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt the generator to MOF topology, linker-node compatibility, charge balance, and synthesizability constraints.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)

### 15. [Older MOF prior art exists] Inverse materials design via joint generation of crystal structures and local electronic descriptors

- Journal/date: npj Computational Materials; `2026-10-15`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1038/s41524-026-02322-4
- Method tags: catalyst active-site descriptor, generative / diffusion / inverse design
- Transfer distance: adjacent materials
- Candidate MOF route: Adapt active-site model-selection and descriptor mining to MOF metal nodes, defects, bimetallic sites, or local-field catalytic motifs.
- MOF transfer note: Active-site descriptor or model-selection idea can transfer to MOF catalysis through metal-node, defect, bimetallic, or local-field descriptors.
- Suggested next step: Test whether active-site descriptors transfer to MOF nodes, defects, bimetallic sites, or local-field-controlled catalytic regimes. Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints.
- Long-horizon MOF prior art:
  - catalyst active-site descriptor: Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks via Machine Learning-Symbolic Regression (arXiv (Cornell University), 2026-08-15)
  - catalyst active-site descriptor: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - generative / diffusion / inverse design: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)

### 16. [Older MOF prior art exists] Advanced engineering of inorganic semiconductor nanowires: Materials-by-design for next-generation green energy technologies

- Journal/date: Energy Reviews; `2026-10-05`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1016/j.enrev.2026.100216
- Method tags: active learning / Bayesian optimization, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - uncertainty / OOD: Predictive Synthesis of MOFs and COFs (arXiv (Cornell University), 2026-10-08)

### 17. [Older MOF prior art exists] Machine learning-accelerated inverse design of energy materials: A critical review of graph neural networks, physics-informed models, and generative AI for batteries, perovskite solar cells, and electrocatalysts

- Journal/date: Next Materials; `2026-07-30`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1016/j.nxmate.2026.102969
- Method tags: active learning / Bayesian optimization, generative / diffusion / inverse design, graph neural network, physics-informed ML, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Generative or inverse-design idea may transfer to MOFs if topology, charge, and synthesizability constraints are made explicit.
- Suggested next step: Recast the generator with MOF topology, linker-node compatibility, charge, and synthetic-accessibility constraints. Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - uncertainty / OOD: Predictive Synthesis of MOFs and COFs (arXiv (Cornell University), 2026-10-08)

### 18. [Older MOF prior art exists] Quantum machine learning: A comprehensive survey of models, tools, and challenges

- Journal/date: Journal of King Saud University - Computer and Information Sciences; `2026-10-19`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1007/s44443-026-01177-5
- Method tags: graph neural network, transfer learning / domain adaptation
- Transfer distance: distant method analogy
- Candidate MOF route: Fine-tune or adapt the representation on sparse MOF labels such as flexibility, defects, guest response, or adsorption regimes.
- MOF transfer note: Pretraining or transfer-learning route is promising for MOF tasks with sparse labels or many related properties.
- Suggested next step: Fine-tune on MOF datasets and test whether transfer helps scarce labels such as flexibility, defects, or guest response. Benchmark node/linker-aware periodic graphs against generic crystal representations on MOF properties.
- Long-horizon MOF prior art:
  - transfer learning / domain adaptation: Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks via Machine Learning-Symbolic Regression (arXiv (Cornell University), 2026-08-15)

### 19. [Older MOF prior art exists] Artificial Intelligence–Driven Molecular Imprinting for Efficient Polymer Design and Enhanced Liquid‐Phase Separation

- Journal/date: Electrophoresis; `2026-10-22`
- Candidate source: Cross-material ML transfer
- Link: https://doi.org/10.1002/elps.70173
- Method tags: active learning / Bayesian optimization
- Transfer distance: adjacent materials
- Candidate MOF route: Use uncertainty or acquisition logic to choose which MOF DFT, MD, or GCMC labels to compute next.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Test humid or multicomponent conditions and connect material metrics to process-level targets.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)

### 20. [Older MOF prior art exists] Closing the learning loop in lithium–sulfur batteries through physics-informed and trustworthy artificial intelligence

- Journal/date: Energy and AI; `2026-10-05`
- Candidate source: Reaction/catalyst ML transfer
- Link: https://doi.org/10.1016/j.egyai.2026.100934
- Method tags: active learning / Bayesian optimization, multimodal or literature-mining model, physics-informed ML, uncertainty / OOD
- Transfer distance: adjacent materials
- Candidate MOF route: Use reaction-specific small-data learning as a template for MOF catalytic active-site or reaction-family datasets.
- MOF transfer note: Active-learning or uncertainty workflow could help decide which MOF DFT/MD/GCMC labels are worth generating next.
- Suggested next step: Use uncertainty-aware active learning to choose MOF calculations that probe new nodes, linkers, and guest-loaded states. Add kinetics, explicit environment effects, and active-site reconstruction checks.
- Long-horizon MOF prior art:
  - active learning / Bayesian optimization: Large language model agents accelerate inverse design of metal-organic frameworks for gas separation (arXiv (Cornell University), 2026-07-12)
  - active learning / Bayesian optimization: AI-integrated manufacturing of advanced materials for energy storage, catalysis, and environmental applications (Frontiers in Chemistry, 2026-07-03)
  - uncertainty / OOD: Predictive Synthesis of MOFs and COFs (arXiv (Cornell University), 2026-10-08)

## Reading Rules

- Fresh means no same method-class tag was found in the recent or long-horizon MOF baselines. It still needs full-paper confirmation.
- Distant cross-domain methods are allowed when the method can be mapped to a concrete MOF object, such as structure images, spectra, isotherms, pore maps, generated CIF checks, or multimodal literature-structure consistency.
- Older prior art means the idea is not new to MOFs, but it may still be worth pursuing if the cross-material paper adds a new representation, label space, uncertainty loop, active-learning strategy, or validation regime.
- Recent MOF activity means lower novelty unless the new method opens a clearly different MOF task or implementation path.
