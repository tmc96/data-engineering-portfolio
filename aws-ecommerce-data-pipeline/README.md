[README.md](https://github.com/user-attachments/files/27573078/README.md)
# 🛒 Olist E-Commerce AWS Data Pipeline

> An end-to-end batch data pipeline that processes Brazilian e-commerce transactions from raw source data into a structured analytical data lake, enabling business insights on sales performance, customer behaviour, seller metrics, and delivery efficiency — built entirely on AWS.


## 🏗️ Architecture

<img width="743" height="696" alt="architecture" src="https://github.com/user-attachments/assets/0b49700b-fc94-4f7a-91ac-22b77eb1fb02" />


> **Bronze → Silver → Gold lakehouse architecture** orchestrated by AWS Step Functions

```
Olist CSV Files (Kaggle)
        │
        ▼
┌─────────────────┐
│   S3 – Bronze   │  Raw CSV ingestion layer
│   (8 tables)    │
└────────┬────────┘
         │  AWS Glue Crawler
         ▼
┌─────────────────┐
│  Glue Data      │  Schema discovery & metadata registry
│  Catalog        │
└────────┬────────┘
         │  AWS Glue ETL Job (PySpark)
         ▼
┌─────────────────┐
│   S3 – Silver   │  Cleaned & typed Parquet files
│  (7 tables)     │  Partitioned by year/month
└────────┬────────┘
         │  AWS Glue ETL Job (PySpark)
         ▼
┌─────────────────┐
│   S3 – Gold     │  Star schema — fact + dimension tables
│  (4 tables)     │  Partitioned by year/month
└────────┬────────┘
         │
    ┌────┴─────┐
    ▼          ▼
┌────────┐  ┌──────────────────┐
│ Athena │  │ Redshift         │
│ (ad    │  │ Serverless       │
│ hoc    │  │ (coming soon)    │
│ SQL)   │  └──────────────────┘
└────────┘

Orchestration:  AWS Step Functions
Monitoring:     AWS CloudWatch
Failure Alerts: AWS Lambda + Amazon SNS (email)
```

---

## 🛠️ Tech Stack

| Layer | Service | Purpose |
|-------|---------|---------|
| Storage | Amazon S3 | Bronze / Silver / Gold data lake |
| Cataloguing | AWS Glue Crawler + Data Catalog | Schema discovery & metadata |
| Transformation | AWS Glue ETL (PySpark) | Data cleaning & star schema |
| Orchestration | AWS Step Functions | End-to-end pipeline workflow |
| Query | Amazon Athena | Serverless SQL on S3 |
| Warehouse | Amazon Redshift Serverless | Analytical warehouse (in progress) |
| Alerting | AWS Lambda + Amazon SNS | Email alerts on pipeline failure |
| Monitoring | AWS CloudWatch | Logs & metrics |
| IaC | AWS IAM | Roles & permissions |

---

## 📋 Business Problem

E-commerce platforms generate large volumes of transactional data across orders, products, customers, sellers, payments, and reviews. Without a structured data pipeline, this data sits in isolated CSV exports — impossible to query efficiently or analyse at scale.

This project builds a production-style AWS data pipeline that:
- **Ingests** raw Olist e-commerce data into a scalable S3 data lake
- **Transforms** it from raw CSVs into clean, typed, partitioned Parquet files
- **Models** it into a star schema optimised for analytical queries
- **Orchestrates** the full pipeline with failure alerting
- **Delivers** actionable business insights via Athena SQL queries

---

## 📦 Dataset

**[Olist Brazilian E-Commerce Public Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)** — Kaggle

| Table | Description | Rows (approx) |
|-------|-------------|----------------|
| orders | Order status and timestamps | 99,441 |
| order_items | Products and sellers per order | 112,650 |
| customers | Customer location data | 99,441 |
| products | Product catalogue and dimensions | 32,951 |
| sellers | Seller location data | 3,095 |
| payments | Payment methods and values | 103,886 |
| reviews | Customer review scores and comments | 99,224 |
| geolocation | Brazilian zip code coordinates | 1,000,163 |

> **Note:** All product category names are in Portuguese as this is a Brazilian dataset. e.g. `beleza_saude` = health & beauty, `relogios_presentes` = watches & gifts.

---

## 🏛️ Data Model — Star Schema

```
                    ┌─────────────────┐
                    │  dim_customers  │
                    │─────────────────│
                    │ customer_id  PK │
                    │ customer_city   │
                    │ customer_state  │
                    └────────┬────────┘
                             │
┌─────────────────┐  ┌───────┴──────────┐  ┌─────────────────┐
│  dim_products   │  │   fact_orders    │  │  dim_sellers    │
│─────────────────│  │──────────────────│  │─────────────────│
│ product_id   PK │◄─│ order_id         │─►│ seller_id    PK │
│ category_name   │  │ customer_id   FK │  │ seller_city     │
│ product_weight  │  │ product_id    FK │  │ seller_state    │
│ dimensions      │  │ seller_id     FK │  └─────────────────┘
└─────────────────┘  │ order_status     │
                     │ order_date       │
                     │ order_year       │
                     │ order_month      │
                     │ price            │
                     │ freight_value    │
                     │ total_item_value │
                     │ payment_value    │
                     │ delivery_delay   │
                     │ is_late_delivery │
                     │ review_score     │
                     │ freight_ratio    │
                     └──────────────────┘
```

---

## 🔄 Pipeline Layers Explained

### Bronze Layer — Raw Ingestion
- Raw CSV files uploaded directly to S3 as-is
- No transformations applied — preserves original source data
- Glue Crawler scans and registers schema in Data Catalog
- Path: `s3://olist-pipeline-tanvi/bronze/`

### Silver Layer — Cleaned & Typed
- CSVs converted to **Parquet** (columnar, compressed, faster to query)
- Timestamp strings cast to proper timestamp types
- Null values handled per business rules (drop vs fill)
- Duplicates removed on primary keys
- Derived columns added (e.g. `delivery_delay_days`, `is_late_delivery`, `total_item_value`)
- Payments aggregated to one row per order
- Partitioned by `order_year` / `order_month`
- Path: `s3://olist-pipeline-tanvi/silver/`

### Gold Layer — Star Schema
- Dimension tables built from cleaned Silver tables (`dim_customers`, `dim_products`, `dim_sellers`)
- Central fact table built by joining orders + items + payments + reviews
- Additional derived metric: `freight_ratio` (freight as % of item price)
- Optimised for analytical queries — minimal joins needed at query time
- Partitioned by `order_year` / `order_month` for Athena cost optimisation
- Path: `s3://olist-pipeline-tanvi/gold/`

---

## ⚙️ Pipeline Orchestration — Step Functions

The full pipeline is orchestrated by an AWS Step Functions state machine:

```
Start
  → Run Bronze Crawler      (refresh Data Catalog)
  → Poll until complete
  → Run Silver ETL Job      (Bronze → Silver transformation)
  → Run Gold ETL Job        (Silver → Gold star schema)
  → Run Gold Crawler        (refresh Gold Data Catalog)
  → Poll until complete
  → Pipeline Succeeded
  → [On any failure] → Lambda → SNS email alert → Pipeline Failed
End
```

**Failure alerting:** Any step failure triggers a Lambda function that sends an email via SNS with the failed state name, error details, execution ID, and a direct link to CloudWatch logs.

---

## 📊 Business Insights

All queries run on Amazon Athena against the Gold layer Parquet files in S3.

### Query 1 — Top 10 Product Categories by Revenue
```sql
SELECT 
    p.product_category_name,
    COUNT(DISTINCT f.order_id)     AS total_orders,
    ROUND(SUM(f.price), 2)         AS total_revenue,
    ROUND(AVG(f.price), 2)         AS avg_order_value
FROM fact_orders f
JOIN dim_products p ON f.product_id = p.product_id
WHERE f.order_status = 'delivered'
GROUP BY p.product_category_name
ORDER BY total_revenue DESC
LIMIT 10;
```
<img width="1510" height="630" alt="query1" src="https://github.com/user-attachments/assets/fa1b7888-b9ce-4501-a798-e6b2d0cd2867" />


**Insight:** Health & beauty and watches & gifts are the top revenue-generating categories, informing inventory and marketing investment decisions.

---

### Query 2 — Monthly Order Volume & Revenue Trend
```sql
SELECT
    order_year,
    order_month,
    COUNT(DISTINCT order_id)    AS total_orders,
    ROUND(SUM(price), 2)        AS monthly_revenue,
    COUNT(DISTINCT customer_id) AS unique_customers
FROM fact_orders
WHERE order_status = 'delivered'
GROUP BY order_year, order_month
ORDER BY order_year, order_month;
```
<img width="1608" height="800" alt="query2" src="https://github.com/user-attachments/assets/c321525d-95a8-4cf5-8b2a-6a9060eb414c" />


**Insight:** Clear month-over-month growth through 2017–2018, with a notable spike in November 2017 (Black Friday). Demonstrates the pipeline handles time-series analysis effectively.

---

### Query 3 — Delivery Performance by Seller State
```sql
SELECT
    s.seller_state,
    COUNT(DISTINCT f.order_id)                            AS total_orders,
    ROUND(AVG(CAST(f.delivery_delay_days AS DOUBLE)), 2)  AS avg_delay_days,
    ROUND(
        SUM(CASE WHEN f.is_late_delivery = true THEN 1 ELSE 0 END) 
        * 100.0 / COUNT(*), 2
    )                                                      AS late_delivery_pct,
    ROUND(AVG(CAST(f.review_score AS DOUBLE)), 2)         AS avg_review_score
FROM fact_orders f
JOIN dim_sellers s ON f.seller_id = s.seller_id
WHERE f.order_status = 'delivered'
    AND f.delivery_delay_days IS NOT NULL
GROUP BY s.seller_state
HAVING COUNT(DISTINCT f.order_id) > 50
ORDER BY late_delivery_pct DESC;
```
<img width="1511" height="719" alt="query3" src="https://github.com/user-attachments/assets/8ef5f61b-3dcf-4996-8c52-e6fc4f64a74e" />


**Insight:** Remote northern states show significantly higher late delivery rates, which directly correlates with lower review scores — a key operational risk signal.

---

### Query 4 — Customer Satisfaction vs Delivery Performance
```sql
SELECT
    CASE 
        WHEN is_late_delivery = true  THEN 'Late'
        WHEN is_late_delivery = false THEN 'On Time'
        ELSE 'Not Delivered'
    END                                           AS delivery_status,
    COUNT(DISTINCT order_id)                      AS total_orders,
    ROUND(AVG(CAST(review_score AS DOUBLE)), 2)   AS avg_review_score,
    SUM(CASE WHEN CAST(review_score AS INT) = 5 THEN 1 ELSE 0 END) AS five_star,
    SUM(CASE WHEN CAST(review_score AS INT) = 1 THEN 1 ELSE 0 END) AS one_star
FROM fact_orders
WHERE review_score IS NOT NULL
GROUP BY is_late_delivery
ORDER BY avg_review_score DESC;
```
<img width="1513" height="270" alt="query4" src="https://github.com/user-attachments/assets/a2b8babb-2bcf-46a3-844c-811dafd9724d" />


**Insight:** On-time deliveries average ~4.2 stars vs ~2.8 stars for late deliveries — quantifying the direct business cost of logistics failures on customer satisfaction.

---

### Query 5 — Top 10 Sellers by Revenue & Performance
```sql
SELECT
    f.seller_id,
    s.seller_state,
    COUNT(DISTINCT f.order_id)                            AS total_orders,
    ROUND(SUM(f.price), 2)                                AS total_revenue,
    ROUND(AVG(CAST(f.review_score AS DOUBLE)), 2)         AS avg_review_score,
    ROUND(AVG(CAST(f.delivery_delay_days AS DOUBLE)), 2)  AS avg_delay_days,
    ROUND(
        SUM(CASE WHEN f.is_late_delivery = true THEN 1 ELSE 0 END) 
        * 100.0 / COUNT(*), 2
    )                                                      AS late_delivery_pct
FROM fact_orders f
JOIN dim_sellers s ON f.seller_id = s.seller_id
WHERE f.order_status = 'delivered'
GROUP BY f.seller_id, s.seller_state
HAVING COUNT(DISTINCT f.order_id) > 20
ORDER BY total_revenue DESC
LIMIT 10;
```
<img width="1520" height="637" alt="query5" src="https://github.com/user-attachments/assets/82220eef-f86e-4641-b088-c9b499db00a2" />


**Insight:** Top sellers by revenue don't always have the best review scores — this query surfaces high-revenue sellers with poor delivery performance, a key business risk indicator.

---

## 📁 Repository Structure

```
aws-ecommerce-data-pipeline/
│
├── glue_jobs/
│   ├── bronze_to_silver_orders.py          # Orders ETL job
│   ├── bronze_to_silver_all_tables.py      # All tables ETL job
│   └── silver_to_gold.py                   # Star schema ETL job
│
├── lambda/
│   └── pipeline_failure_alert.py           # SNS failure alert function
│
├── step_functions/
│   └── olist_pipeline_state_machine.json   # Step Functions definition
│
├── athena_queries/
│   ├── 01_top_categories_by_revenue.sql
│   ├── 02_monthly_order_trend.sql
│   ├── 03_delivery_performance_by_state.sql
│   ├── 04_satisfaction_vs_delivery.sql
│   └── 05_top_sellers_performance.sql
│
├── docs/
│   └── architecture.png                    # Architecture diagram
│
└── README.md
```

---

## 🚀 How to Reproduce

### Prerequisites
- AWS Account with IAM user (AdministratorAccess)
- AWS CLI configured
- Python 3.8+
- Kaggle account (to download dataset)

### Setup Steps

**1. Download the dataset**
```bash
# Install Kaggle CLI
pip install kaggle

# Download Olist dataset
kaggle datasets download -d olistbr/brazilian-ecommerce
unzip brazilian-ecommerce.zip -d olist_data/
```

**2. Create S3 bucket and upload data**
```
Bucket name: olist-pipeline-[yourname]
Region:      eu-north-1 (Stockholm)

Folder structure:
  bronze/orders/
  bronze/order_items/
  bronze/customers/
  bronze/products/
  bronze/sellers/
  bronze/payments/
  bronze/reviews/
  bronze/geolocation/
  silver/
  gold/
  scripts/
  athena-results/
```

**3. Create IAM Roles**
- `GlueS3Role` — for Glue jobs (AmazonS3FullAccess + AWSGlueServiceRole)
- `RedshiftS3Role` — for Redshift (AmazonS3FullAccess + AmazonRedshiftFullAccess)

**4. Run Glue Crawlers**
- Create and run `olist-bronze-crawler` pointing to `s3://your-bucket/bronze/`
- Target database: `olist_bronze_db`

**5. Deploy Glue ETL Jobs**
- Upload scripts from `glue_jobs/` to S3 `scripts/` folder
- Create jobs in AWS Glue console pointing to each script
- IAM Role: `GlueS3Role` | Glue version: 4.0 | Workers: G.1X x2

**6. Deploy Lambda Function**
- Runtime: Python 3.12
- Upload code from `lambda/pipeline_failure_alert.py`
- Environment variable: `SNS_TOPIC_ARN` = your SNS topic ARN

**7. Create SNS Topic**
- Topic name: `olist-pipeline-alerts`
- Add email subscription and confirm

**8. Deploy Step Functions**
- Create state machine from `step_functions/olist_pipeline_state_machine.json`

**9. Configure Athena**
- Query result location: `s3://your-bucket/athena-results/`
- Database: `olist_gold_db`

**10. Run the pipeline**
- Go to Step Functions → `olist-pipeline-orchestration` → Start execution

---

## 💰 Cost Estimate

This project was built and runs within the **AWS Free Tier** with minimal cost:

| Service | Usage | Estimated Cost |
|---------|-------|----------------|
| S3 | ~500MB storage | < $0.01/month |
| Glue ETL | ~10 DPU hours total | ~$4.40 |
| Glue Crawlers | ~5 runs | ~$0.15 |
| Athena | ~50MB scanned | < $0.01 |
| Step Functions | ~10 executions | Free tier |
| Lambda | ~10 invocations | Free tier |
| SNS | ~10 emails | Free tier |
| **Total** | | **~$5.00** |

---

## 🔮 Future Improvements

- [ ] **Redshift Serverless** — Load Gold layer into Redshift for warehouse analytics
- [ ] **Streaming pipeline** — Add Kinesis Firehose for real-time order event ingestion (Project 2)
- [ ] **Data quality checks** — Add Great Expectations validation between Bronze → Silver
- [ ] **English category names** — Add Portuguese → English translation mapping in Glue job
- [ ] **QuickSight dashboard** — Connect to Gold layer for visual business reporting
- [ ] **Terraform IaC** — Infrastructure as code for reproducible deployment

---

## 👩‍💻 Author

**Tanvi Chinnapa**
M.Sc. Computer Aided Mechanical Engineering | AWS Data Engineer

[![GitHub](https://img.shields.io/badge/GitHub-tmc96-black?logo=github)](https://github.com/tmc96/data-engineering-portfolio)

---

## 📄 License

MIT License — feel free to use this project as a reference for your own AWS data engineering portfolio.
