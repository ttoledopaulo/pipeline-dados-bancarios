from pyspark.sql import SparkSession

def extract_bronze(spark: SparkSession, path_arquivo: str):
    print(f"Lendo arquivo: {path_arquivo}")
    return (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(str(path_arquivo))
    )