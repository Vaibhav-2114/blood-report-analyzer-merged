import streamlit as st
import requests
import json
import pandas as pd
from PIL import Image
import io
import time
import os
from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Blood Report Analyzer - Advanced",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "Advanced AI-powered Blood Report Analysis System v1.0\nCombined from BLOOD_TEST_ANALYSIS and blood-report-advanced"
    }
)

# Custom CSS for professional styling
st.markdown("""
<style>
    /* Main container */
    .main {
        padding: 2rem;
    }
    
    /* Header styling */
    h1 {
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
        font-size: 2.5rem;
        font-weight: 700;
    }
    
    h2 {
        color: #2c3e50;
        border-bottom: 3px solid #1f77b4;
        padding-bottom: 0.5rem;
        margin-top: 1.5rem;
    }
    
    /* Status badges */
    .status-normal {
        background-color: #d4edda;
        color: #155724;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        font-weight: bold;
        display: inline-block;
        margin: 0.25rem;
    }
    
    .status-low {
        background-color: #fff3cd;
        color: #856404;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        font-weight: bold;
        display: inline-block;
        margin: 0.25rem;
    }
    
    .status-high {
        background-color: #f8d7da;
        color: #721c24;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        font-weight: bold;
        display: inline-block;
        margin: 0.25rem;
    }
    
    .disclaimer {
        background-color: #ffeaa7;
        border-left: 4px solid #fdcb6e;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
        color: #664d03;
    }
    
    .success-box {
        background-color: #d4edda;
        border-left: 4px solid #28a745;
        padding: 1rem;
        border-radius: 5px;
        color: #155724;
    }
    
    .warning-box {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 1rem;
        border-radius: 5px;
        color: #856404;
    }
    
    .danger-box {
        background-color: #f8d7da;
        border-left: 4px solid #dc3545;
        padding: 1rem;
        border-radius: 5px;
        color: #721c24;
    }
</style>
""", unsafe_allow_html=True)

# API Configuration
try:
    API_URL = st.secrets.get("api_url", "http://127.0.0.1:8000")
except:
    API_URL = "http://127.0.0.1:8000"

# Initialize session state
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = None
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None
if 'extracted_text' not in st.session_state:
    st.session_state.extracted_text = ""

# Helper function
def extract_text_from_session():
    """Extract parameter values from session state"""
    params = {}
    for key in st.session_state:
        if key.startswith("param_"):
            param_name = key.replace("param_", "")
            params[param_name] = st.session_state[key]
    return params

# Title
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.title("🏥 Blood Report Analyzer")
    st.markdown("<p style='text-align: center; color: #666; font-size: 1.1rem;'>Advanced AI-Powered Analysis System</p>", unsafe_allow_html=True)

# Medical Disclaimer
st.markdown("""
<div class='disclaimer'>
<b>⚠️ IMPORTANT DISCLAIMER:</b> This application provides informational analysis only and is NOT a substitute for professional medical advice, diagnosis, or treatment. 
Always consult qualified healthcare professionals for accurate medical diagnosis and treatment decisions. Results are for informational purposes only.
</div>
""", unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.markdown("## 📁 Report Upload & Analysis")
    st.markdown("---")
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Upload blood report file",
        type=['png', 'jpg', 'jpeg', 'pdf'],
        help="Supported formats: PNG, JPG, JPEG, PDF (Max 50MB)"
    )
    
    st.markdown("---")
    st.markdown("### ℹ️ How to Use")
    st.markdown("""
    1. **Upload**: Select your blood report image or PDF
    2. **Review**: Check the extracted text
    3. **Edit** (Optional): Correct any OCR errors
    4. **Analyze**: Generate comprehensive analysis
    5. **Review Results**: Check parameters, risks, and recommendations
    """)
    
    st.markdown("---")
    st.markdown("### 🔧 System Status")
    
    # Check backend connection
    try:
        response = requests.get(f"{API_URL}/", timeout=5)
        if response.status_code == 200:
            st.success("✅ Backend: Connected")
        else:
            st.error("❌ Backend: Error")
    except:
        st.error("❌ Backend: Not Reachable")
    
    st.markdown("---")
    st.markdown("### 📚 Reference Values")
    st.markdown("""
    **Normal Ranges** (typical values):
    - **Hemoglobin**: 12-17 g/dL
    - **WBC**: 4,000-11,000 cells/μL
    - **Platelets**: 150,000-450,000 cells/μL
    - **Creatinine**: 0.6-1.3 mg/dL
    - **SGPT/ALT**: 7-56 U/L
    - **SGOT/AST**: 10-40 U/L
    - **Bilirubin**: 0.1-1.2 mg/dL
    """)

