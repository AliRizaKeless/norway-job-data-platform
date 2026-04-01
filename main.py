from src.ingest import run_ingestion
from src.transform import transform_data


def main():
    run_ingestion()
    transform_data()


if __name__ == "__main__":
    main()