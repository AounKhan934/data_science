"""
Task 18: Handle Missing Embarked Values
"""

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
mode_embarked = df["Embarked"].mode()[0]
print(f"Most common embarkation port (mode): {mode_embarked}")

df["Embarked"] = df["Embarked"].fillna(mode_embarked)
print("Remaining missing values in Embarked:", df["Embarked"].isnull().sum())
