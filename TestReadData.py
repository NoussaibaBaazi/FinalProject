import unittest
import pandas as pd
import os
from newGraph import read_data

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
        file_path = 'QualificationsNVQ.csv'  # Update with your file path
        self.assertTrue(os.path.exists(file_path), "CSV file does not exist.")
    
    def test_csv_read_successfully(self):
        """Check if the CSV file can be read without errors."""
        file_path = 'QualificationsNVQ.csv'  # Update with your file path
        try:
            df = pd.read_csv(file_path)
            self.assertIsInstance(df, pd.DataFrame, "Data read is not a DataFrame.")
        except Exception as e:
            self.fail(f"Reading CSV failed with exception: {e}")

    def test_csv_columns_present(self):
        """Check if specific columns are present in the CSV file."""
        file_path = 'QualificationsNVQ.csv'  # Update with your file path
        df = pd.read_csv(file_path)
        required_columns = ['Code','Area','Year','% with NVQ4+ - aged 16-64: percent','% with no qualifications - aged 16-64: percent','% with NVQ2 only - aged 16-64: percent','% with NVQ3 only - aged 16-64: percent']  # Update with your column names
        for col in required_columns:
            self.assertIn(col, df.columns, f"Column '{col}' is missing in the dataset.")

