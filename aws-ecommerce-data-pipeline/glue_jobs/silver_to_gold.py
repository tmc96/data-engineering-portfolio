import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F

# ============================================================
# INITIALIZE GLUE + SPARK
# ============================================================
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

BUCKET = "s3://olist-pipeline-tanvi"

# ============================================================
# READ ALL SILVER TABLES
# ============================================================
# We read Parquet files this time — not CSVs
# Parquet is faster to read because it's columnar and compressed
print("Reading Silver layer tables...")

orders_df = spark.read.parquet(
    f"{BUCKET}/silver/orders_cleaned/"
)

order_items_df = spark.read.parquet(
    f"{BUCKET}/silver/order_items_cleaned/"
)

customers_df = spark.read.parquet(
    f"{BUCKET}/silver/customers_cleaned/"
)

products_df = spark.read.parquet(
    f"{BUCKET}/silver/products_cleaned/"
)

sellers_df = spark.read.parquet(
    f"{BUCKET}/silver/sellers_cleaned/"
)

payments_df = spark.read.parquet(
    f"{BUCKET}/silver/payments_cleaned/"
)

reviews_df = spark.read.parquet(
    f"{BUCKET}/silver/reviews_cleaned/"
)

# ============================================================
# BUILD DIMENSION TABLES (the "dim_" tables)
# ============================================================
# Dimension tables describe the WHO, WHAT, WHERE of your data
# They are small, descriptive, and don't change often
# Think of them as lookup/reference tables

# ---- dim_customers ----
# Select only the columns we need for analysis
# We don't need every column from the Silver table
print("Building dim_customers...")
dim_customers = customers_df.select(
    "customer_id",
    "customer_unique_id",  # the true unique customer identifier
    "customer_city",
    "customer_state",
    "customer_zip_code_prefix"
)

dim_customers.write \
    .mode("overwrite") \
    .parquet(f"{BUCKET}/gold/dim_customers/")

print(f"dim_customers rows: {dim_customers.count()}")

# ---- dim_products ----
print("Building dim_products...")
dim_products = products_df.select(
    "product_id",
    "product_category_name",
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
)

dim_products.write \
    .mode("overwrite") \
    .parquet(f"{BUCKET}/gold/dim_products/")

print(f"dim_products rows: {dim_products.count()}")

# ---- dim_sellers ----
print("Building dim_sellers...")
dim_sellers = sellers_df.select(
    "seller_id",
    "seller_city",
    "seller_state",
    "seller_zip_code_prefix"
)

dim_sellers.write \
    .mode("overwrite") \
    .parquet(f"{BUCKET}/gold/dim_sellers/")

print(f"dim_sellers rows: {dim_sellers.count()}")

# ============================================================
# BUILD FACT TABLE (the "fact_orders" table)
# ============================================================
# The fact table is the CENTER of the star schema
# It contains measurable business events — in this case orders
# It connects to all dimension tables via foreign keys
# Think of it as: WHAT happened (with numbers attached)

print("Building fact_orders...")

# Step 1 — Start with orders as the base
# Every row in fact_orders represents one order-item combination
# We join order_items first because one order can have
# multiple items — each item becomes its own fact row
fact_df = orders_df.join(
    order_items_df,
    on="order_id",
    # inner join = only keep rows that exist in BOTH tables
    # orders without items and items without orders are excluded
    how="inner"
)

# Step 2 — Join payments to get financial totals per order
# left join = keep all orders even if payment data is missing
fact_df = fact_df.join(
    payments_df,
    on="order_id",
    how="left"
)

# Step 3 — Join reviews to get customer satisfaction score
# left join = keep all orders even without a review
fact_df = fact_df.join(
    reviews_df.select("order_id", "review_score", "has_comment"),
    on="order_id",
    how="left"
)

# Step 4 — Select only the columns we need in the fact table
# Foreign keys (customer_id, product_id, seller_id) link
# this table to the dimension tables — this is the star schema
fact_df = fact_df.select(
    # Primary identifier
    "order_id",

    # Foreign keys — link to dimension tables
    "customer_id",
    "product_id",
    "seller_id",

    # Order details
    "order_status",
    "order_purchase_timestamp",
    "order_year",
    "order_month",

    # Delivery metrics
    "order_estimated_delivery_date",
    "order_delivered_customer_date",
    "delivery_delay_days",
    "is_late_delivery",

    # Financial measures — the actual numbers we analyse
    "price",
    "freight_value",
    "total_item_value",
    "total_payment_value",
    "total_installments",

    # Customer satisfaction
    "review_score",
    "has_comment"
)

# Step 5 — Add a derived metric: freight as % of item price
# High freight ratio = expensive to deliver relative to price
# Useful for seller and product performance analysis
fact_df = fact_df.withColumn(
    "freight_ratio",
    F.round(
        F.col("freight_value") / F.col("price") * 100,
        2  # round to 2 decimal places
    )
)

print(f"fact_orders rows: {fact_df.count()}")
fact_df.show(5)

# Write fact table partitioned by year and month
# Partitioning means Athena/Redshift only scans the 
# partition you query — much faster and cheaper
fact_df.write \
    .mode("overwrite") \
    .partitionBy("order_year", "order_month") \
    .parquet(f"{BUCKET}/gold/fact_orders/")

print("fact_orders done!")

# ============================================================
# ALL DONE
# ============================================================
print("Gold layer complete! Star schema is ready.")
job.commit()
