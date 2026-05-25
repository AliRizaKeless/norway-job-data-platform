from datetime import datetime
from pathlib import Path

import pandas as pd

from src.config_reader import load_config


config = load_config()

PROCESSED_FILE = Path(config["paths"]["processed_data"]) / config["files"]["processed_csv"]
LOG_PATH = Path(config["paths"]["logs"])
REPORT_FILE = LOG_PATH / "data_quality_report.txt"


def validate_data():
    print("[INFO] Starting data validation...")

    if not PROCESSED_FILE.exists():
        raise FileNotFoundError(f"Processed file not found: {PROCESSED_FILE}")

    df = pd.read_csv(PROCESSED_FILE)

    row_count = len(df)
    duplicate_count = df.duplicated().sum()
    null_count = df.isnull().sum().sum()

    report = f"""
Data Quality Report
Generated at: {datetime.now()}

Source file: {PROCESSED_FILE}

Row count: {row_count}
Duplicate rows: {duplicate_count}
Null values: {null_count}

Status: PASSED
"""

    if row_count == 0:
        report = report.replace("Status: PASSED", "Status: FAILED")
        write_report(report)
        raise ValueError("Processed dataset is empty")

    LOG_PATH.mkdir(parents=True, exist_ok=True)
    write_report(report)

    print(f"[INFO] Row count: {row_count}")
    print(f"[INFO] Duplicate rows: {duplicate_count}")
    print(f"[INFO] Null values: {null_count}")
    print(f"[INFO] Data quality report saved to: {REPORT_FILE}")
    print("[INFO] Data validation finished successfully")


def write_report(report):
    LOG_PATH.mkdir(parents=True, exist_ok=True)

    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        file.write(report)