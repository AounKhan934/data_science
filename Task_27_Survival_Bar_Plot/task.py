"""
Task 27: Compare Survival by Sex Using a Bar Plot
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Titanic-Dataset.csv")

plt.figure(figsize=(6, 5))
sns.barplot(
    x="Sex",
    y="Survived",
    data=df,
    hue="Sex",
    legend=False,
    palette=["skyblue", "lightpink"]
)
plt.title("Sex vs Survival")
plt.xlabel("Sex")
plt.ylabel("Average Survival Rate")
plt.savefig("survival_by_sex.png", dpi=300)
plt.show()
