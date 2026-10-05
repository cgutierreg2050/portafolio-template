# Validation record — 2026-10-04

The examples use synthetic data. These checks validate the portfolio demonstrations, not the results of the professional projects.

| Check | Result |
|---|---|
| Python and PowerShell test suite | PASS — 9 tests (6 reporting, 3 planner) |
| Reporting CLI fixture | PASS — 4 records reduced to 3 unique events; CSV and HTML created |
| PowerShell planner CLI fixture | PASS — 2 metadata entries planned without Azure access |
| Docker Compose configuration | PASS — `docker compose config --quiet` |
| Selenium worker syntax | PASS — Python compilation |
| Selenium container execution | NOT RUN — Docker engine unavailable on the validation machine |
| PDF layout | PASS — all 10 pages rendered and visually inspected |

Run the test suite from the package directory:

```sh
python3 -m unittest discover -s tests -v
```

The Docker demonstration still requires a complete build and smoke test on a host with a running Docker engine. No end-to-end Docker or 13-worker performance result is claimed.

The included `.github/workflows/validate.yml` is a reusable workflow template for a standalone repository. When this package is stored in a subdirectory, GitHub does not discover that nested workflow automatically. The results above are local checks, not a claim that hosted CI ran.
