"""
Task 16: Remove Duplicate Rows
"""

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
initial_count = len(df)
df = df.drop_duplicates().copy()
print(f"Initial rows: {initial_count}, Rows after drop_duplicates: {len(df)}")
