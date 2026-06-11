# Literature Tool Reference

## Repository Markers

Treat a directory as the target repository when it contains:

- `run.py`
- `core.py`
- `profiles.py`
- `configs/`

The current project already follows this structure.

## Preferred Entry Points

- One-off CLI run: `python run.py --profile mof_latest --days 365 --limit 20`
- Config-driven run: `python run.py --config configs/weekly_mof_latest.json`
- Combined research-radar workflow: `python -B run_method_transfer_novelty.py`
- Preferred recurring schedule: Codex app automation running the combined workflow every two weeks
- Windows convenience wrapper: `powershell -ExecutionPolicy Bypass -File .\run_latest_mof.ps1`
- Cross-material ML transfer run: `python run.py --config configs/materials_ml_transfer.json`
- Long-horizon MOF method prior-art run: `python run.py --config configs/mof_ml_method_prior_art.json`
- Legacy Windows manual trigger: `powershell -ExecutionPolicy Bypass -File .\run_weekly.ps1 -ConfigPath .\configs\weekly_mof_latest.json`
- Legacy Windows task registration: `powershell -ExecutionPolicy Bypass -File .\register_weekly_task.ps1 -ConfigPath .\configs\weekly_mof_latest.json -TaskName "MOF Literature Weekly" -Force`

## Built-in Profiles

- `mof_latest`: broad MOF adsorption or catalysis scan with ML or DFT or screening or interatomic-potential relevance
- `mof_adsorption`: adsorption, separation, water harvesting, carbon capture, and diffusion
- `mof_catalysis`: catalytic MOF studies with DFT, descriptors, and data-driven discovery
- `cof_transfer_methods`: COF-side methods that may transfer to MOFs, especially MLIP, representation learning, and screening workflows
- `materials_ml_transfer`: cross-material ML method papers that may transfer to MOFs; allows non-MOF papers and prioritizes concrete method novelty, high-impact venues, and unsaturated MOF opportunities
- `mof_ml_method_prior_art`: long-horizon MOF scan for ML method classes; use this as a prior-art baseline before calling a cross-material method genuinely new for MOFs

## Config Keys

Common JSON config fields:

- `name`: label for the run configuration
- `profile`: built-in profile name
- `days`: lookback window
- `limit`: retained paper count after ranking
- `rows_per_query`: per-source fetch count before deduplication
- `output_dir`: fixed output directory
- `output_root`: parent directory for timestamped runs
- `timestamped_output`: whether to append a timestamp folder under `output_root`
- `mailto`: optional polite-pool email for OpenAlex and Crossref
- `use_openai`: optional LLM upgrade, usually `false` for this skill
- `openai_model`: model name for the optional upgrade
- `queries`: explicit query override list
- `schedule.weekday` and `schedule.time`: legacy Windows task settings. Codex app automations own the preferred recurring schedule.

## Output Files

Each run writes:

- `report.md`: readable literature brief
- `papers.json`: normalized metadata with tags, scores, takeaways, and relevance notes
- `papers.tsv`: spreadsheet-friendly export
- `manifest.json`: run metadata, queries, and output paths

Prefer `report.md` for quick synthesis. Open `papers.json` when exact tags, DOI, authors, or selected queries matter.

The combined method-transfer novelty workflow writes a timestamped folder under `reports/method_transfer_novelty/` containing:

- `report.md`: one triage report comparing cross-material method candidates against recent MOF and long-horizon MOF baselines
- `manifest.json`: source output paths for the three component scans

## Research Radar Synthesis

Use this mode when the user asks whether recent literature contains interesting, meaningful, feasible, or high-fit work. Do not only list papers.

Default output:

