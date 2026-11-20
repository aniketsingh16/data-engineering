# Databricks notebook source
files_array = [
    {
        "source_container": "bronze",
        "sink_container": "silver",
        "folder": "events"
    },
    {
        "source_container": "bronze",
        "sink_container": "silver",
        "folder": "coaches"
    }
]

# COMMAND ----------

dbutils.jobs.taskValues.set(key = "array_output", value = files_array )