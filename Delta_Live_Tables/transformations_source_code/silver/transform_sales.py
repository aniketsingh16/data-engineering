import dlt
from pyspark.sql.functions import *

@dlt.view(
    name = "sales_enriched_view"
)
def sales_enriched_view():
    df = spark.readStream.table("sales_stage")
    df = df.withColumn("total_amount",col("quantity") * col("amount"))
    return df

dlt.create_streaming_table(
    name = "sales_enriched"
)

dlt.create_auto_cdc_flow(
    target = "sales_enriched",
    source = "sales_enriched_view",
    keys = ["sales_id"],
    sequence_by = "sale_timestamp",
    # system_sequence_by = None, # optional
    ignore_null_updates = False, # optional
    ignore_null_updates_column_list = None, # optional
    ignore_null_updates_except_column_list = None, # optional
    columns_to_update = None, # optional
    apply_as_deletes = None, # optional
    apply_as_truncates = None, # optional
    column_list = None, # optional
    except_column_list = None, # optional
    stored_as_scd_type = "1", # optional
    track_history_column_list = None, # optional
    track_history_except_column_list = None, # optional
    name = None, # optional
    once = False # optional
)