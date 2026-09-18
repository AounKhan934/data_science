"""
Task 10: Check the Values of the Target Variable
"""

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print("Unique values in 'Survived':", df["Survived"].unique())
