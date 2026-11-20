# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# Read Data
# df = spark.read.format("parquet").load(f"abfss://{source_container}@olympicsprojectsa.dfs.core.windows.net/{folder}")
df = spark.read.format("parquet").load(f"abfss://bronze@olympicsprojectsa.dfs.core.windows.net/athletes")

# COMMAND ----------

# T : Replace null with Unknown
df = df.fillna({"birth_place": "Unknown", "birth_country":"Unknown","residence_place":"Unknown","residence_country":"Unknown"})

# COMMAND ----------

# T: Filter on the basis of current and Name
df_filtered = df.filter((col("current") == True) & (col("name").isin("ALEKSANYAN Artur", "HARUTYUNYAN Arsen", "SEHEN Sajjad")) )


# COMMAND ----------

# DBTITLE 1,Cast height and weight
# T: Cast height & weight to float 
df_casted = df.withColumn('height', col('height').cast(FloatType()))\
    .withColumn('weight', col("weight").cast(FloatType()))

# COMMAND ----------

# T: Sort the dataframe base on height desc & weight asc

df_sorted = df_casted.sort('height', 'weight', ascending = [0,1]).filter(col('weight') > 0)

# COMMAND ----------

# T: Replace a string with another string

df_initials = df_sorted.withColumn('nationality', regexp_replace('nationality','United States','US'))

# COMMAND ----------

# T: Renaming a column
df_initials = df_initials.withColumnRenamed("code", "athelete_id")

# COMMAND ----------

df_initials = df_initials.withColumn("occupation", split("occupation", ','))

# COMMAND ----------

# T: check for duplication
df.groupBy('code').agg(count("code").alias("total_count")).filter(col("total_count") > 1)

# COMMAND ----------

df_final = df_initials.select('athelete_id',
 'current',
 'name',
 'name_short',
 'name_tv',
 'gender',
 'function',
 'country_code',
 'country',
 'country_long',
 'nationality',
 'nationality_long',
 'nationality_code',
 'height',
 'weight')

# COMMAND ----------

display(df_final)

# COMMAND ----------

# Creating a Temporary View based on Dataframe
df_final.createOrReplaceTempView("athletes")

# COMMAND ----------

sql_query = spark.sql("""
                      
    select * from athletes
    """
)


# COMMAND ----------

# Save the table
df_final.write.format("delta")\
    .mode("overwrite")\
    .option("path","abfss://silver@olympicsprojectsa.dfs.core.windows.net/athletes")\
    .saveAsTable("olympics.silver.athletes")