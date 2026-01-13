"""
feature_engineering.py
Stage 2: Feature Engineering
"""

import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import VarianceThreshold

class FeatureEngineering:
    def __init__(self):
        self.num_features = []
        self.cat_features = []
        self.pipeline = None

    def fit(self, df: pd.DataFrame, num_features: list, cat_features: list, remove_low_variance=True):
        self.num_features = num_features
        self.cat_features = cat_features

        numeric_transformer = Pipeline(steps=[
            ('scaler', StandardScaler())
        ])
        categorical_transformer = Pipeline(steps=[
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ])

        transformers = [
            ('num', numeric_transformer, self.num_features),
            ('cat', categorical_transformer, self.cat_features)
        ]

        self.pipeline = ColumnTransformer(transformers=transformers)

        X_transformed = self.pipeline.fit_transform(df)

        if remove_low_variance:
            self.selector = VarianceThreshold()
            X_transformed = self.selector.fit_transform(X_transformed)
        else:
            self.selector = None

        return self

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        if self.pipeline is None:
            raise RuntimeError("Pipeline not fitted yet.")
        X_transformed = self.pipeline.transform(df)
        if self.selector:
            X_transformed = self.selector.transform(X_transformed)
        return pd.DataFrame(X_transformed)

    def fit_transform(self, df: pd.DataFrame, num_features: list, cat_features: list) -> pd.DataFrame:
        self.fit(df, num_features, cat_features)
        return self.transform(df)

    def save_pipeline(self, path: str):
        joblib.dump(self.pipeline, path)

    def load_pipeline(self, path: str):
        self.pipeline = joblib.load(path)