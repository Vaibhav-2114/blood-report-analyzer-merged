# Blood Report Analyzer - Windows Setup Script

@echo off
echo.
echo ============================================================
echo   Blood Report Analyzer - Setup
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install requirements
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo ============================================================
echo   Setup Complete!
echo ============================================================
echo.
echo Next steps:
echo 1. Edit .env file with your API keys (optional)
echo 2. Run: python run.py
echo    OR manually run:
echo    - Terminal 1: python -m uvicorn backend.api.main:app --reload
echo    - Terminal 2: streamlit run frontend/app.py
echo.
echo Frontend: http://localhost:8501
echo API Docs: http://localhost:8000/docs
echo.
pause
