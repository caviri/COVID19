# LOAD DATA INTO GEOPARQUET DATABASE

from pyspark.sql import dataframe

def load_data(df: dataframe.DataFrame):
    """Collect data locally and write to a parquet file.

    :param df: DataFrame to store.
    :return: None
    """

    df.write.parquet("db.parquet")

    return None