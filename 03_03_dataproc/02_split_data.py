from pyspark.sql import SparkSession
from pyspark.sql.functions import quarter
from pyspark.sql.functions import year, month
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("example").getOrCreate()

bucket_name = "de-gcp-example-bucket"
folder_name = "03_03_dataproc"
gcs_file_path = f"gs://{bucket_name}/{folder_name}/sales_data.csv"
output_path = f"gs://{bucket_name}/{folder_name}/output"

# Load data from GCS
df = spark.read.csv(gcs_file_path, header=True, inferSchema=True)

# adding new columns
df = df.withColumn("Quarter", quarter(col("OrderDate")))
df = df.withColumn("Year", year(col("OrderDate")))
df = df.withColumn("Month", month(col("OrderDate")))

# convert to pandas df
pandas_df = df.toPandas()
grouped_by_sales_channel = pandas_df.groupby("SalesChannel")
for sales_channel, group in grouped_by_sales_channel:
    group.to_csv(f"{output_path}/{sales_channel}_sales.csv", index=False)
