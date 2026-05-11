import pickle
import pandas as pd
from app.config import (
    FEATURE_COLUMNS,
    THRESHOLDS,
    RECOMMENDATIONS
)

# Load trained model
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)


# Classify risk level based on anomaly score
def classify_risk(anomaly_score):

    # Define thresholds for risk classification
    if anomaly_score >= 70:
        return "High Risk"

    elif anomaly_score >= 40:
        return "Medium Risk"

    return "Normal"

# Create recommendation based on sensor data and anomaly score
def generate_recommendation(sensor_data, anomaly_score):
    
    # If anomaly score is low, provide general monitoring recommendation
    if anomaly_score < 40:
        return "No immediate action required. Monitor sensor readings regularly."

    recommendations = []

    # Check each sensor against thresholds to generate specific recommendations
    for feature in FEATURE_COLUMNS.keys():
        value = getattr(sensor_data, feature)
        threshold = THRESHOLDS.get(feature)

        if threshold is not None and value >= threshold:
            recommendations.append(RECOMMENDATIONS.get(feature))

    if not recommendations:
        return "Anomaly detected but no specific sensor exceeded thresholds. Investigate further."

    return " ".join(recommendations)


# predict anomaly score and generate recommendation based on incoming sensor data
def predict_anomaly(sensor_data):

    # Create DataFrame for model input
    features = pd.DataFrame([{
        feature: getattr(sensor_data, feature)
        for feature in FEATURE_COLUMNS.keys()
    }])

    # Probability of anomaly 
    probability = model.predict_proba(features)[0][1]

    anomaly_score = round(probability * 100, 2)

    status = classify_risk(anomaly_score)

    recommendation = generate_recommendation(
        sensor_data,
        anomaly_score
    )

    return {
        "machine_id": sensor_data.machine_id,
        "anomaly_score_percent": anomaly_score,
        "status": status,
        "recommendation": recommendation
    }