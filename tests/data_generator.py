"""
test_data_generator.py
~~~~~~~~~~~~~~~
Module used to generate test dataset. 
"""

from pyspark.sql import SparkSession

from covid19_project.extract import extract_data
from covid19_project.transform import transform_date_to_datetime, calc_daily_difference, calc_rolling_mean

from pyspark.sql.functions import udf, to_date
from pyspark.sql.types import TimestampType


def create_testdata(spark: SparkSession) -> None:
    """Method to generate and store in parquet format all the intermediate files of each transformation.

    :param spark: Spark session object.
    :return: None.
    """
    data = extract_data(spark)

    df = data.limit(50)
    df.write.parquet("tests_data/test_input_data.parquet")

    df = df.withColumn("date", to_date("date", 'yyyy-MM-dd'))
    df.write.parquet("tests_data/test_to_date.parquet")

    reg_transform_date_to_datetime = udf(lambda d: transform_date_to_datetime(d), TimestampType())
    df = df.withColumn("datetime", reg_transform_date_to_datetime("date"))
    df.write.parquet("tests_data/test_transform_date_to_datetime.parquet")                                                         
                                                                
    df = df.sort("datetime")
    df.write.parquet("tests_data/test_sort.parquet")
                                                                
    df = calc_daily_difference(df)
    df.write.parquet("tests_data/test_calc_daily_difference.parquet")
                                                                
    df = calc_rolling_mean(df, 7)
    df.write.parquet("tests_data/test_calc_rolling_mean.parquet") 

    return None