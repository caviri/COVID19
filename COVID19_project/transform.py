import datetime 

from pyspark.sql import DataFrame
from pyspark.sql.functions import udf, to_date
from pyspark.sql.types import TimestampType
import pyspark.pandas as ps


def transform_item_date_to_datetime(date: datetime.date) -> datetime.datetime:
    """transform Date format to Datetime. 
    
    It calculates the minimum datetime possible and combine it with the date.

    :param date: Input date.
    :return: Combined date and minimum time output.
    """
    
    min_datetime = datetime.datetime.combine(date, datetime.time.min)
    
    return min_datetime

def transform_col_date_to_datetime(df: DataFrame, input_name: str, output_name: str) -> DataFrame:
    """Transform column date into to column in datetime type.

    :param df: Input Spark DataFrame.
    :param input_name: Name of the column to update.
    :param output_name: Name of the column where to store the result. If input_name is equal to output name, the column will be overwritten.
    :return: Transformed Spark DataFrame.
    """
    
    reg_transform_date_to_datetime = udf(lambda d: transform_item_date_to_datetime(d), TimestampType())
    df = df.withColumn(output_name, reg_transform_date_to_datetime(input_name))
    
    return df

def transform_col_string_to_date(df: DataFrame, input_name: str, output_name: str) -> DataFrame:
    """Transform column date in string to column date in date type.
    
    :param df: Input Spark DataFrame.
    :param input_name: Name of the column to update.
    :param output_name: Name of the column where to store the result. If input_name is equal to output name, the column will be overwritten.
    :return: Transformed Spark DataFrame.
    """
    
    df = df.withColumn(output_name, to_date(input_name, 'yyyy-MM-dd'))
        
    return df


def calc_daily_difference(df: DataFrame, input_name: str , output_name: str) -> DataFrame:
    """Calcultation of daily difference

    :param df: Input Spark DataFrame.
    :param input_name: Name of the column to process.
    :param output_name: Name of the column where to store the result. If input_name is equal to output name, the column will be overwritten.

    :return: Transformed DataFrame.
    """
    
    psdf = df.pandas_api()
    diff_series = psdf[input_name].diff()
    diff_series.name = output_name
    
    diff_psdf = ps.merge(psdf, diff_series, left_index=True, right_index=True, how="left")
    diff_df = diff_psdf.to_spark()

    return diff_df

def calc_rolling_mean(df: DataFrame, temporal_window:int, input_name: str, output_name: str) -> DataFrame:
    """Calcultation of rolling mean

    :param df: Input Spark DataFrame.
    :param temporal_window: The size of the window when calculating the rolling mean.
    :param input_name: Name of the column to process.
    :param output_name: Name of the column where to store the result. If input_name is equal to output name, the column will be overwritten.
    :return: Transformed DataFrame.
    """
    psdf = df.pandas_api()
    roll_series = psdf[input_name].rolling(temporal_window).mean()
    roll_series.name = output_name
    
    roll_psdf = ps.merge(psdf, roll_series, left_index=True, right_index=True, how="left")
    roll_df = roll_psdf.to_spark()
    
    return roll_df


def transform_data(df: DataFrame) -> DataFrame:
    """Transform original dataset.

    :param df: Input Spark DataFrame.
    :return: Transformed Spark DataFrame.
    """
    
    df = transform_col_string_to_date(df, input_name="date", output_name="date")

    df = transform_col_date_to_datetime(df, input_name="date", output_name="datetime")
    
    df = df.sort("datetime")
    
    df = calc_daily_difference(df, input_name="total_cases" , output_name="difference_total_cases" )
    
    df = calc_rolling_mean(df, 7, input_name="difference_total_cases", output_name="rolling_mean_total_cases")
    
    return df
