import dlt
from pyspark.sql.functions import *

expectations_coaches = {
    "rule_1": "code is not null",
    "rule_2": "current is True"
}


@dlt.table(
    name = "source_coaches"
)
def source_table_coaches():
    df = spark.readStream.table("olympics.silver.coaches")
    return df

@dlt.view
def view_coaches():
    df = spark.readStream.table("LIVE.source_coaches")
    df = df.fillna("Unknown")
    return df

@dlt.table
@dlt.expect_all(expectations_coaches)
def coaches():
    df = spark.readStream.table("LIVE.view_coaches")
    return df