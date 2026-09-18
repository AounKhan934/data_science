"""
Task 24: Detect Possible Outliers Using Boxplots
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Titanic-Dataset.csv")
df["Age"] = df["Age"].fillna(df["Age"].median())
numeric_cols = ["Age", "Fare", "SibSp", "Parch"]

plt.figure(figsize=(8, 4))
sns.boxplot(data=df[numeric_cols], palette="Set2")
plt.title("Boxplots of Numerical Features")
plt.savefig("boxplots_numerical.png", dpi=300)
plt.show()
