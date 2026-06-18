\# Norway Job Data Platform



A modern data engineering project that ingests, processes, and analyzes Norwegian statistical data using a layered data architecture and cloud-ready design principles.



\---



\## Overview



This project demonstrates how to build an end-to-end data pipeline that:



\- Ingests real-world data from Statistics Norway (SSB)

\- Processes and cleans the data using Python

\- Validates data quality

\- Loads analytics-ready data into a DuckDB warehouse

\- Runs SQL queries for analysis



The project follows a \*\*medallion-style architecture\*\* (raw → processed → analytics).



\---



\## Architecture



SSB API
   ↓
Ingestion Layer
   ↓
Raw JSON
   ↓
Transformation Layer
   ↓
Processed CSV
   ↓
Validation Layer
   ↓
DuckDB Warehouse
   ↓
Analytics SQL
   ↓
Azure Blob Storage

Infrastructure managed with Terraform
CI/CD powered by GitHub Actions





\---



\## Tech Stack



- Python
- Pandas
- DuckDB
- SQL
- Azure Blob Storage
- Terraform
- GitHub Actions
- YAML
- Logging



\---



\## Features



\- Data ingestion from SSB (Statistics Norway API)

\- JSON-stat data transformation into structured tables

\- Data quality validation (nulls, duplicates, row count)

\- Logging for pipeline monitoring

\- Config-driven pipeline using YAML

\- Analytics-ready warehouse layer

\- SQL query execution



\---



\## Example Analytics Query



```sql

SELECT

&#x20;   Tid,

&#x20;   AVG(value) AS avg\_index\_value

FROM ssb\_construction\_cost\_index

WHERE ContentsCode = 'Construction cost index'

GROUP BY Tid

ORDER BY Tid DESC;



Example Output



| Tid     | avg\_index\_value |

| ------- | --------------- |

| 2026M04 | 159.33          |



Project Structure



norway-job-data-platform/

│

├── data/

│   ├── raw/

│   ├── processed/

│   └── warehouse/

│

├── src/

│   ├── ingest.py

│   ├── transform.py

│   ├── validate.py

│   ├── load.py

│   ├── run\_analytics.py

│   ├── logger.py

│   └── config\_reader.py

│

├── config/

│   └── config.yaml

│

├── sql/

│   └── analytics.sql

│

├── logs/

├── main.py

└── README.md

Infrastructure as Code

The Azure infrastructure is provisioned using Terraform.

Resources managed by Terraform:

- Azure Resource Group
- Azure Storage Account
- Azure Blob Container

Terraform configuration is stored under:

infrastructure/terraform/


CI/CD

GitHub Actions is used to validate the pipeline automatically on every push.

The workflow:

1. Install dependencies
2. Run pipeline validation
3. Execute tests
4. Verify infrastructure configuration


How to Run

1\. Install dependencies

pip install -r requirements.txt



2\. Run the pipeline

py main.py



3\. Run analytics Query

py -m src.run\_analytics


## Azure Blob Storage Integration

The pipeline uploads the processed dataset to Azure Blob Storage after local processing.

Current cloud output:

```text
processed/ssb_construction_cost_index_clean.csv

Azure components used:

Azure Storage Account
Azure Blob Container
Secure connection string via .env
Python Azure SDK (azure-storage-blob)

## Pipeline Orchestration

The pipeline is organized as step-based execution:

1. Ingestion
2. Transformation
3. Validation
4. Warehouse Load

Each step is executed sequentially with logging and error handling.  
If one step fails, the pipeline logs the failing step and stops execution.

---

## Data Quality Report

The validation layer generates a data quality report under:

```text
logs/data_quality_report.txt

The report includes:

row count
duplicate row count
null value count
validation status

This provides basic observability and makes the pipeline easier to monitor.


## Current Status

✅ SSB data ingestion

✅ Data transformation

✅ Data quality validation

✅ DuckDB analytics warehouse

✅ SQL analytics queries

✅ Azure Blob Storage integration

✅ GitHub Actions CI/CD

✅ Terraform Infrastructure as Code

✅ CLI-based pipeline execution 



## Future Improvements

- Incremental data loading
- Automated scheduling (Azure Functions / Airflow)
- Dashboard and visualization layer
- Monitoring and alerting



Author


Built as part of a modern data engineering portfolio project focused on real-world data pipelines and cloud-ready architecture.

