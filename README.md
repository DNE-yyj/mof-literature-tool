# literature_tool

Small CLI for automatically collecting and summarizing recent `MOF/COF` computational-chemistry literature plus transferable ML-method papers from neighboring materials fields.

## What it does

- Queries recent papers from `OpenAlex` and `Crossref`
- Deduplicates overlapping hits
- Ranks papers for `MOF` relevance or cross-material method transferability
- Tags them by theme such as `adsorption`, `catalysis`, `DFT`, `ML`, `high_throughput`, `interatomic_potential`, `foundation_model`, `generative_model`, and `active_learning`
- Writes a Markdown report plus raw `JSON/TSV`
- Can run from a reusable JSON config, which is convenient for recurring research-radar jobs

## Quick start

```powershell
python run.py --profile mof_latest --days 365 --limit 20
```

Windows one-click wrapper:

```powershell
powershell -ExecutionPolicy Bypass -File .\run_latest_mof.ps1
```

Config-driven run:

```powershell
python run.py --config configs/weekly_mof_latest.json
```

More focused runs:

```powershell
python run.py --profile mof_adsorption --days 180 --limit 15
python run.py --profile mof_catalysis --days 365 --limit 15
python run.py --profile cof_transfer_methods --days 365 --limit 15
python run.py --profile materials_ml_transfer --days 1095 --limit 30 --rows-per-query 15
python run.py --profile mof_ml_method_prior_art --days 3650 --limit 60 --rows-per-query 25
python run.py --profile mof_adsorption --query "metal-organic framework water adsorption machine learning" --query "MOF-303 water diffusion interatomic potential" --limit 10
```

Cross-material ML transfer config:

```powershell
python run.py --config configs/materials_ml_transfer.json
```

Long-horizon MOF method prior-art config:

```powershell
python run.py --config configs/mof_ml_method_prior_art.json
```

One-shot combined novelty workflow:

```powershell
python run_method_transfer_novelty.py
```

## Recurring research radar

Preferred recurring setup is a Codex app automation that runs the combined workflow every two weeks:

```powershell
python -B run_method_transfer_novelty.py
```

The automation should read the newest combined report under `reports/method_transfer_novelty/` and summarize high-fit research opportunities, including each core paper's main content, innovation, limitations, fit, and executable next steps. If the scan is thin, it should say there is no strong recommendation rather than forcing a novelty claim.

Manual config test:

```powershell
powershell -ExecutionPolicy Bypass -File .\run_weekly.ps1 -ConfigPath .\configs\weekly_mof_latest.json
```

Legacy Windows Scheduled Task helper:

```powershell
powershell -ExecutionPolicy Bypass -File .\register_weekly_task.ps1 -ConfigPath .\configs\weekly_mof_latest.json -TaskName "MOF Literature Weekly" -Force
```

Register the cross-material ML transfer scan as a separate weekly task:

```powershell
powershell -ExecutionPolicy Bypass -File .\register_weekly_task.ps1 -ConfigPath .\configs\materials_ml_transfer.json -TaskName "Materials ML Transfer Weekly" -Force
```

Register the long-horizon MOF method prior-art scan:

```powershell
powershell -ExecutionPolicy Bypass -File .\register_weekly_task.ps1 -ConfigPath .\configs\mof_ml_method_prior_art.json -TaskName "MOF ML Method Prior Art" -Force
```

The preferred Codex automation path is to schedule `python -B run_method_transfer_novelty.py` instead of registering the three Windows tasks separately. That workflow runs all three scans and writes one combined report under `reports/method_transfer_novelty/`.

Trigger the registered task immediately:

```powershell
powershell -ExecutionPolicy Bypass -File .\trigger_weekly_task_now.ps1 -TaskName "MOF Literature Weekly"
```

If you want a better field-level synthesis and already have an OpenAI API key:

```powershell
$env:OPENAI_API_KEY="your_key_here"
python run.py --profile mof_latest --days 365 --limit 20 --use-openai
```

The default output directory is `output/`.

Config files under `configs/` use `output_root`, so each scheduled run creates a timestamped subfolder automatically.

## Output files

- `report.md`: readable literature brief
- `papers.json`: full normalized metadata
- `papers.tsv`: quick spreadsheet-friendly export
- `manifest.json`: run metadata

The combined novelty workflow writes:

- `reports/method_transfer_novelty/<timestamp>/report.md`: one triage report comparing cross-material ML ideas against recent and long-horizon MOF baselines
- `reports/method_transfer_novelty/<timestamp>/manifest.json`: paths to all three source runs

## Research-radar output

For biweekly summaries, do not only list new papers. Read `report.md` and `papers.json`, then report:

- what each core paper mainly did
- what is innovative
- what is missing or weak
- how closely it fits the current MOF/ML/adsorption-mechanism direction
- which 1-3 ideas are worth turning into executable projects
- a concise workflow, preferably with a Mermaid flowchart, for high-fit ideas

Do not invent papers, DOIs, venue status, or conclusions. Mark preprints, metadata-only records, and unverified claims explicitly.

## Notes

- `OpenAlex` and `Crossref` both support polite-pool usage with an email address. You can pass one with `--mailto your@email`.
- The default summarization path is rule-based, so it works without any extra dependency or API key.
- The optional OpenAI upgrade only changes the high-level field summary; per-paper briefs still remain grounded in the collected metadata and abstract text.
- If you pass one or more `--query` arguments, they replace the built-in query list while keeping the selected profile's relevance filters.
- For recurring Codex automation runs, keep the automation prompt aligned with the desired research-radar output. For manual config runs, the easiest place to change the topic is the `queries` array in a config file such as `configs/weekly_mof_latest.json`.
- If you want to change the built-in profile-level filters themselves, edit `profiles.py`.
- `materials_ml_transfer` intentionally allows non-MOF papers, then filters for concrete transferable method signals and prioritizes high-impact journal families where possible.
- For novelty checks, compare reports generated on the same day. The most reliable workflow is to run `weekly_mof_latest`, `materials_ml_transfer`, and `mof_ml_method_prior_art` back-to-back. Treat cross-material ideas as fresh only if neither the recent MOF run nor the long-horizon MOF prior-art run already contains the same method class, unless the new paper adds a clearly different representation, label, uncertainty, active-learning, or validation angle.
