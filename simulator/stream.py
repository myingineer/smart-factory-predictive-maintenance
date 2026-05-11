import time
import pandas as pd
import requests
from app import config
import csv
import os

# Load the streaming dataset
df = pd.read_csv(config.STREAMING_CSV_FILE)

# The URL of the FastAPI endpoint
API_URL = config.API_URL

# Prediction log file
PREDICTION_LOG_FILE = config.PREDICTION_LOG_FILE

MACHINE_IDS = [
    "Lathe-001",
    "Lathe-002",
    "Lathe-003"
]

# Ensure data directory exists
os.makedirs("data", exist_ok=True)


for index, row in df.iterrows():

    # Simulate multiple machines
    machine_id = MACHINE_IDS[index % len(MACHINE_IDS)]

    payload = {
        "machine_id": machine_id,
        "temperature": row["temperature"],
        "humidity": row["humidity"],
        "vibration": row["vibration"],
        "energy_consumption": row["energy_consumption"],
        "pressure": row["pressure"]
    }

    try:

        response = requests.post(
            API_URL,
            json=payload
        )

        prediction_data = response.json()

        print("\n==============================")
        print(f"[STREAM] #{index + 1}")
        print("==============================")

        print("Payload:")
        print(payload)

        print("\nPrediction:")
        print(prediction_data)

        # Create log entry
        log_entry = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            **prediction_data
        }

        # Include payload data
        log_entry.update(payload)

        # Append log entry to CSV file
        file_exists = os.path.isfile(PREDICTION_LOG_FILE)

        with open(PREDICTION_LOG_FILE, mode="a", newline="") as f:

            writer = csv.DictWriter(
                f,
                fieldnames=log_entry.keys()
            )

            # Write CSV header once
            if not file_exists:
                writer.writeheader()

            writer.writerow(log_entry)

    except Exception as e:

        print(f"Streaming error: {e}")

    # Simulate real-time delay
    time.sleep(1)

