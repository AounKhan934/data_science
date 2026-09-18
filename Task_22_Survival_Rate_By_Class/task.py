"""
Task 22: Compare Survival Rate by Passenger Class
"""

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
rates = df.groupby("Pclass")["Survived"].mean() * 100
print(rates.round(2))
