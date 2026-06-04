@echo off
REM ══════════════════════════════════════════════════════════════
REM Iniciar servidor LinkedIn Content y abrir en navegador
REM ══════════════════════════════════════════════════════════════

cd /d "%~dp0"

echo.
echo ════════════════════════════════════════════════════════════
echo   LinkedIn Content Panel
echo ════════════════════════════════════════════════════════════
echo.
echo   Iniciando servidor en http://localhost:8765
echo.

REM Iniciador servidor en ventana oculta
start /B python server.py

REM Esperar a que el servidor inicie
timeout /t 3 /nobreak >nul

REM Abrir en navegador
start http://localhost:8765

echo   Servidor iniciado. Abriendo navegador...
echo   Cierra esta ventana para detener el servidor.
echo.
pause
