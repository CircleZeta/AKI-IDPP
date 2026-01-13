# feature_engineering.py
# 数据预处理与特征工程模块

import pandas as pd
from sklearn.preprocessing import StandardScaler

class FeatureEngineer:
    """负责数据清洗、特征生成与标准化"""

    def __init__(self):
        self.scaler = StandardScaler()

    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """拟合并转换训练数据"""
        df_processed = self._preprocess(df)
        return self.scaler.fit_transform(df_processed)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """转换测试或验证数据"""
        df_processed = self._preprocess(df)
        return self.scaler.transform(df_processed)

    def _preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        """内部数据清洗方法（可根据需求扩展）"""
        df_clean = df.copy()
        # TODO: 添加缺失值处理、特征衍生等
        return df_clean
