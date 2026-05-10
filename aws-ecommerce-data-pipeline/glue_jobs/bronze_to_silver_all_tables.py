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
# SparkContext is the entry point for Spark functionality
# GlueContext wraps SparkContext and adds Glue-specific features
# spark session is what we use to read/write data
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# Base S3 path — change this if your bucket name is different
BUCKET = "s3://olist-pipeline-tanvi"

# ============================================================
# 1. CUSTOMERS TABLE
# ============================================================
# We read directly from S3 using spark.read instead of the 
# Glue Data Catalog — this ensures headers are recognised
print("Processing customers...")
customers_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(f"{BUCKET}/bronze/customers/")

# Print schema so we can verify column names in the logs
customers_df.printSchema()

# Remove duplicate customer entries based on customer_id
# A customer should only appear once in our dimension table
customers_df = customers_df.dropDuplicates(["customer_id"])

# Drop rows where critical identifier columns are null
# We can't use a customer record without an ID
customers_df = customers_df.dropna(subset=["customer_id"])

# Standardise the city name to uppercase for consistency
# e.g. "sao paulo" and "Sao Paulo" become "SAO PAULO"
customers_df = customers_df.withColumn(
    "customer_city",
    F.upper(F.col("customer_city"))
)

print(f"Total customers after cleaning: {customers_df.count()}")

# Write to Silver layer as Parquet
# Parquet is a columnar format — much faster to query than CSV
# and uses significantly less storage space
customers_df.write \
    .mode("overwrite") \
    .parquet(f"{BUCKET}/silver/customers_cleaned/")

print("Customers done!")

# ============================================================
# 2. PRODUCTS TABLE
# ============================================================
print("Processing products...")
products_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(f"{BUCKET}/bronze/products/")

products_df.printSchema()

# Fill missing category names with "unknown"
# rather than dropping the row — products without a category
# are still useful for revenue calculations
products_df = products_df.fillna(
    {"product_category_name": "unknown"}
)

# Drop rows where product_id is null — we can't use 
# a product record without its primary key
products_df = products_df.dropna(subset=["product_id"])

# Fill missing numeric measurements with 0
# These are physical dimensions — null means not recorded
numeric_cols = [
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]
products_df = products_df.fillna(0, subset=numeric_cols)

print(f"Total products after cleaning: {products_df.count()}")

products_df.write \
    .mode("overwrite") \
    .parquet(f"{BUCKET}/silver/products_cleaned/")

print("Products done!")

# ============================================================
# 3. SELLERS TABLE
# ============================================================
print("Processing sellers...")
sellers_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(f"{BUCKET}/bronze/sellers/")

sellers_df.printSchema()

# Remove duplicate seller records
sellers_df = sellers_df.dropDuplicates(["seller_id"])

# Drop rows where seller_id is null
sellers_df = sellers_df.dropna(subset=["seller_id"])

# Standardise city names to uppercase
sellers_df = sellers_df.withColumn(
    "seller_city",
    F.upper(F.col("seller_city"))
)

print(f"Total sellers after cleaning: {sellers_df.count()}")

sellers_df.write \
    .mode("overwrite") \
    .parquet(f"{BUCKET}/silver/sellers_cleaned/")

print("Sellers done!")

# ============================================================
# 4. ORDER ITEMS TABLE
# ============================================================
print("Processing order items...")
order_items_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(f"{BUCKET}/bronze/order_items/")

order_items_df.printSchema()

# Drop rows where critical keys are null
# We need all three to join this table with others
order_items_df = order_items_df.dropna(
    subset=["order_id", "product_id", "seller_id"]
)

# Calculate total item value = price + freight
# This gives us the true cost per item to the customer
order_items_df = order_items_df.withColumn(
    "total_item_value",
    F.col("price") + F.col("freight_value")
)

# Cast shipping_limit_date to proper timestamp
order_items_df = order_items_df.withColumn(
    "shipping_limit_date",
    F.to_timestamp(F.col("shipping_limit_date"))
)

print(f"Total order items after cleaning: {order_items_df.count()}")

order_items_df.write \
    .mode("overwrite") \
    .parquet(f"{BUCKET}/silver/order_items_cleaned/")

print("Order items done!")

# ============================================================
# 5. PAYMENTS TABLE
# ============================================================
print("Processing payments...")
payments_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(f"{BUCKET}/bronze/payments/")

payments_df.printSchema()

# Drop rows where order_id is null
payments_df = payments_df.dropna(subset=["order_id"])

# One order can have multiple payment methods
# e.g. part credit card, part voucher
# We aggregate to get total payment value per order
payments_agg_df = payments_df.groupBy("order_id").agg(
    # Sum all payment values for this order
    F.sum("payment_value").alias("total_payment_value"),
    # Count how many payment installments
    F.sum("payment_installments").alias("total_installments"),
    # Collect all payment types used (e.g. ["credit_card", "voucher"])
    F.collect_set("payment_type").alias("payment_types"),
    # Count distinct payment methods used
    F.countDistinct("payment_type").alias("num_payment_methods")
)

print(f"Total orders with payments: {payments_agg_df.count()}")

payments_agg_df.write \
    .mode("overwrite") \
    .parquet(f"{BUCKET}/silver/payments_cleaned/")

print("Payments done!")

# ============================================================
# 6. REVIEWS TABLE
# ============================================================
print("Processing reviews...")
reviews_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(f"{BUCKET}/bronze/reviews/")

reviews_df.printSchema()

# Drop rows without an order_id — we need this to join
reviews_df = reviews_df.dropna(subset=["order_id"])

# review_score should be between 1 and 5
# Filter out any invalid scores outside this range
reviews_df = reviews_df.filter(
    (F.col("review_score") >= 1) & 
    (F.col("review_score") <= 5)
)
