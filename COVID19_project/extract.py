import requests
import pandas as pd

from pyspark.sql import SparkSession, DataFrame


def data_validation(df: DataFrame) -> bool:
    """Validate data extracted

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

def extract_data(spark: SparkSession) -> DataFrame:
    """Load data from Parquet file format.

    :param spark: Spark session object.
    :return: Spark DataFrame.
    """

    response = requests.get("https://api.covidtracking.com/v2/us/daily.json")

    if response.status_code != 200:
        raise Exception(f'\n* Request failed with status code {response.status_code} *\n')

    js = response.json()

    dates = []
    total_cases = []

    data = js['data']

    for item in data:
        dates.append(item['date']) 
        total_cases.append(item["cases"]["total"]["value"])


    # Improve this directly in spark.
    pdf = pd.DataFrame({"date": dates, "total_cases": total_cases}).dropna()
    
    assert data_validation(pdf), '\n* Data validation not achieved *\n'
    
    sdf = spark.createDataFrame(pdf)

    return sdf
