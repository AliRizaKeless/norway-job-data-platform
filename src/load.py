import duckdb
from pathlib import Path
from src.config_reader import load_config


config = load_config()
PROCESSED_FILE = Path(config["paths"]["processed_data"]) / config["files"]["processed_csv"]
WAREHOUSE_PATH = Path(config["paths"]["warehouse_data"])
DB_FILE = WAREHOUSE_PATH / config["files"]["duckdb_file"]


def load_to_warehouse():
    print("[INFO] Starting warehouse load...")

    WAREHOUSE_PATH.mkdir(parents=True, exist_ok=True)

    conn = duckdb.connect(str(DB_FILE))

    conn.execute(f"""
        CREATE OR REPLACE TABLE posts AS
        SELECT *
        FROM read_csv_auto('{PROCESSED_FILE.as_posix()}')
    """)

    row_count = conn.execute("SELECT COUNT(*) FROM posts").fetchone()[0]
    print(f"[INFO] Loaded {row_count} rows into warehouse table: posts")

    conn.close()
    print(f"[INFO] DuckDB database saved to: {DB_FILE}")