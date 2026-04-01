import logging
from pathlib import Path


LOG_PATH = Path("logs")
LOG_FILE = LOG_PATH / "pipeline.log"


def setup_logger():
    LOG_PATH.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("pipeline_logger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger