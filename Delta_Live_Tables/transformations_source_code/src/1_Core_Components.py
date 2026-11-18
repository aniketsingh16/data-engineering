# import dlt
# # Streaming Table 

# @dlt.table(
#     name = "first_stream_table"
# )
# def first_stream_table():
#     df = spark.readStream.table("dlt_project.source.orders")
#     return df

# # Materialized View

# @dlt.table(name = "first_materialized_view")
# def first_materialized_view():
#     df = spark.read.table("dlt_project.source.orders")
#     return df

# # Normal View (Batch)

# @dlt.view(name = "first_batch_view")
# def first_batch_view():
#     df = spark.read.table("dlt_project.source.orders")
#     return df

# # Streaming View
# @dlt.view(name = "first_stream_view")
# def first_stream_view():
#     df = spark.readStream.table("dlt_project.source.orders")
#     return df