📊 FMCG Sales Data Engineering & Analytics Pipeline
📌 Project Overview

This project demonstrates an end-to-end data engineering and analytics pipeline using an FMCG retail dataset.
The goal was to ingest raw transactional sales data, perform scalable transformations, orchestrate workflows, and deliver actionable business insights via an interactive Power BI dashboard.

🧰 Tech Stack

SQL – exploratory analysis and aggregations

PySpark (Databricks) – data cleaning and transformation

Apache Airflow – pipeline orchestration

Power BI – data visualization and KPI reporting

Python – supporting scripts and analysis

📂 Dataset

Source: Kaggle – Grocery Store Sales Dataset

Records: ~1900 transactions

Key fields:

Transaction date

Store

Aisle

Product

Quantity

Final sales amount

🔄 Data Pipeline Architecture

Data Ingestion

Raw CSV ingested into Databricks

Data Transformation (PySpark)

Handling missing values

Aggregating sales by product, aisle, store, and date

Workflow Orchestration (Airflow)

DAG scheduled to run daily

Automated transformation and load steps

Analytics & Visualization

Aggregated outputs consumed in Power BI

KPIs and trends visualized for business insights

📈 Power BI Dashboard

Key insights delivered:

Top 10 products by total sales

Top performing stores and aisles

Weekly and daily sales trends

Interactive filtering by date, store, and category

📷 Dashboard snapshots:




📊 Key KPIs

Total Sales

Average Daily Sales

Weekly Sales Trend

Top Product Contribution

Sample SQL Analysis

SQL queries used for validation and exploratory analysis are available in:

/sql/sales_analysis.sql

🚀 How to Run (Optional Section)

Load dataset into Databricks

Run PySpark notebook for transformations

Configure and trigger Airflow DAG

Connect Power BI to processed tables

🎯 What This Project Demonstrates

End-to-end data engineering workflow

Scalable data processing using Spark

Pipeline orchestration with Airflow

Business-focused analytics and visualization

Clean, production-style project structure

📌 Future Improvements

Add cloud storage (S3 / ADLS)

Implement incremental loads

Add data quality checks

Deploy dashboard to Power BI Service

👤 Author

Tanvi Chinnapa
Aspiring Data Engineer / Analytics Engineer
Location: Europe
Skills: SQL | Python | Spark | Airflow | Power BI | AWS (in progress)
