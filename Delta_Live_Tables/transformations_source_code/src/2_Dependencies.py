# import dlt
# from pyspark.sql.functions import col, lower
# @dlt.table
# def staging_orders():
#     df = spark.readStream.table("dlt_project.source.orders")
#     return df

# @dlt.view
# def transformed_orders():
#     df = spark.readStream.table("staging_orders")
#     df = df.withColumn("order_status", lower(col("order_status")))
#     return df



# #Aggregated Data
# @dlt.table
# def aggregated_orders():
#     df = spark.readStream.table("transformed_orders")
#     df = df.groupBy("order_status").count()
#     return df