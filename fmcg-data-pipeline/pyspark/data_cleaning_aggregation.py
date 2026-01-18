# Databricks notebook source
df = spark.table("default.grocery_chain_data")

df.printSchema()
df.show(10)
df.count()

# COMMAND ----------

df.printSchema()
df.show(5, truncate=False)

# COMMAND ----------

#Null inspection
from pyspark.sql.functions import col

df.select([
    col(c).isNull().alias(c) for c in df.columns
]).show()

# COMMAND ----------

#Computes statitistics
df.describe().show()

# COMMAND ----------

#Standardize column names, column cleaning function
def clean_column_name(c):
    return (
        c.lower()
         .replace(" ", "_")
         .replace("-", "_")
         .replace("/", "_")
    )

# COMMAND ----------

#Apply cleaned names and create new dataframe
df_clean = df.select([
    col(c).alias(clean_column_name(c)) for c in df.columns
])

# COMMAND ----------

#Fixing data types
from pyspark.sql.types import IntegerType, DoubleType
from pyspark.sql.functions import col

df_clean = (
    df_clean
    .withColumn("quantity", col("quantity").cast(IntegerType()))
    .withColumn("loyalty_points", col("loyalty_points").cast(IntegerType()))
    .withColumn("unit_price", col("unit_price").cast(DoubleType()))
    .withColumn("total_amount", col("total_amount").cast(DoubleType()))
    .withColumn("discount_amount", col("discount_amount").cast(DoubleType()))
    .withColumn("final_amount", col("final_amount").cast(DoubleType()))
)

# COMMAND ----------

#Date casting
from pyspark.sql.functions import to_date

df_clean = df_clean.withColumn(
    "transaction_date",
    to_date(col("transaction_date"), "yyyy-MM-dd")
)

# COMMAND ----------

# Drop rows missing critical business dimensions
df_clean = df_clean.dropna(
    subset=[
        "customer_id",
        "store_name",
        "transaction_date",
        "product_name"
    ]
)

# Fill safe defaults for non-critical numeric fields
df_clean = df_clean.fillna({
    "quantity": 0,
    "discount_amount": 0.0,
    "loyalty_points": 0
})

# COMMAND ----------

from pyspark.sql.functions import col, sum

df_clean.select([
    sum(col(c).isNull().cast("int")).alias(c)
    for c in df_clean.columns
]).show()

# COMMAND ----------

df_clean.count()
df_clean.show(10)

# COMMAND ----------

from pyspark.sql.functions import col, length, trim

df_clean.filter(
    trim(col("store_name")) == ""
).show(10, truncate=False)

# COMMAND ----------

from pyspark.sql.functions import when, trim

df_clean = df_clean.withColumn(
    "store_name",
    when(trim(col("store_name")) == "", None)
    .otherwise(col("store_name"))
)

# COMMAND ----------

df_clean = df_clean.dropna(subset=["store_name"])

# COMMAND ----------

df_clean.select(
    col("store_name"),
).count()

df_clean.select([
    sum(col(c).isNull().cast("int")).alias(c)
    for c in df_clean.columns
]).show()

# COMMAND ----------

from pyspark.sql.functions import trim, when, col

string_cols = [
    "customer_id",
    "aisle",
    "product_name"
]

for c in string_cols:
    df_clean = df_clean.withColumn(
        c,
        when(trim(col(c)) == "", None).otherwise(col(c))
    )

# COMMAND ----------

df_clean = df_clean.dropna(subset=["customer_id",
    "aisle",
    "product_name"])

# COMMAND ----------

#Save as new cleaned table
df_clean.write.mode("overwrite").saveAsTable(
    "default.grocery_store_sales_clean"
)

# COMMAND ----------

df = spark.table("default.grocery_store_sales_clean")


# COMMAND ----------

import base64
from IPython.display import HTML
df = spark.table("default.grocery_store_sales_clean")
df.printSchema()
# Convert to pandas DataFrame
pandas_df = df.toPandas()


csv_data = pandas_df.to_csv(index=False)
b64 = base64.b64encode(csv_data.encode()).decode()

