# This script is responsible for cleaning the raw sensor data and preparing it for analysis.
# Import necessary libraries
import pandas as pd
from app import config

# Load the raw sensor data from a CSV file
df = pd.read_csv(config.RAW_DATASET_FILE)

# Keep only needed columns
df = df[
    list(config.FEATURE_COLUMNS.keys())
    + [config.TARGET_COLUMN]
]

# Drop rows with missing values
df = df.dropna()

# Reset the index after dropping rows
df = df.reset_index(drop=True)

# Save the cleaned data to a new CSV file
df.to_csv(config.CLEANED_DATASET_FILE, index=False)