\# Norway Job Data Platform



A modern data engineering project that ingests, processes, and models Norwegian job market data.



\## Stack



\- Python

\- SQL

\- DuckDB

\- Azure (later)

\- Terraform (later)



\## Pipeline Overview



This project implements a simple medallion-style data platform:



\- \*\*Bronze layer\*\*: Raw data ingestion from API

\- \*\*Silver layer\*\*: Cleaned and processed dataset

\- \*\*Gold layer\*\*: Analytics-ready data stored in DuckDB



\## Features



\- Data ingestion from external API

\- Data transformation and cleaning

\- Data validation checks

\- Logging system for pipeline monitoring

\- YAML-based configuration management

