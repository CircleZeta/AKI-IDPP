def build_features(raw_input: dict) -> dict:
    """
    raw_input: serialized patient data (from Java or ETL)
    return: feature dict consumed by model
    """
    # placeholder implementation
    return {
        "age": raw_input.get("age"),
        "creatinine": raw_input.get("creatinine"),
        "timestamp": raw_input.get("timestamp")
    }
