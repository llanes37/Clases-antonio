$ErrorActionPreference = "Stop"

if (-not (Test-Path ".venv")) {
    python -m venv .venv
}

. .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if (-not (Test-Path ".env")) {
    Copy-Item .env.example .env
}

$env:FLASK_APP = "app:create_app"
$env:APP_ENV = "development"

Write-Host "Iniciando Proyecto_Flask_Auth_Migraciones en http://127.0.0.1:5000/"
python -m flask run
