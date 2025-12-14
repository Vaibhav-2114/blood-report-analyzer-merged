Welcome to **Blood Report Analyzer** - A Merged Project

## 🎯 Start Here

### 1️⃣ **First Time Setup?**
   - Read: [`QUICKSTART.md`](QUICKSTART.md)
   - Run: `setup.bat` (Windows) or `bash setup.sh` (Linux/macOS)

### 2️⃣ **Want Full Details?**
   - Read: [`README.md`](README.md)
   - See: [`MERGE_SUMMARY.md`](MERGE_SUMMARY.md)

### 3️⃣ **Ready to Run?**
   - Execute: `python run.py`
   - Or manually start backend and frontend (see QUICKSTART.md)

---

## 📚 Documentation Map

| Document | Purpose |
|----------|---------|
| **README.md** | Complete project documentation with all features, setup, and troubleshooting |
| **QUICKSTART.md** | Fast setup guide and quick reference |
| **MERGE_SUMMARY.md** | Details about what was merged and how |
| **This File** | Navigation guide |

---

## 🚀 Project Features

### Core Functionality
✅ **OCR Text Extraction** - Extract text from blood report images & PDFs  
✅ **Parameter Detection** - Automatically identify blood test values  
✅ **Range Comparison** - Compare with normal medical ranges  
✅ **Disease Diagnosis** - Predict possible health conditions  
✅ **Risk Assessment** - Evaluate overall health risk level  
✅ **Professional Reports** - Generate comprehensive analysis  

### Technology Stack
- **Backend**: FastAPI + Python
- **Frontend**: Streamlit
- **OCR**: Tesseract + pytesseract
- **PDF Processing**: PyPDF2 + pdf2image
- **ML**: Scikit-learn
- **Data**: Pandas

### Supported Blood Tests
- Hemoglobin (Hb)
- White Blood Cells (WBC)
- Platelets (Plt)
- Creatinine
- SGPT/ALT
- SGOT/AST
- Bilirubin

---

## 📁 Project Structure

```
blood-report-analyzer-merged/
│
├── backend/                      # FastAPI backend server
│   └── api/
│       ├── main.py              # Main API server
│       ├── services/            # Analysis modules
│       │   ├── ocr_service.py
│       │   ├── extract_service.py
│       │   ├── ml_service.py
│       │   └── disease_service.py
│       └── utils/               # Configuration & mappings
│           ├── normal_ranges.json
│           └── mapping.json
│
├── frontend/                     # Streamlit web interface
│   └── app.py                   # Main frontend app
│
├── ml_model/                     # Machine learning
│   └── train_model.py
│
├── requirements.txt              # Python dependencies
├── pyproject.toml               # Poetry configuration
├── .env.example                 # API keys template
├── run.py                       # One-click launcher
├── setup.bat / setup.sh         # Setup scripts
│
└── Documentation
    ├── README.md                # Full documentation
    ├── QUICKSTART.md            # Quick start guide
    ├── MERGE_SUMMARY.md         # Merge details
    └── LICENSE                  # MIT License
```

---

## 🎬 Quick Start

### Step 1: Setup (First Time Only)
```bash
# Windows
setup.bat

# Linux/macOS
bash setup.sh
```

### Step 2: Run the Application
```bash
python run.py
```

### Step 3: Access
- **Web App**: http://localhost:8501
- **API Docs**: http://localhost:8000/docs

---

## 📖 How to Use

1. **Upload** a blood report (image or PDF)
2. **Extract** text using OCR
3. **Review** extracted parameters
4. **Analyze** to get results
5. **View** comprehensive analysis

---

## 🔧 API Endpoints

```
GET  /              - Health check
POST /upload-report - Extract text from file
POST /analyze       - Analyze blood parameters
POST /full-analysis - One-step analysis
```

See `README.md` for detailed API documentation.

---

## ⚠️ Important Medical Disclaimer

**This tool provides informational analysis only** and is NOT a substitute for professional medical advice. Always consult qualified healthcare professionals for diagnosis and treatment.

---

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| Tesseract not found | Install from https://github.com/UB-Mannheim/tesseract/wiki |
| Port already in use | Check if services are already running or use different port |
| Cannot extract text | Ensure image is clear and well-scanned |
| Backend not responding | Verify backend is running on http://127.0.0.1:8000 |

See `README.md` for more troubleshooting tips.

---

## 📧 Support

For issues or questions:
1. Check documentation (README.md, QUICKSTART.md)
2. Review MERGE_SUMMARY.md for technical details
3. Check error messages in terminal/console

---

## 📝 What's Included

### From BLOOD_TEST_ANALYSIS-main
- Streamlit UI foundation
- Multi-LLM support framework
- General medical report analysis

### From blood-report-advanced  
- FastAPI backend architecture
- Advanced OCR services
- Parameter extraction engine
- Disease diagnosis engine
- Professional UI components
- ML prediction models

### New Enhancements
- Unified architecture
- Combined best features from both
- Comprehensive error handling
- Professional documentation
- Easy setup scripts
- Deployment ready

---

## 🎓 Features Comparison

| Feature | Status | Notes |
|---------|--------|-------|
| Text Extraction | ✅ Complete | PyPDF2 + Tesseract OCR |
| Parameter Detection | ✅ Complete | 7 blood test parameters |
| Range Comparison | ✅ Complete | Gender-specific ranges |
| Disease Diagnosis | ✅ Complete | 7 disease categories |
| Risk Prediction | ✅ Complete | ML + Rule-based fallback |
| Professional UI | ✅ Complete | Streamlit with custom CSS |
| API Documentation | ✅ Complete | Interactive Swagger UI |
| Setup Scripts | ✅ Complete | Windows + Linux/macOS |
| Medical Compliance | ✅ Complete | Disclaimers included |

---

## 🚀 Next Steps

1. **Read QUICKSTART.md** for immediate setup
2. **Run setup script** to install dependencies
3. **Execute run.py** to start the application
4. **Visit http://localhost:8501** in your browser
5. **Upload a blood report** to test the system

---

## 📞 Quick Links

- **Full Documentation**: [README.md](README.md)
- **Quick Setup**: [QUICKSTART.md](QUICKSTART.md)
- **Project Details**: [MERGE_SUMMARY.md](MERGE_SUMMARY.md)
- **API Docs** (after running): http://localhost:8000/docs

---

**Blood Report Analyzer v1.0**  
*Successfully Merged & Ready to Use*

Last Updated: December 2024
