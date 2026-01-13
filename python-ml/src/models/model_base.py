# model_base.py
# 模型训练基类

import pickle
from abc import ABC, abstractmethod

class ModelBase(ABC):
    """机器学习模型基类，所有模型需继承此类"""

    @abstractmethod
    def fit(self, X, y):
        pass

    @abstractmethod
    def predict(self, X):
        pass

    def save(self, path: str):
        """保存模型到文件"""
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, path: str):
        """从文件加载模型"""
        with open(path, 'rb') as f:
            return pickle.load(f)
