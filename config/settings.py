from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml


ROOT_DIR = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT_DIR / "config.yaml"

DEFAULT_CONFIG: dict[str, Any] = {
    "model": {
        "path": "model/model.pkl",
        "version": "1.0.0",
    },
    "prediction_logging": {
        "enabled": True,
        "path": "logs/predictions.jsonl",
    },
}


def _merge_config(defaults: dict[str, Any], overrides: dict[str, Any]) -> dict[str, Any]:
    merged = defaults.copy()
    for key, value in overrides.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = _merge_config(merged[key], value)
        else:
            merged[key] = value
    return merged


@lru_cache
def load_config() -> dict[str, Any]:
    if not CONFIG_PATH.exists():
        return DEFAULT_CONFIG

    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        loaded = yaml.safe_load(file) or {}

    return _merge_config(DEFAULT_CONFIG, loaded)


def resolve_project_path(path_value: str) -> Path:
    path = Path(path_value)
    if path.is_absolute():
        return path
    return ROOT_DIR / path