- Current conclusion: whether there is a strong high-fit opportunity.
- Paper table: main content, innovation, limitations, fit to the user's MOF/ML/adsorption-mechanism direction, and evidence status.
- Selected ideas: only 1-3 high-fit ideas.
- Method-problem alignment: whether each selected idea is method-driven or problem-driven, and how the other side is made concrete.
- Executable plan for each selected idea: entry point, scientific question or application, method lever, expected improvement mechanism, literature basis, data sources, calculation/simulation workflow, ML method, validation metrics, risks, and fallback route.
- Mermaid flowchart for the workflow.
- Evidence limits: preprint status, metadata-only records, missing full text, old report timestamps, or unverified claims.

Fit should weigh topic match and practicality more than short-term novelty. A scan with little relevant content should say "no strong recommendation" and may recap the last 1-3 months of high-fit directions.

## Method-Problem Alignment Checklist

Use this checklist before recommending an executable project:

- If the source paper is mainly a method paper, name the scientific question, application, or bottleneck where the method can land in the user's work. Do not stop at "this method is transferable."
- If the source paper starts from a specific application or scientific question, name the method family that could improve it, what will improve, and how to test the improvement.
- Acceptable improvement targets include better mechanistic resolution, less DFT/MD labeling, longer simulations, uncertainty-aware screening, clearer regime classification, improved wet/defective MOF transferability, or better validation against known adsorption/diffusion observables.
- Prefer topic chains where the first project's computed data can be reused for later MLIP training, universal-MLIP error analysis, uncertainty benchmarking, or broader MOF screening.
- Down-rank ideas with weak mapping between method and science problem even when either side is individually interesting.

## Academic Research Suite Coordination

When turning literature into a proposal, use `academic-research-suite` as a downstream evaluation layer:

- `source_verification_agent`: source existence, venue status, DOI/arXiv/ChemRxiv checks, and source quality.
- `synthesis_agent`: cross-paper convergence, contradictions, and gap analysis.
- `research_question_agent`: FINER-style, answerable research questions.
- `research_architect_agent`: methodology, data strategy, validity checks, and reporting plan.
- `experiment-agent` plan mode: executable computational or ML experiment plan.
- `devils_advocate_agent`: stress-test novelty, feasibility, assumptions, and strongest objections.

Keep these roles inline unless the user explicitly asks for multi-agent or parallel work. If using Codex subagents, give them independent verification/synthesis/feasibility tasks and reconcile their conclusions before reporting.

## Practical Topic Tuning

- Change the config `queries` array first when the user wants a narrower topic.
- Keep the same `profile` when you still want the existing relevance filters.
- Switch profiles when the user changes from adsorption to catalysis or to COF transfer methods.
- Increase `days` or `rows_per_query` when the run returns too few papers.
- For novelty checks, compare MOF, cross-material transfer, and MOF prior-art reports generated on the same date. If they were generated at different times, run all three profiles back-to-back before making a strong claim about whether a method is still fresh for MOFs.
- For `materials_ml_transfer`, treat novelty as three-stage: identify a non-MOF ML method innovation first, check recent MOF papers for the same method class, then check `mof_ml_method_prior_art` for older MOF adoption. Keep it only if MOF adoption is absent or the new paper adds a different representation, label space, uncertainty/active-learning loop, or validation regime.
- For research radar, prioritize fit to the user's current research direction, feasibility with available data/compute, and whether the idea opens a credible executable workflow.

## No-Key Policy

This repository already supports a full no-key flow through rule-based summaries plus OpenAlex and Crossref. Do not enable `--use-openai` unless the user explicitly asks for the optional upgrade and already has a key configured.

## Recurring Schedule

Prefer Codex app automation over Windows Scheduled Tasks for recurring research radar. The intended default is a biweekly automation that runs `python -B run_method_transfer_novelty.py`, reads the newest combined report, and emits the research-radar synthesis.

Windows helpers are legacy/manual compatibility:

- `run_weekly.ps1`: execute a config-driven run and log the output
- `register_weekly_task.ps1`: create or replace a weekly scheduled task
- `trigger_weekly_task_now.ps1`: launch an existing scheduled task immediately

For Codex automation schedule changes, update the automation itself rather than editing the PowerShell registration script.
