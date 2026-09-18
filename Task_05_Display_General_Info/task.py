"""
Task 5: Display General Dataset Information
"""

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
df.info()
