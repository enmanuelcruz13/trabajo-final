@echo off
echo ===================================================
echo 🚀 SUBIR CINEGLOW A GITHUB
echo ===================================================
echo.
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ ERROR: Git no esta instalado o no esta en el PATH.
    echo Por favor, descarga e instala Git desde: https://git-scm.com/
    echo despues de instalarlo, vuelve a ejecutar este archivo.
    echo.
    pause
    exit /b
)

echo ✅ Git detectado correctamente.
echo.
echo 📦 Inicializando y subiendo cambios...
git init
git add .
git commit -m "feat: integrar supabase, limpiar series y agregar chips de categoria premium"
git branch -M main
git remote add origin https://github.com/enmanuelcruz13/trabajo-final
git push -u origin main --force

echo.
echo ===================================================
echo 🎉 ¡Proyecto subido con exito a GitHub!
echo ===================================================
pause