# Main content
if uploaded_file is not None:
    st.session_state.uploaded_file = uploaded_file
    bytes_data = uploaded_file.read()
    
    # File validation
    if len(bytes_data) == 0:
        st.error("❌ Error: Uploaded file is empty")
    elif len(bytes_data) > 50 * 1024 * 1024:
        st.error("❌ Error: File size exceeds 50MB limit")
    else:
        # Step 1: Display file preview
        st.markdown("### 📋 Report Preview")
        col1, col2 = st.columns([2, 1])
        
        with col1:
            try:
                img = Image.open(io.BytesIO(bytes_data))
                st.image(img, use_column_width=True, caption="Uploaded Report Image")
            except Exception as e:
                st.info(f"ℹ️ Image preview not available (PDF detected or unsupported format)")
        
        # Step 2: Process the file
        if st.button("📤 Extract Text from Report", use_container_width=True, key="extract_btn"):
            with st.spinner("🔄 Extracting text using OCR..."):
                try:
                    files = {"file": (uploaded_file.name, bytes_data, uploaded_file.type)}
                    response = requests.post(
                        f"{API_URL}/upload-report",
                        files=files,
                        timeout=120
                    )
                    
                    if response.status_code == 200:
                        data = response.json()
                        st.session_state.extracted_text = data.get("text", "")
                        
                        st.success(f"✅ Extraction Complete! {data.get('parameters_extracted', 0)} parameters found.")
                        
                        # Show extracted text
                        with st.expander("📝 View Extracted Text (Raw OCR Output)", expanded=False):
                            st.text_area(
                                "Extracted text from report:",
                                st.session_state.extracted_text,
                                height=200,
                                disabled=True
                            )
                        
                        # Show initial parameters
                        extracted_params = data.get("values", {})
                        if extracted_params:
                            st.markdown("### ✏️ Extracted Blood Parameters")
                            st.markdown("Review and edit parameters below if needed:")
                            
                            col1, col2, col3 = st.columns(3)
                            cols = [col1, col2, col3]
                            
                            # Store edited values in session state
                            for i, (param, value) in enumerate(extracted_params.items()):
                                with cols[i % 3]:
                                    st.session_state[f"param_{param}"] = st.number_input(
                                        param,
                                        value=float(value),
                                        step=0.1,
                                        format="%.2f",
                                        key=f"input_{param}"
                                    )
                    else:
                        st.error(f"❌ Backend error: {response.status_code} - {response.text}")
                
                except requests.exceptions.Timeout:
                    st.error("❌ Request timeout. The file may be too large. Please try a smaller file.")
                except requests.exceptions.ConnectionError:
                    st.error("❌ Cannot connect to backend. Make sure the API is running on http://127.0.0.1:8000")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        
        # Step 3: Analyze
        if st.session_state.extracted_text and st.button("🔍 Analyze Report", use_container_width=True, key="analyze_btn"):
            with st.spinner("🔄 Analyzing blood parameters and predicting diseases..."):
                try:
                    # Prepare payload with edited values
                    payload = {}
                    extracted_params = extract_text_from_session()
                    
                    # Use edited values if available, otherwise use extracted
                    if extracted_params:
                        for param in extracted_params.keys():
                            payload[param] = st.session_state.get(f"param_{param}", extracted_params[param])
                    
                    if not payload:
                        st.warning("⚠️ No parameters found to analyze. Please extract text first.")
                    else:
                        response = requests.post(
                            f"{API_URL}/analyze",
                            json=payload,
                            timeout=30
                        )
                        
                        if response.status_code == 200:
                            st.session_state.analysis_results = response.json()
                            st.success("✅ Analysis Complete!")
                        else:
                            st.error(f"❌ Analysis error: {response.status_code}")
                
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

