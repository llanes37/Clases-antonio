# * Script de ayuda: crea venv, instala dependencias y arranca Flask
# ! Ejecuta este script desde la carpeta Proyecto_Flask_Final

$ErrorActionPreference = "Stop"

# 1) Crear venv si no existe
if (-not (Test-Path .\.venv)) {
  Write-Host "Creando entorno virtual .venv" -ForegroundColor Cyan
  python -m venv .venv
}

# 2) Activar venv
Write-Host "Activando entorno virtual" -ForegroundColor Cyan
. .\.venv\Scripts\Activate.ps1

# 3) Instalar dependencias
Write-Host "Instalando requirements" -ForegroundColor Cyan
pip install --upgrade pip
pip install -r requirements.txt

# 4) Variables de entorno para la sesión
$env:FLASK_APP = "app:create_app"
$env:APP_ENV = "development"

# 5) Crear DB si no existe (se auto-crea al iniciar)

# 6) Arrancar servidor
Write-Host "Arrancando Flask en http://127.0.0.1:5000" -ForegroundColor Green
python -m flask run
