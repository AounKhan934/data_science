"""
Task 13: Count Missing Values
"""

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print("Missing values per column:")
print(df.isnull().sum())
