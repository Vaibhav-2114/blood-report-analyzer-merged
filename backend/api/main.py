from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pathlib import Path
import logging
import os
from dotenv import load_dotenv

# Import services
from .services import ocr_service, extract_service, ml_service
from .services.disease_service import predict_diseases

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Blood Report Analyzer API",
    description="Advanced AI-powered blood report analysis API with OCR, ML prediction, and disease diagnosis",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "ok",
        "message": "Blood Report Analyzer Backend API",
        "version": "1.0.0",
        "endpoints": {
            "upload": "/upload-report",
            "analyze": "/analyze",
            "docs": "/docs"
        }
    }

@app.post("/upload-report")
async def upload_report(file: UploadFile = File(...)):
    """
    Upload and process a blood report file (image or PDF).
    
    Returns:
        - text: Extracted text from the report
        - values: Extracted blood test parameters and their values
    """
    try:
        logger.info(f"Processing file: {file.filename}")
        content = await file.read()
        logger.info(f"File size: {len(content)} bytes")
        
        # Extract text using OCR
        text = ocr_service.image_to_text(content)
        logger.info(f"OCR extraction complete, text length: {len(text)}")
        
        # Extract key-value pairs
        values = extract_service.extract_key_values(text)
        logger.info(f"Extracted {len(values)} parameters")
        
        return JSONResponse({
            "status": "success",
            "text": text,
            "values": values,
            "parameters_extracted": len(values)
        })
    except Exception as e:
        logger.error(f"Error in upload_report: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

@app.post("/analyze")
async def analyze(values: dict):
    """
    Analyze blood test parameters.
    
    Returns:
        - comparison: Values compared with normal ranges
        - prediction: Overall health risk assessment
        - diseases: Possible disease predictions
    """
    try:
        if not isinstance(values, dict):
            raise HTTPException(status_code=400, detail="values must be a dictionary")
        
        logger.info(f"Analyzing {len(values)} values")
        
        # Compare with normal ranges
        comparison = ml_service.compare_with_ranges(values)
        
        # Predict health risk
        prediction = ml_service.predict_risk(values)
        
        # Predict possible diseases
        diseases_data = predict_diseases(values)
        
        logger.info(f"Analysis complete: Overall risk = {prediction.get('overall_risk')}")
        
        return JSONResponse({
            "status": "success",
            "comparison": comparison,
            "prediction": prediction,
            "diseases": diseases_data
        })
    except Exception as e:
        logger.error(f"Error in analyze: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error analyzing values: {str(e)}")

@app.post("/full-analysis")
async def full_analysis(file: UploadFile = File(...)):
    """
    Complete analysis pipeline: Upload report -> Extract -> Analyze.
    
    Returns:
        Combined results from extraction and analysis
    """
    try:
        logger.info(f"Starting full analysis for: {file.filename}")
        
        # Step 1: Upload and extract
        content = await file.read()
        text = ocr_service.image_to_text(content)
        values = extract_service.extract_key_values(text)
        
        # Step 2: Analyze
        comparison = ml_service.compare_with_ranges(values)
        prediction = ml_service.predict_risk(values)
        diseases_data = predict_diseases(values)
        
        logger.info("Full analysis completed successfully")
        
        return JSONResponse({
            "status": "success",
            "file_name": file.filename,
            "extracted_text": text,
            "parameters": {
                "extracted": values,
                "comparison": comparison
            },
            "health_assessment": {
                "risk_prediction": prediction,
                "disease_predictions": diseases_data
            }
        })
    except Exception as e:
        logger.error(f"Error in full_analysis: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error in full analysis: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "backend.api.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )
