# Databricks notebook source
# MAGIC %md
# MAGIC ### Delta Live Tables - Gold Layer

# COMMAND ----------

""" Delta Live Tables (DLT) is Databricks’ declarative framework for building data pipelines. You define what each table should contain, and Databricks handles orchestration, dependencies, retries, scaling and monitoring. As far as I know, Databricks has since renamed it Lakeflow Spark Declarative Pipelines. The docs and UI may use either name, but the concepts and the dlt Python module are the same.

The core idea

With normal PySpark, you write the read, transform and write steps yourself, then schedule them in the right order with a job. With DLT, you write each table as a function or SQL query, and DLT works out the dependency graph and runs it in the right order."""
# Materialized Views
# Streaming Views
# Streaming Tables

# COMMAND ----------

# MAGIC %md
# MAGIC ### Coaches DLT Pipeline

# COMMAND ----------

import dlt

# COMMAND ----------

@dlt.table

def source_table_coaches():
    df = spark.read.table("olympics.silver.coaches")

    return df
