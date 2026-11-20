# Databricks notebook source
df = spark.read.format("csv")\
    .option("header", True)\
    .option("inferSchema",True)\
    .load("abfss://bronze@olympicsprojectsa.dfs.core.windows.net/nocs")

# COMMAND ----------

df.columns

# COMMAND ----------

# Dropping Irrelevant Column
df = df.drop("country",)

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

df = df.withColumn("tag", split(col("tag"), '-')[0])

# COMMAND ----------

display(df.limit(5))

# COMMAND ----------

# Saves only the data in the Datalake
df.write.format("delta")\
    .mode("overwrite")\
    .option("path", "abfss://silver@olympicsprojectsa.dfs.core.windows.net/nocs")\
    .save()

# COMMAND ----------

# Managed
df.write.format("delta")\
    .mode("overwrite")\
    .saveAsTable("olympics.silver.managed_nocs")

# COMMAND ----------

# External + Saves DDL & Metadata in Metastore
df.write.format("delta")\
    .mode("overwrite")\
    .option("path", "abfss://silver@olympicsprojectsa.dfs.core.windows.net/nocs")\
    .saveAsTable("olympics.silver.nocs")

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE STORAGE CREDENTIAL `ext-bronze_azuremanagedidentity_1793665115172`;

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW EXTERNAL LOCATIONS;