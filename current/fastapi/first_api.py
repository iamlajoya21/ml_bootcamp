import uvicorn
from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
import joblib
import numpy as np

from pydantic import BaseModel, Field, field_validator
from typing import List

class PredictionRequest(BaseModel):
    feature_1: float = Field(..., description="Account age in years")
    feature_2: float = Field(..., description="Number of transactions in last 24h")
    feature_3: float = Field(..., description="Average transaction amount")

    @field_validator("feature_2")
    @classmethod
    def non_negative_txn_count(cls, v):
        if v < 0:
            raise ValueError("feature_2 (transaction count) cannot be negative")
        return v

class PredictionResponse(BaseModel):
    prediction: int
    probability: float
    model_version: str


MODEL_PATH = "./models/model.joblib"
ML_MODELS = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup: load once
    ML_MODELS["fraud_model"] = joblib.load(MODEL_PATH)
    print("model loaded")
    yield
    # shutdown: clean up if needed
    ML_MODELS.clear()

app = FastAPI(title="Fraud Model Serving API", version="1.0.0", lifespan=lifespan)

MODEL_VERSION = "fraud_v1_logreg"

@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": "fraud_model" in ML_MODELS}

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    model = ML_MODELS.get("fraud_model")
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded yet")

    features = np.array([[request.feature_1, request.feature_2, request.feature_3]])

    try:
        pred = int(model.predict(features)[0])
        proba = float(model.predict_proba(features)[0][pred])
    except Exception as e:
        # never let a raw stack trace leak to the client
        raise HTTPException(status_code=500, detail=f"Inference failed: {type(e).__name__}")

    return PredictionResponse(prediction=pred, probability=proba, model_version=MODEL_VERSION)

if __name__ == "__main__":
    uvicorn.run("first_api:app", host="127.0.0.1", port=8080, reload=True)
