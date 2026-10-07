# Kristian Gutierrez | 25 infrastructure and automation projects

[Español](README.es.md) · [LinkedIn](https://www.linkedin.com/in/kristiangutierrez/) · [Website](https://www.kggdev.org/)

Hybrid infrastructure, identity, security and automation with Azure, Microsoft 365, Windows Server, Linux, PowerShell, Python and APIs.

**25 documented professional cases · 25 offline demonstrations · entirely synthetic data · ES/EN documentation.**

Each case separates the professional work described on LinkedIn from the example built for this repository. The demonstrations are AI-assisted reconstructions from those descriptions, using data created from scratch. Test results apply to sample code, not production outcomes.

## Start in one minute

Python 3.11 or later. All 25 new demonstrations use the standard library and need no accounts, credentials, containers or service connections.

```sh
git clone --branch linkedin-portfolio --single-branch https://github.com/cgutierreg2050/portafolio-template.git
cd portafolio-template/cloud-security-automation
python3 demo.py sharepoint
python3 demo.py patch-pilot
python3 -m unittest discover -s tests -v
```

Every project folder contains `README.md`, `input.json` and `output.example.json`. Use `--output generated/result.json` to save a local result.

## All 25 projects

| # | Project | Professional case status | Included demonstration |
|---|---|---|---|
| 01 | [Email security and DMARC diagnostics](projects/dmarc/README.md) | Implemented, as described in the published case | Evaluates strict SPF/DKIM domain alignment against the From domain using supplied synthetic results. |
| 02 | [KeePass to Azure Key Vault migration](projects/key-vault/README.md) | Implemented, as described in the published case | Normalizes synthetic entry names and rejects collisions or fields that could contain credentials. |
| 03 | [Batch transcription and GPU resource control](projects/transcription/README.md) | Implemented, as described in the published case | Packs synthetic jobs into batches within a declared memory budget and separates oversized jobs. |
| 04 | [Office infrastructure relocation](projects/relocation/README.md) | Implemented, as described in the published case | Computes a dependency schedule and detects cycles or missing tasks. |
| 05 | [Terraform and GitHub Actions automation](projects/terraform/README.md) | Implemented, as described in the published case | Reviews a simplified plan for replacements, deletions, management exposure and missing tags. |
| 06 | [Python and Microsoft Graph communications](projects/graph-mail/README.md) | Implemented, as described in the published case | Builds escaped HTML drafts, deduplicates recipients and groups batches with tracking keys. |
| 07 | [Docker and Selenium query automation](projects/docker-selenium/README.md) | Implemented, as described in the published case | Allocates synthetic jobs across workers by estimated cost. The existing Docker/Selenium local-page example is retained. |
| 08 | [Microsoft 365 data lifecycle and archive assessment](projects/data-lifecycle/README.md) | Assessment and design | Selects candidates by activity date, retention and legal holds, recording exclusions. |
| 09 | [Application control with AppLocker and WDAC](projects/applocker-wdac/README.md) | Implemented, as described in the published case | Evaluates synthetic hash/publisher rules with deny precedence and audit-versus-enforcement outcomes. |
| 10 | [Azure VM and site-to-site VPN](projects/azure-vpn/README.md) | Implemented, as described in the published case | Checks network overlap, VM address membership, declared routes and DNS forwarding. |
| 11 | [n8n on Kubernetes with Cloudflare Tunnel](projects/n8n-kubernetes/README.md) | Implemented, as described in the published case | Reviews persistence, readiness, encryption-key reference, internal service, tunnel and access policy. |
| 12 | [Microsoft 365 and SharePoint governance](projects/sharepoint/README.md) | Inventory implemented; changes piloted | Proposes adding an active owner only to pilot sites with verified backups; preserves current owners. |
| 13 | [Microsoft Purview and DLP governance](projects/purview-dlp/README.md) | Implemented, as described in the published case | Detects synthetic markers, proposes labels and external-sharing restrictions, and preserves legal holds. |
| 14 | [Post-incident Microsoft 365 hardening](projects/m365-hardening/README.md) | Implemented, as described in the published case | Reports unapproved administrators, MFA gaps and unapproved external forwarding. |
| 15 | [Azure Arc and hybrid connectivity](projects/azure-arc/README.md) | Implemented, as described in the published case | Reconciles inventory and agent records to detect missing devices, stale data and future timestamps. |
| 16 | [Local AI infrastructure and prototyping lab](projects/ai-lab/README.md) | Lab implemented for testing | Estimates a lower bound for weight memory from parameter count and precision, with configurable reserve. |
| 17 | [Secure file exchange with OpenPGP and SFTP](projects/openpgp/README.md) | Development and validation | Checks subkey metadata, execution context, expiry and revocation. |
| 18 | [LexRAG private document retrieval](projects/lexrag/README.md) | Indexing and validation | Searches authorized synthetic documents for terms and returns source references, or no evidence. |
| 19 | [GLPI test migration and Defender inventory validation](projects/glpi-defender/README.md) | Migration tested in a test environment | Compares table sets and distinguishes inventory mismatches, protection gaps and stale signatures. |
| 20 | [Active Directory and hybrid identity modernization](projects/active-directory/README.md) | AD improvements implemented; Windows Server 2025 planning | Checks supplied replication, DNS, time synchronization, FSMO ownership and recovery-test metadata. |
| 21 | [Infrastructure and security monitoring](projects/monitoring/README.md) | Implemented, as described in the published case | Combines capacity, availability and event severity into a synthetic alert list. |
| 22 | [Vulnerability and patch orchestration](projects/patch-pilot/README.md) | Pilot with selected endpoints | Deduplicates findings and models eligibility, reboot deferral and evidence-gated closure. |
| 23 | [IIS publishing with Cloudflare WAF and TLS](projects/iis-cloudflare/README.md) | Implemented, as described in the published case | Reviews synthetic origin TLS, WAF, access policy, direct exposure and certificate expiry metadata. |
| 24 | [KVM/QEMU Windows VM recovery](projects/kvm-recovery/README.md) | VM startup and console access restored | Inspects synthetic XML and proposes a disk path only when there is one unambiguous candidate. |
| 25 | [Weekly Wazuh security reporting](projects/wazuh-reporting/README.md) | Implemented, as described in the published case | Deduplicates events by agent and ID, filters a UTC window and summarizes severity. The original example generates CSV/HTML. |

## Original examples retained

- [PowerShell: Key Vault naming planner](examples/key-vault-plan/plan.ps1).
- [Python: CSV/HTML event export](examples/wazuh-report/report.py).
- [Docker/Selenium: local page and independent workers](examples/docker-selenium/compose.yaml).

PowerShell 7 is required for the original planner. Docker is optional and its validation is recorded separately. The `demo.py docker-selenium` simulation runs without Docker.

## Code, data and validation

```text
projects/<case>/input.json
        ↓
demo.py → lab/security.py | lab/cloud.py | lab/operations.py
        ↓
JSON result: synthetic=true, production_validation=false
```

- [Synthetic data policy and boundaries](docs/data-policy.md)
- [Validation record](docs/validation.md)
- [Runbook](docs/runbook.md)
- [Machine-readable 25-case catalog](projects/catalog.json)
- [Behavior tests](tests/test_catalog.py)

## Selected PDF briefs

[SharePoint](docs/ficha-sharepoint.pdf) · [Key Vault](docs/ficha-key-vault.pdf) · [Vulnerability pilot](docs/ficha-vulnerabilidades.pdf) · [Technical portfolio overview](docs/portfolio-kristian-gutierrez.pdf)

The retained PDFs cover an earlier selection of cases. The table above is the current complete 25-project catalog.
