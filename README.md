# literature_tool

Small CLI for automatically collecting and summarizing recent `MOF/COF` computational-chemistry literature.

## What it does

- Queries recent papers from `OpenAlex` and `Crossref`
- Deduplicates overlapping hits
- Ranks papers for `MOF` relevance
- Tags them by theme such as `adsorption`, `catalysis`, `DFT`, `ML`, `high_throughput`, and `interatomic_potential`
- Writes a Markdown report plus raw `JSON/TSV`
- Can run from a reusable JSON config, which is convenient for weekly scheduled jobs

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
python run.py --profile mof_adsorption --query "metal-organic framework water adsorption machine learning" --query "MOF-303 water diffusion interatomic potential" --limit 10
```

## Weekly scheduled run

Recommended manual test:

```powershell
powershell -ExecutionPolicy Bypass -File .\run_weekly.ps1 -ConfigPath .\configs\weekly_mof_latest.json
```

Register a weekly Windows scheduled task:

```powershell
powershell -ExecutionPolicy Bypass -File .\register_weekly_task.ps1 -ConfigPath .\configs\weekly_mof_latest.json -TaskName "MOF Literature Weekly" -Force
```

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

## Notes

- `OpenAlex` and `Crossref` both support polite-pool usage with an email address. You can pass one with `--mailto your@email`.
- The default summarization path is rule-based, so it works without any extra dependency or API key.
- The optional OpenAI upgrade only changes the high-level field summary; per-paper briefs still remain grounded in the collected metadata and abstract text.
- If you pass one or more `--query` arguments, they replace the built-in query list while keeping the selected profile's relevance filters.
- For scheduled runs, the easiest place to change the topic is the `queries` array in a config file such as `configs/weekly_mof_latest.json`.
- If you want to change the built-in profile-level filters themselves, edit `profiles.py`.
