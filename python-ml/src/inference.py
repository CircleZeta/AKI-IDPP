from models.model_base import ModelBase
from features.feature_engineering import build_features

def run_inference(raw_input: dict) -> dict:
    """
    raw_input: data from Java side (JSON -> dict)
    """
    features = build_features(raw_input)

    model = ModelBase()
    result = model.predict(features)

    return result


if __name__ == "__main__":
    # manual test stub
    sample_input = {}
    output = run_inference(sample_input)
    print(output)
