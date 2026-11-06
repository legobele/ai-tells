#Requires -Version 7.0
<#
.SYNOPSIS
    Regenerates the detection matrix in SKILL.md from methods/*.md frontmatter.

.DESCRIPTION
    methods/ is the source of truth. SKILL.md's matrix is a derived cache.

    Reads flat `key: value` frontmatter only, so no YAML dependency. Every
    method file is self-describing: it carries its own class, status,
    fidelity, vector, and verification date. There is no central registry
    to fall out of sync.

    Sorting is by terminality, then fidelity, then name:
      vector:   terminal > live > weak > none
      fidelity: very-high > high > medium > low > near-zero

    Entries not verified in 12 months are marked STALE.
    Entries with confidence: low are marked with a trailing ?.

.PARAMETER Write
    Rewrite SKILL.md between the MATRIX markers instead of printing to stdout.

.PARAMETER Json
    Emit the parsed entries as JSON.

.EXAMPLE
    pwsh -File tools/sync-matrix.ps1
    pwsh -File tools/sync-matrix.ps1 -Write
#>
[CmdletBinding()]
param(
    [switch]$Write,
    [switch]$Json
)

$ErrorActionPreference = 'Stop'

$root      = Split-Path -Parent $PSScriptRoot
$methodDir = Join-Path $root 'methods'
$skillPath = Join-Path $root 'SKILL.md'
$staleCut  = (Get-Date).AddMonths(-12)

$vectorRank   = @{ 'terminal' = 0; 'live' = 1; 'weak' = 2; 'none' = 3 }
$fidelityRank = @{ 'very-high' = 0; 'high' = 1; 'medium' = 2; 'low' = 3; 'near-zero' = 4 }

function Get-Rank {
    param($Table, $Key)
    if ([string]::IsNullOrWhiteSpace($Key)) { return 9 }
    $v = $Table[$Key]
    if ($null -eq $v) { return 9 }
    return [int]$v
}

function Read-FrontMatter {
    param([string]$Path)
    $lines = Get-Content -LiteralPath $Path
    if ($lines.Count -lt 3) { return $null }
    if ($lines[0].Trim() -ne '---') { return $null }

    $meta = [ordered]@{}
    for ($i = 1; $i -lt $lines.Count; $i++) {
        if ($lines[$i].Trim() -eq '---') { break }
        if ($lines[$i] -match '^\s*([A-Za-z][A-Za-z0-9_-]*)\s*:\s*(.*?)\s*$') {
            $meta[$Matches[1]] = $Matches[2]
        }
    }
    return $meta
}

# ---- collect -------------------------------------------------------------

$entries = [System.Collections.Generic.List[object]]::new()

foreach ($file in (Get-ChildItem -LiteralPath $methodDir -Filter '*.md' | Sort-Object Name)) {
    if ($file.BaseName -eq '_TEMPLATE') { continue }

    $m = Read-FrontMatter -Path $file.FullName
    if (-not $m) {
        Write-Warning "skipping $($file.Name): no frontmatter"
        continue
    }

    $verified = $m['last-verified']
    $stale    = $false
    $parsed   = [datetime]::MinValue
    if ($verified -and [datetime]::TryParse($verified, [ref]$parsed)) {
        $stale = $parsed -lt $staleCut
    }

    $entries.Add([pscustomobject]@{
        id           = if ($m['id'])   { $m['id'] }   else { $file.BaseName }
        name         = if ($m['name']) { $m['name'] } else { $file.BaseName }
        class        = $m['class']
        status       = $m['status']
        fidelity     = $m['fidelity']
        prevalence   = $m['prevalence']
        vector       = $m['vector']
        verified     = $verified
        confidence   = $m['confidence']
        stale        = $stale
        sortVector   = Get-Rank $vectorRank   $m['vector']
        sortFidelity = Get-Rank $fidelityRank $m['fidelity']
    })
}

if ($entries.Count -eq 0) {
    throw "no method files found in $methodDir"
}

$sorted = $entries | Sort-Object sortVector, sortFidelity, name

if ($Json) {
    $sorted | ConvertTo-Json -Depth 4
    return
}

# ---- render --------------------------------------------------------------

$sb = [System.Text.StringBuilder]::new()
[void]$sb.AppendLine('| Method | Class | Status | Fidelity | Vector | Verified |')
[void]$sb.AppendLine('|---|---|---|---|---|---|')

foreach ($e in $sorted) {
    $flags = ''
    if ($e.stale)              { $flags += ' STALE' }
    if ($e.confidence -eq 'low') { $flags += ' ?' }

    $name = if ($e.name -ne $e.id) { "$($e.name) (``$($e.id)``)" } else { "``$($e.id)``" }

    [void]$sb.AppendLine(
        "| $name | $($e.class) | $($e.status) | $($e.fidelity) | $($e.vector) | $($e.verified)$flags |"
    )
}

[void]$sb.AppendLine()
[void]$sb.AppendLine(
    "_Generated $(Get-Date -Format 'yyyy-MM-dd') from $($entries.Count) method files. " +
    "STALE = not verified in 12 months. ? = low confidence._"
)

$table = $sb.ToString()

if (-not $Write) {
    Write-Output $table
    return
}

# ---- write ---------------------------------------------------------------

if (-not (Test-Path -LiteralPath $skillPath)) {
    throw "SKILL.md not found at $skillPath"
}

$content = [System.IO.File]::ReadAllText($skillPath)
$pattern = '(?s)(<!-- MATRIX:START -->).*?(<!-- MATRIX:END -->)'

if ($content -notmatch $pattern) {
    throw "MATRIX:START / MATRIX:END markers not found in SKILL.md"
}

$updated = [regex]::Replace($content, $pattern, {
        param($match)
        $match.Groups[1].Value + "`n" + $table + $match.Groups[2].Value
    })

# File.WriteAllText avoids Set-Content's encoding behaviour (see AGENTS.md).
$utf8 = [System.Text.UTF8Encoding]::new($false)
[System.IO.File]::WriteAllText($skillPath, $updated, $utf8)

Write-Host "matrix written to SKILL.md ($($entries.Count) methods)" -ForegroundColor Green
