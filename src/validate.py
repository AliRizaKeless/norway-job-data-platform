import pandas as pd
from pathlib import Path


PROCESSED_FILE = Path("data/processed/posts_clean.csv")


def validate_processed_data():
    print("[INFO] Starting data validation...")

    if not PROCESSED_FILE.exists():
        raise FileNotFoundError(f"Processed file not found: {PROCESSED_FILE}")

    df = pd.read_csv(PROCESSED_FILE)

    row_count = len(df)
    duplicate_count = df.duplicated().sum()
    null_count = df.isnull().sum().sum()

    print(f"[INFO] Row count: {row_count}")
    print(f"[INFO] Duplicate rows: {duplicate_count}")
    print(f"[INFO] Null values: {null_count}")

    if row_count == 0:
        raise ValueError("Processed dataset is empty")

    print("[INFO] Data validation finished successfully")