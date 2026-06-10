# Target-System Change Request Template

Use this template after installing the `literature-search-summary` skill when you want to retarget the literature workflow from the default MOF-oriented setting to another material system, experimental focus, or transfer objective.

## 1. New Target

- Target material family:
  - Example: COF, MOF, zeolite, oxide catalyst, polymer membrane, battery cathode.
- Primary research mode:
  - Example: experiment-first, computation-first, mixed experiment/computation.
- Current user goal:
  - Example: find ML methods from other materials fields that can inspire COF experimental design.

## 2. Application Scope

- Main applications to prioritize:
  - Example: gas adsorption, photocatalysis, electrocatalysis, water harvesting, membrane separation, synthesis optimization, stability, conductivity.
- Applications to keep as secondary:
  - Example: general property prediction, structure generation, high-throughput screening.
- Applications to exclude:
  - Example: biomedical, drug delivery, sensors, purely computational benchmarks with no experimental route.

## 3. Method Scope

- ML method classes to prioritize:
  - Example: active learning, Bayesian optimization, generative design, GNN/equivariant models, foundation models, uncertainty/OOD, symbolic regression, ML interatomic potentials.
- Methods that are interesting only if experimentally actionable:
  - Example: closed-loop synthesis, robotic/self-driving labs, synthesis-condition prediction, interpretable descriptors.
- Methods to down-rank:
  - Example: black-box property prediction without synthesis or validation path.

## 4. Novelty Baseline

- Recent target-system window:
  - Example: last 365 days of COF literature.
- Long-horizon target-system prior-art window:
  - Example: last 10 years of COF literature.
- What counts as "already absorbed" by the target field?
  - Example: same method class already applied to COF synthesis, COF property prediction, or COF experimental validation.
- What still counts as new despite prior art?
  - Example: new representation, new label space, new synthesis variable, uncertainty-guided experiment selection, or stronger experimental validation.

## 5. Venue Priority

- Journals or venue families to prioritize:
  - Example: Nature, Science, Cell, Nature Materials, Nature Chemistry, Nature Synthesis, Nature Communications, JACS, Angewandte Chemie, Chemical Science, ACS Central Science, Advanced Materials.
- Field-specific journals to include:
  - Example: Chemistry of Materials, Journal of Materials Chemistry A, ACS Materials Letters, Small, Advanced Functional Materials.
- Preprints:
  - Include / exclude / include only when method is very relevant.

## 6. Desired Profiles And Configs

Request the following changes:

- Add a recent target-system profile:
  - Suggested name: `<target>_latest`
  - Example: `cof_latest`
- Add a cross-material transfer profile:
  - Suggested name: `<target>_materials_ml_transfer`
  - Example: `cof_materials_ml_transfer`
- Add a long-horizon prior-art profile:
  - Suggested name: `<target>_ml_method_prior_art`
  - Example: `cof_ml_method_prior_art`
- Add a combined novelty workflow:
  - Suggested name: `run_<target>_method_transfer_novelty.py`
  - Example: `run_cof_method_transfer_novelty.py`

## 7. Output Expectations

- Combined report should include:
  - Fresh transfer candidates.
  - Older target-system prior art exists.
  - Already active in recent target-system literature.
  - Top opportunities with experimental actionability.
- Per-paper fields to emphasize:
  - Method innovation.
  - Target-system relevance.
  - Experimental feasibility.
  - Missing validation.
  - Suggested next experiment or benchmark.

## 8. Automation

- Preferred schedule:
  - Example: every Monday at 09:00 local time.
- Automation type:
  - Example: Codex automation, not Windows Task Scheduler.
- Desired final command:
  - Example: `python -B run_cof_method_transfer_novelty.py`

## 9. Acceptance Checks

The retargeted workflow is acceptable when:

- The new target profile allows target-system papers and filters out irrelevant biomedical/sensor/drug-delivery work unless requested.
- The transfer profile allows non-target-system papers but keeps only concrete transferable ML method signals.
- The prior-art profile searches a long enough target-system window to avoid mistaking old methods for new opportunities.
- The combined report clearly separates:
  - fresh opportunities,
  - older prior art,
  - recently active topics.
- Tests or a dry run show that the new profiles are recognized by `python run.py --help`.

## Filled Example: COF Experimental User

- Target material family: COF.
- Primary research mode: experiment-first.
- Goal: find ML or data-driven methods from other materials fields that can inspire COF synthesis, structure-property optimization, adsorption/catalysis experiments, or stability studies.
- Prioritize:
  - active learning for experiment selection,
  - Bayesian optimization of synthesis conditions,
  - generative linker/topology design with synthesizability constraints,
  - interpretable descriptors linked to experimental observables,
  - uncertainty-aware prediction before expensive experiments.
- Down-rank:
  - pure benchmark papers without experimental route,
  - methods already widely used in COF literature unless they add a new experimental variable or validation strategy.
- Suggested new profiles:
  - `cof_latest`
  - `cof_materials_ml_transfer`
  - `cof_ml_method_prior_art`
- Suggested combined workflow:
  - `run_cof_method_transfer_novelty.py`
