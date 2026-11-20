import dlt

expectations_nocs = {
    "rule_1": "code is not null"
}
@dlt.view
def source_nocs():
    df = spark.readStream.table("olympics.silver.nocs")
    return df

@dlt.table
@dlt.expect_all(expectations_nocs)
def nocs():
    df = spark.readStream.table("LIVE.source_nocs")
    return df


