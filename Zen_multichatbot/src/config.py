import os
import yaml
from typing import Dict, Any

DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config.yaml")

def load_config(path: str = None) -> Dict[str, Any]:
    cfg_path = path or DEFAULT_CONFIG_PATH
    if not os.path.isfile(cfg_path):
        cfg_path = os.path.join(os.path.dirname(__file__), "..", "config.example.yaml")
    with open(cfg_path, "r") as f:
        return yaml.safe_load(f)
