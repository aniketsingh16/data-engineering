import dlt
from pyspark.sql.functions import *
from pyspark.sql.types import *

@dlt.view(
    name = "products_enriched_view"
)
def products_enriched_view():
    df = spark.readStream.table("products_stage")
    df = df.withColumn("price", col("price").cast(IntegerType()))
    return df

dlt.create_streaming_table(
    name = "products_enriched"
)

dlt.create_auto_cdc_flow(
    target = "products_enriched",
    source = "products_enriched_view",
    keys = ["product_id"],
    sequence_by = "last_updated",
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