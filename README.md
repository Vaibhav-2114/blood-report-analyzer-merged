# Blood Report Analyzer - Merged Project

A comprehensive AI-powered blood report analysis system combining advanced OCR, machine learning, and disease prediction capabilities.

## Features

### 🔍 Text Extraction
- **OCR Processing**: Automatic text extraction from blood report images and PDFs
- **PyPDF2 Integration**: Direct text extraction from PDF documents
- **Image Optimization**: Automatic image preprocessing for better OCR accuracy
- **Multi-format Support**: Handle PNG, JPG, JPEG, and PDF files

### 📊 Data Analysis
- **Parameter Extraction**: Intelligent extraction of blood test parameters
- **Value Normalization**: Automatic parameter name standardization
- **Range Comparison**: Compare extracted values with normal ranges
- **Gender-specific Ranges**: Support for male/female specific normal ranges

### 🤖 Machine Learning
- **Risk Prediction**: ML-based health risk assessment
- **Rule-based Fallback**: Intelligent fallback when ML model unavailable
- **Multiple Risk Levels**: Low, Medium, High risk classifications
- **Confidence Scores**: Probability-based predictions

### 🏥 Disease Diagnosis
- **Disease Prediction**: Analysis of 8 major disease categories
- **Confidence Scoring**: 0-100% confidence ratings for each disease
- **Symptom Mapping**: Associated symptoms for detected conditions
- **Recommendations**: Medical consultation guidelines

### 🎨 User Interface
- **Professional Streamlit Frontend**: Clean, intuitive user interface
- **FastAPI Backend**: High-performance REST API
- **Real-time Analysis**: Instant processing and results
- **Comprehensive Reporting**: Detailed analysis in multiple formats

## Supported Diseases
- Anemia
- Kidney Disease
- Liver Disease
- Infection/Leukemia
- Hemolytic Anemia
- Thrombocytopenia
- Polycythemia

## Blood Parameters Analyzed
- Hemoglobin (Hb)
- WBC (White Blood Cells)
- Platelets (Plt)
- Creatinine
- SGPT/ALT
- SGOT/AST
- Bilirubin

## System Architecture

```
blood-report-analyzer-merged/
├── backend/
│   ├── api/
│   │   ├── main.py                 # FastAPI application
│   │   ├── services/
│   │   │   ├── ocr_service.py       # OCR and text extraction
│   │   │   ├── extract_service.py   # Parameter extraction
│   │   │   ├── ml_service.py        # ML models and predictions
│   │   │   └── disease_service.py   # Disease diagnosis
│   │   └── utils/
│   │       ├── normal_ranges.json   # Normal value ranges
│   │       └── mapping.json         # Parameter name mapping
│   └── crews/                        # (Optional) CrewAI agents for advanced analysis
├── frontend/
│   └── app.py                       # Streamlit web application
├── ml_model/
│   └── train_model.py               # ML model training script
├── requirements.txt                  # Python dependencies
├── pyproject.toml                    # Poetry configuration
├── .env.example                      # Environment template
└── README.md                         # This file
```

## Installation & Setup

### Prerequisites
- **Python**: 3.8 or higher
- **Windows/Linux/macOS**: All platforms supported
- **Tesseract-OCR** (Optional, for enhanced OCR):
  - **Windows**: Download from https://github.com/UB-Mannheim/tesseract/wiki
  - **Linux**: `sudo apt-get install tesseract-ocr`
  - **macOS**: `brew install tesseract`

### Step 1: Clone/Copy the Project
```bash
# If you have the project as a folder
cd blood-report-analyzer-merged
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
# Using pip (recommended)
pip install -r requirements.txt

# Or using Poetry
poetry install
```

### Step 4: Configure Environment Variables
```bash
# Copy the example file
cp .env.example .env

# Edit .env with your API keys (optional)
# GEMINI_API_KEY=your_key_here
# GROK_API_KEY=your_key_here
```

### Step 5: Run the Application

**Terminal 1 - Start the Backend API:**
```bash
python -m uvicorn backend.api.main:app --reload --host 127.0.0.1 --port 8000
```

