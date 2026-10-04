$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath (Join-Path $PSScriptRoot 'frontend')
if (-not (Test-Path -LiteralPath 'node_modules')) {
    pnpm install
}
pnpm run dev
