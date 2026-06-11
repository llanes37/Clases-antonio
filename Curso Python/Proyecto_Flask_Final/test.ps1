# * Ejecutar tests con pytest dentro del venv
$ErrorActionPreference = "Stop"

if (-not (Test-Path .\.venv)) {
  Write-Host "Primero ejecuta ./run.ps1 para crear el venv" -ForegroundColor Yellow
  exit 1
}

. .\.venv\Scripts\Activate.ps1
pytest -q