HTML(f'<a download="cleaned_fmcg_data.csv" href="data:text/csv;base64,{b64}">Click here to download cleaned_fmcg_data.csv</a>')

# COMMAND ----------

spark.sql("SHOW TABLES").show()

# COMMAND ----------

from pyspark.sql.functions import year, month, weekofyear

df_transformed = (
    df
    .withColumn("year", year("transaction_date"))
    .withColumn("month", month("transaction_date"))
    .withColumn("week", weekofyear("transaction_date"))
)

#df_transformed.show(10)

# COMMAND ----------

from pyspark.sql.functions import when, col

df_transformed = df_transformed.withColumn(
    "has_discount",
    when(col("discount_amount") > 0, 1).otherwise(0)
)

#df_transformed.show(10)

# COMMAND ----------

df_transformed = df_transformed.filter(
    (col("quantity") >= 0) &
    (col("final_amount") >= 0) &
    (col("unit_price") >= 0)
)


# COMMAND ----------

df_transformed.printSchema()
df_transformed.show(5, truncate=False)
df_transformed.count()

# COMMAND ----------

df_transformed.write.mode("overwrite").saveAsTable(
    "default.grocery_store_sales_transformed"
)

# COMMAND ----------

df = spark.table("default.grocery_store_sales_transformed")
df.printSchema()

# COMMAND ----------

import base64
from IPython.display import HTML
df = spark.table("default.grocery_store_sales_transformed")
df.printSchema()
# Convert to pandas DataFrame
pandas_df = df.toPandas()


csv_data = pandas_df.to_csv(index=False)
b64 = base64.b64encode(csv_data.encode()).decode()

HTML(f'<a download="cleaned&transformed_fmcg_data.csv" href="data:text/csv;base64,{b64}">Click here to download cleaned&transformed_fmcg_data.csv</a>')

# COMMAND ----------

#Sales by product
from pyspark.sql.functions import sum

sales_by_product = (
    df
    .groupBy("product_name")
    .agg(
        sum("final_amount").alias("total_revenue"),
        sum("quantity").alias("total_units")
    )
)

sales_by_product.orderBy("total_revenue", ascending=False).show(10)

# COMMAND ----------

#Sales by store for store performance
sales_by_store = (
    df
    .groupBy("store_name")
    .agg(
        sum("final_amount").alias("total_revenue"),
        sum("quantity").alias("total_units"),
        sum("has_discount").alias("discounted_transactions")
    )
)

sales_by_store.orderBy("total_revenue", ascending=False).show(10)

# COMMAND ----------

#Daily sales
daily_sales = (
    df
    .groupBy("transaction_date")
    .agg(
        sum("final_amount").alias("daily_revenue"),
        sum("quantity").alias("units_sold")
    )
)

daily_sales.orderBy("transaction_date").show(10)

# COMMAND ----------

#Weekly sales (using derived columns)
weekly_sales = (
    df
    .groupBy("year", "week")
    .agg(
        sum("final_amount").alias("weekly_revenue"),
        sum("quantity").alias("weekly_units")
    )
)

weekly_sales.orderBy("year", "week").show(10)

# COMMAND ----------

#Aisle performance
sales_by_aisle = (
    df
    .groupBy("aisle")
    .agg(
        sum("final_amount").alias("total_revenue"),
        sum("quantity").alias("total_units")
    )
)

sales_by_aisle.orderBy("total_revenue", ascending=False).show(10)

# COMMAND ----------

#Save aggregated tables as gold layer
sales_by_product.write.mode("overwrite").saveAsTable(
    "default.sales_by_product"
)

sales_by_store.write.mode("overwrite").saveAsTable(
    "default.sales_by_store"
)

daily_sales.write.mode("overwrite").saveAsTable(
    "default.daily_sales"
)

weekly_sales.write.mode("overwrite").saveAsTable(
    "default.weekly_sales"
)

sales_by_aisle.write.mode("overwrite").saveAsTable(
    "default.sales_by_aisle"
)

#To check
spark.table("default.sales_by_product").show(5)
spark.table("default.sales_by_store").show(5)
spark.table("default.daily_sales").show(5)

spark.table("default.sales_by_product").count()
