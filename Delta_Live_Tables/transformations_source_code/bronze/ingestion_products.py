import dlt

# Products Expectations
products_rules = {
    "rule_1" : "product_id is not null",
    "rule_2" : "price >=0"
}

@dlt.table(
    name = "products_stage"
)
@dlt.expect_all_or_drop(products_rules)
def products_stage():
    df = spark.readStream.table("dlt_project.source.products")
    return df