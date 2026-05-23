import json
import itertools
from pathlib import Path

import pandas as pd

from src.config_reader import load_config


config = load_config()

RAW_PATH = Path(config["paths"]["raw_data"])
PROCESSED_PATH = Path(config["paths"]["processed_data"])
PROCESSED_FILE_NAME = config["files"]["processed_csv"]


def get_latest_raw_file():
    files = list(RAW_PATH.glob("ssb_raw_*.json"))

    if not files:
        raise FileNotFoundError("No SSB raw JSON files found in data/raw")

    return max(files, key=lambda x: x.stat().st_mtime)


def convert_ssb_jsonstat_to_dataframe(data):
    values = data["value"]
    dimensions = data["dimension"]

    dim_names = data["id"]

    categories = []
    for dim in dim_names:
        labels = list(dimensions[dim]["category"]["label"].values())
        categories.append(labels)

    combinations = list(itertools.product(*categories))

    df = pd.DataFrame(combinations, columns=dim_names)
    df["value"] = values

    return df


def transform_data():
    print("[INFO] Starting transformation...")

    raw_file = get_latest_raw_file()
    print(f"[INFO] Reading file: {raw_file}")

    with open(raw_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    df = convert_ssb_jsonstat_to_dataframe(data)

    df = df.drop_duplicates()
    df = df.dropna()

    PROCESSED_PATH.mkdir(parents=True, exist_ok=True)
    output_file = PROCESSED_PATH / PROCESSED_FILE_NAME

    df.to_csv(output_file, index=False)

    print(f"[INFO] Processed data saved to: {output_file}")