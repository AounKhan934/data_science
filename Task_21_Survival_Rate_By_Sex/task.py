"""
Task 21: Compare Survival Rate by Sex
"""

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
rates = df.groupby("Sex")["Survived"].mean() * 100
print(rates.round(2))
