import os
from pathlib import Path

from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

from src.config_reader import load_config


load_dotenv()

config = load_config()

PROCESSED_FILE = Path(config["paths"]["processed_data"]) / config["files"]["processed_csv"]

AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
AZURE_CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME")


def upload_processed_file_to_azure():
    if not AZURE_STORAGE_CONNECTION_STRING:
        raise ValueError("AZURE_STORAGE_CONNECTION_STRING is missing")

    if not AZURE_CONTAINER_NAME:
        raise ValueError("AZURE_CONTAINER_NAME is missing")

    if not PROCESSED_FILE.exists():
        raise FileNotFoundError(f"Processed file not found: {PROCESSED_FILE}")

    blob_service_client = BlobServiceClient.from_connection_string(
        AZURE_STORAGE_CONNECTION_STRING
    )

    container_client = blob_service_client.get_container_client(AZURE_CONTAINER_NAME)

    blob_name = f"processed/{PROCESSED_FILE.name}"

    with open(PROCESSED_FILE, "rb") as data:
        container_client.upload_blob(
            name=blob_name,
            data=data,
            overwrite=True,
        )

    print(f"[INFO] Uploaded {PROCESSED_FILE} to Azure Blob: {blob_name}")


if __name__ == "__main__":
    upload_processed_file_to_azure()