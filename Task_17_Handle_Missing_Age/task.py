"""
Task 17: Handle Missing Age Values
"""

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
median_age = df["Age"].median()
print(f"Median Age: {median_age}")

df["Age"] = df["Age"].fillna(median_age)
print("Remaining missing values in Age:", df["Age"].isnull().sum())
