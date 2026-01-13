import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

class FeatureEngineering:
    def __init__(self):
        self.num_features = []
        self.cat_features = []
        self.pipeline = None

    def fit(self, df: pd.DataFrame, num_features: list, cat_features: list):
        self.num_features = num_features
        self.cat_features = cat_features

        # 数值特征处理：缺失值均值填充 + 标准化
        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='mean')),
            ('scaler', StandardScaler())
        ])

        # 类别特征处理：缺失值填充（常量"missing"）+ OneHot
        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
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
        # 返回 DataFrame（列名无法完全保留 OneHotEncoder 生成列名，这里可扩展）
        return pd.DataFrame(transformed)

    def fit_transform(self, df: pd.DataFrame, num_features: list, cat_features: list) -> pd.DataFrame:
        self.fit(df, num_features, cat_features)
        return self.transform(df)
