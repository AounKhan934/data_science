"""
Task 28: Find the Five Highest-Paying Passengers
"""

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
topFares = df.sort_values(by="Fare", ascending=False)
top5 = topFares.head(5)
print(top5[["Name", "Sex", "Pclass", "Fare"]])
