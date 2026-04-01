import pandas as pd
import json
from pathlib import Path


RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")


def get_latest_raw_file():
    files = list(RAW_PATH.glob("*.json"))
    latest_file = max(files, key=lambda x: x.stat().st_mtime)
    return latest_file


def transform_data():
    print("[INFO] Starting transformation...")

    raw_file = get_latest_raw_file()
    print(f"[INFO] Reading file: {raw_file}")

    with open(raw_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    # Basit temizlik
    df = df.drop_duplicates()
    df = df.dropna()

    PROCESSED_PATH.mkdir(parents=True, exist_ok=True)
    output_file = PROCESSED_PATH / "posts_clean.csv"

    df.to_csv(output_file, index=False)

    print(f"[INFO] Processed data saved to: {output_file}")