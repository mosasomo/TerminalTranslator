@echo off
setlocal

:: Get the current directory where the script is located
set "PROJECT_DIR=%~dp0"
set "PYTHON_EXE=python"

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python was not found in your PATH. Please install Python first.
    pause
    exit /b 1
)

:: Create the trans.bat content
set "SHORTCUT_PATH=%LOCALAPPDATA%\Microsoft\WindowsApps\trans.bat"
echo @echo off > "%SHORTCUT_PATH%"
echo "%PYTHON_EXE%" "%PROJECT_DIR%translate.py" %%* >> "%SHORTCUT_PATH%"

echo.
echo Setup Complete!
echo You can now use the 'trans' command from any terminal.
echo.
pause
