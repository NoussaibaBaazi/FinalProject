import unittest
import pandas as pd

class TestLibraryImports(unittest.TestCase):

    def test_pandas_import(self):
        """Check if pandas is imported."""
        try:
            import pandas as pd
        except ImportError:
            self.fail("pandas is not imported correctly.")
    
    def test_matplotlib_import(self):
        """Check if matplotlib is imported."""
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            self.fail("matplotlib is not imported correctly.")


class TestCSVReading(unittest.TestCase):

    def test_csv_read_successfully(self):
        """Check if the CSV file can be read without errors."""
        file_path = 'QualificationsCSV.csv' 
        try:
            df = pd.read_csv(file_path)
            self.assertIsInstance(df, pd.DataFrame, "Data read is not a DataFrame.")
        except Exception as e:
            self.fail(f"Reading CSV failed with exception: {e}")

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


class TestCSVReadingWorkforce(unittest.TestCase):

    def test_csv_file_exists(self):
        """Check if the CSV file exists."""
        file_path = 'workforce-jobs-ons.csv' 
        self.assertTrue(os.path.exists(file_path), "CSV file does not exist.")
    
    def test_csv_read_successfully(self):
        """Check if the CSV file can be read without errors."""
        file_path = 'workforce-jobs-ons.csv' 
        try:
            df = pd.read_csv(file_path)
            self.assertIsInstance(df, pd.DataFrame, "Data read is not a DataFrame.")
        except Exception as e:
            self.fail(f"Reading CSV failed with exception: {e}")


class TestPercentRangesQualifications(unittest.TestCase):
    def test_column_value_range(self):
        """Ensuring the percent column only has perecentages not raw numbers"""
        file_path = 'QualificationsCSV.csv'
        df = pd.read_csv(file_path)
        percentage_columns = [
            '% with NVQ4+: percent',
            '% with NVQ3 only: percent',
            '% with NVQ2 only: percent',
            '% with NVQ1 only: percent',
            '% with Trade Apprenticeships: percent',
            '% with no qualifications: percent'
        ]
        for column in percentage_columns:
            with self.subTest(column=column):
                self.assertTrue(
                    df[column].between(0, 100).all(),
                    f"Column '{column}' contains out-of-range values."
                )


class TestDataFrameNumericColumns(unittest.TestCase):
    def setUp(self):
        self.data = pd.read_csv("workforce-jobs-ons.csv")

    def test_columns_are_numeric(self):
        columns_to_check = ['Male_UK','Female_UK','Male_London','Female_London']
        for column in columns_to_check:
            if column in self.data.columns:
                self.data[column] = self.data[column].str.replace(",", "").astype(float)
                
        self.data.to_csv("cleaned_workforce_jobs.csv", index=False)

        for column in columns_to_check:
            with self.subTest(column=column):
                is_numeric = pd.to_numeric(self.data[column], errors='coerce').notna().all()
                self.assertTrue(is_numeric, f"Column {column} contains non-numeric values.")

if __name__ == "__main__":
    unittest.main()
