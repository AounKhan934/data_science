"""
Task 3: Display the First Few Rows
"""

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print("First 5 rows:")
print(df.head())

print("\nFirst 10 rows:")
print(df.head(10))
