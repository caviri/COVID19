import pandas as pd

def data_validation(df: pd.Dataframe) -> bool:

    if df.empty:
        print('\n* No data were downloaded \n*')
        return False
    
    if not pd.Series(df["date"]).is_unique:
        print('\n* Primary key check violated. Terminating extraction *\n')

    if df.isnull().values.any():
        raise Exception('\n* Null values found. Terminating extraction *\n')

    return True