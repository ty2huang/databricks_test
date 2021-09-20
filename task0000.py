# Databricks notebook source
config_file = dbutils.widgets.get("config_file")

# COMMAND ----------

config = "0"
if config_file != "":
  with open(config_file, "r") as f:
    config = f.read()

# COMMAND ----------

dbutils.notebook.exit("Task 0000 completed with config value {}".format(config))

# COMMAND ----------

raise Exception("Notebook exit failed")
