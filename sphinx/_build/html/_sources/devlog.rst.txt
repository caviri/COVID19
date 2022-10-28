DevLog
======

Ideas
~~~~~

-  Integrate map with color per variable.
-  Integrate information of events related with measures. Introduce them
   in the timeline.
-  Accelerate the process
-  Transforms can include moving average as an example.

Dev log
~~~~~~~

23/10
^^^^^

Strategy A: Creating environment.

-  ``python==3.9.13``
-  PySpark uses java: ``conda install openjdk==17.0.3``
-  ``conda install pyspark==3.3.0``
-  ``conda install ipykernel``
-  ``python -m ipykernel install --user --name covid19``

On windows I have some issues starting the SparkSession. It last
forever.

Strategy B: Docker machine

-  ``docker pull jupyter/pyspark-notebook``
-  ``docker run -p 10000:8888 -p 4040:4040 jupyter/pyspark-notebook``

The docker image works fine, and we have access to the dashboard in
``localhost:4040``.

.. _section-1:

24/10
^^^^^

After checking the db structure, the project initially can be organized
as follows:

.. mermaid::

   diagramSequence;
       CT(Covid tracker JSON) --> PS(PySpark Loading)
       subgraph one[ETL]
       PS --> HV(HIVE DB)
       HV --> GP(Geoparquet)
       end
       GP --> BH(Bokeh App)

I found several boilerplates with good templates for data engineering
project using PySpark.

-  `PySpark Example
   Project <https://github.com/AlexIoannides/pyspark-example-project>`__
-  `PySpark Project
   Template <https://github.com/hbaflast/pyspark-project-template>`__
-  `PySpark Spotify
   ETL <https://github.com/Amaguk2023/Pyspark_Spotify_ETL>`__

Following the first example. This seems like a nice project structure to
start with:

.. code:: bash

   root/
    |-- configs/
    |   |-- etl_config.json
    |-- dependencies/
    |   |-- logging.py
    |   |-- spark.py
    |-- jobs/
    |   |-- etl_job.py
    |-- tests/
    |   |-- test_data/
    |   |-- | -- employees/
    |   |-- | -- employees_report/
    |   |-- test_etl_job.py
    |   build_dependencies.sh
    |   packages.zip
    |   Pipfile
    |   Pipfile.lock

I achieved to read without issues the scheme of the JSON for daily.json.
However, when I try to create a DataFrame out of the json obtained via
requests, the parsing of the schema is reduced to the first 2
categories. As a minimum viable proof, I decided to extract manually two
vairables ``total_cases`` and ``date`` in order to follow with the
structure of the project.

I’m exploring the idea of separate the project into 3 docker containers.
One dedicated to the ETL, another to HIVE database, and a third for the
interactive bokeh app. In the latter, I want to include 2 kind of
visualizations, one map based visualization, and another one for the
time series.

.. _section-2:

25/10
^^^^^

In order to simplify the development I took the decission to keep the 3
docker idea as a future update and create a simpler version of the
workflow. The output from the ETL pipeline will be saved in a parquet
(geoparquet) file and this will be picked up by bopkeh in order to do
the visualization.

Ideas for quality control

-  Missing values: interpolate values as approximation, or mean value.
   df.col_name.interpolate df.col_name.fillna
-  Missing values: Pyspark solution. pyspark.ml.feature import Imputer.
   https://www.youtube.com/watch?v=K46pPG8Cepo&ab_channel=WebAgeSolutionsInc
-  Data is in incosistent format
-  Duplicate records
-  Outliers
-  Not normalized input data

We can pass the SQL to the parquet.

.. code:: python

   parqDF.createOrReplaceTempView("ParquetTable")
   parkSQL = spark.sql("select * from ParquetTable where salary >= 4000 ")

.. _section-3:

26/10
^^^^^

After dealing with some problems realted to the date/datetime format I
got the first MVP of the pipeline. Now data is extracted, dates
transformed into a proper datetime type, and data loaded into a parquet
db. Bokeh app is able to read this data from the database and plot a
simple time-series plot in html. This is the first candidate to the
first release.

.. _section-4:

27/10
^^^^^

I included some exceptions for the API request. Now the database can be
overwritten without duplicates issues. And I added another
transformation: Rolling Mean. Now I will include some tests with a small
dataset of those transformations for the unittest.

Test working correctly for one transformation. Now tests needs to be
generated for every transformation.

Application running smoothly with ``python -m covid19_project`` but some
warnings appeared:

.. code:: python

   /usr/local/spark/python/pyspark/sql/pandas/conversion.py:474: FutureWarning: iteritems is deprecated and will be removed in a future version. Use .items instead.
     for column, series in pdf.iteritems():
   /usr/local/spark/python/pyspark/sql/pandas/conversion.py:486: FutureWarning: iteritems is deprecated and will be removed in a future version. Use .items instead.
     for column, series in pdf.iteritems():
   /usr/local/spark/python/pyspark/pandas/utils.py:975: PandasAPIOnSparkAdviceWarning: If `index_col` is not specified for `to_spark`, the existing index is lost when converting to Spark DataFrame.
     warnings.warn(message, PandasAPIOnSparkAdviceWarning)
   22/10/27 11:56:22 WARN WindowExec: No Partition Defined for Window operation! Moving all data to a single partition, this can cause serious performance degradation

In order to test: ``python -m unittest test/test_*.py``

Still some work is required when using spark-submit with
``$SPARK_HOME/bin/spark-submit --master local[*] --files configs/config.json covid19_project/__main__.py``

.. _section-5:

28/10
^^^^^

Applying some style corrections with flake8, and configuring correctly
the docker container for mybinder.
