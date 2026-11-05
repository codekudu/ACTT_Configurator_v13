@echo off
cd /d "%~dp0"
py update-model-manifest.py
echo Model index updated. Refresh the browser with Ctrl+F5.
pause
