"""
Task 9: Check Duplicate Rows
"""

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
duplicate_count = df.duplicated().sum()
print("Duplicate Rows:", duplicate_count)
