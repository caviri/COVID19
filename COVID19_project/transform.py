import datetime 

from pyspark.sql import DataFrame
from pyspark.sql.functions import udf, to_date
from pyspark.sql.types import TimestampType
import pyspark.pandas as ps


def calc_rolling_mean(df: DataFrame, temporal_window:int) -> DataFrame:
    """Calcultation of rolling mean

    :param df: Input Spark DataFrame.
    :param temporal_window: The size of the window when calculating the rolling mean
    :return: Transformed DataFrame.
    """
    psdf = df.pandas_api()
    roll_series = psdf["difference_total_cases"].rolling(temporal_window).mean()
    roll_series.name = "rolling_mean_total_cases"
    
    roll_psdf = ps.merge(psdf, roll_series, left_index=True, right_index=True, how="left")
    roll_df = roll_psdf.to_spark()
    
    return roll_df

def transform_date_to_datetime(date: datetime.date) -> datetime.datetime:
    """transform Date format to Datetime. 
    
    It calculates the minimum datetime possible and combine it with the date.

    :param date: Input date.
    :return: Combined date and minimum time output.
    """
    
    min_datetime = datetime.datetime.combine(date, datetime.time.min)
    
    return min_datetime

def calc_daily_difference(df: DataFrame) -> DataFrame:
    """Calcultation of daily difference

    :param df: Input Spark DataFrame.
    :return: Transformed DataFrame.
    """
    
    psdf = df.pandas_api()
    diff_series = psdf["total_cases"].diff()
    diff_series.name = "difference_total_cases"
    
    diff_psdf = ps.merge(psdf, diff_series, left_index=True, right_index=True, how="left")
    diff_df = diff_psdf.to_spark()

    return diff_df


def transform_data(df: DataFrame) -> DataFrame:
    """Transform original dataset.

    :param df: Input Spark DataFrame.
    :return: Transformed Spark DataFrame.
    """
    
    df = df.withColumn("date", to_date("date", 'yyyy-MM-dd'))
    
    reg_transform_date_to_datetime = udf(lambda d: transform_date_to_datetime(d), TimestampType())
    df = df.withColumn("datetime", reg_transform_date_to_datetime("date"))
    
    df = df.sort("datetime")
    df = calc_daily_difference(df)

    df = calc_rolling_mean(df, 7)
    
    return df
