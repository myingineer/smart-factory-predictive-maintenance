# Configuration file for the application

# =========================
# MODEL CONFIGURATION
# =========================

FEATURE_COLUMNS = {
    "temperature": float,
    "humidity": float,
    "vibration": float,
    "energy_consumption": float,
    "pressure": float
}

TARGET_COLUMN = "maintenance_required"

# =========================
# MAINTENANCE RULES
# =========================

THRESHOLDS = {
    "temperature": 85,
    "vibration": 65,
    "energy_consumption": 4.5,
    "pressure": 4.0
}

RECOMMENDATIONS = {
    "temperature":
        "Critical motor overheating detected. Inspect cooling system immediately.",

    "vibration":
        "Severe vibration anomaly detected. Inspect motor bearings and shaft alignment.",

    "energy_consumption":
        "High energy consumption detected. Inspect motor load and efficiency.",

    "pressure":
        "Abnormal pressure levels detected. Inspect hydraulic or pneumatic systems."
}


# =========================
# API CONFIGURATION
# =========================

API_URL = "http://127.0.0.1:8000/predict/anomaly/v1"


# =========================
# DATASET FILES
# =========================

STREAMING_CSV_FILE = "data/streaming_data.csv"

PREDICTION_LOG_FILE = "data/prediction_logs.csv"

RAW_DATASET_FILE = "data/raw_sensor_data.csv"

CLEANED_DATASET_FILE = "data/cleaned_sensor_data.csv"


# =========================
# MODEL FILE
# =========================

MODEL_FILE_PATH = "models/model.pkl"