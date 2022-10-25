import json
import requests
from datetime import datetime
import pandas as pd

from pyspark.sql import SparkSession 

def extract_data(spark):
    """Load data from Parquet file format.

    :param spark: Spark session object.
    :return: Spark DataFrame.
    """

    response = requests.get("https://api.covidtracking.com/v2/us/daily.json")

    # TODO Check if 200 response

    js = response.json()

    date = []
    total_cases = []

    data = js['data']

    for item in data:
        dates.append(datetime.strptime(item['date'], "%Y-%m-%d"))
        total_cases.append(item["cases"]["total"]["value"])

    pdf = pd.DataFrame({"date": dates, "total_cases": total_cases})
    sdf = spark.createDataFrame(pdf)

    return sdf