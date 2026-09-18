"""
Task 7: Check the Data Type of Every Column
"""

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print(df.dtypes)
