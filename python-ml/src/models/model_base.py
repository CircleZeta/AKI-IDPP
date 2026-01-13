import pickle
from pathlib import Path

class ModelBase:
    """
    基础模型类，用于训练、保存、加载和推理接口。
    所有具体模型应继承此类并实现 train() 和 predict() 方法。
    """
    def __init__(self, model_name: str, save_dir: str = "models"):
        self.model_name = model_name
        self.save_dir = Path(save_dir)
        self.save_dir.mkdir(parents=True, exist_ok=True)
        self.model = None

    def train(self, X, y):
        """
        训练模型，子类必须实现
        """
        raise NotImplementedError("train() must be implemented in subclass.")

    def predict(self, X):
        """
        模型预测，子类必须实现
        """
        raise NotImplementedError("predict() must be implemented in subclass.")

    def save(self):
        """
        保存模型到磁盘
        """
        if self.model is None:
            raise RuntimeError("No model to save. Train the model first.")
        file_path = self.save_dir / f"{self.model_name}.pkl"
        with open(file_path, "wb") as f:
            pickle.dump(self.model, f)

    def load(self):
        """
        从磁盘加载模型
        """
        file_path = self.save_dir / f"{self.model_name}.pkl"
        if not file_path.exists():
            raise FileNotFoundError(f"Model file not found: {file_path}")
        with open(file_path, "rb") as f:
            self.model = pickle.load(f)
