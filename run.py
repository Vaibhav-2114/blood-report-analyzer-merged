#!/usr/bin/env python3
"""
Blood Report Analyzer - Run Script
This script helps users easily start both backend and frontend
"""

import subprocess
import time
import os
import sys
import platform

def print_header():
    print("\n" + "="*60)
    print("🏥 Blood Report Analyzer - Combined Project")
    print("="*60 + "\n")

def print_instructions():
    print("📋 Setup Instructions:")
    print("-" * 60)
    print("1. If first time, install dependencies:")
    print("   pip install -r requirements.txt\n")
    print("2. This script will start both backend and frontend")
    print("3. Frontend will open automatically at http://localhost:8501")
    print("4. API documentation at http://localhost:8000/docs")
    print("-" * 60 + "\n")

def start_backend():
    """Start FastAPI backend"""
    print("🚀 Starting Backend API (port 8000)...")
    
    if platform.system() == "Windows":
        cmd = ["python", "-m", "uvicorn", "backend.api.main:app", "--reload", "--host", "127.0.0.1", "--port", "8000"]
    else:
        cmd = ["python3", "-m", "uvicorn", "backend.api.main:app", "--reload", "--host", "127.0.0.1", "--port", "8000"]
    
    process = subprocess.Popen(cmd)
    print("✅ Backend started (PID: {})".format(process.pid))
    return process

def start_frontend():
    """Start Streamlit frontend"""
    print("\n🎨 Starting Frontend (Streamlit)...")
    
    if platform.system() == "Windows":
        cmd = ["python", "-m", "streamlit", "run", "frontend/app.py"]
    else:
        cmd = ["python3", "-m", "streamlit", "run", "frontend/app.py"]
    
    subprocess.Popen(cmd)
    print("✅ Frontend started")

def main():
    print_header()
    print_instructions()
    
    try:
        print("⏳ Please wait while services are starting...\n")
        
        backend_process = start_backend()
        time.sleep(3)  # Give backend time to start
        start_frontend()
        
        print("\n" + "="*60)
        print("✅ All services started successfully!")
        print("="*60)
        print("\n📱 Frontend: http://localhost:8501")
        print("📚 API Docs: http://localhost:8000/docs\n")
        print("Press Ctrl+C to stop all services\n")
        
        # Keep the script running
        backend_process.wait()
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Stopping services...")
        backend_process.terminate()
        print("✅ Services stopped")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
