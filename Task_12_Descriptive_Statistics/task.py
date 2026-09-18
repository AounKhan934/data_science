"""
Task 12: Generate Descriptive Statistics
"""

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print(df.describe())
