from pydantic import create_model, BaseModel
from app.config import FEATURE_COLUMNS


# Dynamically create a Pydantic model for incoming sensor data based on FEATURE_COLUMNS
DynamicSensorData = create_model(
    "SensorData",

    machine_id=(str, ...),
    **{
        feature: (dtype, ...)
        for feature, dtype in FEATURE_COLUMNS.items()
    }
)

class SensorData(DynamicSensorData):
    pass