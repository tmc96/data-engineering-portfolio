# 📊 FMCG Sales Data Engineering & Analytics Pipeline

##  Project Overview
This project showcases the design and implementation of an **end-to-end data engineering and analytics pipeline** using an FMCG retail sales dataset.

The objective is to transform **raw transactional data** into **business-ready analytics**, enabling stakeholders to track sales performance, identify top products and stores, and analyze trends through an interactive **Power BI dashboard**.

This project reflects real-world data engineering practices, including scalable data processing, workflow orchestration, and analytics delivery.

---

##  Tech Stack
- **SQL** – Data exploration, validation, and aggregations  
- **PySpark (Databricks)** – Scalable data cleaning and transformation  
- **Apache Airflow** – Pipeline orchestration and scheduling  
- **Power BI** – Business intelligence, KPIs, and dashboards  
- **Python** – Supporting scripts and data analysis  

---

##  Dataset
**Source:** Kaggle – Grocery Store Sales Dataset  
**Volume:** ~1,900 transactional records  

### Key Attributes
- Transaction Date  
- Store Name  
- Aisle  
- Product Name  
- Quantity Sold  
- Final Sales Amount  

---

##  Data Pipeline Architecture

### 1 Data Ingestion
- Raw CSV sales data ingested into **Databricks**
- Dataset prepared for distributed processing

### 2 Data Transformation (PySpark)
- Data cleaning and quality improvement
- Handling missing and inconsistent values
- Aggregation of sales metrics by:
  - Product
  - Aisle
  - Store
  - Date

### 3 Workflow Orchestration (Apache Airflow)
- End-to-end pipeline organized using an **Airflow DAG**
- Daily scheduled execution
- Automated transformation and load steps

### 4 Analytics & Visualization
- Curated, aggregated tables exposed to **Power BI**
- KPI-driven dashboards built for business analysis

---

##  Power BI Dashboard

### Business Insights Delivered
- Top 10 products by total sales
- Best-performing stores and aisles
- Daily and weekly sales trends
- Interactive filtering by date for deeper analysis

---

##  Key KPIs
- Total Sales  
- Average Daily Sales  
- Weekly Sales Trend  
- Top Product Contribution  

---

##  Sample SQL Analysis
SQL queries used for exploratory analysis and data validation are available here:

```text
/sql/sales_analysis.sql

---

## ▶️ **How to Run**
1. Ingest raw FMCG sales data into **Databricks**
2. Execute **PySpark notebooks** to perform data cleaning and aggregations
3. Configure and trigger the **Apache Airflow DAG** for pipeline orchestration
4. Connect **Power BI** to the processed tables to analyze KPIs and trends

---

## 💡 **What This Project Demonstrates**
- Design and implementation of an **end-to-end data engineering pipeline**
- Scalable data transformation using **Apache Spark**
- Workflow orchestration and automation with **Apache Airflow**
- Application of **analytics engineering principles**
- Conversion of raw transactional data into **business-ready insights**
- Delivery of KPI-driven dashboards for decision-making

---

## 🚀 **Future Improvements**
- Integrate cloud-based storage such as **AWS S3** or **Azure Data Lake**
- Implement **incremental and partitioned data loads**
- Add automated **data quality checks and monitoring**
- Deploy dashboards to **Power BI Service** for broader stakeholder access
- Introduce **CI/CD pipelines** for data and analytics workflows

👤 Author

Tanvi Chinnapa
Aspiring Data Engineer / Analytics Engineer
Location: Europe
Skills: SQL | Python | Spark | Airflow | Power BI
