"""
Task 6: Find the Number of Rows and Columns
"""

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
rows, columns = df.shape
print(f"Number of rows = {rows}")
print(f"Number of columns = {columns}")
