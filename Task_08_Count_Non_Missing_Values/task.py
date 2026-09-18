"""
Task 8: Count Non-Missing Values
"""

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print("Non-missing values per column:")
print(df.notnull().sum())
