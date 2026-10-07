# Validation record — October 2026

These results concern synthetic portfolio examples, not the professional projects or production environments.

| Check | Result |
|---|---|
| Case coverage | PASS — 25 unique LinkedIn project IDs, 25 case notes, 25 fixtures, 25 sample outputs |
| Python/PowerShell suite | PASS — 55 tests, no failures or skips on the validation host |
| CLI execution | PASS — all 25 new `demo.py` commands completed successfully |
| Offline execution | PASS — all 25 handlers ran with socket creation blocked |
| Sample outputs | PASS — all 25 outputs match the shipped fixtures |
| Fixture preservation | PASS — handlers leave their inputs unchanged |
| Documentation links | PASS — 258 relative Markdown links resolve across 31 documentation files |
| Data review | PASS — fixtures authored from scratch; checked fictional identifiers, domains and documentation networks |
| Original PowerShell planner | PASS — valid input, duplicate source IDs and normalized-name collisions tested |
| Original CSV/HTML report | PASS — six tests covering duplicates, severity, date windows, timezones and spreadsheet formula handling |
| Docker Compose configuration | PASS — `docker compose config --quiet` |
| Actual Docker/Selenium containers | NOT RUN — Docker engine is unavailable on this machine |
| Azure, Graph, Action1, n8n, AD, Purview and other production integrations | NOT RUN — intentionally outside these offline demonstrations |

## Reproduce

```sh
cd cloud-security-automation
python3 -m unittest discover -s tests -v
python3 demo.py sharepoint
python3 demo.py patch-pilot
python3 demo.py lexrag
```

Python 3.11+ is required. PowerShell 7 enables the three original planner tests. If `pwsh` is absent, unittest reports those three as skipped; this does not mean they passed. The new 25-case suite uses only Python's standard library.

The nested `.github/workflows/validate.yml` remains a template for a standalone repository. GitHub does not automatically discover it while this package sits inside another repository. This record reports local execution, not hosted CI.

The legacy PDFs and original Docker worker retain their earlier validation history. This expansion does not claim a new PDF render, live cloud deployment, running AI model, encryption operation, patch job or Docker benchmark.
