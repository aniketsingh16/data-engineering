import dlt
from pyspark.sql.functions import *

# create materialized view

@dlt.table(
    name = "business_sales"
)
def business_sales():
    df_fact = spark.read.table("fact_sales")
    df_dimProducts = spark.read.table("dim_products")
    df_dimCustomers = spark.read.table("dim_customers")

    df_join = df_fact.join(df_dimCustomers, df_fact.customer_id == df_dimCustomers.customer_id, "inner").join(df_dimProducts, df_fact.product_id == df_dimProducts.product_id, "inner")

    df_pruned = df_join.select("region", "category", "total_amount")
    df_agg = df_pruned.groupBy("region", "category").agg(sum("total_amount").alias("total_revenue"))
    
    return df_agg