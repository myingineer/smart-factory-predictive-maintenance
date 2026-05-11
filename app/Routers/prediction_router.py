from fastapi import APIRouter, status
from app.Schemas import schemas
from app.Utils.utils import predict_anomaly

# Create API router for prediction endpoints
router = APIRouter(
    prefix="/predict/anomaly",
    tags=["Anomaly Prediction"]
)

# Define endpoint for anomaly prediction
@router.post("/v1", status_code=status.HTTP_200_OK)
async def anomaly_prediction_router(schema: schemas.SensorData):

    result = predict_anomaly(schema)

    return result
