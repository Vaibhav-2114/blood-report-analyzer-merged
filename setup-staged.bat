@echo off
echo.
echo ============================================================
echo   Blood Report Analyzer - Staged Setup
echo ============================================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

REM Create venv if missing
echo Creating virtual environment (if not exists)...
if not exist venv (
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Upgrading pip, setuptools, wheel...
python -m pip install --upgrade pip setuptools wheel

echo Installing core dependencies (faster, excludes heavy langchain/crewai)...
python -m pip install --no-cache-dir -r requirements-core.txt

echo Core install finished.
echo Now you can optionally install advanced LLM packages (langchain, crewai).
echo To attempt the advanced install, run the following commands manually:
echo ^> python -m pip install --no-cache-dir "SQLAlchemy<3,>=1.4" -v
echo ^> python -m pip install --no-cache-dir langchain langchain-google-genai langchain-community crewai -v
echo If SQLAlchemy install hangs, try clearing pip cache: python -m pip cache purge

echo ============================================================
echo Staged setup complete. If you want everything installed automatically, run: pip install -r requirements.txt
echo ============================================================
echo.
pause
