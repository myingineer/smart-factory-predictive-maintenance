# This script trains a logistic regression model to predict machine failure based on sensor data.

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from app.config import FEATURE_COLUMNS, TARGET_COLUMN, MODEL_FILE_PATH, STREAMING_CSV_FILE, CLEANED_DATASET_FILE
import pickle
import os


# Paths
DATA_PATH = CLEANED_DATASET_FILE
STREAM_DATA_PATH = STREAMING_CSV_FILE
MODEL_PATH = MODEL_FILE_PATH

# Load cleaned data
df = pd.read_csv(DATA_PATH)

# Select features and target
FEATURES = FEATURE_COLUMNS
TARGET = TARGET_COLUMN

X = df[list(FEATURE_COLUMNS.keys())]
y = df[TARGET]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
# model = LogisticRegression(max_iter=1000, class_weight="balanced")
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    class_weight='balanced',
    max_samples=0.8,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)

accuracy = model.score(X_test, y_test)
print(f"Model accuracy: {accuracy:.2f}\n")

print("Classification Report:\n")
print(classification_report(y_test, y_pred))

# Save model
os.makedirs("models", exist_ok=True)

with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

print(f"\nModel saved to {MODEL_PATH}")

# Save test data for streaming simulation (IMPORTANT)
os.makedirs("data", exist_ok=True)

X_test.to_csv(STREAM_DATA_PATH, index=False)

print(f"Streaming data saved to {STREAM_DATA_PATH}")