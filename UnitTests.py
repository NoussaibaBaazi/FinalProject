import unittest
import pandas as pd
import numpy as np

#Unit test class to check library imports
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

    def test_numpy_import(self):
        """Check if numpy is imported."""
        try:
            import numpy as np
        except ImportError:
            self.fail("numpy is not imported correctly.")


#Unit test class to validate reading of the Qualifications CSV file
class TestCSVQualifications(unittest.TestCase):

    def test_csv_read_successfully(self):
        """Check if the CSV file can be read without errors."""
        file_path = 'Data/QualificationsCSV.csv' 
        try:
            df = pd.read_csv(file_path)
            self.assertIsInstance(df, pd.DataFrame, "Data read is not a DataFrame.")
        except Exception as e:
            self.fail(f"Reading CSV failed with exception: {e}")

#Unit test class to validate reading the Workforce jobs CSV file
class TestCSVReadingWorkforce(unittest.TestCase):

    def test_csv_read_successfully(self):
        """Check if the CSV file can be read without errors."""
        file_path = 'Data/workforce-jobs-ons.csv' 
        try:
            df = pd.read_csv(file_path)
            self.assertIsInstance(df, pd.DataFrame, "Data read is not a DataFrame.")
        except Exception as e:
            self.fail(f"Reading CSV failed with exception: {e}")

#Unit test class to validate percentage ranges in Qualifications data
class TestPercentRangesQualifications(unittest.TestCase):
    def test_column_value_range(self):
        """Ensuring the percent column only has perecentages not raw numbers"""
        file_path = 'Data/QualificationsCSV.csv'
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

#Unit test class to validate numeric columns in the Workforce data
class TestDataFrameNumericColumns(unittest.TestCase):
    def setUp(self):
        self.data = pd.read_csv("Data/workforce-jobs-ons.csv")

    def test_columns_are_numeric(self):
        columns_to_check = ['Male_UK','Female_UK','Male_London','Female_London']
        for column in columns_to_check:
            if column in self.data.columns:
                self.data[column] = self.data[column].str.replace(",", "").astype(float)
                
        self.data.to_csv("Data/cleaned_workforce_jobs.csv", index=False)

        for column in columns_to_check:
            with self.subTest(column=column):
                is_numeric = pd.to_numeric(self.data[column], errors='coerce').notna().all()
                self.assertTrue(is_numeric, f"Column {column} contains non-numeric values.")

if __name__ == "__main__":
    unittest.main()

#Unit test class to analyse London employment data
class TestLondonEmploymentAnalysis(unittest.TestCase):

    def setUp(self):
        self.testing_csv = "Data/cleaned_workforce_jobs.csv"
        self.data = pd.read_csv(self.testing_csv)

    def test_percentage_change_calculation(self):
        data = self.data.copy()
        data.columns = ['Date', 'UK_Male', 'UK_Female', 'London_Male', 'London_Female']
        data['Date'] = pd.to_datetime(data['Date'], format='%b-%Y')
        data['Year'] = data['Date'].dt.year
    #Calculate percentage changes for male, female, and total employment
        yearly_data = data.groupby('Year')[['London_Male', 'London_Female']].mean().reset_index()
        yearly_data['London_Total'] = yearly_data['London_Male'] + yearly_data['London_Female']
        yearly_data['London_Male_Pct_Change'] = yearly_data['London_Male'].pct_change() * 100
        yearly_data['London_Female_Pct_Change'] = yearly_data['London_Female'].pct_change() * 100
        yearly_data['London_Total_Pct_Change'] = yearly_data['London_Total'].pct_change() * 100
    #Verify calculated columns exist
        self.assertTrue('London_Male_Pct_Change' in yearly_data.columns)
        self.assertTrue('London_Female_Pct_Change' in yearly_data.columns)
        self.assertTrue('London_Total_Pct_Change' in yearly_data.columns)

class TestLondonQualificationCorrelation(unittest.TestCase):

    def setUp(self):
        """Set up the London qualifications data for testing."""

        self.data = pd.read_csv("Data/QualificationsCSV.csv")

        #Filter for London data only
        self.data_london = self.data[self.data["Area"] == "London"]

        #Renaming columns for clarity
        self.columns_rename = {
            "% with NVQ4+: percent": "NVQ4+",
            "% with NVQ3 only: percent": "NVQ3 Only",
            "% with NVQ2 only: percent": "NVQ2 Only",
            "% with NVQ1 only: percent": "NVQ1 Only",
            "% with Trade Apprenticeships: percent": "Trade Apprenticeships percent",
            "% with no qualifications: percent": "No Qualifications"
        }

        self.data_all_qualifications = self.data_london.rename(columns=self.columns_rename)[
            ["Year"] + list(self.columns_rename.values())
        ]

        #Convert all relevant columns to numeric
        for col in self.columns_rename.values():
            self.data_all_qualifications[col] = pd.to_numeric(
                self.data_all_qualifications[col], errors='coerce'
            )

        #Ensure Year is treated as an integer
        self.data_all_qualifications["Year"] = self.data_all_qualifications["Year"].astype(int)

    def test_correlation_with_year(self):
        """Test for correlation between Year and each qualification level."""
        results = {}
        for qualification in self.columns_rename.values():
            #Drop NaN values for valid correlation computation
            valid_data = self.data_all_qualifications.dropna(subset=["Year", qualification])
            
            #Calculate correlation using numpy's corrcoef
            if not valid_data.empty:
                correlation_matrix = np.corrcoef(valid_data["Year"], valid_data[qualification])
                correlation = correlation_matrix[0, 1]  # Extract the correlation coefficient
            else:
                correlation = np.nan

            #Store results for reference
            results[qualification] = {
                "correlation": correlation
            }

            #Check if correlation is not NaN
            self.assertFalse(
                np.isnan(correlation),
                f"Correlation computation failed for {qualification} due to insufficient data."
            )

        print("Correlation results:")
        for qualification, stats in results.items():
            print(f"{qualification}: Correlation={stats['correlation']:.4f}")

if __name__ == "__main__":
    unittest.main()
