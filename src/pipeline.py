from pyspark.sql import SparkSession
from etl import extract
from utils import paths


def main():
    spark = (
        SparkSession.builder
           .appName("gastos_corporativos")
            .getOrCreate() 
    )

    path_clientes = paths.BRONZE_DIR / "clientes.csv"
    df_bronze_clientes = extract.extract_bronze(spark, path_arquivo=path_clientes)
    
    spark.stop()
if __name__ == "__main__":
    main()