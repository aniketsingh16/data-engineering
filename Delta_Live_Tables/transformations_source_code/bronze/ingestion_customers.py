import dlt

# Customers Expectations
customers_rules = {
    "rule_1" : "customer_id is not null",
    "rule_2" : "customer_name is not null"
}

#Ingesting Customers

@dlt.table(
    name = "customers_stage"
)
@dlt.expect_all_or_drop(customers_rules)
def customers_stage():
    df = spark.readStream.table("dlt_project.source.customers")
    return df