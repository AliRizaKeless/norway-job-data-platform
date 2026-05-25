import argparse

from src.ingest import run_ingestion
from src.transform import transform_data
from src.validate import validate_data
from src.load import load_to_warehouse
from src.logger import setup_logger

logger = setup_logger()


def run_pipeline():
    steps = [
        ("Ingestion", run_ingestion),
        ("Transformation", transform_data),
        ("Validation", validate_data),
        ("Warehouse Load", load_to_warehouse),
    ]

    for step_name, step_func in steps:
        try:
            logger.info(f"Starting step: {step_name}")
            step_func()
            logger.info(f"Finished step: {step_name}")
        except Exception as e:
            logger.error(f"Step failed: {step_name} | Error: {e}")
            raise


def main():
    parser = argparse.ArgumentParser(description="Data pipeline runner")

    parser.add_argument("--run-all", action="store_true")
    parser.add_argument("--ingest-only", action="store_true")
    parser.add_argument("--transform-only", action="store_true")
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument("--load-only", action="store_true")

    args = parser.parse_args()

    logger.info("Pipeline started")

    if args.run_all:
        run_pipeline()
    elif args.ingest_only:
        run_ingestion()
    elif args.transform_only:
        transform_data()
    elif args.validate_only:
        validate_data()
    elif args.load_only:
        load_to_warehouse()
    else:
        run_pipeline()

    logger.info("Pipeline finished successfully")


if __name__ == "__main__":
    main()