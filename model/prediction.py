#basic import
import json
import pickle
from datetime import datetime, timezone
from functools import lru_cache
from uuid import uuid4

import pandas as pd

from config.settings import load_config, resolve_project_path


config = load_config()
MODEL_VERSION = str(config["model"]["version"])


class ModelArtifactNotFoundError(FileNotFoundError):
    """Raised when the configured model artifact is not available at runtime."""


def get_model_path():
    return resolve_project_path(config["model"]["path"])


@lru_cache
def load_model():
    model_path = get_model_path()
    if not model_path.exists():
        raise ModelArtifactNotFoundError(
            "Model artifact is missing. Expected a trained pickle file at "
            f"{model_path}. For Streamlit deployment, commit this file, use Git LFS, "
            "or configure the app to download the artifact before startup."
        )

    with model_path.open("rb") as file:
        return pickle.load(file)


class LazyModelProxy:
    def __getattr__(self, name):
        return getattr(load_model(), name)


# Backward-compatible module attribute for existing imports.
model = LazyModelProxy()


def log_prediction(user_input: dict, prediction: dict) -> None:
    logging_config = config.get("prediction_logging", {})
    if not logging_config.get("enabled", True):
        return

    log_path = resolve_project_path(logging_config["path"])
    log_path.parent.mkdir(parents=True, exist_ok=True)

    event = {
        "request_id": str(uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model_version": MODEL_VERSION,
        "input": user_input,
        "prediction": prediction,
    }

    with log_path.open("a", encoding="utf-8") as file:
        file.write(json.dumps(event) + "\n")


#predict output function
def predict_output(user_input: dict):
    loaded_model = load_model()
    df = pd.DataFrame([user_input])

    # Predict the class
    predicted_class = str(loaded_model.predict(df)[0])

    # Get probabilities for all classes
    probabilities = loaded_model.predict_proba(df)[0]
    probabilities = [float(p) for p in probabilities]

    #confidence
    confidence = float(max(probabilities))

    # Create mapping: {class_name: probability}
    class_labels = loaded_model.classes_.tolist()
    class_probs = dict(zip(class_labels, probabilities))

    prediction = {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": {k: round(v, 4) for k, v in class_probs.items()}
    }
    log_prediction(user_input, prediction)
    return prediction
