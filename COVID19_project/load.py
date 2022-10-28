"""
load.py
~~~~~~~
This Python module contains methods to load transformed data into a database.

"""

import os
from pyspark.sql import SparkSession, DataFrame


def load_data(spark: SparkSession, df: DataFrame, db_file: str = "db.parquet"):
    """Collect data locally and write to a parquet file.

    :param spark: Spark session used. 
    :param df: DataFrame to store.
    :param db_file: Database filename.
    :return: None
    """

    # First let's check if output folder is created
    if not os.path.exists("output"):
        os.mkdir("output")
    
    # If there's a previous version of the db, we need to update it aqnd get
    # rid of duplicates. This makes this loading process idempotem. The database 
    # will remain similar independently of how many times this process is run. 
    # This helps to nmake this ETL process async from others. 
    if os.path.exists(f"output/{db_file}"):
        df_old = spark.read.parquet(f"output/{db_file}").cache()
        df_updated = df.union(df_old).dropDuplicates()
        
        print(f"DB updated with {df_updated.count()} entries")
        
        df_updated.write.mode('overwrite').parquet(f"output/{db_file}")
    else:
        df.write.parquet(f"output/{db_file}")

    return None
