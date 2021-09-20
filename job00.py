# Databricks notebook source
# COMMAND ----------
# Create widgets
dbutils.widgets.text("config_file", "/dbfs/user/thuang/mock_config_file.txt")
dbutils.widgets.text("start_task", "task0000")
dbutils.widgets.text("end_task", "task0002")

# COMMAND ----------

start_task = dbutils.widgets.get("start_task")

# COMMAND ----------

end_task = dbutils.widgets.get("end_task")

# COMMAND ----------

config_file = dbutils.widgets.get("config_file")

# COMMAND ----------

tasks = ['task0000', 'task0001', 'task0002']
activated = 0
for task in tasks:
  if task == start_task: activated = 1
  if activated == 1: print(dbutils.notebook.run(task, 60, {"config_file": config_file}))
  if task == end_task: activated = 0
