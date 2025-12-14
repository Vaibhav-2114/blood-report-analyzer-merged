import re
import json
from pathlib import Path

HERE = Path(__file__).parent
MAPPING_PATH = HERE.parent / "utils" / "mapping.json"

def get_mapping():
    """Load mapping dictionary, with fallback if file doesn't exist"""
    if MAPPING_PATH.exists():
        with open(MAPPING_PATH) as f:
            return json.load(f)
    else:
        # Default mapping if file not found
        return {
            'hemoglobin': ['hemoglobin', 'hb', 'hgb'],
            'wbc': ['wbc', 'white blood cell', 'wbcs'],
            'platelets': ['platelets', 'plt', 'platelet'],
            'creatinine': ['creatinine', 'creat'],
            'sgpt': ['sgpt', 'alt', 'alanine'],
            'sgot': ['sgot', 'ast', 'aspartate'],
            'bilirubin': ['bilirubin', 'bili']
        }

def normalize_key(k: str):
    k = re.sub(r'[^a-z0-9 ]+', '', k.lower())
    mapping = get_mapping()
    for std, variants in mapping.items():
        for v in variants:
            if v in k:
                # Map to proper key names that match normal_ranges.json
                key_map = {
                    'hemoglobin': 'Hemoglobin',
                    'wbc': 'WBC',
                    'platelets': 'Platelets',
                    'creatinine': 'Creatinine',
                    'sgpt': 'SGPT',
                    'sgot': 'SGOT',
                    'bilirubin': 'Bilirubin'
                }
                return key_map.get(std, std.capitalize())
    return None

def extract_key_values(text: str):
    """Extract blood test parameters and values from text"""
    data = {}
    lines = text.splitlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        m = re.search(r'([A-Za-z \-\(\)/]+)[:\s]+([0-9]+(?:\.[0-9]+)?)', line)
        if m:
            raw_key = m.group(1).strip()
            raw_val = m.group(2)
            key = normalize_key(raw_key)
            try:
                val = float(raw_val)
            except:
                continue
            if key:
                data[key] = val
    return data
