"""
test_data_generator.py
~~~~~~~~~~~~~~~
Module used to generate test dataset. 
"""

from pyspark.sql import SparkSession

from covid19_project.extract import extract_data
from covid19_project.transform import transform_col_string_to_date, transform_col_date_to_datetime, calc_daily_difference, calc_rolling_mean


def create_testdata(spark: SparkSession) -> None:
    """Method to generate and store in parquet format all the intermediate 
    files of each transformation.

    :param spark: Spark session object.
    :return: None.
    """
    data = extract_data(spark)

    df = data.limit(50)
    df.write.parquet("tests_data/test_input_data.parquet")

    df = transform_col_string_to_date(df, input_name="date", output_name="date")
    df.write.parquet("tests_data/test_to_date.parquet")

    df = transform_col_date_to_datetime(df, input_name="date", output_name="datetime")
    df.write.parquet("tests_data/test_transform_date_to_datetime.parquet")                                                         
                                                                
    df = df.sort("datetime")
    df.write.parquet("tests_data/test_sort.parquet")
                                                                
    df = calc_daily_difference(df, input_name="total_cases", output_name="difference_total_cases" )
    df.write.parquet("tests_data/test_calc_daily_difference.parquet")
                                                                
    df = calc_rolling_mean(df, 7, input_name="difference_total_cases", output_name="rolling_mean_total_cases")
    df.write.parquet("tests_data/test_calc_rolling_mean.parquet") 

    return None
