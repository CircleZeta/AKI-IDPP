import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

class FeatureEngineering:
    def __init__(self):
        self.num_features = []
        self.cat_features = []
        self.pipeline = None

    def fit(self, df: pd.DataFrame, num_features: list, cat_features: list):
        self.num_features = num_features
        self.cat_features = cat_features

        numeric_transformer = Pipeline(steps=[
            ('scaler', StandardScaler())
        ])
        categorical_transformer = Pipeline(steps=[
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ])

        self.pipeline = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, self.num_features),
                ('cat', categorical_transformer, self.cat_features)
            ]
        )

        self.pipeline.fit(df)
        return self

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        if self.pipeline is None:
            raise RuntimeError("Pipeline is not fitted yet. Call fit() first.")
        transformed = self.pipeline.transform(df)
        return pd.DataFrame(transformed)

    def fit_transform(self, df: pd.DataFrame, num_features: list, cat_features: list) -> pd.DataFrame:
        self.fit(df, num_features, cat_features)
        return self.transform(df)
