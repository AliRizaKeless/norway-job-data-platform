import yaml
from pathlib import Path


CONFIG_FILE = Path("config/config.yaml")


def load_config():
    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)