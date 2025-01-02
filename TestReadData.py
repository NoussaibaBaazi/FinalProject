import unittest
import pandas as pd
import os
from Qualifications_graph import read_qualifications_data

class TestLibraryImports(unittest.TestCase):

    def test_pandas_import(self):
        """Check if pandas is imported."""
        try:
            import pandas as pd
        except ImportError:
            self.fail("pandas is not imported correctly.")
    
    def test_numpy_import(self):
        """Check if numpy is imported."""
        try:
            import numpy as np
        except ImportError:
            self.fail("numpy is not imported correctly.")
    
    def test_matplotlib_import(self):
        """Check if matplotlib is imported."""
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            self.fail("matplotlib is not imported correctly.")


class TestCSVReading(unittest.TestCase):

    def test_csv_file_exists(self):
        """Check if the CSV file exists."""
        file_path = 'QualificationsNVQ.csv' 
        self.assertTrue(os.path.exists(file_path), "CSV file does not exist.")
    
    def test_csv_read_successfully(self):
        """Check if the CSV file can be read without errors."""
        file_path = 'QualificationsNVQ.csv' 
        try:
            df = pd.read_csv(file_path)
            self.assertIsInstance(df, pd.DataFrame, "Data read is not a DataFrame.")
        except Exception as e:
            self.fail(f"Reading CSV failed with exception: {e}")

    def test_csv_columns_present(self):
        """Check if specific columns are present in the CSV file."""
        file_path = 'QualificationsNVQ.csv'  
        df = pd.read_csv(file_path)
        required_columns = ['Code','Area','Year','% with NVQ4+ - aged 16-64: percent','% with no qualifications - aged 16-64: percent','% with NVQ2 only - aged 16-64: percent','% with NVQ3 only - aged 16-64: percent']  # Update with your column names
        for col in required_columns:
            self.assertIn(col, df.columns, f"Column '{col}' is missing in the dataset.")

class TestCSVReadingUnemployment(unittest.TestCase):

    def test_csv_file_exists(self):
        """Check if the CSV file exists."""
        file_path = 'annual-unemployment-region.csv' 
        self.assertTrue(os.path.exists(file_path), "CSV file does not exist.")
    
    def test_csv_read_successfully(self):
        """Check if the CSV file can be read without errors."""
        file_path = 'annual-unemployment-region.csv' 
        try:
            df = pd.read_csv(file_path)
            self.assertIsInstance(df, pd.DataFrame, "Data read is not a DataFrame.")
        except Exception as e:
            self.fail(f"Reading CSV failed with exception: {e}")

    def test_csv_columns_present(self):
        """Check if specific columns are present in the CSV file."""
        file_path = 'annual-unemployment-region.csv'  
        df = pd.read_csv(file_path)
        required_columns = ['Year','Location','numerator','denominator','percent','conf','male numerator','male denominator',
                            'male percent','male conf','female numerator','female denominator','female percent','female conf']
        for col in required_columns:
            self.assertIn(col, df.columns, f"Column '{col}' is missing in the dataset.")

class TestPercentRangesQualifications(unittest.TestCase):
    def test_column_value_range(self):
        """Ensuring the percent column only has perecentages not raw numbers"""
        file_path = 'QualificationsNVQ.csv'
        df = pd.read_csv(file_path)
        percentage_columns = [
            '% with NVQ4+ - aged 16-64: percent',
            '% with NVQ2 only - aged 16-64: percent',
            '% with NVQ3 only - aged 16-64: percent',
            '% with no qualifications - aged 16-64: percent'
        ]
        for column in percentage_columns:
            with self.subTest(column=column):
                self.assertTrue(
                    df[column].between(0, 100).all(),
                    f"Column '{column}' contains out-of-range values."
                )