import requests
import json
from datetime import datetime
from pathlib import Path


RAW_DATA_PATH = Path("data/raw")


def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.json()


def save_raw_data(data):
    RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = RAW_DATA_PATH / f"posts_raw_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    print(f"[INFO] Raw data saved to: {file_path}")


def run_ingestion():
    print("[INFO] Starting ingestion...")
    data = fetch_posts()
    print(f"[INFO] Fetched {len(data)} records")
    save_raw_data(data)
    print("[INFO] Ingestion finished")