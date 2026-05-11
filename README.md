# Smart Factory Predictive Maintenance System

## Overview

This project is a real-time predictive maintenance and anomaly detection platform designed for monitoring industrial electric motors operating within a smart manufacturing facility producing wind turbine components.

The system uses machine learning to analyze industrial IoT telemetry data and predict maintenance risks before machine failures occur.

The application simulates real-time sensor streaming, performs anomaly prediction using a **FastAPI** service, generates maintenance recommendations, and stores operational logs for traceability and analytics.

---

# Features

- Real-time telemetry simulation
- Machine learning anomaly detection
- Probability-based risk scoring
- Explainable maintenance recommendations
- FastAPI REST API
- Persistent prediction logging
- Config-driven architecture
- Dynamic schema generation

---

# Project Structure

```text
project/
│
├── app/
│   ├── main.py
│   ├── config.py
│   │
│   ├── schemas/
│   │   └── schemas.py
│   │
│   ├── routers/
│   │   └── prediction_router.py
│   │
│   └── Utils/
│       └── utils.py
│
├── training/
│   └── train.py
│
├── simulator/
│   └── stream.py
│
├── models/
│   └── model.pkl
│
├── data/
│   ├── raw_sensor_data.csv
│   ├── cleaned_sensor_data.csv
│   ├── streaming_data.csv
│   └── prediction_logs.csv
│
├── requirements.txt
└── README.md
```

---

# Technologies Used

- Python
- FastAPI
- Scikit-learn
- Pandas
- Joblib
- Requests
- Uvicorn
- Pydantic

---

# Machine Learning Model

The system uses a Random Forest Classifier trained on industrial IoT telemetry data.

## Features Used

- Temperature
- Humidity
- Vibration (sound/audible mechanical distress)
- Energy Consumption
- Pressure

## Target Variable

- `maintenance_required`

---

# Installation

## 1. Clone the Repository

```bash
git clone <https://github.com/myingineer/smart-factory-predictive-maintenance>
cd <smart-factory-predictive-maintenance>
```

---

## 2. Create Virtual Environment

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Dataset Preparation

Place the dataset inside:

```text
data/raw_sensor_data.csv
```

# Dataset Preparation

Place the dataset inside:

```text
data/raw_sensor_data.csv
```

After placing the dataset, open:

```text
app/config.py
```

Update the following configuration values to match your dataset columns:

```python
FEATURE_COLUMNS = {
    "temperature": float,
    "humidity": float,
    "vibration": float,
    "energy_consumption": float,
    "pressure": float
}

TARGET_COLUMN = "maintenance_required"
```

You may also update:

- Threshold values
- Maintenance recommendations
- File paths
- API configuration

depending on your dataset structure and industrial use case.

---

# Data Cleaning

Run:

```bash
python3 -m data.clean_data
```

This generates:

```text
data/cleaned_sensor_data.csv
```

---

# Model Training

Run:

```bash
python3 -m training.train
```

This process will:

- Train the machine learning model
- Evaluate model accuracy
- Save the trained model to:

```text
models/model.pkl
```

- Generate streaming simulation data:

```text
data/streaming_data.csv
```

---

# Running the API

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

API URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Running the Telemetry Stream

Open a second terminal and run:

```bash
python3 -m simulator.stream
```

This simulates real-time industrial sensor telemetry and continuously sends prediction requests to the API.

---

# Example API Request

```json
{
  "machine_id": "Lathe-001",
  "temperature": 92.4,
  "humidity": 43.7,
  "vibration": 67.1,
  "energy_consumption": 4.8,
  "pressure": 2.9
}
```

---

# Example API Response

```json
{
  "machine_id": "Lathe-001",
  "anomaly_score_percent": 99.74,
  "status": "High Risk",
  "recommendation": "Critical motor overheating detected. Inspect cooling system immediately."
}
```

---

# Prediction Logs

All predictions are stored inside:

```text
data/prediction_logs.csv
```

The logs contain:

- Timestamp
- Machine ID
- Sensor readings
- Anomaly score
- Machine status
- Maintenance recommendations

---

# Industrial Use Case

The system monitors industrial electric motors powering manufacturing lathes used in the production of wind turbine components.

By continuously analyzing machine telemetry, the platform can detect abnormal operational patterns before catastrophic equipment failures occur.

This enables:

- Predictive maintenance
- Reduced downtime
- Improved operational efficiency
- Lower maintenance costs
- Increased manufacturing reliability

---

# Future Improvements

Potential future improvements include:

- MQTT integration
- Kafka streaming
- Grafana dashboards
- AWS IoT Core integration
- Docker containerization
- Kubernetes deployment
- Automated retraining pipelines

---

# Author

Alexander Soromtochukwu Emeka-Akam<br />
Applied AI Student<br />
@<br />
IUBH Berlin, Germany

---

# License

This project is intended for educational and research purposes.