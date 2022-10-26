import datetime 

from pyspark.sql import DataFrame
from pyspark.sql.functions import udf, to_date
from pyspark.sql.types import TimestampType


def data_validation(df: DataFrame) -> bool:
    """Transform original dataset.

    :param df: Input DataFrame.
    :return: Validation output in boolean
    """

    if df.empty:
        print('\n* No data were downloaded \n*')
        return False
    
    if not pd.Series(df["date"]).is_unique:
        print('\n* Primary key check violated. Terminating extraction *\n')

    if df.isnull().values.any():
        raise Exception('\n* Null values found. Terminating extraction *\n')

    return True

def calc_moving_average(df: DataFrame, temporal_window:int) -> DataFrame:
    """Calcultation of moving average

    :param df: Input Spark DataFrame.
    :param temporal_window: The size of the window when calculating the moving average
    :return: Transformed DataFrame.
    """
    
    return df

def transform_date_to_datetime(date: datetime.date) -> datetime.datetime:
    """transform Date format to Datetime. 
    
    It calculates the minimum datetime possible and combine it with the date.

    :param date: Input date.
    :return: Combined date and minimum time output.
    """
    
    min_datetime = datetime.datetime.combine(date, datetime.time.min)
    
    return min_datetime



def transform_data(df: DataFrame) -> DataFrame:
    """Transform original dataset.

    :param df: Input Spark DataFrame.
    :return: Transformed Spark DataFrame.
    """
    
    df = df.withColumn("date", to_date("date", 'yyyy-MM-dd'))
    
    reg_transform_date_to_datetime = udf(lambda d: transform_date_to_datetime(d), TimestampType())
    df = df.withColumn("datetime", reg_transform_date_to_datetime("date"))
    
    return df
