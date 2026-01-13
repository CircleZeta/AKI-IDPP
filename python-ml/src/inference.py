"""
inference.py
Stage 2: ML inference interface
"""

from python_ml.src.models.model_base import BaseModel
from java_backend.src.main.java.org.aki.javabackend.model.dto import AKIPredictionRequest, AKIPredictionResponse

class InferenceService:
    def __init__(self, model: BaseModel):
        self.model = model

    def predict(self, request: AKIPredictionRequest) -> AKIPredictionResponse:
        X = request.to_dataframe()
        y_pred = self.model.predict(X)
        return AKIPredictionResponse(predictions=y_pred)

    def batch_predict(self, requests: list) -> list:
        return [self.predict(req) for req in requests]
