# CDC Pipeline

import dlt

@dlt.view
def source_athletes():
    df = spark.readStream.table("olympics.silver.athletes")
    return df

dlt.create_streaming_table(
    name = "athletes"
)

#2: Auto CDC flow
dlt.apply_changes(
    target = "athletes", # Empty Streaming Table we created in #1
    source = "source_athletes",
    keys = ["athelete_id"],
    sequence_by = "athelete_id",
    stored_as_scd_type = 1, # SCD or Upserted Table will be decide by 1(upsertedTable)/2(scd)
)