from models.model_base import BaseModel
from features.feature_engineering import FeatureEngineer
import pandas as pd

class InferenceEngine:
    def __init__(self):
        self.model = BaseModel()
        self.feature_engineer = FeatureEngineer()

    def predict(self, raw_df: pd.DataFrame) -> pd.DataFrame:
        X = self.feature_engineer.fit_transform(raw_df)
        preds = self.model.predict(X)
        return pd.DataFrame({'prediction': preds})
