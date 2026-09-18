"""
Task 23: Create Histograms for Numerical Features
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Titanic-Dataset.csv")
df["Age"] = df["Age"].fillna(df["Age"].median())

numeric_cols = ["Age", "Fare", "SibSp", "Parch"]
df[numeric_cols].hist(
    bins=30,
    figsize=(10, 6),
    layout=(2, 2),
    color="steelblue",
    edgecolor="black"
)
plt.tight_layout()
plt.savefig("histograms_numerical.png", dpi=300)
plt.show()
