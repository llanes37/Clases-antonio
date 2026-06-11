# Script mínimo para ejecutar el proyecto básico
$ErrorActionPreference = "Stop"

# * Permitir scripts en esta sesión (no cambia política global)
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

if (-not (Test-Path .\.venv)) {
	Write-Host "Creando entorno virtual .venv" -ForegroundColor Cyan
	python -m venv .venv
}

. .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt

$env:FLASK_APP = "miniapp:create_app"
Write-Host "Arrancando Flask en http://127.0.0.1:5000" -ForegroundColor Green
python -m flask run
