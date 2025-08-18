# Develop a Python project using an object-oriented (OO) approach to convert large datasets into Parquet format. 
# Then, compute the maximum, minimum, average, and absolute values for each column in the dataset.

import pandas as pd
from ucimlrepo import fetch_ucirepo

class ParquetHandler:
    def __init__(self, dataset_id=296):
        self.dataset_id = dataset_id
        self.df = None

    def fetch_data(self):
        # Fetch dataset
        data = fetch_ucirepo(id=self.dataset_id)
        # Combine features and targets
        self.df = pd.concat([data.data.features, data.data.targets], axis=1)
        print(f"Dataset loaded with {self.df.shape[0]} rows and {self.df.shape[1]} columns.")

    def convert_to_parquet(self, filename="hospitaldata.parquet"):
        # Ensure DataFrame is loaded
        if self.df is None:
            raise ValueError("Dataset not loaded. Run fetch_data() first.")
        # Save as Parquet
        self.df.to_parquet(filename, engine='pyarrow', index=False)
        print(f"Data saved to {filename}")
        # Read back to verify
        df2 = pd.read_parquet(filename, engine='pyarrow')
        print(f"Parquet file loaded with {df2.shape[0]} rows and {df2.shape[1]} columns.")
        self.df = df2  # update df to Parquet version

    def column_max(self):
        return self.df.max(numeric_only=True)

    def column_min(self):
        return self.df.min(numeric_only=True)

    def column_average(self):
        return self.df.mean(numeric_only=True)

    def column_abs(self):
        numeric_df = self.df.select_dtypes(include='number')  # only numeric columns
        return numeric_df.abs()

if __name__ == "__main__":
    handler = ParquetHandler()
    handler.fetch_data()
    handler.convert_to_parquet()

    print("\nColumn-wise Maximum:\n", handler.column_max())
    print("\nColumn-wise Minimum:\n", handler.column_min())
    print("\nColumn-wise Average:\n", handler.column_average())
    print("\nColumn-wise Absolute Values (first 5 rows):\n", handler.column_abs().head())
