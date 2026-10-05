# Selected case studies

## Microsoft 365 governance
**Scope:** inventory of more than 600 SharePoint sites. The work covered owners, members,
administrators, application permissions, controlled ownership changes, access checks,
backups and Excel audit reports. A pilot preceded bulk changes.

`Inventory → ownership review → controlled change → access validation → evidence`

The site count is an inventory scope, not a claim that every site was modified.
[Public evidence](https://www.linkedin.com/feed/update/urn:li:activity:7489746347470934016/).

## Key Vault migration
**Documented result:** 187 secrets migrated, zero errors, zero skipped entries.
PowerShell and KPScript connected the KeePass export process to Azure Key Vault.
Access validation, a temporary write check, a simulation and a final report supported the migration.

`KeePass → validation → transformation → Key Vault → reconciliation report`

[Public evidence](https://www.linkedin.com/feed/update/urn:li:activity:7489850755160489984/).

## Vulnerability orchestration
**Status:** pilot with a group of devices. The intended integrated flow combines findings from
Defender/Wazuh, CVE/KB/device correlation, selective Action1 remediation, post-update validation
and SharePoint evidence. Success rates and time savings have not been published.

`Defender / Wazuh → correlation → Action1 → validation → evidence`

Proposed pilot measures: devices in scope, successful jobs / attempted jobs, validation failures,
exceptions, and elapsed time from detection to verified closure. These are measurement proposals,
not achieved results. [Profile](https://www.linkedin.com/in/kristiangutierrez/details/projects/).

## Weekly reporting and container automation
The reporting workflow integrates Wazuh, Python/Bash, CSV/PDF output, SharePoint storage,
Microsoft Graph email and cron. The container automation project scaled Selenium execution
from one to thirteen Linux containers. No throughput multiplier is inferred from container count.

## Portfolio demonstration boundaries
The included examples use synthetic fixtures. The Wazuh example demonstrates local data processing;
it omits live Wazuh, Graph, SharePoint and PDF integrations. The Key Vault example is a metadata-only
planner; it does not migrate secrets. The Selenium example uses one local fixture and independent
smoke checks; it does not reproduce a production queue. None of the demos executes patching.
