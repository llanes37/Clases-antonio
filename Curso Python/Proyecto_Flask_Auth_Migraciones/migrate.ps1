$ErrorActionPreference = "Stop"

. .\.venv\Scripts\Activate.ps1
$env:FLASK_APP = "app:create_app"
$env:APP_ENV = "development"

Write-Host "Comandos sugeridos:"
Write-Host "  python -m flask db init"
Write-Host "  python -m flask db migrate -m `"init modelos auth`""
Write-Host "  python -m flask db upgrade"
