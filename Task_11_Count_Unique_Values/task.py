"""
Task 11: Count Unique Values in Every Column
"""

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print("Number of unique values per column:")
print(df.nunique())
