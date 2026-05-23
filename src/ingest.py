import json
from datetime import datetime
from pathlib import Path

import requests

from src.config_reader import load_config


config = load_config()

RAW_DATA_PATH = Path(config["paths"]["raw_data"])

SSB_TABLE_ID = "08651"
SSB_API_URL = f"https://data.ssb.no/api/pxwebapi/v2/tables/{SSB_TABLE_ID}/data"


def fetch_ssb_data():
    params = {
        "lang": "en",
        "outputFormat": "json-stat2",
    }

    response = requests.get(SSB_API_URL, params=params, timeout=30)
    response.raise_for_status()

    return response.json()


def save_raw_data(data):
    RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = RAW_DATA_PATH / f"ssb_raw_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    print(f"[INFO] Raw data saved to: {file_path}")


def run_ingestion():
    print("[INFO] Starting SSB ingestion...")

    data = fetch_ssb_data()
    save_raw_data(data)

    print("[INFO] SSB ingestion finished")