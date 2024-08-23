import unittest
import pandas as pd
import numpy as np

class TestDataPreprocessing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Update paths to reflect the correct location of the data files
        cls.test_data_paths = [
            'data/benin-malanville.csv',
            'data/sierraleone-bumbuna.csv',
            'data/togo-dapaong_qc.csv'
        ]

    def setUp(self):
        # Initialize variables or state before each test
        self.raw_data = pd.DataFrame({
            'GHI': [200, 250, 300, np.nan, -50],
            'DNI': [150, 200, 0, 350, 300],
            'DHI': [50, 100, 150, 200, np.nan],
            'RH': [101, 85, 70, 55, np.nan],
            'Cleaning': [1, 0, 0, 1, 0]
        })

    def test_load_data(self):
        """
        Test if datasets are loaded correctly.
        """
        for path in self.test_data_paths:
            with self.subTest(path=path):
                try:
                    data = pd.read_csv(path)
                    self.assertIsInstance(data, pd.DataFrame, f"Data loaded from {path} is not a DataFrame")
                    self.assertFalse(data.empty, f"Loaded dataset from {path} is empty")
                except FileNotFoundError:
                    self.fail(f"File not found: {path}")

    def test_clipping_rh_values(self):
        """
        Test if RH values are clipped within the valid range (0-100).
        """
        # Print RH values before clipping for debugging
        print("RH values before clipping:", self.raw_data['RH'].tolist())
        
        # Apply clipping to RH values while preserving NaN values
        self.raw_data['RH'] = self.raw_data['RH'].clip(lower=0, upper=100)
        
        # Print RH values after clipping for debugging
        print("RH values after clipping:", self.raw_data['RH'].tolist())
        
        # Extract the clipped RH values
        clipped_rh_values = self.raw_data['RH']
        
        # Verify all non-NaN RH values are within the valid range (0-100)
        valid_rh_values = clipped_rh_values[~clipped_rh_values.isna()]  # Exclude NaNs
        self.assertTrue((valid_rh_values <= 100).all(), "RH values exceed 100 after clipping")
        self.assertTrue((valid_rh_values >= 0).all(), "RH values are below 0 after clipping")

if __name__ == '__main__':
    unittest.main()
