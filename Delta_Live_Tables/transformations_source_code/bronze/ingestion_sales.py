import dlt

# Sales Expectations
sales_rules = {
    "rule_1" : "sales_id is not null"
}

# Creating empty streaming table
dlt.create_streaming_table(
    name = "sales_stage",
    expect_all_or_drop = sales_rules
)

# Creating east sales flow
@dlt.append_flow(target = "sales_stage")
def east_sales():
    df = spark.readStream.table("dlt_project.source.sales_east")
    return df

# Creating west sales flow
@dlt.append_flow(target = "sales_stage")
def west_sales():
    df = spark.readStream.table("dlt_project.source.sales_west")
    return df


