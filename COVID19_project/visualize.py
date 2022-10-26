"""
visualize.py
~~~~~~~~~~
This Python module contains the visualization code in order to create a Bokeh App

"""
from pyspark.sql import SparkSession, DataFrame
from bokeh.plotting import figure, output_file, save

def read_data(spark: SparkSession) -> DataFrame:
    """Read data from database

    :param spark: spark session
    :return: Spark DataFrame
    """
    #with spark_timezone("Europe/Berlin"):
    data_loaded = spark.read.parquet("db.parquet")
    data_loaded = data_loaded.sort("date", "total_cases")
    
    # Check  datetime format
    
    return data_loaded


def bokeh_app(df: DataFrame) -> None:
    """Bokeh Time-Series visualization

    :param df: Input Spark DataFrame
    :return: None
    """
    
    x = df.select("datetime").rdd.flatMap(lambda x: x).collect()
    y = df.select("total_cases").rdd.flatMap(lambda x: x).collect()
    
    p = figure(title="COVID 19", x_axis_label='Date', y_axis_label='Total Cases', x_axis_type='datetime')
    p.line(x, y, legend_label="Covid cases", line_width=2)
    output_file("covid19.html")
    save(p)
    
    return None