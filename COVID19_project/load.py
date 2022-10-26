# LOAD DATA INTO GEOPARQUET DATABASE

from pyspark.sql import DataFrame

def load_data(df: DataFrame) -> None:
    """Collect data locally and write to a parquet file.

    :param df: DataFrame to store.
    :return: None
    """

    df.write.parquet("db.parquet") # Check if file already exist. 

    return None