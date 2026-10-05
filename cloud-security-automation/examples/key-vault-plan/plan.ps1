<# Synthetic metadata-only planner. Does not read secrets or connect to Azure. #>
[CmdletBinding()]
param([Parameter(Mandatory)][string]$InputPath,[Parameter(Mandatory)][string]$OutputPath)
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$entries = @(Get-Content -LiteralPath $InputPath -Raw | ConvertFrom-Json)
$names = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
$ids = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::Ordinal)
$plan = @()
foreach ($entry in $entries) {
    $id = [string]$entry.id
    if ([string]::IsNullOrWhiteSpace($id) -or -not $ids.Add($id)) { throw 'Missing or duplicate source id' }
    $title = [string]$entry.title
    $name = ($title.ToLowerInvariant() -replace '[^a-z0-9-]', '-').Trim('-')
    if ($name.Length -lt 1 -or $name.Length -gt 127) { throw 'Invalid proposed Key Vault name length' }
    if (-not $names.Add($name)) { throw "Proposed secret name collision: $name" }
    $plan += [pscustomobject]@{ sourceId=$id; proposedName=$name; action='plan-only'; containsSecretValue=$false }
}
$parent = Split-Path -Parent $OutputPath
if ($parent) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }
[pscustomobject]@{ mode='synthetic-metadata-only'; count=$plan.Count; entries=@($plan) } |
    ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $OutputPath -Encoding utf8
Write-Output "Plan generated for $($plan.Count) synthetic entries. No Azure requests performed."
