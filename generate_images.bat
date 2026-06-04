@echo off
REM ══════════════════════════════════════════════════════════════
REM Generador de imágenes para posts de LinkedIn - FLUX.1 [schnell]
REM ══════════════════════════════════════════════════════════════

cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo [ERROR] Entorno virtual no encontrado.
    echo Ejecuta primero: python -m venv .venv
    goto :eof
)

echo.
echo ════════════════════════════════════════════════════════════
echo   Generador de Imagenes - LinkedIn Content
echo ════════════════════════════════════════════════════════════
echo.

if "%~1"=="" (
    echo Uso:
    echo   generate_images.bat list                    - Listar posts
    echo   generate_images.bat generate POST.md        - Generar imagen para un post
    echo   generate_images.bat generate-all            - Generar todas las imagenes faltantes
    echo   generate_images.bat generate-all --force    - Regenerar todas
    goto :eof
)

.venv\Scripts\python.exe generate_images.py %*
