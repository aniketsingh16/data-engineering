import dlt

expectations_events = {
    "rule_1": "event is not null"
}
@dlt.view
def source_events():
    df = spark.readStream.table("olympics.silver.events")
    return df

@dlt.table
@dlt.expect_all(expectations_events)
def events():
    df = spark.readStream.table("LIVE.source_events")
    return df