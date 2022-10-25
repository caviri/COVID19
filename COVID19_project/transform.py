from pyspark.sql import dataframe

def data_validation(df: dataframe.Dataframe) -> bool:
    """Transform original dataset.

    :param df: Input DataFrame.
    :param steps_per_floor_: The number of steps per-floor at 43 Tanner
        Street.
    :return: Transformed DataFrame.
    """
    

    if df.empty:
        print('\n* No data were downloaded \n*')
        return False
    
    if not pd.Series(df["date"]).is_unique:
        print('\n* Primary key check violated. Terminating extraction *\n')

    if df.isnull().values.any():
        raise Exception('\n* Null values found. Terminating extraction *\n')

    return True

def calc_moving_average(df: dataframe.DataFrame, temporal_window:int) -> dataframe.DataFrame:
    """Transform original dataset.

    :param df: Input DataFrame.
    :param steps_per_floor_: The number of steps per-floor at 43 Tanner
        Street.
    :return: Transformed DataFrame.
    """
    
    return None

def transform_data(df: dataframe.DataFrame, temporal_window: int) -> dataframe.DataFrame:
    """Transform original dataset.

    :param df: Input DataFrame.
    :param steps_per_floor_: The number of steps per-floor at 43 Tanner
        Street.
    :return: Transformed DataFrame.
    """

    return df