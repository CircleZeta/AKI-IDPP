class ModelBase:
    def __init__(self):
        self.name = "AKI_BASE_MODEL"
        self.version = "0.1.0"

    def predict(self, features: dict) -> dict:
        """
        features: output of build_features
        return: prediction result dict
        """
        # placeholder inference
        return {
            "aki_risk_score": 0.0,
            "model_name": self.name,
            "model_version": self.version
        }
