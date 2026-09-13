import os
import joblib
import numpy as np
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model_artifacts", "model.joblib")
MODEL_VERSION = "fraud_v1_logreg"

ML_MODELS = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    ML_MODELS["fraud_model"] = joblib.load(MODEL_PATH)
    yield
    ML_MODELS.clear()

app = FastAPI(title="Fraud Model Serving API — Vertex-ready", version="1.0.0", lifespan=lifespan)


class Instance(BaseModel):
    feature_1: float = Field(..., description="Account age in years")
    feature_2: float = Field(..., description="Number of transactions in last 24h")
    feature_3: float = Field(..., description="Average transaction amount")


class VertexPredictRequest(BaseModel):
    instances: List[Instance]


class VertexPredictResponse(BaseModel):
    predictions: List[dict]


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": "fraud_model" in ML_MODELS}

from fastapi import Body, FastAPI, HTTPException

@app.post("/predict", response_model=VertexPredictResponse)
def predict(request: VertexPredictRequest = Body(...)):
    model = ML_MODELS.get("fraud_model")
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded yet")

    if not request.instances:
        raise HTTPException(status_code=400, detail="instances must not be empty")

    features = np.array([[r.feature_1, r.feature_2, r.feature_3] for r in request.instances])

    try:
        preds = model.predict(features)
        probas = model.predict_proba(features)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference failed: {type(e).__name__}")

    predictions = [
        {"prediction": int(p), "probability": float(probas[i][p]), "model_version": MODEL_VERSION}
        for i, p in enumerate(preds)
    ]
    return VertexPredictResponse(predictions=predictions)
