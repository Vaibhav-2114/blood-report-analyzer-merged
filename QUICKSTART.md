# Blood Report Analyzer - Merged Project

## Quick Start Guide

### 1. Setup (First Time)
```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Linux/macOS

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Application
```bash
# Terminal 1: Start Backend API
python -m uvicorn backend.api.main:app --reload --host 127.0.0.1 --port 8000

# Terminal 2: Start Frontend (in new terminal)
streamlit run frontend/app.py
```

### 3. Access Application
- **Web Interface**: http://localhost:8501
- **API Docs**: http://localhost:8000/docs

## Project Structure

```
├── backend/
│   ├── api/
│   │   ├── main.py              # FastAPI server
│   │   ├── services/            # Analysis modules
│   │   │   ├── ocr_service.py
│   │   │   ├── extract_service.py
│   │   │   ├── ml_service.py
│   │   │   └── disease_service.py
│   │   └── utils/               # Config files
│   │       ├── normal_ranges.json
│   │       └── mapping.json
│   └── crews/                   # AI agents (optional)
├── frontend/
│   └── app.py                   # Streamlit UI
├── ml_model/
│   └── train_model.py          # ML training
├── requirements.txt             # Dependencies
└── README.md                    # Full documentation
```

## Key Features

✅ **OCR Text Extraction** - Images & PDFs  
✅ **Parameter Detection** - Automatic blood test data extraction  
✅ **Range Comparison** - Compare with normal values  
✅ **Disease Diagnosis** - Predict possible conditions  
✅ **Risk Assessment** - Health risk prediction  
✅ **Professional UI** - Clean, intuitive interface  

## Supported Blood Parameters

| Parameter | Normal Range |
|-----------|--------------|
| Hemoglobin | 12-17 g/dL |
| WBC | 4,000-11,000 cells/μL |
| Platelets | 150,000-450,000 cells/μL |
| Creatinine | 0.6-1.3 mg/dL |
| SGPT/ALT | 7-56 U/L |
| SGOT/AST | 10-40 U/L |
| Bilirubin | 0.1-1.2 mg/dL |

## Detected Diseases

🔴 Anemia  
🔴 Kidney Disease  
🔴 Liver Disease  
🔴 Infection/Leukemia  
🔴 Hemolytic Anemia  
🔴 Thrombocytopenia  
🔴 Polycythemia  

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Tesseract not found | Install from https://github.com/UB-Mannheim/tesseract/wiki |
| Cannot connect to backend | Ensure port 8000 is not in use |
| Poor OCR results | Use clearer, higher DPI images |
| File too large | Keep files under 50MB, split large PDFs |

## Important Disclaimer

⚠️ This tool provides **informational analysis only**. It is **NOT a medical diagnostic tool**. Always consult qualified healthcare professionals for accurate diagnosis and treatment.

---

For full documentation, see README.md
