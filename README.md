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



\## Current Status



\- Project structure initialized

\- Raw data ingestion implemented

\- Transformation step added

\- Data validation checks added

\- DuckDB warehouse layer added

\- Logging and YAML configuration added



\## Roadmap



\- Replace demo API with Norwegian data source

\- Add analytics SQL queries

\- Add Azure Blob Storage integration

\- Add Terraform infrastructure

\- Add GitHub Actions workflow



\## Next development step



The current pipeline uses a demo API. The next milestone is to replace the demo source with a real Norwegian data source from Statistics Norway (SSB) and adapt the pipeline for labor market analytics.

