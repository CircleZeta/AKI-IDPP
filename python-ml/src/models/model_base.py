import joblib
from abc import ABC, abstractmethod
from sklearn.base import BaseEstimator

class ModelBase(ABC):
    """
    基础模型类，定义训练、预测和模型持久化接口
    所有具体模型应继承此类
    """
    def __init__(self):
        self.model = None  # 具体模型实例

    @abstractmethod
    def build_model(self) -> BaseEstimator:
        """
        构建具体模型实例（sklearn / pytorch / 其他）
        """
        pass

    def fit(self, X, y):
        if self.model is None:
            self.model = self.build_model()
        self.model.fit(X, y)
        return self

    def predict(self, X):
        if self.model is None:
            raise RuntimeError("Model is not built. Call build_model() or fit() first.")
        return self.model.predict(X)

    def save(self, path: str):
        if self.model is None:
            raise RuntimeError("No model to save.")
        joblib.dump(self.model, path)

    def load(self, path: str):
        self.model = joblib.load(path)
        return self
