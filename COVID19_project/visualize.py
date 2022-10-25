"""
visualize.py
~~~~~~~~~~
This Python module contains the visualization code in order to create a Bokeh App

"""

from bokeh.plotting import figure, output_file, save
from pyspark.sql import dataframe

def bokeh_app(df: dataframe.Dataframe):
    x = df['total_cases']
    y = df['date']
    p = figure(title="COVID 19", x_axis_label='Date', y_axis_label='Total Cases')
    p.line(x, y, legend_label="Temp.", line_width=2)
    output_file("covid19.html")
    save(p)
