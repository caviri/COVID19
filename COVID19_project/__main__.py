"""
__main__.py
~~~~~~~~~~
This Python module contains an example Apache Spark ETL job for producing a COVID19 related visualization. 
"""

from .extract import extract_data
from .transform import transform_data
from .load import load_data
from .visualize import read_data, bokeh_app

from dependencies.spark import start_spark

def main():
    """Main ETL script definition.

    :return: None
    """

    # start Spark application and get Spark session, logger and config
    spark, log, config = start_spark(
       app_name='covid19',
       files=['configs/config.json'])

    # log that main ETL job is starting
    log.warn('covid19 job is up-and-running')

    # execute ETL pipeline
    data = extract_data(spark)
    data_transformed = transform_data(data)
    load_data(spark, data_transformed)

    # execute visualization pipeline
    data_loaded = read_data(spark) # Here we can specify the query
    bokeh_app(data_loaded) # Here we can specify the path

    # log the success and terminate Spark application
    log.warn('covid19 job is finished')
    spark.stop()

    return None


if __name__ == '__main__':
    # Check if the api is online and that the version is compatible. 
    main()
    