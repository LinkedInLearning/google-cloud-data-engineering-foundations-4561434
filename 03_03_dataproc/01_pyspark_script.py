from pyspark.sql import SparkSession
from pyspark.sql.functions import quarter
from pyspark.sql.functions import year
from pyspark.sql.functions import col


bucket_name = "de-gcp-example-bucket"
folder_name = "03_03_dataproc"
gcs_file_path = f"gs://{bucket_name}/{folder_name}/sales_data.csv"


def write_to_gcs(df, file_path):
    df.coalesce(1).write.csv(file_path, header=True, mode="overwrite")

spark = SparkSession.builder.appName("example").getOrCreate()
df = spark.read.csv(gcs_file_path, header=True, inferSchema=True)
df.show()

# Find the total sales by each product
total_sales = df.groupBy("SalesChannel").sum("TotalRevenue")
write_to_gcs(total_sales, f"gs://{bucket_name}/{folder_name}/total_sales.csv")

# Find the total sales by each product category
total_sales_by_category = df.groupBy("OrderPriority").sum("TotalRevenue")
write_to_gcs(total_sales_by_category, f"gs://{bucket_name}/{folder_name}/total_sales_by_category.csv")

# Top region each quarter from OrderDate
df = df.withColumn("Quarter", quarter(col("OrderDate")))
df = df.withColumn("Year", year(col("OrderDate")))
top_region = (
    df.groupBy("Region", "Year", "Quarter")
    .sum("TotalRevenue")
    .orderBy("sum(TotalRevenue)", ascending=False)
    .limit(1)
)
write_to_gcs(top_region, f"gs://{bucket_name}/{folder_name}/top_region.csv")
