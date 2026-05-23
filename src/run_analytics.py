import duckdb
from pathlib import Path

from src.config_reader import load_config


config = load_config()

WAREHOUSE_PATH = Path(config["paths"]["warehouse_data"])
DB_FILE = WAREHOUSE_PATH / config["files"]["duckdb_file"]
SQL_FILE = Path("sql/analytics.sql")


def run_analytics_query():
    print("[INFO] Running analytics query...")

    with open(SQL_FILE, "r", encoding="utf-8") as file:
        query = file.read()

    conn = duckdb.connect(str(DB_FILE))
    result = conn.execute(query).fetchdf()
    conn.close()

    print("[INFO] Analytics query result:")
    print(result.head(10))


if __name__ == "__main__":
    run_analytics_query()