# Demo runbook

## Preconditions
- Run from the repository root with Python 3.11+.
- Install PowerShell 7 for the metadata planner.
- Optional browser demo: Docker engine and Compose. Start with two workers; thirteen Chromium
  instances can require substantial memory. Each worker has a 768 MB limit.

## Reporting
1. Inspect the synthetic input in `examples/wazuh-report/events.json`.
2. Run the README command. Expect three unique events from four input records.
3. Open `generated/report/summary.html`; check `summary.csv` for aggregation results.
4. Date windows are UTC, start-inclusive and end-exclusive. Timestamps must contain timezones.
5. Invalid event fields cause a failed run. Correct the fixture and rerun; outputs are reproducible.

## Key Vault planning
1. Use only the bundled metadata fixture; it contains titles and synthetic source IDs.
2. Run `plan.ps1`. Expect two proposed names with `action: plan-only`.
3. Colliding normalized names or duplicate source IDs fail before an output file is written.
4. The demo makes no cloud requests and carries no secret values. It is not a migration tool.

## Browser workers
1. `docker compose -f examples/docker-selenium/compose.yaml config --quiet`
2. Build and start the two-worker demo from README.
3. Inspect `docker compose -f examples/docker-selenium/compose.yaml logs worker` for JSON results.
4. Every worker should report `status: passed`; each tests `DEMO-001` against the local fixture.
5. A failure exits non-zero and records only the exception class. Use the fixture and container logs
   for diagnosis. Stop the demo with `docker compose ... down`.
6. The network is internal and no ports are published. Chromium's sandbox is disabled inside this
   demonstration container; only use the bundled local fixture. Do not point it at untrusted sites.

## Dependencies and scope
Python base images are version-family tags and Selenium is constrained to major version 4. Resolve
and pin exact versions/digests before production adoption. The demo does not access an employer's
systems, implement production retries/queues, or prove service availability.

## Primary references
- Selenium Chrome options: https://www.selenium.dev/documentation/webdriver/browsers/chrome/
- Docker Compose scaling: https://docs.docker.com/reference/cli/docker/compose/scale/
- Key Vault secret naming: https://learn.microsoft.com/azure/key-vault/general/about-keys-secrets-certificates
