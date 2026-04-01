import duckdb
from pathlib import Path


PROCESSED_FILE = Path("data/processed/posts_clean.csv")
WAREHOUSE_PATH = Path("data/warehouse")
DB_FILE = WAREHOUSE_PATH / "job_data.duckdb"


def load_to_warehouse():
    print("[INFO] Starting warehouse load...")

    WAREHOUSE_PATH.mkdir(parents=True, exist_ok=True)

    conn = duckdb.connect(str(DB_FILE))

    conn.execute("""
        CREATE OR REPLACE TABLE posts AS
        SELECT *
        FROM read_csv_auto('data/processed/posts_clean.csv')
    """)

    row_count = conn.execute("SELECT COUNT(*) FROM posts").fetchone()[0]
    print(f"[INFO] Loaded {row_count} rows into warehouse table: posts")

    conn.close()
    print(f"[INFO] DuckDB database saved to: {DB_FILE}")