# Display results
if st.session_state.analysis_results:
    results = st.session_state.analysis_results
    st.markdown("---")
    st.markdown("## 📊 Analysis Results")
    
    # Create tabs for organized display
    tab1, tab2, tab3, tab4 = st.tabs([
        "📋 Parameter Comparison",
        "⚠️ Risk Assessment",
        "🏥 Disease Analysis",
        "📄 Summary Report"
    ])
    
    # Tab 1: Parameter Comparison
    with tab1:
        st.markdown("### Blood Parameter Analysis")
        comparison = results.get("comparison", {})
        
        if comparison:
            # Create dataframe for display
            comp_data = []
            for param, info in comparison.items():
                comp_data.append({
                    "Parameter": param,
                    "Value": f"{info.get('value')} {info.get('unit', '')}",
                    "Status": info.get("status", "Unknown"),
                    "Normal Range": f"{info.get('normal_range', ['N/A', 'N/A'])[0]}-{info.get('normal_range', ['N/A', 'N/A'])[1]} {info.get('unit', '')}"
                })
            
            df = pd.DataFrame(comp_data)
            
            # Color coding function
            def color_status(val):
                if val == "Normal":
                    return 'background-color: #d4edda; color: #155724;'
                elif val == "Low":
                    return 'background-color: #fff3cd; color: #856404;'
                elif val == "High":
                    return 'background-color: #f8d7da; color: #721c24;'
                else:
                    return 'background-color: #e2e3e5; color: #383d41;'
            
            styled_df = df.style.applymap(color_status, subset=['Status'])
            st.dataframe(styled_df, use_container_width=True, hide_index=True)
            
            # Statistics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                normal_count = sum(1 for p in comparison.values() if p.get("status") == "Normal")
                st.metric("Normal", normal_count)
            with col2:
                low_count = sum(1 for p in comparison.values() if p.get("status") == "Low")
                st.metric("Low", low_count)
            with col3:
                high_count = sum(1 for p in comparison.values() if p.get("status") == "High")
                st.metric("High", high_count)
            with col4:
                unknown_count = sum(1 for p in comparison.values() if p.get("status") == "Unknown")
                st.metric("Unknown", unknown_count)
        else:
            st.info("No parameters to display")
    
    # Tab 2: Risk Assessment
    with tab2:
        st.markdown("### Overall Health Risk Assessment")
        prediction = results.get("prediction", {})
        
        # Risk display
        col1, col2, col3 = st.columns(3)
        
        overall_risk = prediction.get("overall_risk", "Unknown")
        risk_color_map = {
            "Low": ("#28a745", "🟢 LOW RISK"),
            "Medium": ("#ffc107", "🟡 MEDIUM RISK"),
            "High": ("#dc3545", "🔴 HIGH RISK"),
            "Unknown": ("#6c757d", "❓ UNKNOWN")
        }
        color, display_text = risk_color_map.get(overall_risk, ("#6c757d", "❓ UNKNOWN"))
        
        with col1:
            st.markdown(f"""
            <div style='background: {color}; padding: 2.5rem; border-radius: 10px; color: white; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
                <h2>{display_text}</h2>
                <p>Overall Health Status</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            risks = prediction.get("risks", [])
            risk_html = '<br>'.join([f'• {risk}' for risk in risks]) if risks else '✅ No specific risks identified'
            st.markdown(f"""
            <div style='background: #f8f9fa; padding: 2rem; border-radius: 10px; border-left: 4px solid #007bff; color: #333;'>
                <h3 style='color: #333;'>🔍 Identified Risks</h3>
                <p style='color: #333;'>{risk_html}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            recommendation = {
                "Low": "✅ Regular monitoring recommended",
                "Medium": "⚠️ Medical consultation advised",
                "High": "🚨 Immediate medical attention needed"
            }.get(overall_risk, "ℹ️ Consult healthcare professional")
            
            st.markdown(f"""
            <div style='background: #e8f5e9; padding: 2rem; border-radius: 10px; border-left: 4px solid #4caf50; color: #2e7d32;'>
                <h3 style='color: #2e7d32;'>📌 Action Required</h3>
                <p style='color: #2e7d32;'>{recommendation}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Tab 3: Disease Analysis
    with tab3:
        st.markdown("### Possible Disease Predictions")
        diseases_result = results.get("diseases", {})
        summary = diseases_result.get("summary", "")
        
        # Summary alert
        if summary:
            if "High risk" in summary or "Immediate" in summary:
                st.markdown(f'<div class="danger-box">{summary}</div>', unsafe_allow_html=True)
            elif "possible" in summary.lower():
                st.markdown(f'<div class="warning-box">{summary}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="success-box">{summary}</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        possible_diseases = diseases_result.get("possible_diseases", {})
        
        if possible_diseases:
            st.markdown(f"**Found {len(possible_diseases)} potential condition(s):**")
            
            for disease_name, disease_data in possible_diseases.items():
                confidence = disease_data.get('confidence', 0)
                risk_level = disease_data.get('risk_level', 'Unknown')
                
                # Color code based on confidence
                if confidence >= 80:
                    color = "#f8d7da"
                    icon = "🔴"
                    border_color = "#dc3545"
                elif confidence >= 60:
                    color = "#fff3cd"
                    icon = "🟡"
                    border_color = "#ffc107"
                else:
                    color = "#d1ecf1"
                    icon = "🔵"
                    border_color = "#17a2b8"
                
                with st.expander(f"{icon} {disease_name} — {confidence}% Confidence", expanded=False):
                    col1, col2 = st.columns([2, 1])
                    
                    with col1:
                        st.markdown(f"**📋 Description:** {disease_data.get('description', 'N/A')}")
                        st.markdown(f"**💊 Recommendation:** {disease_data.get('recommendation', 'N/A')}")
                        
                        st.markdown("**🔍 Matched Health Indicators:**")
                        indicators = disease_data.get('matched_indicators', [])
                        if indicators:
                            for ind in indicators:
                                st.markdown(f"- **{ind['parameter']}**: {ind['value']} (threshold: {ind['condition']})")
                        else:
                            st.markdown("- No specific indicators matched")
                        
                        st.markdown("**⚕️ Associated Symptoms:**")
                        symptoms = disease_data.get('symptoms', [])
                        if symptoms:
                            st.markdown(", ".join([f"*{s}*" for s in symptoms]))
                    
                    with col2:
                        # Determine text color based on background
                        if confidence >= 80:
                            text_color = "#721c24"
                            confidence_icon = "🔴"
                            gauge_emoji = "📊"
                        elif confidence >= 60:
                            text_color = "#856404"
                            confidence_icon = "🟡"
                            gauge_emoji = "📈"
                        else:
                            text_color = "#0c5460"
                            confidence_icon = "🔵"
                            gauge_emoji = "📉"
                        
                        st.markdown(f"""
                        <div style='text-align: center; padding: 1.25rem; background: {color}; border-radius: 12px; border-left: 5px solid {border_color}; box-shadow: 0 2px 8px rgba(0,0,0,0.1);'>
                            <div style='font-size: 1.8rem; margin-bottom: 0.25rem;'>{gauge_emoji}</div>
                            <h2 style='color: {text_color}; margin: 0.25rem 0; font-size: 2.2rem; font-weight: 700; line-height: 1;'>{confidence}%</h2>
                            <p style='margin: 0.25rem 0 0.75rem 0; color: {text_color}; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.5px; font-weight: 600;'>Confidence</p>
                            <div style='background: white; padding: 0.6rem 0.8rem; border-radius: 6px; border: 2px solid {border_color}; display: flex; align-items: center; justify-content: center; gap: 0.5rem;'>
                                <div style='font-size: 1rem;'>{confidence_icon}</div>
                                <strong style='color: {text_color}; font-size: 0.95rem;'>{risk_level}</strong>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        st.progress(int(confidence) / 100)
        else:
            st.markdown("""
            <div class='success-box'>
                <h4>✅ No Significant Diseases Detected</h4>
                <p>Regular health monitoring and a healthy lifestyle are recommended.</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Tab 4: Summary Report
    with tab4:
        st.markdown("### 📄 Complete Analysis Summary")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📊 Parameters Analyzed")
            comparison = results.get("comparison", {})
            param_count = len(comparison)
            
            st.metric("Total Parameters", param_count)
            
            if comparison:
                status_counts = {
                    "Normal": sum(1 for p in comparison.values() if p.get("status") == "Normal"),
                    "Low": sum(1 for p in comparison.values() if p.get("status") == "Low"),
                    "High": sum(1 for p in comparison.values() if p.get("status") == "High"),
                    "Unknown": sum(1 for p in comparison.values() if p.get("status") == "Unknown"),
                }
                
                for status, count in status_counts.items():
                    if count > 0:
                        st.metric(f"{status} Values", count)
        
        with col2:
            st.markdown("#### 🏥 Disease Predictions")
            diseases_result = results.get("diseases", {})
            possible_diseases = diseases_result.get("possible_diseases", {})
            
            st.metric("Possible Conditions Detected", len(possible_diseases))
            
            if possible_diseases:
                top_disease = list(possible_diseases.items())[0]
                st.metric(f"Highest Risk: {top_disease[0]}", f"{top_disease[1]['confidence']}%")
                st.metric("Risk Level", top_disease[1]['risk_level'])
        
        st.markdown("---")
        
        # Overall assessment
        prediction = results.get("prediction", {})
        overall_risk = prediction.get("overall_risk", "Unknown")
        
        st.markdown("#### 🎯 Overall Assessment")
        assessment_text = {
            "Low": "✅ Your blood test results show normal values. Continue regular health check-ups and maintain a healthy lifestyle.",
            "Medium": "⚠️ Some parameters are outside normal ranges. Consult your healthcare provider for further evaluation.",
            "High": "🚨 Multiple parameters show concerning values. Seek immediate medical consultation for proper diagnosis and treatment."
        }.get(overall_risk, "Please consult your healthcare provider for personalized advice.")
        
        st.info(assessment_text)

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #999; font-size: 0.9rem; padding: 2rem 0;'>
<p><b>Blood Report Analyzer v1.0</b></p>
<p>Advanced AI-Powered Medical Analysis | Combined Technology</p>
<p><small>This tool provides informational analysis only. Always consult qualified healthcare professionals for medical diagnosis and treatment.</small></p>
</div>
""", unsafe_allow_html=True)
