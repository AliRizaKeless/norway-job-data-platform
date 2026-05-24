from src.ingest import run_ingestion
from src.transform import transform_data
from src.validate import validate_data
from src.load import load_to_warehouse
from src.logger import get_logger

logger = get_logger()


def main():
    logger.info("Pipeline started")

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

    logger.info("Pipeline finished successfully")


if __name__ == "__main__":
    main()