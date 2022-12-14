"""
visualize.py
~~~~~~~~~~~~
This Python module contains the visualization code in order to create a Bokeh App

"""
from pyspark.sql import SparkSession, DataFrame
from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource

def read_data(spark: SparkSession, db_file: str = "db.parquet") -> DataFrame:
    """Read data from database

    :param spark: spark session
    :param db_file: database file in output folder
    :return: Spark DataFrame
    """

    data_loaded = spark.read.parquet(f"output/{db_file}")
    data_loaded = data_loaded.sort("date").dropna()
    
    # Check  datetime format
    
    return data_loaded


def bokeh_app(df: DataFrame, html_file: str = "covid19.html") -> None:
    """Bokeh Time-Series visualization

    :param df: Input Spark DataFrame
    :param html_file: name of the file output
    :return: None
    """
    
    x = df.select("datetime").rdd.flatMap(lambda x: x).collect()
    y_diff = df.select("difference_total_cases").rdd.flatMap(lambda x: x).collect()
    y_roll = df.select("rolling_mean_total_cases").rdd.flatMap(lambda x: x).collect()
    
    source = ColumnDataSource(data={"date": x, "difference_total_cases": y_diff, "rolling_mean_total_cases": y_roll})

    p = figure(title="COVID 19", x_axis_label="Date", y_axis_label="Cases", x_axis_type="datetime", plot_width=800)
    p.line("date", "difference_total_cases", legend_label="Daily Difference", line_width=2, line_color="blue", source=source)
    p.line("date", "rolling_mean_total_cases", legend_label="Rolling Mean", line_width=2, line_color="red", source=source)
    
    output_file(f"output/{html_file}")
    save(p)
    
    return None