import pandas as pd

class FeatureEngineer:
    def __init__(self):
        pass

    def fit(self, df: pd.DataFrame):
        # TODO: fit transformations
        return self

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        # TODO: apply transformations
        return df

    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        self.fit(df)
        return self.transform(df)
