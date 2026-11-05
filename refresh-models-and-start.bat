@echo off
cd /d "%~dp0"
py update-model-manifest.py
start "" http://localhost:8000
py serve.py
