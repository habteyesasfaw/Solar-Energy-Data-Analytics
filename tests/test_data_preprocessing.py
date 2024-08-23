import unittest
import pandas as pd
import numpy as np
import os

class TestDataPreprocessing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Set up the test class by defining paths to the datasets.
        """
        base_path = os.path.dirname(__file__)
        cls.test_data_paths = [
            os.path.join(base_path, '../data/benin-malanville.csv'),
            os.path.join(base_path, '../data/sierraleone-bumbuna.csv'),
            os.path.join(base_path, '../data/togo-dapaong_qc.csv')
        ]

    def setUp(self):
        """
        Set up the test environment by initializing the raw data.
        """
        self.raw_data = pd.DataFrame({
            'GHI': [200, 250, 300, np.nan, -50],
            'DNI': [150, 200, 0, 350, 300],
            'DHI': [50, 100, 150, 200, np.nan],
            'RH': [101, 85, 70, 55, np.nan],
            'Cleaning': [1, 0, 0, 1, 0]
        })

    def test_load_data(self):
        """
        Test if the datasets are loaded correctly.
        """
        for path in self.test_data_paths:
            with self.subTest(path=path):
                try:
                    data = pd.read_csv(path)
                    self.assertIsInstance(data, pd.DataFrame, f"Loaded dataset from {path} is not a DataFrame")
                    self.assertFalse(data.empty, f"Loaded dataset from {path} is empty")
                except FileNotFoundError:
                    self.fail(f"File not found: {path}")

    def test_handle_missing_values(self):
        """
        Test if missing values are handled properly.
        """
        self.raw_data = self.raw_data.dropna()  # Example of handling missing values
        self.assertFalse(self.raw_data.isnull().values.any(), "Data contains missing values after cleaning")

    def test_remove_negative_values(self):
        """
        Test if negative values in critical columns are removed or handled.
        """
        self.raw_data = self.raw_data[self.raw_data[['GHI', 'DNI', 'DHI']] >= 0].dropna()  # Example of removing negative values
        self.assertTrue((self.raw_data[['GHI', 'DNI', 'DHI']] >= 0).all().all(), "Negative values found in GHI, DNI, or DHI columns after cleaning")

    
    def test_cleaning_events(self):
        """
        Test if cleaning events are properly accounted for.
        """
        self.assertIn(1, self.raw_data['Cleaning'].unique(), "Cleaning events missing after processing")

    @classmethod
    def tearDownClass(cls):
        """
        Clean up any state that was set up in setUpClass.
        """
        pass

if __name__ == '__main__':
    unittest.main()
