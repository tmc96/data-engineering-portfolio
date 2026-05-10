
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from pyspark.sql.types import TimestampType

## Initialize Glue context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

## ---- ORDERS TABLE ----
print("Reading orders from Bronze layer...")
orders_df = glueContext.create_dynamic_frame.from_catalog(
    database="olist_bronze_db",
    table_name="orders"
).toDF()

## Cast timestamp columns from string to timestamp
timestamp_cols = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in timestamp_cols:
    orders_df = orders_df.withColumn(
        col, F.to_timestamp(F.col(col))
    )

## Calculate delivery delay in days
## Positive = late, Negative = early, Null = not delivered yet
orders_df = orders_df.withColumn(
    "delivery_delay_days",
    F.datediff(
        F.col("order_delivered_customer_date"),
        F.col("order_estimated_delivery_date")
    )
)

## Flag late deliveries
orders_df = orders_df.withColumn(
    "is_late_delivery",
    F.when(F.col("delivery_delay_days") > 0, True).otherwise(False)
)

## Drop rows where order_id or customer_id is null (critical columns)
orders_df = orders_df.dropna(subset=["order_id", "customer_id"])

## Extract year and month for partitioning
orders_df = orders_df.withColumn(
    "order_year",
    F.year(F.col("order_purchase_timestamp"))
).withColumn(
    "order_month",
    F.month(F.col("order_purchase_timestamp"))
)

## Show sample output for logging
print(f"Total orders after cleaning: {orders_df.count()}")
print("Sample output:")
orders_df.show(5)

## Write to Silver layer as Parquet, partitioned by year and month
print("Writing orders to Silver layer...")
orders_df.write \
    .mode("overwrite") \
    .partitionBy("order_year", "order_month") \
    .parquet("s3://olist-pipeline-tanvi/silver/orders_cleaned/")

print("Orders ETL complete!")
job.commit()
