# LOAD DATA INTO GEOPARQUET DATABASE

import os
from pyspark.sql import SparkSession, DataFrame

def load_data(spark: SparkSession, df: DataFrame, db_file: str = "db.parquet"):
    """Collect data locally and write to a parquet file.

    :param df: DataFrame to store.
    :return: None
    """
    
    if os.path.exists(db_file):
        df_old = spark.read.parquet(db_file).cache()
        df_updated = df.union(df_old).dropDuplicates()#.cache()
        
        print(f"DB updated with {df_updated.count()} entries")
        
        df_updated.write.mode('overwrite').parquet(db_file)
    else:
        df.write.parquet(db_file)

    return None
