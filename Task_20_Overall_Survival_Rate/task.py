"""
Task 20: Calculate the Overall Survival Rate
"""

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
survival_rate = df["Survived"].mean() * 100
print(f"Overall Survival Rate: {survival_rate:.2f}%")
