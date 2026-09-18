"""
Task 19: Verify Missing Values After Cleaning
"""

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

print("Missing values after cleaning:")
print(df.isnull().sum())
