"""
test_transform.py
~~~~~~~~~~~~~~~
This module contains unit tests for the transformation steps of the ETL
job defined in etl_job.py. It makes use of a local version of PySpark
that is bundled with the PySpark package.
"""

import unittest
import json 

from dependencies.spark import start_spark

import covid19_project.transform as tf


class SparkTransformTests(unittest.TestCase):
    """Test suite for transformation in transform.py
    """

    def setUp(self):
        """Start Spark, define config and path to test data
        """
        self.config = json.loads("""{"temporal_window": 7}""")
        self.spark, *_ = start_spark()
        self.test_data_path = "tests/tests_data/"

    def tearDown(self):
        """Stop Spark
        """
        self.spark.stop()

    def test_transform_to_date(self):
        """Test method for string to date
        """
        # assemble
        input_data = (
            self.spark
            .read
            .parquet(self.test_data_path + "test_input_data.parquet"))

        expected_data = (
            self.spark
            .read
            .parquet(self.test_data_path + "test_to_date.parquet"))

        expected_data_cols = len(expected_data.columns)
        expected_data_rows = expected_data.count()

        # act
        data_transformed = tf.transform_col_date_to_datetime(input_data, input_name="date", output_name="date")

        cols = len(data_transformed.columns)
        rows = data_transformed.count()

        # assert
        self.assertEqual(expected_data_cols, cols)
        self.assertEqual(expected_data_rows, rows)

        self.assertTrue([col in expected_data.columns
                         for col in data_transformed.columns])

    def test_transform_to_datetime(self):
        """Test method to transform date to datetime.
        """
        # assemble
        input_data = (
            self.spark
            .read
            .parquet(self.test_data_path + "test_to_date.parquet"))

        expected_data = (
            self.spark
            .read
            .parquet(self.test_data_path + "test_date_to_datetime.parquet"))

        expected_data_cols = len(expected_data.columns)
        expected_data_rows = expected_data.count()

        # act
        data_transformed = tf.transform_col_string_to_date(input_data, input_name="date", output_name="datetime")

        cols = len(data_transformed.columns)
        rows = data_transformed.count()

        # assert
        self.assertEqual(expected_data_cols, cols)
        self.assertEqual(expected_data_rows, rows)

        self.assertTrue([col in expected_data.columns
                         for col in data_transformed.columns])

    def test_transform_to_sort(self):
        """Test pyspark sort method.
        """
        # assemble
        input_data = (
            self.spark
            .read
            .parquet(self.test_data_path + "test_date_to_datetime.parquet"))

        expected_data = (
            self.spark
            .read
            .parquet(self.test_data_path + "test_sort.parquet"))

        expected_data_cols = len(expected_data.columns)
        expected_data_rows = expected_data.count()

        # act
        data_transformed = input_data.sort("datetime")

        cols = len(data_transformed.columns)
        rows = data_transformed.count()

        # assert
        self.assertEqual(expected_data_cols, cols)
        self.assertEqual(expected_data_rows, rows)

        self.assertTrue([col in expected_data.columns
                         for col in data_transformed.columns])

    def test_calc_daily_difference(self):
        """Test method for calculating daily difference in a time series. 
        """
        # assemble
        input_data = (
            self.spark
            .read
            .parquet(self.test_data_path + "test_sort.parquet"))

        expected_data = (
            self.spark
            .read
            .parquet(self.test_data_path + "test_calc_daily_difference.parquet"))

        expected_data_cols = len(expected_data.columns)
        expected_data_rows = expected_data.count()

        # act
        data_transformed = tf.calc_daily_difference(input_data, input_name="total_cases" , output_name="difference_total_cases" )

        cols = len(data_transformed.columns)
        rows = data_transformed.count()

        # assert
        self.assertEqual(expected_data_cols, cols)
        self.assertEqual(expected_data_rows, rows)

        self.assertTrue([col in expected_data.columns
                         for col in data_transformed.columns])

    def test_calc_rolling_mean(self):
        """Test method for calculating a rolling mean. 
        """
        # assemble
        input_data = (
            self.spark
            .read
            .parquet(self.test_data_path + "test_calc_daily_difference.parquet"))

        expected_data = (
            self.spark
            .read
            .parquet(self.test_data_path + "test_calc_rolling_mean.parquet"))

        expected_data_cols = len(expected_data.columns)
        expected_data_rows = expected_data.count()

        # act
        data_transformed = tf.calc_rolling_mean(input_data, 7, input_name="difference_total_cases", output_name="rolling_mean_total_cases")

        cols = len(data_transformed.columns)
        rows = data_transformed.count()

        # assert
        self.assertEqual(expected_data_cols, cols)
        self.assertEqual(expected_data_rows, rows)

        self.assertTrue([col in expected_data.columns
                         for col in data_transformed.columns])


if __name__ == "__main__":
    unittest.main()
