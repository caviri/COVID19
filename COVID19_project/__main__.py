"""
__main__.py
~~~~~~~~~~
This Python module contains an example Apache Spark ETL job definition
that implements best practices for production ETL jobs.
"""

#from dependencies.spark import start_spark
from pyspark.sql import SparkSession, DataFrame

from extract import extract_data
from transform import transform_data
from load import load_data
from visualize import read_data, bokeh_app

def main():
    """Main ETL script definition.

    :return: None
    """

    # start Spark application and get Spark session, logger and config
    #spark, log, config = start_spark(
    #    app_name='my_etl_job',
    #    files=['configs/config.json'])
    spark = SparkSession.builder.appName('COVID19').enableHiveSupport().getOrCreate()

    # log that main ETL job is starting
    #log.warn('etl_job is up-and-running')

    # execute ETL pipeline
    data = extract_data(spark)
    data_transformed = transform_data(data)
    load_data(data_transformed)

    # execute visualization pipeline
    data_loaded = read_data(spark) # Here we can specify the query
    bokeh_app(data_loaded) # Here we can specify the path

    # log the success and terminate Spark application
    #log.warn('test_etl_job is finished')
    spark.stop()

    return None


if __name__ == '__main__':
    # Check if the api is online and that the version is compatible. 
    main()
    