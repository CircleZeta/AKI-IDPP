# inference.py
# 模型推理接口

from models.model_base import ModelBase
import pandas as pd

class InferenceEngine:
    """统一推理接口，可被 Java 后端调用"""

    def __init__(self, model: ModelBase, feature_engineer=None):
        self.model = model
        self.feature_engineer = feature_engineer

    def predict(self, df: pd.DataFrame):
        """对输入数据进行预测"""
        if self.feature_engineer:
            X = self.feature_engineer.transform(df)
        else:
            X = df
        return self.model.predict(X)
