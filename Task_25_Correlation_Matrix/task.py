"""
Task 25: Create a Correlation Matrix
"""

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
selected_cols = ["Age", "SibSp", "Parch", "Pclass", "Fare"]
print(df[selected_cols].corr().round(2))
