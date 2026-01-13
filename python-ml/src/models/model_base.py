"""
model_base.py
Stage 2: Base model definition
"""

import joblib
from abc import ABC, abstractmethod

class BaseModel(ABC):
    def __init__(self):
        self.model = None

    @abstractmethod
    def fit(self, X, y):
        pass

    @abstractmethod
    def predict(self, X):
        pass

    def evaluate(self, X, y):
        y_pred = self.predict(X)
        return self.metric(y, y_pred)

    @abstractmethod
    def metric(self, y_true, y_pred):
        pass

    def save(self, path: str):
        joblib.dump(self.model, path)

    def load(self, path: str):
        self.model = joblib.load(path)
