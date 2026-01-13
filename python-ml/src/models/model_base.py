import pandas as pd

class BaseModel:
    def __init__(self):
        self.trained = False

    def train(self, X: pd.DataFrame, y: pd.Series):
        # TODO: implement training
        self.trained = True

    def predict(self, X: pd.DataFrame) -> pd.Series:
        if not self.trained:
            raise RuntimeError('Model not trained yet')
        # TODO: implement prediction
        return pd.Series([0]*len(X))
