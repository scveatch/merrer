"""PySpark Dataframe"""

from pyspark.sql import SparkSession
import os

spark = SparkSession.builder.appName("dataframe").getOrCreate()

some_data = [("John", 19), ("Smith", 23), ("Sarah", 18)]
dataframe = spark.createDataFrame(some_data, ["name", "age"])

dataframe.printSchema()

path = os.path.join(os.getenv("SPARK_HOME"), "examples/src/main/resources/people.json")
people_df = spark.read.json(path)

people_df.printSchema()

people_df.createOrReplaceTempView("people")

teenagers = spark.sql("SELECT name FROM people WHERE age >=13 AND age <= 19")

teenagers_df = teenagers.collect()

for row in teenagers_df:
    print(row)

spark.stop()