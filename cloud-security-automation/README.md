# Kristian Gutierrez | Cloud & Security Automation

Senior Systems & Infrastructure Engineer focused on Microsoft Azure, Microsoft 365,
PowerShell, Python and security automation.

[LinkedIn](https://www.linkedin.com/in/kristiangutierrez/) · [Español](README.es.md) · [Technical portfolio](docs/portfolio-kristian-gutierrez.pdf)

## Selected professional work

| Case | Documented scope or result | Status |
|---|---|---|
| Microsoft 365 governance | Inventory of more than 600 SharePoint sites; ownership, access validation and audit records | Documented work, with a controlled pilot before bulk changes |
| KeePass to Azure Key Vault | 187 secrets migrated; 0 errors; 0 skipped entries | Completed migration |
| Vulnerability and patch orchestration | Defender/Wazuh → Action1 → validation → SharePoint evidence | Pilot with a group of devices |
| Security reporting | Wazuh → Python → CSV/PDF → SharePoint → Microsoft Graph email | Weekly workflow implemented |
| Containerized browser automation | Selenium on Linux; execution scaled from 1 to 13 containers | Implemented architecture |

Professional project descriptions are based on my documented LinkedIn work. The code below
was prepared separately as illustrative portfolio material. It is **not an export of an employer's
production implementation** and contains only synthetic data. It does not substantiate
production performance or the completion of the patching pilot.

## Run the demonstrations

Requirements: Python 3.11+; PowerShell 7+ for the migration planner; Docker Compose and a
running Docker engine for the optional browser demo.

```sh
python3 examples/wazuh-report/report.py --input examples/wazuh-report/events.json --out generated/report
pwsh -NoProfile -File examples/key-vault-plan/plan.ps1 -InputPath examples/key-vault-plan/entries.json -OutputPath generated/key-vault-plan.json
python3 -m unittest discover -s tests -v
```

The first demo emits CSV and HTML summaries from synthetic Wazuh-like events, with duplicate
handling and date boundaries. The planner emits proposed Key Vault names and collision errors
from metadata only: it never reads credentials or connects to Azure.

### Optional Docker / Selenium demo

```sh
docker compose -f examples/docker-selenium/compose.yaml up -d --build --scale worker=2
docker compose -f examples/docker-selenium/compose.yaml wait worker
docker compose -f examples/docker-selenium/compose.yaml logs worker
docker compose -f examples/docker-selenium/compose.yaml down
# Larger demonstration, when the host has enough CPU/RAM:
docker compose -f examples/docker-selenium/compose.yaml up -d --build --scale worker=13
docker compose -f examples/docker-selenium/compose.yaml wait worker
docker compose -f examples/docker-selenium/compose.yaml logs worker
docker compose -f examples/docker-selenium/compose.yaml down
```

Each worker runs the same synthetic smoke check against an isolated local demo page and emits
one JSON result. This illustrates independent container execution; it is not a distributed job
queue or a benchmark. No external websites are queried and no host ports are published.

## Architecture and operation

- [Case studies and public evidence](docs/cases.md)
- [Runbook and demo boundaries](docs/runbook.md)
- [Validation record](docs/validation.md)

## Public evidence

- [Microsoft 365 governance](https://www.linkedin.com/feed/update/urn:li:activity:7489746347470934016/)
- [Key Vault migration](https://www.linkedin.com/feed/update/urn:li:activity:7489850755160489984/)
- [Professional project descriptions](https://www.linkedin.com/in/kristiangutierrez/details/projects/)

## Contact and role focus

Senior Systems Engineer · Cloud Infrastructure Engineer · Security Automation Engineer.
Contact through [LinkedIn](https://www.linkedin.com/in/kristiangutierrez/).
