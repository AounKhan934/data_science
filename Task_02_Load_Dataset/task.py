"""
Task 2: Load the CSV File
"""

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print("Dataset loaded successfully.")
print(f"Dimensions: {df.shape[0]} rows, {df.shape[1]} columns")