**Terminal 2 - Start the Frontend:**
```bash
streamlit run frontend/app.py
```

The application will open automatically at: **http://localhost:8501**

**API Documentation** available at: **http://localhost:8000/docs**

## Usage Guide

### Basic Workflow
1. **Upload Report**: Select a blood report image or PDF from your device
2. **Extract Text**: Click "Extract Text from Report" to process the file
3. **Review Data**: Check the extracted parameters and correct any OCR errors if needed
4. **Analyze**: Click "Analyze Report" to generate comprehensive analysis
5. **Review Results**: Examine the parameter comparison, risk assessment, and disease predictions

### Advanced Features

#### Parameter Editing
- Edit extracted values before analysis
- Correct OCR errors manually
- Override automatic extractions

#### Result Interpretation
- **Parameter Comparison Tab**: See how your values compare to normal ranges
- **Risk Assessment Tab**: Understand your overall health risk level
- **Disease Analysis Tab**: Learn about possible conditions based on your results
- **Summary Report Tab**: Get an overview of the complete analysis

#### Export & Sharing
- Take screenshots of analysis results
- Share findings with healthcare providers
- Print comprehensive reports

## API Endpoints

### Health Check
```
GET /
Response: Status and available endpoints
```

### Upload and Extract
```
POST /upload-report
Input: File (image or PDF)
Response: {
    "status": "success",
    "text": "extracted text",
    "values": {"parameter": value, ...},
    "parameters_extracted": count
}
```

### Analyze Parameters
```
POST /analyze
Input: {"parameter": value, ...}
Response: {
    "status": "success",
    "comparison": {...},
    "prediction": {...},
    "diseases": {...}
}
```

### Full Analysis (One-Step)
```
POST /full-analysis
Input: File (image or PDF)
Response: Complete analysis results
```

## Configuration

### Tesseract Path (Windows)
Edit `backend/api/services/ocr_service.py` if Tesseract is installed elsewhere:
```python
TESSERACT_PATH = r"C:\Your\Path\To\tesseract.exe"
```

### API Port
Edit backend startup command:
```bash
python -m uvicorn backend.api.main:app --reload --port 8080
```

## Troubleshooting

### OCR Issues
**Problem**: "Tesseract is not installed"
- **Solution**: Install Tesseract-OCR from https://github.com/UB-Mannheim/tesseract/wiki

**Problem**: Poor text extraction quality
- **Solution**: Ensure report image is clear and well-lit, minimum 200 DPI

### Backend Connection
**Problem**: "Cannot connect to backend"
- **Solution**: Ensure backend is running on http://127.0.0.1:8000
- Check firewall settings allow port 8000

### API Key Issues
**Problem**: "API key not configured"
- **Solution**: Gemini API is optional. Add key to .env for advanced analysis features

### Large File Processing
**Problem**: "Timeout error with large PDFs"
- **Solution**: The system processes first 10 pages max. Try splitting large PDFs

## Performance Tips

1. **Image Quality**: Use clear, well-scanned medical report images
2. **File Size**: Keep file sizes under 50MB for faster processing
3. **Network**: Run backend and frontend on same machine for best performance
4. **System Resources**: Close unnecessary applications for faster OCR

## Medical Disclaimer

⚠️ **IMPORTANT**: This application provides informational analysis only and is **NOT a substitute** for professional medical advice, diagnosis, or treatment. 

- Results are for educational and informational purposes only
- Always consult qualified healthcare professionals for diagnosis
- This tool should not be used for self-diagnosis
- Seek immediate medical attention for serious health concerns
- Blood test interpretation requires clinical context and professional judgment

## Project Sources

This is a merged project combining:
- **BLOOD_TEST_ANALYSIS**: AI-driven medical report analysis with Streamlit
- **blood-report-advanced**: FastAPI backend with OCR, ML, and disease detection

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## Support & Contact

For issues, questions, or suggestions, please open an issue in the project repository.

---

**Version**: 1.0.0  
**Last Updated**: December 2024  
**Python Requirement**: 3.8+
