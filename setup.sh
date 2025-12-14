#!/bin/bash

# Blood Report Analyzer - Linux/macOS Setup Script

echo ""
echo "============================================================"
echo "   Blood Report Analyzer - Setup"
echo "============================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ first"
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "============================================================"
echo "   Setup Complete!"
echo "============================================================"
echo ""
echo "Next steps:"
echo "1. Edit .env file with your API keys (optional)"
echo "2. Run: python3 run.py"
echo "   OR manually run:"
echo "   - Terminal 1: python3 -m uvicorn backend.api.main:app --reload"
echo "   - Terminal 2: streamlit run frontend/app.py"
echo ""
echo "Frontend: http://localhost:8501"
echo "API Docs: http://localhost:8000/docs"
echo ""
