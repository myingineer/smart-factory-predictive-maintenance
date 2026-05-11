from fastapi import FastAPI
from app.Routers import prediction_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prediction_router.router)

app.get("/")
def read_root():
    return {"message": "Welcome to the Machine Anomaly Detection API!"}