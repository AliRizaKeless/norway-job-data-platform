from src.ingest import run_ingestion
from src.transform import transform_data
from src.load import load_to_warehouse


def main():
    run_ingestion()
    transform_data()
    load_to_warehouse()


if __name__ == "__main__":
    main()