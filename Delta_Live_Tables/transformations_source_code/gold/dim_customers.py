import dlt

#1: Create Empty Streaming Table
dlt.create_streaming_table(
    name = "dim_customers"
)

#2: Auto CDC flow
dlt.create_auto_cdc_flow(
    target = "dim_customers", # Empty Streaming Table we created in #1
    source = "customers_enriched_view",
    keys = ["customer_id"],
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
    stored_as_scd_type = 2, # optional
    track_history_column_list = None, # optional
    track_history_except_column_list = None, # optional
    name = None, # optional
    once = False # optional
)

