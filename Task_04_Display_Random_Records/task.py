"""
Task 4: Display Random Records
"""

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print("10 Random Records:")
print(df.sample(10, random_state=42))
